import sqlalchemy as sa
from models.main import Base

class Voucher(Base):
    __tablename__ = "Voucher"
    voucher_id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.String(64), nullable=False)
    discount = sa.Column(sa.REAL, nullable=False)
    days = sa.Column(sa.ARRAY, nullable=False)
    start_date = sa.Column(sa.Date, nullable=False)
    finish_date = sa.Column(sa.Date, nullable=False)
    limit_units = sa.Column(sa.Integer, default=None)

    def __str__(self):
        return self.name