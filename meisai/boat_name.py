import os
import openpyxl
import pandas

Catamarans_data=set()
Single_data=set()
for root, dirs, files in os.walk(r"./train"):  # 获取train中所有文件
    for file in files:
        path=os.path.join(root, file)
        wb = openpyxl.load_workbook(path)  # 读取文件路径

        # 打开指定的工作簿中的指定工作表：
        Catamarans = wb["Catamarans"]
        #ws = wb.active  # 打开激活的工作表
        ws = list(Catamarans.values)  # 转为列表
        # 2.遍历进行读取数据
        for r in ws:
            Catamarans_data.add(r[0]+' '+str(r[1]))

        # 打开指定的工作簿中的指定工作表：
        Single = wb["Monohulled Sailboats "]
        #ws = wb.active  # 打开激活的工作表
        ws = list(Single.values)  # 转为列表
        # 2.遍历进行读取数据
        for r in ws:
            Single_data.add(r[0]+' '+str(r[1]))
Single_data=sorted(Single_data)
Catamarans_data=sorted(Catamarans_data)
print(Single_data)
print(Catamarans_data)

# with open('test.txt', 'w') as f:
#     f.write(str(head_info))
df = pandas.DataFrame(Single_data,columns=["ship_name"])
df.to_csv("Single.csv",index=False)
df = pandas.DataFrame(Catamarans_data,columns=["ship_name"])
df.to_csv("Catamarans.csv",index=False)
