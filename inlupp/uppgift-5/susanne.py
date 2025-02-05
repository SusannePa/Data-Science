import pandas as pd

# URL of the Excel file
file_url = 'C:\Users\IdeaPad\OneDrive\Dokument\DataScience\Bostadsenkät_2024.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_url)

# Display the first few rows of the DataFrame
print(df.head())

