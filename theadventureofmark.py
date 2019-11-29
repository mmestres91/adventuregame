import time
import random



monsters = ["The Moblin General", "Commander Lynel",
            "Ganondorf", "Skulluta Soldier", "Deku Captain"]
monster = random.choice(monsters)

def print_pause(str):
    print(str)
    time.sleep(2)

def print_pause_2(str1, str2, str3):
    print(str1, str2, str3)
    time.sleep(2)

def start_game():
    print_pause("You find yourself in a desolate Kokiri Forest...")
    print_pause_2("Rumor has it that", monster, "is roaming the area.")
    print_pause("In front of you are two areas to explore.")
    game_intro()

def game_intro():
    print_pause("To your left are The Lost Woods.")
    print_pause("To your right is a small grotto.")
    print_pause("Which way do you want to go?")
    start_gamechoice()

def grotto():
    if grotto.has_been_Called is False:
        print_pause("You find yourself in an underground grotto.")
        print_pause("In front of you is a pedestal with"
                    " a shining object stuck within it...")
        print_pause("You have found The Master Sword,"
                    " the Great Blade of Evil's Bane!!!")
        print_pause("You discard your Kokiri Sowrd and hold your"
                    " new legendary weapon proudly.")
        print_pause("You head back outside...")
        grotto.has_been_Called = True
    else:
        print_pause("You find yourself in an underground grotto.")
        print_pause("You have already pulled The"
                    " Master Sword out of it's pedestal...")
        print_pause("You head back to find and prevail against evil!")
    game_intro()

def lostwoods():
    print_pause("You cautiously enter into The Lost Woods...")
    print_pause("You hear a noise creak steadily behind you.")
    print_pause("Turning around slowly, you unsheath your sword!")
    print_pause_2("You are not alone as", monster, "has appeared!")
    fight_choice()

def start_gamechoice():
    choice = input("(Please enter 1 to head into"
                    " The Lost Woods or 2 to enter the grotto.)")
    if choice == "1":
        lostwoods()
    elif choice == "2":
        grotto()
    else:
        start_gamechoice()

def fight_choice():
    choice = input("Will you fight(y) or run away(n)?")
    if choice == "y":
        print_pause("You decide to fight!")
        game_ending()
    elif choice == "n":
        print_pause("You safely head out of the woods!")
        game_intro()
    else:
        fight_choice()

def game_ending():
    if grotto.has_been_Called is True:
        print_pause_2("With the power of The Master Sword in"
                        " your left hand, you vanquish", monster, "!")
        print_pause("You have saved Kokiri Forest and are victorious!")
    else:
        print_pause_2("With only a Kokiri Sword in hand, you attempt"
                        " to fight", monster, "but are struck down!")
        print_pause("You have died! GAME OVER")
    play_again()

def play_again():
    choice = input("Would you like to play again? (y/n)")
    if choice == "y":
        print_pause("Excellent! Starting the game over again...")
        game_start()
    elif choice == "n":
        print("Thanks for playing! See you again.")
    else:
        play_again()

def game_start():
    grotto.has_been_Called = False
    start_game()
    
game_start()
