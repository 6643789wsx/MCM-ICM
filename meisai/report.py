# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# df = pd.read_excel('./data2/single_colleration.xlsx')
#
# plt.figure(figsize=(8,6))
# sns.scatterplot(x='DWL', y='ListingPrice', data=df, hue='ListingPrice')
# plt.title('Relationship between Sailboat Length and Price Range')
# plt.xlabel('Length (feet)')
# plt.ylabel('Price Range (HKD)')
# plt.savefig('.\picture\Sailboat Length and Price Range.png', dpi=300)
# #plt.show()
#
# features = ['Width', 'Displacement', 'SA/Disp', 'Fuel', 'Water', 'ListingPrice']
# corr = df[features].corr()
#
# plt.figure(figsize=(10,8))
# sns.heatmap(corr, cmap='Blues', annot=True)
# plt.title('Factors Influencing Sailboat Pricing')
# plt.savefig('.\picture\Factors.png', dpi=300)
# #plt.show()
#
# plt.figure(figsize=(10,8))
# ranges = df.groupby(pd.cut(df['DWL'], [0, 25, 30, 40, 1000], include_lowest=True)).mean()
# sns.barplot(x=ranges.index, y=ranges['ListingPrice'], palette='Blues')
# plt.title('Recommended Price Ranges for Used Sailboats')
# plt.xlabel('Sailboat Length (feet)')
# plt.ylabel('Price Range (HKD)')
# plt.savefig('.\picture\Recommended Price Ranges .png', dpi=300)
# #plt.show()






# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
#
# # Load data from CSV
# df = pd.read_excel('./data2/single_colleration.xlsx')

# # Create a scatter plot of sailboat width versus listing price
# plt.figure(figsize=(8,6))
# sns.scatterplot(x='Width', y='ListingPrice', data=df)
# plt.title('Sailboat Width versus Listing Price')
# plt.xlabel('Width (meters)')
# plt.ylabel('Listing Price (HKD)')
# plt.savefig('.\picture\Sailboat Width.png', dpi=300)
#
# Create a scatter plot of sailboat displacement versus listing price
# plt.figure(figsize=(8,6))
# sns.boxplot(x='Displacement', y='ListingPrice', data=df)
# plt.title('Sailboat Displacement versus Listing Price')
# plt.xlabel('Displacement (kg)')
# plt.ylabel('Listing Price (HKD)')
#plt.savefig('.\picture\Sailboat Displacement versus Listing Price.png', dpi=300)
#
# # Create a scatter plot of sailboat SA/Disp versus listing price
# plt.figure(figsize=(8,6))
# sns.scatterplot(x='SA/Disp', y='ListingPrice', data=df)
# plt.title('Sailboat SA/Disp versus Listing Price')
# plt.xlabel('SA/Disp')
# plt.ylabel('Listing Price (HKD)')
# plt.savefig('.\picture\SADisp.png', dpi=300)
#
# # Create a box plot of sailboat listing prices by rigging type
# plt.figure(figsize=(8,6))
# sns.boxplot(x='Rigging Type', y='ListingPrice', data=df)
# plt.title('Sailboat Listing Prices by Rigging Type')
# plt.xlabel('Rigging Type')
# plt.ylabel('Listing Price (HKD)')
# plt.savefig('.\picture\Sailboat Listing Prices by Rigging Type.png', dpi=300)



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel('./data2/important.xlsx')

plt.figure(figsize=(8,6))
sns.scatterplot(x='Displacement', y='Monohull Listing Price', data=df,hue='Monohull Listing Price')
#plt.title('Relationship between Displacement and Listing Price')
plt.xlabel('Displacement')
plt.ylabel('Monohull Listing Price')
plt.savefig('.\picture\Monohulled.png', dpi=300)
#plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x='Fuel', y='Catamarans Listing Price', data=df,hue='Catamarans Listing Price')
#plt.title('Relationship between Fuel and Listing Price')
plt.xlabel('Fuel')
plt.ylabel('Catamarans Listing Price')
plt.savefig('.\picture\Catamarans.png', dpi=300)
#plt.show()