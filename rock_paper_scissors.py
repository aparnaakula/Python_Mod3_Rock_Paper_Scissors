import random

rock = ''
paper = ''
scissors = ''

game_images = [rock, paper, scissors]

while True:
    user_choice = int(input("What do you choose? \n1.Rock \n2.Paper \n3.Scissors.\n"))

    if user_choice >= 4 or user_choice < 1:
        print("You typed an invalid number, you lose!")
    else:
        print(game_images[user_choice - 1])  # Adjust index to match user input

        computer_choice = random.randint(1, 3)
        print(f"Computer chose: {computer_choice}")
        print(game_images[computer_choice - 1])  # Adjust index to match computer choice

        if user_choice == computer_choice:
            print("It's a draw")
        elif (
            (user_choice == 1 and computer_choice == 3)
            or (user_choice == 2 and computer_choice == 1)
            or (user_choice == 3 and computer_choice == 2)
        ):
            print("You win!")
        else:
            print("You lose")

    play_again = input('Would you like to play again? (y/n) ')
    if play_again.lower() != 'y':
        print('Thank you for playing!')
        break
