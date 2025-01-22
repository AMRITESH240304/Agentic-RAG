from service.crewai.main_crew import LatestAiDevelopmentCrew

def run(topic:str):
  """
  Run the crew.
  """
  inputs = {
    'topic': topic
  }
  return LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)