# m, n = map(int, input().split())
# board = []
# for i in range(m):
#     board.append(input())

m, n = 6, 6
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

for i in range(0, m):
    board[i] = list(board[i])

check = []

while True:
    for i in range(0, m - 1):
        j = 0
        while j < (n - 1):
            if board[i][j] != '0' and board[i][j] == board[i][j + 1] and board[i + 1][j] == board[i + 1][j + 1] and board[i][j] == board[i + 1][j]:
                tmp = [i, j]
                check.append(tmp)

            if board[i][j + 1] != board[i + 1][j + 1]:
                j += 2
            else:
                j += 1
    if len(check) == 0:
        break

    for i in range(0, len(check)):
        board[check[i][0]][check[i][1]] = '0'
        board[check[i][0] + 1][check[i][1]] = '0'
        board[check[i][0]][check[i][1] + 1] = '0'
        board[check[i][0] + 1][check[i][1] + 1] = '0'
    check.clear()

    for i in range(0, n):
        for j in range(m-1, 0, -1):
            while board[j][i] == '0':
                non_zero = 0
                for k in range(j, 0, -1):
                    if board[k-1][i] != '0':
                        non_zero += 1
                    board[k][i] = board[k-1][i]
                board[0][i] = '0'
                if non_zero == 0:
                    break

result = 0
for i in range(0, m):
    result += board[i].count('0')
print(result)