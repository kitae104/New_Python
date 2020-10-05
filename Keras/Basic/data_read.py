import numpy as np
data = np.loadtxt(filename, delimiter=',', skiprows=1)

import pandas as pd
data = pd.read_csv(filename, delimiter=',')
data = pd.read_json(filename)
data = pd.read_sql(con, "select * from table")