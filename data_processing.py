import pandas as pd

def process_data(raw_data):
    # Assuming raw_data is a pandas DataFrame
    count_values = raw_data['Count'].unique()
    count_values.sort()
    return count_values

# Assuming raw_data is loaded from some source
raw_data = pd.read_csv('raw_data.csv')
data = process_data(raw_data)