import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': range(1, 5),
    'B': pd.date_range('20230101', periods=4),
    'C': pd.Series([3] * 4, dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

print(df)