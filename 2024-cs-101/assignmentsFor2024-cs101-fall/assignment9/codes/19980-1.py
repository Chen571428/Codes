#@Nickname: Chen571428
#@StuNum: 2400934013
from queue import Queue as PriorityQueue

def main():
    n, m = [int(x) for x in input().split()]
    mat = [input().split() for x in range(n)]

    dist = [[0x3f3f3f3f for _ in range(m)] for __ in range(n)]

    def bfs(si,sj):# SPFA ??! --> Dij
        dist[si][sj] = 0
        q = PriorityQueue()
        q.put((0,(si,sj)))
        vis = set()
        vis.add((si,sj))
        ans = 0x3f3f3f3f

        while q.qsize():
            (curDist,(cx,cy)) = q.get()
            vis.remove((cx,cy))
            if mat[cx][cy] == '1':
                ans = min(dist[cx][cy],ans)
            for (nx,ny) in [(cx+1,cy),(cx,cy+1),(cx-1,cy),(cx,cy-1)]:
                if nx >= 0 and ny >= 0 and nx < n and ny < m and mat[nx][ny] != '2':
                    if curDist + 1 < dist[nx][ny]:
                        dist[nx][ny] = curDist + 1
                        
                        if (nx,ny) not in vis:
                            vis.add((nx,ny))
                            q.put((dist[nx][ny],(nx,ny)))
        return 'NO' if ans == 0x3f3f3f3f else ans


    print(bfs(0,0))

if __name__=="__main__":
    main()