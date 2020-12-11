# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:31:24 2020

@author: Troi Vergara
"""

import pandas as pd
import numpy as np

games = pd.read_csv("bkn_2019-2020.csv")
#remove rows 0,21-22,43-44 & 65-66
drop_rows = [0, 21, 22, 43, 44, 65, 66]
games = games.drop(drop_rows)

# remove columns "Unamed:0, "", ".1"
drop_cols = [0,3,24]
games = games.drop(games.columns[drop_cols], axis=1)

#Feature Engineering