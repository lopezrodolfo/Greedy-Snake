"""
Module: snake3

Author: Rodolfo Lopez and Justin de Sousa

Description: A Python implementation of greedy snake

Iteration 3: Put controls in the control frame 
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

        # Create frame for controls, and put controls in the frame
        self.control_frame = tk.Frame(
            self.window,
            width=num_cols * self.CELL_SIZE + self.SCORE_FRAME_WIDTH,
            height=self.CONTROL_FRAME_HEIGHT,
            borderwidth=1,
            relief="solid",
        )
        self.control_frame.grid(
            row=2, column=1, columnspan=2
        )  # use grid layout manager
        self.control_frame.grid_propagate(False)
        (
            self.start_button,
            self.pause_button,
            self.step_speed_slider,
            self.reset_button,
            self.quit_button,
            self.wrap_around_checkbox,
        ) = self.add_control()

        # Create frame for score
        self.score_frame = tk.Frame(
            self.window,
            width=self.SCORE_FRAME_WIDTH,
            height=num_rows * self.CELL_SIZE,
            bg="green",
            borderwidth=1,
            relief="solid",
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

    def add_control(self):
        """
        Create control buttons and slider, and add them to the control frame
        """
        start_button = tk.Button(self.control_frame, text="Start")
        start_button.grid(row=1, column=1)
        pause_button = tk.Button(self.control_frame, text="Pause")
        pause_button.grid(row=1, column=2)
        step_speed_slider = tk.Scale(
            self.control_frame,
            from_=1,
            to=10,
            label="Step Speed",
            showvalue=0,
            orient=tk.HORIZONTAL,
        )
        step_speed_slider.grid(row=1, column=3)
        reset_button = tk.Button(self.control_frame, text="Reset")
        reset_button.grid(row=1, column=4)
        quit_button = tk.Button(self.control_frame, text="Quit")
        quit_button.grid(row=1, column=5)
        wrap_around_checkbox = tk.Checkbutton(self.control_frame, text="Wraparound")
        wrap_around_checkbox.grid(row=1, column=6)

        # Vertically center the controls in the control frame
        self.control_frame.grid_rowconfigure(1, weight=1)

        # Horizontally center the controls in the control frame
        self.control_frame.grid_columnconfigure(0, weight=1)
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.control_frame.grid_columnconfigure(2, weight=1)
        self.control_frame.grid_columnconfigure(3, weight=1)
        self.control_frame.grid_columnconfigure(4, weight=1)
        self.control_frame.grid_columnconfigure(5, weight=1)
        self.control_frame.grid_columnconfigure(6, weight=1)
        self.control_frame.grid_columnconfigure(7, weight=1)

        return (
            start_button,
            pause_button,
            step_speed_slider,
            reset_button,
            quit_button,
            wrap_around_checkbox,
        )


if __name__ == "__main__":
    snake_game = Snake()
