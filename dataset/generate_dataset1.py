import pandas as pd
import numpy as np

np.random.seed(42)

TOTAL_ROWS = 1000
COMPLIANT_RATIO = 0.6

num_compliant = int(TOTAL_ROWS * COMPLIANT_RATIO)
num_non = TOTAL_ROWS - num_compliant

data = []

# ----------------------------
# COMPLIANT DATA (SAFE VALUES)
# ----------------------------
for _ in range(num_compliant):

    moisture = np.random.uniform(8, 12)               # ≤ 12
    pesticide = np.random.uniform(0, 0.1)             # ≤ 0.1
    aflatoxin = np.random.uniform(0, 8)               # ≤ 8
    microbial = np.random.uniform(500, 9000)          # ≤ 10,000
    heavy = np.random.uniform(0, 0.1)                 # ≤ 0.1
    storage = np.random.uniform(5, 30)
    temp = np.random.uniform(10, 25)
    packaging = np.random.choice(["Good", "Fair"], p=[0.8, 0.2])

    compliant = 1

    data.append([
        moisture, pesticide, aflatoxin, microbial,
        heavy, storage, temp, packaging, compliant
    ])

# --------------------------------
# NON-COMPLIANT DATA (FAIL VALUES)
# --------------------------------
for _ in range(num_non):

    moisture = np.random.uniform(12.5, 25)            # > 12
    pesticide = np.random.uniform(0.11, 0.5)          # > 0.1
    aflatoxin = np.random.uniform(9, 50)              # > 8
    microbial = np.random.uniform(11000, 50000)       # > 10,000
    heavy = np.random.uniform(0.11, 0.5)              # > 0.1
    storage = np.random.uniform(30, 90)
    temp = np.random.uniform(25, 40)
    packaging = np.random.choice(["Poor", "Fair"], p=[0.7, 0.3])

    compliant = 0

    data.append([
        moisture, pesticide, aflatoxin, microbial,
        heavy, storage, temp, packaging, compliant
    ])

# ----------------------------
# CREATE DATAFRAME
# ----------------------------
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

# Shuffle dataset
df = df.sample(frac=1).reset_index(drop=True)

# Save file
df.to_csv("agricqual_dataset.csv", index=False)

# Output summary
print("✅ Dataset generated successfully!")
print("\nClass Distribution:")
print(df["compliant"].value_counts())