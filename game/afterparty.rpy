# The after party - in a paddock
# This is a Fox, Hen, Grain problem - where Thom needs to go to the second party then come back.

label going:
    #going to the afterparty

    scene bg nightstreets
    "Going to the After Party"
    "It's in a Paddock east of town."
    return

label paddock:
    $ goaround = 0

    "The paddock is dark."

    # This party breaks down, and you need to move to another party. But there is only 1 scotter, and 2 helmets?
    #Sophie
    v "Hey, one of you three can jump on and I'll take you one by one to the next party?"
    t "Will you come back and get the others?"
    v "Sure. But it will take three trips because I don't trust anyone else driving my scooter."
    ""
    menu:
        "Who do you want Sophie to take to the House Party first?"
        "Send Alex":
            call paddockA
        "Go yourself":
            call partyway #explain the way to the party
            call house1
        "Send Allan":
            call paddockB
    return


label house1:
    #Thom arrives at the 2nd Party
    #ST SCOOTER splash
    scene bg houseparty

    menu:
        "Who do you ask to come next?"
        "Ask for Alex":
            call house2
        "Ask for Allan":
            call house3
    
    #S SCOOTER
    return


label house2:
    #Alex arrives
    #SA SCOOTER

    if goaround >= 1:
        #If Alex arrives after Allan was sent back
        "Alex arrives..."
    else:
        "Sophie returns with Alex"

    #Plan to get Allan here
    menu:
        "How do you get Allan here?"
        "You go back to get Allan":
            call house4
        "Send Sophie back to get Allan":
            #S SCOOTER
            call houseB
        "Send Alex back to get Allan":
            $ goaround += 1
            #SA SCOOTER
            call house3
    return


label house3:
    #Allan arrives
    #SX SCOOTER

    if goaround >= 1:
        #If Allan arrives after Alex was sent back
        "Allan arrives"

    else:
        "Sophie returns with Allan"

    #Plan to get Alex
    menu:
        "How do you get Alex here?"
        "You go back to get Alex":
            call house5
        "Send Sophie back to get Alex":
            #S SCOOTER
            call houseA
        "Send Allan back to get Alex":
            #SX SCOOTER
            $ goaround += 1
            call house2
    return


label house4:
    #You go back and get Allan to go to houseparty
    t "Sophie, I'll ride back with you to get Allan."
    #ST SCOOTER

    call paddockway #tell player the way to the paddock
    scene paddock

    "You wave to Sophie and Allan as they ride off down the driveway."
    #SX SCOOTER
    call paddock2 #Thom gets a ride with Holly
    return


label house5:
    #You go back and get Alex to go to houseparty
    t "Sophie, I'll ride back with you to get Alex."
    #ST SCOOTER

    call paddockway #tell player the way to the paddock from party

    scene paddock

    "You wave to Alex and Sophie as they ride off down the driveway."
    #SA SCOOTER
    call paddock2 #Thom gets a ride with Holly
    return


# # # # # # # # # #
# BAD ENDINGS
# # # # # # # # # #

label paddockA:
    #Bad end?
    #Thom and Allan fight?
    t "Alex, you should go."
    t "Allan and I will find another way there."
    z "Sure. Thom and I need to have a chat..."

    return


label paddockB:
    #Bad end?
    #Alex and Thom fight?
    t "Allan you should go."
    t "Alex and I will come soon."
    a "Are you sure Allan is sober enough to ride pillion?"

    ""

    return


label houseA:
    #Bad end?
    #Thom and Allan fight?
    "Bad end at the house"

    return


label houseB:
    #Bad end?
    #Thom and Alex fight?
    "BAD end at the house"

    return
 