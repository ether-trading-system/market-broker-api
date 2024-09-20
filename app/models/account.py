from sqlalchemy import Column, String, DateTime

from app.models.base import Base


class Account(Base):
    __tablename__ = 'T_ACCOUNT'

    account_number = Column("ACCOUNT_NUMBER", String, primary_key=True)
    api_key = Column("API_KEY", String, primary_key=True)
    access_token = Column("ACCESS_TOKEN", String, nullable=False)
    product_id = Column("PRODUCT_ID", String)
    cr_dt = Column("CR_DT", DateTime)
