import os
import sys
import pickle
import json

import pandas as pd
from sklearn.metrics import r2_score

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython evaluate.py data-file model\n")
    sys.exit(1)

df = pd.read_csv(sys.argv[1])
df.index = df.period_start
df = df.dropna()
X = df.iloc[:,[1,2,3,4]]
y = df.iloc[:,-1]

with open(sys.argv[2], "rb") as fd:
    cb = pickle.load(fd)

y_predict=model.predict(X)

r2 = mean_absolute_error(y, y_predict)

prc_file = os.path.join("evaluate", "r2_score.json")
os.makedirs(os.path.join("evaluate"), exist_ok=True)

with open(prc_file, "w") as fd:
    json.dump({"r2_score": r2}, fd)