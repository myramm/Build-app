label svetlana_button_depot:
    show anon a_wave with {'master': dissolve}:
        xoffset 100
        xzoom -1
    anon "Hey, {b}Svet{/b}."
    show anon a_sides
    show svetlana a_sides:
        xoffset 150
        xzoom -1
    with dissolve
    svetlana "Hello."

    menu svetlana_button_depot.choice:
        "Just guarding the old office door, huh?":
            jump svetlana_button_depot.guard
        "You ever take a break?":

            jump svetlana_button_depot.break
        "Have fun.":

            pass

    anon f_normal "Enjoy your whole standing still and looking menacing thing."
    svetlana "Da."
    svetlana f_smirk "Enjoy your sexy times with {b}Miss Chernyshevsky{/b}."
    anon f_surprised @ -m_talk "!!!"
    svetlana "I shall be counting the orgasms."
    show anon a_behind_head f_shy of_blush with {'master': dissolve}
    anon "Wow, okay..."
    anon "... No pressure though, right?"
    svetlana f_concerned "Pressure is essential to good orgasm."
    svetlana f_smirk "Try using it on clitoris for explosive results."
    show anon a_surprised f_shock -of_blush with {'master': dissolve}
    anon @ -m_talk "..."
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "R-right."
    show anon a_salute
    with {'master': dissolve}
    anon "Will do."
    show anon a_sides
    with {'master': dissolve}
    anon "Thanks, {b}Svetlana{/b}."
    show svetlana a_wave with {'master': dissolve}
    svetlana "Farewell, {b}[firstname]{/b}" (show_native="Do svidaniya, {b}[firstname]{/b}.")
    hide anon with dissolve
    return


label svetlana_button_depot.break:
    anon f_normal "When's your next break?"
    show svetlana a_crossed f_normal with {'master': dissolve}
    svetlana "{b}Miss Chernyshevsky{/b} does not pay me to take breaks."
    anon f_confused "Yeah, okay... But surely you have to sleep sometime?"
    show anon f_surprised
    show svetlana a_sides f_annoyed
    with {'master': dissolve}
    svetlana "My sleep schedule should not concern you."
    show anon f_worried
    svetlana "I am bodyguard and {b}Miss Chernyshevsky{/b} pays me big monies."
    svetlana f_happy "She is good woman and I will not let her down."
    anon @ -m_talk "Hmm."
    anon f_normal "Alright, that's fair enough, I guess..."
    jump svetlana_button_depot.choice


label svetlana_button_depot.guard:
    anon f_confused "Just guarding the old office door, huh?"
    svetlana f_normal "Da."
    show anon f_normal
    svetlana "{b}Miss Chernyshevsky{/b} prefers privacy while inside office."
    show svetlana a_hips f_happy
    with {'master': dissolve}
    svetlana "But I am always ready should she require me."
    anon @ -m_talk "Mhmm."
    pause
    show svetlana a_sides with {'master': dissolve}
    anon f_shy "Welp, cool beans, I guess."
    jump svetlana_button_depot.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
