import pandas as pd
import numpy as np

# ==========================================================
# IT SECURITY & DATA ANALYTICS
# Fictional Financial Services Organisation
# ==========================================================

print("IT Security Data Analysis")
print("=" * 50)

# Create synthetic security data
np.random.seed(42)

departments = [
    "IT",
    "Finance",
    "Claims",
    "Underwriting",
    "Risk",
    "Operations",
    "HR",
    "Customer Service"
]

event_types = [
    "Successful Login",
    "Failed Login",
    "Suspicious Login",
    "Phishing Alert",
    "Malware Detection",
    "Unusual Network Activity",
    "Privilege Escalation"
]

severity_levels = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

sources = [
    "Microsoft Entra ID",
    "Microsoft Defender",
    "Microsoft Sentinel"
]

# Generate 500 security events
data = []

for i in range(500):

    department = np.random.choice(departments)
    event_type = np.random.choice(event_types)
    severity = np.random.choice(
        severity_levels,
        p=[0.40, 0.35, 0.20, 0.05]
    )
    source = np.random.choice(sources)

    data.append({
        "event_id": f"EV{i+1:04d}",
        "department": department,
        "event_type": event_type,
        "severity": severity,
        "source": source
    })

df = pd.DataFrame(data)

# ----------------------------------------------------------
# ANALYSIS
# ----------------------------------------------------------

print("\nTotal Security Events:")
print(len(df))

print("\nEvents by Severity:")
print(
    df["severity"]
    .value_counts()
)

print("\nEvents by Department:")
print(
    df["department"]
    .value_counts()
)

print("\nEvents by Security Source:")
print(
    df["source"]
    .value_counts()
)

# High-risk events
high_risk = df[
    df["severity"].isin(["High", "Critical"])
]

print("\nHigh/Critical Security Events:")
print(len(high_risk))

print("\nHigh-Risk Events by Department:")
print(
    high_risk["department"]
    .value_counts()
)

# Save dataset
df.to_csv(
    "security_events.csv",
    index=False
)

print("\nDataset saved successfully.")
