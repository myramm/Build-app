label nadya_button_pregnant:
    if L_warehouse_depot.is_here(M_nadya):
        jump nadya_button_pregnant_depot
    jump nadya_button_pregnant_office


label nadya_button_pregnant_depot:
    pause .1
    show nadya f_surprised
    show svetlana f_surprised
    "{i}*Workers chattering*{/i}"
    show svetlana a_crossed
    show nadya a_angry f_angry:
        xoffset 675
        xzoom -1
    with {'master': dissolve}
    nadya "Hey, stop loitering about!"
    show svetlana:
        xoffset 450
    with {'master': dissolve}
    nadya "Back to work, all of you!"
    show anon f_worried behind nadya with dissolve:
        xoffset -100
    nadya "What, you think because I am pregnant I will not walk over and make example of you?!"
    show anon f_worried_surprised
    nadya "I stuff you in potato sack and ship you back Russia!"
    show anon f_worried
    anon "Ehh, {b}Nadya{/b}?"
    show anon a_surprised_up_both f_worried_surprised
    show nadya a_hips f_frowning:
        xoffset 100
        xzoom 1
    show svetlana a_sides f_curious:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    nadya "What?!"
    show svetlana f_happy
    nadya f_normal "Oh."
    show anon a_sides f_worried
    with {'master': dissolve}
    nadya "Sorry, {b}[firstname]{/b}." (show_native="Izvinite, {b}[firstname]{/b}.")
    nadya "The hormones are running crazy inside me..."
    show anon a_surprised f_shy_cringe
    show nadya f_angry:
        xoffset 675
        xzoom -1
    show svetlana f_concerned_back
    with {'master': dissolve}
    nadya "... And my idiot workforce is testing my last nerve!"
    show anon a_sides f_worried with {'master': dissolve}
    anon f_worried "Y-yeah, I can see that."
    show nadya f_frowning:
        xoffset 100
        xzoom 1
    show svetlana f_normal
    with dissolve
    pause

    menu nadya_button_pregnant_depot.choice:
        "How's the baby?" if 1 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_depot.sick

        "How's the baby?" if 2 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_depot.predict

        "How's the baby?" if 3 <= M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_depot.soon
        "Shouldn't you be off your feet?":

            jump nadya_button_pregnant_depot.work
        "I'll leave you to it.":

            pass

    anon f_shy "Just be careful, okay?"
    nadya f_normal "Bah, you worry too much."
    nadya "I am fine."
    show svetlana a_hips f_concerned:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "Ugh, what are they doing?"
    show anon f_confused
    show nadya f_confused:
        xoffset 675
        xzoom -1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"
    show anon f_surprised_teeth
    show nadya a_angry f_angry
    with {'master': dissolve}
    nadya "Hey, those are for VIP customer!"
    show anon f_surprised
    nadya "Put them in overnight delivery pile, you fucking morons!"
    show anon a_facepalm f_eyeroll with {'master': dissolve}
    svetlana "You should have payed extra for literate workers..."
    hide anon with dissolve
    return


