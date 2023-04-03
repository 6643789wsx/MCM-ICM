import pandas as pd
import numpy as np
import math

double_init = pd.read_excel('data3/double.xlsx')
single_init = pd.read_excel('data3/single.xlsx')
hk_init=pd.read_excel('data3/HK.xlsx')

double_all=pd.read_excel('data3/double - 副本.xlsx')
single_all=pd.read_excel('data3/single - 副本.xlsx')

def autoNorm(data): #传入一个矩阵
    normData = np.zeros(np.shape(data)) #生成一个与 data矩阵同规格的normData全0矩阵，用于装归一化后的数据
    for i in range(len(data)):
        normData[i]=(data[i]-min(data))/(max(data)-min(data))
    return normData

def cosine_similarity_fun(a, b):
    dot_product = sum([a[i]*b[i] for i in range(len(a))])
    norm_a = math.sqrt(sum([a[i]**2 for i in range(len(a))]))
    norm_b = math.sqrt(sum([b[i]**2 for i in range(len(b))]))
    return dot_product / (norm_a * norm_b)

single_data=pd.DataFrame(columns=single_all.columns)
double_data=pd.DataFrame(columns=double_all.columns)
index1=set()
index2=set()
print(len(hk_init.values))
for i in range(len(hk_init.values)):
    list1=hk_init.values[i]
    list1=autoNorm(list1)
    # Converting lists into numpy arrays
    array1 = list1
    for j in range(len(single_init.values)):
        list2=single_init.values[j]
        list2=autoNorm(list2)

        array2 = list2

        # # Calculating the Euclidean distance
        # distance = np.sqrt(np.sum(np.square(array1 - array2)))

        # Calculating cosine similarity using dot product
        cosine_similarity = cosine_similarity_fun(array1,array2)

        if cosine_similarity>=0.99999:
            print(cosine_similarity)
            index1.add(j)
            #data.loc[len(data)] = list2

    for j in range(len(double_init.values)):
        list2=double_init.values[j]
        list2=autoNorm(list2)

        array2 = list2

        # # Calculating the Euclidean distance
        # distance = np.sqrt(np.sum(np.square(array1 - array2)))

        # Calculating cosine similarity using dot product
        cosine_similarity = cosine_similarity_fun(array1,array2)

        #print(cosine_similarity)
        if cosine_similarity>=0.999999:
            index2.add(j)
            #data.loc[len(data)] = list2

    print(i)

for i in index1:
    single_data.loc[len(single_data)]=single_all.values[i]

for i in index2:
    double_data.loc[len(double_data)]=double_all.values[i]

double_data.to_csv("./data3/double_near.csv",index=False)
single_data.to_csv("./data3/single_near.csv",index=False)