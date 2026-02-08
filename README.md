# multi_agent_system


This project demonstrates a multi-agent system using local LLMs with Ollama and Python. 
It covers different aspects of agent orchestration, including:

- **Agent Specialization**: Each agent has a specific role (Researcher, Writer, Reviewer).
- **Manager-Worker Architecture**: Delegating tasks from a manager to workers.
- **Shared Memory & Communication**: Agents exchange information through a shared dictionary.
- **Consensus & Conflict Resolution**: Multiple strategies to aggregate agent outputs.
- **Collaborative CrewAI Setup**: Orchestrating agents with CrewAI (local LLM).

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) local server running
- Python packages:

  pip install ollama crewai llmlite python-dotenv

