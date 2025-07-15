from dotenv import load_dotenv    # For loading API key

from crew import agent_crew

load_dotenv()

def run(stock: str):
    result = agent_crew.kickoff(inputs={"stock": stock}) # It passes the stock name into the AI pipeline (inputs={"stock": stock}), triggering tasks like analysis and trading decision.
    # whatever variable we are creating in (tasks directory) we have to mention that variable in input={}                                                      # .kickoff(...): This is a method that starts or "kicks off" the AI pipeline (task execution).
    print(result)

if __name__ =="__main__":
    run("GOOGL")
