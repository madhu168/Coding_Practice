def majorityElement(v: [int]) -> [int]:
    # Write your code here
    n = len(v)
    ans_map = {}

    for i in range(n):
        if v[i] in ans_map:
            ans_map[v[i]] += 1
        else:
            ans_map[v[i]] = 1

    ans = []
    for i in ans_map:
        if ans_map[i] > n//3:
            ans.append(i)
    ans.sort()
    return ans
