#@Nickname: Chen571428
#@StuNum: 2400934013
from queue import Queue

def main():
    n, m = [int(x) for x in input().split()]
    mat = [input().split() for x in range(n)]

    # dist = [[-0x3f3f3f3f for _ in range(m)] for __ in range(n)]

    def bfs(si,sj):# SPFA ??!
        if mat[si][sj] == '1':
            return 0
        steps = [[0x3f3f3f3f for _ in range(m)] for __ in range(n)]
        steps[si][sj] = 0
        vis = {(si,sj):1}
        q = Queue()
        q.put((si,sj))

        valid = lambda x,y: x >= 0 and y >= 0 and x < n and y < m
        next = lambda cx,cy: [(cx+1,cy),(cx,cy+1),(cx-1,cy),(cx,cy-1)]
        ans = 0x3fffffff
        while q.qsize():
                (cx,cy) = q.get()
                vis[(cx,cy)] = 0
                
                for (nx,ny) in next(cx,cy):
                    if valid(nx,ny):
                        if mat[nx][ny] != '2' and steps[cx][cy] +1 <= steps[nx][ny] :
                            steps[nx][ny] = steps[cx][cy] + 1
                            if mat[nx][ny] == '1':
                                ans = min(ans,steps[cx][cy] +1)
                            if not vis.get((nx,ny)) or vis[(nx,ny)] == 0:
                                q.put((nx,ny))
                                vis[(nx,ny)] = 1
        return 'NO' if ans == 0x3fffffff else ans

    print(bfs(0,0))

if __name__=="__main__":
    main()