import random
import time

def txt(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Intro
txt("Welcome to the game!")
txt("The rules are simple: choose a number between 1 and 100.")
txt("Score the highest possible score to win.")
txt("If the score is too low, you lose.")
txt("Let's start the game...")
input("Press ENTER to continue...")

def main():
    player_points = 0
    opponent_points = 0
    rounds = 5
    cards = {
        "Attack Boost": "+1 point",
        "Shield": "No loss next round",
        "Double Points": "Next win gives 2 points",
        "Lose Turn": "Skip your next dice roll",
        "Steal Point": "Steal 1 point from opponent"
    }

    # Effect flags
    player_shield = False
    player_double = False
    skip_player = False

    opponent_double = False
    opponent_shield = False
    skip_opponent = False

    for round_num in range(1, rounds + 1):
        txt(f"\n--- Round {round_num} ---")

        input("Press ENTER to draw a card...")
        magic_card = random.choice(list(cards.keys()))
        txt(f"You pulled the card: {magic_card} - {cards[magic_card]}")

        # Opponent draws a card
        opponent_card = random.choice(list(cards.keys()))
        txt(f"Opponent pulled the card: {opponent_card} - {cards[opponent_card]}")

        # Player card effects
        if magic_card == "Double Points":
            player_double = True
            txt("Double Points! Your next win will give 2 points.")
        elif magic_card == "Shield":
            player_shield = True
            txt("Shield activated! You are protected this round.")
        elif magic_card == "Lose Turn":
            skip_player = True
            txt("You lost your turn this round!")
        elif magic_card == "Steal Point":
            player_points += 1
            txt("You stole 1 point from your opponent!")
        elif magic_card == "Attack Boost":
            player_points += 1
            txt("You gained 1 bonus point!")

        # Opponent card effects
        if opponent_card == "Double Points":
            opponent_double = True
            print("Opponent activated Double Points!")
        elif opponent_card == "Shield":
            opponent_shield = True
            print("Opponent activated a Shield!")
        elif opponent_card == "Lose Turn":
            skip_opponent = True
            print("Opponent lost their turn this round.")
        elif opponent_card == "Steal Point":
            if player_points > 0:
                player_points -= 1
                opponent_points += 1
                print("Opponent stole 1 point from you!")
        elif opponent_card == "Attack Boost":
            opponent_points += 1
            print("Opponent gained a bonus point!")

        # Skip turn logic
        if skip_player:
            txt("You skip this round!")
            skip_player = False
            bluedice = 0  # auto lose
        else:
            bluedice = int(input("Enter a number (1-100): "))

        if skip_opponent:
            print("Opponent skips this round!")
            skip_opponent = False
            reddice = 0  # auto lose
        else:
            reddice = random.randint(1, 100)

        txt(f"Your roll: {bluedice}")
        txt(f"Opponent's roll: {reddice}")

        # Round outcome
        if bluedice > reddice:
            if player_double:
                player_points += 2
                txt("You won with DOUBLE POINTS!")
                player_double = False
            else:
                player_points += 1
                txt("You won this round!")
        elif reddice > bluedice:
            if player_shield:
                txt("You lost, but your SHIELD protected you.")
                player_shield = False
            else:
                player_points -= 1
                txt("You lost this round.")

            # Opponent scores if not skipping
            if not skip_opponent:
                if opponent_double:
                    opponent_points += 2
                    print("Opponent won with DOUBLE POINTS!")
                    opponent_double = False
                else:
                    opponent_points += 1
                    print("Opponent won this round!")
        else:
            txt("It's a tie! No points gained.")

        # Scores
        txt(f"Score — You: {player_points} | Opponent: {opponent_points}")

        # End game condition
        if player_points <= -3:
            txt("Game Over: You lost.")
            break
        elif opponent_points >= 5:
            txt("Game Over: Opponent won.")
            break

    txt(f"Final Score — You: {player_points} | Opponent: {opponent_points}")

if __name__ == "__main__":
    main()