n = int(input())
arr = list(map(int, input().split()))

nums = set(arr)
longest = 0
for x in nums:
    if x-1 not in nums:
        current = x
        length = 1
        while current + 1 in nums:
            current += 1
            length += 1

        longest = max(longest, length)
print(longest)


