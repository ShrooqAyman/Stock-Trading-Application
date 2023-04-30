from observer import Observer
from helper import send_notification_email

class StockObserver(Observer):
    def __init__(self, symbol):
        self.symbol = symbol
        self.traders = []


    def add_trader(self, trader):
        self.traders.append(trader)


    def update(self, symbol,price):
        for trader in self.traders:
                msg = f'Hi, {trader.get_name()}, stock : {symbol} has new price of {price}'
                send_notification_email(trader.get_email(), msg)
                print(msg)

            
         