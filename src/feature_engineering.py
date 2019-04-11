#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Editor: lishu
Update: 2019/04/11
"""
import time
import numpy as np 
import pandas as pd 
import math

import ks_rank
import tools


def get_ks_rank_directly():
    ks_rank = pd.read_csv('../csv/ks_rank.csv')  
    return ks_rank
    
def output_ks_rank(df_backup):
    return get_ks_rank(df_backup)

if __name__ == "__main__":
    filepath = '../csv/LoanStats3d_securev.csv'
    df_backup, feature_list = read_data(filepath)
    ks_rank = get_ks_rank_directly()
    best_fea = list(ks_rank[ks_rank['value']>10].feature)
    string_fea = get_string_feature(feature_list)