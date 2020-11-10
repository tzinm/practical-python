class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    @property 
    def cost(self):
        return self._shares * self.price

    def sell(self,sellnum):
        self._shares -= sellnum 
    
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, valor):
        if not isinstance(valor, int):
            raise TypeError('expecting an integer')
        self._shares = valor

"""
    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'
"""

class NewStock(Stock):
    def yow(self):
        print('Yow!')

