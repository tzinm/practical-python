# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    portfolio = []
    portfolio_dic = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            portfolio_dic['Name'] = record['name']
            portfolio_dic['Shares'] = int(record['shares'])
            portfolio_dic['Price'] = float(record['price'])
            portfolio.append(portfolio_dic)
            portfolio_dic = {}
    return portfolio

def read_prices(filename):
    prices = {}
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            for row in rows:
                prices[row[0]] = float(row[1])
    except IndexError:
        pass
    return prices

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
        
headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in make_report(read_portfolio(sys.argv[1]), read_prices('Data/prices.csv')):
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
