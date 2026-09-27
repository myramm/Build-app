label yumi_button_driveway:
    show anon f_worried with dissolve:
        flip
        xoffset -200
    anon "Hey, {b}Yumi{/b}."

    anon "You got a second?"

    yumi "Sure thing, {b}[firstname]{/b}."

    yumi "Come have a seat in my office."

    anon "Ya baiklah."

    hide anon with dissolve

    scene expression game.timer.image('backgrounds/location_police_car_interior{}.jpg')
    show anon b_dressed_car f_worried
    show yumi b_dressed_car_front f_concerned_left a_down
    show xtra 30
    yumi "Everything alright?" with fade

    menu yumi_button_driveway.choice:
        "Seen anything suspicious?":
            jump yumi_button_driveway.stakeout
        "News from {b}Harold{/b}?":

            jump yumi_button_driveway.harold
        "{b}[deb_name]{/b} and {b}[jen_name]{/b}.":

            jump yumi_button_driveway.family

        "Donat." if M_mia.is_state(S_mia_impress_harold):
            jump yumi_button_driveway.donuts
        "I'm good, thanks.":

            pass

    anon f_worried "I'm good, thanks."

    show yumi f_normal_left
    anon "I just wanted to check in with you."

    anon "Make sure everything is going alright, you know?"

    yumi @ f_concerned_left "Yeah, I get it."

    yumi "There's no need to worry."

    yumi "Those Russians won't try anything with me sitting here."

    anon f_worried "Saya harap Anda benar."

    pause
    anon "Sampai jumpa nanti."

    yumi "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return


label yumi_button_driveway.donuts:
    $ renpy.dynamic(topping=M_harold.get('topping'))
    anon f_worried "I don't suppose you would happen to know what kind of donuts {b}Harold{/b} likes?"

    yumi f_concerned_left "Hah?"

    yumi "Mengapa kamu bertanya?"

    anon "Oh, I'm... Trying to get him to like me."

    yumi "Huh. That's... Strange."

    show anon of_blush with {'master': dissolve}
    anon f_worried_left "I know, but I'm friends with his daughter and-"

    yumi f_normal_left @ f_laugh "Haha! You don't need to explain. I think I got the picture."

    show anon f_worried_surprised
    yumi "Well, every time we visit the donut shop... He puts {b}[topping]{/b} on the top of his donuts."

    show anon -of_blush with {'master': dissolve}
    anon f_normal @ f_shy "Benar-benar?"

    yumi f_normal_left "Yeah, he always gets that topping."

    anon @ f_shy "Okay, thanks for helping me!"

    yumi "Tidak masalah!"

    jump yumi_button_driveway.choice


label yumi_button_driveway.family:
    yumi f_concerned_left "How are your housemates holding up?"

    anon f_worried @ -m_talk "Hmm?"

    anon "Oh, uhh... Fine, I think..."

    yumi f_normal_left "{b}[deb_name]{/b} is such a nice lady!"

    show anon f_normal
    yumi "You know she brought me out a big cup of coffee and a slice of pie this morning?"

    anon "Let me guess, apple?"

    yumi "No, cherry."

    anon f_surprised "!!!"
    anon "Oh snap, she made cherry?!"

    yumi @ -m_talk "Mhmm."

    yumi "Enak sekali!"

    anon "Is there any left?"

    yumi @ f_laugh "Heh, I have no idea..."

    yumi "You'd better hurry and check."

    anon f_normal "Yeah, it's my favorite."

    jump yumi_button_driveway.choice


label yumi_button_driveway.harold:
    anon f_worried "News from {b}Harold{/b}?"

    yumi f_concerned_left "Belum ada apa-apa."

    anon "Oh."

    pause
    yumi f_normal_left "Jangan khawatir, {b}[firstname]{/b}."

    yumi "{b}Harold{/b} and the chief will get something worked out soon."

    yumi "I'm sure of it."

    anon "Ya, saya harap begitu."

    pause
    yumi "I'll let you know as soon as I hear anything."

    anon "Thanks, {b}Yumi{/b}."

    jump yumi_button_driveway.choice


label yumi_button_driveway.stakeout:
    anon f_worried "Seen anything suspicious?"

    yumi f_concerned_left "Yes, actually..."

    anon "Benar-benar?!"

    anon "It wasn't that blacked out car again, was it?"

    anon "Because I should warn-"

    yumi "Do you know the boy who lives next door?"

    pause
    anon f_confused "Hah?"

    yumi "Red hair, freckles, a bit on the hefty side..."

    anon f_normal "Yeah, that's my friend {b}Erik{/b}."

    anon "I've known him practically forever."

    yumi "Is he in the drama class at your school or something?"

    anon "No, I don't think so."

    anon "Mengapa?"

    yumi "He came outside a little bit ago wearing nothing but a fur loincloth and swinging this big toy hammer around..."

    anon f_worried "Oh."

    yumi "It was weird..."

    pause
    yumi f_annoyed_left "... And a little gross."

    anon "Uhh, yeah... That's just {b}Erik{/b} being {b}Erik{/b}."

    anon "He's really into fantasy roleplaying."

    yumi f_concerned_left "Fantasy roleplaying?"

    anon "You know, like orcs and goblins and elves."

    anon "That sorta thing."

    yumi @ -m_talk "Hmm."

    pause
    yumi "Well, I guess that explains it."

    jump yumi_button_driveway.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
