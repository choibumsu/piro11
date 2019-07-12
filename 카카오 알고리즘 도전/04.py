import copy


class kakao4:
    def __init__(self, height, width, board):
        self.height = height
        self.width = width
        self.board = board
        self.board_trans = self.transform_board()
        while self.delete_point(self.check_point()):
            pass
        self.print_result()

    def transform_board(self):
        trans_board = []

        for i in range(0, self.width):
            tmp_list = []
            for j in range(self.height - 1, -1, -1):
                tmp_list.append(self.board[j][i])
            trans_board.append(list())
            trans_board[i] = copy.deepcopy(tmp_list)
            tmp_list.clear()
        return trans_board

    def check_point(self):
        check = []
        for i in range(0, self.width - 1):
            for j in range(0, min(len(self.board_trans[i]), len(self.board_trans[i + 1])) - 1):
                logic1 = (self.board_trans[i][j] == self.board_trans[i][j + 1])
                logic2 = (self.board_trans[i + 1][j] == self.board_trans[i + 1][j + 1])
                logic3 = (self.board_trans[i][j] == self.board_trans[i + 1][j])

                if logic1 and logic2 and logic3:
                    check.append([i, j])
                    check.append([i, j + 1])
                    check.append([i + 1, j])
                    check.append([i + 1, j + 1])

        check = [item for i, item in enumerate(check) if item not in check[:i]]
        check.sort(key=(lambda elem: elem[1]))

        if len(check) == 0:
            return False
        else:
            return check

    def delete_point(self, check):
        if not check:
            return False
        else:
            for i in range(len(check) - 1, -1, -1):
                del self.board_trans[check[i][0]][check[i][1]]
            return True

    def print_result(self):
        result = 0
        for i in range(0, self.width):
           result += len(self.board_trans[i])
        result = self.width * self.height - result
        print(result)


kakao4(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'])
# m, n = map(int, input().split())
# game = []
# for i in range(m):
#     game.append(input())
# kakao4(m, n, game)