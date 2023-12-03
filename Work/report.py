# report.py
#
# Exercise 2.11

import csv


def read_portfolio(filename: str) -> list[dict[str, int, float]]:
    """
    Reads a given portfolio file into a list of dictionaries
    """
    portfolio = []

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = ['name', 'shares', 'price']
        next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
                row = name, shares, price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            row = dict(zip(headers, row))
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
                price_dict.update({row[0]: float(row[1])})
            except IndexError as e:
                print(f"Empty line in file input: {e}")
    return price_dict


def calc_gains(portfolio: str, market_report: str) -> float:
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
        ticker = stock["name"]
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


def make_report(portfolio: list, prices: dict[str, float]) -> list[tuple]:
    """
    reads stock prices and returns a table
    """
    table_rows = []
    for stock in portfolio:
        try:
            ticker = stock["name"]
        except ValueError as e:
            print(f'{stock} has no ticker: {e}')
        basis = stock["price"]
        num_shares = stock["shares"]
        price = prices[ticker]
        change = price - basis

        table_row = (ticker, num_shares, price, change)
        table_rows.append(table_row)
    return table_rows


def display_report(data: list):
    headers = ('Name', 'Shares', 'Price', 'Change')
    name, shares, price, change = headers
    sep = '-'*10

    print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
    print(f'{sep:>10s} {sep:>10s} {sep:>10s} {sep:>10s} ')
    for row in data:
        print('%10s %10d %10.2f %10.2f' % row)


if __name__ == "__main__":
    portfolio = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")
    print(make_report(portfolio, prices))
