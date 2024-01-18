import sys
import os
import yaml
import pickle

import pandas as pd
from catboost import CatBoostRegressor

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython dt.py data-file model \n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("models", sys.argv[2])
os.makedirs(os.path.join("models"), exist_ok=True)

params = yaml.safe_load(open("params.yaml"))["train"]
p_iterations = params["iterations"]
p_early_stopping_rounds = params["early_stopping_rounds"]
p_verbose = params["verbose"]
p_depth = params["depth"]
p_eval_metric = params["eval_metric"]

df = pd.read_csv(f_input)
df.index = df.period_start
df = df.dropna()
X = df.iloc[:,[1,2,3,4]]
y = df.iloc[:,5]

cb = CatBoostRegressor(iterations=p_iterations,
                          early_stopping_rounds=p_early_stopping_rounds,
                          verbose=p_verbose,
                          depth=p_depth,
                          eval_metric=p_eval_metric)

cb.fit(X, y)

with open(f_output, "wb") as fd:
    pickle.dump(cb, fd)