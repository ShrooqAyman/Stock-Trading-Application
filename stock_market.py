
class StockMarket:

    def __init__(self):
        self.stocks = []
        self.observers = []
    
    
    def add_stock(self, stock):
            self.stocks.append(stock)

    def add_observer(self, observer):
        self.observers.append(observer)


    def update_prices(self, prices):
        for symbol, price in prices.items():
            for stock in self.stocks:
                if stock.get_symbol() == symbol:
                    stock.update_price(price)

                    for observer in self.observers:
                        if observer.symbol == symbol:
                            observer.update(symbol, price)
                        