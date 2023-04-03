import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file and store it in a pandas dataframe
data = pd.read_excel(r'.\data2\single_colleration.xlsx')

# calculate correlation coefficient
corr = data.corr()

# plot heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='BuGn', ax=ax)
plt.tight_layout()

# save plot
plt.savefig('.\picture\single_heatmap.png', dpi=300)
plt.show()
