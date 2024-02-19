import pandas as pd
from sklearn.preprocessing import StandardScaler

json = pd.read_json('clint_budget_demo.json')
df = pd.Dataframe(json)

print(df)