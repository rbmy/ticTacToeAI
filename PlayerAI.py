import random
from BoardState import BoardState


class PlayerAI:

    def __init__(self, token):
        self.token = token
        self.opponent = None

    def random_move(self, board_state: BoardState) -> BoardState:
        has_not_moved = True
        while has_not_moved:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            if board_state.board[row][column] == "blank":
                board_state.move(row, column, self.token)
                print(f"Next move:\n{board_state}")
                return board_state

    def deliberate(self, board_state: BoardState) -> BoardState:
        if board_state.is_blank():
            board_state.move(random.randint(0, 2), random.randint(0, 2), self.token)
            print(f"Next move:\n{board_state}")
            return board_state
        else:
            next_move = (0, board_state)

            for row in range(0, 3):
                for column in range(0, 3):
                    if board_state.board[row][column] == "blank":
                        board_state.move(row, column, self.token)
                        winning_score = self.minimax(board_state, True, 0)

                        if winning_score > next_move[0]:
                            next_move = (winning_score, board_state)
                        else:
                            board_state.move(row, column, "blank")

            print(f"Next move:\n{next_move[1]}")
            return next_move[1]

    def minimax(self, board_state, my_turn: bool, depth: int) -> int:
        if self.winner(board_state):
            return 1
        elif self.opponent.winner(board_state):
            return -1
        elif board_state.is_draw():
            return 0

        for row in range(0, 3):
            for column in range(0, 3):
                if board_state.board[row][column] == "blank":
                    if my_turn:
                        board_state.move(row, column, self.token)
                        score = max(1, self.minimax(board_state, False, depth+1)) - depth
                    else:
                        board_state.move(row, column, self.opponent.token)
                        score = min(-1, self.minimax(board_state, True, depth+1)) + depth
                    board_state.move(row, column, "blank")
                    return score

    def winner(self, board_state: BoardState) -> bool:
        return board_state.winning_row(self.token) or \
            board_state.winning_column(self.token) or \
            board_state.winning_diagonal(self.token)
