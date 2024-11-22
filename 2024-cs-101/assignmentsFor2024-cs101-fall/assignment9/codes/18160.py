#@Nickname: Chen571428
#@StuNum: 2400934013
from queue import Queue

def main():
    T = int(input()) + 1
    while T:= T-1:
        N ,M = [int(x) for x in input().split()]
        mat = [input() for _ in range(N)]

        vis = {}
        def bfs(startI,startJ):
            q = Queue()
            q.put((startI,startJ))
            vis[(startI,startJ)] = 1
            
            ans = 1
            valid = lambda x,y: x >= 0 and y >= 0 and x < N and y < M
            next = lambda cx,cy: [(cx+1,cy),(cx,cy+1),(cx-1,cy),(cx,cy-1),(cx+1,cy-1),(cx+1,cy+1),(cx-1,cy-1),(cx-1,cy+1)]

            while q.qsize():
                (cx,cy) = q.get()
                for (nx,ny) in next(cx,cy):
                    if valid(nx,ny):
                        if (not vis.get((nx,ny))) and mat[nx][ny] == 'W':
                            vis[(nx,ny)] = 1
                            ans += 1
                            q.put((nx,ny))

            return ans
        
        ans = 0
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 'W' and not vis.get((i,j)):
                    ans = max(ans,bfs(i,j))

        print(ans)


if __name__=="__main__":
    main()