label nadya_button_pregnant_depot.predict:
    show anon f_normal

    if M_nadya.pregnancy.baby_gender == 'girl':
        anon "How is the baby{#girl} doing?"
        show nadya a_idle f_sexy_down with {'master': dissolve}
        nadya "She starts to kick."
        anon f_confused "She?"
        nadya f_happy "Da, is girl."
        anon "You can tell?"
        show svetlana a_hips f_happy with {'master': dissolve}
        svetlana "{b}Miss Chernyshevsky{/b} is craving sweet things."
        svetlana "This means baby is girl."
    else:

        anon "How is the baby{#boy} doing?"
        show nadya a_idle f_sexy_down with {'master': dissolve}
        nadya "He starts to kick."
        anon f_confused "He?"
        nadya f_happy "Da, is boy."
        anon f_confused "You can tell?"
        show svetlana a_crossed f_normal with {'master': dissolve}
        svetlana "{b}Miss Chernyshevsky{/b} is craving savory things."
        svetlana "This means baby is boy."

    anon f_skeptical "What?"
    anon "That sounds like old wives tale nonsense to me..."
    show nadya a_hips f_angry
    show svetlana a_sides f_annoyed
    with {'master': dissolve}
    svetlana "It is known."
    show anon f_worried
    nadya "Da, it is known."
    show anon a_hands_up f_worried_surprised with {'master': dissolve}
    anon "Okay, okay... it is known."
    show nadya f_normal
    show svetlana f_normal
    show anon a_sides f_tired
    with {'master': dissolve}
    anon "Sheesh."
    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_depot.sick:
    anon f_normal "How is the baby doing?"
    nadya f_normal "Is not baby yet."
    show svetlana f_concerned_back
    nadya f_annoyed_down "More like peanut, with unreasonable hatred for breakfast."
    anon f_worried "You've been feeling sick in the mornings?"
    nadya f_frowning "Da."
    show svetlana f_concerned
    nadya f_normal "{b}Svetlana{/b} says, is perfectly normal."
    show svetlana a_hips f_normal with {'master': dissolve}
    svetlana @ -m_talk "Mhmm."
    svetlana "Baby always makes sick during early pregnancy."
    svetlana "It will stop eventually."
    anon f_shy "Well, that's good news."
    show svetlana a_sides with dissolve
    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_depot.soon:
    anon f_normal "How is the baby doing?"
    show anon f_worried
    show svetlana f_concerned_back
    show nadya f_annoyed_down

    if M_nadya.pregnancy.baby_gender == 'girl':
        nadya "She stubbornly refuses to leave womb..."
    else:
        nadya "He stubbornly refuses to leave womb..."

    nadya "... Is infuriating!"
    show nadya f_frowning
    show svetlana f_concerned:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    svetlana "I tell you, orgasm make baby come faster."
    show anon f_surprised
    nadya @ f_eyeroll "And I tell you..."
    show anon a_surprised_up m_talk
    with {'master': dissolve}
    nadya "... {b}Katya{/b} gives me six orgasm yesterday and still no baby!"
    show anon a_surprised_up_both f_surprised_teeth -m_talk
    with {'master': dissolve}
    nadya "My clitoris is swollen like balloon animal!"
    svetlana @ f_curious "Well, it always work for me..."
    show anon a_sides f_surprised
    with {'master': dissolve}
    nadya f_bored_down @ f_bored "{i}*Sigh*{/i} Just stop talking."
    svetlana f_timid "Da, {b}Miss Chernyshevsky{/b}."
    show svetlana:
        xoffset -100
        xzoom 1
    with {'master': dissolve}
    anon "Wow, okay then."
    pause
    anon f_shy "Is there anything I can do?"
    nadya f_bored "No." (show_native="Nyet.")
    show anon f_worried
    nadya f_worried "I will just occupy mind with work."
    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_depot.work:
    show anon f_confused
    show svetlana a_surprised f_surprised
    with {'master': dissolve}
    anon "Shouldn't you be off your feet?"
    nadya f_frowning @ -m_talk "Hmm?"
    show svetlana a_sides f_concerned_back
    with {'master': dissolve}
    nadya "I am pregnant, not handicapped."
    show anon a_behind_head f_shy with {'master': dissolve}
    anon "Y-yeah, but-"
    show svetlana a_crossed f_concerned with {'master': dissolve}
    svetlana "Business does not wait for baby."
    svetlana f_normal "{b}Russian{/b} women are strong."
    show anon a_sides f_worried
    with {'master': dissolve}
    svetlana "I see them give birth in wheat field and go right back to work."
    show anon f_shock
    svetlana "No problem."
    nadya f_normal "See, {b}Svetlana{/b} knows!"
    show anon f_surprised
    show svetlana a_sides
    with {'master': dissolve}
    nadya "I will continue work."
    show anon f_worried_surprised
    nadya "Lots of monies to be made."
    anon @ -m_talk "..."
    jump nadya_button_pregnant_depot.choice


label nadya_button_pregnant_office:
    show anon b_sit with dissolve:
        xoffset -250
    nadya "Hello, {b}[firstname]{/b}." (show_native="Privet, {b}[firstname]{/b}.")
    nadya f_confused "You come to check on me?"

    menu nadya_button_pregnant_office.choice:
        "How's the baby?" if 1 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_office.tired

        "How's the baby?" if 2 == M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_office.kick

        "How's the baby?" if 3 <= M_nadya.pregnancy.stage:
            jump nadya_button_pregnant_office.soon
        "Can I get you anything?":

            jump nadya_button_pregnant_office.anything
        "I'll let you rest.":

            pass

    anon "I'll let you rest."
    nadya f_normal "Yes, rest."
    nadya "We'll talk more later."
    anon "See ya, {b}Nadya{/b}."
    hide anon with dissolve
    return


label nadya_button_pregnant_office.anything:
    anon f_normal "How about a foot rub?"
    nadya f_sexy_low "Mmm, that does sound nice..."
    pause
    nadya f_sexy "... Perhaps later, da?"
    anon "Yeah, of course."
    jump nadya_button_pregnant_office.choice


label nadya_button_pregnant_office.kick:
    anon "How is the baby doing?"
    nadya f_worried "Ugh, baby starts to kick now."
    anon "Oh, yeah?"
    nadya "Is annoyance during downtime."
    nadya f_annoyed_down "Be quiet and sit still!"
    anon f_worried_surprised "Umm, maybe you shouldn't yell at the fetus?"
    nadya f_frowning "You want I should yell at you instead?!"
    show anon a_surprised f_surprised with {'master': dissolve}
    anon "I uhh-"
    pause
    show anon a_idle f_worried_low with {'master': dissolve}
    anon "N-no."
    nadya "Then be silent!"
    nadya f_annoyed_down "Both of you!"
    show anon f_worried
    nadya f_worried "Mama needs relaxation time."
    jump nadya_button_pregnant_office.choice


label nadya_button_pregnant_office.soon:
    anon "How is the baby doing?"
    nadya f_normal "{b}Svetlana{/b} says baby will come soon."
    nadya "I am eager to be done with this."
    anon f_worried "Yeah, I know you're uncomfortable..."
    anon f_shy "... But you just gotta hang in there a few more days, right?"
    nadya f_worried "{i}*Sigh*{/i} Yes."
    pause
    nadya f_pouting "I would kill for cigarette right now."
    jump nadya_button_pregnant_office.choice


label nadya_button_pregnant_office.tired:
    anon "How is the baby doing?"
    nadya f_worried "Please, no questions... I am tired from long day."
    anon f_worried "Oh, umm... Okay."
    jump nadya_button_pregnant_office.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
