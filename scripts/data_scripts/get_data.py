#!/usr/bin/python3

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


    
df = pd.read_excel('df_ses.xlsx')

df_train, df_test = train_test_split(df, test_size=0.25, random_state=42, shuffle=False)
df_train.to_csv('../../data/raw/df_train.csv', index=False)
df_test.to_csv('../../data/raw/df_test.csv', index=False)