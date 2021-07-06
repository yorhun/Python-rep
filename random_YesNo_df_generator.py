import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5,4),["Book1", "Book2", "Book3", "Book4", "Book5"], ["Name1","Name2","Name3", "Name4"])

sz_rows = len(df)
sz_cols = len(df.iloc[0])
i=0
j=0
while i < sz_rows:
    while j < sz_cols:
        if df.iloc[i,j] > 0.5:
            df.iloc[i,j] = "Yes"
        else:
            df.iloc[i,j] = "No"
        j+=1
    i+=1
    j=0

print(df)
