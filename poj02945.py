#@Nickname: Chen571428
#@StuNum: 2400934013
'''
A N^2 solution which is over-dped.States before N is not need for the answer
 

def makeSure(a):
    if len(a) == 0:
        return 1
    else:
        return max(a)
def main():
    k = int(input())
    missieHeights ,f = [],[]
    [missieHeights.append(int(x)) for x in input().split()]
    [f.append(1 if x == 0 else makeSure([f[x-t] + 1 for t in range(1,x+1) if missieHeights[x-t] >= missieHeights[x]])) for x in range(k)]
    print(max(f))
if __name__=="__main__":
    main()
'''

# A better version uses greedy.Only using the smallest number to maintain the longest non-lowering seq always gives the right answer.
# Unfortunately ,using PyPy3 ,first foo version is almost 50 ms faster than the second version.
# don't know why
from bisect import bisect_right
def main():
        k = int(input())
        # missieHeights = list(map(int,input().split()))
        missieHeights = [int(x) for x in input().split()]
        missieHeights.reverse()

        defensedMissies = [missieHeights[0]]

        for i in range(1,k):
            pos = bisect_right(defensedMissies,missieHeights[i])
            if pos < len(defensedMissies):
                 defensedMissies[pos] = missieHeights[i]
            else:
                 defensedMissies.append(missieHeights[i])

        print(len(defensedMissies))

if __name__=="__main__":
    main()