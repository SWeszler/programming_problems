
def knapsack(values, weights, W):
    dp = [[0 for j in range(W + 1)] for i in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    return dp[-1][-1]