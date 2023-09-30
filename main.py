import os
import time
import random

class Text:
    RESET = "\033[0m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    BLUE = "\033[34m"
    CYAN = "\033[96m"

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
    global weapons

    print("********************")
    while player_hp > 0 and target_hp > 0:
        time.sleep(3)
        if "axe" in weapons:
            player_attack = random.randint(0, 2)
        elif "sword" in weapons:
            player_attack = random.randint(0, 5)
        else:
            player_attack = random.randint(0, 1)
        player_attack = min(player_attack, target_hp)
        target_hp -= player_attack
        print("\n")
        print(f">You hit {player_attack} damage. Target has {target_hp} health left.")

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
    time.sleep(1)


def starting_point():
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

    bedroom()


def bedroom():
    global weapons
    global tools

    time.sleep(3)
    print("You wake up, and oddly its still dark outside. The smell of smoke is in the air... \nYou hop out of bed.")
    time.sleep(3)

    print("You see an axe laying up against the wall.")
    time.sleep(2)
    take_axe = input_prompt(f">Take Axe?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if take_axe == 'y':
        weapons.append("axe")
        print(f"{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
        time.sleep(1)
        print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
        time.sleep(2)
        go_downstairs = input_prompt(f"You should head downstairs now.\nType {Text.GREEN}go{Text.RESET}: ", ["go"])
        if go_downstairs == "go":
            time.sleep(2)
            downstairs()
    else:
        print("Ok. If you dont think you'll need it.")
        print("You head downstairs.")
        time.sleep(2)
        downstairs()


def downstairs():
        print("You're downstairs and its deadly quiet... You see your frontdoor ajar.\nDo you:")
        time.sleep(2)
        print(f">Go {Text.GREEN}left{Text.RESET} to search the kitchen first for possible supplies?\n-or-\n>Go {Text.GREEN}right{Text.RESET} in a panic and head straight outside to assess the situation?")
        direction = input_prompt(f"Type {Text.GREEN}left {Text.RESET}or {Text.GREEN}right{Text.RESET}: ", ["left", "right"])
        if direction == "left":
            print("You head into the kitchen.")
            time.sleep(2)
            kitchen()
        else:
            print("You frantically run out your frontdoor")
            time.sleep(3)
            outside()


def kitchen():
        print("You look around your kitchen and see a matchbox laying on the kitchen table.")
        time.sleep(2)
        take_matchbox = input_prompt(f">Do you take the matchbox?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
        if take_matchbox == 'y':
            tools.append("matchbox")
            print(f"{Text.MAGENTA}>Matchbox was added to your inventory.{Text.RESET}")
            time.sleep(2)
            print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
            time.sleep(3)
            print("You should head outside now.")
            go_outside = input_prompt(f"Type {Text.GREEN}go{Text.RESET}: ", ["go"])
            if go_outside == "go":
                time.sleep(3)
                outside()
        else:
            print("Ok. If you dont think you'll need it.")
            print("You head for your front-door to go check outside.")
            time.sleep(2)
            outside()
            time.sleep(4)


def outside():
    print("You step outside. The sky is filled with smoke, with no sign of the sun.. or people. The air smells of burning wood and everything is scortched and black.")
    time.sleep(2)
    print("You look to the left and see your neighbours door wide-open.")
    time.sleep(2)
    print("You look to the right and see smoke burning from the town square.")
    time.sleep(2)
    print(f"Do you:\n>Go {Text.GREEN}left{Text.RESET} and check on your neighbour?\n-or-\n>Go {Text.GREEN}right{Text.RESET} and head straight for the city?")
    time.sleep(2)
    direction = input_prompt(f"Type {Text.GREEN}left{Text.RESET} or {Text.GREEN}right{Text.RESET}: ", ["left", "right"])
    if direction == "left":
        time.sleep(2)
        neighbours_house()
    else:
        time.sleep(2)
        print("You head for the town square.")
        time.sleep(5)
        town_square()


def neighbours_house():
    print("You open the door to your neighbours house, it smells horrible in here!")
    time.sleep(2)
    print("You hear a ruffling noise coming from upstairs...")
    time.sleep(1)
    check_noise = input_prompt(f">Do you go check out the noise?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if check_noise == 'y':
        print("You head up the creaky stairs...")
        time.sleep(4)
        print(f"{Text.RED}A Zombie appeared!{Text.RESET}\nTime to fight!")
        if fight(player_hp = 5, target_hp = 4):
            print("You run out of the house and head for the town-square.")
            time.sleep(5)
            town_square()
        else:
            print("Run!")
            town_square()
    else:
        print("You turn around and head towards the town square instead.")
        time.sleep(4)
        town_square()


def town_square():
    global tools

    if "matchbox" and "torch" in tools:
        time.sleep(4)
        print("You arrive back in the town square with the proper stuff this time.")
        print(">You light the torch and make your way across the bridge")
        time.sleep(2)
        the_bridge()
    else:
        print("You arrive in town square.")
        time.sleep(2)
        print("Everything's charred, with some buildings still slightly burning. And no sign of any people around.")
        time.sleep(5)
        print("You suddenly realize the castle lights are on straight ahead.")
        time.sleep(2)
        print("But before heading to the castle, you might want to look around first for a lightsource to get across the bridge safely.")
        time.sleep(5)
        print(f">You look {Text.GREEN}left{Text.RESET} and see a path with a Lumber Shop.\n>You look to the {Text.GREEN}right{Text.RESET} and see a path with an abandoned General Store.")
        direction = input_prompt(f"Type {Text.GREEN}left{Text.RESET} or {Text.GREEN}right{Text.RESET}: ", ['left', 'right'])
        if direction == "left":
            if "key" not in tools:
                time.sleep(1)
                print("The door is locked. Maybe I should look for a key.")
                time.sleep(2)
                print("You walk over to the right to check out the General Store.")
                time.sleep(5)
                general_store()
            else:
                lumber_shop()
        else:
            print("You make your way to the General Store.")
            time.sleep(4)
            general_store()


def general_store():
    global tools

    print("You arrive at the General Store and immediately notice a vial containing red liquid on the shelf behind the front-counter.")
    take_potion = input_prompt(f">Take the Health Potion?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if take_potion == 'y':
        tools.append("health potion")
        print(f"{Text.MAGENTA}>Health Potion was added to your inventory.{Text.RESET}")
        time.sleep(3)
    else:
        print("Ok. If you dont think you'll need it.")
        time.sleep(2)
    print("You look around and notice a trap-door that leads to the basement.")
    general_store_basement = input_prompt(f">To go to the basement\nType {Text.GREEN}go{Text.RESET}: ", ["go"])
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
    global weapons

    print("You arrive at the Lumber Shop.")
    time.sleep(2)
    print("If you have a key the door should open.")
    time.sleep(2)
    print(f"Remeber, you can type {Text.YELLOW}inv{Text.RESET} at any time to see your current inventory.")
    shall_you_pass = input_prompt(f"Type {Text.GREEN}unlock{Text.RESET}: ", ["unlock"])
    print("You turn the key...")
    time.sleep(2)
    if shall_you_pass == "unlock":
        if "key" in tools:
            print(f"{Text.CYAN}*click*{Text.RESET}")
            time.sleep(2)
            print("You enter the Lumber Shop.")
            time.sleep(3)
            print("You look around for a stick to act as a torch.")
            time.sleep(4)
            print("You find a decent looking stick.")
            time.sleep(1)
            tools.append("torch")
            print(f"{Text.MAGENTA}>Torch was added to your inventory.{Text.RESET}")
            time.sleep(2)
            print("You head back to the town sqaure to make your way across the bridge.")
            time.sleep(4)
            town_fountain()
        else:
            print("It doesnt work. Back to the General Store you go.")
            time.sleep(4)
            general_store()

def town_fountain():
    global weapons
    global tools

    print("You arrive back in the town square and make your way to the bridge that leads to the castle.")
    time.sleep(2)
    print("But something catches your eye in the fountain, in the middle of the square.")
    time.sleep(2)
    print("Its a sword!")
    time.sleep(1)
    weapons.append("sword")
    print(f"{Text.MAGENTA}>Sword was added to your inventory.{Text.RESET}")
    time.sleep(2)
    print("You notice strange writing on the side of the blade but cant understand the language. And on the other side, a picture of a dragon?")
    time.sleep(1)
    print("You feel a lot stronger with this.")
    time.sleep(2)
    if "matchbox" in tools:
        print("You make your way towards the bridge")
        time.sleep(5)
        the_bridge()
    else:
        print("You have nothing to light your stick with.\nBack to your house to check the kitchen!")
        time.sleep(5)
        kitchen()



def the_bridge():
    global weapons
    global tools
    tools.append("matchbox")
    tools.append("torch")
    weapons.append("sword")

    print("You start making your way across the bridge.")
    time.sleep(2)
    print("Its quiet and still pretty dark even with your torch lit.")
    time.sleep(3)
    print(f"{Text.RED}A Zombie appears!{Text.RESET}\nTime to fight!")
    time.sleep(2)
    if fight(player_hp=5, target_hp=4):
        print("You continue your way across the bridge.")
        time.sleep(4)
        print("Finally you arrive at the castle and it smells horrible.\nYou make your way inside.")
        the_castle()
    else:
        print("You run back to recooperate in the town sqaure.")
        time.sleep(3)
        town_square()

def the_castle():
    print("You walk inside the castle and notice a skeleton of what use to be a king, sitting on a charred throne.")


starting_point()