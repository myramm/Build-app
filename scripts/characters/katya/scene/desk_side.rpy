label scene_katya_sex_desk_side:
    $ M_katya.set('sex speed', 1 / 8.)
    $ renpy.dynamic(variant='first')

    call scene_katya_sex_desk_side.stage
    with fade
    anon "Man, you really do have a great ass!"
    katya "Da?"
    anon "Mhmm!"
    katya "Thank you." (show_native="Spasibo.")
    katya "Ehm, you can put it in now..."
    anon "Yeah, okay."
    call scene_katya_sex_desk_side.insert
    with {'master': dissolve}
    katya "!!!"
    call scene_katya_sex_desk_side.animate
    with {'master': dissolve}
    call scene_katya_sex_desk_side.dialogue (1)
    pause
    katya "My mistress was right, you're very large!"
    anon "I know."
    pause
    anon "It's not hurting you, is it?"
    katya "A little bit."
    anon "You want me to stop?"
    katya "N-no, don't stop."
    pause
    anon "You sure?"
    katya "Da."
    katya "I just need a minute."
    pause
    katya "It's so thick!" (show_native="Nastol'ko gustoy!")
    katya "It's like I'm a virgin again!" (show_native="Kak budto ya snova devstvennik!")
    pause
    katya "Oh, wow!" (show_native="Oy!")
    katya "Fuck me!" (show_native="Trakhni menya!")
    anon "Feeling good now?"
    katya "Da!"
    katya "Very good!"
    pause
    call scene_katya_sex_desk_side.dialogue (2)
    pause
    call scene_katya_sex_desk_side.dialogue (3)
    pause
    call scene_katya_sex_desk_side.dialogue (4)
    pause
    call scene_katya_sex_desk_side.dialogue (5)
    pause
    call scene_katya_sex_desk_side.dialogue (6)
    pause
    call scene_katya_sex_desk_side.dialogue (7)
    pause
    call scene_katya_sex_desk_side.dialogue (8)
    pause
    label scene_katya_sex_desk_side.resume:
    call scene_katya_sex_desk_side.loop

    if _return == 'switch':
        jump scene_katya_sex_desk_top.switch

    hide anim

    if _return == 'inside':
        show katya sex_desk_side b_cum
    else:
        show katya sex_desk_side a_pre b_base f_orgasm m_talk o_cumshot

    anon "HNNGGG!!!" with flash

    if _return == 'inside':
        show xray_side as xray:
            anchor (.5, .5)
            pos (250 + 59, 250 + 176)
            rotate 35
            rotate_pad False
            xzoom -1
            zoom .7
        with {'master': fastdissolve}
    else:
        show katya o_cumshot3

    katya "NGGHHH!!!"
    pause
    hide xray

    if _return == 'inside':
        show katya a_insert b_base
    else:
        show katya f_normal_back -m_talk

    with {'master': dissolve}
    anon "Haah... Haah..."

    if _return == 'inside':
        katya "Incredible." (show_native="Neveroyatnyy.")
    else:
        katya "So much..." (show_native="Tak mnogo...")

    pause
    return


label scene_katya_sex_desk_side.stage:
    scene location_warehouse_office_desk_side_day
    show katya sex_desk_side
    return


label scene_katya_sex_desk_side.insert:
    show katya sex_desk_side a_insert
    return


label scene_katya_sex_desk_side.animate:
    hide katya
    show katya_sex_desk_side_body_b_anim as anim
    return


label scene_katya_sex_desk_side.loop:
    call screen scene_katya_sex_desk_side_controls

    if _return:
        return _return

    python hide:
        blocks = 8
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_katya_sex_desk_side.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_katya_sex_desk_side.loop


