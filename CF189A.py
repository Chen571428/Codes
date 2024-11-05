#@Nickname: Chen571428
#@StuNum: 2400934013
#Almost The Same As poj23421

def maxSure(x):
    if len(x):
        return max(x)
    else:
        return 0
        
def main():
    N, a, b, c = [int(x) for x in input().split()]
    biggestCuttedPieces = {0:0, a:1, b:1, c:1}
    for length in range(0,N+1):
        for cutting in (a,b,c):
            if length + cutting > N :
                continue
            elif biggestCuttedPieces.get(length,0):
                biggestCuttedPieces[length + cutting] = max((biggestCuttedPieces[length] + 1,biggestCuttedPieces.get(length + cutting,0)))
            else:
                continue
    print(biggestCuttedPieces[N])
if __name__=="__main__":
    main()