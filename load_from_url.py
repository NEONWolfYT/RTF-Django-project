import sys
import sqlite3
import pandas as pd
import requests
from io import StringIO

def fetch_csv(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return pd.read_csv(StringIO(r.text))

def generate_html(df):
    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce", utc=True)
    df = df[df["published_at"].notna()]
    df["year"] = df["published_at"].dt.year
    df["name_lower"] = df["name"].astype(str).str.lower()
    df["is_python"] = df["name_lower"].apply(lambda x: any(k in x for k in ["python", "питон", "пайтон"]))
    df["salary_from"] = pd.to_numeric(df["salary_from"], errors="coerce")
    df["salary_to"] = pd.to_numeric(df["salary_to"], errors="coerce")
    df["avg_salary"] = df[["salary_from", "salary_to"]].mean(axis=1)
    df = df[df["avg_salary"] < 10_000_000]

    html = {}

    html["Общая статистика"] = (
        df.groupby("year")["avg_salary"].mean().round().reset_index(name="Средняя зарплата").to_html(index=False)
        + "<br><br>" +
        df["year"].value_counts().sort_index().reset_index()
          .rename(columns={"index": "Год", "year": "Количество вакансий"}).to_html(index=False)
    )

    df_py = df[df["is_python"]]
    html["Востребованность"] = (
        df_py.groupby("year")["avg_salary"].mean().round().reset_index(name="Средняя зарплата").to_html(index=False)
        + "<br><br>" +
        df_py["year"].value_counts().sort_index().reset_index()
              .rename(columns={"index": "Год", "year": "Количество вакансий"}).to_html(index=False)
    )

    top_cities = df["area_name"].value_counts(normalize=True)
    top_cities = top_cities[top_cities > 0.01].index

    city_salary = df[df["area_name"].isin(top_cities)].groupby("area_name")["avg_salary"].mean().round()
    city_share = df["area_name"].value_counts(normalize=True)[top_cities].mul(100).round(2).astype(str) + "%"

    html["География"] = (
        city_salary.reset_index(name="Средняя зарплата").rename(columns={"area_name": "Город"}).to_html(index=False)
        + "<br><br>" +
        city_share.reset_index().rename(columns={"index": "Город", "area_name": "Доля"}).to_html(index=False)
    )

    return html

def save_to_sqlite(html_by_section):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("DELETE FROM analytics_section")
    cur.execute("INSERT INTO analytics_section (title, html_content, image) VALUES (?, ?, ?)",
                ("Главная", "<p>Данные обновлены автоматически с CSV.</p>", None))
    for title, html in html_by_section.items():
        cur.execute("INSERT INTO analytics_section (title, html_content, image) VALUES (?, ?, ?)",
                    (title, html, None))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❗ Использование: python load_from_url.py <прямая_ссылка_на_csv>")
        sys.exit(1)
    url = sys.argv[1]
    print("📥 Загружаю CSV с:", url)
    try:
        df = fetch_csv(url)
        html = generate_html(df)
        save_to_sqlite(html)
        print("✅ Данные обновлены и сохранены в базу.")
    except Exception as e:
        print("❌ Ошибка:", e)