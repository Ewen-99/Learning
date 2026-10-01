from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()
tavily_search = TavilySearchResults(
    max_results=1, 
    search_depth="basic"
    )
search_docs = tavily_search.invoke("What is LangGraph?")
print(search_docs)
