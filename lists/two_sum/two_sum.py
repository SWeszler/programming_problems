from itertools import combinations, permutations, product
nums = [1,2,3]

print("All 2-length combinations from nums:")
res = []
for i, n1 in enumerate(nums):
    for j in range(i + 1, len(nums)):
        res.append((n1, nums[j]))
print(res)
print("")

print("All 2-length combinations from nums - itertools.combinations:")
print(list(combinations(nums, 2)))
print("")

print("All 2-length permutations without repetitions of nums:")
res = []
for i, n1 in enumerate(nums):
    for j in range(i + 1, len(nums)):
        res.append((n1, nums[j]))
        res.append((nums[j], n1))
print(res)
print("")

print("All 2-length permutations without repetitions of nums - itertools.permutations:")
print(list(permutations(nums, 2)))
print("")

print("All 2-length permutations with repetition of nums:")
res = []
for n1 in nums:
    for n2 in nums:
        res.append((n1, n2))
print(res)
print("")

print("All 2-length permutations with repetition of nums - itertools.product:")
print(list(product(nums, repeat=2)))
print("")


print("All 3-length combinations from 4-nums:")
res = []
nums = [1,2,3,4]
for i, n1 in enumerate(nums):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            res.append((n1, nums[j], nums[k]))
print(res)