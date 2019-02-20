import numpy as np

import pandas.core.groupby
import pandas as pd

df_dict = [["Przemek", "Warsaw", 5],
           ["Przemek", "Warsaw", 4],
           ["Ania", "Radom", 17],
           ["Magda", np.nan, 147],
           ["Magda", np.nan, 294],
           ["Magda", np.nan, 300]]

df = pd.DataFrame(df_dict, columns=["name", "location", "number"])
highest_values_df = df.groupby(["name", "location"]).mean()

print("Data frame:")
print(df)
print("Grouped by:")
print(highest_values_df)  # NAs are dropped silently
