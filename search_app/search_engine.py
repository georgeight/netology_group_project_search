"""Основная логика поискового движка"""

from typing import List, TypedDict
from pathlib import Path


class WordDocumentData(TypedDict):
    """
    Определение типа данных для описания кол-ва вхождений
    слова из поискового индекса в документ
    """
    document_id: int
    count: int


class WordData(TypedDict):
    """
    Определение типа данных для слова в поисковом индексе
    """
    total_count: int
    documents: List[WordDocumentData]


class DocumentStorage:
    """Класс для обращения к хранилищу документов

    Args:
        db_path (Path): Путь к базе данных
    """
    def __init__(self, db_path: Path) -> None:
        pass

    def load_documents(self, documents: List[str]) -> None:
        """Загрузка документов в хранилище
        
        Args:
            documents (List[str]): Список документов
        """

    def get_documents(self, keys: List[int]) -> List[str]:
        """Получение документов по их ключам

        Args:
            keys (List[int]): Список ключей документов
        """


class SearchIndex:
    """Класс для работы с поисковым индексом

    Args:
        db_path (Path): Путь к базе данных
    """
    def __init__(self, db_path: Path) -> None:
        pass

    def update(self, words: List[WordData]) -> None:
        """Обновление поискового индекса

        Args:
            words (WordData): Слова для обновления
        """

    def search(self, words: List[WordData]) -> List[int]:
        """
        Поиск документов по запросу
        
        Args:
            words (List[WordData]): Список слов для поиска

        Returns:
            List[int]: Список ключей документов
        """


class SearchEngine:
    """Класс для работы с поисковым движком

    Args:
        db_path (str): Путь к базе данных
    """
    def __init__(self, db_path: str) -> None:
        pass

    def _tokeinze(self, text: str) -> List[str]:
        """Токенизация текста

        Args:
            text (str): Текст для токенизации
        """

    def index(self, documents: List[str]) -> None:
        """Индексирование документов

        Args:
            documents (List[str]): Список документов
        """

    def search(self, query: str) -> List[str]:
        """Поиск документов по запросу

        Args:
            query (str): Поисковый запрос

        Returns:
            List[str]: Список документов
        """
