# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str,
    select: list = None,
    types: list = None,
    has_headers: bool = False,
    delimiter: str = ",",
    silence_errors: bool = False,
) -> list:
    """
    Parse a CSV into a list of records
    """
    if select and not has_headers and not silence_errors:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        for row in rows:
            colnum = len(row)
            break

    types_dict = {"name": str, "price": float, "shares": int}
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # read the file headers
        if has_headers:

            headers = next(rows)

        if types:
            types_sorted = [i for i in types]
        elif not types and has_headers:
            types_sorted = [types_dict[colname] for colname in headers]
        else:
            # TODO skips first line          # types_sorted = [str for _ in range(len(next(rows)))]
            types_sorted = [str for _ in range(colnum)]

        if has_headers:

            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select

            else:
                indices = [headers.index(colname) for colname in headers]
        records = []

        for row in rows:

            if not row:
                continue
            # filter the selected columns if specified

            if has_headers:
                if indices:
                    try:
                        row = [types_sorted[index](row[index]) for index in indices]
                    except ValueError as e:
                        if not silence_errors:

                            print(e, f"Cant read row {row}")
                        continue
                record = dict(zip(headers, row))
                records.append(record)

            else:
                # set_trace()
                try:
                    row = tuple(
                        types_sorted[index](row[index]) for index in range(len(row))
                    )
                except ValueError as e:
                    if not silence_errors:

                        print(e, f"Cant read row {row}")
                    continue

                records.append(row)

            # make a dictionary

    return records
