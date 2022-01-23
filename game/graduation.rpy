#The graduation (Thursday)
label dinner:
    #a graduation dinner


    #background of school hall?
    "High School Graduation was on a Thursday."
    "In the morning there was a ceremony in the school hall."
    ""
    #change to background of hall
    scene bg sportsclub
    with dissolve
    "Then in the evening there was a dinner at the Sports Club Hall."
    ""
    "Dinner was served quickly."
    return

label photos:
    #after the meal there is a photo of everyone in the year on the stage
    #You line up alphabetically so it is Harriet Gardener, *Thomas Henry, Peter Hendrix, Stephanie Hind, Holly Hua,
    "A little bit after the main course was cleared, Mrs Compte called the students to line up at the edge of the dance floor."
    "She gives a short speech"
    show mrsCompte speech
    c "I will like to introduce everyone for the last time to each of the students in the year of 2001."
    c "Alex Alaric"
    show alex happy
    "Your friend Alex is the first to walk across the dance floor, in his mauve shirt and tie."
    ""
    "Mrs Compte continues to calls each student in alphabetical order up to the stage..."
    ""
    hide mrsCompte speech
    hide alex happy

    #Harriet is wearing Wingtip 2 tone shoes.
    show thom happy
    show shadows line
    show harriet happy
    t "Those shoes looks expensive Harriet. Where did you get them?"
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
    return

    
label bestdress:
    t "Who do you think is best dressed today?"
    x "...\nI don't know, do you have someone in mind?"
    "" #maybe turn a little bit embarrased?
    t "I think Holly, she has a nice fitting dress and her hair looks good done up."
    x "You should tell her."
    ""
    t "Maybe she can hear us?" #eyes widen.
    show steph happy 
    s "Who can hear what?"
    x "Thom thinks Holly is the best looking tonight."
    hide harriet happy
    s "Did you hear that Holly?"
    ""
    show holly worried
    h "Hear what?"
    t "I think you're dress and hair looks very nice."
    h "Thanks. You look charming too Thom."
    "Peter gives you a nudge."
    p "Charming..."
    hide holly worried
    hide steph happy
    hide shadows line
    jump presento
    
label partyplan:
    t "What are your plans for the after party?"
    x "I'm going home after this. Have a shift starting at 7am tomorrow morning."
    ""
    hide harriet happy
    show peter happy
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
    hide peter happy
    hide shadows line
    jump presento

label presento:
    # Mrs Compte should be in the top corner of the picture or something...
    show mrsCompte speech
    c "Thomas Henry."
    "You quickly brush down your shirt, then walk smartly across the room. Shake hands with Mrs Compte."
    ""
    "Mrs Compte says something quietly, and then you climb the stairs to wait with the others on statge."
    ""
    hide thom happy
    scene bg stage
    # The stage fills and then a photo is taken.
    show peter happy
    c "Peter Hendrix"
    "Peter wears a cheap black suit, and his matted hair is its natural brown colour for a change."
    "Peter has always shared homerooms with you since Year 7, But you have never shared any other classes with him. He owns a Mini he always talks about since he broke up with Carlay Button in year 11 after a 4 years."
    hide peter happy
    show steph happy
    c "Stephanie Hind"
    "Stephanie is wearing a long flowing black dress, green heals and big ear-rings."
    "Stephanie was your Year 10 Class School Council Representative. She also plays tennis and often missed school for tournaments. For the past year you have sat behind Stephanie in Mathematics, listening to her gossip and trying to explain differentiation to her."
    show holly worried
    c "Holly Wh...\nSorry.\nHolly Hua"
    "Holly is wearing a tight green dress with a high collar, her hair has been styled and her face noticably madeup whiter."
    "Holly moved from China two years ago. She was in your History and Mathematics class, but she always sat on the other side of the room."
    hide holly worried
    ""

    #The photo of the whole year is taken.
    "Mrs Compte continues to call up each of the hundred and thirty students in the year."
    ""
    c "and lastly."
    c "Allan Zedeki"
    z "Woo!"
    "Allan jumps across the dance floor. A little out of character, but recently he has been acting a bit differently. Maybe it is because he found out he is colour blind and can't get into the Defence Force."
    ""
    "Everyone in the year (except those like Burt Thalys who didn't turn up) is now on the stage."
    c "Everyone say 2001!"

    #YEAR GROUP PHOTO with flash    
    "You all say 2001, then cheeze for the serries of photos."
    #YEAR GROUP PHOTO with flash
    ""
    c "There will now be group photos taken just behind the stage here."

    scene bg photobooth
    "The girls get a group photo taken first. Whilst they get ready and the photo is taken all the guys group around and watch."
    ""
    "It takes a long few minutes for the stage to disperse."
    ""
    "Then a few more minutes for the photographer to get ready."
    ""

    #The group is now Thom, Alex and Allan
    # Thom attempts to get out of the photos
    t "Should we just go sit down?"
    a "Why don't you want more photos?"
    menu:
        "Why don't you want more photos?"
        "I feel ugly.":
            call pimples
        "I think I'm the only guy not wearing the tie.":
            call noschooltie

    "The girls do one photo, and then quickly move out into the waiting area next to the stage."
        
    call photos1 #guys photos

    # Stephanie and Carla ask if you want to join the mathematics class photo.
    s "Thomas, everyone in our Mathematics class is getting a photo together."
    k "You need to join us."
    s "We can't have a math class photo without all the boys."
    t "I was the only boy in class. Twenty three in class, and only 1 guy."
    k "We know. So will you get a photo with us?"
    menu:
        "Join the girls in your matheamtics class for a second group photo?"
        "yes":
            call photos2 #matheamtics class photo
        "no":
            t "um..."
            z "Are you affraid to get a photo with the girls?"
            t "no.\nI just don't want anyone to see it one day and think I was the only boy to attended an all girls school."
            k "We would just photoshop you in, either way."
        
    ""

    call photos3 #Photos with Thom, Alex and Allan.

    #You have been avoiding dancing, and soon your parents say they are going home.
    return


label photos1:
    #Photo of the guys

    "All the guys get into the back half of the stage and have their photo taken."
    "There are a few funny faces, then a serious photo."
    ""
    with fade
    #BOYS GROUP PHOTO 

    "Frank lays across the floor infront of the group."

    with fade
    "For the last photo Peter jumps up doing a specky over your shoulders."
    with fade
    "After the flash. You crash into an open section of the floor almost face first."
    ""

    p "Sorry. Hopefully it makea good photo."
    "Peter helps you up."

    "Everyone then shuffles out into the waiting area again."
    ""
    return

label photos2:
    #You were the only guy in your mathematics class
    #the girls ask you to join the class photo, after the photo of the boys and girls.
    z "Thom, you getting a photo with the girls?"
    t "Yup. My matheamtics class."
    ""
    #MATH CLASS PHOTO

    with fade

    ""

    return

label photos3:
    #A photo with Allan and Alex

    #THREE GROUP PHOTO
    a "Where do you think we will be in 10 years time?"
    z "Probly back here at a reunion"

    t "It is a pitty Burt isn't here. He booked a set on our table and didn't show up."

    return