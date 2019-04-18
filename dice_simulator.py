from random import randint

def get_input():
    return input("Do you want to roll again? [y/n] " )

def roll_dice(sides=6):
    num_rolled = randint(1,sides)
    return num_rolled

def  main():
    rolling = True
    while rolling:
        print("you rolled a {}".format(roll_dice()))
        rolling = "y" in get_input()

        if not rolling:
                return print("Game Over")
           
if __name__ == '__main__':
    main()
