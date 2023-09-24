from os import system
import time

class Text:
    RESET = "\033[0m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

name = ''
weapons = []
tools = []

def title():
    global name

    system("cls")
    print(f"{Text.RED}***WELCOME TO DYSTOPIA***{Text.RESET}")
    print(f"{Text.CYAN}By: Jeff MacPherson{Text.RESET}")
    time.sleep(4)
    system("cls")
    print("Start by giving your character a name.")
    name = input("Enter your name: ")
    time.sleep(6)
    

def get_current_inventory():
    print(weapons, tools)


def input_prompt(prompt, valid_res):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_res:
            return user_input
        else:
            print("Did you make a typo? Try again.")
            time.sleep(3)


def starting_point():
    global weapons
    global tools

    system("cls")
    print("You wake up, and oddly its still dark outside. The smell of smoke is in the air... \nYou hop out of bed.")
    time.sleep(3)

    print("You see an axe laying up against the wall.")
    time.sleep(2)
    take_axe = input_prompt("Take >Axe?\nType y or n: ", ['y', 'n'])
    if take_axe == 'y':
        weapons.append("axe")
        print(f"{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
        time.sleep(2)
    else:
        print(f"You should take the axe...\n{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
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
            take_matchbox = input_prompt("You look around your kitchen and see matches laying on the kitchen table.\nType *take* to take the matchbox.\n:", ["take"])
            if take_matchbox == "take":
                tools.append("matchbox")
                print(f"{Text.MAGENTA}>Matchbox was added to your inventory.{Text.RESET}")
                time.sleep(3)
                go_outside = input("If you'd like to head outside now type *go*: ")
                if go_outside == "go":
                    time.sleep(3)
                    system("cls")
                    outside()
                else:
                    just_go_outside = input("What now?\nType *go* to go outside.")
                    if just_go_outside == "go":
                        time.sleep(3)
                        outside()
        else:
            print("You frantically run out your frontdoor")
            time.sleep(3)
            outside()


def outside():

    print("You go outside and everything is burnt black and there's no sign of anyone around...")
    time.sleep(2)
    print("You look to the left and see your neighbours door ajar.")
    print("You look to the right and see smoke burning from the town square.")
    time.sleep(2)
    direction = input_prompt("Do you\nGo >left and check on your neighbour?\n-or-\nGo >right and head straight for the city?\nType *left* or *right*: ", ["left", "right"])
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
        print(f"{Text.RED}A Zombie appeared!{Text.RESET}\nTime to fight! or you can try to run.")
    else:
        print("You turn around and head towards the town square instead.")
        time.sleep(4)
        town_square()


def town_square():
    print("You arrive in town square")


title()
starting_point()