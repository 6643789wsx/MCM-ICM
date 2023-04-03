import pandas as pd
import numpy as np

# 读取表格A和表格B
df_a = pd.read_excel('./train/2023_MCM_Problem_Y_Boats.xlsx')
df_b = pd.read_csv('train/single_all.csv')
# 处理df_a
df_a['Make'] = df_a['Make'].astype('str')
df_a['Variant'] = df_a['Variant'].astype('str')
df_a['Name'] = df_a['Make'] + '-' + df_a['Variant']
for i in range(len(df_a)):
    df_a.iloc[i,7] = df_a.iloc[i,7].replace(' ', '-')

# 处理df_b
for i in range(len(df_b)):
    df_b.iloc[i,0] = df_b.iloc[i,0].replace(' ', '-')
df_b

# 联合
df_c = pd.merge(df_a,df_b,on='Name',how='left')
df_c.to_csv('single_result_my.csv',encoding='gbk')

