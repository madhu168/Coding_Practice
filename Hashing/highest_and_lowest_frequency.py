from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    v_map = {}
    ans = []
    for i in range(len(v)):
        if(v[i] in v_map):
            v_map[v[i]] += 1
        else:
            v_map[v[i]] = 1
    v_max = 0
    v_max_index = 0
    for i in v_map:
        if(v_map[i] > v_max):
            v_max = v_map[i]
            v_max_index = i
        if(v_map[i] == v_max):
            v_max_index = min(i,v_max_index)
    ans.append(v_max_index)
    
    v_min = v_map[v[0]]
    v_min_index = v[0]
    for i in v_map:
        if(v_map[i] < v_min):
            v_min = v_map[i]
            v_min_index = i
        if(v_map[i] == v_min):
            v_min_index = min(i,v_min_index)
    ans.append(v_min_index)
    
    return ans