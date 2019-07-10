heights = list()
h_sum = 0
for i in range(0, 9):
    heights.append(int(input()))
    h_sum += heights[i]

for i in range(0, 9):
    for j in range(i, 9):
        if (h_sum - heights[i] - heights[j]) == 100:
            one, two = i, j
            break

del heights[two], heights[one]
heights.sort()

for i in range(0, 7):
    print(heights[i])