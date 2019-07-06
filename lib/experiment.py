from pathlib import Path
import os


class Experiment:
    def __init__(self, name):
        self.name = name
        self._build_paths()

    def _build_paths(self):
        # Define folders
        self.folders = {}
        self.folders["experiment"] = Path("experiments", self.name)
        self.folders["agents"] = Path(self.folders["experiment"], "agents")
        self.folders["checkpoints"] = Path(self.folders["experiment"], "checkpoints")
        self.folders["stats"] = Path(self.folders["experiment"], "stats")
        self.folders["outputs"] = Path(self.folders["experiment"], "outputs")

        # Build paths
        for path in [
            self.folders["experiment"],
            self.folders["checkpoints"],
            self.folders["stats"],
            self.folders["outputs"],
            self.folders["agents"],
        ]:
            if not os.path.exists(path):
                os.mkdir(path)
