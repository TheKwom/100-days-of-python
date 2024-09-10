# Day 3 - Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
decision = input(' '*4+f'Type "left" or "right"\n').lower()

if decision == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    decision = input(' '*4+f'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if decision == "wait":
        print("You arrive at the island unharmed. There is a house with three doors.")
        decision = input(' '*4+f'One "red", one "yellow" and one "blue". Which color do you choose?\n').lower()  
        if decision == "yellow":
            print("You found the treasure. You win!")
        elif decision == "red":
            print("It's a rooom full of fire. Game over.")
        elif decision == "blue":
            print("You entered a room full of beasts. Game over.")
        else:
            print("You entered a room that doesn't exist. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")