def solution(s):
    upper, lower = '', ''
    for i in s:
        if i.islower(): lower += i
        if i.isupper(): upper += i
    return "".join(sorted(lower,reverse=True))+"".join(sorted(upper,reverse=True))