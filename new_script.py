import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import mpi4py
import pytables

x = np.random.random(100)

df = pd.DataFrame(x)

df.plot()
plt.show()
