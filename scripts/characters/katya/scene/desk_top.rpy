label scene_katya_sex_desk_top:

    return


label scene_katya_sex_desk_top.stage:
    scene location_warehouse_office_desk_top_day
    show katya sex_desk_top
    return


label scene_katya_sex_desk_top.insert:
    show katya sex_desk_top b_anim06
    return


label scene_katya_sex_desk_top.animate:
    hide katya
    show katya_sex_desk_top_body_b_anim as anim
    return


label scene_katya_sex_desk_top.loop:
    call screen scene_katya_sex_desk_top_controls

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

    jump scene_katya_sex_desk_top.loop


label scene_katya_sex_desk_top.switch:
    hide anim
    call scene_katya_sex_desk_side.insert
    with {'master': dissolve}
    anon "Hei, kamu pikir kamu bisa membalikkan badan?"

    katya "Punggungku?"

    anon "Ya."

    anon "Aku ingin melihat wajah cantikmu itu."

    katya "Tentu saja."


    $ M_katya.set('sex speed', 1 / 8.)

    call scene_katya_sex_desk_top.stage
    with fade
    anon "Sobat, kamu cantik."

    katya "Heh, hentikan!"

    katya "Kamu membuatku tersipu."

    call scene_katya_sex_desk_top.insert
    with {'master': dissolve}
    katya "!!!"
    call scene_katya_sex_desk_top.animate
    with {'master': dissolve}

    call scene_katya_sex_desk_top.loop
    jump scene_katya_sex_desk_side.switch


screen scene_katya_sex_desk_top_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Switch') action Return()

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
