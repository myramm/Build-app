label scene_svetlana_furnace_cowgirl:
    $ M_svetlana.set('sex speed', 1 / 8.)
    $ renpy.dynamic(variant='first')

    call scene_svetlana_furnace_cowgirl.stage
    with fade
    anon @ -m_talk "!!!"
    anon "Oh, god..."
    anon "... This is really gonna happen, huh?"
    svetlana "Da."
    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana "Mmm, a perfect fit." (show_native="Mmm, ideal'no podkhodit.")
    anon "Oh my god, oh my god, oh my god!"
    call scene_svetlana_furnace_cowgirl.animate
    with {'master': dissolve}
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (1)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (2)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (3)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (4)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (5)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (6)
    pause

    label scene_svetlana_furnace_cowgirl.resume:
    call scene_svetlana_furnace_cowgirl.loop

    if _return == 'switch':
        jump scene_svetlana_furnace_doggy.switch

    svetlana "Finish inside!"
    anon "Really?"
    svetlana "Da!"

    if variant == 'first':
        anon "W-what if you get pregnant?!"
        svetlana "I cannot!"
        anon "You cannot?!"

    svetlana "Cum in me!" (show_native="Konchi v menya!!")

    if variant == 'first':
        anon "How can you be sure-"
    else:
        pause

    svetlana "I'm cumming!"
    svetlana "Oh, I'm cumming!!!"
    anon "Holy shit!"
    svetlana "NGGHHH!!!"
    hide anim
    show svetlana furnace_cowgirl b_cum
    anon "HNNGGG!!!" with flash
    show xray_front_top as xray:
        anchor (.5, .5)
        pos (250 + 358, 250 + 168)
        rotate -110
        rotate_pad False
        xzoom -1
        zoom .68
    with {'master': fastdissolve}
    pause
    hide xray
    show svetlana b_insert o_pullout
    show anon svet_furnace_cowgirl
    with {'master': dissolve}
    svetlana "I feel it!" (show_native="Ya chuvstvuyu eto!")
    show svetlana b_base d_after o_after
    with {'master': dissolve}
    svetlana "What a torrent!" (show_native="Kakoy torrent!")
    anon "Haah... Haah..."
    pause
    anon "... Jesus Christ."
    svetlana "Haah... Haah..."
    anon "That was intense!"
    svetlana "Da."

    if variant == 'repeat':
        return

    svetlana "It has been a very long time since a man made me cum so..."
    anon "Oh?"
    svetlana "... I need a moment."
    anon "Yeah, of course!"
    anon "T-take your time."
    return


label scene_svetlana_furnace_cowgirl.stage:
    scene location_warehouse_furnace_convey_side_any
    show svetlana furnace_cowgirl
    show anon svet_furnace_cowgirl
    return


label scene_svetlana_furnace_cowgirl.insert:
    show svetlana furnace_cowgirl b_insert
    show anon svet_furnace_cowgirl
    return


label scene_svetlana_furnace_cowgirl.animate:
    hide anon
    hide svetlana
    show svetlana_furnace_cowgirl_body_b_anim as anim
    return


label scene_svetlana_furnace_cowgirl.loop:
    call screen scene_svetlana_furnace_cowgirl_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_svetlana_furnace_cowgirl.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_svetlana_furnace_cowgirl.loop


label scene_svetlana_furnace_cowgirl.dialogue(opt, rng=-1):

    if opt == 1:
        anon "Haaaaah!!!"

        if variant == 'first':
            svetlana "Are all Americans this malleable?" (show_native="Vse li Amerikantsy takiye podatlivyye?")
        else:


            svetlana "Do all Americans make such silly noises during sex?" (show_native="Neuzheli vse amerikantsy izdayut takiye glupyye zvuki vo vremya seksa?")


        anon "Hmm?"
        anon "I don't know what you're say-"
        svetlana "Shut up!"
        anon "{i}*Gulp*{/i} Y-yes, ma'am."

    elif opt == 2:
        svetlana "You like this?"
        anon "..."

        if rng < .15:
            svetlana "You like it when I ride your big, fat American cock?"
            anon "D-do you want me to answer, or-"

        svetlana "Say it!!"
        anon "Ahh, yes!"

        if rng < .15:
            anon "Yes, I love it when you ride my big, fat American cock!!"

    elif opt == 3:
        svetlana "{b}Nadya{/b} is a fortunate woman..." (show_native="{b}Nadya{/b} schastlivaya zhenshchina...")
        svetlana "... To have claimed such a man." (show_native="... Zavoyevat' takogo muzhchinu.")

    elif opt == 4:
        anon "Oh, Jesus... You're so sexy!"

        if rng < .4:
            svetlana "You like my pussy?"
            anon "Yes, I love it!!"

    elif opt == 5:
        if rng < .3:
            svetlana "Mmm, you're going to make me cum!" (show_native="Mmm, ty zastavish' menya konchit'!")
            anon "What?"

        svetlana "I cum soon!"
        anon "Ngh, yeah... me too!"

    elif opt == 6:
        svetlana "So fucking good!" (show_native="Tak chertovski khorosho!")
        svetlana "Ahh!"

    return


label scene_svetlana_furnace_cowgirl.switch:
    anon "Haah... Haah..."
    anon "I'm running on fumes here."
    svetlana "Hmm?"
    call scene_svetlana_furnace_doggy.stage
    with {'master': dissolve}
    anon "Can you get back on top for a while?"
    svetlana "Da."
    svetlana "I will ride."
    anon "Thanks."

    call scene_svetlana_furnace_cowgirl.stage
    with fade
    anon "Your body is incredible!"
    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana @ -m_talk "Mmmm."
    anon "Oh my god!"
    call scene_svetlana_furnace_cowgirl.animate
    with {'master': dissolve}
    jump scene_svetlana_furnace_cowgirl.resume


label scene_svetlana_furnace_cowgirl.first:
    jump scene_svetlana_furnace_cowgirl


label scene_svetlana_furnace_cowgirl.repeat:
    $ M_svetlana.set('sex speed', 1 / 8.)
    $ renpy.dynamic(variant='repeat')

    call scene_svetlana_furnace_cowgirl.stage
    with fade
    anon "Oh, god..."
    anon "... Your body is incredible!"
    svetlana "Da."
    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana "Mmm, your penis is the best." (show_native="Mmm, tvoy penis samyy luchshiy.")
    anon "Oh my god, oh my god, oh my god!"
    call scene_svetlana_furnace_cowgirl.animate
    with {'master': dissolve}
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (1)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (2)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (3)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (4)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (5)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (6)
    pause
    jump scene_svetlana_furnace_cowgirl.resume


label scene_svetlana_furnace_cowgirl.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['svetlana']['variants']['02_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_warehouse_furnace) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_svetlana_furnace_cowgirl.first

            "Repeat" if 'repeat' in variants:
                jump scene_svetlana_furnace_cowgirl.repeat

    jump expression 'scene_svetlana_furnace_cowgirl.{}'.format(next(iter(variants)))


screen scene_svetlana_furnace_cowgirl_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_svetlana.set, 'sex speed',
                                 1 / (1 / M_svetlana.get('sex speed') - 2)),
                        Return(False))
                sensitive M_svetlana.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_svetlana.set, 'sex speed',
                                 1 / (1 / M_svetlana.get('sex speed') + 2)),
                        Return(False))
                sensitive M_svetlana.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