label scene_katya_sex_desk_side.dialogue(opt, rng=-1):
    if opt == 1:
        katya "Oh, my!"

    elif opt == 2:
        katya "Ah, you're stretching me so much!"

    elif opt == 3:
        katya "Faster!" (show_native="Bystreye!")

        if rng < .3:
            anon "I have no idea what you're saying but it sounds like you're enjoying yourself so I'm just gonna assume this is going well..."

        katya "Yes!!"

        if rng < .3:
            anon "... Cool."

    elif opt == 4:
        katya "I can see why {b}Nadya{/b} likes you so much..."

    elif opt == 5:
        katya "Fuck me harder!" (show_native="Yebi menya zhostche!")

        if rng < .2:
            anon "Hmm?"
            katya "Harder!!" with hpunch
            $ M_katya.set('sex speed', 1 / (
                20. if rng < 0 else (1 / M_katya.get('sex speed') + 4)))

        anon "Yes, ma'am."

    elif opt == 6:
        anon "God, you Russian girls sound sexy when you're moaning!"
        katya "Ahh!!"
        anon "Fuck yes!"

    elif opt == 7:
        anon "C'mon, talk dirty to me."
        katya "Oh, {b}[firstname]{/b}!"
        katya "You're amazing!" (show_native="Ty udivitel'nyy!")

    elif opt == 8:
        katya "You're making me crazy!" (show_native="Ty svodish' menya s uma!")
        anon "Oh, I'm getting close."

    return


label scene_katya_sex_desk_side.switch:
    call scene_katya_sex_desk_top.stage
    with {'master': dissolve}
    anon "Hey, you think you could turn over on your stomach?"
    katya "My stomach?"
    anon "Yeah."
    anon "I wanna watch that gorgeous ass bounce."
    katya "Heh, of course."

    $ M_katya.set('sex speed', 1 / 8.)

    call scene_katya_sex_desk_side.stage
    with fade
    anon "Man, look at this thing!"
    katya "Heh, stop it!"
    katya "You make me blush."
    pause
    call scene_katya_sex_desk_side.insert
    with {'master': dissolve}
    katya "!!!"
    call scene_katya_sex_desk_side.animate
    with {'master': dissolve}
    jump scene_katya_sex_desk_side.resume


label scene_katya_sex_desk_side.repeat:
    $ M_katya.set('sex speed', 1 / 8.)
    $ renpy.dynamic(variant='repeat')

    call scene_katya_sex_desk_side.stage
    with fade
    anon "Ahh, there's that beautiful ass again!"
    katya @ f_laugh "Hehe!"
    call scene_katya_sex_desk_side.insert
    with {'master': dissolve}
    katya "!!!"
    call scene_katya_sex_desk_side.animate
    with {'master': dissolve}
    pause
    call scene_katya_sex_desk_side.dialogue (1)
    pause
    call scene_katya_sex_desk_side.dialogue (2)
    pause
    call scene_katya_sex_desk_side.dialogue (3)
    pause
    call scene_katya_sex_desk_side.dialogue (4)
    pause
    call scene_katya_sex_desk_side.dialogue (5)
    pause
    call scene_katya_sex_desk_side.dialogue (6)
    pause
    call scene_katya_sex_desk_side.dialogue (7)
    pause
    call scene_katya_sex_desk_side.dialogue (8)
    pause
    jump scene_katya_sex_desk_side.resume


label scene_katya_sex_desk_side.first:
    jump scene_katya_sex_desk_side


label scene_katya_sex_desk_side.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['katya']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_warehouse_office) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_katya_sex_desk_side.first

            "Repeat" if 'repeat' in variants:
                jump scene_katya_sex_desk_side.repeat

    jump expression 'scene_katya_sex_desk_side.{}'.format(next(iter(variants)))

    return


screen scene_katya_sex_desk_side_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if variant == 'repeat':
                textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_katya.set, 'sex speed',
                                 1 / (1 / M_katya.get('sex speed') - 2)),
                        Return(False))
                sensitive M_katya.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_katya.set, 'sex speed',
                                 1 / (1 / M_katya.get('sex speed') + 2)),
                        Return(False))
                sensitive M_katya.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
