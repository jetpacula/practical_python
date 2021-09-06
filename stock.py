import typedproperty as tpp

class Stock:
    name = tpp.String('name')
    shares = tpp.Integer('shares')
    price = tpp.Float('price')
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def sell(self,amount):
        self.shares -= amount

#TODO fix get item
    def __getitem__(self,index):
        return self.__slots__[index]

    @property
    def cost(self):
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value,int):
            raise TypeError('Expected int')
        self._shares = value

    def __repr__(self):
        return f'Stock({self.name}, {self.shares:d}, {self.price:0.2f})'
    '''
    def __getattr__(self,field):
        if field=='name':
            return self.name
        elif field=='shares':
            return self.shares
        elif field=='price':
            return self.price
        else:
            raise Exception()
    '''
