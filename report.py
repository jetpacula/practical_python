#!/usr/bin/env python3
# report.py
#
import ipdb
import csv
import sys
import fileparse
import gzip
from stock import Stock
from portfolio import Portfolio
import tableformat

def portfolio_report(portfoliofile: str, pricefile: str, fmt : str = 'txt'):
    """
    Make a stock report from filepaths to portfolio file and prices file
    """
    #read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    
    #generate report
    report = make_report(portfolio, prices)

    #output the report
    formatter = tableformat.create_formatter(fmt)
    print_report(report,formatter)



def make_report(portfolio: list, prices: dict = None) -> list:
    """
    Get list of stocks, update prices and make a report- list containing tuples
    """

    report = []
    for s in portfolio:
        if s.name in prices.keys():
            report.append(
                (
                    s.name,
                    s.shares,
                    prices[s.name],
                    prices[s.name] - s.price,
                )
            )
    return report


def print_report(reportdata: tuple, formatter) -> None:
    """
    prints table from tuple
    """
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

  #  print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
   # breaker = "-" * 10
  #  print(f'{breaker+" ":s}{breaker+" ":s}{breaker+" ":s}{breaker+" ":s}')
   # for i in report:
    #    print(f"{i[0]:>10s} {i[1]:>10d} ${i[2]:>10.2f} {i[3]:>10.2f}")


def read_portfolio(filename, **opts) -> list:
    """
    open file with data and return list filled with dicts
    """
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(
                lines,
                select=['name','shares','price'],
                types=[str,int,float],
                **opts)
    '''
    if filename.endswith('.csv'):
        with open(filename, 'rt') as f:
            res = fileparse.parse_csv(f, has_headers=True)
    elif filename.endswith('.gz'):
        with gzip.open(filename, 'rt') as f:
            res = fileparse.parse_csv(f)
    else:
        res = fileparse.parse_csv(filename)
    '''


    return Portfolio([ Stock(**d) for d in portdicts])
#    return Portfolio([ Stock(str(d['name']).strip('"'), d['shares'], d['price']) for d in res])


#
def update_prices(portfolio: dict, prices: tuple):
    """
    get dict and price tuple to check price
    """
    for item in portfolio:
        if item["name"] in prices:
            item["price"] = prices[item["name"]]
    return portfolio



def read_prices(filename: str = "Data/prices.csv") -> dict:
    """
    adds prices for change tracking in portfolio report
    """
    if filename.endswith('.csv'):
        with open(filename, 'rt') as f:
            pricelist = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    elif filename.endswith('.gz'):
        with gzip.open(filename, 'rt') as f:
            pricelist = fileparse.parse_csv(f)
    else:
        pricelist = fileparse.parse_csv(filename, types=[str, float], has_headers=False)

 #   pricedict = dict((x, y) for x, y in pricelist)
    pricedict = dict(pricelist)
    return pricedict

def main(args):
    
    print('generating report')
    portfolio_report(portfoliofile = args[1], pricefile= args[2], fmt=args[3])
if __name__=='__main__':
    if len(sys.argv) < 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile format (csv/txt/html)')
    main(sys.argv[:]) 
# Exercise 2.4
