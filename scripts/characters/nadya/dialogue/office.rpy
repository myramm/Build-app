label nadya_button_office:
    show anon b_sit with {'master': dissolve}:
        xoffset -250
    anon "Well, you look comfortable."
    nadya "Da."
    show nadya b_dressed_couch_relax with {'master': dissolve}
    nadya "You can say many terrible things about my father but it's hard to deny, he had good taste."
    pause
    nadya "Come, sit closer if you’d like...."
    nadya "... I do not bite."
    show anon f_happy

    menu nadya_button_office.choice:
        "So how does it feel to be in charge?":
            jump nadya_button_office.boss
        "Where's {b}Katya{/b}?":

            jump nadya_button_office.katya
        "Sex":

            jump nadya_button_office.sex
        "I can't stay.":

            pass

    anon f_shy "I can't stay, {b}Nadya{/b}."
    show nadya b_dressed_couch f_pouting with {'master': dissolve}
    nadya "No?"
    nadya "Well, that is pity."
    nadya f_sexy "I was looking forward to sexy times with your beautiful cock."
    anon "Sorry."
    show anon a_shy_neck f_shy with {'master': dissolve}
    anon "Another time, perhaps?"
    nadya f_normal "Yes, yes... Another time."
    show anon a_idle
    with {'master': dissolve}
    nadya "{b}Katya{/b} will service me instead."
    anon f_normal "Alright, well... Good night, {b}Nadya{/b}."
    nadya "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    return


label nadya_button_office.blowjob:
    anon f_shy "Your mouth felt really good last time..."
    nadya f_confused "You want to make sexy times in my mouth?"
    show anon f_shy_low
    pause
    nadya f_normal "Very well..."
    show anon f_shy
    nadya "... But I hope you plan to return favor one day!"
    anon f_flirt "That can probably be arranged."
    pause
    nadya f_sexy "Come."
    show anon a_idle b_sit_naked_up f_shy_low od_naked_dick3:
        xoffset 0
    with dissolve
    pause

    call scene_nadya_blowjob.repeat
    $ unlock_scene('nadya', '01_unlocked')

    call nadya_button_stage
    show nadya b_naked_couch a_cig_smoking
    show anon b_sit_back_remove_shorts2 f_worried_down od_dick1:
        xoffset -250
    with fade
    pause
    show anon a_remove_shorts1 b_sit
    show nadya a_down_cig f_pouting o_smoke
    with dissolve
    pause
    show anon a_idle b_sit f_worried
    show nadya f_normal -o_smoke
    with {'master': dissolve}
    nadya "There."
    nadya "Cigarette is taste better."
    anon f_confused "You should really quit smoking, you know?"
    nadya f_frowning "Bah!"
    anon f_worried "Seriously, it's bad for you."
    show anon f_surprised
    nadya @ f_eyeroll "\"Seriously, is bad for you.\""
    show anon f_unimpressed
    nadya "You Americans become such pussy these days..."
    nadya "... I have no idea how you win cold war."
    anon @ -m_talk "..."
    nadya "Spare me your silly lecture and tell {b}Svetlana{/b} to send for {b}Katya{/b}."
    show anon f_tired
    nadya f_normal "She will finish me off."
    anon f_sad_down "Y-yeah, okay."
    nadya f_happy "Good boy."
    hide anon
    show nadya a_cig_smoking
    with dissolve
    pause
    show nadya a_down_cig f_pouting o_smoke with dissolve
    pause
    show nadya f_happy -o_smoke with dissolve
    pause

    call svetlana_button_stage
    show svetlana a_crossed f_concerned:
        xoffset 150
        xzoom -1
    with fade
    show anon a_sides with dissolve:
        xoffset 100
        xzoom -1
    svetlana "Over so soon?"
    anon f_worried "Yeah, umm..."
    show anon a_point_back
    with {'master': dissolve}
    anon "... She asked for {b}Katya{/b}."
    show svetlana a_sides f_smirk with {'master': dissolve}
    svetlana "Heh, that is not surpise."
    show anon a_sides
    with {'master': dissolve}
    svetlana "{b}Katya{/b} is very skilled with tongue."
    anon f_shy "Yeah, that's what I hear."
    svetlana f_laugh "Heh, I will get her."
    svetlana f_happy "Have safe journey home."
    anon f_normal "Thanks."
    return


label nadya_button_office.bow:
    anon "How about you lie down on your side again?"
    nadya f_happy "Da."
    show anon f_happy
    nadya "This is good position!"
    nadya "I like very much."

    call scene_nadya_sex_office.repeat
    $ unlock_scene('nadya', '02_unlocked')

    call nadya_button_stage
    show nadya b_naked_couch
    show anon b_sit_back_remove_shorts2 f_shy_down od_dick1:
        xoffset -250
    with fade
    pause
    show anon a_remove_shorts1 b_sit with {'master': dissolve}
    nadya "This was good sexy times."
    show anon a_idle b_sit f_normal with {'master': dissolve}
    anon "Yeah, it was."
    nadya f_sexy "You come back soon, we do more."
    anon f_flirt "Absolutely."
    nadya f_normal "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    anon f_normal "Goodbye, {b}Nadya{/b}."
    hide anon with dissolve

    call svetlana_button_stage
    show svetlana f_smirk:
        xoffset 150
        xzoom -1
    with fade
    show anon a_sides with dissolve:
        xoffset 100
        xzoom -1
    svetlana "Sounds like you manage to please her once again."
    anon f_brag "Yeah, I believe so."
    svetlana "She have many orgasm... I hear."
    show anon a_rub f_worried with {'master': dissolve}
    anon "Oh, right... ummm... sorry."
    svetlana f_curious @ -m_talk "Hmm?"
    show anon a_sides with {'master': dissolve}
    anon "I'm sure it's awkward for you, having to listen to us."
    svetlana f_smirk "No..." (show_native="Nyet...")
    svetlana "... I do not mind."
    show anon f_normal
    pause
    svetlana "Truthfully, is kind of exciting."
    show anon a_shy_neck f_shy_left of_blush with {'master': dissolve}
    anon "Oh?"
    show anon f_shy
    svetlana "Perhaps, {b}Miss Chernyshevsky{/b} would let me guard from opposite side of door in future, eh?"
    show anon a_sides with {'master': dissolve}
    anon "Heh, yeah... Maybe."
    show anon f_normal -of_blush
    with dissolve
    pause
    return


