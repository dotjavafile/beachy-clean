# the party after the after party -
# once Alex and Allan are at the 2nd Party Thom is with the small group at the field.
# You can talk to all of the remaining people.

label paddock2:
    #Thom gets a ride with Holly (who didn't know the way)
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

    call mazda

    return


label mazda:
    #You give Holly directions to the party
    t "I never knew you owned such a cool car"
    h "It's my Dad's. He is away I drove it tonight."
    t "That is still pretty cool."
    h "..."
    "You get into the white mazda and Holly turns on the engine and then the lights pop up."
    ""

    return