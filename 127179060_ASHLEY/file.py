//enter no of elements
n = int(input())
//enter elements in array
arr = list(map(int, input().split()))

first_index = {}

for i in range(n):
    value = arr[i]

    if value in first_index:
        distance = i - first_index[value]
        print(value, distance)
        break
    else:
        first_index[value] = i
else:
    print("NONE")
