import pandas as pd
import numpy as np
import random

# ==========================================
# 1. SETUP REALISTIC REGIONAL DATA
# ==========================================
print("⏳ Generating realistic Maharashtra admission data...")

np.random.seed(42)
num_students = 5000

# --- Features ---
cet_scores = np.random.normal(loc=85, scale=15, size=num_students) # Normal distribution around 85
cet_scores = np.clip(cet_scores, 10, 99.99) # Keep between 10 and 99.99

jee_scores = np.random.normal(loc=75, scale=20, size=num_students)
jee_scores = np.clip(jee_scores, 0, 99.99)

branches = np.random.choice(['CS', 'IT', 'EnTC', 'Mech', 'Civil'], num_students, p=[0.35, 0.25, 0.20, 0.10, 0.10])
castes = np.random.choice(['OPEN', 'OBC', 'SC', 'ST', 'EWS'], num_students, p=[0.5, 0.2, 0.15, 0.05, 0.1])
gender = np.random.choice(['Male', 'Female'], num_students)

# --- Logic to Assign Colleges (Simulating CAP Rounds) ---
admitted_colleges = []

for cet, jee, branch, caste in zip(cet_scores, jee_scores, branches, castes):
    
    # Boost score for Reserved Categories to simulate lower cutoffs
    effective_score = cet + 5 if caste in ['SC', 'ST'] else cet
    
    # 1. Top Tier (Pune/Mumbai)
    if effective_score > 99.0:
        college = "COEP Pune"
    elif effective_score > 98.5:
        college = "VJTI Mumbai"
    elif effective_score > 97.5:
        college = "PICT Pune"
    elif effective_score > 96.0:
        college = "SPIT Mumbai"
    elif effective_score > 95.0:
        college = "Walchand Sangli"
        
    # 2. High Tier
    elif effective_score > 93.0:
        college = "VIT Pune"
    elif effective_score > 91.0:
        college = "PCCOE Pune"
    elif effective_score > 89.0:
        college = "DY Patil Akurdi"
        
    # 3. Mid Tier (Solapur / Other Regions)
    elif effective_score > 85.0:
        college = "WIT Solapur"
    elif effective_score > 82.0:
        college = "Govt College Karad"
    elif effective_score > 80.0:
        college = "Sinhgad Pune"
    elif effective_score > 75.0:
        college = "Orchid Solapur"
        
    # 4. Lower Tier
    elif effective_score > 60.0:
        college = "Local City College"
    else:
        college = "Not Allotted"

    admitted_colleges.append(college)

# Create DataFrame
df = pd.DataFrame({
    'MHT_CET': np.round(cet_scores, 2),
    'JEE_Main': np.round(jee_scores, 2),
    'Branch': branches,
    'Category': castes,
    'Gender': gender,
    'Allocated_College': admitted_colleges
})

# Save to CSV
df.to_csv("maharashtra_admissions.csv", index=False)
print("✅ Data generated: 'maharashtra_admissions.csv' with 5000 records.")
print(df.head())