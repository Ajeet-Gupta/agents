from agents import Agent, WebSearchTool, ModelSettings,set_default_openai_client,set_tracing_disabled
from dotenv import load_dotenv
from openai import AsyncOpenAI
# import os

# load_dotenv(override=True)
# MODEL_NAME_TEMP = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")

MODEL_NAME = "llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollamaClient = AsyncOpenAI(base_url=OLLAMA_BASE_URL,api_key="ollama")
model = "llama3.2"
set_tracing_disabled(True)
set_default_openai_client(ollamaClient)

INSTRUCTIONS = """
You are a research assistant. Given a search term, you search the web for that term and 
produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

# settings = ModelSettings(tool_choice="required")
# tools = [WebSearchTool()]

search_agent = Agent(name="Search Agent", instructions=INSTRUCTIONS, model=MODEL_NAME)