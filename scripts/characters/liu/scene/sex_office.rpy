label scene_liu_sex_office:

    return


label scene_liu_sex_office.stage:
    scene location_bank_office_printer_sex
    show liu b_sex_printer_base
    return


label scene_liu_sex_office.pre:
    show liu b_sex_printer_insert
    return


label scene_liu_sex_office.insert:
    hide liu
    show liu_sex_printer_anim 5 as animation
    return


label scene_liu_sex_office.animate:
    python:
        anim_toggle = True
        animated = True
    hide anon
    hide liu
    show liu_sex_printer_anim as animation
    return


label scene_liu_sex_office.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show liu_sex_printer_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_liu_sex_office.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'liu_sex_printer_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_liu_sex_office.dialogue
        $ animcounter += 1
    call screen scene_liu_sex_office_controls
    if not _return:
        jump scene_liu_sex_office.loop
    return _return


label scene_liu_sex_office.dialogue:
    if animcounter == 0 and randomizer() > 75:
        liu "NGH!!{w=1}{nw}"

    elif animcounter == 0 and randomizer() > 75:
        liu "Ahh, sial!!{w=1}{nw}"

        anon "Ssst!{w=1}{nw}"

        anon "Seseorang akan mendengar.{w=1}{nw}"

        pause 1
        liu "Saya tidak bisa-{w=1}{nw}"

        pause 1
        liu "Bantulah!{w=1}{nw}"

    elif animcounter == 1 and randomizer() > 75:
        liu "YA TUHAN!{w=1}{nw}"

        liu "{b}[nama depan!u]{/b}!!!{w=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        anon "Gah, kamu ketat sekali!{w=1}{nw}"

        liu "{i}*Merengek*{/i}{w=1}{nw}"

    return


label scene_liu_sex_office.switch:
    call scene_liu_sex_office.stage
    call scene_liu_sex_office.animate
    with fade
    jump scene_liu_sex_office.resume


label scene_liu_sex_office.cum(where):
    anon "aku akan keluar!"

    liu "Buru-buru!"

    pause
    liu "Ya Tuhan!!"

    liu "Ya Tuhan!!"

    pause
    liu "{i}* Merengek*{/i}"

    liu "NGGHHH!!!"

    hide animation
    if where == 'inside':
        show liu b_sex_printer_cum
    else:
        show liu b_sex_printer_base f_surprised_down od_cumshot
    anon "HNNGGG!!!" with flash
    if where == 'inside':
        show xray_liu_sex_printer with fastdissolve
        pause
        hide xray_liu_sex_printer with {'master': dissolve}
    else:
        show liu od_cumshot3
    anon "Haah... Haah..."

    return where


label scene_liu_sex_office.repeat:
    python hide:
        M_liu.set('sex speed', 1 / 8.)

    call scene_liu_sex_office.stage
    with fade
    liu "Seperti ini?"

    anon "Sama seperti itu."

    liu "O-oke tapi pelan-pelan..."

    call scene_liu_sex_office.pre
    with dissolve
    liu "... Kita tidak bisa membuat pelanggan mendengar-"

    call scene_liu_sex_office.insert
    liu "OOOHHH!!" with hpunch
    liu "USS!"

    anon "Wah!"

    call scene_liu_sex_office.animate
    with dissolve
    pause
    liu "NGH!!"

    pause
    liu "Ahhh, sial!!"

    anon "Ssst!"

    pause
    anon "Seseorang akan mendengar."

    liu "aku tidak bisa-"

    liu "Tolong!"

    pause
    liu "YA TUHAN!"

    liu "{b}[nama depan!u]{/b}!!!"

    pause
    anon "Gah, kamu sangat ketat!"

    liu "{i}* Merengek*{/i}"

    pause
    label scene_liu_sex_office.resume:
    call scene_liu_sex_office.loop
    if _return == 'switch':
        jump scene_liu_sex_office_pov.switch
    call scene_liu_sex_office.cum (_return)
    $ renpy.dynamic(where=_return)

    if where == 'inside':
        show liu b_sex_printer_base o_dick_after with dissolve
        liu "Aku tidak percaya betapa panasnya itu..."

        anon "Y-ya."

        liu "Aku datang dengan susah payah... Ya ampun!"

        pause
        liu @ -m_talk "MM."

        liu "Bagaimana aku bisa kembali bekerja setelah itu?!"

        anon "hehe!"

        call call_pregnancy_minigame (None, M_liu)
    else:

        liu f_shy "Oh, wah..."

        liu "Heh, kamu datang dengan pakaianku!"

        anon "Ah kawan, aku minta maaf..."

        anon "... Aku tidak bermaksud-"

        pause
        anon "Semuanya terjadi begitu cepat!"

        liu "Tidak, tidak apa-apa."

        liu "Itu akan hilang..."

        liu "... menurutku."

        pause
        liu "Saya hanya berharap {b}Tina{/b} tidak melihat noda sore ini."


    return where


label scene_liu_sex_office.replay:
    jump scene_liu_sex_office.repeat


screen scene_liu_sex_office_controls(angle='side'):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if angle == 'side':
                textbutton _('Cum Inside') action Return('inside')
                textbutton _('Cum Outside') action Return('outside')
            textbutton _('Change angle') action Return('switch')

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
                sensitive M_liu.get('sex speed') > 1 / 12.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
