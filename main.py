from inflection import underscore
import argparse
import importlib

if __name__ == "__main__":
    # Get agent
    parser = argparse.ArgumentParser()
    parser.add_argument("agent")
    args = parser.parse_args()

    # Make the agent run!
    agent_module = importlib.import_module(("agents.{}").format(underscore(args.agent)))
    Agent = getattr(agent_module, args.agent)
    Agent().run()