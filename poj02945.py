#@Nickname: Chen571428
#@StuNum: 2400934013
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