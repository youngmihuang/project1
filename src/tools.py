#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Editor: lishu
Update: 2019/04/11
"""

def read_data(filepath):
    df = pd.read_csv(filepath).reset_index().drop('index', axis=1)
    feature_list = list(df.columns.values)
    return df, feature_list

def output_string_feature(feature_list):
    doc = open('string_feature0.txt','w')
    for item in feature_list:
        if type(df.loc[0,item]) == str:
            print(item,'   ',df.loc[0,item])
            print(df[item].value_counts(),file = doc)
    doc.close()
    
def get_string_feature(feature_list):
    string_fea = []
    for item in feature_list:
        if type(df_backup.loc[0,item]) == str:
            string_fea.append(item)
    string_fea.append('desc')
    return string_fea
    # term 属性只有36Months 与 60months 两种值
    # emp_title 职业有很多种，也有许多职业的条目数为1，这些可以统一划分到“other"中
    # emp_length 职业长度。
    # home_ownership 一共有4中，最后一种any个数为2.这个any可以直接忽视么
    # verification_status  一共有三种，分布平均
    # issue_d 一共有12种（对应12个月），分布平均
    # loan_status 已经转换为label属性了，因此可以舍去
    # 一共有405057条目,pymnt_plan 有405055个为“n"，剩余两条可能是nan。该条属性可忽略
    # URL， 直接忽略
    # purpose， 较多，共14种目的，但用于结婚、教育的只有5例。
    # title，和上一条的意义类似。共有20多种，但是有一半的类型都只有一个条目。
    # zip_code， 反映地区位置，有许多类，其中很多只有一个条目。可放弃
    # addr_state， 地区位置，50个州。最多是CA，有50000条目，最小是ND，只有464条目。
    # earliest_cr_line  很多类，也有较大一部分类里仅有1个条目
    # revol_util， 百分数字符串。有超过100%的。存在很多为1条目的结果。
    # desc  描述，大多为空。可直接忽略。