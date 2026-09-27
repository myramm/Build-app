label scene_eve_sex_shower:

    return


label scene_eve_sex_shower.animate:
    if gender == 'trans':
        hide penis
        show eve_sex_shower_anim_trans as animation
    else:
        show eve_sex_shower_anim_cis as animation
    return


label scene_eve_sex_shower.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_eve_sex_shower.animate
                $ animated = True
            pause 5
            call scene_eve_sex_shower.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = range(1, 8)
            $ poses_done = []
            while poses_done != pose_list:
                show expression "eve_sex_shower_anim {} {}".format(
                    gender, pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_eve_sex_shower.dialogue
        $ animcounter += 1
    call screen scene_eve_sex_shower_controls()
    if not _return:
        jump scene_eve_sex_shower.loop
    return _return


label scene_eve_sex_shower.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        eve "Ahh!!{w=1}{nw}"

        if gender == 'trans':
            eve "Persetan, {b}[firstname]{/b}!!{w=2.5{nw}"

            eve "OH, sial!!!{w=2}{nw}"

        else:
            eve "Persetan denganku, {b}[firstname]{/b}!!{w=2.5{nw}"

            eve "OH, PERCAYA AKU!!!{w=2}{nw}"

    elif animcounter == 0 and rng <= .66:
        eve "Ah, disana!!{w=2}{nw}"


    elif animcounter == 1 and rng <= .33:
        if gender == 'trans':
            anon "Pantatmu luar biasa, {b}Eve{/b}!{w=3}{nw}"

        else:
            anon "Ini luar biasa, {b}Hawa{/b}!{w=2.5{nw}"

        eve "Ahh!{w=1}{nw}"

    elif animcounter == 1 and rng <= .66:
        eve "SIALAN YA!!!{w=1.5{nw}"

        eve "Aku cinta kamu, {b}[firstname]{/b}!{w=2.5{nw}"


    elif animcounter == 2 and rng <= .33:
        if gender == 'trans':
            anon "Sangat ketat!{w=2}{nw}"

        else:
            anon "Kamu sangat ketat!{w=2}{nw}"

        eve "Oh, {b}[firstname]{/b}!!{w=1.5{nw}"

    elif animcounter == 2 and rng <= .66:
        eve "Aku sangat mencintaimu-{w=2}{nw}"

        eve "...Ngh, BANYAK!!{w=1.5{nw}"


    return


label scene_eve_sex_shower.cum(where):
    anon "Aku semakin dekat!"

    eve "Saya juga!"

    pause
    eve "Pegang aku erat-erat!"

    anon "Seperti ini?"

    eve "Ya, begitu saja!!"

    pause
    eve "Ya, ya, ya!!!"

    eve "NGGHHH!!!"


    show eve_body_b_sex_shower_cum as animation

    if gender == 'trans':
        show eve_body_b_sex_shower_cum_alt as penis behind steam

    anon "HNNGGG!!!" with flash

    if gender == 'cis' and where == 'inside':
        show xray_eve_sex_shower as xray
        with fastdissolve

    pause
    hide xray
    with {'master': dissolve}

    anon "Haah... Haah..."

    eve "Haah... Haah..."

    hide animation
    hide penis
    show eve b_naked_shower_kiss01 f_drink behind steam:
        xoffset -175 xzoom -1 yalign 1. zoom 1.25

    if gender == 'trans':
        show eve od_dick02
    else:
        show eve od_scar

    with {'master': dissolve}
    eve "Sialan, apa aku kelelahan!"

    show eve f_nervous
    anon "Fiuh, aku juga."

    eve f_nervous_down "Setidaknya kita tidak perlu membereskan kekacauan kali ini."

    anon "Hehe, ya."

    eve f_nervous "Anda mungkin harus membantu saya keluar."

    anon "Benar-benar?"


    if gender == 'trans':
        show eve od_dick01
        with {'master': dissolve}

    eve f_happy "Ya, aku merasa seperti akan terjungkal..."

    anon "hehe!"

    eve f_laugh "... Hehehe!"


    if gender == 'cis' and where == 'inside':
        call call_pregnancy_minigame (None, M_eve)
    return


label scene_eve_sex_shower.repeat(gender):
    python:
        renpy.dynamic(anim_toggle=True, animated=True, animcounter=0,
                      pose_counter=0, pose_list=None, poses_done=None)
        M_eve.set('sex speed', 1 / 8.)

    scene location_tattoo_bathroom_shower:
        align (.25, 1.) zoom 1.25

    if gender == 'trans':
        show eve_sex_shower_anim_trans 1 as animation
    else:
        show eve_sex_shower_anim_cis 1 as animation

    show location_tattoo_bathroom_shower_steam as steam:
        align (.25, 1.) zoom 1.25
    show eve_sex_shower_anim_water as water:
        align (.25, 1.) zoom 1.25
    show shower_steam
    with fade
    eve "Haah!"

    anon "Wow, semuanya berjalan cukup mudah saat itu."

    call scene_eve_sex_shower.animate
    eve "Ya, untukmu..."

    eve "... Mungkin..."

    eve "...Ah, sial!"

    anon "Apakah itu terlalu dalam?"

    eve "Tidak."

    anon "Apa kamu yakin?"

    eve "Y-ya!"

    eve "sial!!"

    pause
    anon "Aduh, beruap sekali di sini..."

    eve "Eh ya!"

    pause
    anon "... Bisakah kita menurunkan suhu air sedikit?"

    eve "Tidak!!"

    pause
    anon "{b}Malam{/b}?"

    eve "Hmm?"

    anon "Sudahlah."

    eve "T-tidak, apa yang kamu katakan?"

    anon "Tidak ada yang penting."


    call scene_eve_sex_shower.loop
    call scene_eve_sex_shower.cum (_return)
    return


label scene_eve_sex_shower.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Eve']['variants']['08_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_tattooparlor_bathroom) with fade
        menu:
            "Cis" if 'cis' in variants:
                call scene_eve_sex_shower.repeat ('cis')

            "Trans" if 'trans' in variants:
                call scene_eve_sex_shower.repeat ('trans')
    else:

        call scene_eve_sex_shower.repeat (next(iter(variants)))

    return


screen scene_eve_sex_shower_controls():
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
                action (Function(M_eve.set, 'sex speed',
                                 1 / (1 / M_eve.get('sex speed') - 2)),
                        Return(False))
                sensitive M_eve.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_eve.set, 'sex speed',
                                 1 / (1 / M_eve.get('sex speed') + 2)),
                        Return(False))
                sensitive M_eve.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
