label scene_eve_sex_wake:

    return


label scene_eve_sex_wake.stage:
    scene location_tattoo_bedroom_sex_wakeup
    show eve sex_wake trans
    if gender == 'cis':
        show eve cis -trans
    if anal:
        show eve anal
    return


label scene_eve_sex_wake.animate:
    hide eve
    show eve_sex_wake_anim trans
    if gender == 'cis':
        show eve_sex_wake_anim cis -trans
    if anal:
        show eve_sex_wake_anim anal
    return


label scene_eve_sex_wake.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_eve_sex_wake.animate
                $ animated = True
            pause 5
            call scene_eve_sex_wake.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "eve_sex_wake_anim {} {} {}".format(
                    gender, 'anal' if anal else '', pose_list[pose_counter]) as eve_sex_wake_anim
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_eve_sex_wake.dialogue
        $ animcounter += 1
    call screen scene_eve_sex_wake_controls(gender, anal)
    if not _return:
        jump scene_eve_sex_wake.loop
    return _return


label scene_eve_sex_wake.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        eve "Sial!{w=1}{nw}"


    elif animcounter == 0 and rng <= .55:
        anon "Apakah terlalu dalam?{w=1}{nw}"

        eve "Tidak.{w=1}{nw}"

        anon "Apakah Anda yakin?{w=1}{nw}"

        eve "Y-ya!{w=1}{nw}"

        eve "Ah, sial!!{w=1}{nw}"


    elif animcounter == 1 and rng <= .33:
        anon "Apakah itu terasa enak?{w=1.5{nw}"

        eve "Ya!!{w=1}{nw}"


    elif animcounter == 1 and rng <= .66:
        anon "Apakah tidak apa-apa?{w=1}{nw}"

        eve "Hmm!{w=1}{nw}"

        anon "Rasanya enak?{w=1}{nw}"

        eve "Ya!!{w=1}{nw}"


    elif animcounter == 1 and rng <= .88 and gender == 'cis':
        anon "Aku tidak percaya betapa basahnya kamu!{w=2}{nw}"

        eve "{i}*Merengek*{/i}{w=1}{nw}"


    elif animcounter == 1 and rng <= .88 and gender == 'trans':
        anon "Aku suka melihat gadismu memantul saat aku menidurimu...{w=2.5{nw}"

        eve "{i}*Merengek*{/i}{w=1}{nw}"

        anon "... Menggemaskan sekali!{w=1}{nw}"


    elif animcounter == 2 and rng <= .22 and anal:
        anon "Pantatmu luar biasa, {b}Eve{/b}!{w=2}{nw}"

        eve "Ahh!{w=1}{nw}"

        pause 1
        anon "Sangat ketat!{w=1}{nw}"

        eve "Oh, {b}[firstname]{/b}!!{w=1}{nw}"


    elif animcounter == 2 and rng <= .33:
        eve "Sangat dalam!{w=1.5{nw}"

        eve "Ahh!{w=1}{nw}"

        pause 1
        eve "Oh, {b}[firstname]{/b}!!{w=1}{nw}"


    elif animcounter == 2 and rng <= .55:
        eve "Aku cinta kamu, {b}[firstname]{/b}!{w=1}{nw}"

        pause 1
        eve "Aku sangat mencintaimu-{w=1.5}{nw}"

        eve "...Ngh, BANYAK!!{w=1}{nw}"


    return


label scene_eve_sex_wake.anal:
    call scene_eve_sex_wake.stage
    show eve insert lipbite
    with {'master': dissolve}
    anon "Bolehkah aku menaruhnya di pantatmu lagi?"

    show eve embarrassed
    with {'master': fastdissolve}
    eve "Saya tidak peduli di mana Anda menaruhnya, cepatlah!"

    eve "Silakan!"

    $ anal = True
    show eve anal lipbite
    with {'master': dissolve}
    anon "Baiklah."

    show eve slam
    eve "!!!" with hpunch
    eve "Ahhh!"

    jump scene_eve_sex_wake.resume


label scene_eve_sex_wake.vaginal:
    call scene_eve_sex_wake.stage
    show eve insert lipbite
    with {'master': dissolve}
    anon "Bisakah saya menukarnya kembali?"

    show eve embarrassed
    with {'master': fastdissolve}
    eve "Lakukan saja padaku!"

    eve "Silakan!"

    $ anal = False
    show eve -anal lipbite
    with {'master': dissolve}
    anon "Baiklah."

    show eve slam
    eve "!!!" with hpunch
    eve "Ngghhh!"

    jump scene_eve_sex_wake.resume


