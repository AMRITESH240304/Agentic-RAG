# from crewai_tools import WebsiteSearchTool
from crewai_tools import SerperDevTool

print("Serper is ready to use")

search_tool = SerperDevTool(n_results=1)