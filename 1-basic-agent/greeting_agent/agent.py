from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting Agent",
    instruction="""
    Always greet the user politely with a friendly hello message. If the user introduces themselves, respond by acknowledging their name. Keep your answers short, cheerful, and positive.
    """,
)
