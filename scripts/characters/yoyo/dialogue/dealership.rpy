label yoyo_button_dealership:
    show anon f_worried with dissolve
    yoyo "Wercome to Saga Dearership, how can {b}Kim{/b} herp-"
    yoyo "Oh, is you."
    show yoyo a_idle
    with {'master': dissolve}
    yoyo "What you want dumb guy?"

    menu yoyo_button_dealership.choice:
        "Can we not do this?":
            jump yoyo_button_dealership.vendetta

        "What's the deal with you and {i}other{/i} {b}Kim{/b}?" if M_yoyo.is_state(S_yoy01_init):
            jump yoyo_button_dealership.villain
        "Nothing.":

            pass

    anon f_brag "Nothing."
    yoyo "Then go away."
    yoyo "Your day of reckoning quickry approaches."
    yoyo "You wirr rue the day you mess with {b}Kim{/b} famiry."
    anon "Uh huh."
    show anon a_wave f_unimpressed with {'master': dissolve}
    anon "Best of luck with that."
    hide anon with dissolve
    yoyo f_angry @ -m_talk "..."
    pause
    yoyo "Silly dumb guy..."
    yoyo "... I get you soon."
    return


label yoyo_button_dealership.vendetta:
    anon f_confused "Can we just not?"
    yoyo f_quizzical @ -m_talk "...?"
    anon f_worried "You know, this whole arch nemesis... evil villain wanting revenge for their similarly evil family..."
    show yoyo f_normal
    anon "... Because I gotta tell ya, I'm pretty burnt out after dealing with your brother..."
    pause
    anon f_confused "... No?"
    show yoyo a_crossed with dissolve
    pause
    anon f_tired "{i}*Sigh*{/i} Fine."
    jump yoyo_button_dealership.choice


label yoyo_button_dealership.villain:
    anon f_confused "What's the deal with you and your brother anyway?"
    yoyo f_quizzical "Dear?!"
    anon "Yeah, you know... the whole comic book evil villain thing..."
    anon f_confused "... Do you guys have some tragic back story or something that explains all this?"
    yoyo f_confused "You think {b}Kim{/b} evir?"
    show anon a_frustrated f_shy
    with {'master': dissolve}
    anon "Well, if the shoe fits..."
    show yoyo a_gimme f_annoyed
    with {'master': dissolve}
    yoyo "Is it evir to furfirr ones destiny?!"
    show anon a_sides f_confused
    with {'master': dissolve}
    anon "... Uhh?"
    show yoyo a_reach
    with {'master': dissolve}
    yoyo "The {b}Kim{/b} famiry are fated to read!"
    show anon f_surprised
    yoyo "It is heavy burden that {b}Kim{/b} must humbry bear for sake of humanity!"
    show yoyo a_sides
    with {'master': dissolve}
    anon f_worried "Okay, so you're legit crazy."
    yoyo "{b}Kim{/b} not crazy, {b}Kim{/b} god!"
    show anon f_surprised
    show yoyo a_fists
    with {'master': dissolve}
    yoyo f_angry @ f_angry_teeth_up "DEARERSHIP GOD!!"
    anon f_skeptical "Yeah, see... that's crazy talk."
    show yoyo a_hips f_quizzical
    with {'master': dissolve}
    yoyo "Oh, now {b}Kim{/b} evir {i}and{/i} crazy?!"
    anon f_worried "I'm saying you should consider that possibility, yes."
    show anon a_surprised_up_both f_surprised_teeth
    show yoyo a_frustrated f_angry
    yoyo "NO!!!" with hpunch
    show anon a_surprised_up f_worried_surprised
    with {'master': dissolve}
    yoyo "{b}Kim{/b} supreme reader!!"
    show anon a_sides f_unimpressed
    with {'master': dissolve}
    yoyo "{b}Kim{/b} must rure from on high with iron fist!!"
    anon "Right."
    show anon a_point_back
    with {'master': dissolve}
    anon "Umm, I'm just gonna go."
    yoyo "Worrd wirr trembre at {b}Kim{/b} feet!"
    hide anon
    with {'master': dissolve}
    yoyo "Hey, where you going?!"
    yoyo "Get back here and kneer before {b}Kim{/b}!!"
    show yoyo a_hips
    with {'master': dissolve}
    yoyo "You bad boy!!"
    yoyo "Come back and beg forgiveness!!"
    return T_yoy01_init
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
