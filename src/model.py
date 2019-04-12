# -*_ coding: utf-8 -*-
"""
Created on Apr 11 22:50:12 2019
@author: Youngmi Huang
@email: cyeninesky3@gmail.com

"""

import time
import numpy as np 
import pandas as pd 
import pickle
import datetime
import lightgbm as lgb
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.metrics import classification_report, precision_score, roc_auc_score, recall_score
from keras.models import Model
from keras.layers import Input, Dense, Embedding, Concatenate, Flatten, BatchNormalization, Dropout
from keras.losses import binary_crossentropy, mse
from keras.callbacks import EarlyStopping, ModelCheckpoint
from data_clean import preprocess

def get_input(df, indices):
    num_cols = [i for i in df.columns if i not in ['member_id', 'label']]
    X = df.loc[indices, num_cols]
    y = df.loc[indices, 'label']
    return X, y

def nn_model(num_feats):
    numerical_inputs = Input(shape=(num_feats,), name='num')
    numerical_logits = numerical_inputs
    numerical_logits = BatchNormalization()(numerical_logits)

    numerical_logits = Dense(128,activation='relu')(numerical_logits)
    numerical_logits = Dense(64,activation='relu')(numerical_logits)

    logits = Dense(32,activation='relu')(numerical_logits)
    out = Dense(1, activation='sigmoid')(logits)
    model = Model(inputs = numerical_inputs, outputs=out)    
    model.compile(optimizer='sgd',loss=binary_crossentropy)
    print(model.summary())
    return model

def result_report(y_valid, y_valid_pred):
    y_valid_pred = (y_valid_pred>0.5).astype(int)[:,0]
    print(classification_report(y_valid, y_valid_pred))


def main():
    # 拆分為 train & test
    df = pd.read_csv('../csv/LoanStats3d_securev.csv')
    df = preprocess(df)
    train_indices, test_indices = train_test_split(df.index.values, test_size=0.1, random_state=6, stratify=df.label)
    train = df.loc[train_indices].reset_index(drop=True)
    test = df.loc[test_indices].reset_index(drop=True)

    # train 使用 5-fold 分層抽樣訓練
    X, y = get_input(train, train.index.values)
    sampling = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=10)
    auc_scores, precisions, recalls = [], [], []
    for train_index, val_index in sampling.split(X, y):
        X_train, y_train = get_input(train, train_index)
        X_valid, y_valid = get_input(train, val_index)
        
        model = nn_model(X_train.shape[1])  # feats 個數    
        check_point = ModelCheckpoint('model.hdf5',verbose=0, save_best_only=True)
        early_stop = EarlyStopping(patience=5,verbose=0)
        model.fit(X_train, y_train,
                  validation_data=(X_valid, y_valid),
                  epochs=150,
                  verbose=0,
                  callbacks=[early_stop,check_point]) 
        

        y_valid_pred = model.predict(X_valid)
        auc_scores.append(roc_auc_score(y_valid, y_valid_pred))   
        precisions.append(precision_score(y_valid, (y_valid_pred>0.5).astype(int)[:,0]))
        recalls.append(recall_score(y_valid, (y_valid_pred>0.5).astype(int)[:,0]))
        result_report(y_valid, y_valid_pred)

    print('='*80)
    print('5-fold average Auc score on Validation data: {}'.format(np.mean(auc_scores)))
    print('5-fold average Precision on Validation data: {}'.format(np.mean(precisions)))
    print('5-fold average Recall on Validation data: {}'.format(np.mean(recalls)))
    
    # To do: model 保存& 取最優的來預測
    X_test, y_test = get_input(test, test.index.values)
    y_test_pred = model.predict(X_test)
    print("="*80)
    print(result_report(y_test), y_test_pred))
    print('Auc score on Test data: {}'.format(auc_scores(y_test, y_test_pred)))
    print('Precision on Test data: {}'.format(precision_scores(y_test, y_test_pred)))

if __name__ == '__main__':
    main()