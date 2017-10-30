# !/usr/bin/python
# -*- coding:utf-8 -*-
import pdb
## 邻居节点表
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}
## 开销表
infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

## 父节点表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

##　已经处理过节点表
processed = []

def find_lowst_node(list):
    low_cost_node = float('inf')
    node = None
    for item in list:
        if list[item]<low_cost_node and  item not in processed:
            node = item
            low_cost_node = list[item]
    return node

def find_path(list):
    next_one = 'fin'
    list_return = [next_one]
    while list_return[-1] != 'start':
        list_return.append(list[next_one])
        next_one = list[next_one]
    return list_return

if __name__ == '__main__':
    node = find_lowst_node(costs)
    while node is not None:
        processed.append(node)
        cost = costs[node]
        neighbors = graph[node]
        for item in neighbors:
            new_cost = cost + neighbors[item]
            if costs[item]>new_cost:
                costs[item] = new_cost
                parents[item] = node
        node = find_lowst_node(costs)
    print '最短路径:'
    #pdb.set_trace()
    path = find_path(parents)
    print_list = 'start'
    for x in path[::-1]:
        if x != 'start':
            print_list += '->%s' % x
    print print_list
## 狄克斯特拉斯算法，加权情况下寻找最短路径
## 好困呀
## 建立四个表:所有节点的邻居节点表，开销表，父节点表，处理过的节点表
## 对开销表中当前未处理过的最小开销进行处理，处理包括所有邻居节点的开销比较
## ，更新最小开销，更新父节点表，更新已处理过节点表
