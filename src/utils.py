# -*_ coding: utf-8 -*-
"""
Created on Apr 13 9:43:00 2019
@author: Youngmi Huang
@email: cyeninesky3@gmail.com

"""

def get_bin_sizes(df, col):
    limit = round(len(df)*0.1)
    score_dict={}
    for i in df[col]:
        score_dict.setdefault(i,0)
        score_dict[i] +=1

    nums = []
    for key in sorted(score_dict.keys()):
        nums.append(score_dict[key])
        
    grp_num=[]
    total = 0
    for num in nums:
        if total < limit:
            total += num
        else:
            grp_num.append(total)
            total = num
    grp_num.append(total) # the last bin
    return grp_num

def get_KS_IV(df, grp_num):
    value_cnt_total = dict(df['label'].value_counts())
    total_goods, total_bads = value_cnt_total[0], value_cnt_total[1]
    acc_of_goods=0
    acc_of_bads=0
    KSs=[]
    IVs=[]
    prev=0

    for bin_size in grp_num:
        sub = df[prev: prev+bin_size]
        value_cnt = dict(sub['label'].value_counts())
        if len(value_cnt) == 1:
            goods = value_cnt[0]
            bads = 0
        else:
            goods = value_cnt[0]
            bads = value_cnt[1]
        acc_of_goods += goods
        acc_of_bads += bads
        percentage_of_goods = goods/float(total_goods)
        percentage_of_bads = bads/float(total_bads)
        percentage_of_acc_goods = acc_of_goods/float(total_goods)
        percentage_of_acc_bads = acc_of_bads/float(total_bads)
        ks = abs(percentage_of_acc_goods - percentage_of_acc_bads)
        iv = (percentage_of_goods - percentage_of_bads) * np.log(percentage_of_goods/percentage_of_bads)    
        KSs.append(ks)
        IVs.append(iv)
        prev+=bin_size
    KS = 100*max(KSs)
    IV = np.sum(IVs)
    return KS, IV

def process_effect_dataset(data):
    print '===== Now processing'    
    ranked_feas = list(data.keys()) # get all feature names as a list object
    ranked_feas.sort() # a toy ranking example
    
    IVs={}
    KSs={}
    error_code=[]
    for feat in ranked_feas:
        try:
            print(feat)
            sub = data[['label', feat]]
            sub = sub.dropna()
            sub = sub.sort_values(by=[feat]) # order from low to high
            grp_num = get_bin_sizes(sub, feat)
            KS, IV = get_KS_IV(sub, grp_num)
            KSs[feat] = KS
            IVs[feat] = IV
        except:
            error_code.append(feat)
    order_by_value_ks = sorted([(i[1],i[0]) for i in KSs.items()], reverse=True) # 依照 value 排序
    order_by_value_iv = sorted([(i[1],i[0]) for i in IVs.items()], reverse=True) # 依照 value 排序
    return order_by_value_ks, order_by_value_iv, error_code

