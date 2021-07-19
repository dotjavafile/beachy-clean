# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Holly")
define t = Character("Thom") # main character
define m = Character("Mum") 
define d = Character("Dad")
# Alex and Allan - your friends who shared a table at the school graduation dinner with you.
# Frank - guy who lives around the corner, son of Mum's friend

# The game starts here.

label start:

    scene bg room #/images/bg room.jpg (or png)
    show eileen happy #/images/eileen happy.png

    call drive #Holly drives you home

    call wakeup #You find out something happened

    # This ends the game.

    return

label drive:
    # Holly drives you home in her Dad's sports car with the top down.

    scene bg road
    with fade

    "Just before driving you home, Holly had pulled back the soft-top roof on the little white sports car." 
    "You smiled the whole way home through the sparse morning traffic. Seeing the first shops opening, reminded you that you had been up all night."
    "As the chrisp air swirled through the cabin, you thought about how High School was now over, and you had a new friend driving you home."
    "Holly didn't hear you as you asked her to turn onto your street. She drove right past it still at speed."
    "She then smiled as you, and you updated the directions. You both drove around the block. Past your Primary School, and then the empty park always full of dumped rubbish, before stopping out front your parents place."
    
    # You got out of the car.
    h "I wish we met earlier."
    t "..."
    "You didn't know how to reply. All you could do was smile."
    "Holly smiled back and then started the car. 
    By the time she reached the end of your street, you were already inside your parent's house..."

    return

label wakeup:
    # Wake up to news something had happened... (remember when your mum asked if you walked home from a party 10km out of town...)

    scene bg room
    with fade


    t "Sure, but what's a \"visual novel?\""
    menu:
       "WHAT"
       "It's a videogame.":
           $x = 1
       "It's an interactive book.":
           $x =2

    m "Where were you last night?"
    t "After the graduation dinner? Alex's Dad drove Alex, Allan and I to one of the parties."
    d "I thought Allan's dad said he would drive you?"
    t "..."
    m "Did you just go to the one party?"
    t "Yeah. I mean, I stayed there until 3 or 4..."
    m "But you didn't get home until 8."

    return

