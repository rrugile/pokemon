# Pokémon Top Trumps Game

## Introduction

This is a text-based Pokémon Top Trumps game that utilizes the [PokéAPI](https://pokeapi.co/) to fetch random Pokémon and their attributes. The game allows a player to select a Pokémon, choose a stat, and compete against an opponent (computer) to determine the winner.

## Features

- Fetches random Pokémon using PokéAPI.
- Allows the player to select a Pokémon from a list of three.
- Players choose a stat (ID, height, or weight) to compete against an opponent.
- The game consists of three rounds, and the player with the most wins emerges victorious.
- A high-score tracking system records the longest winning streak.

## How to Play

1. Run the script.
2. Choose an option from the menu:
   - **[1] Play the game**
   - **[2] View high scores**
   - **[3] Exit the game**
3. If playing, select a Pokémon from the provided list.
4. Choose a stat (**ID**, **height**, or **weight**) to compare with the opponent.
5. The round winner is determined based on the chosen stat.
6. The game continues for three rounds, and the overall winner is declared.
7. High scores are saved and can be viewed later.

## Requirements

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

```sh
# Clone this repository
git clone https://github.com/rrugile/pokemon.git

# Navigate to the project directory
cd pokemon

# Install dependencies
pip install requests

# Run the game
python main.py
```

## File Structure

```
├── main.py           # Main game script
├── high_scores.txt   # Stores high scores
```

## Future Improvements

- Add more Pokémon (extend beyond 151)
- Implement graphical interface
- Add multiplayer mode

