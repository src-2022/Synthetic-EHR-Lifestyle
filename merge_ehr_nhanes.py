import pandas as pd
import numpy as np

# Load the datasets
ehr_df = pd.read_csv("ehr_dataset.csv")
lifestyle_df = pd.read_csv("merged_nhanes_lifestyle.csv")

# Match each EHR patient by closest age in NHANES
ehr_ages = ehr_df['Age'].values
nhanes_ages = lifestyle_df['RIDAGEYR'].values

# Find the index of the closest age match
matched_indices = [np.argmin(np.abs(nhanes_ages - age)) for age in ehr_ages]

# Extract matched lifestyle rows
matched_lifestyle = lifestyle_df.iloc[matched_indices].reset_index(drop=True)

# Drop columns that will duplicate or conflict
matched_lifestyle = matched_lifestyle.drop(columns=['SEQN', 'RIDAGEYR'])

# Combine EHR with matched lifestyle data
ehr_df_reset = ehr_df.reset_index(drop=True)
full_merged_df = pd.concat([ehr_df_reset, matched_lifestyle], axis=1)

# Save the result
output_filename = "ehr_plus_lifestyle.csv"
full_merged_df.to_csv(output_filename, index=False)

print(f"✅ Merged dataset saved to: {output_filename}")

