import pandas as pd

# Load your CSV
df = pd.read_csv('SPY_Dividend_Data.csv')

df['Date'] = df['Type'].astype(str) + ', ' + df['Payment Date'].astype(str)

df.rename(columns={'Ex-Dividend Date': 'Amount'}, inplace=True)

#Delete unncessary colummns
df = df.drop(['Type', 'Payment Date', 'Dividend'], axis=1)

# Save the updated CSV
df.to_csv('formatted_SPY_Dividend.csv', index=False)