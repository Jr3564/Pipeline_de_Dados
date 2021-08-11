class DataBaseHandler:
    @staticmethod
    def create_database(name: str) -> str:
        create = f'CREATE DATABASE IF NOT EXISTS {name}'
        print(create)
        return create

    @staticmethod
    def drop_table(name: str) -> str:
        drop = f'DROP TABLE IF EXISTS {name}'
        print(drop)
        return drop

    @staticmethod
    def create_table(name: str, keys: list[tuple[str, str]]) -> str:
        spread_keys = ','.join([f'{key} {typing}' for key, typing in keys])
        create = f'CREATE TABLE {name}({spread_keys});'
        print(create)
        return create

    @staticmethod
    def insert_into(table_name: str, key_value: dict):
        keys = ','.join([str(key) for key in key_value.keys()])
        values = ','.join([str(value) for value in key_value.values()])
        insert = f'INSERT INTO {table_name}({keys}) VALUES ({values})'
        print(insert)
        return insert
