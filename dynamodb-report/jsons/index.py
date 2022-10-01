import json
import os

files = os.listdir()

for file in files:
    if not 'py' in file:
        print(file)
