from random import randint, sample
from typing import List
from datetime import datetime
import hashlib

CUSTOM_RANDOM_STOCKS = [
    "MSFT", "AAPL", "AMZN", "GOOGL", "TSLA", "META", "NVDA", "FINTUAL"
]
DATE_FORMAT = "%Y-%m-%d"
MESSAGE_ERROR = "Invalid date format. Please use the format yyyy-mm-dd."

class InvalidDateFormat(Exception):
    """Exception raised for errors in the format of the date."""
    
    def __init__(self, date: str) -> None:
        """Initialize the exception with the invalid date and a custom error message.
        
        Args:
            date (str): The date string that caused the error.
        """
        super().__init__(f"{date} is not a valid date. {MESSAGE_ERROR}")

class Stock:
    """Represents a single stock with a name and a method to generate its price."""
    
    def __init__(self, name: str) -> None:
        """Initialize a Stock instance with a given name.
        
        Args:
            name (str): The name of the stock.
        """
        self.name = name
    
    def _generate_random_price(self) -> float:
        """Generate a random stock price between $1.01 and $1000.99.
        
        Returns:
            float: A randomly generated stock price.
        """
        return randint(1, 1000) + randint(1, 100) / 100
    def __generate_hash_from_string(self, *argv) -> str:
        """Generate a hash from a string.
        
        Args:
            *argv (str): The strings to be hashed.
        
        Returns:
            str: The hashed string.
        """
        return hashlib.sha256("".join(argv).encode()).hexdigest()
    def get_price(self) -> float:
        """Get the current price of the stock.
        
        Returns:
            float: The current stock price.
        """
        return self._generate_random_price()

class Portfolio:
    """Represents a portfolio of randomly selected stocks with methods to calculate profit."""
    
    def __init__(self) -> None:
        """Initialize a Portfolio instance with a random selection of stocks."""
        self.stocks = self._generate_random_stocks()
        
    def _generate_random_stocks(self) -> List[Stock]:
        """Generate a random list of Stock instances.
        
        Returns:
            List[Stock]: A list of randomly selected Stock instances.
        """
        stock_count = randint(1, len(CUSTOM_RANDOM_STOCKS))
        return [Stock(name) for name in sample(CUSTOM_RANDOM_STOCKS, stock_count)]
    
    def _validate_date_format(self, date_str: str) -> datetime:
        """Validate and convert a date string to a datetime object.
        
        Args:
            date_str (str): The date string to validate.
        
        Returns:
            datetime: The corresponding datetime object if the date is valid.
        
        Raises:
            InvalidDateFormat: If the date string does not match the required format.
        """
        try:
            return datetime.strptime(date_str, DATE_FORMAT)
        except ValueError:
            raise InvalidDateFormat(date_str)
        
    def _calculate_days_difference(self, start_date: datetime, end_date: datetime) -> int:
        """Calculate the difference in days between two dates.
        
        Args:
            start_date (datetime): The start date.
            end_date (datetime): The end date.
        
        Returns:
            int: The number of days between the two dates.
        """
        return abs((end_date - start_date).days)
    
    def _calculate_years_difference(self, start_date: datetime, end_date: datetime) -> float:
        """Calculate the difference in years between two dates.
        
        Args:
            start_date (datetime): The start date.
            end_date (datetime): The end date.
        
        Returns:
            float: The number of years between the two dates.
        """
        return self._calculate_days_difference(start_date, end_date) / 365
    
    def _calculate_annualized_return(self, initial_price: float, final_price: float, years: float) -> float:
        """Calculate the annualized return between two prices over a number of years.
        
        Args:
            initial_price (float): The initial price of the portfolio.
            final_price (float): The final price of the portfolio.
            years (float): The number of years over which the return is calculated.
        
        Returns:
            float: The annualized return as a percentage.
        """
        return ((final_price / initial_price) ** (1 / years) - 1) * 100

    
    def _calculate_profit_percentage(self, initial_price: float, final_price: float) -> float:
        """Calculate the profit percentage between two prices.
        
        Args:
            initial_price (float): The initial price of the portfolio.
            final_price (float): The final price of the portfolio.
        
        Returns:
            float: The profit as a percentage.
        """
        return (final_price - initial_price) / initial_price * 100
    
    def _get_portfolio_value(self) -> float:
        """Calculate the total value of the portfolio.
        
        Returns:
            float: The total value of the portfolio based on current stock prices.
        """
        return sum(stock.get_price() for stock in self.stocks)
    
    def calculate_profit_between(self, start_date_str: str, end_date_str: str) -> None:
        """Calculate and print the profit and annualized profit between two dates.
        
        Args:
            start_date_str (str): The start date as a string in the format 'yyyy-mm-dd'.
            end_date_str (str): The end date as a string in the format 'yyyy-mm-dd'.
        """
        self._validate_date_format(start_date_str)
        self._validate_date_format(end_date_str)
        
        initial_price = self._get_portfolio_value()
        final_price = self._get_portfolio_value()
        
        total_profit = self._calculate_profit_percentage(initial_price, final_price)

        print(f"Profit between {start_date_str} and {end_date_str}: {total_profit:.2f}%")

    
    def calculate_profit_annualized(self, start_date_str: str, end_date_str:str) -> None:
        """Calculate and print the profit and annualized profit from a start date until today.
        
        Args:
            start_date_str (str): The start date as a string in the format 'yyyy-mm-dd'.
        """
        start_date = self._validate_date_format(start_date_str)
        end_date = self._validate_date_format(end_date_str)
        
        initial_price = self._get_portfolio_value()
        final_price = self._get_portfolio_value()

        years = self._calculate_years_difference(start_date, end_date)

        total_profit = self._calculate_profit_percentage(initial_price, final_price)
        annualized_profit = self._calculate_annualized_return(initial_price, final_price, years)

        print(f"Profit since {start_date_str}: {total_profit:.2f}%")
        print(f"Annualized profit: {annualized_profit:.2f}%")

#example of use

# if __name__ == "__main__":
#     portafolio = Portfolio()
#     portafolio.calculate_profit_between("2022-01-01", "2020-01-01")
#     portafolio.calculate_profit_annualized("2022-01-01", "2020-01-01")
        


    
    
    

    
