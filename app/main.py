from fastapi import FastAPI
from app.graph.workflow import app as graph_app

app = FastAPI()

@app.post("/research")
def research(query: str):

    result = graph_app.invoke({"query": query})

    return {
        "response": result["final"]
    }