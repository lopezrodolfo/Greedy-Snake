"""
Module: snake2

Author: Rodolfo Lopez and Justin de Sousa

Description: A Python implementation of greedy snake

Iteration 2: Put cells in the grid frame
"""

import tkinter as tk


class Snake:
    """This is the controller"""

    def __init__(self):
        """Initializes the snake game"""
        # Define parameters
        self.NUM_ROWS = 30
        self.NUM_COLS = 30

        # Create view
        self.view = SnakeView(self.NUM_ROWS, self.NUM_COLS)

        # Start the simulation
        self.view.window.mainloop()


class SnakeView:
    def __init__(self, num_rows, num_cols):
        """Initialize view of the game"""
        # Constants
        self.CELL_SIZE = 20
        self.CONTROL_FRAME_HEIGHT = 100
        self.SCORE_FRAME_WIDTH = 200

        # Size of grid
        self.num_rows = num_rows
        self.num_cols = num_cols

        # Create window
        self.window = tk.Tk()
        self.window.title("Greedy Snake")

        # Create frame for grid of cells, and put cells in the frame
        self.grid_frame = tk.Frame(
            self.window,
            width=num_cols * self.CELL_SIZE,
            height=num_rows * self.CELL_SIZE,
        )
        self.grid_frame.grid(row=1, column=1)  # use grid layout manager
        self.cells = self.add_cells()

        # Create frame for controls
        self.control_frame = tk.Frame(
            self.window,
            width=num_cols * self.CELL_SIZE + self.SCORE_FRAME_WIDTH,
            height=self.CONTROL_FRAME_HEIGHT,
            bg="blue",
        )
        self.control_frame.grid(
            row=2, column=1, columnspan=2
        )  # use grid layout manager

        # Create frame for score
        self.score_frame = tk.Frame(
            self.window,
            width=self.SCORE_FRAME_WIDTH,
            height=num_rows * self.CELL_SIZE,
            bg="green",
        )
        self.score_frame.grid(row=1, column=2)  # use grid layout manager

    def add_cells(self):
        """Add cells to the grid frame"""
        cells = []
        for r in range(self.num_rows):
            row = []
            for c in range(self.num_cols):
                frame = tk.Frame(
                    self.grid_frame,
                    width=self.CELL_SIZE,
                    height=self.CELL_SIZE,
                    borderwidth=1,
                    relief="solid",
                )
                frame.grid(row=r, column=c)  # use grid layout manager
                row.append(frame)
            cells.append(row)
        return cells


if __name__ == "__main__":
    snake_game = Snake()
