from agents import Agent, function_tool, ModelSettings,set_tracing_disabled,set_default_openai_client
from messenger import send_email, push
from openai import AsyncOpenAI
# import os
# from dotenv import load_dotenv
# load_dotenv(override=True)

# MODEL_NAME_TEMP = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")
USE_EMAIL = "true"

MODEL_NAME = "llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollamaClient = AsyncOpenAI(base_url=OLLAMA_BASE_URL,api_key="ollama")
model = "llama3.2"
set_tracing_disabled(True)
set_default_openai_client(ollamaClient)

settings = ModelSettings(tool_choice="required")

@function_tool
def send_email_tool(subject: str, text_body: str, html_body: str) -> str:
    """
    Send out an email with the given subject and body
    
    Args:
        subject: The subject of the email
        text_body: The body of the email as plain text
        html_body: The HTML body of the email
    """
    if USE_EMAIL:
        send_email_demo(subject, text_body, html_body)
    else:
        push(f"Subject: {subject}\n\n{text_body}")
    return "Email sent successfully"


INSTRUCTIONS = """
You are provided with a detailed report. Use your tool to send an email, converting the report into
a clean, well presented HTML email with an appropriate subject line.
"""

email_agent = Agent(name="Email Agent", instructions=INSTRUCTIONS, tools=[send_email_tool], model=MODEL_NAME, model_settings=settings)


def send_email_demo(subject, text_body, html_body):
    print(f"This message will sent over the email=> but I am printing here this msg..\n\n")
    print(f"Subject: {subject} AND Text Body: {text_body}")
    print(f"Body: {html_body}")
