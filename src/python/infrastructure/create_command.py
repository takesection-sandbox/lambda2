import psycopg2
import os

def _connect():
    db_endpoint = os.environ['DB_ENDPOINT']
    db_port = 5432
    db_name = 'test'
    db_user = 'test'
    db_password = 'test1234'
    dsn = 'postgresql://%s:%s/%s' % (db_endpoint, db_port, db_name)
    return psycopg2.connect(dsn, user = db_user, password = db_password)

def create(id, name):
    with _connect() as conn:
        with conn.cursor() as cur:
            sql = '''INSERT INTO sample_users (
                id,
                name
                ) VALUES (
                %s,
                %s
                );'''
            cur.execute(sql, (id, name))
            rowcount = cur.rowcount
        conn.commit()
        print(rowcount)
