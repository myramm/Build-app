label ano27_peek_warehouse_depot:
    scene expression background(280, 496, 5) as stage
    show nadya a_fingernails b_traditional f_bored_down:
        xoffset 100
        xzoom -1
    show raz f_annoyed_low:
        xoffset -100
        xzoom -1
    show dimitri
    show debbie a_tied f_sad_up:
        offset (-200, 250)
    show jenny a_tied f_concerned_up:
        offset (50, 250)

    if M_jenny.pregnancy.to_string == '_pregnant_belly':
        show jenny a_pregnant_belly_tied b_dressed_pregnant_belly
    elif M_jenny.pregnancy.to_string == '_pregnant_bump':
        show jenny a_pregnant_bump_tied b_dressed_pregnant_bump

    raz "I've had enough of your lies!"
    debbie "B-but we're not lying..."
    raz f_annoyed "{b}Dimitri{/b}, you know what to do."
    dimitri "Da, boss."
    show debbie f_sad_back_up
    show dimitri b_dressed_tied f_grin_low:
        xoffset 300
    show raz f_annoyed_low
    with {'master': dissolve}
    dimitri "Come, pretty girls..."
    show jenny f_gross_high
    dimitri f_grin_back_low "... We will find truth, one way or another."
    show dimitri f_grin_low
    show jenny f_upset_back_low:
        offset (650, 0)
        xzoom -1
    with {'master': dissolve}
    jenny "Hey, watch it you fucking asshole!"
    show debbie f_wincing:
        offset (475, 0)
        xzoom -1
    show dimitri a_sides b_dressed f_angry_right:
        xoffset -150
    show jenny f_concerned_back behind debbie
    show raz f_annoyed
    with {'master': dissolve}
    debbie "Ow, you're hurting me!"
    show debbie f_crying_closed:
        xoffset 525
    show dimitri a_push b_dressed f_angry:
        xoffset 320
        xzoom -1
    show jenny f_angry:
        xoffset 700
    dimitri "Shut up and walk, bitch!" with hpunch
    hide debbie
    hide dimitri
    hide jenny
    with dissolve
    pause
    show raz f_normal with dissolve:
        xoffset 300
    goon "C'mon boss, can't we make sexy times with them first?"
    show raz f_eyeroll
    pause
    show raz f_annoyed with {'master': dissolve}:
        xoffset -200
        xzoom 1
    raz "No."
    show goon f_concerned with {'master': dissolve}:
        xoffset -150
        xzoom -1
    goon "I'm only saying, they are very pretty girls... is wasteful to-"
    raz "They have something I want and there will be no sexy times until it is mine!"
    goon "But {b}Dimitri{/b} will cut them to pieces..."
    raz f_angry "Do I pay you to give opinion?!"
    goon a_thinking f_curious "I uhh-"
    pause
    goon a_idle "N-no?"
    show goon f_concerned
    raz f_annoyed "That's right."
    raz "I pay you to keep mouth shut and do as you're told!"
    raz a_point_back "Now take tiny prick to the workers and stop bothering me, eh?!"
    raz a_idle @ a_finger "But check progress first!"
    goon "Right away, boss."
    hide goon
    show raz:
        xoffset 300
        xzoom -1
    with dissolve
    pause
    raz "And the rest of you idiots must resume packing warehouse!"
    raz "This is no time for games!"
    raz "We go back to motherland in few days and nothing is to be left behind!"
    pause
    raz f_angry "Remember to be careful with weapon crates... I want no more explosive accidents costing me money!"
    raz "Understand?!" (show_native="Ponyat'?!")
    pause
    show nadya f_bored
    show raz f_normal:
        xoffset -200
        xzoom 1
    with {'master': dissolve}
    raz "Come, beloved..." (show_native="Prikhodi, lyubimyye...")
    raz "... We have work to do." (show_native="... U nas yest' rabota.")
    show nadya a_sides f_eyeroll
    show raz:
        xoffset 300
        xzoom -1
    with dissolve
    pause .5
    hide nadya
    hide raz
    with dissolve

    scene
    show screen ano27_peek_warehouse_depot()
    with fade
    anon "( Oh, thank god... I'm not too late! )"
    anon "( The girls are still alive. )"
    anon "..."
    anon "( I'd better get the guys in here quick if I want them to stay that way! )"
    anon "( {b}I should look around for something useful.{/b} )"

    label ano27_peek_warehouse_depot.loop:
        call screen empty()

        if _return:
            call expression 'ano27_peek_warehouse_depot.' + _return
            jump ano27_peek_warehouse_depot.loop

    scene expression background(400,400,2, l=L_warehouse_furnace) as stage
    show anon f_worried with dissolve
    anon @ -m_talk "( There's way too many of them in there, I'll never reach an exit! )"
    anon f_thinking @ -m_talk "( {b}Maybe there's something I can use in here{/b}? )"
    hide anon with dissolve
    return


label ano27_peek_warehouse_depot.cards:
    anon "( Looks like a group of Russians are playing a card game. )"
    anon "..."
    anon "( I wonder which one? )"
    return


label ano27_peek_warehouse_depot.drink:
    anon "( Man, they're all over the place! )"
    anon "..."
    anon "( I can't sneak my way through all of them. )"
    anon "( I need a distraction or something. )"
    return


label ano27_peek_warehouse_depot.forklift:
    anon "( Hmm, that forklift would make a great distraction if there was any way to reach it... )"
    anon "( ... But unfortunately, there isn't. )"
    anon "..."
    anon "( I should keep looking. )"
    return


label ano27_peek_warehouse_depot.lab:
    anon "( Hmm, I wonder where that leads? )"
    anon "( I'll have to get {b}Harold{/b} and {b}Tony{/b} in here first to clear out these goons. )"
    anon "..."
    anon "( There has to be a way. )"
    return


label ano27_peek_warehouse_depot.office:
    anon "( That must be the door to {b}Raz{/b}'s office. )"
    anon "( {b}Nadya{/b} will be there waiting for me. )"
    anon "( But there's no way to reach it now... not with all these guards here. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
