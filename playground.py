from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()
phi.api = os.getenv("PHI_API")

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

app = Playground(agents=[websearch_agent,finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app(app)