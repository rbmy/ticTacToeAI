class BoardState:

    def __init__(self):
        self.board = [["blank", "blank", "blank"],
                      ["blank", "blank", "blank"],
                      ["blank", "blank", "blank"]]

    def is_blank(self) -> bool:
        return self.board[0] == self.board[1] == self.board[2] == ["blank", "blank", "blank"]

    def is_draw(self) -> bool:
        for row in range(0, 3):
            for column in range(0, 3):
                if self.board[row][column] == "blank":
                    return False
        return True

    def move(self, x, y, token):
        self.board[x][y] = token

    def winning_row(self, token) -> bool:
        for row in range(0, 3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == token:
                return True
        return False

    def winning_column(self, token) -> bool:
        for column in range(0, 3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] == token:
                return True
        return False

    def winning_diagonal(self, token) -> bool:
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == token or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] == token:
            return True
        return False

    def __str__(self):
        string = ""
        for row in self.board:
            string += "["
            for token in row:
                string += f"\t{token},\t "
            string += "]\n"
        return string
