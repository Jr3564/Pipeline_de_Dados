from contextlib import contextmanager
import pymysql.cursors


@contextmanager
def connection():
    connection_instance = pymysql.connect(
        host="localhost",
        user='root',
        port=3306,
        db="school_census",
        password="sua_senha_aqui",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield connection_instance
    finally:
        connection_instance.commit()
        connection_instance.close()
