import sqlalchemy as sa
from models.main import Base

class Store(Base):
    __tablename__ = "Store"
    store_id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(64), nullable=False)
    address = sa.Column(sa.String(128), nullable=False)
    logo = sa.Column(sa.String, default='https://www.pngitem.com/pimgs/m/150-1503945_transparent-user-png-default-user-image-png-png.png')
    work_days = sa.Column(sa.ARRAY, nullable=False)
    start_hours = sa.Column(sa.Time, nullable=False)
    finish_hours = sa.Column(sa.Time, nullable=False)
    #work_days_hours = sa.Column(Schedule, nullable=False)
    #products = sa.Column(Product, nullable=False) # one to mani

    def __str__(self):
        return self.name

