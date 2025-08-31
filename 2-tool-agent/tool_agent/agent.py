from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
import random

# we can create and give it as a tool to adk agents --- Current time function
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

# This is the function for the random joke generator --- custom function
def get_random_joke() -> dict:
    """
    Return a random joke from a predefined list of jokes.

    Returns:
        dict: A dictionary containing a single key "joke" with the joke text as its value.
    """
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? It caught a virus!",
        "Why was the math book sad? Because it had too many problems!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]

    return {
        "joke": random.choice(jokes)
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
    # tools=[get_current_time],
    tools=[get_random_joke],
    
    # tools=[google_search, get_current_time], # <--- Doesn't work
)