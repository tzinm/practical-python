# pcost.py
#
# Exercise 1.27

import csv
import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

if len(sys.argv) == 2:
   filename = sys.argv[1]
else:
   filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
