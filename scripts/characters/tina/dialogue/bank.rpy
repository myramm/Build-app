label tina_button_bank:
    $ renpy.dynamic(schedule=M_tina.sex != game.timer._game_day)

    if L_bank_lobby.is_here(M_tina):
        show tina f_laugh
        show anon with dissolve:
            flip
        tina "Good morning, sir!"
        tina "Welcome to-"
        tina f_normal "Oh, it's you."
        pause
        tina f_sexy "What brings you here, {b}[firstname]{/b}?"
    else:
        show anon with dissolve
        anon "Hey, {b}Tina{/b}."
        tina @ -m_talk "Hmm?"
        tina f_sexy "Babyface?!"
        tina "What brings you into my office today?"

    menu tina_button_bank.choice:
        "So you're the bank manager?":

            jump tina_button_bank.manager
        "Did you know my dad?":

            jump tina_button_bank.frank
        "How's {b}Becca{/b}?":

            jump tina_button_bank.becca

        "Schedule sex?" if schedule and player.location == L_bank_cubicle:
            jump tina_button_bank.schedule

        "Schedule sex?" if schedule and player.location == L_bank_lobby:
            jump tina_button_bank.rendezvous

        "Office sex?" if M_tina.sexfriend and player.location == L_bank_cubicle:
            if not M_tina.once('office_sex'):
                jump tina_button_bank.suggest
            else:
                jump tina_button_bank.sex
        "I should go.":

            pass

    anon f_normal @ a_wave "I should go."
    tina f_normal "Yeah, I should get back to work myself."
    anon "It was nice seeing you though."
    tina @ f_laugh "You too, {b}[firstname]{/b}."
    tina "Come back real soon."
    hide anon with dissolve
    return


label tina_button_bank.becca:
    anon f_normal "How's {b}Becca{/b}?"
    tina f_normal @ -m_talk "Hmm?"
    tina @ f_eyeroll "Oh, who knows..."
    tina f_suspicious "She's really changed a lot since her father died."
    tina "I can barely get a sentence out of her nowadays..."
    tina f_annoyed "... And those friends of hers are a bad influence!"
    anon "Oh?"
    tina "That {b}Missy{/b} girl is the most scatterbrained person I've ever met!"
    tina "She's got no filter whatsoever!"
    anon @ f_laugh "Heh, that's true."
    tina "And then there's {b}Roxxy{/b}."
    pause
    tina f_suspicious "Did you know she lives in a trailer park?"
    tina "Eugh, if I'd known my daughter was gonna start bringing home white trash, I would've stayed in the city."
    anon f_worried @ f_surprised -m_talk "..."
    jump tina_button_bank.choice


label tina_button_bank.frank:
    anon f_normal "Did you know my dad?"
    show tina f_normal
    anon "He used to work here."
    tina "No kidding?"
    tina "What was his name?"
    anon "{b}Frank Cummings{/b}."
    tina f_surprised "!!!"
    tina "Are you serious?!"
    anon f_surprised "So, you did know him?"
    tina f_sad "No, not personally."
    tina "He was let go by the previous manager..."
    tina "... But the police were here asking a lot of questions about him."
    show anon f_worried
    tina f_annoyed "I had to spend two weeks combing through bank records because of that mess!"
    anon f_sad_down "Oh, I see."
    tina f_sad "Err, I didn't mean-"
    pause
    tina "Aww, I'm sorry, kid."
    tina "That was uncalled for..."
    anon f_worried "No, it's fine."
    anon "I've been dealing with his mess too."
    jump tina_button_bank.choice


label tina_button_bank.manager:
    anon f_normal "So you're the bank manager?"
    tina f_normal @ -m_talk "Mhmm."
    tina "I was studying to become an accountant when I met Luigi and he encouraged me to keep at it."
    anon "Really?"
    tina "He even paid off my school loans."
    anon @ f_laugh "That's awesome!"
    tina @ f_sad "I couldn't understand why it was so important to him at the time..."
    tina "... But now that he's gone, I'm grateful for it."
    tina "It gives me purpose, you know?"
    anon "Yeah, I get that."
    tina "If it wasn't for this job, I'd probably just be sitting on my ass at home all day."
    jump tina_button_bank.choice


