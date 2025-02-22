from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


websearch_agent = Agent(
    name="websearch",
    role="search",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[ DuckDuckGo()],
    instructions=["alwways include source and date in your search"],
    markdown=True,
    show_tool_calls=True
    )

finance_agent = Agent(
    name="websearch",
    role="search",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[ YFinanceTools(stock_fundamentals=True, company_news=True, analyst_recommendations=True, technical_indicators=True)],
    instructions=["use table to display data"],
    markdown=True,
    show_tool_calls=True
    )
mukti_ai_agent = Agent(
    team=[websearch_agent,finance_agent],
    instructions=["use table to display data","alwways include source and date in your search"],
    markdown=True,
    show_tool_calls=True
)
mukti_ai_agent.print_response("stock price of apple")