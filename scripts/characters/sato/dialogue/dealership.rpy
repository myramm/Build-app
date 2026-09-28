label sato_button_dealership:
    show anon with dissolve
    if game.timer.is_day():
        sato "Oh, hello again, sir."
        sato "I hope you're having a wonderful experience here at our little dealership?"
        anon "It's certainly been interesting."
        sato "Anything I can help you with?"
    else:
        sato "Oh, hello again, sir."
        sato "I'm afraid we're about to be close for the night."
        sato "Is there any last second things I can assist you with?"

    menu sato_button_dealership.choice:
        "Are you in charge here?":

            jump sato_button_dealership.boss
        "Your daughter.":

            jump sato_button_dealership.josie

        "Your employee {b}Kim{/b}." if M_kim.state is None:
            jump sato_button_dealership.kim
        "Additional services?":

            jump sato_button_dealership.service

        "Look! A three-headed monkey!" if M_anon.is_state(S_ano05_cell) and player.stats._dex <= 3:
            jump ano05_cell_sato.fail

        "Woah! Cool sword!" if M_anon.is_state(S_ano05_cell) and player.stats._dex > 3:
            jump ano05_cell_sato.pass
        "I'm good.":

            pass

    anon f_normal "I don't need anything right now."
    sato "Well, if you're looking to buy a vehicle, please see one of our sales people."
    sato f_smiling "I'm sure my daughter {b}Josephine{/b} would be delighted to tend to your needs."
    hide anon with dissolve
    return


label sato_button_dealership.boss:
    anon f_normal "Are you in charge here?"
    sato f_smiling "Yes, indeed."
    sato "Took me twelve years to climb the ladder but I'm finally at the top."
    sato "The only guy I have to answer to now, is me!"
    pause
    sato f_confused "Well, unless you count the regional manager... He's technically my boss."
    pause
    sato "And the company president is his boss..."
    show anon f_worried
    sato "So, I suppose I answer to him too."
    pause
    sato "And then there's the owner."
    anon "So you're more like, halfway up the ladder?"
    sato f_smiling "Well, let's call it three-quarters of the way up."
    show anon f_unimpressed
    pause
    sato f_normal "Right."
    jump sato_button_dealership.choice


label sato_button_dealership.josie:
    anon f_normal "She doesn't seem to like working here very much."
    sato f_angry "My daughter doesn't know what's good for her."
    sato "She's got no ambition!"
    sato "If she had it her way, she'd be lazying about at home, watching the boobtube or whatever it is you kids do nowadays..."
    anon f_shy "Hey, it could be worse."
    sato f_confused "Heh, I don't see how it could be..."
    anon "She could be doing camshows for money."
    sato "Cam- Huh?"
    sato "I don't follow..."
    anon f_unimpressed "Ehh, never mind."
    show sato f_normal
    jump sato_button_dealership.choice


label sato_button_dealership.kim:
    anon f_worried "Your employee {b}Kim{/b}."
    sato "What about him?"
    anon "He's a real ass cactus!"
    sato f_confused "I'm not sure I heard you correctly..."
    sato "Did you say ass cactus?"
    anon "Yes, he was very rude to me."
    sato "{b}Kim Jun Wang{/b}?"
    anon "Yup, that's the one."
    sato f_smiling "You must be mistaken, sir!"
    sato "{b}Kim{/b} is our best salesman and employee of the month, five months running."
    anon f_unimpressed "You've got to be joking."
    sato "No, not at all."
    pause
    anon f_skeptical "Exactly how many salesman do you have working here?"
    sato f_confused "Well, two... If you count my daughter."
    sato "She hasn't made a sale yet, so she's still technically an intern, but I'm sure she'll make one real soon."
    anon "Uh huh."
    show sato f_normal
    pause
    anon "I'm guessing you don't sell many cars here, do you?"
    sato "Hey, c'mon now... We have the highest percentage car sales in all of Summerville!"
    anon f_unimpressed "You're the only dealership in town!"
    sato @ f_confused "Ugh, well, when you put it like that, it sounds way less impressive..."
    anon "Just-"
    anon "Forget it."
    jump sato_button_dealership.choice


label sato_button_dealership.service:
    anon f_worried "You offer additional services?"
    sato "Of course."
    show anon f_normal
    sato "We offer free maintenance to all our customers, so long as their car is under warranty."
    sato "Just see our head mechanic downstairs in the garage, and he'll have you back on the road in no time."
    anon "Alright."
    anon "Anything else?"
    sato "Well, you're welcome to help yourself to some complimentary donuts or coffee, if you'd like."
    sato "You can find some in our break room, just off the show room floor."
    anon @ f_laugh "Okay, I'll keep that in mind."
    jump sato_button_dealership.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
