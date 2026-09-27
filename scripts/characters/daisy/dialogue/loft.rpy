label daisy_button_loft:
    scene location_barn_top_night
    show location_barn_top_night_hay as hay
    show daisy b_naked_sleep f_sad_closed
    show location_barn_top_night_post as rail
    daisy "{i}*Mumbles*{/i} N-no!"

    show anon b_dressed_crawl_left behind hay:
        xoffset 300
    with {'master': dissolve}
    pause 1
    show anon b_dressed_crawl_right:
        xoffset 110
    with {'master': dissolve}
    pause 1
    show anon b_dressed_floor f_shy_low:
        xoffset -148
    show daisy behind anon
    show location_barn_top_night_hay as hay behind daisy
    with dissolve
    anon @ -m_talk "( Aww, she's so precious when she's sleeping. )"

    show daisy b_naked_sleep_nightmare f_afraid_closed
    with {'master': dissolve}
    daisy "{i}*Mumbles*{/i} There is no cow level..."

    show anon f_confused_low
    daisy "{i}*Mumbles*{/i} ... High runes are just a myth!"

    anon f_worried_low @ -m_talk "( Sounds like she's having a nightmare. )"


    menu daisy_button_loft.choice:
        "Soothe her.":
            pass
        "Wake her up.":

            jump daisy_button_loft.wake

    show anon a_pat1
    with {'master': dissolve}
    anon "Shh, everything's alright, {b}Daisy{/b}."

    show anon a_pat
    show daisy f_sad_closed
    with {'master': dissolve}
    anon "You're home in your nice warm hay and I'm right here with you."

    show daisy b_naked_sleep f_normal_smelling
    with {'master': dissolve}
    daisy "{i}*Mumbles*{/i} Mmm, {b}[firstname]{/b}..."

    show anon a_pat1 f_shy_low
    with {'master': dissolve}
    daisy "{i}*Mumbles*{/i} ... You'll keep the cow king safe."

    anon "Heh, yes... I'll keep everyone safe."

    anon "You just sleep."

    daisy @ -m_talk "{i}*Zzz*{/i}"

    show anon a_down
    with {'master': dissolve}
    anon @ -m_talk "( There we go. )"

    anon @ -m_talk "( She's sleeping peacefully now. )"

    show anon b_dressed_crawl_right behind hay:
        xoffset -30
        xzoom -1
    with {'master': dissolve}
    pause 1
    hide anon with dissolve
    return


label daisy_button_loft.wake:
    $ renpy.dynamic(first_time=not M_daisy.once('loft_sex'))

    show anon a_poke
    with {'master': dissolve}
    anon "{b}Daisy{/b}?"

    show anon a_poke1
    show daisy f_sad_closed
    with {'master': dissolve}
    daisy "Hmm?"

    show anon a_down f_worried
    show daisy a_wipe_tears b_naked_sleep_up f_sad
    with {'master': dissolve}
    daisy "{b}[firstname]{/b}?"

    show daisy a_down
    with {'master': dissolve}

    if first_time:
        anon "Apakah kamu baik-baik saja?"

        show anon b_dressed_floor_hug_daisy f_surprised
        hide daisy
        with {'master': dissolve}
        daisy "I was having a terrible dream!"

        anon f_worried "Oh?"

        daisy "This mean lady was coming to kill the cow king with ice magic and steal his special rocks!"

        anon "That sounds... umm, bad?"

        daisy "It was really bad!"

    else:

        anon "Bad dreams again?"

        show anon b_dressed_floor_hug_daisy
        hide daisy
        with {'master': dissolve}
        daisy "Ya!!"


        if random.random() < .33:
            daisy "This mean old man was coming to kill the cow king with an army of spooky skeletons!"

        elif random.random() < .50:
            daisy "This mean lady with shiny armor and bow and arrow was coming to kill the cow king!"

        else:
            daisy "This big mean man with blue tattoos was coming to kill the cow king with an axe!"


        anon f_shy "The cow king again?"

        daisy "It was really scary!"


    show anon b_dressed_floor o_boner
    show daisy b_naked_sleep_up behind rail
    with {'master': dissolve}
    daisy "Thank you for waking me up."

    anon f_shy "Terima kasih kembali."

    pause

    if first_time:
        daisy f_sad @ f_surprised_low "{i}*Gasp*{/i} Oh no, your weasel!"

        anon f_confused @ -m_talk "Hmm?"

        daisy "He's sick again!"

        anon f_confused_down "Oh, uhh..."

        show anon f_shy of_blush
        with {'master': dissolve}
        daisy f_shy "Do you wanna use my floogina to make him feel better?"

        anon "Heh, it's {i}va{/i}-gina, {b}Daisy{/b}."

        daisy "Oh right, sorry!"

        daisy f_normal "{i}Va{/i}-gina."

        pause
        daisy "You can use my vagina if you want, {b}[firstname]{/b}..."

        show anon f_happy -of_blush
        with {'master': dissolve}
        daisy "... I really like it when you do!"

        anon "Ya?"

        daisy "Ya!"

        daisy f_shy_back "And it always makes me really sleepy too..."

        daisy f_normal "... I'll have the best dreams!"

    else:

        daisy f_low "Do you think we could play hide the weasel again?"

        anon f_confused @ -m_talk "Hmm?"

        daisy f_normal "You know, to help me sleep?"

        anon f_confused_down "Oh, uhh..."


    anon f_shy "Well, if you think it'll help-"

    show anon a_empty
    show daisy a_pull_anon
    with {'master': dissolve}
    daisy "Yes, come, come!"


    call scene_daisy_sex_loft.repeat
    $ unlock_scene('Daisy', '03_unlocked')

    scene location_barn_top_night
    show location_barn_top_night_hay as hay
    show daisy a_wipe_tears b_naked_sleep_up f_normal_smelling
    show anon b_dressed_floor:
        xoffset -148
    show location_barn_top_night_post as rail
    with fade
    daisy "{i}*Yaaaaaaaaaawn*{/i}"

    show daisy a_down f_normal
    with {'master': dissolve}
    anon "Think you'll sleep better now?"

    show anon f_shy_low
    show daisy b_naked_sleep f_normal_smelling
    with {'master': dissolve}
    daisy @ -m_talk "Mhmm."

    daisy "Terima kasih, {b}[firstname]{/b}."

    show anon a_pat1
    with {'master': dissolve}
    anon "You're welcome, {b}Daisy{/b}."

    show anon a_pat
    with {'master': dissolve}
    pause
    show anon a_pat1
    with {'master': dissolve}
    anon "Sweet dreams."

    show anon a_down
    with {'master': dissolve}
    daisy @ -m_talk "{i}*Zzz*{/i}"

    show anon b_dressed_crawl_right behind hay:
        xoffset -30
        xzoom -1
    with {'master': dissolve}
    pause 1
    hide anon with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
