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
        if nums[i] < nums[i-1] and dp[up][0] + 1 >= dp[down][0]:
            dp[down][0] = dp[up][0] + 1
            dp[down][1] = i
            
        if nums[i] > nums[i-1] and dp[down][0] + 1 >= dp[up][0]:
            dp[up][0] = dp[down][0] + 1
            dp[up][1] = i
    
    print(max(dp[down][0],dp[up][0]))
        
if __name__=="__main__":
    main()