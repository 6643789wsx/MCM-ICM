import pandas as pd
import numpy as np

# 读取表格A和表格B
#df_a = pd.read_excel('train/2023_MCM_Problem_Y_Boats.xlsx',sheet_name="Catamarans")
df_a = pd.read_excel('train/2023_MCM_Problem_Y_Boats.xlsx',sheet_name="Monohulled Sailboats ")
df_b = pd.read_csv('train/single_all.csv',encoding='gbk')

list_b = list(df_b.values)
list_c = []

for item in range(len(list_b)):
    #print(list_b[item][0])
    list_c.append(list_b[item][0].replace(' ', '-'))



# 根据表格A的第一列数据，从表格B中获取对应行数据，并将其拼接到表格A中
tmp=pd.concat([df_a, df_b],axis=1)
finish=pd.DataFrame(columns=tmp.columns)
not_count=[]
#print(finish.columns)
for index, row in df_a.iterrows():
    key1 = row[df_a.columns[0]]
    key2 = row[df_a.columns[1]]
    key = key1 + '-' + str(key2)
    key = key.replace(' ', '-')
    if key in list_c:
        index_c = list_c.index(key)
        data = df_b.iloc[[index_c]]
        select_cols = data.columns[:]
        finish.loc[len(finish.index)] = list(np.append(df_a.iloc[[index]].values,data[select_cols].values))
    else:
        not_count.append(key)

# 将结果保存到新的Excel文件中
print(not_count)
finish.to_csv('./train/single_result.csv', index=False)
