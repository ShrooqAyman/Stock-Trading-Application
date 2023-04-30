class Stock:
    """
    class representing a stock.

    Attributes:
        symbol (str): stock's symbol.
        name (str): stock's name.
        price (float): stock's price
    """
    def __init__(self, symbol:str, name:str, price):
        """
        Creates a new stock instance.

        Args:
            symbol (str): stock's symbol.
            name (str): stock's name.
            price (float): stock's price
        """
        self.symbol = symbol
        self.name = name
        self.price = price
        

    def update_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol
