print(r'''
*******************************************************************************
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
left_or_right = input('Type "left" or "right"\n').lower()

if left_or_right == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input('Type "wait" to wait for a boat.'
                 'Type "swim" to swim across.\n').lower()
    if lake == "wait":
        print("Your arrive at the island unharmed.  There is a house with 3 doors.")
        which_doors = input("One red, one yellow and one blue. Which color do you choose?\n").lower()
        if which_doors == "red":
            print("Burned by fire.\n"
                  "Game Over.")
        elif which_doors == "blue":
            print("Eaten by beast.\n"
                  "Game Over.")
        elif which_doors == "yellow":
            print("You found the treasure!  You Win!")
        else:
            print("Game Over.")
    else:
        print("attacked by trout.\n"
              "Game Over.")
else:
    print("Fall into a hole.\n"
          "Game Over.")