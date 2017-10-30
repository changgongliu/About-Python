# !/usr/bin/python
# -*- coding:utf-8 -*-
import pdb
def quicksort(list):
    #pdb.set_trace()
    if len(list)<2:
        return list
    flag = list[0]
    low = []
    high = []
    for item in list[1:]:
        if item>flag:
            high.append(item)
        else:
            low.append(item)
    return quicksort(low)+[flag]+quicksort(high)

st = [3, 4, 2, 9, 10, 12, 5, 6]
print quicksort(st)

## 快速排序
## 时间复杂度:o(nlogn)
