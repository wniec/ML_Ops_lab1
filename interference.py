# inference.py
import pickle
from typing import Iterable
from sklearn.base import ClassifierMixin
import numpy as np
from sklearn.datasets import load_iris


def load_model(filename: str = "model.pkl") -> ClassifierMixin:
    with open(filename, "rb") as f:
        model = pickle.load(f)
    return model


def predict(model: ClassifierMixin, input_features: Iterable) -> str:
    iris = load_iris()
    prediction = model.predict(np.array(input_features).reshape(1, -1))
    predicted_class = iris.target_names[prediction[0]]
    return predicted_class
