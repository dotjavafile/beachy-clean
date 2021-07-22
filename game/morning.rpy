#Holly and Thom get away from the after party together...


label breakfast:
    # Holly takes you back to her place for breakfast.
    # She cooks noodles, it is nice. Holly then asks you if you want to go to bed, before her mum chases you two out of the kitchen.

    #Holly cooks noodles, and explains Wuhan Hot Dry Noodles (Re.gan.mian).
    "Holly turned on the stove, filled a pot with water and left it to boil as she rummaged through the cupboards."
    t "What will you cook?"
    h "Hot Dry  Noodles.\nThey are very popular breakfast or late night snack in my hometown."
    "As you waited to boil, Holly directed you to mix together a suace of vinegar, soy sauce and a paste in a small bowl."
    t "Will it be spicy?"
    h "Not much. I don't like spice too much."
    "The water came to a rapid boil. Holly opened a bunch of noodles and put them into two small strainers. She put the noodles into the strainers."
    "Holly dipped the two small strainers of noodles into the boiling pot of water for just under a minute.\nShe then drained them and tipped the noodles into a bowl where she added a dash of seasame oil, the sauce, and then some vegtables from a small jar."
    "Holly then topped off the two bowls with a some coriander and dash of chilli oil. She smiled at you."
    h "Rè.gān.miàn.\nBreakfast noddles."
    "You tried to hold the chop sticks together, but the noodles kept slipping back into the bowl. But you persisted.\nEventually the sticky noodles were easier to pick up and shovel from the bowl into you mouth."

    #The kitchen is peaceful, you two are eating in tranquil silence...
    "The rising sun shone through the kitchen windows. Sparkling on the countertop."
    "Holly pushed her bowl forward then smiled at you."
    h "I think we should go to bed."
    
    #You can misunderstand what Holly means by "I think we should go to bed"... is she asking to sleep with you, or asking that you go home?
    menu:
        "{i}Holly just invited you to go to bed...{/i}"
        "Is there a spare bed here I can crash on?":
            $nice += 1
        "Do you want to have sex?":
            $perv += 1
    
    #Holly's mum barges into the room just as you answer. She yells lots of Chinese, and Holly leads you out the back door into the garden and then the garage.
    "Just as you were about to ask, Holly's mum came into the room."
    #You have a few words with Holly, then it is the opening of the game - the drive home.
    return