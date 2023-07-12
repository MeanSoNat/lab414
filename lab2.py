import os
os.system('clear')
n = 3
dp = [[0 for i in range(1,7)] for i in range(n+1)]
for i in range(2, n+1):
    for j in range(1,7):
        dp[1][i] += j
        print(dp)