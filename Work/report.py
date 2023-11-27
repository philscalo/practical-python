# report.py
#
# Exercise 2.4

import csv


def read_portfolio(filename: str) -> list[dict]:
    """
    Reads a given portfolio file into a list of tuples
    """
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.DictReader(f)
        for row in rows:
            portfolio.append(row)

    return portfolio


def read_prices(filename: str) -> dict:
    """
    reads tuples into a dict
    """
    price_dict = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                price_dict.update({row[0]: row[1]})
            except IndexError as e:
                print(f"Empty line in file input: {e}")
    return price_dict


def calc_gains(portfolio, market_report):
    """
    reads a portfolio, compares to current price file, and returns calculated
    unrealized gains of the portfolio
    """
    unrealized_gains = 0.0
    current_total_portfolio_value = 0.0
    total_cost_basis = 0.0

    portfolio_basis = read_portfolio(portfolio)
    portfolio_current = read_prices(market_report)
    for stock in portfolio_basis:
        ticker = stock['name']
        num_shares = int(stock["shares"])
        basis = num_shares * float(stock["price"])
        total_cost_basis += basis
        current_price = float(portfolio_current[ticker])
        current_value = num_shares * current_price
        current_total_portfolio_value += current_value
        unrealized_gain = current_value - basis
        print(f"{ticker} = {unrealized_gain:.2f}")
        unrealized_gains += unrealized_gain

    print(f"\nTotal Portfolio Basis: {total_cost_basis:.2f}\n")
    print(f"\nCurrent Total Portfolio Value: {current_total_portfolio_value:.2f}\n")
    return unrealized_gains


if __name__ == "__main__":
    print(calc_gains("Data/portfolio.csv", "Data/prices.csv"))
