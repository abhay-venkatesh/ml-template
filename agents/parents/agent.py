from inflection import underscore
from lib.experiment import Experiment
from pathlib import Path
import os
import shutil


class Agent:
    def __init__(self):
        self.experiment = Experiment(underscore(self.__class__.__name__))
        self._save_agent_state()

    def run(self):
        raise NotImplementedError("Implement this method.")

    def _save_agent_state(self):
        agent_file = Path("agents", underscore(self.__class__.__name__) + ".py")
        if not os.path.exists(agent_file):
            raise RuntimeError(str(agent_file) + " in wrong folder.")
        shutil.copy2(agent_file, self.experiment.folders["agents"])

        # Save parent class states too
        for base in self.__class__.__bases__:
            if base.__name__ != "object":
                agent_file_name = underscore(base.__name__) + ".py"
                copied = False
                for agent_file in [
                    Path("agents", agent_file_name),
                    Path("agents", "parents", agent_file_name),
                    Path("agents", "deprecated", agent_file_name),
                ]:
                    if os.path.exists(agent_file):
                        shutil.copy2(agent_file, self.experiment.folders["agents"])
                        copied = True

                if not copied:
                    raise RuntimeError(str(agent_file_name) + " in wrong folder.")
