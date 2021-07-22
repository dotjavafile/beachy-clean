# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Holly") # main character Holly Hua - real name Xiaohui
define t = Character("Thom") # player character Thomas Henry
define m = Character("Mum")
define z = Character("Allan") #Allan Zedeki
define a = Character("Alex") #Alex Alaric
define c = Character("Mrs Compte") #Year advisor
define p = Character("Peter") #Peter Hendrix
define x = Character("Harriet") #Harriet Gardener
define s = Character("Stephanie") #Stephanie Hind
define f = Character("Frank") #Frank Finlayder - guy who lives around the corner, son of Mum's friend

# The game starts here.

label start:
    # Each chapter is the story.

    scene bg room #/images/bg room.jpg (or png)
    show eileen happy #/images/eileen happy.png

    call drive #Holly drives you home

    call wakeup #You find out something happened


    #call graduation #A ceremony for the end of Year12.
    #nothing important happens after the ceremony - you hang out with Allan
    #call dinner #School graduation dinner. Families at the sports club function room.
    #call photos #Year advisor calls everyone up onto the stage, and there is a photo taken. Then groups take photos - Alex, Allan and you get one.
    #call cheongsam #You meet Holly, she is wearing a cheongsam (never noticed she had a waist comment, hear bad things...)
    #call plans #You find out plans for the party


    #call paddock #The party is in a paddock. Two or three big circles of people - you can chat to groups of people about a few subjects
    #call firepit #At the firepit you try to keep warm. Soon your friends have disapeared...
    #call longtalk #The conversation with Holly goes on, and you notice everyone else has left
    #call skipout #Holly invites you to drive with her.


    #call mazada #Holly drives you in her dad's sportscar
    #call dreams #Holly tells you how she imagined Australia would be beachy
    #call citylights #You two walk up from the city gardens to the memorial
    if perv <= 10:
        call breakfast #Holly takes you to her home for noodles
    else:
        #call pervending #ending where Holly calls you out as a pervert

    # This ends the game.
    return

label drive:
    # Holly drives you home in her Dad's sports car with the top down.
    # This is the start of the story, and the last time you see Holly...

    scene bg road
    with fade

    "Just before driving you home, Holly had pulled back the soft-top roof on the little white sports car."
    h "It's nice to drive with the top town."
    "You smiled the whole way home through the sparse morning traffic. Seeing the first shops opening, reminded you that you had been up all night."
    "As the chrisp air swirled through the cabin, you thought about how High School was now over, and you had a new friend driving you home."
    #maybe have a scene transition from the streets to the suburb
    "Holly didn't hear you as you asked her to turn onto your street. She drove right past it still at speed."
    "She then smiled as you, and you updated the directions."
    "You both drove around the block. Past your Primary School, and then the empty park, before stopping out front your parents place."
    
    # You got out of the car.
    t "Thanks. Good morning." #you say as a good bye.
    h "Good morning." #Holly repeats.
    "Holly puts the car into gear, and then turns to tell you something..."
    h "I wish we met earlier."
    t "..."
    "You didn't know how to reply. All you could do was smile."
    "Holly smiled back and then drove off.\nBy the time she reached the end of your street, you were already inside your parent's house..."

    #You then go to bed and sleep.

    return

label wakeup:
    # Wake up to news something had happened... (remember when your mum asked if you walked home from a party 10km out of town...)

    scene bg room
    with fade

    m "Thom you in there?\nThom?"
    t "..."
    m "Thom, where were you last night?\nWhat did you do after the grad dinner?"

    menu:
       "{i}Where did you go after the graduation dinner?{/i}"
       "To the after party. Alex's dad drove us, it was just just out of town.":
           $x = 1
       "To a party just out of town.":
           $x =2
       "Why?":
        jump conti

    m "wha??"

label conti:
    m "Where were you last night?"
    t "After the graduation dinner? Alex's Dad drove Alex, Allan and I to one of the parties."
    d "I thought Allan's dad said he would drive you?"
    t "..."
    m "Did you just go to the one party?"
    t "Yeah. I mean, I stayed there until 3 or 4..."
    m "But you didn't get home until 8."
    return


