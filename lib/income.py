from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sqlite3
from models import Expense, User, Income

engine = create_engine("sqlite:///budget.db")
Session = sessionmaker(bind=engine)

def create_session():
    return Session()

def create_income(description, amount, income_type, income_date, user_id):
    session = create_session()
    income = Income(
        description=description,
        amount=amount,
        income_type=income_type,
        income_date=income_date,
        user_id=user_id
    )
    session.add(income)
    session.commit()
    session.close()

def update_income(income_id, description=None, amount=None, income_type=None, income_date=None, user_id=None):
    session = create_session()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        if description:
            income.description = description
        if amount:
            income.amount = amount
        if income_type:
            income.income_type = income_type
        if income_date:
            income.income_date = income_date
        if user_id:
            income.user_id = user_id
        session.commit()
    else:
        print("income not found.")
    session.close()

def get_all_incomes():
    session = create_session()
    incomes = session.query(Income).all()
    session.close()
    return incomes

def delete_income(income_id):
    session = create_session()
    income = session.query(Income).filter_by(id=income_id).first()
    if income:
        session.delete(income)
        session.commit()
        print("income deleted.")
    else:
        print("income not found.")
    session.close()

def calculate_total_incomes():
    session = create_session()
    total = session.query(func.sum(Income.amount)).scalar() or 0
    session.close()
    return total
