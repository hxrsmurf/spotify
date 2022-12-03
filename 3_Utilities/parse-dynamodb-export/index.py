import os
import pandas as pd

from datetime import datetime

current = datetime.utcnow().strftime('%Y-%M-%H%M%S')

files = os.listdir()

output_file = f'{current}.csv'

dfs = []

for file in files:
    if '.json' in file:
        print(file)
        with open(file, 'r', encoding='utf8') as f:
            df = pd.read_json(f, lines=True)
            data = pd.json_normalize(df['Item'])
            dfs.append(data)

all_dfs = pd.concat(dfs, sort=False)

all_dfs.to_csv(output_file, index=False)