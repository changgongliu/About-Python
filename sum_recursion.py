# !/usr/bin/python
# -*- coding:utf-8 -*-
import pdb
def sum(st):
    if st == []:
        return 0
    return st[0]+sum(st[1:])


def count(list):
    if list == []:
        return 0
    return 1+count(list[1:])

def compare(list):
    if list == []:
        return 0
    return list[0] if list[0]>compare(list[1:]) else compare(list[1:])
if __name__ == '__main__':
    st = [1, 2, 3, 4, 5, 6, 10, 11, 100, 90]
    #pdb.set_trace()
    #print sum(st)

## 迭代
## 包含基线条件和递归条件：基线条件为递归结束条件，不断将问题分解，知道符合基线条件

    #print count(st)2 
    print compare(st)
## 注意pop返回的是删除元素，而非删除后的剩余数组
