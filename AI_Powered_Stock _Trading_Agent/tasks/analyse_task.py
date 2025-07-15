from crewai import Task
from agents.analyst_agent import agent_analyst


stock_analysis =  Task(
    description=(
        "Analyze the recent performance of the stock: {stock}. Use the MarketPulse to retrieve "
        "current price, percentage change, trading volume, and other market data."
        "Provide a summary of how the stock is performing today and highlight any key observations from the data."
        "Analyze the current performance of a given stock using real-time market data, financial indicators, and recent trends."
        "Identify key metrics such as price movement, growth signals, and risk factors to generate actionable insights and recommend whether to Buy, Sell, or Hold."
        "Provide a clear recommendation to Buy, Sell, or Hold."
    ),
    expected_output=(
        "Stock Analysis Report:\n" # (\n = new line )
        "----------------------\n"
        "Stock: {stock}\n"
        "Current Price: <value> <currency>\n"
        "Daily Change: <absolute_change> (<percentage_change>%)\n"
        "Trading Volume: <volume>\n"
        "High/Low Today: <high> / <low>\n"
        "Sector: <sector>\n\n"
        "Key Observations:\n"
        "- [Observation 1]\n"
        "- [Observation 2]\n"
        "- [Observation 3]\n"  # (\n\n = adds a blank line)
        "Actionable Recommendation: <Buy/Sell/Hold>\n"
        "Rationale: <Brief explanation of the decision based on market trends, growth signals, and risk factors>\n"

    ),
    agent = agent_analyst

)
