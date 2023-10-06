import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(database="beauty_saloon",
                            user="postgres",
                            password="plombier520796",
                            host="localhost",
                            port="5432")

    cursor = conn.cursor()


    def func_postgresql(func):
        cursor.execute(func)
        conn.commit()


    def finish(lol):
        try:
            cursor.execute(lol)
            r = list(cursor.fetchall())
            for x in r:
                print(x)
        except (Exception, Error) as error:
            print('Ошибка в подключении PostgreSQL :', error)

        finally:
            if conn:
                conn.close()
                cursor.close()
                print('Соединение с PostgreSQL закрыто')


    random_fn_postres = """
    CREATE OR REPLACE FUNCTION max_pay(i int)
    RETURNS int
    AS $$
    DECLARE maxpay int;
     BEGIN
     	SELECT MAX(s.pay_₽)
    	INTO maxpay
    	FROM staff s;
    	RETURN maxpay;
     END;
    $$
    LANGUAGE 'plpgsql';
    """
    func_postgresql(random_fn_postres)

    d = """
    SELECT fl_name, age, post, aver_price_₽, pay_₽
    FROM staff s, services d 
    where s.pay_₽ = max_pay(1)
    and s.fk_services_id = d.services_id
    """
    finish(d)
except:
    print('Ошибка в подключении PostgreSQl\n*проверьте введеные данные')
