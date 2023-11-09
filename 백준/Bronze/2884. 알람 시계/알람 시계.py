hour, minute = map(int, input().split())
if hour==0 and minute<45:
    print('%d %d' %(23, 60-(45-minute)))
elif minute<45:
    print('%d %d' %(hour-1, 60-(45-minute)))
else:
    print("%d %d" %(hour, minute-45))