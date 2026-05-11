from sqlalchemy import select, ColumnElement
from sqlalchemy.orm import Session
from typing import List
from ..models.category import Category
from ..schemas.category import CategoryCreate


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db  # Получаем базу данных для работы

    def get_all(self) -> List[Category]:
        """
            Получить все категории.

            Метод обращается к базе данных, получает все категории
            :return: возвращает список категорий
        """

        return list(self.db.scalars(select(Category)).all())
        # return self.db.query(Category).all()  # Устаревший синтаксис

    def get_by_id(self, category_id: int) -> Category | None:
        """
        Метод обращается к базе данных, ищет категорию по id
        :param category_id: ID категории
        :return: Возвращает категорию или None
        """
        return self.db.scalars(select(Category).where(Category.id == category_id)).first()
        # return self.db.query(Category).filter(Category.id == category_id).first()   # Устаревший синтаксис

    def get_by_slug(self, slug: str) -> Category | None:
        """
        Метод обращается к базе данных, ищет категорию по slug
        :param slug: ЧПУ категории
        :return: Возвращает категорию или None
        """
        return self.db.scalars(select(Category).where(Category.slug == slug)).first()
        # return self.db.query(Category).filter(Category.slug == slug).first()   # Устаревший синтаксис

    def create(self, category_data: CategoryCreate) -> Category:
        """
        Создание категории
        Получает в параметрах данные новой категории
        :param category_data: name, slug
        :return: Сохраняет категорию, и возвращает ее
        """
        db_category = Category(**category_data.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category
