from data_base.connection import connection
from data_base.DataBaseHandler import DataBaseHandler
from extraction_pack.reader.XslxReader import XslxReader

etapas_de_ensino = XslxReader.read_page_xlsx("../data/Tabelas Auxiliares.xlsx", "Anexo7 - Tabelas Etapas")

cod_and_name: list[tuple] = list()
for row in etapas_de_ensino:
    if row[1].value:
        cod_and_name.append(tuple([item.value for item in row][:2]))

items: list[dict] = list()
header = ['TP_ETAPA_ENSINO', 'NAME_ETAPA_ENSINO']
for item in cod_and_name[1:]:
    items.append({header[0]: item[0], header[1]: f'"{item[1]}"'})

with connection() as connect:
    with connect.cursor() as cursor:
        for item in items:
            insert = DataBaseHandler.insert_into('etapas_de_ensino_tabela_auxiliar', item)
            cursor.execute(insert)