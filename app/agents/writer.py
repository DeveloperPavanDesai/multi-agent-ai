from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from app.config import GROQ_API_KEY, GROQ_MODEL

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL
)

writer_prompt = PromptTemplate(
    input_variables=["research"],
    template="""
    You are a writer agent.

    Write a clear draft based on:
    {research}
    """
)


def writer_agent(state):
    chain = writer_prompt | llm

    response = chain.invoke({
        "research": state["research"]
    })

    return {
        "draft": response.content
    }
