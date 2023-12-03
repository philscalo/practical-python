# pcost.py
#
# Exercise 1.27, 2.15
import csv


def calc_cost_basis(filename: str) -> float:
    with open(filename) as fp:
        rows = csv.reader(fp)
        headers = next(rows)
        total_cost = 0.0
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
                continue

    return total_cost


if __name__ == '__main__':
    print(f"Total cost {calc_cost_basis('Data/portfolio.csv'):.2f}")
