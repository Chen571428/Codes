#@Nickname: Chen571428
#@StuNum: 2400934013
class matrix:
    def __init__(self,info,n):
        self.n = n
        self.dat = [[0 for i in range(n)] for j in range(n)]
        for i in info:
            self.dat[i[0]][i[1]] = i[2]
    def print(self):
        i,j = 0,0
        while i < self.n:
            j = 0
            while j < self.n:
                if self.dat[i][j] != 0:
                    print(f'{i} {j} {self.dat[i][j]}')
                j += 1
            i += 1
    def __mul__(self,mat2):
        ans = matrix([],self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    ans.dat[i][j] += self.dat[i][k] *  mat2.dat[k][j]
        return ans

def main():
    N ,m1,m2= [int(x) for x in input().split()]
    info = []
    [info.append([int(x) for x in input().split()]) for _ in range(m1)]
    mat1 = matrix(info,N)
    
    info = []
    [info.append([int(x) for x in input().split()]) for _ in range(m2)]
    mat2 = matrix(info,N)

    (mat1*mat2).print()
    

if __name__=="__main__":
    main()