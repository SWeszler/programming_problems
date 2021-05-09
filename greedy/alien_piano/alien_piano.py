def alien_piano(K, notes):
  A = [notes[i] for i in range(K) if i == 0 or notes[i - 1] != notes[i]]
  up_count = 0
  down_count = 0
  violations = 0

  for i in range(1, len(A)):
    if A[i] > A[i - 1]:
      up_count += 1
      down_count = 0
    else:
      down_count += 1
      up_count = 0
    if up_count > 3 or down_count > 3:
      violations += 1
      up_count = down_count = 0
  return violations


def alien_piano_bf(K, notes):

    def find_min(start, i):
        if i < 0:
            return K

        min_val = float('inf')

        down, up = 1, 5
        if 0 < i < K:
            if notes[i] > notes[i - 1]:
                down = start + 1
                up = 5
            elif notes[i] < notes[i - 1]:
                down = 1
                up = start

        breaks = 1
        if down >= up:
            breaks = 0
            down, up = 1, 5

        for c in range(down, up):
            min_val = min(min_val, find_min(c, i - 1) - breaks)

        return min_val
    
    mn = K
    for c in range(1, 5):
        mn = min(mn, find_min(c, K - 1))
    return mn


def alien_piano_mem(K, notes):
    dp = {}
    def find_min(start, i):
        if (start, i) in dp:
            return dp[start, i]
        if i < 0:
            return K

        min_val = float('inf')

        down, up = 1, 5
        if 0 < i < K:
            if notes[i] > notes[i - 1]:
                down = start + 1
                up = 5
            elif notes[i] < notes[i - 1]:
                down = 1
                up = start

        breaks = 1
        if down >= up:
            breaks = 0
            down, up = 1, 5

        for c in range(down, up):
            min_val = min(min_val, find_min(c, i - 1) - breaks)

        dp[start, i] = min_val
        return min_val
    
    mn = K
    for c in range(1, 5):
        mn = min(mn, find_min(c, K - 1))
    return mn


def alien_piano_dp(K, notes):
    dp = [[K for j in range(4)] for i in range(K)]

    for j in range(4):
        dp[0][j] = 0

    for i in range(1, K):
        for jp in range(4):
            for j in range(4):
                violation = 1
                if (notes[i] > notes[i - 1] and j > jp) or (notes[i] < notes[i - 1] and j < jp) or (notes[i] == notes[i - 1] and j == jp):
                    violation = 0
                dp[i][j] = min(dp[i][j], dp[i - 1][jp] + violation)

    return min(dp[-1])