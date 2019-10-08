import numpy as np
import matplotlib.pyplot as plt

horizontal = np.zeros((8,8))
horizontal[1::2, 0::2] = 1
horizontal[1::2, 1::2] = 1

plt.imshow(horizontal, cmap="binary")
plt.show()
