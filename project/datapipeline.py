# %% [markdown]
# # Impact of Climate change on various species of trees in Frankfurt
# 

# %% [markdown]
# Coorelation of Planation year temperature with the crown diameter, trunk height etc of various species of trees?
# How it varies across different species of plants?

# %% [markdown]
# ## Extraction from 2 CSV files

# %%
#import required dependencies here:
import pandas as pd
#from config import db_password

# %%
#read csv 1
df1 = pd.read_csv("https://offenedaten.frankfurt.de/dataset/73c5a6b3-c033-4dad-bb7d-8783427dd233/resource/257690bb-f40a-4e3a-93da-1310214f392f/download/baumauswahl.csv",sep = ';')


# %%
url='https://github.com/omerjadoon/TemperatureData/raw/main/temperature.csv.zip'
df2 = pd.read_csv(url)


# %% [markdown]
# # Transform

# %%
frankfurt_df = df2[df2['City'] == 'Frankfurt']


# %%
#drop last 3 columns
frankfurt_df.drop(frankfurt_df.columns[[2,3,4,5,6]], axis=1, inplace=True)


# %%
age_nan_count = frankfurt_df['AverageTemperature'].isna().sum()

print(f"Number of NaN values in 'Age' column: {age_nan_count}")

# %%
df2_cleaned = frankfurt_df.dropna(subset=['AverageTemperature'])


# %%
df2_cleaned['dt'] = pd.to_datetime(df2_cleaned['dt'])

# Step 3: Extract the year from the 'dt' column
df2_cleaned['Year'] = df2_cleaned['dt'].dt.year

# Step 4: Group by the year and calculate the average temperature per year
annual_avg_temp_df = df2_cleaned.groupby('Year')['AverageTemperature'].mean().reset_index()

# Display the result
print(annual_avg_temp_df)

# %%
extended_df = pd.merge(df1, annual_avg_temp_df, left_on='PFLANZJAHR', right_on='Year', how='left')

# Drop the 'dt' column as it's no longer needed
extended_df = extended_df.drop(columns=['Year'])


# %%
extended_df = extended_df.rename(columns={
    "OBJECTID": "ObjectID",
    "BAUMNUMMER": "TreeNumber",
    "HOCHWERT": "Latitude",
    "RECHTSWERT": "Longitude",
    "GATTUNG": "Genus",
    "GA_LANG": "ScientificName",
    "KR_DURCHM": "CrownDiameter",
    "ST_UMFANG": "TrunkCircumference",
    "STRASSE": "Street",
    "BAUMHOEHE": "TreeHeight",
    "ST_DURCHM": "TrunkDiameter",
    "PFLANZJAHR": "PlantingYear",
})


# %%
extended_df.drop(columns=["ObjectID", "TreeNumber", "Latitude", "Longitude", "ScientificName", "Street"], axis=1, inplace=True)

# %%
extended_df.dropna()

# %% [markdown]
# # Load

# %%
extended_df.to_csv('../data/data.csv')

# %%


# %%



