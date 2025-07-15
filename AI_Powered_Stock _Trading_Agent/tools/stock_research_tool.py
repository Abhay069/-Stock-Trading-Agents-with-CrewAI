import yfinance as yf
from crewai.tools import tool

@tool("MarketPulse")
def stock_price(stock_name: str) -> str:  # This defines a function. You give it a stock name and it will return a text string.
    """
    Returns key stock metrics such as price, daily change, sector, and financial growth indicators.
    """

    # stock_name: str : for eg(AAPL, etc.)
    stock = yf.Ticker(stock_name)  # .Ticker("") gives us access to everything about Apple’s stock — price, history, financials, etc.
                                   # Loads live info for the company you're looking up.
    info = stock.info              #This accesses the .info property of the stock object.
                                   #It gives you a dictionary (a data structure like a list of key-value pairs).


    current_price = info.get("regularMarketPrice")
    recommendation = info.get("recommendationKey")
    today_high = info.get("dayHigh")
    today_low = info.get("dayLow")
    change = info.get("regularMarketChange")
    change_precent = info.get("regularMarketChangePercent")
    currency = info.get("currency","USD")
    revenue_growth = info.get("revenueGrowth")
    dividend_return = info.get("dividendYield")
    growth_rate = info.get("earningsQuarterlyGrowth")
    sector = info.get("sector")

    if current_price is None:
        return f"could not fetch price for {stock_name}. Please check the name or symbol."

    return (
        f"Stock: {stock_name.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"change:{change} ({round(change_precent, 2)}%)\n"
        f"High/Low Today: {today_high} / {today_low}\n"
        f"Sector: {sector}\n"
        f"Recommendation: {recommendation}\n"
        f"Quarterly Earnings Growth: {growth_rate}\n"
        f"Revenue Growth: {revenue_growth}\n"
        f"Dividend Yield: {dividend_return}\n"
    )