label nadya_button_office.boss:
    anon f_normal "So how is leadership suiting you?"
    show nadya a_up f_happy with {'master': dissolve}
    nadya "Is wonderful."
    nadya "I do as I please and everyone obeys."
    show nadya a_idle
    with {'master': dissolve}
    nadya "We are finally making profits and now that we are legitimate business, we have no more problems with police."
    anon "That's good to hear."
    nadya "Da."
    pause
    nadya f_normal "Have you make decision yet?"
    anon f_confused @ -m_talk "Hmm?"
    nadya "My offer..."
    nadya "... For job."
    anon f_shy "Oh, umm... No, sorry."
    anon "I need some more time."
    nadya f_frowning "{i}*Sigh*{/i} Very well."
    pause
    nadya f_sexy "Heh."
    anon f_confused "What?"
    show nadya a_up f_bored with {'master': dissolve}
    nadya "All day, it's, \"Yes, boss.\" or \"Right away boss!\""
    show nadya a_idle
    with {'master': dissolve}
    nadya f_pouting "You are only person who tells me I must wait..."
    anon "Oh?"
    nadya f_sexy "It excites me."
    anon f_flirt "{i}*Gulp*{/i} I see."
    jump nadya_button_office.choice


label nadya_button_office.katya:
    anon f_normal "Do you know where {b}Katya{/b} is?"
    nadya f_normal "I give her evenings off."
    nadya "To do as she pleases."
    nadya "She has proven to be surprisingly good business advisor and I would keep her happy."
    anon f_confused "Oh?"
    nadya "American men seem especially... susceptible, to her charms."
    show nadya a_up f_happy
    with {'master': dissolve}
    nadya "They bend over backwards to please her."
    anon f_shy "Y-yeah, I could see that."
    show nadya a_idle with dissolve
    jump nadya_button_office.choice


label nadya_button_office.sex:
    anon f_shy "Might you want to-"
    nadya f_sexy "I am always eager for sexy times with you, {b}[firstname]{/b}."
    pause
    show nadya b_dressed_couch with {'master': dissolve}
    nadya "Let's get rid of clothes, eh?"
    show nadya a_undress1 f_sexy_down with {'master': dissolve}
    anon "Good idea."
    show anon f_shy_low
    show nadya b_dressed_couch_undress2
    with dissolve
    pause
    show anon a_surprised f_surprised_high behind nadya
    show nadya b_dressed_couch_undress3
    with dissolve
    pause
    show anon f_surprised_down o_sit_boner
    show nadya a_undress4 b_naked_couch behind anon
    with dissolve
    pause
    show anon a_idle f_flirt_low
    show nadya a_undress5
    with dissolve
    pause
    show nadya a_undress6 f_happy_back with dissolve
    pause
    show nadya a_idle f_happy with dissolve
    pause
    nadya "There."
    show anon f_flirt
    nadya "You like to watch, yes?"
    anon "{i}*Gulp*{/i} Y-yeah, I do."
    show anon f_flirt_low
    show nadya f_sexy_down
    pause
    nadya f_sexy "Is your turn now."
    anon f_confused @ -m_talk "Hmm?"
    nadya f_bored @ -m_talk "..."
    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Oh, right."
    anon "Sorry."
    show nadya f_sexy_down
    show anon a_remove_shorts1 f_shy_down
    with dissolve
    pause
    show anon b_sit_back_remove_shorts2 -o_sit_boner od_dick_spring with {'master': dissolve}
    nadya f_laugh "Hehe!"
    show anon b_sit_naked_remove_shirt od_dick2
    with {'master': dissolve}
    nadya f_sexy_down @ -m_talk "Mmm."
    show anon a_idle b_sit_naked f_flirt with {'master': dissolve}
    nadya f_sexy "I like to watch too."
    nadya "You are very pretty man, {b}[firstname]{/b}."
    show anon a_shy_neck f_shy_left with {'master': dissolve}
    anon @ -m_talk "..."
    nadya f_laugh "Hehe!"
    show anon f_shy
    pause
    show anon a_idle with {'master': dissolve}
    nadya f_sexy "So..."
    nadya "... What we do now?"

    menu:
        "Blowjob.":
            call nadya_button_office.blowjob
        "Sex.":

            call nadya_button_office.bow

    show svetlana a_wave with {'master': dissolve}
    svetlana "Farewell, {b}[firstname]{/b}." (show_native="Do svidaniya, {b}[firstname]{/b}.")
    show anon a_wave with {'master': dissolve}
    anon "Goodbye, {b}Svet{/b}."
    show svetlana a_sides
    hide anon
    with dissolve
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
