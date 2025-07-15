from crewai import Crew

from tasks.analyse_task import stock_analysis
from tasks.trade_task import trade_decision
from agents.analyst_agent import agent_analyst
from agents.trader_agent import agent_trader

agent_crew = Crew(
    agents = [agent_analyst,agent_trader],
    tasks = [stock_analysis,trade_decision],
    verbose = True
)
