#!/usr/bin/env python3
# report.py
#
import csv
import sys
import fileparse
import gzip

def portfolio_report(portfolio: str, prices: str):
    """
    high-level function to make report
    accepts filepaths and prints report in a table
    """
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)
    print_report(make_report(portfolio, prices))



def make_report(portfolio: list = None, prices: dict = None) -> list:
    """
    Get list of stocks, update prices and make a report- list containing tuples
    """

    report = []
    for stonk in portfolio:
        if stonk["name"] in prices.keys():
            report.append(
                (
                    stonk["name"],
                    stonk["shares"],
                    prices[stonk["name"]],
                    prices[stonk["name"]] - stonk["price"],
                )
            )
    return report


def print_report(report: tuple) -> None:
    """
    prints table from tuple
    """
    print(f'{"Name":>10s} {"Shares":>10s} {"Price":>10s} {"Change":>10s}')
    breaker = "-" * 10
    print(f'{breaker+" ":s}{breaker+" ":s}{breaker+" ":s}{breaker+" ":s}')
    for i in report:
        print(f"{i[0]:>10s} {i[1]:>10d} ${i[2]:>10.2f} {i[3]:>10.2f}")


def read_portfolio(filename) -> list:
    """
    open file with data and return list filled with dicts
    """
    if filename.endswith('.csv'):
        with open(filename, 'rt') as f:
            res = fileparse.parse_csv(f, has_headers=True)
    elif filename.endswith('.gz'):
        with gzip.open(filename, 'rt') as f:
            res = fileparse.parse_csv(f)
    else:
        res = fileparse.parse_csv(filename)
    return res


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
    portfolio_report(args[1],args[2])

if __name__=='__main__':
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    main(sys.argv[:]) 
# Exercise 2.4
