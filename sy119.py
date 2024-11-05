#@Nickname: Chen571428
#@StuNum: 2400934013

ans=0
rec= []
def recans(start,end):
    global rec
    rec.append("{star}->{en}".format(star=start,en=end));

def move(n,s,t,m):
    global ans
    if n == 1:
        ans += 1
        recans(s,t)
        return
    if n <= 2:
        ans += 3
        recans(s,m)
        recans(s,t)
        recans(m,t)
        return
    move(n-1,s,m,t)
    ans += 1
    recans(s,t)
    move(n-1,m,t,s)

def main():
    global ans,rec
    n = int(input())
    move(n,'A','C','B')
    print('%d'%ans)
    [print(x) for x in rec]

if __name__=="__main__":
    main()