label scene_tina_sex_office:

    return


label scene_tina_sex_office.ready:
    show tina b_sex_office_base
    show anon_sex_office_base
    show anon_sex_office_dick pre
    with fade
    return


label scene_tina_sex_office.insert:
    hide anon_sex_office_base
    hide anon_sex_office_dick
    show tina b_sex_office_insert
    with dissolve
    return


label scene_tina_sex_office.animate:
    python:
        anim_toggle = True
        animated = True
        M_tina.set('sex speed', .1)
    hide tina
    show tina_body_b_sex_office_anim as animation
    with dissolve
    return


label scene_tina_sex_office.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show tina_body_b_sex_office_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_tina_sex_office.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'tina_body_b_sex_office_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_tina_sex_office.dialogue
        $ animcounter += 1
    call screen scene_tina_sex_office_controls
    if not _return:
        jump scene_tina_sex_office.loop
    return _return


label scene_tina_sex_office.dialogue:
    if animcounter == 0 and randomizer() > 75:
        tina "Oh, persetan denganku!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 75:
        tina "Di sana!{p=1}{nw}"

    elif animcounter == 1 and randomizer() > 75:
        tina "Sangat dalam!{p=1}{nw}"

    if animcounter == 2 and randomizer() > 75:
        tina "Saya-{p=1}{nw}"

        tina "Aku akan keluar!!{p=1}{nw}"

    return


label scene_tina_sex_office.cum(where):
    anon "Aku semakin dekat!"

    tina "Jangan berhenti!"

    pause
    anon "aku tidak bisa-"

    tina "Ya Tuhan!!"

    pause
    hide animation

    if where == 'inside':
        show tina b_sex_office_cum
    else:
        show tina b_sex_office_base
        show anon_sex_office_base
        show anon_sex_office_dick cumshot

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_tina_office with fastdissolve:
            align (0,0)

    tina "NGGHHH!!!"


    if where == 'inside':
        show tina b_sex_office_insert o_sex_office_pullout
        hide xray_tina_office
    else:
        show anon_sex_office_dick pre
        show tina o_sex_office_dick_cumshot3

    with dissolve
    pause

    if where == 'inside':
        show tina b_sex_office_base o_empty
        show anon_sex_office_base
        show anon_sex_office_dick after
        with dissolve

    anon "Haah... Haah..."

    anon "Wah!"

    anon "Itu tadi..."

    tina "Kuat?"

    anon "Y-ya."

    tina "hehe!"

    pause

    if where == 'inside':
        tina "Mmm, aku bisa merasakanmu keluar dari diriku..."

        anon "Ya, sebaiknya aku mundur, ya?"

    else:
        tina "Mmm, ada air mani di jaketku..."

        anon "Ya, sebaiknya aku membidik ke tempat lain, ya?"


    tina "Hehe, tidak apa-apa."


    if where == 'inside':
        call call_pregnancy_minigame (None, M_tina)
    return where


label scene_tina_sex_office.repeat:
    scene location_bank_office_cubicle_sex
    call scene_tina_sex_office.ready
    tina "Silakan, masukkan."

    anon "Ya, Bu."

    call scene_tina_sex_office.insert
    tina "Ngh!"

    pause
    call scene_tina_sex_office.animate
    tina "Itu dia!"

    tina "Berikan padaku, {b}[firstname]{/b}!"

    pause
    anon "Anda suka itu?"

    tina "Ya!"

    anon "Anda suka membungkuk di atas meja Anda?"

    tina "Ah, ya!!"

    call scene_tina_sex_office.loop
    call scene_tina_sex_office.cum (_return)
    return _return


label scene_tina_sex_office.replay:
    jump scene_tina_sex_office.repeat


screen scene_tina_sex_office_controls():
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
                action (Function(M_tina.set,
                                 'sex speed',
                                 M_tina.get('sex speed') + 0.02),
                        Return(False))
                sensitive M_tina.get('sex speed') < .1
            textbutton _('Faster »'):
                action (Function(M_tina.set,
                                 'sex speed',
                                 M_tina.get('sex speed') - 0.02),
                        Return(False))
                sensitive M_tina.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
