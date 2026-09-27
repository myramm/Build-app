label scene_crystal_sex_trailer:

    return


label scene_crystal_sex_trailer.insert:
    show crystal_sex_chair_anim 8 as animation
    return

label scene_crystal_sex_trailer.animate:
    show crystal_sex_chair_anim as animation
    return


label scene_crystal_sex_trailer.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_crystal_sex_trailer.animate
                $ animated = True
            pause 5
            call scene_crystal_sex_trailer.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = range(1, 11)
            $ poses_done = []
            while poses_done != pose_list:
                show expression "crystal_sex_chair_anim {}".format(
                    pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_crystal_sex_trailer.dialogue
        $ animcounter += 1
    call screen scene_crystal_sex_chair_controls()
    if not _return:
        jump scene_crystal_sex_trailer.loop
    return _return


label scene_crystal_sex_trailer.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        crystal "Ya seperti itu, Romeo?{w=2}{nw}"

        anon "Y-ya!{w=1}{nw}"

        if rng <= .06:
            crystal "Aku bilang, kamu suka caraku mengerjakan vagina itu?!{w=4}{nw}"

            anon "YA!!{w=1}{nw}"

            crystal "Hehe!{w=1}{nw}"


    elif animcounter == 0 and rng <= .66:
        crystal "Cukup bagus bukan?{w=2}{nw}"

        anon "Mhmm!{w=1.5{nw}"

        crystal "Iya pak, itu latihan bertahun-tahun... Iya!{w=4}{nw}"


    elif animcounter == 1 and rng <= .33:
        crystal "Ya, sebaiknya pegang erat-erat sekarang, karena aku akan menaikkan suhunya!{w=4.5{nw}"

        anon "!!!{w=1}{nw}"


    elif animcounter == 1 and rng <= .66:
        crystal "Ngh, inilah yang saya butuhkan!{w=2}{nw}"

        crystal "Tidak ada yang lebih baik untuk memompa darah!{w=3.5{nw}"


    elif animcounter == 1 and rng <= .99:
        crystal "Sooey, itu sangat menyebalkan!{w=2}{nw}"

        anon "Ssst, {b}Roxxy{/b} akan mendengarkanmu!!{w=2.5{nw}"

        crystal "Oh, dia tidak peduli apa yang aku lakukan di sini...{w=3}{nw}"

        crystal "... Kamu fokus saja untuk mengisi hatiku!{w=2.5{nw}"


    elif animcounter == 2 and rng <= .33:
        crystal "Ambil mah titty, itu akan membantu kamu cum lebih cepat.{w=3.5{nw}"


    elif animcounter == 2 and rng <= .66:
        crystal "Hati-hati ya, jangan bersandar terlalu jauh ke belakang sekarang...{w=3.5}{nw}"

        crystal "... Tidak ingin kamu merusak kursi duduk yang bagus!{w=3.5{nw}"

        anon "Ini kursi duduk Anda yang bagus?{w=2.5}{nw}"

        crystal "Kamu juga ikutan!{w=1.5{nw}"


    elif animcounter == 2 and rng <= .99:
        crystal "Sialan, aku belum pernah mendapatkan penis sebagus ini selama bertahun-tahun!{w=2.5{nw}"

        crystal "Ya membuatku bocor seperti kandang ayam di tengah hujan badai!{w=4.5}{nw}"

        anon "Hah?!{w=1.5{nw}"


    return


label scene_crystal_sex_trailer.cum(where):
    anon "Ya ampun, aku tidak bisa bertahan lebih lama lagi..."

    crystal "Tidak apa-apa, aku juga dekat."

    crystal "Lanjutkan dan keluarkan racun itu!"

    anon "O-oke."

    pause
    anon "Ini dia..."

    anon "... Datang!!"

    crystal "NGGHHH!!!"

    show crystal_body_b_sex_chair_cum as animation

    if where == 'outside':
        show crystal_sex_chair_cumshot as cum

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_crystal_sex_chair as xray
        with {'master': fastdissolve}

    pause
    hide xray
    with {'master': dissolve}

    anon "Haah... Haah..."

    show crystal_body_b_sex_chair_unmount as animation

    if where == 'outside':
        show crystal_body_b_sex_chair_unmount_cum as cum

    with {'master': dissolve}
    crystal "Haah..."

    return where


label scene_crystal_sex_trailer.repeat:
    python:
        renpy.dynamic(anim_toggle=True, animated=True, animcounter=0,
                      pose_counter=0, pose_list=None, poses_done=None)
        M_crystal.set('sex speed', 1 / 8.)

    scene location_trailer_sex_chair_evening
    show crystal_body_b_sex_chair_insert as animation
    with fade
    crystal "Mmm, itu dia..."

    crystal "... Ini dia Bu!"

    call scene_crystal_sex_trailer.insert
    with {'master': dissolve}
    crystal "Aduh!"

    crystal "Nah, itu lebih ketat daripada agas brengsek..."

    call scene_crystal_sex_trailer.animate
    with {'master': dissolve}
    pause
    crystal "Sialan!"

    pause
    crystal "Oh, itu dia..."

    crystal "... Bagus dan dalam."


    call scene_crystal_sex_trailer.loop
    call scene_crystal_sex_trailer.cum (_return)
    return _return


label scene_crystal_sex_trailer.replay:
    jump scene_crystal_sex_trailer.repeat


screen scene_crystal_sex_chair_controls():
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
                action (Function(M_crystal.set, 'sex speed',
                                 1 / (1 / M_crystal.get('sex speed') - 2)),
                        Return(False))
                sensitive M_crystal.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_crystal.set, 'sex speed',
                                 1 / (1 / M_crystal.get('sex speed') + 2)),
                        Return(False))
                sensitive M_crystal.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
