from crewai import Task
from agents.trader_agent import agent_trader

trade_decision = Task(
    description= (
        "Use live market data and stock performance indicators for {stock} to make a strategic trading decision."
        "Assess key factors such as current price, daily change percentage, volume trends, and recent momentum."
        "Analyze the stock: {stock} using real-time market data and key financial indicators. "
        "Based on price movement, growth signals, and risks, decide whether to Buy, Sell, or Hold. "
        "Provide a brief, reasoned explanation for your decision."
    ),
    expected_output=(
        "Trade Decision Report:\n"
        "----------------------\n"
        "Stock: {stock}\n"
        "Current Price: <value> <currency>\n"
        "Daily Change: <absolute_change> (<percentage_change>%)\n"
        "Volume Trend: <increasing/stable/decreasing>\n"
        "Recent Momentum: <bullish/bearish/neutral>\n\n"
        "Decision: <Buy/Sell/Hold>\n"
        "Reasoning: <One or two lines explaining the decision based on data trends and market signals>\n"

    ),
    agent = agent_trader

)