
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "analytics_section" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(200) NOT NULL,
    "html_content" text NOT NULL,
    "image" varchar(100) NULL
);
INSERT INTO "analytics_section" ("id", "title", "html_content", "image") VALUES
(1, "Главная", "<p>Профессия Python-программиста — одна из самых востребованных в IT. Python применяется в веб-разработке, анализе данных, машинном обучении, DevOps, автоматизации и других сферах. Удобный синтаксис и мощные библиотеки делают его идеальным языком как для новичков, так и для профессионалов.</p>", NULL),
(2, "Общая статистика", "<h3>Динамика средней зарплаты по годам:</h3><ul><li>2011 — 45 682 ₽</li><li>2012 — 60 077 ₽</li><li>2013 — 54 651 ₽</li><li>2022 — 133 712 ₽</li><li>2024 — 174 533 ₽</li></ul>", "images/salary_by_year_python.png");
COMMIT;
