# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task,before_kickoff, after_kickoff
from crewai_tools import SerperDevTool
from service.crewai.tools.vector_search import my_secret_code_tool
from config import settings

search_tool = SerperDevTool(n_results=1)


llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.5,
    api_key=settings.GEMINI_API_KEY
)

@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  @agent
  def researcher(self) -> Agent:
    return Agent(
      config=self.agents_config['researcher'],
      verbose=True,
      tools=[my_secret_code_tool,search_tool],
      llm=llm
    )

  @agent
  def reporting_analyst(self) -> Agent:
    return Agent(
      config=self.agents_config['reporting_analyst'],
      llm=llm,
      verbose=True
    )

  @task
  def research_task(self) -> Task:
    return Task(
      config=self.tasks_config['research_task'],
    )

  @task
  def reporting_task(self) -> Task:
    return Task(
      config=self.tasks_config['reporting_task'],
      output_file='output/report.md' 
    )
  @crew
  def crew(self) -> Crew:
    """Creates the LatestAiDevelopment crew"""
    return Crew(
      agents=self.agents, 
      tasks=self.tasks,
      process=Process.sequential,
      verbose=True,
    )
  @before_kickoff
  def before_kickoff_function(self, inputs):
    print(f"Before kickoff function with inputs: {inputs}")
    return inputs 

  @after_kickoff
  def after_kickoff_function(self, result):
    print(f"After kickoff function with result: {result}")
    return result 
    
