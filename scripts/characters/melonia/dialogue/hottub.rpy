label melonia_button_hottub:
    return

label melonia_button_hottub.intro0:
    show anon f_worried_low with dissolve
    anon "Excuse me, {b}Mrs. Rump{/b}?"
    melonia "What?"
    anon "May I ask you something?"
    melonia @ f_annoyed_up "Ugh, fine but make it quick!"
    melonia "I'm trying to relax here, {b}Hector{/b}."
    return


label melonia_button_hottub.intro1:
    show anon f_worried_low with dissolve
    anon "Excuse me, {b}Mrs. Rump{/b}?"
    melonia "What?"
    anon "May I ask you something?"
    melonia "That depends..."
    melonia @ f_smirk_peek "... Are you going to entertain me today?"
    anon @ f_skeptical "Entertain you?"
    melonia f_smirk_up "Dance for me, {b}Hector{/b}."
    show anon f_unimpressed
    pause
    anon "I thought we were finished with all that \"Hector\" nonsense?"
    melonia f_smirk_up "Heh, dance for me and I'll call you whatever you want."
    return


label melonia_button_hottub.intro2:
    show anon f_worried_low
    anon "Good afternoon, ma'am."
    melonia "Please, {b}[firstname]{/b}..."
    melonia "... Call me {b}Melonia{/b}."
    anon "Alright."
    return


label melonia_button_hottub.outro0:
    jump melonia_button_common.outro0


label melonia_button_hottub.outro1:
    jump melonia_button_common.outro1


label melonia_button_hottub.outro2:
    anon f_worried_low "I should go."
    melonia f_pouting_up "What, already?"
    anon "Yeah, I'm afraid so."
    melonia f_annoyed_up "But you haven't even fucked me yet!"
    anon "Sorry, maybe later."
    hide anon with dissolve
    melonia "{b}[firstname]{/b}!!"
    show melonia b_jacuzzi_topless_edge f_annoyed with dissolve
    melonia "Don't leave!"
    pause
    melonia f_yell "Get back here and fuck me this instant!"
    return


