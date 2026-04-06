# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading dataset...")
df = pd.read_csv("dataset/agricqual_dataset.csv")

# 1. Preprocessing Pipeline
# Convert categorical 'packaging_integrity' to numbers so the ML model can read it
packaging_map = {"Good": 2, "Fair": 1, "Poor": 0}
df['packaging_integrity'] = df['packaging_integrity'].map(packaging_map)

# Separate features (X) and target (y)
X = df.drop("compliant", axis=1)
y = df["compliant"]

# 2. Train the Random Forest Model
print("Training Random Forest Model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 3. Save the model (Matches Section 4.3.2)
joblib.dump(model, "rf_agricqual_model.joblib")
print("✅ Model trained and saved successfully as 'rf_agricqual_model.joblib'")