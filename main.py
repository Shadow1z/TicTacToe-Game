import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)  # Set the window to a fixed size
        self.window.geometry("450x450")  # Set the window size to 450x450 pixels
        self.window.configure(background="black")  # Set the background to black
        self.player_turn = "X"

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6, font=("Arial", 24), bg="black", fg="white")
                button.grid(row=i, column=j, padx=10, pady=10)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.player_turn == "X":
                self.buttons[row][column].config(fg="red")
            else:
                self.buttons[row][column].config(fg="blue")
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def reset_game(self):
        self.player_turn = "X"
        for row in self.buttons:
            for button in row:
                button['text'] = ""
                button.config(fg="white")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()