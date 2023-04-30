class Portfolio:
    """
        A class representing a portfolio.

        Attributes:
            stocks : list of stocks
    """
    def __init__(self):
       
        """
        Creates a new Portfolio instance.
        """
        self.stocks = []


    def add_stock(self, stock):
        """
        Adds stock to the portfolio.

        Args:
            stock :stock to be added.
        """
        try:
            self.stocks.append(stock)
        except Exception as e:
            print(f'Error: {e}')
    
    def remove_stock(self, stock):
        """
        Removes stock from  portfolio.

        Args:
            stock :stock to be removed.
        """
        try:
            self.stocks.remove(stock)
        except Exception as e:
            print(f'Error: {e}')
