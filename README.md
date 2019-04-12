# lendingclub
quantitive credit risk and default analysis course project1


## Description

Todo/Model performance / others… 

4/12(youngmi)

1. add `model.py` => NN model (only using 74 numerical feats)

   | date | model | Performance                                                  |
   | ---- | ----- | ------------------------------------------------------------ |
   | 4/12 | NN    | 5-fold average Auc score on Validation data: 0.9500247628653332<br/>5-fold average Precision on Validation data: 0.9587681231206997<br/>
5-fold average Recall on Validation data: 0.5736161616161616 |
   |      |       |                                                              |
   |      |       |                                                              |

2. nn structure

   ![nnmodel_stucture](/Users/youngmihuang/Desktop/project1/img/nnmodel_stucture.png)

4/11 (lishu)

1. add `tools.py` : 包含三个用来处理字符串特征的小函数。

2. add `ks_rank.py` : 用来处理全部的数值型特征，计算KS并排序，输出到同目录下的ks_rank.csv

3. add `string_feature.txt`, `ks_rank.csv`： 字符串特征的分布输出，ks按照高低排序的特征，之后可以直接读取，避免再次计算。

4. add `tree_main.py`: 决策树算法，AUC结果在0.91左右。


4/10 (youngmi)

1. add `data_clean.py` : 处理原数据`LoanStats3d_securev1` dataframe 格式问题，调用 `trans_format()` 及能解决此问题 

2. 按照助教要求，将 loan_status 取 Charged Off, Current, Fully-paid ，并打好标签，去除不能使用的 X 因子，调用 `preprocess()` 即可

   PS. loan_status 处理前各分类数量

   ![description](img/description.png)

   

## About Update

每次要上传代码前，要先抓取最新

`git pull`

然后直接 push 到 master/origin 即可（只上传 code ）

`git add example.py`

`git commit -m 'update' `

`git push`


`
