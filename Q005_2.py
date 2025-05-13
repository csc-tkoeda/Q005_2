h, w = map(int, input().split())
# h = rows
# w = columns

gridA = []
gridB = []

for i in range(h):
    gridA.append(list(input()))

for i in range(h):
    gridB.append(list(input()))


def shift(grid, rows, cols):
    return [
        [grid[(rows + j) % h][(cols + i) % w] for i in range(w)] for j in range(h)
    ]


match = False
for i in range(h):
    for j in range(w):
        if shift(gridA, i, j) == gridB:
            match = True
            break
    if match:
        break

print("Yes" if match else "No")
