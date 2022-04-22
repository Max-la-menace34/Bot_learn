from operator import index
import random as rm
from textwrap import indent
import pandas as pd
import numpy as np
df_data=pd.DataFrame()
close = np.array([i for i in range(150,250,2)])
open = np.array([i for i in range(50,150,2)])
df_data['close']=close
df_data['open']=open
print(df_data['open'])

