# tests/test_scraper.py
import os
# from dotenv import load_dotenv
import sys

# load_dotenv()  # Loads environment variables from .env file

# # Debug: Print PYTHONPATH to ensure it's loaded correctly
# print(f"PYTHONPATH is: {os.getenv('PYTHONPATH')}")


# Ensure src/ is in the path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scraper import fetch_stock_price

def test_fetch_stock_price():
    stock_symbol = "AAPL"
    price = fetch_stock_price(stock_symbol)
    assert price is not None
    assert isinstance(price, float)