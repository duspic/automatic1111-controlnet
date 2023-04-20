# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/resolve/main/docs/python.md

from cog import BasePredictor, Input, Path
from typing import Any

class Predictor(BasePredictor):
    def setup(self):
        pass

    def predict(self) -> Any:
        pass