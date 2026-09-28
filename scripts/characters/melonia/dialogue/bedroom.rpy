label melonia_button_bedroom:
    return

label melonia_button_bedroom.intro0:
    show melonia f_confused
    show anon f_worried with dissolve
    melonia "{b}Hector{/b}?!"
    melonia "What are you doing in my bedroom?"
    pause
    melonia f_surprised "{i}*Gasp*{/i} Did you break in here to have your way with me?!"
    anon f_surprised "!!!"
    melonia f_smirk "Are you going to pin me down?"
    melonia "Rip off all my clothes?!"
    show anon f_surprised_teeth
    melonia "Ravage me?!!"
    anon "N-no, ma'am!"
    melonia f_surprised a_dramatic "Oh dear, I'm completely defenseless!"
    melonia "Whatever will I-"
    anon "I swear, I just want to talk!"
    show melonia f_confused
    pause
    melonia a_idle "Y-you just want to talk?"
    anon f_worried "Yes!"
    show melonia f_pouting
    pause
    melonia f_annoyed "Ugh, fine."
    melonia "Make it quick!"
    return


label melonia_button_bedroom.intro1:
    show melonia f_smirk
    show anon f_worried with dissolve
    melonia "Oh my, {b}Hector{/b}..."
    melonia @ a_dramatic "Are you here to ravage me again?"
    show anon f_unimpressed
    pause
    anon "I thought we were finished with all that \"Hector\" nonsense?"
    melonia @ f_laugh "Heh, fuck me like last time and I'll call you whatever you want."
    return


label melonia_button_bedroom.intro2:
    show melonia b_naked f_smirk
    show anon f_worried_low with dissolve
    melonia "Hey there, {b}[firstname]{/b}."
    show melonia b_naked_sexy with dissolve
    melonia "See something you like?"
    return


label melonia_button_bedroom.outro0:
    anon "I should probably get to work."
    melonia f_normal @ a_point "Don't forget to put your uniform on."
    anon "Yes, ma'am."
    hide anon with dissolve
    return


label melonia_button_bedroom.outro1:
    jump melonia_button_common.outro1


label melonia_button_bedroom.outro2:
    anon f_normal "I should go."
    melonia f_pouting "What, already?"
    anon "Yeah, I'm afraid so."
    show melonia b_naked a_idle f_annoyed with dissolve
    melonia "But you haven't even fucked me yet!"
    anon f_surprised_teeth @ f_worried a_wave "Sorry, maybe later."
    hide anon with dissolve
    melonia "{b}[firstname]{/b}!!"
    melonia "Don't leave!"
    pause
    hide melonia with dissolve
    melonia "Get back here and fuck me this instant!"
    return 'escape'


label melonia_button_bedroom.dirty:
    if _return == 'cumshot':
        show melonia o_cumshot

    with fade
    melonia "Mmm, that was incredible!"
    show anon a_sides b_dressed f_unimpressed_low
    with {'master': dissolve}
    melonia "Thank you, {b}[firstname]{/b}."
    anon "Uh huh."
    melonia "Your money is on the night stand."
    anon "Yeah, great."
    hide anon
    with {'master': dissolve}
    melonia "Fetch me a towel, would you?"
    anon "Fetch it yourself."
    show melonia b_onbed_naked_belly_turn f_surprised
    with {'master': dissolve}
    melonia "Excuse me?!"
    anon "You heard me!"
    melonia f_smirk_lipbite @ -m_talk "Mmm!"
    pause
    show melonia b_onbed_naked_back f_normal
    with {'master': dissolve}
    melonia "Fuck it."
    return 'afterglow'


label melonia_button_bedroom.guards:
    anon f_worried "Can you help with the guards?"
    melonia f_normal "Would you like me to send the guards away tonight?"
    anon f_worried "No, I still don't have the code to get through the door."
    melonia "Well, I can't help you there."
    melonia "It's my husband's code, I don't know it."
    anon "Does anyone else know it?"
    melonia "Our daughter assists him with his work sometimes..."
    melonia "... He might have told her the code."
    anon "{b}Iwanka{/b}?"
    melonia @ -m_talk "Mhmm."
    anon f_normal "Interesting."
    anon f_thinking @ -m_talk "( {b}Iwanka{/b} would probably give me the code if I helped her out. )"
    anon @ -m_talk "( I should speak with her. )"
    jump melonia_button_common.choice


