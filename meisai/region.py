import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the Excel file
df = pd.read_excel(r'.\data3\region_single.xlsx')

# Set style for the plot
sns.set(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df,x="Variant",y='ListingPrice(USD)', hue="GeographicRegion",
                palette="Set1", alpha=0.9, edgecolor="none")

# Add title, labels, and legend to the plot
#plt.title("Regional Effects on Sailboat Variants", fontsize=18)
plt.xlabel("Variant", fontsize=14)
plt.ylabel("ListingPrice(USD)", fontsize=14)
legend = plt.legend(title="Region", title_fontsize=12, fontsize=12, loc='center left', bbox_to_anchor=(1.01, 0.5))

# Adjust the position of the legend
plt.savefig(r".\picture\region_single.png", bbox_extra_artists=(legend,), bbox_inches='tight')
#plt.show()






# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
#
# # Generate the falsified data
# data = {'Region': ['Eastern', 'Western', 'Southern', 'Northern', 'Central'],
#         'Value': [23, 35, 28, 33, 29],
#         'Sailboat Variant': ['Catalina 22', 'J/105', 'Hunter 33', 'O\'Day 34', 'Beneteau 40']}
# df = pd.DataFrame(data)
#
# # Set style for the plot
# sns.set(style="whitegrid")
#
# # Create the scatter plot
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x="Value", y="Sailboat Variant", hue="Region",
#                 palette="Set1", s=500, alpha=0.9, edgecolor="none")
#
# # Add title and labels to the plot
# plt.title("Regional Effects on Sailboat Variants")
# plt.xlabel("Regional Value")
# plt.ylabel("Sailboat Variant")
#
# # Add annotations to the plot
# for line in range(0, df.shape[0]):
#      plt.text(df['Value'][line] + 0.5, df['Sailboat Variant'][line],
#               df['Region'][line], horizontalalignment='left',
#               size='medium', color='black', weight='semibold')
#
# plt.show()


