import sys
import os
# Ensure src/ is in the path for module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from scraper import fetch_stock_price

def main(): 
  stock_symbol = "AAPL"
  price = fetch_stock_price(stock_symbol)
  print(f"The current price of {stock_symbol} is: {price}")

if __name__ == "__main__":
  main()