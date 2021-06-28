# -*- coding:UTF-8 -*-
# @author zhousanfu
# @create 2021-05-17
# 时间复杂度：O(nlogN)

import random



def ave_group(k, personnel_list):
    # 按@k值对数组@personnel_list进行随机平均分组：
    # 1、编号元素序号
    # 2、按@k步长添加

    every_len = int(len(personnel_list) / k)
    arr_flag = []
    random_num = []
    index = 0
    for i in range(len(personnel_list)):
        arr_flag.append(True)
        random_num.append(index)
        index += 1

    random.shuffle(random_num)

    result_arr = []
    every_arr = []
    index = 0
    for i in range(0, len(personnel_list) - 1, every_len):
        index += 1
        for j in range(every_len):
            every_arr.append(personnel_list[random_num[i]])
            i += 1
        result_arr.append(every_arr)
        every_arr = []
        if index >= k:
            break

    for i in range(len(random_num) - len(result_arr) * every_len):
        result_arr[i].append(personnel_list[random_num[len(personnel_list) - 1 - i]])

    # print(result_arr[0:3])


 

if __name__ == "__main__":
    k = random.randint(1,9)
    personnel_list = list(range(1,20))
    print('k = ', k)
    ave_group(k, personnel_list)
