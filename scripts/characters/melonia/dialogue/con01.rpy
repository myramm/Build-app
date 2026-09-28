label con01_init_melonia:
    anon f_worried "Could I talk to you about {b}Consuela{/b}?"
    melonia f_confused "Who?"
    anon "You know, the maid?"
    melonia @ -m_talk "..."
    anon "The woman who cleans your house."
    melonia "Oh, you mean that chubby bitch with the teeth gap?"
    anon "{i}*Sigh*{/i} I guess?"
    melonia "My husband didn't get her pregnant, did he?"
    anon f_surprised "WHAT?!"
    melonia f_annoyed "Because I'll have her ass on a boat back home before she can blink!"
    anon "NO!!"
    anon "No, no, no!"
    show anon f_worried
    melonia "You're sure?"
    anon "Pretty sure."
    melonia f_normal @ f_eyeroll a_heart "Okay, phew..."
    melonia "Don't scare me like that, {b}Hector{/b}!"
    anon "S-sorry."
    pause
    anon "Can I ask why you hired her in the first place?"
    melonia f_annoyed "I didn't."
    melonia "My stupid husband hired her and not for her cleaning abilities, I can tell you that!"
    anon "Why don't you just replace her with someone else?"
    melonia f_normal @ f_eyeroll "Like it's that simple..."
    melonia "Find me someone who will do housework for less than minimum wage and put up with my husband constantly harassing them."
    anon "If I do, will you let me take {b}Consuela{/b} out of here?"
    melonia f_confused "You want to take her?"
    anon "Yes."
    pause
    melonia "For what?!"
    pause
    melonia f_smirk @ f_eyeroll "You know what, never mind."
    melonia "I don't care, take her."
    pause
    melonia @ f_confused "Though why you want that ugly bitch is beyond me..."
    melonia "She can't even speak English!"
    anon f_normal "I'll {b}bring you a replacement{/b}, don't worry."
    melonia @ f_eyeroll "Uh huh."
    hide anon with {'master': dissolve}
    melonia @ f_laugh "Bring me a leprechaun too, while you're at it!"

    $ player.go_to(L_rump_lobby)
    scene expression player.location.background_blur with None
    show anon f_thinking with dissolve
    anon @ -m_talk "( Hmm, so I need {b}to find someone{/b} who will clean this house for less than minimum wage and won't be bothered by the mayor constantly harassing them... )"
    pause
    anon f_sad_down @ -m_talk "( I'm never going to find someone like that! )"
    anon @ -m_talk "( This was such a crappy plan. )"
    pause
    anon f_worried @ -m_talk "( Maybe {b}I should speak with Ricky{/b} and see if he knows anyone that might be willing? )"
    hide anon with dissolve

    $ M_consuela.trigger(T_con01_init)
    return


label con01_plan_melonia:
    melonia "Did you find a replacement for that disgusting maid yet?"

    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "No, not yet."
    melonia f_laugh "Good luck finding someone who will do housework for less than minimum wage and put up with my husband constantly harassing them."

    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal

    anon "I'll {b}find a replacement{/b}."
    anon @ a_point "Just remember, you promised to let me take {b}Consuela{/b} out of here when I do."
    melonia @ f_eyeroll "Uh huh."
    jump melonia_button_common.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
