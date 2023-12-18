import psycopg2, time
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect(user="postgres",
                            password="123456",
                            host="localhost",
                            port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()
    sql_create_database = 'create database postgres_db'
    cursor.execute(sql_create_database)
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    for i in range(10):
        t0 = time.perf_counter()
        cursor.execute('SELECT "VendorID", count(*) FROM public.trips group by 1;')
        res1 = cursor.fetchall()
        t1 = time.perf_counter()
        sum1 += (t1 - t0)
        t0 = time.perf_counter()
        cursor.execute('SELECT "passenger_count", avg(total_amount) FROM public.trips GROUP BY 1;')
        res2 = cursor.fetchall()
        t1 = time.perf_counter()
        sum2 += (t1 - t0)
        t0 = time.perf_counter()
        cursor.execute('SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM public.trips GROUP BY 1, 2;')
        res3 = cursor.fetchall()
        t1 = time.perf_counter()
        sum3 += (t1 - t0)
        t0 = time.perf_counter()
        cursor.execute('SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM public.trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;')
        res4 = cursor.fetchall()
        t1 = time.perf_counter()
        sum4 += (t1 - t0)
        if i == 9:
            print("Query 1")
            print("Result: ", res1)
            print("Average time: ", sum1 / 10)
            print()
            print("Query 2")
            print("Result: ", res2)
            print("Elapsed time: ", sum2 / 10)
            print()
            print("Query 3")
            print("Result: ", res3)
            print("Elapsed time: ", sum3 / 10)
            print()
            print("Query 4")
            print("Result: ", res4)
            print("Elapsed time: ", sum4 / 10)
            print()

except (Exception, Error) as error:
    print("error con to bd:", error)
finally:
    if conn:
        cursor.close()
        conn.close()
