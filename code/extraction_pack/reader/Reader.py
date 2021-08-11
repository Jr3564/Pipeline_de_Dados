from abc import ABC, abstractmethod
from typing import Callable


class Reader(ABC):
    @staticmethod
    @abstractmethod
    def read_line_by_line(file_name: str, callback: Callable[[dict], None]):
        raise NotImplementedError
