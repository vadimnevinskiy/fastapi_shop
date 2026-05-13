from typing import TYPE_CHECKING
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base

if TYPE_CHECKING:
    from .product import Product


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="category")

    # Устаревший синтаксис
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String, unique=True, nullable=False, index=True)
    # slug = Column(String, unique=True, nullable=False, index=True)
    #
    # products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
