from pydantic import BaseModel, Field
from agents import Agent,set_tracing_disabled,set_default_openai_client
# import os
from openai import AsyncOpenAI
# from dotenv import load_dotenv
# load_dotenv(override=True)

# MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")
HOW_MANY_SEARCHES = 5
# int(os.getenv("HOW_MANY_SEARCHES", 5))

MODEL_NAME = "llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollamaClient = AsyncOpenAI(base_url=OLLAMA_BASE_URL,api_key="ollama")
model = "llama3.2"
set_tracing_disabled(True)
set_default_openai_client(ollamaClient)

INSTRUCTIONS = f"""
You are a research assistant. Given a user query, come up with a set of web searches
to perform to best answer the query. Output {HOW_MANY_SEARCHES} terms to query for.
"""

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    
planner_agent = Agent(name="Planner Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=WebSearchPlan)