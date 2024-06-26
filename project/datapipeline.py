import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
# Load the datasets
economy_df = pd.read_csv('https://opendata.com.pk/dataset/4acccdea-baea-4bc7-8499-94835f352059/resource/5eed074c-c7ed-427a-816c-8482edb070a1/download/economy-and-growth_pak.csv')
climate_df = pd.read_csv('https://opendata.com.pk/dataset/ececec4f-1835-4278-ae0c-5bd7c4ded652/resource/492b13f4-5b47-4437-a680-4e1b965c1ea2/download/climate-change-indicators-for-pakistan-1.csv')

# Clean the data by removing the first row (header information) and resetting the index
economy_df = economy_df[1:].reset_index(drop=True)
climate_df = climate_df[1:].reset_index(drop=True)

# Convert the Year and Value columns to numeric
economy_df['Year'] = pd.to_numeric(economy_df['Year'])
economy_df['Value'] = pd.to_numeric(economy_df['Value'], errors='coerce')

climate_df['Year'] = pd.to_numeric(climate_df['Year'])
climate_df['Value'] = pd.to_numeric(climate_df['Value'], errors='coerce')

# Pivot the data to have indicators as columns
economy_pivot = economy_df.pivot_table(index='Year', columns='Indicator Name', values='Value')
climate_pivot = climate_df.pivot_table(index='Year', columns='Indicator Name', values='Value')

# Merge the two datasets on the Year column
merged_df = pd.merge(economy_pivot, climate_pivot, on='Year', how='inner')

# Define the selected indicators
selected_indicators = [
    'Agricultural land (sq. km)',
    'Urban population',
    'CO2 emissions (kt)',
    'Electric power consumption (kWh per capita)',
    'Forest area (sq. km)',
    'Cereal yield (kg per hectare)',
    'Inflation, consumer prices (annual %)'

]

# Filter the merged DataFrame to include only the selected indicators
merged_df = merged_df[selected_indicators]
# Filter the data to include only the years between 1970 and 2014
merged_df = merged_df[(merged_df.index >= 1970) & (merged_df.index <= 2014)]
scaler = StandardScaler()
scaled_df = pd.DataFrame(scaler.fit_transform(merged_df.dropna()), columns=merged_df.columns, index=merged_df.dropna().index)


# %% [markdown]
# # Load

# %%
scaled_df.to_csv('data/data.csv')

# %%


# %%



