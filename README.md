Intelligent Query Routing Chatbot
This repository contains a LangGraph-powered chatbot that intelligently routes user queries to specialized AI agents based on intent. Instead of relying on a single prompt for all tasks, the system efficiently directs queries to the most suitable agent, ensuring better accuracy, efficiency, and modularity.

🔍 Key Features:
Dynamic Query Routing: Routes user requests to the correct agent based on keywords and intent.
Multi-Agent System: Supports multiple AI agents, each handling a specific task.
Streamlit Interface: Provides an interactive web UI for user input and response display.
Scalable & Modular: Easily add new agents without modifying the core routing logic.
🤖 Supported AI Agents:
📚 General Knowledge Agent – Answers factual questions.
📝 Summarization Agent – Condenses long text into key insights.
🔍 Entity Extraction Agent – Identifies names, dates, emails, and other key entities.
🚀 How It Works:
User Input: The user enters a query, prefixed with keywords like "Summarize", "Extract entities", or "General knowledge".
Routing Engine: LangGraph analyzes the query and directs it to the correct agent.
Agent Execution: The selected agent processes the request and returns a response.
Output Display: The chatbot presents the response via Streamlit.
⚡ Tech Stack:
LangGraph – For building the multi-agent workflow.
LangChain – To power AI-driven responses.
Streamlit – For a simple and interactive user interface.
Python – Backend logic and AI processing.
🎯 Why Use This Chatbot?
Specialized Task Handling: Ensures accurate results by routing tasks to dedicated agents.
Better Efficiency: Reduces unnecessary LLM calls by leveraging external tools when needed.
Scalability: Easily extendable to support additional AI capabilities.
🛠️ Getting Started:
Clone the repo, install dependencies, and launch the chatbot with Streamlit. See the README for detailed setup instructions! 🚀







