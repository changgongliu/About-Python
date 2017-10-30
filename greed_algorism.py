# !/usr/bin/python
# -*- coding:utf-8 -*-
##　需要覆盖的州
import pdb
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

states = {}
states['kone'] = set(['id', 'nv', 'ut'])
states['ktwo'] = set(['wa', 'id', 'mt'])
states['kthree'] = set(['or', 'nv', 'ca'])
states['kfour'] = set(['nv', 'ut'])
states['kfive'] = set(['ca', 'az'])

final_states = set()
pdb.set_trace()
while states_needed:
    best_station = None
    states_covered = set()
    for state, states_for_station in states.items():##此处天items()
        covered = states_for_station & states_needed
        if len(covered) > len(states_covered):
            states_covered = covered
            best_station = state
    final_states.add(best_station)
    states_needed -= states_covered
print final_states
## 贪婪算法
