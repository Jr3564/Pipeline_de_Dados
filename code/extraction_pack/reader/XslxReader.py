from extraction_pack.reader.Reader import Reader
from openpyxl import load_workbook


class XslxReader(Reader):
    @staticmethod
    def read_page_xlsx(file_name: str, page_name: str):
        file_xlsx = load_workbook(filename=file_name)
        return file_xlsx[page_name]
