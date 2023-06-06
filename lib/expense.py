from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sqlite3
from models import Expense, User

engine = create_engine("sqlite:///budget.db")
Session = sessionmaker(bind=engine)

def create_session():
    return Session()

def create_expense(description, amount, expense_type, expense_date, user_id):
    session = create_session()
    expense = Expense(
        description=description,
        amount=amount,
        expense_type=expense_type,
        expense_date=expense_date,
        user_id=user_id
    )
    session.add(expense)
    session.commit()
    session.close()

def update_expense(expense_id, description=None, amount=None, expense_type=None, expense_date=None, user_id=None):
    session = create_session()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        if description:
            expense.description = description
        if amount:
            expense.amount = amount
        if expense_type:
            expense.expense_type = expense_type
        if expense_date:
            expense.expense_date = expense_date
        if user_id:
            expense.user_id = user_id
        session.commit()
    else:
        print("Expense not found.")
    session.close()

def get_all_expenses():
    session = create_session()
    expenses = session.query(Expense).all()
    session.close()
    return expenses

def delete_expense(expense_id):
    session = create_session()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted.")
    else:
        print("Expense not found.")
    session.close()

def calculate_total_expenses():
    session = create_session()
    total = session.query(func.sum(Expense.amount)).scalar() or 0
    session.close()
    return total
