from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Date, Numeric, Index
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.db_setup import Base
from datetime import datetime, timezone, date


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    transactions = relationship("Transaction", back_populates="category")



class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Numeric(12,2), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="transactions")
    date = Column(DateTime(timezone=True), server_default=func.now())
# index to speed up (category_id/date) filters
Index("ix_transactions_category_date", Transaction.category_id, Transaction.date)
#weekly budget goals for user

class Goal(Base):
    __tablename__ = "goals"

    #primary key
    id = Column(Integer, primary_key=True, index=True)

    #link to categories.id
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, unique=True, index = True)

    #Dollar amount allowed per week
    weekly_budget = Column(Numeric(12,2), nullable=False)

    #when goal was created
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # access category object from a goal
    category = relationship("Category", backref="goal", foreign_keys=[category_id])