# Create single and multi agents using Googles' ADK(Agent Development Kit)

# Install virtual environment for python

# Run below commands in sequence in your terminal

    python3.11 -m venv .venv
    source .venv/bin/activate
    pip install google-adk

# Test if adk installed correctly

    pip show google-adk

# Cerate first agent using adk

adk create stock_agent

 <!--Choose a model for the root agent:
1. gemini-2.5-flash
2. Other models (fill later)
Choose model (1, 2): 1
1. Google AI
2. Vertex AI
Choose a backend (1, 2): 1-->

# Run Agent Now

adk run stock_agent

# Run agent on a web browser

adk web --port 8000
