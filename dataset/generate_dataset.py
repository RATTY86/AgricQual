import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

rows = 1000
data = []

for _ in range(rows):
    # 1. GENERATING REALISTIC SENSOR/LAB DATA
    # Using Normal/Exponential distributions so data clusters around averages
    
    moisture = round(np.random.normal(10, 3), 2)  # Mean 10%, SD 3%
    moisture = max(5.0, min(moisture, 25.0))      # Clip between 5% and 25%
    
    pesticide = round(np.random.exponential(0.04), 3) # Skews data toward 0
    pesticide = min(pesticide, 0.5)
    
    aflatoxin = round(np.random.exponential(4.0), 2)  # Skews data toward 0
    aflatoxin = min(aflatoxin, 50.0)
    
    microbial = int(np.random.normal(15000, 8000))
    microbial = max(500, min(microbial, 50000))
    
    heavy = round(np.random.exponential(0.05), 3)
    heavy = min(heavy, 0.5)
    
    storage = int(np.random.uniform(5, 90))
    temp = round(np.random.normal(25, 5), 1)
    
    # Let's assume most packaging is at least 'Fair'
    packaging = np.random.choice(["Good", "Fair", "Poor"], p=[0.6, 0.3, 0.1])

    # 2. 🔥 REALISTIC DECISION LOGIC (Based on EU/Codex Standards)
    score = 0

    if moisture > 12.0: score += 1       # >12% promotes mold
    if pesticide > 0.05: score += 1      # Strict EU MRL limits
    if aflatoxin > 5.0: score += 1       # Strict Aflatoxin B1 limits
    if microbial > 25000: score += 1     # High bacterial load
    if heavy > 0.1: score += 1           # Lead/Cadmium limits
    if packaging == "Poor": score += 1   # Logistics failure

    # Add randomness (simulates inspector leniency or unrecorded factors)
    noise = np.random.choice([0, 1], p=[0.85, 0.15])

    # If the batch has 2 or more strikes (including noise), it fails (0).
    compliant = 1 if (score + noise) < 2 else 0

    data.append([
        moisture, pesticide, aflatoxin, microbial,
        heavy, storage, temp, packaging, compliant
    ])

# 3. EXPORT TO CSV
df = pd.DataFrame(data, columns=[
    "moisture_content",
    "pesticide_residue",
    "aflatoxin_b1",
    "microbial_load",
    "heavy_metals",
    "storage_duration",
    "temperature",
    "packaging_integrity",
    "compliant"
])

df.to_csv("agricqual_dataset.csv", index=False)

# Print the percentage of passing vs. failing batches
print("--- Compliance Breakdown (%) ---")
print(df["compliant"].value_counts(normalize=True) * 100)
print("\n✅ Dataset 'agricqual_dataset.csv' generated successfully!")