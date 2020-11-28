import numpy as np
x = np.array([[20, 10], [20, 10]])
res = np.mean(x[:,1])
print(res)

# np_baseball is available
np_baseball = np.array([[21, 10], [22, 10]])
# Import numpy
import numpy as np

# Create np_height from np_baseball

np_height=np_baseball[:,0]
# Print out the mean of np_height

print(np.mean(np_height))
# Print out the median of np_height
print(np.median(np_height))