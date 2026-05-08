from pathlib import Path
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "decision_tree_model.pkl"

FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]


class Rose:
    def __init__(self):
        pass

    def model_exists(self):
        return _MODEL_PATH.exists()

    def train_and_save(self):
        df = pd.read_csv(_CSV_PATH)

        df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
        df["Age"] = df["Age"].fillna(df["Age"].median())

        X = df[FEATURES]
        y = df["Survived"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = DecisionTreeClassifier(random_state=42)
        model.fit(X_train, y_train)

        joblib.dump(model, _MODEL_PATH)

        accuracy = model.score(X_test, y_test)
        return {"model_path": str(_MODEL_PATH), "accuracy": round(accuracy, 4)}
