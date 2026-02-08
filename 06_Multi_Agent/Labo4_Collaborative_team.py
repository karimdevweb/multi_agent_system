from crewai import Agent, Crew , Task
from ollama import chat
import os
from dotenv import load_dotenv
from crewai.llm import LLM  
from langchain_openai import ChatOpenAI



#  install llmlite

# CrewAI agents
researcher_agent = Agent(
    role="Researcher",
    goal="Collect black clover information",
    backstory="You are an AI researcher collecting facts and data.",
  
    llm=LLM(model="ollama/mistral:latest", base_url="http://localhost:11434")
)

writer_agent = Agent(
    role="Writer",
    goal="Write a summary",
    backstory="You are an AI writer creating clear summaries from data.",
   
    llm=LLM(model="ollama/mistral:latest", base_url="http://localhost:11434")
)

reviewer_agent = Agent(
    role="Reviewer",
    goal="Proofread and clarify the summary",
    backstory="You are an AI reviewer improving clarity and correctness.",
   
    llm=LLM(model="ollama/mistral:latest", base_url="http://localhost:11434")
)


tasks = [
    Task(
        description="Collect information about Black Clover",
        expected_output="A factual paragraph about Black Clover",
        agent=researcher_agent
    ),
    Task(
        description="Summarize the collected information",
        expected_output="A short and clear summary",
        agent=writer_agent
    ),
    Task(
        description="Improve clarity and correctness of the summary",
        expected_output="A clean, well-written final summary",
        agent=reviewer_agent
    )
]

crew = Crew(
    agents=[researcher_agent, writer_agent, reviewer_agent],
    tasks=tasks,
    verbose=True
)

result = crew.kickoff()
print(result)


