from sqlalchemy import select, ColumnElement
from sqlalchemy.orm import Session, joinedload
from typing import List
from ..models.product import Product
from ..schemas.products import ProductCreate


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Product]:
        return list(self.db.scalars(select(Product).options(joinedload(Product.category))).all())

    def get_by_id(self, product_id: int) -> Product | None:
        return self.db.scalars(
            select(Product)
            .options(joinedload(Product.category))
            .where(Product.id == product_id)
        ).first()

    def get_by_category(self, category_id: int) -> List[Product]:
        return list(
            self.db.scalars(
                select(Product)
                .options(joinedload(Product.category))
                .where(Product.category_id == category_id)
            ).all()
        )

    def create(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_multiple_by_ids(self, product_ids: List[int]) -> List[Product]:
        return list(
            self.db.scalars(
                select(Product)
                .options(joinedload(Product.category))
                .where(Product.id.in_(product_ids))
            ).all()
        )