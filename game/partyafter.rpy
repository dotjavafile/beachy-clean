# the party after the after party -
# once Alex and Allan are at the 2nd Party Thom is with the small group at the field.
# You can talk to all of the remaining people.

label paddock2:
    #Thom gets a ride with Holly (who didn't know the way)

    scene bg paddock

    "You look around the paddock."
    "There is now only three other people here, probably all waiting for a ride too."
    menu:
        "Who do you approach to chat to?"
        "Holly":
            h "Hi again."
        "Frank":
            f "..."
        "Esmay":
            e "I don't think I've spoken to you in years Thom."

    #It is taking time, and Holly reminds you she has a car.
    #Frank and Esmay don't know the way, so you can offer to show Holly the way
    call mazda #give directions to Holly for way to Party

    return


label mazda:
    #You give Holly directions to the party
    
    #MX5 SPLASH
    t "I never knew you owned such a cool car"
    h "It's my Dad's. He is away I drove it tonight."
    t "That is still pretty cool."
    h "..."
    "You get into the white mazda and Holly turns on the engine and then the lights pop up."
    ""

    #the way to the party...
    menu:
        "Where to first?"
        "Left turn onto Highway":
            "" #correct
        "Right turn onto Highway":
            ""
    
    menu:
        "Stay on this road until..."
        "After the Hospital":
            "" #correct
        "After the Railway Line":
            ""
    
    menu:
        "We pass HOSPITAL now where?"
        "Left then up the hill":
            ""
        "Second Left then up the hill":
            "" #correct
    
    menu:
        "Which street?"
        "Ridge Street":
            ""
        "Morning Hill Road":
            "" #correct

    "" #arrive at the party

    return


label partyway:
    #demonstrate the way to the party, for Thom on the back of Sophie's scooter
    "left turn towards town on Highway"
    "past the water works"
    "turn off after Hospital"
    "second left"
    "continue up Morning Hill Road"
    return


label paddockway:
    #demonstrate the way from party to paddock, for Thom on back of Sophie's scooter
    "down Morning Hill Road to railway"
    "right and then right again onto Highway"
    "past Hospital"
    "continue on Highway out of town"
    "turn off two kilometers after water works"
    return


label houseparty:
    #Holly and You sit out front of the house party

    return