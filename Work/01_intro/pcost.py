# pcost.py
import csv


def share_calc(filepointer):
    with open(filepointer, newline='') as fp:
        portfolio_reader = csv.reader(fp, dialect='unix')
        next(portfolio_reader, None)  # skip header row

        portfolio_total = 0
        for row in portfolio_reader:
            try:
                position_value = int(row[1]) * float(row[2])
            except ValueError:
                print(f"ValueError occurred: {row}")
            except Exception as e:
                print(f"Exception occurred: {e}")

            portfolio_total += position_value
            print(f"Current Potfolio Total Value: {portfolio_total:,.2f}")


if __name__ == '__main__':
    share_calc('../Data/portfolio.csv')
