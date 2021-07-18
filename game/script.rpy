# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    scene bg room #/images/bg room.jpg (or png)
    show eileen happy #/images/eileen happy.png

    call drive


    # This ends the game.

    return

label drive:

    "something something something"
    "and then some more"
    
    return