import random, requests
from datetime import datetime

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

   #then get the player_choice stat based on chosen Pokemon:
    # ensure input validation is in place by running everything in a loop
    chosen_pokemon = None #{'pokemon': "stats"}
    while not chosen_pokemon:
        player_poke_choice = input(f"Choose a Pokémon from the list: {', '.join(pokemon_names)}: ")
        for pokemon in player_pokemons:
            if pokemon['name'] == player_poke_choice:
                chosen_pokemon = pokemon
                print("\nAwesome choice!\n")
                print(f"Here are the stats of your chosen Pokemon: {chosen_pokemon}")
                break #for improved code quality (if no break then loop continues looking for 'name' in multi_poke list even after finding it)
        if not chosen_pokemon:
            print("Please input a valid Pokemon name.\n")


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
        return 'win'
    
    elif player_wins_count < opponent_wins_count:
        print("Tough luck! You lost the game.")
        return 'lose'

    else:
        print("There game ended in a draw!")
        return 'draw'

def high_scores():
    longest_streak = 0
    current_streak = 0

    #loop through the game to allow player keep their streak
    while True:
        result = multi_round_game()

        # if game is won then increment current_streak
        if result == 'win':
            current_streak += 1
        # if game is lost then reset current_streak
        elif result == 'lose':
            current_streak == 0
        # if game is a draw then do not change current_streak
        else:
            pass

        if current_streak > longest_streak:
            longest_streak = current_streak
        
        #ask if player wants to keep playing the game
        #if answer is not yes then streak is lost
        play_again = input("Would you like to play again and continue your streak? [yes/no]: ")
        if play_again != 'yes':
            break

    #create and open a new file to store high_scores
    with open('high_scores.txt', 'w+') as file:
        #get the current_time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        #add an entry of longest_streak
        file.write(f"Longest streak of wins: {longest_streak} at {current_time}\n")

def view_high_scores():
    with open("best_scores.txt", "r") as file:
        contents = file.read()
        print(contents)

def menu():
    print("[1] Play the game")
    print("[2] View high scores")
    print("[3] Exit the game")

menu()
option = int(input("Enter your option: "))

while option != 3:
    if option == 1:
        high_scores()

    elif option == 2:
        view_high_scores()

    else:
        "Please enter a valid option"

    print()
    menu()
    option = int(input("Enter your option: "))

print()
print("Thank you for playing! Goodbye.\n")
