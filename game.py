def new_game():
    print("Creation in prgoress\nThank You for trying!")

def load_game():
    print("Creation in prgoress\nThank You for trying!")

def leave_game():
    print("See You next time!")
    exit()

def main():
    print("""
        ,  ,
          \\\\ \\\\           
          ) \\\\ \\\\    _p_ 
          )^\\))\\))  /  *\ 
           \_|| || / /^`-' 
  __       -\ \\\\--/ / 
<'  \\\\___/   ___. )'
     `====\ )___/\\\\ 
          //     `"
          \\\\    /  \\
          `"
Welcome in the RPG_Game
v0.002""".center(40))
    while(True):
        print("\nRPG_Game")
        print("1 = New Game (comming soon)")
        print("2 = Load Game (comming soon)")
        print("3 = Leave game")
        user_input = input()
        if user_input == "1":
            new_game()
        elif user_input == "2":
            load_game()
        elif user_input == "3":
            leave_game()
        else:
            print("Incorrect command!\nTry again!", user_input)


if __name__ == "__main__":
    main()

