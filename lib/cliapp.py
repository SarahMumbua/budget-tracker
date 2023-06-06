import click
from expense import (
    create_expense,
    update_expense,
    get_expenses_by_category,
    calculate_total_expenses,
)
from income import (
    create_income,
    update_income,
    get_incomes_by_category,
    calculate_total_incomes,
)

@click.group()
def cli():

@cli.command()
@click.option('--category', type=str, help='Expense category')
@click.option('--amount', type=float, help='Expense amount')
def add_expense(category, amount):
    # Validate and process user input
    if not category or not amount:
        click.echo("Please provide both expense category and amount.")
        return

    # Add the expense to the database
    create_expense(category, amount)

    click.echo(f"Expense added: Category: {category}, Amount: {amount}")

@cli.command()
@click.option('--category', type=str, help='Expense category')
def get_expenses(category):
    # Fetch expenses from the database based on the category
    expenses = get_expenses_by_category(category)

    # Display the retrieved expenses
    click.echo(f"Expenses for category '{category}':")
    for expense in expenses:
        click.echo(f"Category: {expense.category}, Amount: {expense.amount}")

@cli.command()
def calculate_total():
    # Calculate the total expenses from the database
    total = calculate_total_expenses()

    click.echo(f"Total expenses: {total}")

if __name__ == '__main__':
    cli()
