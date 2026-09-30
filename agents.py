from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from tools import web_search, scrape_url
import os
from dotenv import load_dotenv
load_dotenv()

GROQ_MODEL = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

groq_llm = ChatGroq(model=GROQ_MODEL, temperature=0, max_tokens=800)
ollama_llm = ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=0)
llm = groq_llm.with_fallbacks(fallbacks=[ollama_llm], exceptions_to_handle=(Exception,))

# 1st Agent
def build_search_agent():
    return create_agent(
        model= llm,
        tools=[web_search]
    )


# 2nd agent
def build_reader_agent():
    return create_agent(
        model= llm,
        tools= [scrape_url]
    )

# writer chain
writer_prompt = ChatPromptTemplate.from_messages([
   ("system", "You are an expert research writer. Write clear, structured and insightful report"),
   ("human", """Write a detailed research report on the topic below.

   Topic : {topic}
   
   Research Gathered:
   {research}

   Structure the report as:
   - Introduction
   - Key Findings (Minimum 3 well-explained points)
   - Conclusion
   - Sources (list all URLs Found in the research)

   Be detailed, factual and professional.
 
   """)
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic_chain

critic_prompt = ChatPromptTemplate.from_messages([
("system", "You are a sharp and constructive research critic. Be honest and specific."),
("human", """

Report :
{report}

Response in this exact format:

Score : x/10

Strenghs:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
.....
""")
])


critic_chain = critic_prompt | llm | StrOutputParser()

