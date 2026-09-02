import asyncio
# from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import (
    Agent,
    Runner,
    set_tracing_disabled,
    set_default_openai_client,
)

# load_dotenv(override=True)

set_tracing_disabled(True)

client = AsyncOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)

set_default_openai_client(client)

agent = Agent(
    name="Jokester",
    instructions="You are a joke teller",
    model="llama3.2",
)

async def agentCall():
    result = await Runner.run(
        agent,
        "Tell a joke about Autonomous AI Agents"
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(agentCall())