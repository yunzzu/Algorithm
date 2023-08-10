def solution(s):
    res = False
    a = [chr(97+i) for i in range(26)] + [chr(65+i) for i in range(26)]
    if len(s)==4 or len(s)==6: #조건 추가
        for i in s:
            if i not in a:
                res = True
            else:
                res = False
                break
    return res 
