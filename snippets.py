def prefix_sum(nums):
    """
    Prefix Sum
    """
    ps = [0]

    for n in nums:
        ps.append(ps[-1] + n)

    return ps


def double_shorter_list(A, B):
    """
    Double values of shorter list in place.
    This function doesn't return anything, it's changing values of given reference to the list.
    """
    short = A
    if len(A) > len(B):
        short = B

    for i in range(len(short)):
        short[i] *= 2


def remove_odds(nums):
    """
    DO NOT DO USE THIS!
    Remove odd values in place, using while loop and 'del'.
    Time complexity is close to O(n^2), deletion takes O(n).
    """
    i = 0
    while i < len(nums):
        if nums[i] % 2:
            del nums[i]
        else:
            i += 1