label tina_button_bank.rendezvous:
    anon f_flirt "Want to have sex later?"
    tina f_surprised "Shh, not so loud!"
    anon f_worried "Oh, umm..."
    anon f_shy @ a_behind_head "... My bad."
    show tina with dissolve:
        unflip
        xoffset -500
    pause
    show tina f_sexy with dissolve:
        flip
        xoffset 0
    tina "You're free this evening then?"
    anon "Yup."
    tina @ f_laugh "Wonderful!"
    tina "I'll send {b}Becca{/b} over to her friend's house and we'll have the entire evening to ourselves."
    anon f_flirt "I can't wait."
    tina "Mmm, me neither."
    hide anon with {'master': dissolve}
    anon "See you tonight."
    return 'schedule'


label tina_button_bank.schedule:
    anon f_flirt "Want to have sex later?"
    tina f_sexy "Oh, I'll take it that means you're free this evening then?"
    anon "Yup."
    tina @ f_laugh "Wonderful!"
    tina "I'll send {b}Becca{/b} over to her friend's house and we'll have the entire evening to ourselves."
    anon @ f_laugh a_cheering "I can't wait."
    tina "Mmm, me neither."
    hide anon with {'master': dissolve}
    anon "See you later."
    return 'schedule'


label tina_button_bank.suggest:
    anon f_shy "Can't we have sex here?"
    tina f_sexy "Oh, you naughty boy..."
    tina "... We can't do that!"
    anon f_worried "Why not?"
    tina @ f_laugh "Because there's no lock on my door!"
    tina "What if {b}Liu{/b} comes in?"
    anon f_flirt "I'm sure she'll knock first..."
    pause
    anon @ f_laugh "... And if she doesn't, well then, we'll just ask her to join us."
    tina @ f_laugh "Hah!"
    anon "She'll be into that, don't you think?"
    label tina_button_bank.sex:
    tina "You're so bad..."
    anon "C'mon, I'll be quick."
    show tina f_sexy_down_lipbite
    pause
    tina f_sexy "Well, not too quick I hope."
    anon f_normal "Is that a yes?"
    tina @ f_eyeroll "I suppose."
    show tina with dissolve:
        xoffset -100
    anon f_shy "Really?!"
    tina "Just try to keep your voice down, okay?"
    pause
    anon "Oh, totally!"
    anon "Can do!"
    anon "Not a problem!"
    tina @ f_laugh "Heh, you're too cute!"
    show tina b_dressed_open f_sexy_down_lipbite with dissolve
    pause
    show tina b_dressed_open_boobs_drop01 with dissolve
    pause
    show tina b_dressed_open_boobs_drop02 with dissolve
    show tina b_dressed_open_boobs_drop03 with dissolve
    show tina b_dressed_open_boobs_drop04 with dissolve
    pause
    show tina b_dressed_open_back o_empty with dissolve
    pause
    show tina b_dressed_open_back_undress with dissolve
    pause

    call scene_tina_sex_office.repeat
    $ unlock_scene('tina', '02_unlocked')

    scene expression background(712, 400, 2.5) as stage
    if _return == 'inside':
        show tina b_dressed_open_back
    else:
        show tina f_sexy b_dressed_open_boobs o_glasses
    show anon f_flirt
    with fade
    anon "I'll go get you some paper towels from the bathroom."
    if _return == 'inside':
        show tina f_sexy b_dressed_open_boobs o_glasses with dissolve
    tina "It's alright, I'll take care of it."
    anon f_shy "Are you sure?"
    tina "Yup."
    show tina b_dressed_open_boobs_kiss o_empty
    hide anon
    with dissolve
    pause
    show tina b_dressed_open_boobs o_glasses
    show anon
    with dissolve
    tina "Just promise me we'll do that again sometime..."
    anon f_flirt "Yeah?"
    tina @ f_sexy_down_lipbite -m_talk "Mhmm."
    anon "Definitely."
    tina "See you soon, babyface."
    hide tina with dissolve
    pause 0.5
    anon f_laugh @ -m_talk "( That was awesome! )"
    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
