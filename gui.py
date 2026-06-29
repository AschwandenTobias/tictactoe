from tkinter import *
from tkinter import messagebox

import gamelogic as gl
from engines.random_engine import RandomEngine
from engines.perfect_player import PerfectPlayer


# "human", RandomEngine(), or PerfectPlayer()
white_player = PerfectPlayer()     
black_player = "human"  

game = gl.Game()
stop_game = False

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def clicked(row, col):
    global stop_game

    if stop_game:
        return

    # Only allow clicking if current player is human
    if game.white_turn and white_player != "human":
        return

    if not game.white_turn and black_player != "human":
        return

    move = (row, col)

    if not gl.move_validity(move, game):
        return

    gl.make_move(game, move)
    update_buttons()
    check_game_end()

    if not stop_game:
        root.after(300, ai_move_if_needed)


def ai_move_if_needed():
    global stop_game

    if stop_game:
        return

    if game.white_turn:
        if white_player == "human":
            return
        move = white_player.get_move(game)
    else:
        if black_player == "human":
            return
        move = black_player.get_move(game)

    gl.make_move(game, move)
    update_buttons()
    check_game_end()

    if not stop_game:
        root.after(300, ai_move_if_needed)


def update_buttons():
    for row in range(3):
        for col in range(3):
            value = game.board[row][col]

            if value == 1:
                buttons[row][col].configure(text="X")
            elif value == 2:
                buttons[row][col].configure(text="O")
            else:
                buttons[row][col].configure(text="")


def check_game_end():
    global stop_game

    if gl.somebody_won(game):
        stop_game = True

        if game.winner == 1:
            messagebox.showinfo("Winner", "X won!")
        else:
            messagebox.showinfo("Winner", "O won!")

    elif gl.is_game_over(game):
        stop_game = True
        messagebox.showinfo("Draw", "It's a draw!")


def restart_game():
    global game, stop_game

    game = gl.Game()
    stop_game = False
    update_buttons()

    root.after(300, ai_move_if_needed)


root = Tk()
root.title("Tic Tac Toe")
root.resizable(0, 0)

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(
            root,
            height=4,
            width=8,
            font=("Helvetica", 20),
            command=lambda r=i, c=j: clicked(r, c)
        )
        buttons[i][j].grid(row=i, column=j)

restart_button = Button(
    root,
    text="Restart",
    font=("Helvetica", 16),
    command=restart_game
)
restart_button.grid(row=3, column=0, columnspan=3, sticky="we")

root.after(300, ai_move_if_needed)
root.mainloop()