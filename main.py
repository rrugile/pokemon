'''
Option [1] 
Project Brief: Top Trumps 
In this project you'll create a small game where players compare stats, similar to the Top Trumps card game. The basic flow of the games is: 
1. You are given a random card with different stats 
2. You select one of the card's stats 
3. Another random card is selected for your opponent (the computer) 
4. The stats of the two cards are compared 
5. The player with the stat higher than their opponent wins 
The standard project will use the Pokemon API, but you can use a different API if you want after completing the required tasks. 
You will not need any additional knowledge beyond what is covered in this course to complete this project. 

Required Tasks 

These are the required tasks for this project. You should aim to complete these tasks before adding your own ideas to the project. 

1. Generate a random number between 1 and 151 to use as the Pokemon ID number 
# random library (x)
# get pokemon id using rand(1,151)

2. Using the Pokemon API get a Pokemon based on its ID number 
# import request
# request.get()
# url https://pokeapi.co/api/v2/pokemon/{    }/

3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (★ https://pokeapi.co/) 
# dict = {key:value}

4. Get a random Pokemon for the player and another for their opponent 
player_pokemon 
opponent_pokemon

5. Ask the user which stat they want to use (id, height or weight) 
get_input = input("")

6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    height
    players_stat > < =
for loop:

if else

'''

import random, requests
from pprint import pprint

def top_trumps():
    #get a random number
    #print the stats
#1. Generate a random number between 1 and 151 to use as the Pokemon ID number 
#2. Using the Pokemon API get a Pokemon based on its ID number 

    pokemon_id = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'

    #ask for response from API
    response = requests.get(url)

    #get info from API
    pokemon = response.json()

#3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (https://pokeapi.co/) 
    return {'name': pokemon['name'], 'id': pokemon['id'], 'height': pokemon['height'], 'weight': pokemon['weight']}
  
#4. Get a random Pokemon for the player and another for their opponent
def comparison():
    #get random number for the players
    #print out the outcome of the game
    player = top_trumps()
    opponent = top_trumps()

#5. Ask the user which stat they want to use (id, height or weight) 
    options = ['id', 'height', 'weight']
    player_choice = input("Choose a stat to use from id, height, weight: ")

# Allow the opponent (computer) to choose a stat that they would like to compare
    computer_choice = random.choice(options)

    #below code is referencing the specific stat directly from the json library
    player_stat = player[player_choice]

    opponent_stat = opponent[computer_choice]

#6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    if player_stat > opponent_stat:
        print(f"Player wins because opponent's stat was: {opponent_stat} and choice was: {computer_choice}")
    elif player_stat < opponent_stat:
        print(f"Player loses because opponent's stat was: {opponent_stat} and choice was: {computer_choice}")
    else:
        print("Draw")

comparison()


# Get multiple random Pokemon and let the player decide which one that they want to use

# Play multiple rounds and record the outcome of each round. The player with most number of rounds won, wins the game

# Record high scores for players and store them in a file
