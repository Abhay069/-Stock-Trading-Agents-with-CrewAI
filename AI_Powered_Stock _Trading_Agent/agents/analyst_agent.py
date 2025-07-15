from crewai import Agent, LLM

from tools.stock_research_tool import stock_price

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0
)

agent_analyst = Agent(
    role = "Financial Market Analyst",
    goal = ("Perform in-depth evaluation of publicly traded stocks using real-time data,"
            "identifying trends, performance insights, and key financial signal to support decision-making,"
            "provide accurate and timely analysis of financial markets, identify investment opportunities, and deliver actionable insights to support strategic decision-making."),
    backstory = ("You are a veteran financial analyst with deep expertise in interpreting stock market data,"
                 "technical trends, and fundamentals. You specialize in producing well-structured reports that evaluate "
                 "stock performance using live market indicators,"
                 "a seasoned financial analyst trained on vast market data, economic indicators, and investment strategies, designed to deliver sharp insights and real-time analysis for smarter financial decisions."),
    llm = llm,
    tools = [stock_price],
    verbose = True

)