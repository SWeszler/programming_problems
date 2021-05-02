from typing import List
from collections import defaultdict
from itertools import product

def plates_bf_itertools(N: int, K: int, P: int, stacks: List[List]):
    """The most naive approach to solve the Plates problem from Google KickStart 2020 Round A"""
    res = 0

    for p in product(range(K + 1), repeat=N):
        if sum(p) == P:
            s = 0
            for i, np in enumerate(p):
                s += sum(stacks[i][:np])
            res = max(res, s)

    return res


def plates_bf_my_product(N: int, K: int, P: int, stacks: List[List]):
    res = 0

    def product(set_len, n_sets):
        """ Iteratively generate all permutations with repetition."""
        res = [[]]
        for n in range(n_sets):
            new_res = []
            for x in res:
                for y in range(set_len + 1):
                    new_res.append(x + [y])
            res = new_res
        return res

    def product_recursive(set_len, n_sets):
        """Recursively generate all permutations with repetition."""
        if n_sets == 0:
            return [[]]
        res = []
        for y in range(set_len + 1):
            for x in product_recursive(set_len, n_sets - 1):
                res.append(x + [y])
        return res

    for p in product_recursive(K, N):
        if sum(p) == P:
            s = 0
            for i, np in enumerate(p):
                s += sum(stacks[i][:np])
            res = max(res, s)
    return res


def plates_bf_0(N: int, K: int, P: int, stacks: List[List]):
    res = 0

    def combinations(n_stacks, plates_to_pick):
        if n_stacks == 0:
            return [[]]
        res = []
        for y in range(min(plates_to_pick, K)):
            for x in combinations(n_stacks - 1, plates_to_pick - y):
                res.append(x + [y])

        return res

    for p in combinations(N, P + 1):
        s = 0
        for i, np in enumerate(p):
            s += sum(stacks[i][:np])
        res = max(res, s)
    return res

def plates_bf(N: int, K: int, P: int, stacks: List[List]):

    def findMax(n_stacks, plates_to_pick):
        if n_stacks < 0 or plates_to_pick <= 0:
            return 0

        max_val = findMax(n_stacks - 1, plates_to_pick)

        s = 0
        for y in range(min(plates_to_pick, K)):
            s += stacks[n_stacks][y]
            max_val = max(max_val, s + findMax(n_stacks - 1, plates_to_pick - y - 1))

        return max_val

    return findMax(N - 1, P)


def plates_mem(N: int, K: int, P: int, stacks: List[List]):
    """Dynamic Programming - Memoization"""
    dp = defaultdict(lambda: defaultdict(int))

    def findMax(n_stacks, plates_to_pick):
        if dp[n_stacks][plates_to_pick]:
            return dp[n_stacks][plates_to_pick]

        if n_stacks < 0 or plates_to_pick <= 0:
            return 0

        max_val = findMax(n_stacks - 1, plates_to_pick)

        s = 0
        for y in range(min(plates_to_pick, K)):
            s += stacks[n_stacks][y]
            max_val = max(max_val, s + findMax(n_stacks - 1, plates_to_pick - y - 1))

        dp[n_stacks][plates_to_pick] = max_val
        return max_val

    return findMax(N - 1, P)


def plates_dp(N: int, K: int, P: int, stacks: List[List]):
    """Dynamic Programming - Intermediate State"""
    sums = [[0 for j in range(K + 1)] for i in range(N + 1)]
    dp = [[0 for j in range(P + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            sums[i][j] = stacks[i - 1][j - 1]
            sums[i][j] += sums[i][j - 1]

    for i in range(1, N + 1):
        for j in range(1, P + 1):
            for x in range(min(j + 1, K + 1)):
                dp[i][j] = max(dp[i][j], sums[i][x] + dp[i - 1][j - x])

    return dp[-1][-1]