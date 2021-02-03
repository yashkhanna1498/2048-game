import random
from tkinter import Frame, Label, CENTER

import logic
import constants as c


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)

        # self.gamelogic = gamelogic
        self.commands = {c.KEY_UP: logic.move_up, c.KEY_DOWN: logic.move_down,
                         c.KEY_LEFT: logic.move_left, c.KEY_RIGHT: logic.move_right,
                         c.KEY_UP_ALT: logic.move_up, c.KEY_DOWN_ALT: logic.move_down,
                         c.KEY_LEFT_ALT: logic.move_left,
                         c.KEY_RIGHT_ALT: logic.move_right}

        self.cells = []
        self.initialize_game()
        self.initialize_matrix()
        self.update_matrix()

        self.mainloop()

    def initialize_game(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,
                           width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                             width=c.SIZE / c.GRID_LEN,
                             height=c.SIZE / c.GRID_LEN)
                cell.grid(row=i, column=j, padx=c.GRID_PADDING,
                          pady=c.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=c.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.cells.append(grid_row)

    def gen(self):
        return random.randint(0, c.GRID_LEN - 1)

    def initialize_matrix(self):
        self.matrix = logic.start_game(4)
        self.history_matrixs = list()
        self.matrix = logic.add_new_two(self.matrix)
        self.matrix = logic.add_new_two(self.matrix)

    def update_matrix(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.cells[i][j].configure(
                        text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.cells[i][j].configure(text=str(
                        new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self, event):
        key = repr(event.char)
        if key == c.KEY_BACK and len(self.history_matrixs) > 1:
            self.matrix = self.history_matrixs.pop()
            self.update_matrix()
            print('back on step total step:', len(self.history_matrixs))
        elif key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = logic.add_new_two(self.matrix)
                # record last move
                self.history_matrixs.append(self.matrix)
                self.update_matrix()
                done = False
                if logic.get_current_state(self.matrix) == 'WIN':
                    self.cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.cells[1][2].configure(
                        text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logic.game_state(self.matrix) == 'LOST':
                    self.cells[1][1].configure(
                        text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.cells[1][2].configure(
                        text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2


game2048 = Game2048()


