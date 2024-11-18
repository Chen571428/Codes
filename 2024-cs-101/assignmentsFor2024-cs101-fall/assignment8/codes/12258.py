#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    n,m = [int(x) for x in input().split()]
    si ,sj ,ans = 0 , 0 , 0
    mat = [input().split() for _ in range(n)]
    vis = {}
    flag = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '1':
                si ,sj = i,j
                flag = 1
                break
        if flag:
            break
    
    def dfs(i,j):
        nonlocal ans
        vis[(i,j)] = 1
        ans += 4
        for (x,y) in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
            if x < n and y < m and x >= 0 and y >= 0:
                if mat[x][y] == '1':
                    ans -= 1
                    if not vis.get((x,y)):
                        dfs(x,y)
    
    dfs(si,sj)
    print(ans)
    




if __name__=="__main__":
    main()
