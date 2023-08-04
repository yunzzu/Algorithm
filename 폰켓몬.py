def solution(nums):
    ans = 0
    d = {}
    for i in nums:
        if i in d.keys(): d[i]+=1 
        else: d[i] = 1 
    if len(d)>len(nums)/2: #종류가 더 많을 때 
        return int(len(nums)/2)
    else:
        return len(d)