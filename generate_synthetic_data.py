
import pandas as pd
import numpy as np
import random

# Load original data
df = pd.read_csv('ehr_plus_lifestyle.csv')

# Number of synthetic records to generate
target_count = 10000
original_count = len(df)

# Calculate how many new rows we need
additional_rows = target_count - original_count

# New rows list
synthetic_rows = []

# Controlled mutation ranges for numeric columns
def mutate_numeric(val, percent=0.1):
    noise = val * percent
    return val + np.random.uniform(-noise, noise)

# Choose categorical alternatives from existing data
def random_choice_except(current, options):
    return random.choice([opt for opt in options if opt != current])

# Expand using duplication + mutation
for _ in range(additional_rows):
    row = df.sample(1).iloc[0].copy()

    # Mutate numeric columns slightly
    for col in df.select_dtypes(include=[np.number]).columns:
        if col not in ['label']:  # don't mutate target labels
            row[col] = mutate_numeric(row[col], 0.1)

    # Optionally change diagnosis
    if 'label' in df.columns:
        diagnoses = df['label'].unique()
        if np.random.rand() < 0.2:  # 20% chance to reassign label
            row['label'] = random_choice_except(row['label'], diagnoses)

    synthetic_rows.append(row)

# Create synthetic DataFrame
synthetic_df = pd.DataFrame(synthetic_rows)

# Combine original and synthetic
full_df = pd.concat([df, synthetic_df], ignore_index=True)

# Save to CSV
output_path = 'ehr_plus_lifestyle_synthetic.csv'
full_df.to_csv(output_path, index=False)

print(f"✅ Synthetic dataset saved to: {output_path}")
