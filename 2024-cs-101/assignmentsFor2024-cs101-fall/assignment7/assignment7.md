# Assignment \#7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>

**说明：**

1）⽉考： AC6<mark>（请改为同学的通过数）</mark> 。考试题⽬都在"题库（包括计概、数算题目）"⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧"作业评论"。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。

## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

代码：

``` python
#@Nickname: Chen571428
#@StuNum: 2400934013
import functools
def cmp(a,b):
    if a[0]>b[0]:
        return -1
    elif a[0]==b[0]:
        return a[2]<b[2]
    else:
        return 1
def main():
    info ,pq ,cnt,I,age,inputPatient= [], [],0,1,0,[]
    N= int(input())
    while I <= N:
        inputPatient = input().split()
        age = int(inputPatient[1])
        if age >= 60:
            pq.append((age,inputPatient[0],I))
        else:
            info.append(inputPatient[0])
        I += 1
    pq.sort(key=functools.cmp_to_key(cmp))
    [print(i[1]) for i in pq]
    [print(i) for i in info]
if __name__=="__main__":
    main()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

<figure>
<img
src="https://github.com/Chen571428/picx-images-hosting/raw/master/image.51e61qm6qz.webp"
alt="image" />
<figcaption aria-hidden="true">image</figcaption>
</figure>

### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

代码：

``` python
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
                    ans.dat[i][j] += self.dat[i][k] *  mat2.dat[k][j]
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
```

代码运行截图 ==（至少包含有"Accepted"）==

<figure>
<img
src="https://github.com/Chen571428/picx-images-hosting/raw/master/image.1lbuas08n2.webp"
alt="image" />
<figcaption aria-hidden="true">image</figcaption>
</figure>

### M18182: 打怪兽

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

代码：

``` python
#@Nickname: Chen571428
#@StuNum: 2400934013
from queue import PriorityQueue as pq
def main():
    nCases, caseNum= int(input()) , 1
    while caseNum <= nCases:
        n, m, b = [int(x) for x in input().split()]
        tkNum ,tks,tking,flag,tkset= 1,{0:pq()},[],False,{0:0}
        while tkNum <= n:
            tick, damage= [int(x) for x in input().split()]
            if not tkset.get(tick):
                tkset[tick] = 1
                tking.append(tick)
            if not tks.get(tick):
                tks[tick] = pq()
            tks[tick].put(-damage)
            tkNum +=1
        tking.sort()
        for tick in tking:
            for i in range(min(tks[tick].qsize(),m)):
                b += tks[tick].get()
                if b <= 0:
                    print(tick)
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print("alive")
        caseNum += 1
if __name__=="__main__":
    main()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![image](https://github.com/Chen571428/picx-images-hosting/raw/master/image.5tr1kn41pi.webp)

### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

代码：

``` python
#@Nickname: Chen571428
#@StuNum: 2400934013
def mkSure(x):
    if len(x) == 0:
        return 0x3f3f3f3f
    else:
        return min(x)
def main():
    n ,m = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    if m == 0:
        if 0 in values:
            print(1)
        else:
            print(-1)
        return
    minimalizedCoinNums = [0x3f3f3f3f if x not in values else 1 for x in range(m+5)]
    for conValue in range(1,m+1):
        minimalizedCoinNums[conValue] = min(minimalizedCoinNums[conValue],mkSure([minimalizedCoinNums[conValue - value] + 1 for value in values if conValue - value > 0]))
    print(minimalizedCoinNums[m] if minimalizedCoinNums[m] != 0x3f3f3f3f else -1)
if __name__=="__main__":
    main()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

<figure>
<img
src="https://github.com/Chen571428/picx-images-hosting/raw/master/image.2objlqe1jd.webp"
alt="image" />
<figcaption aria-hidden="true">image</figcaption>
</figure>

### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

代码：

``` python
#@Nickname: Chen571428
#@StuNum: 2400934013
unitNum = 'thousand million'
singleNum = 'zero  one  two  three  four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen  seventeen  eighteen  nineteen  twenty  thirty  forty  fifty  sixty  seventy  eighty  ninety'
numOfStr  = {
        'zero':0, 'one' :1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
        'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
        'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,
        'hundred':100,'thousand':1000,'million':1000000

    }
def main():
    ans ,flag ,currentSingleNum= 0 , 1 , 0
    numStr = input().split()
    if numStr[0] == 'negative':
        flag = -1
        del numStr[0]
    while len(numStr) >0:
        while len(numStr) > 0 and numStr[0] in singleNum:
            currentSingleNum += numOfStr[numStr[0]]
            del numStr[0]
        if len(numStr) == 0:
            ans += currentSingleNum
            break
        elif numStr[0] == 'hundred':
            currentSingleNum = currentSingleNum * numOfStr[numStr[0]]
            del numStr[0]
            if len(numStr) == 0:
                ans += currentSingleNum
                break
        else:
            ans += currentSingleNum * numOfStr[numStr[0]]
            del numStr[0]
            currentSingleNum = 0
    print(ans*flag)
  
if __name__=="__main__":
    main()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

<figure>
<img
src="https://github.com/Chen571428/picx-images-hosting/raw/master/image.ic507ibtq.webp"
alt="image" />
<figcaption aria-hidden="true">image</figcaption>
</figure>

### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

代码：

``` python
#@Nickname: Chen571428
#@StuNum: 2400934013
def mkSure(x):
    if len(x) == 0:
        return 0
    return max(x)
  
def main():
    n = int(input())
    ans = 0
    shorttestEventStartTimeOfEnd, maxEventsEndedIn= [-1] * 61, [0] * 61
    while n > 0:
        startT , endT = [int(x) for x in input().split()]
        shorttestEventStartTimeOfEnd[endT] = max(shorttestEventStartTimeOfEnd[endT],startT)
        n -= 1
  
    if shorttestEventStartTimeOfEnd[0] == 0:
        maxEventsEndedIn[0] = 1
    i = 1
    while i <= 60:
        if shorttestEventStartTimeOfEnd[i] != -1:
            maxEventsEndedIn[i] = maxEventsEndedIn[shorttestEventStartTimeOfEnd[i]-1]+1
        maxEventsEndedIn[i] = max(maxEventsEndedIn[i],maxEventsEndedIn[i-1])
        i += 1
    print(maxEventsEndedIn[60])
  
if __name__=="__main__":
    main()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

<figure>
<img
src="https://github.com/Chen571428/picx-images-hosting/raw/master/image.2a53v9lqf0.webp"
alt="image" />
<figcaption aria-hidden="true">image</figcaption>
</figure>

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ"计概2024fall每日选做"、CF、LeetCode、洛谷等网站题目。</mark>
