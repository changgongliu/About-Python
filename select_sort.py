# !/usr/bin/python
# -*- coding:utf-8 -*-
import pdb
def selectionSort(arr):
    newArr = []
    pdb.set_trace()
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def findSmallest(arr):
    small = arr[0]
    small_index = 0
    for i in range(1, len(arr)):
        if arr[i]<small:
            small = arr[i]
            small_index = i
    return small_index
print selectionSort([5, 3, 6, 2, 10])

## arr.pop()返回的删除的值
## 此排序为选择排序，每次选择最大的值，进行排序
## 时间复杂度：Ｏ(n^2)
