#!/usr/bin/env python3.9
# pcost.py

import report


def portfolio_cost(filename: str) -> float:
    portfolio = report.read_portfolio(filename)
    total_cost = 0.0
    for stock in portfolio:
        total_cost += stock.shares * stock.price

    return total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit("Usage: %s portfoliofile" % args[0])
    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":
    import sys

    main(sys.argv)
