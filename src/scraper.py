import requests
from bs4 import BeautifulSoup

def fetch_stock_price(symbol):
    """
    Fetch the current stock price for a given symbol from Yahoo Finance.

    Args:
        symbol (str): The stock symbol to fetch the price for (e.g., "AAPL" for Apple).

    Returns:
        float: The stock price if found, or None if not found.
    """
    # Construct the URL for the stock page on Yahoo Finance
    url = f"https://finance.yahoo.com/quote/{symbol}"

    try:
        # Send a GET request to the Yahoo Finance page
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception for a bad response (4xx, 5xx)

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Try to find the element containing the stock price using its HTML class
        price_element = soup.find('fin-streamer', {'data-field': 'postMarketPrice'})

        if price_element:
            # Clean the price and return it as a float
            price = float(price_element.text.replace(',', ''))  # Removing commas (if any)
            return price
        else:
            # If the price element is not found, return None
            return None

    except requests.RequestException as e:
        # Handle any network or request-related errors
        print(f"Error fetching data for {symbol}: {e}")
        return None