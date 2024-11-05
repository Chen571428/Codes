#@Nickname: Chen571428
#@StuNum: 2400934013

def arrange(n,pos,rec):
    if(pos == n):
        print(rec[:len(rec)-1])
        return
    else:
        [arrange(n,pos+1,rec+nxt+' ') for nxt in [str(x) for x in range(1,n+1)] if nxt not in rec]
def main():
    n = int(input())
    ans=''
    arrange(n,0,ans)
if __name__=="__main__":
    main()