#pip install yfinance
#from google.adk.agents.llm_agent import Agent
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from google.adk.tools import google_search

import yfinance as yf


def get_stock_price(symbol: str):
    """
    Retrieves the current stock price for a given symbol.

    Args:
        symbol (str): The stock symbol (e.g., "AAPL", "GOOG").

    Returns:
        float: The current stock price, or None if an error occurs.
    """
    try:
        stock = yf.Ticker(symbol)
        historical_data = stock.history(period="1d")
        if not historical_data.empty:
            current_price = historical_data['Close'].iloc[-1]
            return current_price
        else:
            return None
    except Exception as e:
        print(f"Error retrieving stock price for {symbol}: {e}")
        return None


root_agent = Agent(
    model='gemini-2.5-flash',
    name='stock_agent',
    instruction= 'Considering yourself as Wall street trade broker agent who retrieves stock prices based on a customer request. If a ticker symbol is provided in yFinance module, fetch the current price. If only a company name name is given, first perform a Google search to find the correct ticker symbol before retrieving the stock price. If the provided ticker symbol is invalid or data cannot be retrieved, inform the user that the stock price could not be found and they need to try again with the correct company/symbol/ticker name.',
    description='This agent specializes in retrieving real-time stock prices. Given a stock ticker symbol (e.g., AAPL/APPLE/TGT/GOOG/MSFT etc.) or the stock name, use the tools and reliable data sources to provide the most up-to-date price.',
    # calling python function as Tools
    ##tools=[get_stock_price]
    # You can only attach one tool at a time unless using agents as tools.
    # Now using Google search as tools in this case
    tools = [google_search]
)
