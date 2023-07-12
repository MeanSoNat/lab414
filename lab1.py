import os
os.system('clear')

def diceSum(n):

    dp = [[0 for i in range(n*6)]
          for i in range(n+1)]
    # print(dp)
    # print(len(dp[1])) # check len of possible value in dice
	
    # for single throwing
    for i in range(6):
        dp[1][i] = 1/6
    # print(dp)

    for i in range(2, n+1):
        # # check number of dice for loop in dimension arrays
        # print(i) 
        for j in range(len(dp[i-1])):
            for k in range(6):
                if(dp[i-1][j] != 0 and dp[i-1][k] != 0):
                    dp[i][j + k] += (dp[i - 1][j] * dp[1][k])
    print(dp)
    for i in range(len(dp[n]) - n + 1):
        print("%d %0.3f" % (i + n, dp[n][i]))
        
    # for i in range(len(dp)):
    #     print("For %s dice \n %s"%(i, dp[i]))
n = 3
diceSum(n)