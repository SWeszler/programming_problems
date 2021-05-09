def min_tickets_cost_bf(days, costs):

    def min_cost(day, i):
        if i >= len(days):
            return 0

        if days[i] < day:
            return min_cost(day, i + 1)

        cost = min(
            costs[0] + min_cost(days[i] + 1, i + 1),
            costs[1] + min_cost(days[i] + 7, i + 1),
            costs[2] + min_cost(days[i] + 30, i + 1)
        )
        return cost

    return min_cost(days[0], 0)


def min_tickets_cost_mem(days, costs):
    dp = {}

    def min_cost(day, i):
        if day in dp:
            return dp[day]

        if i >= len(days):
            return 0

        if days[i] < day:
            return min_cost(day, i + 1)

        cost = min(
            costs[0] + min_cost(days[i] + 1, i + 1),
            costs[1] + min_cost(days[i] + 7, i + 1),
            costs[2] + min_cost(days[i] + 30, i + 1)
        )

        dp[day] = cost
        return cost

    return min_cost(days[0], 0)


def min_tickets_cost_tab(days, costs):
    N = days[-1] + 1
    dp = [-1 for i in range(N)]
    for day in days:
        dp[day] = 0

    for i in range(N):
        if dp[i] == -1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[i - 1] + costs[0],
                dp[max(0, i - 7)] + costs[1],
                dp[max(0, i - 30)] + costs[2]
            )

    return dp[-1]
