# Multi-Agent AI (FastAPI + LangGraph + Groq)

A simple multi-agent research API built with FastAPI and LangGraph.

## What it does

This app runs a 4-step agent pipeline for a user query:

1. `planner` creates a plan from the input query.
2. `researcher` expands the plan into research notes.
3. `writer` converts research notes into a draft.
4. `reviewer` improves the draft and returns final output.

The API returns the `final` response from the graph state.

## Tech stack

- FastAPI
- LangGraph
- LangChain
- Groq (`langchain-groq`)
- Python dotenv

## Project structure

```text
app/
  agents/
    planner.py
    researcher.py
    writer.py
    reviewer.py
  graph/
    workflow.py
  state/
    state.py
  config.py
  main.py
```

## State flow

Graph state keys:

- `query`
- `plan`
- `research`
- `draft`
- `final`

Current execution order in `workflow.py`:

`START -> planner -> researcher -> writer -> reviewer -> END`

## Prerequisites

- Python 3.12+
- A Groq API key

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment variables

Create a `.env` file in project root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant

LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=multi-agent-ai
```

Notes:

- `GROQ_MODEL` is optional; default is `llama-3.1-8b-instant`.
- `LANGCHAIN_*` vars are optional, useful for tracing/observability.

## Run the API

Always run with the same Python where dependencies are installed:

```bash
source venv/bin/activate
python -m uvicorn app.main:app --reload
```

Server:

- `http://127.0.0.1:8000`

## Test the endpoint

Use query param:

```bash
curl -X POST "http://127.0.0.1:8000/research?query=car"
```

Expected response shape:

```json
{
  "response": "..."
}
```

## Common issues

- `ModuleNotFoundError: No module named 'langchain_groq'`
  - Cause: running with a different Python/interpreter than your venv.
  - Fix: use `python -m uvicorn ...` after activating `venv`.

- `groq.GroqError: ... GROQ_API_KEY ...`
  - Cause: missing/invalid `GROQ_API_KEY`.
  - Fix: set key in `.env` and restart server.

- `KeyError` for state fields (`plan`, `research`, `draft`, `final`)
  - Cause: graph order or node return keys mismatch.
  - Fix: ensure each agent returns the key needed by the next node.
