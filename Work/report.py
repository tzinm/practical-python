# report.py
#
# Exercise 2.4

import csv
import sys
import tableformat
#from portfolio import Portfolio
from fileparse import parse_csv
from stock import Stock
from portfolio2 import Portfolio

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionarires with keys
    name, shares and price.
    '''
    with open(filename) as lines:
        portdict = parse_csv(lines, columns=['name','shares','price'], types=[str,int,float], has_headers=True)    
    portfolio = [Stock(d['name'],d['shares'],d['price']) for d in portdict ]
    return Portfolio(portfolio)

def read_prices(filename):
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float]))

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
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

    for row in portfolio:
        linea = (row['name'], row['shares'], prices[row['name']], round(prices[row['name']] - row['price'],2))
        result.append(linea)
    return result

def print_report(report,formatter):       
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    #Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    
    #Create the report data
    report = make_report(portfolio, prices)

    #Print it out
    formatter = tableformat.create_formatter(fmt)
    return print_report(report, formatter)

def main(args):
    if len(args) != 4:
        raise SystemExit('Usage: %s portfile pricefile format' % args[0])
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
