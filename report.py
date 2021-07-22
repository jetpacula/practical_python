# report.py
# from ipdb import set_trace
#
import csv
import sys
import fileparse


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


def read_portfolio(filename: str = "Data/portfolio.csv") -> list:
    """
    open file with data and return list filled with dicts
    """
    return fileparse.parse_csv(filename=filename, has_headers=True)


#
def update_prices(portfolio: dict, prices: tuple):
    """
    get dict and price tuple to check price
    """
    for item in portfolio:
        if item["name"] in prices:
            item["price"] = prices[item["name"]]
    return portfolio


'''
def portfolio_cost(portfolio: dict) -> int:
    """
    gets dict and counts total cost of portfolio
    """
    cost = 0
    for i in portfolio:
        cost += i["shares"] * i["price"]
    return cost
'''


def read_prices(filename: str = "Data/prices.csv") -> dict:
    """
    adds prices for change tracking in portfolio report
    """
    pricelist = fileparse.parse_csv(
        filename=filename, types=[str, float], has_headers=False
    )
    pricedict = dict((x, y) for x, y in pricelist)
    return pricedict


def portfolio_report(portfolio: str, prices: str):
    """
    high-level function to make report
    """
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)
    print_report(make_report(portfolio, prices))


# cost = portfolio_cost(read_portfolio())
# print('Total cost:', cost)
# Exercise 2.4
