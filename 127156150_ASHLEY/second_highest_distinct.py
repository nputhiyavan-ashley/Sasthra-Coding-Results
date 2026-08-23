n = int(input())
arr = list(map(int, input().split()))

highest = None
second_highest = None

for x in arr:
    if highest is None or x > highest:
        second_highest = highest
        highest = x
    elif x != highest and (second_highest is None or x > second_highest):
        second_highest = x

if second_highest is None:
    print("NA")
else:
    index = arr.index(second_highest)
    print(second_highest, index)