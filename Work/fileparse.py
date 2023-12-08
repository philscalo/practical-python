# fileparse.py
#
# Exercise 3.10
import csv


def parse_csv(
    file,
    select=None,
    types=None,
    has_headers=True,
    delimit_char=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records
    """
    # Safety check
    if isinstance(file, str):
        raise RuntimeError(f"iterable expected, str received ({file})")
    if not hasattr(file, '__iter__'):
        raise RuntimeError("iterable expected for iterable argument")

    if select and has_headers is False:
        raise RuntimeError("select argument requires column headers")
    if delimit_char and delimit_char != ",":
        rows = csv.reader(file, delimiter=delimit_char)
    else:
        rows = csv.reader(file)

    if has_headers:
        headers = next(rows)

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if silence_errors is not True:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: {e}")
                else:
                    continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
