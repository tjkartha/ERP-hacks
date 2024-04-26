import pandas as pd
a = pd.read_csv("export.csv")

a = a.iloc[0:, 1]

names = []
rolls = []
for x in a:
    rolls.append(x[:16])
    names.append(x[18:])

rolls_names = list(zip(rolls, names))
rolls_names_df = pd.DataFrame(rolls_names)
rolls_names_df.to_csv("Rolls_names.csv")

