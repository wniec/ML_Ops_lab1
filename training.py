import pickle
from typing import Tuple

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import ClassifierMixin


def load_data() -> Tuple[np.ndarray, np.ndarray]:
    iris = load_iris()
    X, y = iris.data, iris.target
    return X, y


def train_model() -> ClassifierMixin:
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def save_model(model: ClassifierMixin, filename: str = "model.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    model = train_model()
    save_model(model)
