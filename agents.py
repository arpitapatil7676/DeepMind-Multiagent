from tools import (
    web_scraping_urls,
    web_search_tool
)

from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
import os

print("OPENAI KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)
def _build_search_agent():
    return create_react_agent(
        model = llm,
        tools= [web_search_tool]
    )

def _build_scraping_agent():
    return create_react_agent(
        model = llm,
        tools= [web_scraping_urls]
    )

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

    Topic: {topic}

    Research Gathered:
    {research}

    Structure the report as:
    - Introduction
    - Key Findings (minimum 3 well-explained points)
    - Conclusion
    - Sources (list all URLs found in the research)

    Be detailed, factual and professional.""")
])


writer_chain_ = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()