# =====================
# Importing Libraries
# =====================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from skimpy import skim  # Optional for data overview

# Load dataset
dfe = pd.read_csv("/content/production_and_emissions.csv")

# Initial Data Overview
skim(dfe)

# Set plot style for consistent readability
sns.set_theme(style="whitegrid")

# =====================
# Data Cleaning and Preparation
# =====================

# Step 1: Replace commas with dots in 'Valeur (TWh)' and convert to numeric format
dfe['Valeur (TWh)'] = dfe['Valeur (TWh)'].str.replace(',', '.', regex=False).astype(float)

# Step 2: Convert 'Date' column to datetime format
dfe['Date'] = pd.to_datetime(dfe['Date'], errors='coerce')  # Coerce handles incorrect formats

# Step 3: Filter data for years between 2000 and 2023
dfe = dfe[(dfe['Date'].dt.year >= 2000) & (dfe['Date'].dt.year <= 2023)]

# Step 4: Extract year and month for additional analysis
dfe['Year'] = dfe['Date'].dt.year
dfe['Month'] = dfe['Date'].dt.month

# =====================
# Data Transformation
# =====================

# Step 5: Separate total production data into a new DataFrame
df_total = dfe[dfe['Filière'] == 'Production totale'][['Date', 'Valeur (TWh)']].rename(columns={'Valeur (TWh)': 'Total Production (TWh)'})

# Step 6: Filter out 'Production totale' from other energy types
dfe = dfe[dfe['Filière'] != 'Production totale']

# Step 7: Pivot data to organize by energy type
dfe_pivot = dfe.pivot_table(index='Date', columns='Filière', values='Valeur (TWh)', aggfunc='sum').reset_index()

# Step 8: Merge total production with pivoted data
df_final = pd.merge(df_total, dfe_pivot, on='Date', how='outer')

# Step 9: Replace NaN values with 0 for specific energy types
columns_to_replace = ['Eolien', 'Hydraulique', 'Nucléaire', 'Solaire', 'Thermique fossile', 'Thermique renouvelable et déchets']
df_final[columns_to_replace] = df_final[columns_to_replace].fillna(0)

# =====================
# Calculating CO₂ Emissions
# =====================

# Emission factors (kg CO₂/MWh) by energy source
factors = {
    'Eolien': 0,
    'Hydraulique': 10,
    'Nucléaire': 12,
    'Solaire': 40,
    'Thermique fossile': 700,
    'Thermique renouvelable et déchets': 200
}

# Step 10: Calculate CO₂ emissions for each energy type and convert to Mt
for energy, factor in factors.items():
    df_final[f'{energy}_emissions (Mt CO₂)'] = (df_final[energy] * factor * 1e6) / 1e6  # kg to Mt conversion

# Step 11: Calculate total CO₂ emissions by summing all sources
df_final['Total_CO2_Emissions (Mt CO₂)'] = df_final[[f'{energy}_emissions (Mt CO₂)' for energy in factors.keys()]].sum(axis=1)

# =====================
# Renaming Columns and Final Adjustments
# =====================

# Step 12: Rename energy columns for clarity
df_final.rename(columns={
    'Eolien': 'Eolien (TWh)',
    'Hydraulique': 'Hydraulique (TWh)',
    'Nucléaire': 'Nucléaire (TWh)',
    'Solaire': 'Solaire (TWh)',
    'Thermique fossile': 'Thermique fossile (TWh)',
    'Thermique renouvelable et déchets': 'Thermique renewable and waste (TWh)',
}, inplace=True)

# Step 13: Include Year and Month columns for analysis
df_final['Year'] = df_final['Date'].dt.year
df_final['Month'] = df_final['Date'].dt.month

# Step 14: Display the final cleaned DataFrame
print(df_final.head())

# =====================
# Data Visualization
# =====================

# 1. Total Energy Production Over Time
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_final, x='Date', y='Total Production (TWh)', color='blue')
plt.title("Total Energy Production (TWh) Over Time")
plt.xlabel("Date")
plt.ylabel("Total Production (TWh)")
plt.show()

# 2. Total CO₂ Emissions Over Time
plt.figure(figsize=(14, 7))
sns.lineplot(data=df_final, x='Date', y='Total_CO2_Emissions (Mt CO₂)', color='red')
plt.title("Total CO₂ Emissions (Mt CO₂) Over Time")
plt.xlabel("Date")
plt.ylabel("Total CO₂ Emissions (Mt CO₂)")
plt.show()

# 3. Energy Production by Type (Stacked Area Chart)
plt.figure(figsize=(14, 7))
energy_types = ['Eolien (TWh)', 'Hydraulique (TWh)', 'Nucléaire (TWh)', 'Solaire (TWh)', 'Thermique fossile (TWh)', 'Thermique renewable and waste (TWh)']
df_final[energy_types].plot.area(stacked=True, alpha=0.6, figsize=(14, 7), colormap='tab20')
plt.title("Energy Production by Type Over Time")
plt.xlabel("Date")
plt.ylabel("Production (TWh)")
plt.legend(title="Energy Source")
plt.show()

# 4. CO₂ Emissions by Energy Type (Stacked Area Chart)
emission_types = [f'{energy}_emissions (Mt CO₂)' for energy in factors.keys()]
df_final[emission_types].plot.area(stacked=True, alpha=0.6, figsize=(14, 7), colormap='tab20')
plt.title("CO₂ Emissions by Energy Type Over Time")
plt.xlabel("Date")
plt.ylabel("CO₂ Emissions (Mt CO₂)")
plt.legend(title="Emission Source")
plt.show()

# =====================
# Exporting Cleaned Data
# =====================

# Save the cleaned DataFrame to CSV with semicolon delimiter
df_final.to_csv('cleaned_data_for_power_bi.csv', index=False, sep=';')