label melonia_button_bedroom.sex:
    melonia "Well?"
    anon f_flirt @ -m_talk "Hmm?"
    melonia f_annoyed b_naked a_idle "Are you gonna undress?"
    anon "Oh, right."
    show melonia f_smirk_low
    show anon b_dressed_changing3 with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    pause
    show anon b_naked_undress_bottom with dissolve
    pause
    show anon b_naked f_flirt_low a_sides od_naked_dick1 with dissolve
    melonia f_smirk "Very nice!"
    hide anon
    show melonia b_naked_kiss
    with dissolve
    melonia "I want that big cock inside me right this instant!"

    if venue == 'bedroom':
        scene location_rump_bedroom_bed_closeup as stage

    show anon b_onbed_naked_falling od_empty behind melonia:
        flip
        xoffset -200
    show melonia b_naked_push

    if venue == 'bedroom':
        with fastfade
    else:
        with fastdissolve

    anon "W-whoa!"
    show anon b_onbed_naked f_surprised -od_empty with {'master': dissolve}:
        flip
        offset (-240, -20)
    melonia @ f_laugh "Hehe!"
    show melonia b_naked_back_climb with dissolve:
        flip
        xoffset -200
    melonia "Mmm, give it to me {b}[firstname]{/b}!"

    call scene_melonia_sex.repeat
    $ unlock_scene('melonia', '01_unlocked', variant='repeat')

    scene location_rump_bedroom_bed_closeup as stage
    show melonia b_onbed_naked_back
    show anon b_dressed_changing:
        xoffset -50

    if _return == 'blowjob':
        jump melonia_button_bedroom.shock

    if _return in ('creampie', 'cumshot'):
        jump melonia_button_bedroom.dirty

    with fade
    pause
    show anon a_sides b_dressed f_shy_low
    with {'master': dissolve}
    anon "Did you need anything else, ma'am?"
    melonia @ -m_talk "Hmm?"
    melonia "Oh, no... Thank you, but... I just want to lie here awhile."
    anon "Alright."
    melonia "You were wonderful as always, {b}[firstname]{/b}."
    melonia "There's money on the nightstand for you."
    anon @ f_laugh a_cheering "Awesome, thanks!"
    hide anon with dissolve
    melonia @ -m_talk "Mhmm."
    return 'afterglow'


label melonia_button_bedroom.shock:
    if _return == 'blowjob':
        show melonia o_cumface

    with fade
    pause
    show anon a_sides b_dressed f_happy_low
    with {'master': dissolve}
    anon "Now that was fun!"
    melonia "{i}*Groan*{/i}"
    anon f_worried_low "Uhh, you good?"
    melonia "Mlem..."
    melonia @ -m_talk "{i}*Gulp*{/i}"
    anon "{b}Melonia{/b}?"
    melonia @ -m_talk "Mhmm?"
    anon "You good?"
    melonia "I found that to be surprisingly enjoyable."
    anon f_flirt_low "Heh, you and me both."
    anon "Money on the nightstand?"
    melonia @ -m_talk "Mhmm."
    show anon a_wave
    with {'master': dissolve}
    anon "See you later."
    hide anon
    with {'master': dissolve}
    melonia @ -m_talk "..."
    return 'afterglow'


label melonia_button_bedroom.suggest:
    anon f_flirt "Want to have sex?"
    melonia f_smirk "Mmm, you read my mind."

    if not M_melonia.outfit.is_naked:
        show anon f_flirt_low
        show melonia a_undress1 f_smirk_down
        with dissolve
        pause
        show melonia b_dressed_undress2 with dissolve
        pause
        show melonia b_dressed_undress3 with dissolve
        pause
        show melonia b_undies a_undress4 with dissolve
        pause
        show melonia b_dressed_undress5 with dissolve
        pause
        show melonia b_dressed_undress6 with dissolve
        show melonia b_dressed_undress7 with dissolve
        pause
        show melonia b_naked a_pull_panties f_smirk with dissolve
        pause
        show melonia b_swimsuit_bottom_remove2 with dissolve
        pause
        show melonia b_naked_sexy f_smirk with dissolve

    pause
    jump melonia_button_bedroom.sex
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
