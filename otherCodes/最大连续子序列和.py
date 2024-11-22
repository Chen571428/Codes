#@Nickname: Chen571428
#@StuNum: 2400934013

def main():
    a = [int(x) for x in input().split()]
    # 输入到一个list
    sum = [0] 
    # 最前面预留一位，避免取sum[0-1]时取到不合适的值

    for i in range(len(a)):
        sum.append(sum[i] + a[i])
    # 求前缀和：到i前面所有元素的和(i本身除外)
    # sum[i+1] = sum[i] + a[i]
    ans = -2147483647 # 初始答案设为负无穷（用比较大的负数代替）
    for i in range(len(a)):
        for j in range(i): # 只要枚举1到i的起点就可以啦
            ans = max(sum[i+1] - sum[j],ans) 
            # 当前区间的和与答案比较，比答案大就更新答案
            # 注意sum[i] 表示 [0,i)范围的元素的和
            # [0,i+1) - [0,j) = [j,i]
    
    print(ans) # 输出就好啦

if __name__=="__main__":
    main()