#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    n ,m ,a=[int(x) for x in input().split()]
    print((((n // a) + (1 if (n % a) else 0)) * ((m // a) + (1 if m % a else 0))))


if __name__=="__main__":
    main()