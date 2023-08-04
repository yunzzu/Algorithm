#sol1 
import datetime 
def solution(a, b):
    week = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return week[datetime.datetime(2016,a,b).weekday()]

#sol2 
def solution2(a, b):
    days = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED']
    months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31]
    return days[(sum(months[:a-1])+b)%7]
