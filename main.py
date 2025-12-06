"""Calculate budget splits given an amount"""

import sys

from prettytable import PrettyTable, TableStyle


def calculate_budget(salary: float):
    """Calculate budget splits given a salary amount"""
    # ESPP = 0.07
    # 401k = 0.08
    # savings_split = 0.10  # already maxed out savings
    stocks_split = 0.25
    crypto_split = 0.05
    spending_split = 0.55

    stocks_amount = salary * stocks_split
    crypto_amount = salary * crypto_split
    # savings_amount = salary * savings_split
    spending_amount = salary * spending_split

    return stocks_amount, crypto_amount, spending_amount


def main():
    """Main function"""
    taxed_income = float(sys.argv[1])

    stocks, crypto, spending = calculate_budget(taxed_income)

    table = PrettyTable()
    table.set_style(TableStyle.SINGLE_BORDER)
    table.field_names = ["Category", "Amount ($)"]
    table.add_rows(
        [
            ["Stocks (25%)", f"{stocks:,.2f}"],
            ["Crypto (5%)", f"{crypto:,.2f}"],
            # ["Savings (10%)", f"{savings:,.2f}"],
            ["Spending (55%)", f"{spending:,.2f}"],
        ]
    )

    print(f"For your salary of ${taxed_income:,.2f}:")
    print(table)


if __name__ == "__main__":
    main()
