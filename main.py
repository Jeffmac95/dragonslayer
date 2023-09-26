import os
import time
import random

class Text:
    RESET = "\033[0m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[34m"
    CYAN = "\033[96m"

name = ''
weapons = []
tools = []

def input_prompt(prompt, valid_res):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_res:
            return user_input
        elif user_input == "inv":
            get_current_inventory()
        else:
            print("Did you make a typo? Try again.")
            time.sleep(3)


def fight(player_hp, target_hp):
    print("********************")
    while player_hp > 0 and target_hp > 0:
        time.sleep(3)
        player_attack = random.randint(0, 1)
        target_hp -= player_attack
        print("\n")
        print(f">You hit {player_attack} damage. Target has {target_hp} health left.")
        print("\n")

        if target_hp <= 0:
            print("You won the fight.")
            print("\n")
            print("********************")
            time.sleep(2)
            return True
        
        time.sleep(3)
        target_attack = random.randint(0, 1)
        player_hp -= target_attack
        print(f">The target hits and does {target_attack} damage. You have {player_hp} health left.")
        print("\n")

        if player_hp <= 0:
            print("You lost the fight.")
            print("********************")
            time.sleep(2)
            return False
        

def get_current_inventory():
    print(f"{Text.YELLOW}Weapons: {weapons}\nItems: {tools}{Text.RESET}")
    time.sleep(3)


def title():
    global name

    terminal_width = os.get_terminal_size().columns
    game_title = "*** D R A G O N   S L A Y E R ***"
    game_author = "By: Jeff MacPherson"
    game_title_padding = int((terminal_width - len(game_title)) / 2)
    game_author_padding = int((terminal_width - len(game_author)) / 2)

    os.system("cls")
    print("\n" * 6)
    print(" " * game_title_padding + f"{Text.CYAN}{game_title}{Text.RESET}")
    print("\n")
    print(" " * game_author_padding + f"{Text.BLUE}{game_author}{Text.RESET}")
    time.sleep(5)
    os.system("cls")
    
    print("Enter your name: ")
    name = input("> ")


