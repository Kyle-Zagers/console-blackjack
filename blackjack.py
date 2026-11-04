from p1_random import P1Random

# Creating variables to track the stats of the game.
player_wins = 0
dealer_wins = 0
ties = 0

# Setting up variables for the loop that runs the game.
exit_option = False
game_number = 1
rng = P1Random()
card_total = 0


# Summoning cards and telling the player their hand.
def game_on(total):
    card = rng.next_int(13) + 1
    total += card if card <= 10 else 10

    if card == 1:
        card = "ACE"
    if card == 11:
        card = "JACK"
    if card == 12:
        card = "QUEEN"
    if card == 13:
        card = "KING"

    print(f"\nYour card is a {card}!")
    print(f"Your hand is: {total}")
    return total


# Calculates the winner of the game based on their cards and increments the win stats of the game.
def calc_win(player, dealer, wins, tie, losses):
    if dealer > 21:
        if player <= 21:
            wins += 1
            print("You win!")
        if player > 21:
            tie += 1
            print("It's a tie! No one wins!")
    elif dealer <= 21:
        if 21 >= player > dealer:
            wins += 1
            print("You win!")
        if player <= 21 and dealer > player:
            losses += 1
            print("Dealer wins!")
        if player <= 21 and player == dealer:
            tie += 1
            print("It's a tie! No one wins!")
    else:
        print("error")  # error message
    return wins, tie, losses


# Prints the game number for the first game.
# Only time game number increments is when stats are selected, blackjack, or exceeding 21.
print(f"START GAME #{game_number}")

# Variable that tells the loop if it is preserving the result from game_on.
# Only preserves when player requests stats or when they enter an invalid input.
preserve = False


# Primary loop for the game which calls the prior functions based on player input and other factors.
# Also increments stats and handles output if the player gets blackjack or exceeds 21.
while not exit_option:
    option = 0

    if not preserve:
        card_total = game_on(card_total)
    else:
        preserve = False

# Increments stats and handles output if the player gets blackjack or exceeds 21.
    if card_total == 21:
        print("\nBLACKJACK! You win!")
        player_wins += 1
        game_number += 1
        card_total = 0
        print(f"\nSTART GAME #{game_number}")
        option = 1
    elif card_total > 21:
        print("\nYou exceeded 21! You lose.")
        dealer_wins += 1
        game_number += 1
        card_total = 0
        print(f"\nSTART GAME #{game_number}")
        option = 1
    else:
        print("\n1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit")
        option = int(input("\nChoose an option: "))

# Output and logic for player input.
    if option == 4:
        exit_option = True

    if option == 2:
        dealerHand = rng.next_int(11)+16
        print(f"\nDealer's hand: {dealerHand}")
        print(f"Your hand is: {card_total}\n")
        player_wins, ties, dealer_wins = calc_win(card_total, dealerHand, player_wins, ties, dealer_wins)
        card_total = 0
        game_number += 1
        print(f"\nSTART GAME #{game_number}")

    if option == 3:
        print(f"\nNumber of Player wins: {player_wins}")
        print(f"Number of Dealer wins: {dealer_wins}")
        print(f"Number of tie games: {ties}")
        print(f"Total # of games played is: {game_number - 1}")
        print(f"Percentage of Player wins: {(player_wins / (game_number - 1)) * 100}%")
        preserve = True

    if option <= 0 or option >= 5:
        print("Invalid input!\nPlease enter an integer value between 1 and 4.")
        preserve = True
