# report.py
#
# Exercise 2.4

import csv
import sys
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionarires with keys
    name, shares and price.
    '''
    return parse_csv(filename)

def read_prices(filename):
    return parse_csv(filename, has_headers=False)

def gain_loss(portfolio, prices):
    gain_loss = []
    gain_loss_dic = {}
    gain_loss_in_dic = {}
    
    for row in portfolio:
        differences = round(prices[row['name']] - row['price'],2)
        gain_loss_in_dic['adquisition'] = float(row['price'])
        gain_loss_in_dic['now'] = float(prices[row['name']])
        gain_loss_in_dic['difference'] = differences
        if differences > 0:
            gain_loss_in_dic['g/l'] = 'gain'
        else:
            gain_loss_in_dic['g/l'] = 'loss'
        gain_loss_dic[row['name']] = gain_loss_in_dic
        gain_loss.append(gain_loss_dic)
        gain_loss_dic = {}
        gain_loss_in_dic = {}
    
    return gain_loss

def make_report(portfolio, prices):
    result = []

    for row in portfolio:
        linea = (row['Name'], row['Shares'], prices[row['Name']], round(prices[row['Name']] - row['Price'],2))
        result.append(linea)
    return result

def print_report(report):
            
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

def portfolio_report(portfolio_file, prices_file):
    
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    report = make_report(portfolio, prices)

    return print_report(report)
