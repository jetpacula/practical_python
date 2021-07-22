# pcost.py
#
# Exercise 1.27

import csv

import report


def portfolio_cost(portfolio: str = None) -> int:
    """
    gets dict and counts total cost of portfolio
    """
    portfolio = report.read_portfolio(portfolio)
    cost = 0
    for i in portfolio:
        cost += i["shares"] * i["price"]
    return cost
