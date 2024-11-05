# Assignment #6: Recursion and DP


## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image|300](https://github.com/Chen571428/picx-images-hosting/raw/master/image.175e3wvkmb.webp)




### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
def arrange(n,pos,rec):
    if(pos == n):
        print(rec[:len(rec)-1])
        return
    else:
        [arrange(n,pos+1,rec+nxt+' ') for nxt in [str(x) for x in range(1,n+1)] if nxt not in rec]
def main():
    n = int(input())
    ans=''
    arrange(n,0,ans)
if __name__=="__main__":
    main()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image|300](https://github.com/Chen571428/picx-images-hosting/raw/master/image.10268hu36e.webp)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
'''
A N^2 solution which is over-dped.States before N is not need for the answer
 

def makeSure(a):
    if len(a) == 0:
        return 1
    else:
        return max(a)
def main():
    k = int(input())
    missieHeights ,f = [],[]
    [missieHeights.append(int(x)) for x in input().split()]
    [f.append(1 if x == 0 else makeSure([f[x-t] + 1 for t in range(1,x+1) if missieHeights[x-t] >= missieHeights[x]])) for x in range(k)]
    print(max(f))
if __name__=="__main__":
    main()
'''

# A better version uses greedy.Only using the smallest number to maintain the longest non-lowering seq always gives the right answer.
# Unfortunately ,using PyPy3 ,first foo version is almost 50 ms faster than the second version.
# don't know why
from bisect import bisect_right
def main():
        k = int(input())
        missieHeights = list(map(int,input().split()))
        missieHeights.reverse()

        defensedMissies = [missieHeights[0]]

        for i in range(1,len(missieHeights)):
            pos = bisect_right(defensedMissies,missieHeights[i])
            if pos < len(defensedMissies):
                 defensedMissies[pos] = missieHeights[i]
            else:
                 defensedMissies.append(missieHeights[i])
        
        print(len(defensedMissies))

if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![image|400](https://github.com/Chen571428/picx-images-hosting/raw/master/image.9nzso5gmmq.webp)


### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
import functools
weight, price, selected, ansRec, N, B = [], [], [], {}, 0, 0

def maxSure(x):
    if len(x):
        return max(x)
    else:
        return 0
@functools.lru_cache(maxsize=None,typed=False)
def biggestBaggedPrice(baggedVolume,baggedPrice,selection):
    global N, B, price, weight, selected, ansRec
    if ansRec.get(baggedVolume,0):
        return ansRec[baggedVolume]
    elif baggedVolume == 0:
        return baggedPrice
    else:
        selected.append(selection)
        ansRec[baggedVolume] = maxSure([biggestBaggedPrice(baggedVolume - weight[i],baggedPrice + price[i],i) for i in range(N) if baggedVolume - weight[i] >= 0 and i not in selected])
        selected.pop()
        return ansRec[baggedVolume]
        
def main():
    global N,B,price,weight
    N,B    = [int(x) for x in input().split()]
    price  = [int(x) for x in input().split()]
    weight = [int(x) for x in input().split()]
    print(biggestBaggedPrice(B,0,''))
    
if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image|400](https://github.com/Chen571428/picx-images-hosting/raw/master/image.lvqibqrjv.webp)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
import functools
ans = []
def search_answer(n,procQueenLine,ansRec,occuMarker1,occuMarker2):
    global ans
    if(procQueenLine == n+1):
        ans.append(int(ansRec))
        return
    else:
        if(len(ansRec)):
            x ,y = procQueenLine-1, int(ansRec[len(ansRec)-1])
            # [occuMarker.append((x+_,y))   for _ in range(1,n+1)]
            # [occuMarker.append((x+_,y+_)) for _ in range(1,n+1)]
            # [occuMarker.append((x+_,y-_)) for _ in range(1,n+1)]
            occuMarker1.append(x+y)
            occuMarker2.append(x-y)         
	        [search_answer(n,procQueenLine+1,ansRec+'{}'.format(_),occuMarker1,occuMarker2)for _ in range(1,9) if (str(_) not in ansRec) and (procQueenLine + _ not in occuMarker1) and (procQueenLine - _ not in occuMarker2)]
	        
        if(len(ansRec)):
            del occuMarker1[-1],occuMarker2[-1]
def main():
    global ans
    n = int(input())
    search_answer(8,1,'',[],[])
    ans.sort()
    [print(ans[int(input())-1]) for x in range(n)]
if __name__=="__main__":
	main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image|400](https://github.com/Chen571428/picx-images-hosting/raw/master/image.1vynobzwnb.webp)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：



代码：

```python
#@Nickname: Chen571428
#@StuNum: 2400934013
#Almost The Same As poj23421
def maxSure(x):
    if len(x):
        return max(x)
    else:
        return 0
def main():
    N, a, b, c = [int(x) for x in input().split()]
    biggestCuttedPieces = {0:0, a:1, b:1, c:1}
    for length in range(0,N+1):
        for cutting in (a,b,c):
            if length + cutting > N :
                continue
            elif biggestCuttedPieces.get(length,0):
                biggestCuttedPieces[length + cutting] = max((biggestCuttedPieces[length] + 1,biggestCuttedPieces.get(length + cutting,0)))
            else:
                continue
    print(biggestCuttedPieces[N])
if __name__=="__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![image|400](https://github.com/Chen571428/picx-images-hosting/raw/master/image.969qzq531m.webp)


## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>




