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
        if "axe" in weapons:
            player_attack = randint(0, 2)
        elif "sword" in weapons:
            player_attack = randint(0, 5)
        else:
            player_attack = randint(0, 1)

        player_attack = min(player_attack, target_hp)
        sleep(3)
        target_hp -= player_attack
        print("\n")
        print(f">You hit {player_attack} damage. Target has {target_hp} health left.")

        if target_hp <= 0:
            print("\n")
            sleep(2)
            print(f"{Text.GREEN}You won the fight.{Text.RESET}")
            print("\n")
            print("********************")
            sleep(2)
            return True
        
        if "red" in team:
            reds_attack = randint(0, 2)
            reds_attack = min(reds_attack, target_hp)
            target_hp -= reds_attack
            print(f">Prisoner hit {reds_attack} damage. Target has {target_hp} health left.")

        if player_hp <= 5 and "health potion" in tools:
            sleep(2)
            player_hp += 6
            tools.remove("health potion")
            print(f">{Text.GREEN}You drink your health potion for +6 hitpoints.{Text.RESET}\nYour hitpoints is now: {Text.GREEN}{player_hp}{Text.RESET}.")
            sleep(2)
        
        sleep(3)

        if "dragon" in target:
            target_attack = randint(0, 5)
        else:
            target_attack = randint(0, 1)

        target_attack = min(target_attack, player_hp)
        player_hp -= target_attack
        print("\n")
        print(f">The target hits you and does {target_attack} damage. You have {player_hp} health left.")
        print("\n")
            
        if player_hp <= 0:
            print(f"{Text.RED}You lost the fight.{Text.RESET}")
            print("********************")
            sleep(3)
            return False
        

def get_current_inventory():
    print(f"{Text.YELLOW}Team: {team}\nWeapons: {weapons}\nItems: {tools}{Text.RESET}")
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
    sleep(4)
    os.system("cls")


def starting_point():
    global name


    display_title()

    name = input("Enter your characters name: ")
    sleep(1)
    os.system("cls")
    print(f"Name: {Text.CYAN}{name}{Text.RESET}")
    print(f"Type {Text.YELLOW}inv{Text.RESET} at any prompt throughout the game to see your current inventory.")
    terminal_width = os.get_terminal_size().columns
    print("*" * terminal_width)
    print("\n" * 2)
    sleep(4)

    bedroom()


