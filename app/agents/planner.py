from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from app.config import GROQ_API_KEY, GROQ_MODEL

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL
)

planner_prompt = PromptTemplate(
    input_variables=["query"],
    template="""
    You are a planning agent.

    Create a plan for:
    {query}
    """
)

def planner_agent(state):
    chain = planner_prompt | llm

    response = chain.invoke({"query": state["query"]})

    return {
        "plan": response.content
    }