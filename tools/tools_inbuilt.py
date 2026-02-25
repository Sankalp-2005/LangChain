from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

#------------------------Web search Tool-------------------------------

search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke("What is the weather in Hyderabad")
print(result)

#------------------------Shell Tool-------------------------------

shell_tool=ShellTool()
result = shell_tool.invoke("pip install flask")
print(result)