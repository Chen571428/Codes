#@Nickname: Chen571428
#@StuNum: 2400934013
# def Solve_Greedy():
#     while n := int(input()):
#         tianHorse = sorted([int(x) for x in input().split()],reverse=True)
#         kingHorse = sorted([int(x) for x in input().split()],reverse=True)

#         ans = 0
#         while len(tianHorse) and len(kingHorse):
#             if tianHorse[0] > kingHorse[0]:
#                 del tianHorse[0],kingHorse[0]
#                 ans += 1
#             elif tianHorse[-1] > kingHorse[-1]:
#                 del tianHorse[-1],kingHorse[-1]
#                 ans += 1
#             elif tianHorse[-1] < kingHorse[0]:
#                 ans -= 1 
#                 del tianHorse[-1],kingHorse[0]
#             else: # 平局
#                 del tianHorse[-1],kingHorse[0]
#         print(ans * 200)

def Solve_DP():
    while n := int(input()):
        tianHorse = sorted([int(x) for x in input().split()],reverse=True)
        kingHorse = sorted([int(x) for x in input().split()],reverse=True)

        ans = 0
        dp = [[0 for _ in range(n+3)] for __ in  range(2)]
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