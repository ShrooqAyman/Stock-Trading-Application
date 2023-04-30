from stock_factory import StockFactory
from stock_market import StockMarket
from portfolio import Portfolio
from trader import Trader
from stock_observer import StockObserver


if __name__ == '__main__':
    # Create a StockFactory object
    factory = StockFactory.get_instance()

    # Create some sample stocks
    apple_stock = factory.create_stock('AAPL', 'Apple Inc.', 130.21)
    google_stock = factory.create_stock('GOOG', 'Alphabet Inc.', 2069.66)
    microsoft_stock = factory.create_stock(
        'MSFT', 'Microsoft Corporation', 235.75)

    # Create a StockMarket object and add the stocks to it
    stock_market = StockMarket()

    stock_market.add_stock(apple_stock)
    stock_market.add_stock(google_stock)
    stock_market.add_stock(microsoft_stock)

    # Create a Portfolio object and add some stocks to it
    portfolio = Portfolio()
    portfolio.add_stock(apple_stock)
    portfolio.add_stock(google_stock)

    # Create a Trader object and link it to the portfolio
    trader = Trader('shurouq', 'shurouqewaili@gmail.com', portfolio)

    # Create StockObservers for each stock and add them to the StockMarket
    apple_observer = StockObserver('AAPL')
    apple_observer.add_trader(trader)

    google_observer = StockObserver('GOOG')
    google_observer.add_trader(trader)

    microsoft_observer = StockObserver('MSFT')

    p2 = Portfolio()
    t2 = Trader('noor', 'shurouqewaili@gmail.com', p2)
    stock_market.add_observer(microsoft_observer)
    microsoft_observer.add_trader(t2)

    # Create TraderObservers for the trader's stocks and add them to the StockMarket
    for stock in trader.portfolio.stocks:
        stock_observer = StockObserver(stock.symbol)
        stock_observer.add_trader(trader)
        stock_market.add_observer(stock_observer)

    # Update the prices of the stocks in the StockMarket
    prices = {'AAPL': 140.21, 'GOOG': 2100.66, 'MSFT': 250.75}

    print('before change price')
    for stock in trader.portfolio.stocks:
        print(stock.symbol, stock.name, stock.price)

    stock_market.update_prices(prices)

    print('\nAfter')
    # Output the trader's updated portfolio
    for stock in trader.portfolio.stocks:
        print(stock.symbol, stock.name, stock.price)

    # for stock in stock_market.stocks:
    #     print(stock)
    #     print(stock.symbol, stock.name, stock.price)