def starting_point():
    global weapons
    global tools

    os.system("cls")
    time.sleep(3)
    print("You wake up, and oddly its still dark outside. The smell of smoke is in the air... \nYou hop out of bed.")
    time.sleep(3)

    print("You see an axe laying up against the wall.")
    time.sleep(2)
    take_axe = input_prompt("Take >Axe?\nType y or n: ", ['y', 'n'])
    if take_axe == 'y':
        weapons.append("axe")
        print(f"{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
        time.sleep(2)
        print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
        time.sleep(2)
    else:
        print(f"You should take the axe...\n{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
        time.sleep(2)
        print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
        time.sleep(2)
    
    go_downstairs = input_prompt("You should head downstairs now.\nType *go*: ", ["go"])
    if go_downstairs == "go":
        time.sleep(2)
        downstairs()


def downstairs():
        print("You're downstairs and its deadly quiet... You see your frontdoor ajar.\nDo you:")
        time.sleep(2)
        direction = input_prompt("Go >left to search the kitchen first for possible supplies?\n-or-\nGo >right in a panic and head straight outside to assess the situation?\nType *left* or *right*: ", ["left", "right"])
        if direction == "left":
            time.sleep(2)
            take_matchbox = input_prompt("You look around your kitchen and see a matchbox laying on the kitchen table.\nTo take the matchbox\nType *take*: ", ["take"])
            if take_matchbox == "take":
                tools.append("matchbox")
                print(f"{Text.MAGENTA}>Matchbox was added to your inventory.{Text.RESET}")
                time.sleep(2)
                print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
                time.sleep(3)
                go_outside = input_prompt("If you'd like to head outside now type *go*: ", ["go"])
                if go_outside == "go":
                    time.sleep(3)
                    os.system("cls")
                    outside()
                else:
                    just_go_outside = input_prompt("What now?\nType *go* to go outside.", ["go"])
                    if just_go_outside == "go":
                        time.sleep(3)
                        outside()
        else:
            print("You frantically run out your frontdoor")
            time.sleep(3)
            os.system("cls")
            outside()


def outside():
    print("You go outside. The sky is filled with smoke, with no sign of the sun.. or people. The air smells of burning wood and everything is scortched and black.")
    time.sleep(2)
    print("You look to the left and see your neighbours door wide-open.")
    time.sleep(2)
    print("You look to the right and see smoke burning from the town square.")
    time.sleep(2)
    direction = input_prompt("Do you:\nGo >left and check on your neighbour?\n-or-\nGo >right and head straight for the city?\nType *left* or *right*: ", ["left", "right"])
    if direction == "left":
        time.sleep(2)
        neighbours_house()
    else:
        time.sleep(2)
        town_square()


def neighbours_house():
    print("You open the door to your neighbours house, it smells horrible in here!")
    time.sleep(2)
    print("You hear a ruffling noise coming from upstairs...")
    time.sleep(1)
    check_noise = input_prompt("Do you go check out the noise?\nType y or n: ", ['y', 'n'])
    if check_noise == 'y':
        print("You head up the creaky stairs...")
        time.sleep(4)
        print(f"{Text.RED}A Zombie appeared!{Text.RESET}\nTime to fight!")
        if fight(player_hp = 5, target_hp = 3):
            print("You run out of the house and head for the town-square.")
            time.sleep(3)
            town_square()
        else:
            print("Run!")
    else:
        print("You turn around and head towards the town square instead.")
        time.sleep(4)
        town_square()


def town_square():
    global tools

    print("You arrive in town square.")
    time.sleep(2)
    print("Everything's charred, with some buildings still slightly burning. And no sign of any people around.")
    time.sleep(5)
    print("You suddenly realize the castle lights are on straight ahead.")
    time.sleep(2)
    print("But before heading to the castle, you might want to look around first for a lightsource to get across the bridge safely.")
    time.sleep(5)
    direction = input_prompt("You look to the >left and see a path with a Lumber Shop.\nYou look to the >right and see a path with an abandoned General Store.\nType *left* or *right*: ", ['left', 'right'])
    if direction == "left":
        if tools[-1] != "key":
            print("The door is locked. Maybe I should look for a key.")
            time.sleep(2)
            print("You walk over to the right to check out the General Store.")
            time.sleep(4)
            general_store()
        else:
            lumber_shop()
    else:
        general_store()


def general_store():
    global tools

    print("You arrive at the General Store and immediately notice a vial containing red liquid on the shelf behind the front-counter.")
    take_potion = input_prompt("Take the >Health Potion?\nType y or n: ", ['y', 'n'])
    if take_potion == 'y':
        tools.append("health potion")
        print(f"{Text.MAGENTA}>Health Potion was added to your inventory.{Text.RESET}")
        time.sleep(3)
    else:
        print("Ok. If you dont think you'll need it.")
        time.sleep(2)
    print("You look around and notice a trap-door that leads to the basement.")
    general_store_basement = input_prompt("To go to the basement type *go*: ", ["go"])
    if general_store_basement == "go":
        print("You head down to the basement and look around for anything useful...")
        time.sleep(6)
        print("You find a key!")
        time.sleep(2)
        tools.append("key")
        print(f"{Text.MAGENTA}>Key was added to your inventory.{Text.RESET}")
        time.sleep(2)
    print("You head back upstairs and out of the General Store to try the key at the lumber shop.")
    time.sleep(4)
    lumber_shop()


def lumber_shop():
    global tools

    print("You arrive at the Lumber Shop. If you have a key the door should open.")
    print(f"Remeber, you can type {Text.YELLOW}inv{Text.RESET} at any time to see your current inventory.")
    shall_you_pass = input_prompt("Type *unlock*: ", ["unlock"])
    print("You turn the key.")
    time.sleep(3)
    if shall_you_pass == "unlock":
        if tools[-1] == "key":
            print("You enter the Lumber Shop.")
        else:
            print("It doesnt work, back to the General Store you go.")
            time.sleep(4)
            general_store()

title()
starting_point()