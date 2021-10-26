import sqlalchemy as sa
from sqlalchemy.orm import relationship
from models.main import Base

class Cart(Base):
    __tablename__ = "Cart"
    id = sa.Column(sa.Integer, primary_key=True)
    products = sa.Column(Product, default=None)
    total_price = sa.Column(sa.REAL, sa.ForeignKey("authors.id"))
    author = relationship("Author", backref=backref("books"))

    def __str__(self):
        return self.products 