def bedroom():
    global weapons


    print("You wake up, and oddly its still dark outside. The smell of smoke is in the air... \nYou hop out of bed.")
    sleep(3)

    print("You see an axe laying up against the wall.")
    sleep(1)
    take_axe = input_prompt(f">Take Axe?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if take_axe == 'y':
        weapons.append("axe")
        print(f"{Text.MAGENTA}>Axe was added to your inventory.{Text.RESET}")
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
        print(f">Go {Text.GREEN}left{Text.RESET} to search the kitchen first for possible supplies? or,\n>Go {Text.GREEN}right{Text.RESET} in a panic and head straight outside to assess the situation?")
        direction = input_prompt(f"Type {Text.GREEN}left {Text.RESET}or {Text.GREEN}right{Text.RESET}: ", ["left", "right"])
        if direction == "left":
            print("You head into the kitchen.")
            sleep(3)
            kitchen()
        else:
            print("You frantically run out your frontdoor")
            sleep(3)
            outside()


def kitchen():
        global tools


        print("You look around your kitchen and see a matchbox laying on the kitchen table.")
        sleep(1)
        take_matchbox = input_prompt(f">Take the matchbox?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
        if take_matchbox == 'y':
            tools.append("matchbox")
            print(f"{Text.MAGENTA}>Matchbox was added to your inventory.{Text.RESET}")
            sleep(3)
            print("You should head outside now.")
            sleep(1)
            go_outside = input_prompt(f"Type {Text.GREEN}go{Text.RESET}: ", ["go"])
            if go_outside == "go":
                sleep(3)
                outside()
        else:
            print("Ok. If you dont think you'll need it.")
            sleep(1)
            print("You head for your front-door to go check outside.")
            sleep(5)
            outside()


def outside():
    print("You step outside. The sky is filled with smoke, with no sign of the sun.. or people. The air smells of burning wood and everything is scortched and black.")
    sleep(3)
    print("You look to the left and see your neighbours door wide-open.")
    sleep(2)
    print("You look to the right and see smoke burning from the town square.")
    sleep(2)
    print(f"Do you:\n>Go {Text.GREEN}left{Text.RESET} and check on your neighbour?\n-or-\n>Go {Text.GREEN}right{Text.RESET} and head straight for the city?")
    sleep(2)
    direction = input_prompt(f"Type {Text.GREEN}left{Text.RESET} or {Text.GREEN}right{Text.RESET}: ", ["left", "right"])
    if direction == "left":
        print("You make your way across your lawn towards the neighbours frontdoor.")
        sleep(2)
        neighbours_house()
    else:
        sleep(2)
        print("You head for the town square.")
        sleep(5)
        town_square()


def neighbours_house():
    global target
    global tools


    print("You arrive at your neighbours.")
    sleep(1)
    print("You slowly push the frontdoor and stick your head inside.")
    sleep(2)
    print("You hear a ruffling noise coming from upstairs...")
    sleep(1)
    check_noise = input_prompt(f">Do you go check out the noise?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if check_noise == 'y':
        print("You head up the creaky stairs...")
        sleep(4)
        target.append("zombie")
        print(f"{Text.RED}A Zombie appeared!{Text.RESET}")
        if fight(player_hp = 5, target_hp = 4):
            target.remove("zombie")
            sleep(2)
            tools.append("health potion")
            print(f"{Text.MAGENTA}>Health Potion was added to your inventory for killing the zombie.{Text.RESET}")
            sleep(3)
            print("You run out of the house and head for the town-square.")
            sleep(5)
            town_square()
        else:
            target.remove("zombie")
            print("Run!")
            sleep(1)
            print("You make your way to the town square.")
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
        sleep(4)
        print("You suddenly realize the lights to the castle are on.")
        sleep(3)
        print("But before heading to the castle, you might want to look around for a lightsource first, to get across the bridge safely.")
        sleep(4)
        print(f">You look {Text.GREEN}left{Text.RESET} and see a path with a Lumber Shop.")
        sleep(2)
        print(f">You look to the {Text.GREEN}right{Text.RESET} and see a path with an abandoned General Store.")
        sleep(1)
        direction = input_prompt(f"Type {Text.GREEN}left{Text.RESET} or {Text.GREEN}right{Text.RESET}: ", ['left', 'right'])
        if direction == "left":
            if "key" not in tools:
                sleep(2)
                print("The door is locked. Maybe I should look for a key.")
                sleep(1)
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


    print("You arrive at the General Store.")
    sleep(3)
    print("You look around and notice a vial of red liquid on the shelf behind the frontcounter.")
    sleep(2)
    take_potion = input_prompt(f">Take the Health Potion?\nType {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
    if take_potion == 'y':
        tools.append("health potion")
        print(f"{Text.MAGENTA}>Health Potion was added to your inventory.{Text.RESET}")
        sleep(2)
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
    print("You head back upstairs and make your way out of the General Store.\nPerhaps this key will open the Lumber Shop.")
    sleep(4)
    lumber_shop()


def lumber_shop():
    global tools


    print("You arrive at the Lumber Shop.")
    sleep(2)
    print("You should try the key you found.")
    sleep(1)
    shall_you_pass = input_prompt(f"Type {Text.GREEN}unlock{Text.RESET}: ", ["unlock"])
    print("You turn the key...")
    sleep(2)
    if shall_you_pass == "unlock":
        if "key" in tools:
            print(f"{Text.GREEN}Unlocked.{Text.RESET}")
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
            print("You need to find a key to get in here. Back to the General Store you go.")
            sleep(4)
            general_store()


def town_fountain():
    global weapons
    global tools


    print("You arrive back in the town square to make your way to the bridge that leads to the castle.")
    sleep(2)
    print("But something catches your eye in the fountain, in the middle of the square.")
    sleep(2)
    print("Its a sword!")
    sleep(1)
    weapons.append("sword")
    print(f"{Text.MAGENTA}>Sword was added to your inventory.{Text.RESET}")
    sleep(2)
    print("You notice an unfamiliar language engraved in the side of the blade. And on the other side.. a picture of a dragon?")
    sleep(1)
    print("You feel a lot stronger now.")
    sleep(2)
    if "matchbox" in tools:
        print("You light your torch and make your way towards the bridge.")
        sleep(4)
        the_bridge()
    else:
        print("You have nothing to light your stick with.\nBack to your house to check the kitchen for matches!")
        sleep(5)
        kitchen()



def the_bridge():
    global target


    print("You start making your way across the bridge.")
    sleep(2)
    print("You feel the bridge slightly shaking under your feet..Wonder what that could be.")
    sleep(3)
    target.append("zombie")
    print(f"{Text.RED}A Zombie appears!{Text.RESET}\nTime to fight!")
    sleep(2)
    if fight(player_hp=10, target_hp=4):
        target.remove("zombie")
        print("You continue your way across the bridge.")
        sleep(4)
        print("Finally you arrive at the castle.")
        sleep(2)
        the_castle()
    else:
        target.remove("zombie")
        print(f"{Text.RED}Game over.{Text.RESET}")
        sleep(2)
        end_game()


def the_castle():
    global weapons
    global team


    print("You walk inside the castle and notice a skeleton of what use to be a king, sitting on a charred throne.")
    sleep(2)
    print("You hear a loud thumping noise coming from the dungeon that shakes the castle.")
    sleep(2)
    print("You make your way down the spiral staircase towards the dungeons to investigate...")
    sleep(5)
    print(f"You arrive in the middle floor. It appears to be the prison of the castle.\nDo you: walk down the corridor to {Text.GREEN}explore{Text.RESET} the cells or {Text.GREEN}go{Text.RESET} to the bottom floor.")
    direction = input_prompt(f"Type {Text.GREEN}explore{Text.RESET} or {Text.GREEN}go{Text.RESET}: ", ["explore", "go"])
    if direction == "explore":
        print("You make your way down the hallway looking in all of the cells...")
        sleep(4)
        print("For the first time you notice a person!")
        sleep(1)
        print("You attempt to talk to the person whos sleeping in one of the cells.")
        sleep(2)
        print("He wakes up and introduces himself to you as 'Red'.")
        sleep(3)
        print("The stranger expresses his excitement of finally seeing someone. He tells you hes been a prisoner for over 5 years now, but hasnt seen anyone in weeks - since the incident.")
        sleep(4)
        print("You ask about the incident, that left the villages and town in fire and ruins.")
        sleep(2)
        print("Red tells you that a dragon and several other beasts were resurrected by a local warlock, who then couldnt control the dragon..")
        sleep(3)
        print("Eventually, whatever was left of the kings true knights were able to capture and lock the dragon in the basement of the castle, before fleeing the town with the survivors.")
        sleep(4)
        print("You tell Red that you plan on killing the dragon with this strange sword you found in the town square.")
        sleep(3)
        print("Red then asks you if you can try to free him from the cell..")
        sleep(4)
        if "axe" in weapons:
            print("Maybe you can free the prisoner with a swing of your axe?")
            free_prisoner = input_prompt(f"Type {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", ['y', 'n'])
            if free_prisoner == 'y':
                print(f"{Text.CYAN}>You swing your axe and free Red!{Text.RESET}")
                sleep(2)
                print("Red thanks you for freeing him.\nHe then offers to help fight the dragon if you would give him your axe.")
                sleep(1)
                print("Do you trust Red with your >Axe?")
                sleep(1)
                give_axe = input_prompt(f"Type {Text.GREEN}y{Text.RESET} or {Text.GREEN}n{Text.RESET}: ", {'y', 'n'})
                if give_axe == 'y':
                    weapons.remove("axe")
                    print(f"{Text.RED}>You give Red your axe.{Text.RESET}")
                    team.append("red")
                    print(f"{Text.YELLOW}>Red joins your team.{Text.RESET}")
                    sleep(2)
                    print("You and Red make your way towards the dungeon.")
                    sleep(4)
                    battle_room()
                else:
                    print("You dont trust a prisoner enough to give him an axe.")
                    sleep(2)
                    print("You head towards the staircase to go downstairs.")
                    sleep(4)
                    battle_room()
            else:
                print("You dont trust the prisoner.")
                sleep(2)
                print("You head towards the staircase to go downstairs.")
                sleep(4)
                battle_room()
        else:
            print("You tell Red you have nothing to free him with.")
            sleep(2)
            print("With no way to free Red, you turn and head towards the staircase leading to the basement...")
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
    if fight(player_hp=10, target_hp=20):
        target.remove("dragon")
        print("You beat the dragon!")
        sleep(2)
        print("You and Red have restored peace in the town again.")
        sleep(10)
        end_game()
    else:
        target.remove("dragon")
        print(f"{Text.RED}Game over.{Text.RESET}")
        sleep(6)
        end_game()


def end_game():
    print("\n" * 6)
    exit_ = input_prompt(f"Type {Text.GREEN}quit{Text.RESET} to exit: ", ["quit"])
    if exit_ == "quit":
        display_title()
        quit()




starting_point()