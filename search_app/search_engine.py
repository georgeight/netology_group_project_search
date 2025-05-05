"""Основная логика поискового движка"""

from typing import List, Dict, TypedDict
from pathlib import Path


class Document(TypedDict):
    """
    Определение типа данных для документа
    """
    document_id: int
    document_content: str


class WordDocumentData(TypedDict):
    """
    Определение типа данных для описания кол-ва вхождений
    слова из поискового индекса в документ
    """
    document_id: int
    word_tf: float


class WordData(TypedDict):
    """
    Определение типа данных для слова в поисковом индексе
    """
    documents: List[WordDocumentData]


class DocumentStorage:
    """Класс для обращения к хранилищу документов

    Args:
        db_path (Path): Путь к базе данных
    """
    def __init__(self, db_path: Path) -> None:
        pass

    def load_documents(self, documents: List[Document]) -> None:
        """Загрузка документов в хранилище
        
        Args:
            documents (List[Document]): Список документов
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

    def update(self, words: Dict[WordData]) -> None:
        """Обновление поискового индекса

        Args:
            words (WordData): Слова для обновления
        """

    def search(self, words: List[str]) -> Dict[WordData]:
        """
        Поиск документов по запросу
        
        Args:
            words (List[str]): Список слов для поиска

        Returns:
            Dict[WordData]: Результат
        """


class SearchEngine:
    """Класс для работы с поисковым движком

    Args:
        db_path (str): Путь к базе данных
    """
    def __init__(self, db_path: str) -> None:
        pass

    @staticmethod
    def _tokeinze(text: str) -> List[str]:
        """Токенизация текста

        Args:
            text (str): Текст для токенизации

        Returns:
            List[str]: Список токенов
        """

    def index(self, documents_path: Path) -> None:
        """Индексирование документов

        Args:
            documents_path (Path): Путь к директории с документами
        """

    def search(self, query: str) -> List[str]:
        """Поиск документов по запросу

        Args:
            query (str): Поисковый запрос

        Returns:
            List[str]: Список документов
        """
