# File: calculate_alos.py
import pandas as pd

# Load hospital patient data from hospital_data.csv
df = pd.read_csv('hospital_data.csv')

# Convert admission_date and discharge_date to datetime
df['admission_date'] = pd.to_datetime(df['admission_date'])
df['discharge_date'] = pd.to_datetime(df['discharge_date'])

# Calculate Length of Stay (LOS) for each patient
df['length_of_stay'] = (df['discharge_date'] - df['admission_date']).dt.days

# Filter data for the past year
one_year_ago = pd.Timestamp.now() - pd.DateOffset(years=1)
df_last_year = df[df['admission_date'] >= one_year_ago]

# Group by department and calculate the average length of stay (ALOS)
alos_by_department = df_last_year.groupby('department')['length_of_stay'].mean().reset_index()

# Rename the columns for clarity
alos_by_department.columns = ['Department', 'Average Length of Stay']

# Save the result to alos_by_department.csv
alos_by_department.to_csv('alos_by_department.csv', index=False)

# Print the result
print(alos_by_department)
