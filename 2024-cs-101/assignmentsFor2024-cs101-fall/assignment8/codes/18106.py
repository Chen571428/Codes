#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    n = int(input())
    mat = [[0 for _ in range(n)] for __ in range(n)]
    def putRight(i,j,recNum):
        mat[i][j] = recNum + 1
        if j + 1 < n and mat[i][j+1] == 0:
            putRight(i,j+1,recNum + 1)
        elif mat[i+1][j] == 0:
            putDown(i+1,j,recNum + 1)

    def putDown(i,j,recNum):
        mat[i][j] = recNum + 1 
        if i + 1 < n and mat[i+1][j] == 0:
            putDown(i+1,j,recNum + 1)
        elif mat[i][j-1] == 0:
            putLeft(i,j-1,recNum + 1)
    
    def putLeft(i,j,recNum):
        mat[i][j] = recNum + 1 
        if j - 1 >= 0 and mat[i][j-1] == 0:
            putLeft(i,j-1,recNum + 1)
        elif mat[i-1][j] == 0:
            putUp(i-1,j,recNum + 1)

    def putUp(i,j,recNum):
        mat[i][j] = recNum + 1 
        if i - 1 >= 0 and mat[i-1][j] == 0:
            putUp(i-1,j,recNum + 1)
        elif mat[i][j+1] == 0:
            putRight(i,j+1,recNum + 1)
    putRight(0,0,0)
    for _ in mat:
        for x in _:
            print(x,end=' ')
        print('')
if __name__=="__main__":
    main()
