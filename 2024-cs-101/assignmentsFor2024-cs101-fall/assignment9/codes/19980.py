#@Nickname: Chen571428
#@StuNum: 2400934013
from queue import Queue

def main():
    n, m = [int(x) for x in input().split()]
    mat = [input().split() for x in range(n)]

    # dist = [[-0x3f3f3f3f for _ in range(m)] for __ in range(n)]

    def bfs(si,sj):# SPFA ??!
        
        steps = [[0x3f3f3f3f for _ in range(m)] for __ in range(n)]
        steps[si][sj] = 0
        vis = set()
        vis.add((si,sj))
        q = Queue()
        q.put((si,sj))

        valid = lambda x,y: x >= 0 and y >= 0 and x < n and y < m
        next = lambda cx,cy: [(cx+1,cy),(cx,cy+1),(cx-1,cy),(cx,cy-1)]
        ans = 0x3f3f3f3f
        while q.qsize():
                (cx,cy) = q.get()
                vis.remove((cx,cy))
                if mat[cx][cy] == '1':
                    ans = min(ans,steps[cx][cy])
                for (nx,ny) in next(cx,cy):
                    if valid(nx,ny):
                        if mat[nx][ny] != '2' and steps[nx][ny] > steps[cx][cy] + 1:
                            steps[nx][ny] = steps[cx][cy] + 1
                            if (nx,ny) not in vis:
                                q.put((nx,ny))
                                vis.add((nx,ny))
        
        return f"{ans}" if ans != 0x3f3f3f3f else 'NO'

    print(bfs(0,0))

if __name__=="__main__":
    main()