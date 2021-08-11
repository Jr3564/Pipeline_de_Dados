from typing import Callable
from extraction_pack.reader.Reader import Reader
import csv


class CsvReader(Reader):
    @staticmethod

    def read_line_by_line(file_name: str, callback: Callable[[dict], None], delimiter='|'):
        with open(file_name, "r") as file:
            header = next(csv.reader(file, delimiter=delimiter))

            for student in csv.reader(file, delimiter=delimiter):
                student_full_data = {
                    current_title: current_content
                    for current_title, current_content
                    in zip(header, student)
                }

                callback(student_full_data)
