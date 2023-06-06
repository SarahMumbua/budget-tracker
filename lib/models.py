from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    expenses = relationship("Expense", back_populates="user")
    incomes = relationship("Income", back_populates="user")

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    amount = Column(Integer)
    expense_type = Column(String(50))
    expense_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="expenses")

class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True)
    description = Column(String(100))
    amount = Column(Integer)
    income_type = Column(String(50))
    income_date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="incomes")
