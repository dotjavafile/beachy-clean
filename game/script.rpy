# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    define h = Character("Holly", color="#1e7b1e") # main character Holly Hua - real name Xiaohui
    define t = Character("Thom", color="#008B8B") # player character Thomas Henry

    #Thom's two friends
    define z = Character("Allan") #Allan Zedeki
    define a = Character("Alex") #Alex Alaric
    
    #Teachers and Parents
    define c = Character("Mrs Compte") #Year advisor
    define d = Character("Dad")
    define m = Character("Mum")
    
    #People in Thom and Holly's Home-room/School House
    define p = Character("Peter") #Peter Hendrix
    define x = Character("Harriet") #Harriet Gardener
    define s = Character("Stephanie") #Stephanie Hind

    #Other students in the grade
    define f = Character("Frank") #Frank Finlayder - guy who lives around the corner, son of Mum's friend
    define k = Character("Carlay") #Carlay Button Peter's old girlfriend, fashion student
    define v = Character("Sophie") #Sophie North - see has a scooter and will give you guys a ride to the House Party
    define e = Character("Esmay") #Esmay Port - you had Art and IT with her in year 8 and 9. But haven't spoken to her since.



# The game starts here.

label start:
    # Each chapter is the story.

    scene bg room #/images/bg room.jpg (or png)
    show eileen happy #/images/eileen happy.png

    call drive #Holly drives you home

    #hook to go back in time and tell the story of graduation night.
    
    # At the graduation dinner
    call dinner #
    call photos #Year advisor calls everyone up onto the stage, and there is a whole year photo and then group photos

    #At the afterparty
    call going
    call paddock

    #call paddock #The party is in a paddock. Two or three big circles of people - you can chat to groups of people about a few subjects
    #call firepit #At the firepit you try to keep warm. Soon your friends have disapeared...
    #call longtalk #The conversation with Holly goes on, and you notice everyone else has left
    #call skipout #Holly invites you to drive with her.


    #call mazada #Holly drives you in her dad's sportscar
    #call dreams #Holly tells you how she imagined Australia would be beachy
    #call citylights #You two walk up from the city gardens to the memorial
    call breakfast #Holly takes you to her home for noodles
    
    # This ends the game.
    return


label drive:
    # Holly drives you home in her Dad's sports car with the top down.
    # This is the start of the story, and the last time you see Holly...

    scene bg drivestreets
    with fade

    "Just before driving you home, Holly had pulled back the soft-top roof on the little white sports car."
    h "It's nice to drive with the top town."
    ""
    "You smiled the whole way home through the sparse morning traffic. Seeing the first shops opening, reminded you that you had been up all night."
    "As the chrisp air swirled through the cabin, you thought about how High School was now over, and you had a new friend driving you home."
    #maybe have a scene transition from the streets to the suburb
    ""
    "Holly didn't hear you as you asked her to turn onto your street. She drove right past it still at speed."
    t "That was my street."
    "She smiled as you updated the directions."
    t "Just make a right before the school, then we'll drive around the block."
    "She drove slowly past your old Primary School,\nand then the empty park,\nbefore stopping out front your parents place."
    ""
    scene bg drivehome
    # You got out of the car.
    t "Thanks. Good morning." #you say as a good bye.
    h "Good morning." #Holly repeats.
    "Holly puts the car into gear, and then turns to tell you something..."
    h "I wish we met earlier."
    t "..."
    "You didn't know how to reply. All you could do was smile."
    "Holly smiled back and then drove off."
    ""
    "By the time she reached the end of your street, you were already inside your parent's house..."

    #You then go to bed and sleep.

    return


