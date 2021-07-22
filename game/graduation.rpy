#The graduation (Thursday)

label dinner:
    #graduation dinner at Sports club with Year 12 students and families

    return

label photos:
    #after the meal there is a photo of everyone in the year on the stage
    #You line up alphabetically so it is Harriet Gardener, *Thomas Henry, Peter Hendrix, Stephanie Hind, Holly Hua,

    #Harriet is wearing Wingtip 2 tone shoes.
    t "Those shoes looks expensive, where did you get them?"
    x "They are wingtips. I had to order them in Melbourne. They are hand made."
    t "Wow, did you buy them for graduation?"
    x "Yes, I went down on Monday after the History exam."
    t "Monday? That was my birthday."
    x "You had two exams on your birthday?"
    t "It could had been worse.\nBoth subjects were my favourites - History and Software Development."
    x "..."
    #shuffle foward, names get called out...
    "As the names get called and one by one the pupils walk across the hall to Mrs Compte, then onto the stage you need to make a bit more conversation."
    menu:
        "What should you talk to Harriet and those around you about?"
        "Best dressed student":
            jump bestdress
        "Plans for tonight":
            jump partyplan

    
    label bestdress:
        t "Who do you think is best dressed today?"
        x "...\nI don't know, do you have someone in mind?"
        t "I think Holly, she has a nice fitting dress and her hair looks good done up."
        x "You should tell her."
        t "Maybe she can hear us?" #eyes widen.
        s "Who can hear what?"
        x "Thom thinks Holly is the best looking tonight."
        s "Did you hear that Holly?"
        h "Thanks. You look charming too Thom."
        "Peter gives you a nudge."
        p "Charming..."
        jump presento
    
    label partyplan:
        t "What are your plans for the after party?"
        x "I'm going home after this. Have a shift starting at 7am tomorrow morning."
        t "What about you Peter, do you have plans after this?"
        p "Thom, are you asking if I am going to the afterparty?"
        t "Are you going to the afterparty?"
        p "Of course. Do you know how to get out to River Bend Road? It on the paddock on the corner."
        t "Oh, that far out."
        p "I can give you a lift if you want. There's no one in the back seat of my mini yet."

        menu:
            "Will you take Peter up on his offer of a ride to the after party?"
            "Yes":
                $ride = 1
            "No":
                $ride = 0

        p "No problem..."
        jump presento

label presento:
    # Mrs Compte should be in the top corner of the picture or something...
    c "Thomas Henry."
    "You quickly brush down your shirt, then walk smartly across the room. Shake hands with Mrs Compte."
    "She whispers something quietly and then you climb the stairs to wait with the others on statge."
    # The stage fills and then a photo is taken.
    return
    