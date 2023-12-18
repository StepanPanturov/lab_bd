# Лабораторная работа
В результате лабораторной работы я сравнил три библиотеки (psycopg2, SQLite, DuckDB) для работы с базами данных, используя tiny датасет
# SQL запросы 
1. SELECT VendorID, count(*) FROM trips GROUP BY 1;
2. SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;
3. SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;
4. SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;
# График
График сравнения времени выполнения четырех запросов в секундах для разных библиотек на tiny датасете:

<img width="510" alt="image" src="https://github.com/StepanPanturov/lab_bd/assets/149319607/8de86fc8-f565-4897-82f4-f7608e30e2c1">


# Выводы и анализ графика
Исходя из графика, DuckDB явлется самым быстрым способом работы с базой данных. Это происходит потому, что она выполняет запросы путём векторизации, ориентированной на столбцы, в то время как SQLite, PostgreSQL  обрабатывают каждую строку последовательно. Также DuckDB имеет сравнительно простой синтаксис. Самой медленной библиотекой является SQLite, но она удобна в использовании. psycopg2 - среднее решение между упомянутыми библиотеками.
