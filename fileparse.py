# fileparse.py
#
# Exercise 3.3
import csv
import io


def parse_csv(
    lines,
    select: list = None,
    types: list = None,
    has_headers: bool = True,
    delimiter: str = ",",
    silence_errors: bool = False,
) -> list:
    """
    Parse a CSV into a list of records
    """

    if type(lines) not in [list,tuple,io.TextIOWrapper] and not silence_errors:
        raise RuntimeError(f"can parse only list, tuple or file, not {type(lines)}")
    if not type(lines) is list:
        lines = lines.readlines()

    if select and not has_headers and not silence_errors:
        raise RuntimeError("select argument requires column headers")
    colnum = len(lines[0])



    types_dict = {"name": str, "price": float, "shares": int}
    # read the file headers
    if has_headers:

        headers = lines[0].strip().split(delimiter)

    if types:
        types_sorted = [i for i in types]
    elif not types and has_headers:
        types_sorted = [types_dict[colname] for colname in headers]
    else:
        types_sorted = [str for _ in range(colnum)]
    records = []
    if has_headers:
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = [headers.index(colname) for colname in headers]
        #print(i,l,'hello')
        for line in lines:
            line = line.strip().split(delimiter)
            if has_headers:
                has_headers=False
                continue
            
            try:
                line = [types_sorted[index](line[index]) for index in indices]
            except ValueError as e:
                if not silence_errors:
                    print(e, f"Cant read line {line}")
                continue

            record = dict(zip(headers, line))
            records.append(record)
    else:
        for line in lines:
            if  len(line.split(delimiter))<2:
                continue
            line = line.replace('"','').strip('\n').split(delimiter)
            try:
                line = tuple(types_sorted[index](line[index]) for index in range(len(line)))
            except ValueError as e:
                if not silence_errors:
                    print(e, f"Cant read line {line}")

            records.append(line)
    return records
