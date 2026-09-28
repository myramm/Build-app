label ano20_oval_rump_office:
    scene expression background(808, 350, 3.5) as stage
    show anon f_surprised with dissolve:
        flip
    anon @ -m_talk "( Whoa... )"
    anon @ -m_talk "( It's like the Oval Office in here! )"
    anon f_thinking a_thinking @ -m_talk "( I wonder if {b}Mayor Rump{/b} has presidential aspirations one day? )"
    pause
    anon a_idle f_grin @ -m_talk "( Yeah, right. )"
    anon @ -m_talk "( Like anyone would vote for a guy like him! )"
    anon f_laugh "( Ridiculous! )"
    hide anon with dissolve
    return


label ano20_open_bobblehead:
    scene expression background(736, 328, 10.) as stage
    show closeup_bobblehead
    with fade
    anon "( {b}2020{/b}, huh? )"
    anon "( It's just some leftover swag from his campaign... )"
    pause
    anon "( Seems kind of out of place here with all this expensive looking stuff. )"
    return


label ano20_open_bookcase:
    show screen rump_office_bookcase(_layer='master')
    anon "( Heh, look at the little {b}Rump{/b} bobblehead! )"
    anon "( It's kinda cute! )"
    call screen empty()
    return


label ano20_open_papers:
    scene expression background(256, 320, 2.75) as stage
    show anon f_worried_low with dissolve:
        flip
    anon @ -m_talk "( Nope, nothing but political documents here... )"
    anon @ -m_talk "( ... I should have known it wouldn't be that easy. )"
    hide anon with dissolve
    return


label ano20_open_safe:
    if M_anon.is_state(S_ano20_find):
        scene expression background(504, 296, 4) as stage
        show anon f_worried_high with dissolve:
            yoffset 300
        anon @ -m_talk "( Hmm? )"
        show anon b_dressed_bending_phone with dissolve:
            offset (50, 220)
        pause
        show anon b_dressed_pickup with dissolve:
            offset (100, 50)
        pause
        show anon b_dressed f_skeptical with dissolve:
            offset (200, 0)
        anon @ -m_talk "( I think there's something behind this picture frame! )"

        scene location_rump_office_cutscene01
        show text _ ("I knew what I was going to find before I even moved the picture frame.") as caption
        with fade
        pause
        hide caption with dissolve
        show text _ ("Of course, {b}Mayor Rump{/b} had a hidden wall safe...") as caption with dissolve
        pause
        hide caption with dissolve
        show text _ ("... That was like rule number one in the evil villain handbook, right?") as caption with dissolve
        pause

    show screen minigame_safe((2, 0, 2, 0), _layer='master') with fade

    if M_anon.is_state(S_ano20_find):
        anon "Well, hello there."
        anon "What are you hiding?"
        anon "( Looks like I need a {b}four digit{/b} combination to open this. )"
        "..."
        anon "( I bet it's a {b}date{/b} that's important to him. )"
        anon "( ... Like his birthday or something. )"
    else:

        anon "( I can do this. I just need to think of a {b}date{/b} that's important to him. )"

    call screen empty()

    if _return.fail == 'abort':
        jump ano20_open_safe.abort

    if _return.fail:
        $ renpy.dynamic(combo=' - '.join(str(i) for i in _return.input))
        jump ano20_open_safe.fail

    anon "Bingo!{w=1.}{nw}"

    scene safe_background
    show safe_door_open at left
    with fade
    anon "!!!"

    $ renpy.dynamic(seen=set())

    label ano20_open_safe.loop:
        call screen rump_office_safe(seen)

        if _return:
            call expression 'ano20_open_safe.' + _return
            jump ano20_open_safe.loop

    $ renpy.dynamic(unknown=Character('???', kind=character.raz))

    scene expression background(504, 344, 3.5) as stage
    show anon a_recorder f_looking_down:
        xoffset 200
    with fade
    anon @ -m_talk "( I wonder what's on this recording? )"
    show anon a_recorder_listen f_thinking with dissolve
    rump "So the shipment was intact then?"
    unknown "Da."
    unknown "With the exception of a few girls who didn't survive the boat ride."
    rump "What happened there?"
    unknown "Overdose, I think."
    unknown "Or bad reaction to sedative?"
    unknown "Who can say?"
    unknown "We toss them overboard, is not problem."
    rump "Yeah, I suppose there's plenty more where they came from, eh?"
    rump "Hahahaah!"
    pause
    rump "See, I uhh... I told ya there wouldn't be any more problems on my end."
    unknown "Hmph, your accountant steals my money."
    show anon f_worried
    unknown "This is big problem for you."
    rump "{b}Raz{/b}, c'mon... He wasn't \"my\" accountant... You know that."

    $ renpy.dynamic(unknown=Character('"Raz"', kind=character.raz))

    unknown "You hire him."
    rump "Well, yes... I hired him."
    rump "But he was an independent contractor that got recommended to me."
    rump "It's not like I personally knew the guy."
    pause
    rump "There was no way I could have forseen him doing something stupid like that!"
    rump "You know, I'd be happy to have my security go out and look for him."
    rump "I'm sure-"
    unknown "Do not concern yourself."
    unknown "{b}Mr. Cummings{/b} is not long for this world..."
    anon f_surprised_teeth @ f_shock "!!!" with hpunch
    unknown "{b}Dimitri{/b} will find him."
    rump "Right, yeah... Okay."
    rump "I'll just, uhh... Focus on getting that warehouse for ya."
    anon "( This proves that they killed him... )"
    anon f_hurt "( ... And {b}Mayor Rump{/b} knew about it! )"
    anon f_angry @ -m_talk "( That son of a bitch! )"
    anon a_recorder @ -m_talk "( Surely this is enough to take them all down. )"
    anon @ -m_talk "( I need to get this evidence to {b}Harold{/b} right away! )"
    hide anon with dissolve
    return True


label ano20_open_safe.abort:
    anon "( It's no good, there are too many possible combinations. )"
    anon "( He must have used something memorable, maybe there's a clue around here... )"
    return


label ano20_open_safe.cash:
    anon "( Look at all this cash! )"
    anon "( There must be like five thousand dollars here! )"
    return


label ano20_open_safe.cassette:
    anon "( \"Russian Pee Girl?\" )"
    anon "( Eww!! )"
    anon "( Just- )"
    "..."
    anon "( Eww. )"
    return


label ano20_open_safe.fail:
    anon "( No, that's not it. )"
    anon "( Whatever the combination is, it's not {k=-1}[combo]{/k}. )"

    scene expression background(504, 344, 3.5) as stage
    show anon f_thinking:
        xoffset 200
    with fade
    anon @ -m_talk "( There has to be a clue in his office somewhere. )"
    anon @ -m_talk "( I should look around more. )"
    hide anon with dissolve
    return


label ano20_open_safe.folder:
    anon "( \"Offshore accounts?\" )"
    "..."
    anon "( This must be all the documentation for business dealings with the Russian mob. )"
    return


label ano20_open_safe.hint:
    anon "( I'm not done looking through all this stuff yet! )"
    return


label ano20_open_safe.passport:
    anon "( This is a Russian passport. )"
    anon "( It doesn't exactly link him to the Russians but it's suspicious that he has this and is hiding it away. )"
    return


label ano20_open_safe.recorder:
    anon "Hmm."
    anon "( This looks like some kind of recording device. )"
    anon "( I wonder what's on it? )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
