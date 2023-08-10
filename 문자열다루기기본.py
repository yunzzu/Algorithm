def solution(s):
    res = True
    a = [chr(97+i) for i in range(26)] + [chr(65+i) for i in range(26)]
    for i in s:
        if i in a:
            res = False 
            break 
    return res 