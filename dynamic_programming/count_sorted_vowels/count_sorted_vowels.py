def count_sorted_vowels_bf(N):
    perms = ['']
    vowels = 'aeiou'
    res = 0

    for i in range(N):
        new_perms = []
        for s in perms:
            for v in vowels:
                new_perms.append(s + v)
        perms = new_perms

    for s in perms:
        if s == "".join(sorted(s)):
            res += 1

    return res


def count_sorted_vowels_dp(N):
    dp = [[1] * 6] + [[0] * 6 for i in range(N)]

    for i in range(1, N + 1):
        for j in range(1, 6):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
