from extraction_pack.reader.CsvReader import CsvReader
from data_base.connection import connection
from data_base.DataBaseHandler import DataBaseHandler


def map_reducer_education_level(student: dict):
    student_clean = {
        'ESCOLARIDADE_COD': student['TP_ETAPA_ENSINO'] or '""',
        'MUNICIPIO_COD': student['CO_MUNICIPIO'] or '""',
        'UF_COD': student['CO_UF'] or '""',
        'SEXO_COD': student['TP_SEXO'] or '""',
        'IDADE_COD': student['NU_IDADE'] or '""',
        'COR_RACA_COD': student['TP_COR_RACA'] or '""',
    }

    with connection() as connect:
        with connect.cursor() as cursor:
            insert = DataBaseHandler.insert_into('top_10', student_clean)
            cursor.execute(insert)


keys = [
    (key, 'varchar(255)') for key in
            [
                'ESCOLARIDADE_COD',
                'MUNICIPIO_COD',
                'UF_COD',
                'SEXO_COD',
                'IDADE_COD',
                'COR_RACA_COD'
            ]
        ]

with connection() as connect:
    with connect.cursor() as cursor:
        cursor.execute(DataBaseHandler.drop_table('top_10'))
        cursor.execute(DataBaseHandler.create_table('top_10', keys))


CsvReader.read_line_by_line('../data/matricula_co.CSV', map_reducer_education_level)






