#n = int(input())
#arr1 = list(map(int, input().split()))
#arr2 = list(map(int, input().split()))

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

result = [str(bin(arr1[i] | arr2[i]))[2:].zfill(n).replace("1", "#").replace("0", " ") for i in range(0, n)]

print(result)
