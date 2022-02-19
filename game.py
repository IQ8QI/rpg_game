def debug(input):
    print("Debug result:")
    print(input, '\n')


def work_in_progress():
    print("Creation in progress\nThank You for trying!")

def init_starting_variables():
    # 1 = Warrior
    # 2 = Mage
    # 3 = Rogue
    # -1 = NA
    global class_dict
    class_dict = {'1': "Warrior", '2': "Mage", '3': 'Rogue'}



def error_wrong_input():
    print("Incorrect command!\nTry again!\n")


def new_game():
    global player_class
    player_class = "-1"
    while player_class == "-1":
        print("Please select You class")
        print("1 = Warrior")
        print("2 = Mage")
        print("3 = Rogue")
        user_input = input('\n')
        if (user_input == "1") | (user_input == "2") | (user_input == "3"):
            player_class = user_input
            debug(player_class)
        else:
            error_wrong_input()
    work_in_progress()


def load_game():
    work_in_progress()


def leave_game():
    print("See You next time!\n*Press Enter key to leave*")
    input()
    exit()


def main():
    init_starting_variables()

    print("""
        ,  ,
          \\\\ \\\\           
          ) \\\\ \\\\    _p_ 
          )^\\))\\))  /  *\\ 
           \\_|| || / /^`-' 
  __       -\\ \\\\--/ / 
<'  \\\\___/   ___. )'
     `====\\ )___/\\\\ 
          //     `"
          \\\\    /  \\
          `"
Welcome in the RPG_Game
v0.003a""")
    while True:
        print("\nRPG_Game")
        print("1 = New Game (comming sooner)")
        print("2 = Load Game (comming soon)")
        print("3 = Leave game")
        user_input = input('\n')
        if user_input == "1":
            new_game()
        elif user_input == "2":
            load_game()
        elif user_input == "3":
            leave_game()
        else:
            error_wrong_input()


if __name__ == "__main__":
    main()
