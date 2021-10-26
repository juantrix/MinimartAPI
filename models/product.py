import sqlalchemy as sa
from sqlalchemy.sql.schema import ForeignKey
from models.voucher import Voucher
from models.main import Base


class Product(Base):
    __tablename__ = "Product"
    product_id = sa.Column(sa.Integer, primary_key=True)
    store_id = sa.Column(sa.Integer, ForeignKey=True)
    stock = sa.Column(sa.Integer, default=0)
    category = sa.Column(sa.String, nullable=False)
    price = sa.Column(sa.REAL, nullable=False)
    #voucher = sa.Column(Voucher, default=None)
    name = sa.Column(sa.String, nullable=False)

    def __str__(self):
        return self.name