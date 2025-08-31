from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

# we can create and give it as a tool to adk agents
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tools_agent",
    model="gemini-2.0-flash",
    description="Tool Agent",
    instruction="""
    You can use various tools to assist with tasks. It can search the web, access databases, and perform other actions as needed. You are a helpful assistant that can use the Following tools:
    - Get Current Time
    """,
    # tools=[google_search]
    tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)