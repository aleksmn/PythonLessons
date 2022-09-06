import random


dice_drawing = {
    1: [
        "|     |",
        "|  *  |",
        "|     |"
    ],
    2: [
        "|  *  |",
        "|     |",
        "|  *  |"
    ],
    3: [
        "|  *  |",
        "|  *  |",
        "|  *  |"
    ],
    4: [
        "|*   *|",
        "|     |",
        "|*   *|"
    ],
    5: [
        "|*   *|",
        "|  *  |",
        "|*   *|"
    ],
    6: [
        "|*   *|",
        "|*   *|",
        "|*   *|"
    ]

}


# def roll_dice():

#     dice = random.randint(1, 6)
#     for l in dice_drawing[dice]:
#         print(l)

#     print()
#     return dice


# doRoll = "y"

# while doRoll != "n":

#     d1 = roll_dice()
#     d2 = roll_dice()

#     print(d1, d2)

#     doRoll = input("Roll again? (Y/n)\n")



# ---------------
# Second Example

def roll_dice():

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    for l in range(3):
        print(dice_drawing[dice1][l], "   ", dice_drawing[dice2][l])

    print()
    print("Count:", dice1, dice2, end=". ")

    if dice1 == dice2:
        print("Draw!")
    elif dice1 > dice2:
        print("First player win!")
    else:
        print("Second player win!")


print("Welcome to Dice Roll!\n")

doRoll = "y"

while doRoll != "n":

    roll_dice()

    doRoll = input("Roll again? (Y/n)\n")


