import matplotlib.pyplot as plt
import matplotlib

from skimage import data

matplotlib.rcParams['font.size'] = 18

fig, axes = plt.subplots(4, 5, figsize=(10, 10))
ax = axes.ravel()
images = data.lfw_subset()
for i in range(20):
    ax[i].imshow(images[90+i], cmap=plt.cm.gray)
    ax[i].axis('off')
fig.tight_layout()
plt.show()