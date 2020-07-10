from typing import List
from collections import defaultdict
from itertools import product

def plates_bf_itertools(N: int, K: int, P: int, stacks: List[List]):
    """The most naive approach to solve the Plates problem from Google KickStart 2020 Round A"""
    res = 0

    for p in product(range(K + 1), repeat = N):
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


def plates_bf(N: int, K: int, P: int, stacks: List[List]):
    res = 0

    def combinations(k_plates, n_stacks, plates_to_pick):
        if n_stacks == 0:
            return [[]]
        res = []
        for y in range(min(plates_to_pick, k_plates)):
            for x in combinations(k_plates, n_stacks - 1, plates_to_pick - y):
                res.append(x + [y])

        return res

    for p in combinations(K + 1, N, P + 1):
        print(p)
        s = 0
        for i, np in enumerate(p):
            s += sum(stacks[i][:np])
        res = max(res, s)
    return res


def plates_mem(N: int, K: int, P: int, stacks: List[List]):
    """Dynamic Programming Memoization technique"""
    res = 0
    dp = defaultdict(lambda: defaultdict(int))

    def find_max(curr_stk, K, plates_left):
        """Using defaultdict as cache"""
        if dp[curr_stk][plates_left]:
            return dp[curr_stk][plates_left]

        if plates_left <= 0 or curr_stk < 0:
            return 0

        max_b = find_max(curr_stk - 1, K, plates_left)
        curr_b = 0
        for i in range(min(plates_left, K)):
            curr_b += stacks[curr_stk][i]
            max_b = max(max_b, curr_b + find_max(curr_stk - 1, K, plates_left - i - 1))

        dp[curr_stk][plates_left] = max_b
        return max_b
        
    res = find_max(N - 1, K, P)
    return res


def plates_dp(N: int, K: int, P: int, stacks: List[List]):
    """Dynamic Programming - intermediate state"""
    res = 0
    return res
