#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    n=int(input())
    print(len([1 for x in range(n) if input().count('1') > 1 ]))
if __name__=="__main__":
    main()