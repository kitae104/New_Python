from skimage import io
import matplotlib.pyplot as plt

img = io.imread("bad.png")
io.imshow(img)
plt.show()