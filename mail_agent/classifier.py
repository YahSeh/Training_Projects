"""Simple email classifier.

This module expects a scikit-learn model stored with joblib. The model
should output labels such as ``urgent`` or ``pub``. If no model file is
found, the classifier returns ``unknown`` for all inputs.
"""

from pathlib import Path
from typing import Optional

import joblib

MODEL_PATH = Path(__file__).with_name("classifier.joblib")


class EmailClassifier:
    """Wrapper around a scikit-learn model."""

    def __init__(self, model_path: Path = MODEL_PATH) -> None:
        self.model_path = model_path
        if model_path.exists():
            self.model = joblib.load(model_path)
        else:
            self.model = None

    def predict(self, text: str) -> str:
        """Predict a label for the given text."""
        if self.model is None:
            return "unknown"
        return str(self.model.predict([text])[0])
