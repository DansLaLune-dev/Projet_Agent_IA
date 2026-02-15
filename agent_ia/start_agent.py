import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

import mlflow

from agent_ia.utils.state import workflow_create
mlflow.langchain.autolog()

from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

def main():
    memory = MemorySaver()
    app = workflow_create(memory)
    config = {"configurable": {"thread_id": "session_finale_01"}}

    inputs = {"messages": [("user", "Lance le rapport.")]}
    
    while True:
        for event in app.stream(inputs, config=config, stream_mode="values"):
            if "messages" in event and event["messages"]:
                last_msg = event["messages"][-1]
                if last_msg.type == "ai" and last_msg.content:
                    print(f"\n[AI] : {last_msg.content}")

        user_input = input("\n[Humain] > ")
        if user_input.lower() in ["exit", "quitter"]: break

        inputs = Command(resume=user_input)

if __name__ == "__main__":
    main()