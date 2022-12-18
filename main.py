from BoardState import BoardState
from PlayerAI import PlayerAI
import matplotlib.pyplot as mpt


def start() -> int:
    board_state = BoardState()

    print("Starting a new game. Initial configuration:")
    print(board_state)

    print("Initializing Player 1 using token X.")
    player_1 = PlayerAI("X")

    print("Initializing Player 2 using token O.\n")
    player_2 = PlayerAI("O")

    return play_game(player_1, player_2, board_state)


def play_game(player_1, player_2, board_state) -> int:
    player_1.opponent = player_2
    player_2.opponent = player_1

    print("Player 1 begins.")
    current_player = 1

    while not player_1.winner(board_state) and not player_2.winner(board_state) and not board_state.is_draw():
        if current_player == 1:
            board_state = player_1.deliberate(board_state)
            current_player = 2
        else:
            board_state = player_2.random_move(board_state)
            current_player = 1

    print(f"Winner is player: ")

    if player_1.winner(board_state):
        print(f"\tPlayer 1 with token {player_1.token}")
        return 1
    elif player_2.winner(board_state):
        print(f"\tPlayer 2 with token {player_2.token}")
        return 2
    else:
        print("\tDRAW")
        return 0


if __name__ == '__main__':
    players = ["Neither", "Player 1", "Player 2"]
    winners = [0, 0, 0]
    for games in range(100):
        winners[start()] += 1

    print("Stats:")
    print(f"\t Player 1 (with AI) won {100*winners[1]/100}% of the time.")
    print(f"\t Player 2 (random choice) won {100*winners[2] / 100}% of the time.")
    print(f"\t There was a draw {100*winners[0] / 100}% of the time.")

    mpt.bar(players, winners)
    mpt.title("Win percentage")
    mpt.xlabel("Player")
    mpt.ylabel("Winning percentage")
    mpt.show()
