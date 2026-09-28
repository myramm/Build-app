label hospital_recovery_nadya_first:
    $ renpy.dynamic(boy=M_nadya.pregnancy.baby_gender == 'boy')

    scene expression game.timer.image('location_hospital_baby_bed{}')
    show svetlana b_dressed f_happy:
        crop (0, 0, 1024, 650)
        xoffset 300
        xzoom -1
        zoom .9
    show nadya b_gown_bed
    with fade
    show anon f_normal with {'master': dissolve}
    nadya f_happy "Ahh, here is papa."
    show svetlana a_sides:
        xoffset -100
        xzoom 1
    with {'master': dissolve}

    if boy:
        nadya "Come say hello to your son."
    else:
        nadya "Come say hello to your daughter."

    show anon f_normal_low with {'master': dissolve}:
        xoffset 150
    anon "Wow, so you were right..."
    show anon f_normal with {'master': dissolve}:
        xoffset 0

    if boy:
        anon "... It's a boy."
    else:
        anon "... It's a girl."

    nadya "Did we not tell you it is known?"
    svetlana "It is known."
    show anon f_shy_low

    if boy:
        anon "He's beautiful."
    else:
        anon "She's beautiful."

    show anon f_normal
    nadya "Da."
    pause

    if boy:
        nadya "We must ensure he is strong as well."
    else:
        nadya "We must ensure she is strong as well."

    if M_nadya.pregnancy.first_baby:
        if boy:
            nadya "He will face many challenges, leading Bratva in future times."
        else:
            nadya "She will face many challenges, leading Bratva in future times."

        show anon f_worried
        pause
        show anon a_frustrated f_confused with {'master': dissolve}

        if boy:
            anon "What if he doesn't want to lead the Bratva?"
        else:
            anon "What if she doesn't want to lead the Bratva?"

        show svetlana f_concerned_back
        show nadya f_confused

        if boy:
            nadya "Why would he not want lead?"
        else:
            nadya "Why would she not want lead?"

        show anon a_sides f_worried with {'master': dissolve}
        nadya "Is tradition."
        show anon f_shy
        show svetlana f_concerned

        if boy:
            anon "I'm just saying, the choice should be his."
        else:
            anon "I'm just saying, the choice should be hers."

        show svetlana f_concerned_back
        nadya f_sexy "Heh, this is ridiculous thinking in Russia..."
        show anon f_worried
        pause
        nadya f_sexy_down "... But perhaps you are right."
        show anon f_happy

        if boy:
            nadya "We live in America now, and the decision should be his."
        else:
            nadya "We live in America now, and the decision should be hers."

        pause
        show nadya f_normal
        show svetlana f_smirk_back

        if boy:
            nadya "But we must give him siblings, should he not wish to lead."
        else:
            nadya "But we must give her siblings, should she not wish to lead."

        show anon f_surprised
        show svetlana f_smirk
        nadya "Bratva must remain in family."
        anon f_flirt "I'm down for that."
        show svetlana f_normal
        nadya f_sexy_down "You hear that little one?"
        nadya "How many brothers and sisters shall we make for you, eh?"
        show anon f_normal
        show svetlana:
            xoffset 400
            xzoom -1
        with {'master': dissolve}
        svetlana "As many as possible."
        svetlana "Big family is much stronger than small."
        show anon a_pocket with {'master': dissolve}
    else:

        if boy:
            nadya "Leadership of Bratva might fall to him, one day."
        else:
            nadya "Leadership of Bratva might fall to her, one day."

        show anon f_worried_low
        show svetlana:
            xoffset 400
            xzoom -1
        with {'master': dissolve}
        svetlana "Siblings will strengthen each other."
        show anon f_worried
        svetlana "Is good to have many babies."
        show svetlana f_happy_down
        nadya f_sexy_down "You hear that little one?"
        show anon f_flirt_grin
        nadya "We shall make many brothers and sisters for you, eh?"
        anon f_flirt "I'm down for that."
        pause
        show anon f_normal

    nadya f_bored "Mmm, all this talk of family is making me sleepy."
    nadya "Would you mind taking baby while I sleep?"
    svetlana f_happy "Is no problem, {b}Miss Chernyshevsky{/b}."
    svetlana "I take."
    show nadya b_gown_bed_sleep
    show svetlana a_baby f_happy_down
    with dissolve
    nadya "Thank you, {b}Svetlana{/b}." (show_native="Spasibo, {b}Svetlana{/b}.")
    show nadya f_sleep
    show svetlana:
        xoffset -50
        xzoom 1
    with {'master': dissolve}
    nadya "Eh, I will see you later, da?"
    anon "Yeah, of course."
    anon "I'll let you get some rest."
    nadya "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    anon "Goodbye, {b}Nadya{/b}."
    show anon a_wave
    show svetlana f_happy
    with {'master': dissolve}
    anon "Goodbye, little one."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
