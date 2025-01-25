def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious forest. There are paths leading in different directions.")
    print("Your objective is to make the right choices to escape the forest.")
    print("Good luck!")

def choose_path():
    print("\nYou come to a fork in the road. Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()
    
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice! Please type 'left' or 'right'.")
        choose_path()

def left_path():
    print("\nYou decided to go left. You walk for a while and find a clearing with a peaceful pond.")
    print("Suddenly, a giant bear appears and roars at you! Do you want to fight or run?")
    
    choice = input("Type 'fight' or 'run': ").lower()
    
    if choice == 'fight':
        print("\nYou bravely fight the bear and, surprisingly, defeat it! You find a treasure chest!")
        treasure()
    elif choice == 'run':
        print("\nYou run away and find a hidden cave. Inside, you discover a way out of the forest.")
        exit_game()
    else:
        print("Invalid choice! Please type 'fight' or 'run'.")
        left_path()

def right_path():
    print("\nYou decide to go right. After walking for a while, you come across a large river.")
    print("You see a small boat tied to a post. Do you want to cross the river or turn back?")
    
    choice = input("Type 'cross' or 'turn back': ").lower()
    
    if choice == 'cross':
        print("\nYou bravely get into the boat and row across the river.")
        print("On the other side, you find an ancient temple. Do you want to enter?")
        choice = input("Type 'yes' or 'no': ").lower()
        
        if choice == 'yes':
            print("\nYou enter the temple and discover the lost artifact! You've won!")
            exit_game()
        elif choice == 'no':
            print("\nYou decide not to enter the temple. You walk around and eventually find an exit from the forest.")
            exit_game()
        else:
            print("Invalid choice! Please type 'yes' or 'no'.")
            right_path()
    elif choice == 'turn back':
        print("\nYou turn back and find a safe path leading out of the forest.")
        exit_game()
    else:
        print("Invalid choice! Please type 'cross' or 'turn back'.")
        right_path()

def treasure():
    print("\nYou open the chest and find a magical sword!")
    print("Suddenly, the forest begins to shake, and a massive tree creature appears.")
    print("Do you want to fight or try to talk to the creature?")
    
    choice = input("Type 'fight' or 'talk': ").lower()
    
    if choice == 'fight':
        print("\nYou use the magical sword and defeat the tree creature! You are victorious!")
        exit_game()
    elif choice == 'talk':
        print("\nYou calmly talk to the creature, and it leads you safely out of the forest.")
        exit_game()
    else:
        print("Invalid choice! Please type 'fight' or 'talk'.")
        treasure()

def exit_game():
    print("\nCongratulations! You've escaped the forest!")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    
    if choice == 'yes':
        intro()
        choose_path()
    elif choice == 'no':
        print("\nThanks for playing! Goodbye!")
    else:
        print("Invalid choice! Please type 'yes' or 'no'.")
        play_again()

# Start the game
intro()
choose_path()
