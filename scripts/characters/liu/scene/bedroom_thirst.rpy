label scene_liu_bedroom_thirst:

    return


label scene_liu_bedroom_thirst.insert:
    show liu_bedroom_thirst 1 as anim
    return


label scene_liu_bedroom_thirst.animate:
    show liu_bedroom_thirst as anim
    return


label scene_liu_bedroom_thirst.loop:
    call screen scene_liu_bedroom_thirst_controls

    if _return:
        return _return

    python hide:
        blocks = 4
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_liu_bedroom_thirst.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_liu_bedroom_thirst.loop


label scene_liu_bedroom_thirst.dialogue(opt, rng=-1):
    if opt == 1:
        liu "Ahh, {b}[firstname]{/b}!!"


    elif opt == 2:
        liu "Anda pria yang luar biasa!"


        if rng < .6:
            liu "Aku tidak ingin kamu berhenti bercinta denganku!"


        if rng < .3:
            anon "Gan, aku harus..."

            anon "... Berhenti..."

            anon "... Akhirnya."

            liu "Tidak, tidak pernah!"


    elif opt == 3:
        anon "{i}*Suara ciuman*{/i}"

        liu "Ah, ya!!"


        if rng < .3:
            anon "Kamu cantik sekali, {b}Liu{/b}..."

            liu "Tidak!!"


    elif opt == 4:
        liu "Pegang aku lebih erat..."

        liu "... Tolong, {b}[firstname]{/b}!"

        anon "Baiklah."


    return


label scene_liu_bedroom_thirst.switch:
    $ M_liu.set('sex speed', 1. / 8)

    show liu_sex_bed_anim 1 as anim
    with {'master': dissolve}
    liu "MM."

    call scene_liu_bedroom_thirst.insert
    with {'master': dissolve}
    pause .5
    call scene_liu_bedroom_thirst.animate
    with {'master': dissolve}
    call scene_liu_bedroom_thirst.dialogue (1)
    pause
    call scene_liu_bedroom_thirst.dialogue (2)
    pause
    call scene_liu_bedroom_thirst.dialogue (3)
    pause
    call scene_liu_bedroom_thirst.dialogue (4)
    pause
    call scene_liu_bedroom_thirst.loop
    jump scene_liu_sex_bedroom.switch


screen scene_liu_bedroom_thirst_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') - 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') + 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
