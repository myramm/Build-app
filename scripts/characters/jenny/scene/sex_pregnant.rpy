label scene_jenny_sex_pregnant:
    call scene_jenny_sex_pregnant.stage
    with fade
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Engkau, ahh tord eww sangat baik mendatangkan ribuan hari!"

    anon "Ya, bukan itu bagian yang menjadi masalahku..."

    jump scene_jenny_sex_pregnant.resume


label scene_jenny_sex_pregnant.stage:
    scene location_home_jennybedroom_sex_preg as stage
    show jenny_sex_preg_pre as animation
    show jenny_sex_preg_insert as dick
    return


label scene_jenny_sex_pregnant.animate:
    hide dick
    show jenny_sex_preg_anim as animation
    return


label scene_jenny_sex_pregnant.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                call scene_jenny_sex_pregnant.animate
                $ animated = True
            pause 5
            call scene_jenny_sex_pregnant.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_sex_preg_anim {}".format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_jenny_sex_pregnant.dialogue
        $ animcounter += 1
    call screen scene_jenny_sex_pregnant_controls
    if not _return:
        jump scene_jenny_sex_pregnant.loop
    return _return


label scene_jenny_sex_pregnant.dialogue:
    $ renpy.dynamic(rng=renpy.random.random())

    if animcounter == 0 and rng <= .33:
        jenny "Oh, di 'belut oh' bagus sekali!{w=1.5{nw}"


    elif animcounter == 0 and rng <= .66:
        jenny "NGGHHH!!!{w=1}{nw}"


    elif animcounter == 0:
        jenny "Ya Tuhan, ya Tuhan, YA Tuhan!!!{w=1.5{nw}"


    elif animcounter == 1 and rng <= .33:
        jenny "Mmm, sial sekali!{w=1}{nw}"

        pause 1
        jenny "Sungguh 'sialan' eep!{w=1}{nw}"


    elif animcounter == 1 and rng <= .66:
        jenny "Eww 'iking iss guys?{w=1}{nw}"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{w=1}{nw}"


    elif animcounter == 2 and rng <= .33:
        jenny "Uhh, 'iss sayang belum' 'sedang bangun!{w=1.5}{nw}"

        anon "Masih?!{w=1}{nw}"

        jenny "Ya, apakah Anda sudah merasakannya?{w=1.5{nw}"


    elif animcounter == 2 and rng <= .44:
        jenny "Jangan berhenti!{w=1}{nw}"

        jenny "Aku akan cum lagi!!{w=1}{nw}"

        anon "Wah, lagi?!{w=1}{nw}"

        jenny "YA TUHAN! YA!!!{w=1}{nw}"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{w=1}{nw}"

        pause 1
        jenny "NGGHHH!!!{w=2}{nw}" with flash
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{w=1}{nw}"


    return


label scene_jenny_sex_pregnant.cum:
    anon "Ini dia!"

    jenny "Ya!!"

    anon "Dimana kamu menginginkannya?"

    jenny "YA!!!"

    anon "{b}[jen_name]{/b}?!"

    jenny "Perutku!!"

    jenny "Saya-"

    jenny "NGGHHH!!!"

    show jenny_sex_preg_cum as animation
    show jenny_sex_preg_cumshot as dick
    anon "HNNGGG!!!" with flash
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    hide dick
    show jenny_sex_preg_after as animation
    anon "Hurggk!!" with vpunch
    pause
    anon "Haah... haah..."

    pause
    anon "{b}[jen_name]{/b}?"

    pause
    anon "Kamu baik-baik saja?"

    jenny "{i}*Bergumam tak jelas*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    anon "Um, apa?"

    pause
    anon "{b}[jen_name]{/b}?!"

    jenny "Ugh... diam..."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    return


label scene_jenny_sex_pregnant.repeat:
    call scene_jenny_sex_pregnant.stage
    with fade
    jenny "Coba sekarang dan baru saja!"

    anon "Ya, bicaralah sendiri..."


    label scene_jenny_sex_pregnant.resume:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_jenny.set('sex speed', 1 / 8.)

    jenny "Ahhh, sial!!!"

    jenny "Oh!"

    pause
    call scene_jenny_sex_pregnant.animate
    with dissolve
    jenny "Oh, di 'belut oh' bagus sekali!"

    pause
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Mmm, 'sialan!"

    pause
    jenny "Ini sangat 'sialan' eep!"

    jenny "Aku akan keluar!"

    pause
    jenny "NGGHHH!!!" with flash
    pause
    jenny "Ya Tuhan, ya Tuhan, ya Tuhan!!!"

    pause
    jenny "Eww 'iking itu laki-laki?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    jenny "Uhh sayang jadi gila di sini!"

    anon "Benar-benar?"

    jenny "Ya, apakah kamu merasa menendangnya?"

    pause
    jenny "Jangan berhenti!"

    jenny "Aku akan cum lagi!!"

    anon "Wah lagi?!"

    jenny "YA!!!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    jenny "NGGHHH!!!" with flash
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    jenny "Apakah kita sudah dekat?"

    anon "Agak."

    pause
    jenny "Baiklah, 'cepatlah!!"

    jenny "Aku tidak tahu apakah aku bisa-"

    $ M_jenny.set('sex speed', 1 / 14.)
    with vpunch
    jenny "OH, sial!!!"

    call scene_jenny_sex_pregnant.loop
    call scene_jenny_sex_pregnant.cum
    return


label scene_jenny_sex_pregnant.replay:
    jump scene_jenny_sex_pregnant.repeat


screen scene_jenny_sex_pregnant_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('outside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_jenny.set, 'sex speed',
                                 1 / (1 / M_jenny.get('sex speed') - 2)),
                        Return(False))
                sensitive M_jenny.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_jenny.set, 'sex speed',
                                 1 / (1 / M_jenny.get('sex speed') + 2)),
                        Return(False))
                sensitive M_jenny.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
