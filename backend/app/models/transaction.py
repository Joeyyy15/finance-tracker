from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.db.db_setup import Base

class Transaction(Base):
    __tablename__ = "Transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())