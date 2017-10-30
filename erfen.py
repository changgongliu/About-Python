# !/usr/bin/python
# -*- coding:utf-8 -*-
import pdb
def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)/2
        if(list[mid] == item):
            return mid
        if(list[mid] < item):
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == '__main__':
    list = [1, 3, 5, 7, 9]
    #db.set_trace()
    result = binary_search(list, 3)
    print result
## 关于细节的问题，注意mid向下取整，所以这个程序low<=high不能改只能是这样
## 时间复杂度:log2(n)
##　二分法查找数据　
