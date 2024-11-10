#@Nickname: Chen571428
#@StuNum: 2400934013
def mkSure(x):
    if len(x) == 0:
        return 0x3f3f3f3f
    else:
        return min(x)


def main():
    n ,m = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    if m == 0:
        if 0 in values:
            print(1)
        else:
            print(-1)
        return
    
    minimalizedCoinNums = [0x3f3f3f3f if x not in values else 1 for x in range(m+5)]

    for conValue in range(1,m+1):
        minimalizedCoinNums[conValue] = min(minimalizedCoinNums[conValue],mkSure([minimalizedCoinNums[conValue - value] + 1 for value in values if conValue - value > 0]))

    print(minimalizedCoinNums[m] if minimalizedCoinNums[m] != 0x3f3f3f3f else -1)

if __name__=="__main__":
    main()