label melonia_button_hottub.dance:
    if level == 1:
        anon f_worried_low "Fine, I'll dance."
        melonia f_smirk_up "Good boy."
    else:
        anon f_shy_low "Should I dance for you?"
        melonia f_smirk_up "Oh, yes!"
        melonia f_laugh a_clap "I could do with some entertainment."
    show melonia f_smirk_lipbite a_idle
    show anon b_dressed_changing3
    with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_naked_undress_bottom with dissolve
    pause
    melonia f_smirk "That's perfect, right there."
    show anon b_naked a_empty f_worried_low od_naked_dick1
    show anon_arms_naked_a_cover
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    anon "Don't you want me in my uniform for this?"
    melonia "No, I want you just like that."
    show anon f_worried_left
    pause
    anon f_worried_low "What if someone sees me?"
    melonia f_smirk_up "It's just {b}Ricky{/b} and I out here."
    melonia "Besides, what do you have to be shy about?"
    anon @ f_worried_left -m_talk "..."
    anon "Alright, fine."
    anon "Whatever."
    melonia @ f_laugh "Hehe, delightful!"
    melonia f_smirk "You can begin."
    anon "Ehh."
    hide anon_arms_naked_a_cover
    show anon b_naked_spin_frown_down od_empty:
        xoffset 150
    with dissolve
    pause
    show anon b_naked_spin_worried_low_talk with dissolve
    anon "Like this?"
    show anon b_naked_spin_worried_low
    melonia @ -m_talk "Mhmm."
    pause
    show ricky f_smirk_low behind anon with dissolve:
        flip
        xoffset -200
    pause
    melonia "Come to enjoy the show, {b}Ricky{/b}?"
    show anon b_naked_spin_frown_down
    ricky "Si, señora."
    ricky @ f_laugh "That is quite the impressive display, amigo!"
    show anon b_naked_spin_frown_down_talk
    anon "It is?"
    show anon b_naked_spin_frown_down
    pause
    ricky @ f_laugh "Es like a helicopter!"
    melonia "Heh, you're right!"
    pause
    melonia "You think he might fly away?"
    ricky "You ever see the police man twirl a billy club?"
    melonia @ f_laugh "{i}*Snort*{/i} No."
    ricky a_finger_tub "It looks just like this..."
    pause
    ricky a_idle @ a_finger "Es giving me flash backs to El Salvador!"
    melonia "Don't worry, I won't let him hurt you."
    ricky "There are worse ways to go, señora..."
    melonia @ f_laugh "Haha!"
    show anon b_naked od_naked_dick1 a_idle f_frown_down with dissolve
    anon "You know, this is awkward enough without the back and forth from you two..."
    melonia f_smirk_up "Aww, poor {b}Hector{/b}..."
    melonia @ f_laugh "You've embarrassed him, {b}Ricky{/b}!"
    ricky @ a_up f_smirk "Apologies, amigo."
    show anon b_naked_undress_bottom od_empty with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    anon "I think that's enough for today."
    show anon b_dressed_changing with dissolve
    melonia "Boo!!"
    show anon b_dressed f_unimpressed a_sides with dissolve
    melonia @ f_laugh a_clap "Encore, encore!"
    ricky f_smirk "Well, it was good while it lasted."
    ricky @ a_finger "I guess, I'll get back to the garden..."
    melonia f_pouting "Aww, c'mon guys!"
    hide ricky with dissolve
    melonia "Things were just getting good!"
    hide anon with dissolve
    pause
    if M_melonia.outfit.is_naked:
        show melonia b_jacuzzi_topless_edge with dissolve
    else:
        show melonia b_jacuzzi_edge with dissolve
    melonia "Guys?!"
    melonia "Don't leave..."
    pause
    if M_melonia.outfit.is_naked:
        show melonia b_jacuzzi_topless f_annoyed with dissolve
    else:
        show melonia b_jacuzzi f_annoyed with dissolve
    melonia "Grr!"
    return 'dance'


label melonia_button_hottub.suggest:
    anon f_flirt_low "Want to have sex?"
    melonia f_smirk_up "Mmm, you read my mind."
    melonia "Let's head up to my bedroom."

    if M_melonia.outfit.is_naked:
        show melonia b_jacuzzi_climb_naked:
            flip
    else:
        show melonia b_jacuzzi_climb:
            flip

    show location_rump_backyard_jacuzzi_overlay as hottub behind melonia
    with dissolve
    pause
    show layer master:
        ease 1.6 xpos 485
    with None

    if M_melonia.outfit.is_naked:
        show melonia b_naked_pulling_anon f_smirk:
            flip
            offset (-960, 0)
    else:
        show melonia b_swimsuit_hatless_pulling_anon o_pulling_anon_hat f_smirk:
            flip
            offset (-960, 0)

    show anon b_empty f_flirt o_melonia_pulling:
        flip
        xoffset -530
    with dissolve
    anon "Yes, ma'am."

    scene location_rump_bedroom_bed_closeup

    if M_melonia.outfit.is_naked:
        show melonia f_smirk b_naked
        show anon f_flirt_low
    else:
        show melonia f_smirk b_swimsuit_hatless a_hips_no_shall
        show anon f_flirt

    with fade
    melonia "I'm so glad my husband hired you!"

    if not M_melonia.outfit.is_naked:
        show anon f_flirt_low
        show melonia a_remove1 f_smirk_down
        with dissolve
        pause
        show melonia b_swimsuit_remove2 with dissolve
        pause
        show melonia b_swimsuit_remove3 with dissolve
        show melonia b_swimsuit_remove4 with dissolve
        pause
        show melonia b_swimsuit_bottom a_idle with dissolve
        pause
        show melonia b_swimsuit_bottom a_remove_bottom1 with dissolve
        pause
        show melonia b_swimsuit_bottom_remove2 with dissolve
        pause
        show melonia b_naked_sexy f_smirk with dissolve

    pause
    jump melonia_button_bedroom.sex
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
