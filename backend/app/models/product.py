from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from datetime import datetime
from ..database import Base

# # if TYPE_CHECKING:
# #     from .category import Category



class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=False)
    image_url: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    # category: Mapped["Category"] = relationship("Category", back_populates="products")
    category = relationship("Category", back_populates="products")

    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String, nullable=False, index=True)
    # description = Column(Text)
    # price = Column(Float, nullable=False)
    # category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    # image_url = Column(String)
    # created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
