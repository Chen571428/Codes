#@Nickname: Chen571428
#@StuNum: 2400934013
def main():
    d = int(input())
    n = int(input())
    size = 1025
    mat = [[0 for _ in range(size)]for __ in range(size)]
    cnt = 0
    precurprefixSum = [[0 for _ in range(size+1)]for __ in range(size)]
    prefixSum =  [[0 for _ in range(size+1)]for __ in range(size+1)]
    while cnt < n:
        x,y,i = [int(x) for x in input().split()]
        mat[x][y] = i
        cnt += 1
    i,j = 0,0
    while i < size:
        j = 0
        while j < size:
            precurprefixSum[i][j+1] = precurprefixSum[i][j] + mat[i][j]
            j += 1
        i += 1


    i,j = 0,0
    
    while j < size +1:
        i = 0
        while i < size:
            prefixSum[i+1][j] = prefixSum[i][j] + precurprefixSum[i][j]
            i += 1
        j += 1
    
    maxAnsCnt , maxAns = 0,0
    i,j = 0,0
    while i < size:
        j = 0
        while j < size:
            sum = (prefixSum[min(i + d +1,size)][min(j+ d +1,size)] - prefixSum[max(i-d,0)][min(j+d+1,size)]) - \
                    (prefixSum[min(i + d +1,size)][max(j-d,0)] - prefixSum[max(i-d,0)][max(j-d,0)])
            
            if sum > maxAns:
                maxAns = sum
                maxAnsCnt = 1
            elif sum == maxAns:
                maxAnsCnt += 1
            j += 1 
        i += 1
    
    print(f"{maxAnsCnt} {maxAns}")
if __name__=="__main__":
    main()