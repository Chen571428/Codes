#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    M,N =[int(x) for x in input().split()]
    ans=0
    if M == 1 and N == 1:
        print(0)
    elif M <= 2 and N <= 2 :
        print(N + M - 2)
    else:
        if M % 2:
            ans += N//2
        ans += (M // 2) * N
        print(ans)

if __name__=="__main__":
    main()