# AI Research Studio

This project is a multi-agent research assistant that searches the web, reads a relevant webpage, writes a research report, and critiques the generated output.

It combines:
- web search
- webpage scraping
- AI-powered structured writing
- AI-based review and critique

The system is designed for research and educational workflows and can be run from a terminal or through a Streamlit web interface.

## Features

- Search for recent and relevant information on a topic
- Select a promising result from search output
- Scrape the selected webpage for deeper content
- Combine search and scraped content into a single research context
- Generate a structured research report
- Critique the report for quality and accuracy
- Run the workflow through a simple Streamlit dashboard

## Tech Stack

- Python
- LangChain
- Groq
- Ollama
- Tavily
- BeautifulSoup
- Streamlit

## Project Structure

- app.py – Streamlit user interface
- pipeline.py – main research pipeline
- agents.py – model and agent definitions
- tools.py – search and scraping tools
- pyproject.toml – project dependencies and metadata

## How it works

1. The user enters a topic.
2. The search agent looks up recent and relevant information.
3. The reader agent reviews the search output and chooses a promising source.
4. The scraper extracts deeper content from the selected page.
5. The writer agent creates a structured research report.
6. The critic agent reviews the report and provides feedback.

## Prerequisites

Before running the project, make sure you have:

- Python 3.12 or newer
- A valid Groq API key
- Tavily API key
- Ollama installed locally for fallback usage
- Internet access for search and scraping

## Environment Setup

Create a .env file in the root directory with variables similar to the following:

```bash
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=qwen/qwen3.8-27b
TAVILY_API_KEY=your_tavily_key
OLLAMA_MODEL=qwen3:4b
OLLAMA_BASE_URL=http://localhost:11434
```

## Installation

Install the project dependencies using:

```bash
uv sync
```

If needed, install the UI and fallback package explicitly:

```bash
uv add streamlit
uv add langchain-ollama
```

## Run the pipeline from terminal

```bash
python pipeline.py
```

Then enter a topic when prompted.

## Run the Streamlit UI

```bash
uv run streamlit run app.py
```

Open the local Streamlit URL displayed in the terminal.

## Example Use Cases

- market and business research
- trend exploration
- educational topic summaries
- technology updates
- general research workflows

## Notes

- This project is intended for research and educational purposes.
- Some model providers may rate-limit requests depending on usage or quota.
- Local Ollama can be used as a fallback when Groq is unavailable or rate-limited.
- Generated reports should be reviewed for factual correctness before being treated as final research output.

## Limitations

- Search results depend on the current web state and source quality.
- Web scraping depends on site structure and accessibility.
- AI-generated reports may include cautious wording depending on the model and prompt.
- Final output should be checked for completeness, citations, and accuracy.

## License

This project is intended for educational and learning use.
