# Bitcoin Buzz: LLM-Powered Crypto News Summarizer

This Python app fetches the latest Bitcoin news and uses a large language model (LLM) to summarize key themes and sentiment.

## Features
- Fetches real-time Bitcoin news headlines
- Summarizes using Open Source LLM models
- Simple CLI output for quick insights
- Modular CLI with multiple modes

## Setup

1. **Clone the repo**  
- get api keys, deepseek, newsdata.io, fmp, etc. whatever your preference that is compatible and put in secretes folder/config.py etc.
- run pip env and requirements.text
`pip install -r requirements.txt`

## CLI
- python main.py --mode bitcoin   # Summarize Bitcoin market data
- python main.py --mode both      # Summarize Bitcoin + LLM news
