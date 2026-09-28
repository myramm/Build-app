label melonia_button_common(venue, level):
    call expression 'melonia_button_{}.intro{}'.format(venue, level)

    label melonia_button_common.choice:
    if level == 0:
        menu:
            "Please, stop calling me Hector...":
                jump melonia_button_common.hector
            "What's it like being the mayor's wife?":

                jump melonia_button_common.wife

            "Consuela." if venue == 'bedroom' and M_consuela.is_state(S_con01_init):
                jump con01_init_melonia

            "Replacement for Consuela." if M_consuela.between_states(S_con01_plan, S_con01_give) and not M_consuela.finished_state(S_con01_skip):
                jump con01_plan_melonia
            "Never mind.":

                pass

    elif level == 1:
        menu:
            "Whatever I'd like?":
                jump melonia_button_common.names

            "Fine, I'll dance." if venue == 'hottub':
                jump melonia_button_hottub.dance
            "What's it like being the mayor's wife?":

                jump melonia_button_common.wife

            "Consuela." if venue == 'bedroom' and M_consuela.is_state(S_con01_init):
                jump con01_init_melonia

            "Replacement for Consuela." if M_consuela.between_states(S_con01_plan, S_con01_give) and not M_consuela.finished_state(S_con01_skip):
                jump con01_plan_melonia

            "Help with the guards." if game.timer.is_evening() and M_anon.is_state(S_ano19_code):
                jump melonia_button_bedroom.guards

            "Help with the guards." if game.timer.is_evening() and M_anon.is_state(S_ano20_init):
                jump ano20_init_melonia_guards
            "Sex.":

                jump expression 'melonia_button_{}.suggest'.format(venue)
            "Maybe later.":

                pass
    else:

        menu:
            "You're naked!":
                jump melonia_button_common.naked
            "About your husband...":

                jump melonia_button_common.husband

            "Should I dance for you?" if venue == 'hottub':
                jump melonia_button_hottub.dance
            "Sex.":

                jump expression 'melonia_button_{}.suggest'.format(venue)
            "I should go.":

                pass

    call expression 'melonia_button_{}.outro{}'.format(venue, level)
    return _return


label melonia_button_common.hector:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "My name is {b}[firstname]{/b}."

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Oh, stop playing around, {b}Hector{/b}."
    melonia "I'm not in the mood for games."
    anon "I'm serious!"

    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    melonia "So am I."
    pause
    anon @ f_sad_down "{i}*Sigh*{/i}"
    jump melonia_button_common.choice


label melonia_button_common.husband:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "About your husband..."

    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal b_naked a_idle with dissolve

    anon "I guess you're pretty happy now that your husband is gone, huh?"
    melonia "Oh, it's like a weight has been lifted, {b}[firstname]{/b}!"
    melonia f_disgusted "An a big, fat, wrinkly, orange weight..."

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "In fact, I'm thinking about taking a vacation or something!"

    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon "Oh?"
    melonia "Have you ever been to The Bahamas, {b}[firstname]{/b}?"
    anon "Can't say that I have, no."
    melonia "I make one phone call and we can be on the beach, sipping Mai Tais within hours."
    melonia "What do you say?"

    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Ehh, I dunno..."
    anon "... This isn't really a good time for me."

    if venue == 'hottub':
        show melonia f_confused_up
    else:
        show melonia f_confused

    melonia @ -m_talk "Hmm?"
    anon "Maybe another time?"

    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    melonia "Seriously?"
    anon "Sorry."
    melonia "Alright, fine."
    pause

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "I guess, we'll just have to entertain ourselves here, hmm?"

    if venue != 'hottub':
        show melonia b_naked_sexy with dissolve
    jump melonia_button_common.choice


label melonia_button_common.names:
    anon f_skeptical "Whatever I'd like?"

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia @ -m_talk "Mhmm."

    melonia "Anything!"
    anon f_thinking @ -m_talk "Hmm."
    anon f_skeptical "Sir?"

    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    pause
    melonia @ f_eyeroll "I was hoping for something a little more imaginative."

    if venue == 'hottub':
        show anon f_shy_low
    else:
        show anon f_shy

    anon "Master?"

    if venue == 'hottub':
        show melonia f_confused_up
    else:
        show melonia f_confused

    melonia "Really?"

    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "No?"

    anon f_thinking a_thinking "Okay..."
    pause

    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon a_idle "How about, \"{b}King [firstname]{/b}?\""

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Oh, now you're getting my engine going!"
    melonia "Shall I attend to your royal scepter, {b}King [firstname]{/b}?"
    pause
    anon f_grin @ f_surprised "Wait, I got it!"
    pause
    anon f_brag_closed a_point_self "Call me..."
    anon "\"Mr. President!\""
    show anon f_grin a_idle with dissolve

    if venue == 'hottub':
        show melonia f_surprised_up
    else:
        show melonia f_surprised

    pause
    melonia f_disgusted_down "Eww!"

    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "No?"
    melonia "My lady wood just went from midnight to six."
    anon "Huh?!"
    melonia "That was just wrong!"
    anon f_sad_down "Aww, man."
    jump melonia_button_common.choice


label melonia_button_common.naked:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Why are you naked?"

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia b_naked a_idle f_smirk with dissolve

    melonia "Why not?"
    show anon f_flirt_low
    melonia "It's my house now and I'll do what I like."
    pause
    melonia "I think the better question is..."
    melonia "... Why are you still wearing clothes?"
    jump melonia_button_common.choice


label melonia_button_common.wife:
    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon @ f_skeptical "What's it like being the mayor's wife?"

    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal

    melonia "Ugh, it's a neverending assault of soul-crushing boredom."
    anon "R-really?"
    melonia "Most of my time is spent playing the role of eye candy and letting geriatric fucks ogle me in exchange for campaign funding..."
    anon "So, it sucks?"
    melonia @ f_eyeroll "Well, not all of it..."
    melonia "I have servants waiting on me twenty-four hours a day and constantly kissing my ass."
    anon @ -m_talk "..."

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "It's quite fun ordering them around."
    pause
    melonia "What do you say, {b}Hector{/b}?"
    melonia "Would you like me to... Order you around?"

    if venue == 'hottub':
        show anon f_surprised_low
    else:
        show anon f_surprised

    anon "{i}*Gulp*{/i} Y-yeah, maybe..."
    melonia @ f_laugh "Hahaha!"
    jump melonia_button_common.choice


label melonia_button_common.outro0:
    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon "I should probably get to work."

    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal

    melonia "Don't forget to put your uniform on."
    anon "Yes, ma'am."
    hide anon with dissolve
    return


label melonia_button_common.outro1:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Maybe later."

    if venue == 'hottub':
        melonia f_pouting_up "Just a quick dance..?"
    else:
        melonia f_pouting "But I want it now..."

    anon a_behind_head "Sorry."

    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    melonia "You're not seriously saying no, are you?"
    anon "I've got stuff to do."
    pause

    if venue == 'hottub':
        show melonia f_yell
    else:
        show melonia f_yell a_fists with dissolve

    melonia "Ugh, fine!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
