#@Nickname: Chen571428
#@StuNum: 2400934013

def mkSure(x):
    if len(x) == 0:
        return 0
    return max(x)

def main():
    n = int(input())
    ans = 0
    shorttestEventStartTimeOfEnd, maxEventsEndedIn= [-1] * 61, [0] * 61
    while n > 0:
        startT , endT = [int(x) for x in input().split()]
        shorttestEventStartTimeOfEnd[endT] = max(shorttestEventStartTimeOfEnd[endT],startT)
        n -= 1

    if shorttestEventStartTimeOfEnd[0] == 0:
        maxEventsEndedIn[0] = 1
    i = 1
    while i <= 60:
        if shorttestEventStartTimeOfEnd[i] != -1:
            maxEventsEndedIn[i] = maxEventsEndedIn[shorttestEventStartTimeOfEnd[i]-1]+1
        maxEventsEndedIn[i] = max(maxEventsEndedIn[i],maxEventsEndedIn[i-1])
        i += 1
    
    print(maxEventsEndedIn[60])

if __name__=="__main__":
    main()