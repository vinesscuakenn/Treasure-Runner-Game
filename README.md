Treasure Runner - Python Terminal Game
Files included in this single file for easy copy-paste to your GitHub repo:
- treasure_runner.py (this file contains the game code)
- README.md (printed below and also can be written by running with --write-readme)


If you want separate files, run:
python treasure_runner.py --write-readme
which will create README.md in the current directory.

Have fun! If you publish to GitHub Sponsors, consider adding the README content as-is.

README.md
===========
# Treasure Runner


**Treasure Runner** is a lightweight, text-based, roguelite-style terminal game written in Python. Dash through a tiny dungeon, avoid monsters, collect treasure, and reach the exit! Perfect for showing off on GitHub or GitHub Sponsors.

## Features
- Simple keyboard controls (WASD or arrow keys)
- Procedurally generated small dungeons
- Monsters that move toward the player
- Items: treasure (+score), health potion
- Saveable high score
- No external dependencies (pure Python, works in Windows/macOS/Linux terminal)

## How to play
1. Clone the repo and run `python treasure_runner.py`.
2. Move with `W A S D` or arrow keys.
3. Collect `T` (treasure) to increase your score.
4. Pick up `P` (potion) to restore health.
5. Avoid monsters `M` — if they catch you, it's game over.
6. Reach `E` (exit) to complete a level; levels get harder.

## Controls
- `W` / Up arrow — move up
- `S` / Down arrow — move down
- `A` / Left arrow — move left
- `D` / Right arrow — move right
- `Q` — quit

## Files
- `treasure_runner.py` — game code
- `README.md` — this README (auto-writable)
- `highscores.json` — created automatically when you finish a game

## License
MIT License — See LICENSE file or add one on your repo.

## Sponsor
If you enjoy this little game, consider sponsoring the project on GitHub Sponsors to support further features and improvements!