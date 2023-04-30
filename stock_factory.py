from stock import Stock


class StockFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_instance():
        if StockFactory._instance is None:
            StockFactory()
        return StockFactory._instance
    
    def create_stock(self, symbol, name, price):
        
        return Stock(symbol,name, price)
