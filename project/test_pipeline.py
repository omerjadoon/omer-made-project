import os
import pandas as pd

# Define the path to the output file
output_file_path = 'data/data.csv'

# Check if the output file exists
assert os.path.exists(output_file_path), "Output file does not exist."

# Load the output file
output_df = pd.read_csv(output_file_path)

# Check if the output file is not empty and has the expected columns
expected_columns = [
    'Agricultural land (sq. km)',
    'Urban population',
    'CO2 emissions (kt)',
    'Electric power consumption (kWh per capita)',
    'Forest area (sq. km)',
    'Cereal yield (kg per hectare)',
    'Inflation, consumer prices (annual %)'
]
assert not output_df.empty, "Output file is empty."
assert list(output_df.columns[1:]) == expected_columns, "Output file does not have the expected columns."

print("All tests passed!")
