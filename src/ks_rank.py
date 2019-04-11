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
import tools

def get_ks_rank(df_backup):
    feature_list = list(df_backup.columns.values)
    string_fea = get_string_feature(feature_list)
    ranked_feas = []
    for item in feature_list:
        if item not in string_fea:
           ranked_feas.append(item) 
    
    KS_record = []
    del ranked_feas[-1] # delete 'label' column
    del ranked_feas[1] # delete 'member_id' column
    del ranked_feas[0] # delete 'id' column
    
    for attribute in ranked_feas:
        df = df_backup[['label', attribute]]
        df = df.dropna()
        length = len(df)
        least = math.ceil(0.1*length)
        df = df.sort_values(by = [attribute],ascending = True)
        df = df.reset_index(drop=True)
        total_bad = np.sum(df.label)
        total_good = length - total_bad
    
        accm_good_ratio = 0
        accm_bad_ratio = 0 
    
        KS_list=[]
        counter = 0
        bin_sizes = []
        num_bins = 0
        KS, IV = 0.0, 0.0
        temp_score = []
        group_score = []
        num = 0
        score_list = list(set(df[attribute].tolist()))
        score_list.sort(reverse = False)
        
        for score in score_list:      
            temp_score.append(score)
            df_part = df[df[attribute]==score]
            num = num + len(df_part)
            if (num >= least  or  score == score_list[-1]):
                num_bins = num_bins + 1
                bin_sizes.append(num)     
                num = 0
                group_score.append(temp_score)
                temp_score = []  
        # Normalized to the size (the number of samples) of the dataset.                
        bin_sizes = list(np.array(bin_sizes) / len(df))    
        # Calculate KS
        accm_good_ratio = 0
        accm_bad_ratio = 0   
        KS_list = []
        total_bad = np.sum(df.label)
        total_good = len(df) - total_bad
        for group in group_score:
            df['condition'] = df[attribute].apply(lambda x : 1 if (x >= group[0] and x <= group[-1]) else 0)
            df_part = df[df['condition'] == 1]
    
            bad_ratio = np.sum(df_part.label) / total_bad
            good_ratio = (len(df_part) - np.sum(df_part.label)) / total_good
            accm_bad_ratio = accm_bad_ratio + bad_ratio
            accm_good_ratio = accm_good_ratio + good_ratio
            KS_list.append((accm_good_ratio-accm_bad_ratio)*100)
    
        KS_list = np.abs(KS_list)
        KS = np.max(KS_list)    
        KS_record.append(KS)
        print(attribute,KS)
        
    time_end=time.time()
    print('time cost',time_end-time_start,'s')     
    ks_rank = pd.Series(KS_record, index=ranked_feas).sort_values(ascending = False)
    # Write the result to csv 
    ks_rank.to_csv('ks_rank0.csv',index=True,sep=',')
    return ks_rank
    
    
    
    
    
    
    
    