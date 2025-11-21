# pip install langchain-core
# pip install langchain-community
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

import os
import sys
sys.path.append("..")
import google.cloud.logging

from google.adk import Agent
from google.adk.tools.langchain_tool import LangchainTool # import

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from dotenv import load_dotenv

load_dotenv()
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

root_agent = Agent(
    name="lanchgain_tool_agent_Wiki",
    model='gemini-2.5-flash',
    description="Answers questions using Wikipedia.",
    instruction="""WIkipedia research on behalf of the user.""",
    tools = [
        LangchainTool(
            tool=WikipediaQueryRun(
              api_wrapper=WikipediaAPIWrapper()
            )
        )
    ]
)