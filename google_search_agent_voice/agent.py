from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

root_agent = Agent(
   # A unique name for the agent.
   name="basic_search_agent",
   # LLMs list: https://google.github.io/adk-docs/get-started/streaming/quickstart-streaming/#supported-models
   model="gemini-live-2.5-flash-preview",  # for example: model="gemini-2.0-flash-live-001" or model="gemini-2.0-flash-live-preview-04-09"
   # A short description of the agent's purpose.
   description="Agent to answer questions using Google Search.",
   # Instructions to set the agent's behavior.
   instruction="You are an expert researcher. You always stick to the facts.",
   # Add google_search tool to perform grounding with Google search.
   tools=[google_search]
)