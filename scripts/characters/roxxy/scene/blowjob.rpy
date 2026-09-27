label scene_roxxy_blowjob:

    return


label scene_roxxy_blowjob.stage:
    scene location_trailer_bedroom_sex_bj
    show roxxy_sex_bj_pre as animation
    return


label scene_roxxy_blowjob.insert:
    show roxxy_sex_bj_anim01 as animation
    return


label scene_roxxy_blowjob.animate:
    show roxxy_blowjob as animation
    return


label scene_roxxy_blowjob.loop:
    call screen scene_roxxy_blowjob_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_roxxy_blowjob.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_roxxy_blowjob.loop


label scene_roxxy_blowjob.dialogue(opt, rng=-1):

    if opt == 1:
        anon "Oh, {b}Roxxy{/b}!"

        roxxy "{i}*Sluuuuurp*{/i}"

        anon "Ya, begitu saja!"


    elif opt == 2:
        anon "{i}*Phew*{/i} that's it."

        anon "Who's my dirty little bitch, huh?"

        roxxy "Ahh arm!"


        if rng < .33:
            roxxy "{i}*Smack*{/i}"

            anon "Yeah, you are."


    elif opt == 3:
        anon "Gobble that cock, {b}Roxxy{/b}."

        roxxy "Mmm, furg ahds aahwt."


        if rng < .33:
            anon "Less talking, more sucking!"

            roxxy "Ohm, nom!"


    elif opt == 4:
        anon "Yeah, use that tongue!"

        roxxy "{i}*Mlehh*{/i}"

        anon "Ahhh!"


    elif opt == 5:
        roxxy "{i}*Sluuuuurp*{/i}"

        anon "Man, you look great with that dick in your mouth..."

        roxxy "Ahh eww?"


        if rng < .33:
            anon "Oh ya!"

            roxxy "Hehehe!"


    return


label scene_roxxy_blowjob.repeat:
    $ M_roxxy.set('sex speed', 1 / 8.)

    call scene_roxxy_blowjob.stage
    with fade
    anon "I bet you never thought you'd be doing this with me, huh?"

    call scene_roxxy_blowjob.insert
    with {'master': dissolve}
    anon "Ah, wow!"

    roxxy "MM."

    call scene_roxxy_blowjob.animate
    with {'master': dissolve}
    pause
    call scene_roxxy_blowjob.dialogue (1)
    pause
    call scene_roxxy_blowjob.dialogue (2)
    pause
    call scene_roxxy_blowjob.dialogue (3)
    pause
    call scene_roxxy_blowjob.dialogue (4)
    pause
    call scene_roxxy_blowjob.dialogue (5)
    pause

    call scene_roxxy_blowjob.loop

    anon "I'm getting close, {b}Roxxy{/b}!"

    roxxy "{i}*Sluuuuurp*{/i}"

    roxxy "Ohm, nom!"

    anon "Ah, geez!"

    pause
    anon "aku akan-"

    anon "I'M GONNA-"

    pause
    show roxxy_sex_bj_cum as animation
    show roxxy_sex_bj_cum_drip as cum
    anon "HNNGGG!!!" with flash
    pause
    hide cum
    show roxxy_sex_bj_swallow as animation
    with {'master': dissolve}
    anon "Haah... Haah..."

    roxxy "{i}*Meneguk*{/i}"

    show roxxy_sex_bj_after as animation
    show roxxy sex_bj_after f_tired
    with {'master': dissolve}
    roxxy "{i}*Mlehh*{/i}"

    show roxxy f_happy
    anon "Ah, you beautiful bitch..."

    roxxy "hehe!"

    anon "... You're the best girlfriend ever, {b}Roxxy{/b}!"

    roxxy "Hehe, aku tahu."

    return


label scene_roxxy_blowjob.replay:
    jump scene_roxxy_blowjob.repeat


screen scene_roxxy_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_roxxy.set, 'sex speed',
                                 1 / (1 / M_roxxy.get('sex speed') - 2)),
                        Return(False))
                sensitive M_roxxy.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_roxxy.set, 'sex speed',
                                 1 / (1 / M_roxxy.get('sex speed') + 2)),
                        Return(False))
                sensitive M_roxxy.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
