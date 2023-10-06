import os
from time import sleep
from random import randint

class Text:
    RESET = "\033[0m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    BLUE = "\033[34m"
    CYAN = "\033[96m"

name = ''
weapons = []
tools = []
target = []
team = []


def input_prompt(prompt, valid_res):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_res:
            return user_input
        elif user_input == "inv":
            get_current_inventory()
        else:
            print("Did you make a typo? Try again.")
            sleep(3)


def fight(player_hp, target_hp):
    global weapons
    global team

    print("********************")
    while player_hp > 0 and target_hp > 0:
        sleep(3)
        if "axe" in weapons:
            player_attack = randint(0, 2)
        elif "sword" in weapons:
            player_attack = randint(0, 5)
        else:
            player_attack = randint(0, 1)

        player_attack = min(player_attack, target_hp)
        
        target_hp -= player_attack

        print("\n")
        print(f">You hit {player_attack} damage. Target has {target_hp} health left.")


        if target_hp <= 0:
            print("\n")
            print(f"{Text.GREEN}You won the fight.{Text.RESET}")
            print("\n")
            print("********************")
            sleep(2)
            return True
        
        if "prisoner" in team:
            prisoner_attack = randint(0, 2)
            prisoner_attack = min(prisoner_attack, target_hp)
            target_hp -= prisoner_attack
            print(f">Prisoner hit {prisoner_attack} damage. Target has {target_hp} health left.")
        
        sleep(3)
        if "dragon" in target:
            target_attack = randint(0, 5)
        else:
            target_attack = randint(0, 1)

        target_attack = min(target_attack, player_hp)

        player_hp -= target_attack

        print(f">The target hits you and does {target_attack} damage. You have {player_hp} health left.")
        print("\n")

        if player_hp <= 0:
            print(f"{Text.RED}You lost the fight.{Text.RESET}")
            print("********************")
            sleep(2)
            return False

        #if "health potion" in tools and player_hp <= 5:
            #print(">You drink the health potion")
            #player_hp += n
        

def get_current_inventory():
    print(f"{Text.YELLOW}Weapons: {weapons}\nItems: {tools}{Text.RESET}")
    sleep(1)


def display_title():
    terminal_width = os.get_terminal_size().columns
    game_title = "*** D R A G O N   S L A Y E R ***"
    game_author = "By: Jeff MacPherson"
    game_title_padding = int((terminal_width - len(game_title)) / 2)
    game_author_padding = int((terminal_width - len(game_author)) / 2)

    os.system("cls")
    print("\n" * 6)
    print(" " * game_title_padding + f"{Text.RED}{game_title}{Text.RESET}")
    print("\n")
    print(" " * game_author_padding + f"{Text.BLUE}{game_author}{Text.RESET}")
    sleep(5)
    os.system("cls")


def starting_point():
    global name

    display_title()

    name = input("Enter your characters name: ")
    sleep(1)
    os.system("cls")
    sleep(3)

    bedroom()


def bedroom():
    global weapons

    print("You wake up, and oddly its still dark outside. The smell of smoke is in the air... \nYou hop out of bed.")
    sleep(3)

    print("You see an axe laying up against the wall.")
    sleep(2)
    take_axe = input_prompt(f">Take Axe?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if take_axe == 'y':
        weapons.append("axe")
        print(f"{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
        sleep(1)
        print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
        sleep(2)
        go_downstairs = input_prompt(f"You should head downstairs now.\nType {Text.GREEN}go{Text.RESET}: ", ["go"])
        if go_downstairs == "go":
            sleep(2)
            downstairs()
    else:
        print("Ok. If you dont think you'll need it.")
        print("You head downstairs.")
        sleep(2)
        downstairs()


def downstairs():
        print("You're downstairs and its deadly quiet... You see your frontdoor ajar.\nDo you:")
        sleep(2)
        print(f">Go {Text.GREEN}left{Text.RESET} to search the kitchen first for possible supplies?\n-or-\n>Go {Text.GREEN}right{Text.RESET} in a panic and head straight outside to assess the situation?")
        direction = input_prompt(f"Type {Text.GREEN}left {Text.RESET}or {Text.GREEN}right{Text.RESET}: ", ["left", "right"])
        if direction == "left":
            print("You head into the kitchen.")
            sleep(2)
            kitchen()
        else:
            print("You frantically run out your frontdoor")
            sleep(3)
            outside()


def kitchen():
        global tools

        print("You look around your kitchen and see a matchbox laying on the kitchen table.")
        sleep(2)
        take_matchbox = input_prompt(f">Do you take the matchbox?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
        if take_matchbox == 'y':
            tools.append("matchbox")
            print(f"{Text.MAGENTA}>Matchbox was added to your inventory.{Text.RESET}")
            sleep(2)
            print(f"Type {Text.YELLOW}inv{Text.RESET} at anytime to see your current inventory.")
            sleep(3)
            print("You should head outside now.")
            go_outside = input_prompt(f"Type {Text.GREEN}go{Text.RESET}: ", ["go"])
            if go_outside == "go":
                sleep(3)
                outside()
        else:
            print("Ok. If you dont think you'll need it.")
            print("You head for your front-door to go check outside.")
            sleep(2)
            outside()
            sleep(4)


def outside():
    print("You step outside. The sky is filled with smoke, with no sign of the sun.. or people. The air smells of burning wood and everything is scortched and black.")
    sleep(2)
    print("You look to the left and see your neighbours door wide-open.")
    sleep(2)
    print("You look to the right and see smoke burning from the town square.")
    sleep(2)
    print(f"Do you:\n>Go {Text.GREEN}left{Text.RESET} and check on your neighbour?\n-or-\n>Go {Text.GREEN}right{Text.RESET} and head straight for the city?")
    sleep(2)
    direction = input_prompt(f"Type {Text.GREEN}left{Text.RESET} or {Text.GREEN}right{Text.RESET}: ", ["left", "right"])
    if direction == "left":
        sleep(2)
        neighbours_house()
    else:
        sleep(2)
        print("You head for the town square.")
        sleep(5)
        town_square()


def neighbours_house():
    global target

    print("You open the door to your neighbours house, it smells horrible in here!")
    sleep(2)
    print("You hear a ruffling noise coming from upstairs...")
    sleep(1)
    check_noise = input_prompt(f">Do you go check out the noise?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if check_noise == 'y':
        print("You head up the creaky stairs...")
        sleep(4)
        target.append("zombie")
        print(f"{Text.RED}A Zombie appeared!{Text.RESET}\nTime to fight!")
        if fight(player_hp = 5, target_hp = 4):
            target.remove("zombie")
            print("You run out of the house and head for the town-square.")
            sleep(5)
            town_square()
        else:
            target.remove("zombie")
            print("Run!")
            town_square()
    else:
        print("You turn around and head towards the town square instead.")
        sleep(4)
        town_square()


def town_square():
    global tools

    if "matchbox" and "torch" in tools:
        sleep(4)
        print("You arrive back in the town square with the proper stuff this time.")
        print(">You light the torch and make your way across the bridge")
        sleep(2)
        the_bridge()
    else:
        print("You arrive in town square.")
        sleep(2)
        print("Everything's charred, with some buildings still slightly burning. And no sign of any people around.")
        sleep(5)
        print("You suddenly realize the castle lights are on straight ahead.")
        sleep(2)
        print("But before heading to the castle, you might want to look around first for a lightsource to get across the bridge safely.")
        sleep(5)
        print(f">You look {Text.GREEN}left{Text.RESET} and see a path with a Lumber Shop.\n>You look to the {Text.GREEN}right{Text.RESET} and see a path with an abandoned General Store.")
        direction = input_prompt(f"Type {Text.GREEN}left{Text.RESET} or {Text.GREEN}right{Text.RESET}: ", ['left', 'right'])
        if direction == "left":
            if "key" not in tools:
                sleep(1)
                print("The door is locked. Maybe I should look for a key.")
                sleep(2)
                print("You walk over to the right to check out the General Store.")
                sleep(5)
                general_store()
            else:
                lumber_shop()
        else:
            print("You make your way to the General Store.")
            sleep(4)
            general_store()


def general_store():
    global tools

    print("You arrive at the General Store and immediately notice a vial containing red liquid on the shelf behind the front-counter.")
    take_potion = input_prompt(f">Take the Health Potion?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if take_potion == 'y':
        tools.append("health potion")
        print(f"{Text.MAGENTA}>Health Potion was added to your inventory.{Text.RESET}")
        sleep(3)
    else:
        print("Ok. If you dont think you'll need it.")
        sleep(2)
    print("You look around and notice a trap-door that leads to the basement.")
    general_store_basement = input_prompt(f">To go to the basement\nType {Text.GREEN}go{Text.RESET}: ", ["go"])
    if general_store_basement == "go":
        print("You head down to the basement and look around for anything useful...")
        sleep(6)
        print("You find a key!")
        sleep(2)
        tools.append("key")
        print(f"{Text.MAGENTA}>Key was added to your inventory.{Text.RESET}")
        sleep(2)
    print("You head back upstairs and out of the General Store to try the key at the lumber shop.")
    sleep(4)
    lumber_shop()


def lumber_shop():
    global tools

    print("You arrive at the Lumber Shop.")
    sleep(2)
    print("If you have a key the door should open.")
    sleep(2)
    print(f"Remeber, you can type {Text.YELLOW}inv{Text.RESET} at any time to see your current inventory.")
    shall_you_pass = input_prompt(f"Type {Text.GREEN}unlock{Text.RESET}: ", ["unlock"])
    print("You turn the key...")
    sleep(2)
    if shall_you_pass == "unlock":
        if "key" in tools:
            print(f"{Text.CYAN}*click*{Text.RESET}")
            sleep(2)
            print("You enter the Lumber Shop.")
            sleep(3)
            print("You look around for a stick to act as a torch.")
            sleep(4)
            print("You find a decent looking stick.")
            sleep(1)
            tools.append("torch")
            print(f"{Text.MAGENTA}>Torch was added to your inventory.{Text.RESET}")
            sleep(2)
            print("You head back to the town sqaure to make your way across the bridge.")
            sleep(4)
            town_fountain()
        else:
            print("It doesnt work. Back to the General Store you go.")
            sleep(4)
            general_store()

def town_fountain():
    global weapons
    global tools

    print("You arrive back in the town square and make your way to the bridge that leads to the castle.")
    sleep(2)
    print("But something catches your eye in the fountain, in the middle of the square.")
    sleep(2)
    print("Its a sword!")
    sleep(1)
    weapons.append("sword")
    print(f"{Text.MAGENTA}>Sword was added to your inventory.{Text.RESET}")
    sleep(2)
    print("You notice strange writing on the side of the blade but cant understand the language. And on the other side, a picture of a dragon?")
    sleep(1)
    print("You feel a lot stronger with this.")
    sleep(2)
    if "matchbox" in tools:
        print("You make your way towards the bridge")
        sleep(5)
        the_bridge()
    else:
        print("You have nothing to light your stick with.\nBack to your house to check the kitchen!")
        sleep(5)
        kitchen()



def the_bridge():
    global target

    print("You start making your way across the bridge.")
    sleep(2)
    print("Its quiet and still pretty dark even with your torch lit.")
    sleep(3)
    target.append("zombie")
    print(f"{Text.RED}A Zombie appears!{Text.RESET}\nTime to fight!")
    sleep(2)
    if fight(player_hp=5, target_hp=4):
        target.remove("zombie")
        print("You continue your way across the bridge.")
        sleep(4)
        print("Finally you arrive at the castle and it smells horrible.\nYou make your way inside.")
        the_castle()
    else:
        target.remove("zombie")
        print("You run back to recooperate in the town sqaure.")
        sleep(3)
        town_square()


def the_castle():
    global weapons
    global team

    print("You walk inside the castle and notice a skeleton of what use to be a king, sitting on a charred throne.")
    sleep(2)
    print("You hear a loud thumping noise coming from the dungeon below your feet.")
    sleep(2)
    print("You make your way down the spiral staircase towards the dungeons...")
    sleep(5)
    print(f"You arrive in the middle floor. Appears to be the prison of the castle.\nDo you: walk down the corridor to {Text.GREEN}explore{Text.RESET} the cells or {Text.GREEN}go{Text.RESET} to the bottom floor.")
    direction = input_prompt(f"Type {Text.GREEN}explore{Text.RESET} or {Text.GREEN}go{Text.RESET}: ", ["explore", "go"])
    if direction == "explore":
        print("You make your way down the hallway looking in the cells...")
        sleep(4)
        print("For the first time you notice a person!")
        sleep(1)
        print("You attempt to talk to the person whos sleeping in one of the cells.")
        sleep(2)
        print("He wakes up and turns to you and you tell him your name.")
        sleep(3)
        print("The stranger tells you hes been a prisoner for over 5 years now. And several weeks ago a dragon came to the town and burned everything and almost everyone...\nand that any survivers made underground bunkers 10 feet under the dirt.")
        sleep(3)
        print("He also mentions the dragon was captured by some of the kings men and is locked in the basement of the castle but may be hard to beat by yourself.")
        sleep(6)
        if "axe" in weapons:
            print("Maybe you can free the prisoner with a swing of your axe?")
            free_prisoner = input_prompt(f"Type {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
            if free_prisoner == 'y':
                print(f"{Text.CYAN}>You swing your axe and free the prisoner!{Text.RESET}")
                print("The prisoner thanks you for freeing him.\nHe's willing to help you fight the dragon if you would give him your axe...")
                sleep(1)
                print("Do you give your >Axe to the stranger?")
                give_axe = input_prompt(f"Type {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", {'y', 'n'})
                if give_axe == 'y':
                    weapons.remove("axe")
                    print(f"{Text.RED}>You give the stranger your axe.{Text.RESET}")
                    team.append("prisoner")
                    print(f"{Text.YELLOW}>The prisoner joins your team.{Text.RESET}")
                    sleep(2)
                    print("You say to the prisoner; Lets head downstairs friend.")
                    sleep(4)
                    battle_room()
                else:
                    print("You dont trust a prisoner enough to give him an axe.")
                    sleep(2)
                    print("You head towards the stairvcase to go downstairs.")
                    sleep(4)
                    battle_room()
            else:
                print("You dont trust the prisoner.")
                sleep(2)
                print("You head towards the staircase to go downstairs.")
                sleep(4)
                battle_room()
        else:
            print("With no way to free the prisoner, you turn and head towards the staircase leading to the basement...")
            sleep(4)
            battle_room()
    else:
        print("You head straight to the sprial staircase to make your to the dungeons in the basemnet.")
        sleep(4)
        battle_room()


def battle_room():
    global weapons
    global team
    global target

    print("You arrive in the basement and prepare to fight the dragon.\nHope your ready.")
    sleep(3)
    target.append("dragon")
    print(f"{Text.RED}A Dragon appeared!{Text.RESET}")
    sleep(3)
    if fight(player_hp=10, target_hp=15):
        target.remove("dragon")
        print("You beat the dragon!")
        sleep(2)
        print("You and your new friend make your way out of the castle to let the people underground know the dragon has been defeated and they can live the rest of their lives on the surface of Earth again!")
        sleep(6)
        end_game()
    else:
        target.remove("dragon")
        print(f"{Text.RED}Game over.{Text.RESET}")
        sleep(2)
        end_game()

def end_game():
    display_title()
    quit()

starting_point()