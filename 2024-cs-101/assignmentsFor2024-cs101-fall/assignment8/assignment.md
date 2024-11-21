# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image](https://github.com/Chen571428/picx-images-hosting/raw/master/image.1ap0q6brkw.webp)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：



代码：

```python
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
```



代码运行截图 ==（至少包含有"Accepted"）==

![image](https://github.com/Chen571428/picx-images-hosting/raw/master/image.2h8bysnkcg.webp)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
def main():
    d = int(input())
    n = int(input())
    size = 1025
    mat = [[0 for _ in range(size)]for __ in range(size)]
    cnt = 0
    precurprefixSum = [[0 for _ in range(size+1)]for __ in range(size)]
    prefixSum =  [[0 for _ in range(size+1)]for __ in range(size+1)]
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![image](https://Chen571428.github.io/picx-images-hosting/image.3nrn8wbj87.webp)




### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    n = int(input())
    nums = [int(x) for x in input().split()]
    dp = [[_ for _ in range(n)] for __ in range(2)]

    up , down = (0,1)

    dp[up][0] = 1
    dp[up][1] = 0
    dp[down][0] = 1
    dp[down][1] = 0
    for i in range(1,n):
        if nums[i] < nums[i-1] and dp[up][0] + 1 > dp[down][0]:
            dp[down][0] = dp[up][0] + 1
            dp[down][1] = i
        if nums[i] > nums[i-1] and dp[down][0] + 1 > dp[up][0]:
            dp[up][0] = dp[down][0] + 1
            dp[up][1] = i
    
    print(max(dp[down][0],dp[up][0]))
        
if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![image](https://github.com/Chen571428/picx-images-hosting/raw/master/image.45hoyg72in.png)




### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
  
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    maxA = max(a)
    minA = min(a)
  
    num = [0 for _ in range(maxA+5)]
    for i in a:
        num[i+3] += i # right shift for 3 nums .Easier to dp
  
    dp = [0 for _ in range(maxA+5)]
    for i in range(1,maxA+1):
        dp[i+3] = max(dp[i+3-2] + num[i+3],dp[i+3-3] + num[i+3])
    print(max(dp))
if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![image](https://github.com/Chen571428/picx-images-hosting/raw/master/image.1ap0sotjok.png)




### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
# def Solve_Greedy():
#     while n := int(input()):
#         tianHorse = sorted([int(x) for x in input().split()],reverse=True)
#         kingHorse = sorted([int(x) for x in input().split()],reverse=True)
  
#         ans = 0
#         while len(tianHorse) and len(kingHorse):
#             if tianHorse[0] > kingHorse[0]:
#                 del tianHorse[0],kingHorse[0]
#                 ans += 1
#             elif tianHorse[-1] > kingHorse[-1]:
#                 del tianHorse[-1],kingHorse[-1]
#                 ans += 1
#             elif tianHorse[-1] < kingHorse[0]:
#                 ans -= 1
#                 del tianHorse[-1],kingHorse[0]
#             else: # 平局
#                 del tianHorse[-1],kingHorse[0]
#         print(ans * 200)
  
def Solve_DP():
    while n := int(input()):
        tianHorse = sorted([int(x) for x in input().split()],reverse=True)
        kingHorse = sorted([int(x) for x in input().split()],reverse=True)
  
        ans = 0
        dp = [[0 for _ in range(n+3)] for __ in  range(2)]
        # stateij = 0
        # statei_1j = 0
        # stateij_1 = 0
        for i in range(n):
            for j in range(n):
                if tianHorse[i] > kingHorse[j]:
                    dp[1][j] = max([dp[0][j-1] + 1,dp[1][j-1] - 1,dp[0][j] - 1])
                elif tianHorse[i] == kingHorse[j]:
                    dp[1][j] = max([dp[0][j-1] + 0,dp[1][j-1] - 1,dp[0][j] - 1])
                else:
                    dp[1][j] = max([dp[0][j-1] - 1,dp[1][j-1] - 1,dp[0][j] - 1])
            dp[0] = [x for x in dp[1]]
  
        print(dp[1][n-1] * 200)
  
def main():
    Solve_DP()
    # Solve_Greedy()
  
if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![image](https://github.com/Chen571428/picx-images-hosting/raw/master/image.54xseyj53p.png)


## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>




