#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Editor: lishu
Update: 2019/04/11
"""
import numpy as np 
import pandas as pd 
import math

import lightgbm as lgb
import xgboost as xgb

from sklearn import metrics
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import feature_engineering

# In[]
# read data and prepare

filepath = '../csv/LoanStats3d_securev.csv'
df_backup, feature_list = read_data(filepath)
ks_rank = get_ks_rank_directly()
best_fea = list(ks_rank[ks_rank['value']>10].feature) # HERE we get 20 features
string_fea = get_string_feature(feature_list)

targetcols = ['label']
traincols = best_fea
split_train = int(np.floor(0.7* len(df_backup)))
split_dev = int(np.floor(0.85* len(df_backup)))

# In[]
# prepare data for sklearn.tree

df = df_backup[traincols+targetcols].fillna(0)

sscaler = StandardScaler() # StandardScaler from sklearn.preprocessing
sscaler.fit(df[traincols]) # fit training data to get mean and variance of each feature term

all_matrix = sscaler.transform(df[traincols]) # transform training data to standardized vectors
train_matrix = all_matrix[0:split_train,:]
dev_matrix = all_matrix[split_train+1:split_dev,:]
test_matrix = all_matrix[split_dev+1:,:]


all_labels = np.array(df[targetcols])
train_labels = all_labels[0:split_train]
dev_labels = all_labels[split_train+1:split_dev]
test_labels = all_labels[split_dev+1:]

print(train_matrix.shape, train_labels.shape)

# In[]
# Model Selection Pipeline of Tree

best_depth = None # the best decision tree depth we want to find
train_size = train_matrix.shape[0] # size of training data

depth_paras = np.arange(3, 13, 2) # define the parameter search spaces
auc_scores = [] # used to store auc scores

display_flag = True
# start simple grid search
for depth in depth_paras:
    clf = tree.DecisionTreeClassifier(max_depth=int(depth)) # try a decision tree with 'max_depth' equals 'depth'
    clf.fit(train_matrix, train_labels) # training
    dev_predict = clf.predict_proba(dev_matrix)[:, 1] # get predicting probs of class '1'
    auc_score = metrics.roc_auc_score(y_true=dev_labels, y_score=dev_predict)
    if display_flag:
        print("Finish training DecisionTreeClassifier(max_depth=%d)..." % int(depth))
        print("AUC on validation set:%.6f" % auc_score)
    auc_scores.append(auc_score)
idx_max = np.argmax(auc_scores)
best_depth = int(depth_paras[idx_max])
print("Find best tree depth: %d" % best_depth)



## In[]
## Preparing data for lightgbm
#df_t = df_backup[traincols+targetcols].fillna(0).loc[0:split_train]
#df_d = df_backup[traincols+targetcols].fillna(0).loc[split_train+1:split_dev]
#df_test = df_backup[traincols+targetcols].fillna(0).loc[split_dev+1:]
#
## train data
#Xt = df_t[traincols].values
#Yt = df_t[targetcols].values
#
## develop data
#Xd = df_d[traincols].values
#Yd = df_d[targetcols].values
#
## test data
#Xtest = df_test[traincols].values
#Ytest = df_test[targetcols].values
#print(Xt.shape, Xd.shape, Xtest.shape)
## In[]
#print ('Training lightgbm')
#params = {"objective" : "binary",
#          "metric" : "binary_logloss",
#          "num_leaves" : 60,
#          "max_depth": -1,
#          "learning_rate" : 0.01,
#          "bagging_fraction" : 0.9,  # subsample
#          "feature_fraction" : 0.9,  # colsample_bytree
#          "bagging_freq" : 5,        # subsample_freq
#          "bagging_seed" : 2018,
#          "verbosity" : -1 }
#
#
#lgtrain, lgval = lgb.Dataset(Xt, Yt[:,0]), lgb.Dataset(Xd, Yd[:,0])
#lgbmodel = lgb.train(params, lgtrain, 2000, valid_sets=[lgtrain, lgval], early_stopping_rounds=100, verbose_eval=200)
#





























