label scene_grace_sex_apt:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_grace.set('sex speed', 1 / 8.)

    call scene_grace_sex_apt.stage
    with fade
    pause
    call scene_grace_sex_apt.insert
    with {'master': dissolve}
    grace "{i}*Terkesiap*{/i} Ya Tuhan..."

    call scene_grace_sex_apt.animate
    with {'master': dissolve}
    grace "{i}* Merengek*{/i}"

    pause
    anon "Kamu sangat cantik, {b}Grace{/b}."

    grace "Ahhh!"

    pause
    anon "Aku ingin melakukan ini sejak lama..."

    anon "... Sejak pertama kali aku melihatmu."

    grace "Ngh!"

    pause
    anon "Kamu berhak untuk bahagia, {b}Rahmat{/b}."

    anon "Anda pantas-"

    grace "{i}* Merengek*{/i}"

    anon "Ahh!!"

    pause
    call scene_grace_sex_apt.loop
    call scene_grace_sex_apt.cum (_return)
    return


label scene_grace_sex_apt.stage:
    scene location_tattoo_apartment_grace_sex_solo
    show grace sex_apt pre normal
    return


label scene_grace_sex_apt.insert:
    show grace insert
    return


label scene_grace_sex_apt.animate:
    hide grace
    show grace_sex_apt_anim
    return


label scene_grace_sex_apt.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_grace_sex_apt.animate
                $ animated = True
            pause 5
            call scene_grace_sex_apt.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'grace_sex_apt_anim {}'.format(
                    pose_list[pose_counter]) as grace_sex_apt_anim
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_grace_sex_apt.dialogue
        $ animcounter += 1
    call screen scene_grace_sex_apt_controls()
    if not _return:
        jump scene_grace_sex_apt.loop
    return _return


label scene_grace_sex_apt.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        grace "Oh, {b}[firstname]{/b}!{w=1}{nw}"

        grace "Ya Tuhan!{w=1}{nw}"


    elif animcounter == 1 and rng <= .33:
        grace "Kamu sangat besar!{w=1.5{nw}"

        pause 1
        anon "Apakah rasanya enak?{w=1}{nw}"

        grace "Ya!!{w=1}{nw}"


    elif animcounter == 2 and rng <= .33:
        grace "Ini sangat buruk, {b}[firstname]{/b}!{w=1}{nw}"

        grace "Kita jahat sekali, apa yang kita-{w=1}{nw}"

        grace "Ahh, ya Tuhan!!{w=1}{nw}"


    return


label scene_grace_sex_apt.cum(where):
    anon "Apakah kamu semakin dekat?"

    grace "Mhmm!"

    anon "Saya juga."

    pause
    anon "Anda ingin cum bersama?"

    grace "YA!"

    pause
    anon "Ini dia!"

    grace "Sial!!"

    hide grace_sex_apt_anim

    if where == 'inside':
        show grace sex_apt cum
    else:
        show grace sex_apt cumshot exhausted

    anon "HNNGGG!!!" with flash
    grace "NGGHHH!!!"


    if where == 'inside':
        show xray_grace_sex_apt as xray
        with fastdissolve

    pause
    hide xray
    show grace sex_apt exhausted pre

    if where == 'inside':
        show grace inside
    else:
        show grace outside

    with {'master': dissolve}
    anon "Haah... haah..."

    pause
    show anon grace_sex_apt f_happy
    show grace after concerned
    with {'master': dissolve}
    anon "Itu luar biasa!"

    show grace head
    with {'master': dissolve}
    anon "aku hanya-"

    anon "Wah!"

    pause
    show anon f_concerned
    anon "Hei, kamu baik-baik saja?"

    show grace normal
    grace "Aku adalah saudara perempuan yang sangat buruk..."

    anon "Apa?!"

    anon "T-tidak, ayolah... jangan lakukan itu..."

    show grace angry down
    with {'master': dissolve}
    grace "saya!"

    grace "Kamu adalah orang pertama yang {b}Eve{/b} pernah... dan aku-"

    pause
    grace "Sial!"


    if where == 'inside':
        call call_pregnancy_minigame (None, M_grace)
    return


label scene_grace_sex_apt.repeat:
    return


label scene_grace_sex_apt.replay:
    jump scene_grace_sex_apt


screen scene_grace_sex_apt_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_grace.set, 'sex speed',
                                 1 / (1 / M_grace.get('sex speed') - 2)),
                        Return(False))
                sensitive M_grace.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_grace.set, 'sex speed',
                                 1 / (1 / M_grace.get('sex speed') + 2)),
                        Return(False))
                sensitive M_grace.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
