label scene_nadya_sex_office:
    call scene_nadya_sex_office.stage
    pause
    call scene_nadya_sex_office.common
    nadya f_normal "Oh, aku pikir kita..."

    nadya "... Akan mendapat teman yang sangat baik, {b}[firstname]{/b}."

    anon "Y-ya, aku juga."

    nadya f_laugh "hehe!"


    if _return == 'inside':
        call call_pregnancy_minigame (None, M_nadya)
    return


label scene_nadya_sex_office.stage:
    scene location_warehouse_office_sex
    show nadya nadya_sex_couch
    with fade
    return


label scene_nadya_sex_office.pre:
    show nadya a_insert b_base with {'master': dissolve}
    return


label scene_nadya_sex_office.insert:
    hide nadya
    show nadya_sex_couch_anim 8 as animation
    with dissolve
    return


label scene_nadya_sex_office.animate:
    python:
        anim_toggle = True
        animated = True
        M_nadya.set('sex speed', .1)
    hide anon
    hide nadya
    show nadya_sex_couch_anim as animation
    with dissolve
    return


label scene_nadya_sex_office.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show nadya_sex_couch_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_nadya_sex_office.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'nadya_sex_couch_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_nadya_sex_office.dialogue
        $ animcounter += 1
    call screen scene_nadya_sex_office_controls
    if not _return:
        jump scene_nadya_sex_office.loop
    return _return


label scene_nadya_sex_office.dialogue:
    if animcounter == 0 and randomizer() > 75:
        nadya "Saya tidak menginginkan belas kasihan.{w=1}{nw}"

        anon "Umm, oke...{w=1}{nw}"

    elif animcounter == 0 and randomizer() > 75:
        nadya "Mmm, that feels good.{w=1}{nw}" (show_native="Mmm, khorosho.")
    elif animcounter == 1 and randomizer() > 75:
        nadya "Ahh!{w=1}{nw}"

        pause 1
        anon "Wow, Anda menerima semuanya tanpa masalah!{w=1}{nw}"

        nadya "Kurangi bicara, perbanyak omongan!{w=1}{nw}"

        anon "Baiklah.{w=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        nadya "Your cock is amazing!{w=1}{nw}" (show_native="U tebya potryasayushchiy chlen!")
        nadya "Persetan denganku!!{w=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        nadya "Ya!{w=1}{nw}"

        nadya "Ya ampun!{w=1}{nw}"

    return


label scene_nadya_sex_office.cum(where):
    anon "Apakah kamu dekat?"

    nadya "Ya!!"

    anon "Bagus, karena aku tidak bisa bertahan lebih lama lagi!"

    pause
    nadya "I'm cumming!!" (show_native="Ya konchayu!!")
    nadya "Ahh, I'm cumming!!" (show_native="Ahh, ya konchayu!!")
    nadya "NGGHHH!!!"

    hide animation
    show nadya nadya_sex_couch f_surprised m_talk
    if where == 'inside':
        show nadya b_cum
    else:
        show nadya a_cumshot b_base
    anon "HNNGGG!!!" with flash
    if where == 'inside':
        show xray_nadya_sex_couch with fastdissolve
        pause
        hide xray_nadya_sex_couch with {'master': dissolve}
    else:
        show nadya a_cumshot3
    show nadya -m_talk
    anon "Haah... Haah..."

    if where == 'inside':
        show nadya a_insert b_base o_after with dissolve
        pause
        show nadya b_pre with {'master': dissolve}
    return where


label scene_nadya_sex_office.common:
    call scene_nadya_sex_office.pre
    nadya "Persetan dengan vaginamu, oke?"

    nadya "Saya tidak menginginkan belas kasihan."

    anon "Um, oke..."

    call scene_nadya_sex_office.insert
    nadya "Mmm, that feels good." (show_native="Mmm, khorosho.")
    pause
    call scene_nadya_sex_office.animate
    nadya "Ahhh!"

    pause
    anon "Wow, kamu menerima semuanya tanpa masalah!"

    nadya "Kurangi bicara, perbanyak bicara!"

    anon "Baiklah."

    pause
    nadya "Your cock is amazing!" (show_native="U tebya potryasayushchiy chlen!")
    nadya "Persetan denganku!!"

    pause
    nadya "Ya!"

    nadya "Ya ampun!"

    pause
    call scene_nadya_sex_office.loop
    call scene_nadya_sex_office.cum (_return)
    return _return


label scene_nadya_sex_office.repeat:
    call scene_nadya_sex_office.stage
    nadya "Ayo..."

    nadya "... Memekku sudah meneteskan nafsu."

    anon "Y-ya, oke."

    call scene_nadya_sex_office.common

    if _return == 'inside':
        nadya "Wow!" (show_native="Ukh ty!")
        nadya f_normal "Kamu membuatku kenyang!"

        anon "Y-ya."

        nadya "Ini pasti akan membuat bayi!"

        pause
        anon "Apakah itu hal yang buruk?"

        nadya "Of course not!" (show_native="Konechno, nyet!")
        nadya "Saya membutuhkan ahli waris untuk mengambil alih Bratva di masa depan."

        nadya "Mudah-mudahan itu perempuan."

        call call_pregnancy_minigame (None, M_nadya)
    else:

        pause
        nadya "Wow!" (show_native="Ukh ty!")
        nadya f_normal "Anda menjatuhkan beban yang mengesankan!"

        anon "Y-ya."

        nadya "Lihat itu, lari ke bawah."

        pause
        nadya f_laugh "hehe!"


    return


label scene_nadya_sex_office.replay:
    jump scene_nadya_sex_office.repeat


screen scene_nadya_sex_office_controls():
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
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') + 0.02),
                        Return(False))
                sensitive M_nadya.get('sex speed') < .1
            textbutton _('Faster »'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') - 0.02),
                        Return(False))
                sensitive M_nadya.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
