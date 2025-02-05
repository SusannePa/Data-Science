import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = r'https://github.com/SusannePa/Data-Science/blob/main/Bostadsenk%C3%A4t_2024.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())