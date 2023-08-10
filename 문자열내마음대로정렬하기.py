#sol1 
def solution1(strings, n):
    strings.sort()
    return sorted(strings, key=lambda a: a[n])

#sol2
def solution2(strings, n):
    return sorted(strings, key=lambda a: (a[n],a))