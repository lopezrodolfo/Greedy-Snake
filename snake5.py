"""
Module: snake5

Author: Rodolfo Lopez and Justin de Sousa

Description: A Python implementation of greedy snake

Iteration 5: Connect user actions performed on the controls (in the SnakeView class)
to handler functions in the controller (the Snake class).
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

        # Set up the control

        # Start
        self.view.set_start_handler(self.start_handler)

        # Pause
        self.view.set_pause_handler(self.pause_handler)

        # Step speed
        self.view.set_step_speed_handler(self.step_speed_handler)

        # Reset
        self.view.set_reset_handler(self.reset_handler)

        # Quit
        self.view.set_quit_handler(self.quit_handler)

        # Wrap around
        self.view.set_wrap_around_handler(self.wrap_around_handler)

        # Change Direction
        self.view.set_change_direction(self.change_direction)

        # Start the simulation
        self.view.window.mainloop()

    def start_handler(self):
        """Start simulation"""
        print("Start simulation")

    def pause_handler(self):
        """Pause simulation"""
        print("Pause simulation")

    def step_speed_handler(self, value):
        """Adjust simulation speed"""
        print("Step speed: Value = %s" % (value))

    def reset_handler(self):
        """Reset simulation"""
        print("Reset simulation")

    def quit_handler(self):
        """Quit life program"""
        print("Quit program")

    def wrap_around_handler(self):
        """Toggles wrap around mode"""
        if self.view.status.get() == 1:
            print("Wrap around mode: on")
        else:
            print("Wrap around mode: off")

    def change_direction(self):
        pass


class SnakeView:
    def __init__(self, num_rows, num_cols):
        """Initialize view of the game"""
        # Constants
        self.CELL_SIZE = 20
        self.CONTROL_FRAME_HEIGHT = 100
        self.SCORE_FRAME_WIDTH = 200
        self.game_over_text = " "

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

        # Create frame for score, and put widgets in the frame
        self.score_frame = tk.Frame(
            self.window,
            width=self.SCORE_FRAME_WIDTH,
            height=num_rows * self.CELL_SIZE,
            borderwidth=1,
            relief="solid",
        )
        self.score_frame.grid(row=1, column=2)  # use grid layout manager
        self.score_frame.grid_propagate(False)
        (
            self.score_label,
            self.points_frame,
            self.points_label,
            self.time_frame,
            self.time_label,
            self.points_per_sec_frame,
            self.points_per_sec_label,
            self.game_over_label,
        ) = self.add_score()

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
        Create control buttons, slider, and checkbox, and adds them to the control frame
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
        self.status = tk.IntVar()
        wrap_around_checkbox = tk.Checkbutton(
            self.control_frame, text="Wraparound", variable=self.status
        )
        wrap_around_checkbox.grid(row=1, column=6)

        # Vertically center the controls in the control frame
        self.control_frame.grid_rowconfigure(1, weight=1)

        # Horizontally center the controls in the control frame
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.control_frame.grid_columnconfigure(2, weight=1)
        self.control_frame.grid_columnconfigure(3, weight=1)
        self.control_frame.grid_columnconfigure(4, weight=1)
        self.control_frame.grid_columnconfigure(5, weight=1)
        self.control_frame.grid_columnconfigure(6, weight=1)

        return (
            start_button,
            pause_button,
            step_speed_slider,
            reset_button,
            quit_button,
            wrap_around_checkbox,
        )

    def add_score(self):
        """
        Creates labels and frames, and adds them to the score frame
        """
        score_label = tk.Label(self.score_frame, text="Score")
        score_label.grid(row=1, column=1)

        points_frame = tk.Frame(self.score_frame, borderwidth=1, relief="solid")
        points_frame.grid(row=2, column=1)
        points_label = tk.Label(points_frame, text="Points:")
        points_label.grid(row=1, column=1)

        time_frame = tk.Frame(self.score_frame, borderwidth=1, relief="solid")
        time_frame.grid(row=3, column=1)
        time_label = tk.Label(time_frame, text="Time:")
        time_label.grid(row=1, column=1)

        points_per_sec_frame = tk.Frame(self.score_frame, borderwidth=1, relief="solid")
        points_per_sec_frame.grid(row=4, column=1)
        points_per_sec_label = tk.Label(points_per_sec_frame, text="Points Per Sec:")
        points_per_sec_label.grid(row=1, column=1)

        game_over_label = tk.Label(self.score_frame, text=self.game_over_text)
        game_over_label.grid(row=5, column=1)

        # Horizontally center the widgets in the score frame
        self.score_frame.grid_columnconfigure(1, weight=1)

        # Vertically center the widgets in the score frame
        self.score_frame.grid_rowconfigure(1, weight=1)
        self.score_frame.grid_rowconfigure(2, weight=1)
        self.score_frame.grid_rowconfigure(3, weight=1)
        self.score_frame.grid_rowconfigure(4, weight=1)
        self.score_frame.grid_rowconfigure(5, weight=1)

        return (
            score_label,
            points_frame,
            points_label,
            time_frame,
            time_label,
            points_per_sec_frame,
            points_per_sec_label,
            game_over_label,
        )

    def set_start_handler(self, handler):
        """set handler for clicking on start button to the function handler"""
        self.start_button.configure(command=handler)

    def set_pause_handler(self, handler):
        """set handler for clicking on pause button to the function handler"""
        self.pause_button.configure(command=handler)

    def set_step_speed_handler(self, handler):
        """set handler for dragging the step speed slider to the function handler"""
        self.step_speed_slider.configure(command=handler)

    def set_reset_handler(self, handler):
        """set handler for clicking on reset button to the function handler"""
        self.reset_button.configure(command=handler)

    def set_quit_handler(self, handler):
        """set handler for clicking on quit button to the function handler"""
        self.quit_button.configure(command=handler)

    def set_wrap_around_handler(self, handler):
        """set handler for clicking on the wrap around checkbox to the function handler"""
        self.wrap_around_checkbox.configure(command=handler)

    def set_change_direction(self, handler):
        """set handler to change snake's direction"""
        pass


if __name__ == "__main__":
    snake_game = Snake()
