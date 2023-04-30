class Trader:
    """
    class representing a trader who can buy and sell stocks.

    Attributes:
        portfolio :the trader's portfolio.
    """
    def __init__(self, name,email, portfolio):
        """
        Creates a new Trader instance.

        Args:
            portfolio :the trader's portfolio.
        """
        self.name =name
        self.email = email
        self.portfolio = portfolio

    def buy(self, stock):
        """
        Buys a stock and adds it to the trader's portfolio.

        Parameters:
            stock : stock to be bought.
        """
        self.portfolio.add_stock(stock)
        
    def sell(self, stock):
        """
        Sells a stock and remove it from the trader's portfolio.

        Parameters:
            stock : stock to be sold.
        """
        self.portfolio.remove_stock(stock)




    def get_name(self):
        """"
        Return trader's name
        """
        return self.name
    
    def get_email(self):
        """"
        Return trader's email
        """
        return self.email
