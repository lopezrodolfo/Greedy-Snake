# Greedy Snake Game

A Python implementation of the classic Snake game using Tkinter for the graphical user interface.

## Description

This project implements a Snake game with a Model-View-Controller (MVC) architecture. The game features a snake that moves around a grid, eating food to grow longer. The player's goal is to grow the snake as long as possible without colliding with the walls or the snake's own body.

## Authors

- Rodolfo Lopez
- Justin de Sousa

## Date

Spring 2020

## Features

- Graphical user interface using Tkinter
- Start, pause, and reset game functionality
- Adjustable game speed
- Wraparound mode toggle
- Score tracking (points, time, and points per second)
- Game over detection

## Files

- `snake7.py`: Main game file containing the Snake (controller), SnakeView, and SnakeModel classes
- `snake.py` to `snake7.py`: Iterative development versions of the game

## How to Run

1. Ensure you have Python installed on your system (Python 3.x recommended).
2. Clone or download this repository.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the game using the command:

   ```
   python snake7.py
   ```

## Controls

- Use the arrow keys to change the snake's direction.
- Click the "Start" button to begin the game.
- Click the "Pause" button to pause the game.
- Use the "Step Speed" slider to adjust the game speed.
- Click the "Reset" button to restart the game.
- Click the "Quit" button to exit the game.
- Toggle the "Wraparound" checkbox to enable/disable wraparound mode.

## Development

The game was developed iteratively, with each version (`snake.py` to `snake7.py`) adding new features and refining the implementation. The final version is `snake7.py`, which includes all features and the complete MVC architecture.

## Testing

The `SnakeModelTest` class in `snake7.py` includes unit tests for the game model. To run the tests, you can use a testing framework like unittest or pytest.

## Future Improvements

- Add difficulty levels
- Implement high score tracking
- Add sound effects and background music
- Create power-ups or obstacles
