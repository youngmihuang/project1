
# -*_ coding: utf-8 -*-
"""
Created on Apr 10 23:05:00 2019
@author: Youngmi Huang
@email: cyeninesky3@gmail.com

"""
import time
import numpy as np 
import pandas as pd 
import pickle
import datetime

def trans_format():
    filepath = '../csv/LoanStats3d_securev1.csv'
    df = pd.read_csv(filepath)
    df = df.reset_index()
    origin_cols = df.columns
    trans_cols = df.iloc[0].values

    col_dict ={}
    for i in range(len(trans_cols)):
        col_dict[origin_cols[i]] = trans_cols[i]
    df = df.rename(columns=col_dict).iloc[1:]
    df.to_csv('../csv/LoanStats3d_securev.csv')
    return df

def preprocess(df):
    drop_feats= ['funded_amnt', 'funded_amnt_inv', 'int_rate', 'installment','grade', 'sub_grade', 
                 'initial_list_status', 'out_prncp', 'out_prncp_inv','total_pymnt', 'total_pymnt_inv', 
                 'collection_recovery_fee', 'last_pymnt_d','last_pymnt_amnt', 'next_pymnt_d', 'last_credit_pull_d', 
                 'last_fico_range_high', 'last_fico_range_low', 'collections_12_mths_ex_med', 'mths_since_last_major_derog',
                 'policy_code', 'application_type']
    df = df.copy()
    df = df[~df['loan_status'].isin(['Late (31-120 days)', 'In Grace Period', 'Late (16-30 days)', 'Default'])]
    df['label'] = df.loc[:, 'loan_status'].apply(lambda x: 1 if x == 'Charged Off' else 0)
    df = df.drop(drop_feats, axis=1)

    # 先處理 numerical 的部分
    df_numeric = df.select_dtypes(exclude=["object"])
    df_numeric = df_numeric.fillna(0)
    df_numeric = df_numeric.reset_index(drop=True)    
    return df_numeric

def statistical():
    data = pd.read_csv('../csv/LoanStats3d_securev.csv')
    print('Total: {}'.format(len(data)))
    print('Total features: {}'.format(len(data.columns)))
    print(data['loan_status'].value_counts())

    # use sample data to do data preprocessiing 
    sample = pd.read_csv('../csv/2015Sample.csv')
    print(preprocess(sample))

if __name__ == '__main__':
    statistical()
    
