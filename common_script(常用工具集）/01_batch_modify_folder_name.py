# coding=utf-8

"""
需求：把code文件夹所有的文件重命名为wss_code
"""
import os


flag = 2
file_list = os.listdir()  # 获取code文件夹的目录列表
print(file_list)

for i in file_list:
    if flag == 1:
        # new_name = 'wss_' + 原文件i
        new_name = 'wss_' + i
    elif flag == 2:
        num = len('wss_') # 删除前缀
        new_name = i[num:]
    os.rename(i, new_name)  # 重命名
