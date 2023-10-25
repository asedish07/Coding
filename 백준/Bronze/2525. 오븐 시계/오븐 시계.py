hour, minute = map(int, input().split())
time = input()
time = int(time)
if time+minute>60 and hour+((minute+time)//60)<=23:
    hour = hour+((minute+time)//60)
    minute = ((minute+time)%60)
    print('%d %d' %(hour, minute))
elif hour+((minute+time)//60)>23:
    hour = hour+((minute+time)//60)-24
    minute = ((minute+time)%60)
    print('%d %d' %(hour, minute))
else:
    print('%d %d' %(hour, minute+time))