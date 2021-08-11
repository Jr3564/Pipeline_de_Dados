from data_base.connection import connection
from data_base.DataBaseHandler import DataBaseHandler
from extraction_pack.reader.XslxReader import XslxReader

municipios_ufs = XslxReader.read_page_xlsx("../data/Tabelas Auxiliares.xlsx", "Anexo10 - UFS e Municípios")

table = []
for row in municipios_ufs:
    colm = [item.value for item in row][:-1]
    table.append(colm)

table = table[5:-2]

header = table[0]

matrix: list[dict] = list()
for row in table[1:]:
    colmn = dict()
    for index, item in enumerate(row):
        colmn[header[index]]= f'"{item}"'
    matrix.append(colmn)


with connection() as connect:
    with connect.cursor() as cursor:
        for item in matrix:
            insert = DataBaseHandler.insert_into('municipios_ufs_tabela_auxiliar', item)
            cursor.execute(insert)