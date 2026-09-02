from pydantic import BaseModel, Field
from agents import Agent
from openai import AsyncOpenAI
from agents import set_tracing_disabled,set_default_openai_client
from dotenv import load_dotenv
import os

load_dotenv(override=True)
model_name_gpt=os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")

MODEL_NAME = "llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollamaClient = AsyncOpenAI(base_url=OLLAMA_BASE_URL,api_key="ollama")
model = "llama3.2"
set_tracing_disabled(True)
set_default_openai_client(ollamaClient)

INSTRUCTIONS = """
You are a senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query, and some research.
Generate a comprehensive report based on the research and the query.
The final output should be in markdown format, and it should be lengthy and detailed. Aim 
for 5-10 pages of content, at least 1000 words.
"""


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(name="Writer Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=ReportData)
