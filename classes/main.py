
from rich.console import Console
from rich.table import Column, Table
from packages.credit_card import CreditCard

if __name__ == "__main__":
    wallet = []
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Customer")
    table.add_column("Bank", justify="right")
    table.add_column("Account", justify="right")
    table.add_column("Limit", justify="right")
    table.add_column("Balance", justify="right")

    # Data 
    customer_1 = CreditCard("John Doe", "1st Bank", "5391 0375 9387 5309", 1000)
    customer_2 = CreditCard("Jane Doe", "1st Bank", "5390 0875 9087 5000", 21000)

    if not wallet:
        wallet.append(customer_1)
        wallet.append(customer_2)

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)

    for c in wallet:
        c: CreditCard  # using type inorder to get the right class members in list
        table.add_row(
            c.get_customer(),
            c.get_bank(),
            c.get_account(),
            c.get_limit().__str__(),
            c.get_balance().__str__(),
        )
        print(
            c.get_customer(),
            c.get_bank(),
            c.get_account(),
            c.get_limit().__str__(),
            c.get_balance().__str__(),
        )
        while c.get_balance() > 100.00:
            c.make_payments(100)
            print("New balance =", c.get_balance())
        print()

    console.print(table)