label scene_eve_sex_wake.cum(where):
    anon "Aku semakin dekat!"

    eve "Saya juga!"

    pause
    eve "Astaga!"

    eve "Oh, persetan denganku!!"

    pause
    eve "Haah!"

    pause

    if gender == 'trans':
        $ AnimatedImage2.signal(-1)

    eve "NGGHHH!!!" with flash
    pause

    if gender == 'cis':
        eve "Ohhh!"

    else:

        eve "Oh tidak..."

        anon "Wow, apakah kamu baru saja-"

        eve "{b}* Merengek*{/b}"


    anon "Kamu sangat seksi, {b}Eve{/b}!"

    anon "aku akan-"


    call scene_eve_sex_wake.stage

    if where == 'inside':
        show eve cum
    else:
        show eve cumshot gasp

    anon "HNNGGG!!!" with flash





    pause
    hide xray

    if where == 'inside':
        show eve pullout
    else:
        show eve after outside

    show eve lipbite
    with {'master': dissolve}
    anon "Haah... Haah..."


    if where == 'inside':
        show eve after inside
        with {'master': dissolve}

    if gender == 'trans':
        eve surprised "Aku tidak percaya aku melakukan itu..."

        anon "Hmm?"

        eve "Aku sangat malu... Aku-"

        anon "Jangan malu!"

        anon "Itu luar biasa!"

        show eve embarrassed
        with {'master': dissolve}
        eve "Hehe, benarkah?"

        anon "Ya Tuhan, ya!"

        pause
    else:

        eve horny "Wah!"

        eve "Itu tadi-"

        pause
        eve "Wow."

        show eve laugh
        with {'master': fastdissolve}
        eve "Hehehe!"


        if where == 'inside':
            anon "hehe!"


            if not anal:
                call call_pregnancy_minigame (None, M_eve)

            return

    show eve horny
    with {'master': fastdissolve}
    pause
    eve "Itu bukan jenis mandi yang biasa kulakukan di pagi hari..."

    anon "hehe!"

    show eve laugh
    with {'master': fastdissolve}
    eve "Hehehe!"

    show eve horny
    with {'master': fastdissolve}
    pause
    anon "Biarkan aku mengambilkanmu handuk."

    eve "Ya terima kasih."

    return


label scene_eve_sex_wake.repeat(gender, anal=True):
    python:
        renpy.dynamic(anim_toggle=True, animated=True,
                      animcounter=0, animstate=None)
        M_eve.set('sex speed', 1 / 8.)
        anal = gender == 'trans' or (False if anal else None)

    call scene_eve_sex_wake.stage
    with fade
    anon "Wow, itu pemandangan yang membuat saya senang bangun setiap pagi!"

    eve "Ah, jangan menggodaku..."


    if gender == 'cis':
        eve "... Aku sangat basah untukmu."

    else:
        eve "... Aku sangat sulit untukmu."


    anon "Ya, saya bisa melihatnya."

    show eve insert
    with {'master': dissolve}
    eve "Aku ingin kamu ada di dalam diriku!"


    if gender == 'cis':
        show eve lipbite
        with {'master': fastdissolve}
        anon "Baiklah."

        show eve slam
        eve "!!!" with hpunch
    else:

        show eve embarrassed
        with {'master': fastdissolve}
        eve "Lambat saja..."

        eve "... Aku mulai terbiasa tapi kamu sudah sangat besar."

        show eve lipbite
        with {'master': fastdissolve}
        anon "Saya akan."

        show eve enter
        with {'master': dissolve}
        eve "!!!"

    eve "Sial!"

    label scene_eve_sex_wake.resume:
    call scene_eve_sex_wake.animate
    with dissolve
    call scene_eve_sex_wake.loop
    if _return == 'switch':
        if anal:
            jump scene_eve_sex_wake.vaginal
        else:
            jump scene_eve_sex_wake.anal
    call scene_eve_sex_wake.cum (_return)
    return


label scene_eve_sex_wake.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Eve']['variants']['07_unlocked'])

    if variants >= {'cis', 'trans'}:
        scene expression background(l=L_tattooparlor_bedroom) with fade
        menu:
            "Cis" if 'cis' in variants:
                call scene_eve_sex_wake.repeat ('cis', 'cis anal' in variants)

            "Trans" if 'trans' in variants:
                call scene_eve_sex_wake.repeat ('trans')
    else:

        call scene_eve_sex_wake.repeat (next(iter(variants)), True)

    return


screen scene_eve_sex_wake_controls(gender, anal):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            if gender == 'cis':
                if anal is True:
                    textbutton _('Vaginal') action Return('switch')
                elif anal is False:
                    textbutton _('Anal') action Return('switch')

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
