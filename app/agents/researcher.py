from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from app.config import GROQ_API_KEY, GROQ_MODEL

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL
)

research_prompt = PromptTemplate(
    input_variables=["plan"],
    template="""
    You are a research agent.

    Perform detailed research based on:
    {plan}
    """
)

def researcher_agent(state):
    chain = research_prompt | llm

    response = chain.invoke({
        "plan": state["plan"]
    })

    return {
        "research": response.content
    }