#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import csv
import report
import sys

def portfolio_cost(portfile: str = None) -> int:
    """
    accepts filepath do portfolio, parses it into dict and counts total cost of portfolio
    """
    portfolio = report.read_portfolio(filename=portfile)
    cost = 0
    for i in portfolio:
        cost += i["shares"] * i["price"]
    print(f'Total cost: {cost}')
    return cost

def main(args):
    '''
    get pcost.py and filepath string from stdin and pass second argument to portfolio_cost
    '''
    portfile = args[1]
    portfolio_cost(portfile)
if __name__=='__main__':
        if len(sys.argv) != 2:
            raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
                    
        main(sys.argv)
