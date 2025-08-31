from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tools_agent",
    model="gemini-2.0-flash",
    description="Tool Agent",
    instruction="""
    You can use various tools to assist with tasks. It can search the web, access databases, and perform other actions as needed. You are a helpful assistant that can use the Following tools:
    - Google Search
    """,
    tools=[google_search]
)