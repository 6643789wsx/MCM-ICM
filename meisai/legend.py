import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# read in image
img = plt.imread('./picture/region4.png')

# create a new figure
fig, ax = plt.subplots()

# plot image
ax.imshow(img)

# create legend handles
pink_patch = mpatches.Patch(color=[242/255, 58/255, 238/255], label='Catamarans')
green_patch = mpatches.Patch(color=[29/255, 242/255, 1/255], label='Monohulls')

# remove x and y axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

# add legend to figure
ax.legend(handles=[pink_patch, green_patch], loc='upper left')
plt.tight_layout()

# show figure
plt.savefig('./picture/region_world.png')
#plt.show()
