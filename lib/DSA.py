import click

expense_categories = ["Food", "Rent", "Transportation", "Entertainment"]

income_types = ("Salary", "Business", "Investment", "Bonus")

currency_symbols = {
    "USD": "$",
    "KES": "Ksh"
}

@click.command()
def main():
    click.echo("Welcome to Budget Tracker CLI!")

    expense_category = click.prompt("Enter expense category", type=click.Choice(expense_categories))

    income_type = click.prompt("Enter income type", type=click.Choice(income_types))

    currency = click.prompt("Enter currency", type=click.Choice(currency_symbols.keys()))

    click.echo(f"Expense Category: {expense_category}")
    click.echo(f"Income Type: {income_type}")
    click.echo(f"Currency Symbol: {currency_symbols[currency]}")

if __name__ == "__main__":
    main()
