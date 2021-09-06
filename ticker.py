# ticker.py

from follow import follow
import csv 
import report
import tableformat
import ipdb
def ticker(portfile,logfile,fmt):
    portfolio = report.read_portfolio(portfile)
    rows = filter_symbols(
            parse_stock_data(
                follow(logfile)),
                portfolio
            )
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name','price','change'])
#    ipdb.set_trace()
    for rowline in rows:
        formatter.row([str(i) for i in rowline.values()])



def convert_types (rows, types):
    for row in rows:
        yield (func(val) for func, val in zip(types,row))

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers,row))


def select_columns(rows,indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_stock_data(lines):

    rows = csv.reader(lines)
    rows = select_columns(rows,[0,1,4])
    rows = convert_types(rows,[str,float,float])
    rows = make_dicts(rows,['name','price','change'])
    return rows

def filter_symbols(rows,names):
    rows = (row for row in rows if row['name'] in names)
    for row in rows:
 #       if row['name'] in names:
            yield row


if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)


