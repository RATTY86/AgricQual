import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier

import joblib

# ----------------------------
# LOAD DATA
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "dataset", "agricqual_dataset.csv")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

# ----------------------------
# PREPROCESSING
# ----------------------------

# Encode packaging
le = LabelEncoder()
df["packaging_integrity"] = le.fit_transform(df["packaging_integrity"])

X = df.drop("compliant", axis=1)
y = df["compliant"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# ----------------------------
# MODEL DEFINITIONS (TUNED)
# ----------------------------

models = {

    "Logistic Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(
            C=1.0,
            max_iter=1000,
            class_weight="balanced"
        ))
    ]),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=5,
        min_samples_split=10,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=150,
        max_depth=10,
        random_state=42
    ),

    "SVM": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVC(
            kernel="rbf",
            C=1.0,
            gamma="scale"
        ))
    ]),

    "XGBoost": XGBClassifier(
        n_estimators=150,
        learning_rate=0.1,
        max_depth=5,
        subsample=0.8,
        random_state=42,
        eval_metric="logloss"
    )
}

results = []

# ----------------------------
# TRAIN & EVALUATE
# ----------------------------
'''
for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"{name} Performance:")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")

    results.append((name, f1)) '''

for name, model in models.items():
    print(f"\nTraining {name}...")

    # =========================
    # K-FOLD CROSS VALIDATION
    # =========================
    cv_scores = cross_val_score(model, X, y, cv=5)

    print(f"{name} Cross-Validation Scores: {cv_scores}")
    print(f"{name} Mean CV Accuracy: {cv_scores.mean():.4f}")

    # =========================
    # NORMAL TRAINING (UNCHANGED)
    # =========================
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(f"{name} Performance:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))
# ----------------------------
# SELECT BEST MODEL
# ----------------------------

best_model_name = max(results, key=lambda x: x[1])[0]
best_model = models[best_model_name]

print("\nBest Model:", best_model_name)

# Retrain best model
best_model.fit(X_train, y_train)

# Save model
MODEL_PATH = os.path.join(BASE_DIR, "model", "agricqual_model.pkl")
joblib.dump(best_model, MODEL_PATH)

print("Model saved successfully:", MODEL_PATH)






