import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load dataset
df = pd.read_csv("C:\\Users\\moham\\Downloads\\greenhouse-gas-emissions-industry-and-household-September-2024-quarter.csv")

# Info and head
print(df.info())
print(df.head())
print(df.describe())
print(df.nunique())

# Missing values
print(df.isnull().sum())

# Plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Get the latest period
latest = df['Period'].max()

# Filter data for the latest period
latest_df = df[df['Period'] == latest]

# Group and sort emissions by sector
grouped = latest_df.groupby('Anzsic_descriptor')['Data_value'].sum()
top10 = grouped.sort_values(ascending=False).head(10)

# Create basic vertical bar graph
plt.bar(range(len(top10)), top10.values, color='green')
plt.xticks(range(len(top10)), top10.index, rotation=45)
plt.title('Top 10 Emitting Sectors')
plt.xlabel('Sector')
plt.ylabel('Emissions (Kilotonnes)')
plt.tight_layout()
plt.show()
#line graph
df_households = df[df['Anzsic_descriptor'] == 'Households']

# Group and sum emissions by period
g = df_households.groupby('Period')['Data_value'].sum()

# Create the line plot with markers
plt.plot(g.index, g.values, marker='o')

plt.title('Emission Trend - Households')
plt.xlabel('Period')
plt.ylabel('Emissions (Kilotonnes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Pie Chart - Top 5 sectors
latest = df['Period'].max()

# Filter data for the latest period
latest_df = df[df['Period'] == latest]

# Group, sum, and get top 5 contributors
grouped5 = latest_df.groupby('Anzsic_descriptor')['Data_value'].sum().sort_values(ascending=False).head(5)

# Plot basic pie chart
plt.pie(grouped5, labels=grouped5.index, autopct='%1.1f%%', startangle=100)
plt.title('Top 5 Emission Contributors')
plt.tight_layout()
plt.show()

# 4. Emission Intensity (Scatter Plot)
df_sector = df[df['Anzsic_descriptor'] == 'Households']

# Group by Period and sum the emissions
grouped = df_sector.groupby('Period')['Data_value'].sum().reset_index()

# Create scatter plot
plt.scatter(grouped['Period'], grouped['Data_value'])

plt.title('Emission Intensity - Households')
plt.xlabel('Period')
plt.ylabel('Emissions (Kilotonnes)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Pair Plot
sns.pairplot(df[['Period', 'Data_value']])
plt.suptitle("Pair Plot of Numerical Variables", y=2.02)
plt.tight_layout()
plt.show()

# 5. Heatmap (Correlation)
corr_data = df[['Period', 'Data_value']].corr()
sns.heatmap(corr_data, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# 6. Boxplot for Outliers
sns.boxplot(data=df, x='Data_value')
plt.title('Outliers in Emissions')
plt.tight_layout()
plt.show()

# 7. Z-score Outliers
df['Z_score'] = zscore(df['Data_value'])
outliers = df[abs(df['Z_score']) > 3]
print(outliers[['Anzsic_descriptor', 'Period', 'Data_value', 'Z_score']])




