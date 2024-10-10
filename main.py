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
#from pprint import pprint

def top_trumps():
    #get a random number
    #print the stats
#1. Generate a random number between 1 and 151 to use as the Pokemon ID number 
#2. Using the Pokemon API get a Pokemon based on its ID number 

    pokemon_id = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'

    #connect to the API
    response = requests.get(url)
    #check whether connection successful ( 200 = successful connection)
    #print(response.status_code)

    #get data from the API
    pokemon = response.json()

#3. Create a dictionary that contains the returned Pokemon's name, id, height and weight (https://pokeapi.co/) 
    return {'name': pokemon['name'], 'id': pokemon['id'], 'height': pokemon['height'], 'weight': pokemon['weight']}

#4. Get a random Pokemon for the player and another for their opponent  
def comparison():
# Get multiple random Pokemon and let the player decide which one they want to use
    number_pokemons = 3
    player_pokemons = []

    #retrieve data from API based on the number of pokemons needed using a for loop
    for i in range(number_pokemons):
        player_pokemons.append(top_trumps())

    #get random pokemon for the opponent (computer)
    opponent = top_trumps()

# Ask player which pokemon they want to use
    #must first extract only the names from the list of player_pokemons (which contains the dictionaries of each poke with its stats)
    pokemon_names = []
    for pokemon in player_pokemons:
        pokemon_names.append(pokemon['name'])

    #the above can also be rewritten as a list comprehension:
    #pokemon_names = [pokemon["name"] for pokemon in player_pokemons]

    #now print out the names, each on a new line, and ask which pokemon the player wants to use
    player_poke_choice = input(f"Choose a pokemon from the list: {", ".join(pokemon_names)}: ")

#5. Ask the user which stat they want to use (id, height or weight) 
    options = ['id', 'height', 'weight']

# Input validation: player makes a typo or chooses a non-existent stat
    #run an infinite loop
    while True:
        #ask for input
        player_choice = input("Choose a stat to use from id, height, weight: ")
        #if input is valid then break out of the infinite while loop
        if player_choice in options:
            break
        #if input is invalid print error message and continue the loop
        else:
            print("Please input a valid stat.")

# Allow the opponent (computer) to choose a stat
    computer_choice = random.choice(options)

    #below code is referencing the specific stat directly from the json library
    #get the player_choice stat from player_pokemons list based on the selected player_poke_choice name
    #to do this must first find the pokemon dictionary in player_pokemons based on the selected player_poke_choice
    chosen_pokemon = None
    for pokemon in player_pokemons:
        if pokemon['name'] == player_poke_choice:
            #store the dictionary from the player_pokemons in a chosen_pokemon variable
            chosen_pokemon = pokemon
            break
    #then, use the chosen_pokemon to find the player_choice stat and store it in player_stat
    player_stat = chosen_pokemon[player_choice]

    opponent_stat = opponent[computer_choice]

#6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
    if player_stat > opponent_stat:
        print(f"\nYou won this round because opponent's stat was: {opponent_stat} and choice was: {computer_choice}\n")
        #to be able to easily refer later when counting wins in the multi_round_game() function, return a keyword of who won the round
        return 'player'
    elif player_stat < opponent_stat:
        print(f"\nYou lost this round because opponent's stat was: {opponent_stat} and choice was: {computer_choice}\n")
        return 'opponent'
    else:
        print("\nDraw\n")
        return 'draw'

#comparison()

# Play multiple rounds and record the outcome of each round. The player with most number of rounds won, wins the game
    # call the comparison() function for a set number of times
    # for each time the comparison is called, log the outcome of the game into a player_wins_count and opponent_wins_count
    # compare the number of player_wins_count with opponent to print out who won the game
def multi_round_game():
    player_wins_count = 0
    opponent_wins_count = 0

    print("This is a 3 round game\n")
    print("Player who wins majority rounds will win the game!\n")
    print("Goodluck!\n")

    for i in range(3):
        result = comparison()

        if result == 'player':
            player_wins_count += 1
        elif result == 'opponent':
            opponent_wins_count+= 1
    
    if player_wins_count > opponent_wins_count:
        print("You won the game! Congratulations")
    
    elif player_wins_count < opponent_wins_count:
        print("Tough luck! You lost the game.")

    else:
        print("There game ended in a draw!")

multi_round_game()

# Record high scores for players and store them in a file
