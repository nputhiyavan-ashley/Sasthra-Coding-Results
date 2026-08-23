r, c = map(int, input().split())

a = []
for i in range(r):
    a.append(list(map(int, input().split())))

s = 0
for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            s += a[i][j]
print(s) 