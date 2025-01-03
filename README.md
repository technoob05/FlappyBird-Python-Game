# FlappyBird Python Game

A Python implementation of the classic Flappy Bird game using Pygame. The game features a bird that players can control to navigate through pipes while trying to achieve the highest score possible.

## Features

- Smooth bird animation with multiple sprite states (upflap, midflap, downflap)
- Dynamic pipe obstacles with random heights
- Score tracking system
- Gravity-based gameplay mechanics
- Collision detection
- Night theme background
- Game over and restart functionality
## Demo
![image](https://github.com/user-attachments/assets/1a843403-0418-4644-8617-4853ebb2a6e6)

## Technologies Used

- Python 3.x
- Pygame library
- Built-in libraries:
  - sys
  - random
- TrueType font (04B_19)

## Project Structure

```
FlappyBird/
│
├── assets/           # Game assets folder
├── sound/           # Sound effects folder
│
├── FlappyBirth.py   # Main game file (5 KB)
├── game.py          # Basic pygame setup file (0 KB)
├── 04B_19           # TrueType font file (7 KB)
├── background-night # Background image (6 KB)
├── FlappyBirth.sln  # Visual Studio Solution file (1 KB)
└── FlappyBirth      # Python project files (3 KB)
```

## Installation

1. Make sure you have Python installed on your system
2. Install Pygame if you haven't already:
```bash
pip install pygame
```
3. Clone this repository or download the source code
4. Ensure all assets and sound files are in their respective folders

## How to Play

1. Run the game using Python:
```bash
python FlappyBirth.py
```
2. Press SPACEBAR to make the bird flap and start the game
3. Navigate through the pipes without hitting them
4. Try to achieve the highest score possible
5. When you crash, press SPACEBAR to restart

## Game Controls

- SPACEBAR: Make the bird flap/jump
- SPACEBAR (after game over): Restart the game

## Technical Features

- Screen Resolution: 432x768 pixels
- FPS: 120
- Gravity System: Constant acceleration of 0.2
- Pipe Spawn Interval: 1200ms
- Bird Animation Interval: 200ms

## Game Mechanics

- The bird continuously falls due to gravity
- Each successful pipe passage awards 1 point
- Game ends when the bird:
  - Collides with pipes
  - Hits the ground
  - Flies too high (above the screen)

## Development Environment

The game was developed using Visual Studio with Python support, as indicated by the .sln solution file. However, you can run and modify the game using any Python IDE or text editor of your choice.

## Contributing

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature suggestions.

## Credits

This game is inspired by the original Flappy Bird game created by Dong Nguyen. Assets and game mechanics are reimagined for educational purposes.
