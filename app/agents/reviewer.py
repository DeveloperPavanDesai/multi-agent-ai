from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from app.config import GROQ_API_KEY, GROQ_MODEL

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL
)

review_prompt = PromptTemplate(
    input_variables=["draft"],
    template="""
    You are a review agent.

    Review and improve this draft:
    {draft}
    """
)


def reviewer_agent(state):
    chain = review_prompt | llm

    response = chain.invoke({
        "draft": state["draft"]
    })

    return {
        "final": response.content
    }
