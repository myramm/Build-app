label scene_debbie_diane_bedroom:

    return


label scene_debbie_diane_bedroom.animate:
    show debbie_diane_anim as animation
    return


label scene_debbie_diane_bedroom.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show debbie_diane_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_debbie_diane_bedroom.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'debbie_diane_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_debbie_diane_bedroom.dialogue
        $ animcounter += 1
    call screen scene_debbie_diane_bedroom_controls
    if not _return:
        jump scene_debbie_diane_bedroom.loop
    return _return


label scene_debbie_diane_bedroom.dialogue:
    $ renpy.dynamic(rng=renpy.random.random(),
                    slow=M_debbie.get('sex speed') <= 1. / 12)

    if animcounter == 0 and rng <= .66:
        if slow:
            debbie "Bagaimana Anda selalu menemukan tempat yang sempurna?!{w=2}{nw}"

            diane "Oh, ayolah... kita berteman baik.{w=2}{nw}"

            diane "Kalau ada yang tahu tempatmu, itu aku.{w=2}{nw}"

            debbie "Hehe, menurutku itu masuk akal.{w=2}{nw}"

        else:
            diane "Astaga!{w=1}{nw}"

            debbie "Ahh!{w=1}{nw}"

            pause 1
            diane "Oh, {b}[deb_name]{/b}!{w=1}{nw}"

            pause 1
            diane "Ini terasa luar biasa!!{w=1}{nw}"

        pause 1

    elif animcounter == 1 and rng <= .33:
        if slow:
            diane "Ya Tuhan, kamu basah kuyup...{w=1.5{nw}"

            debbie "{b}Diane{/b}!!{w=1}{nw}"

            debbie "Jangan berkata seperti itu, kamu tahu itu membuatku malu!{w=2}{nw}"

            diane "Hehe!{w=1}{nw}"

            diane "Ya, tapi itu juga membuat Anda bersemangat.{w=1.5{nw}"

            debbie "Ngh!{w=1}{nw}"

            pause .5
            diane "Lihat!{w=1}{nw}"

        else:
            diane "Aku sangat senang kita bisa dekat lagi, seperti dulu!!{w=2}{nw}"

            debbie "Saya juga!{w=1}{nw}"

            diane "Aku sangat merindukanmu, {b}[deb_name]{/b}!{w=2}{nw}"

            debbie "Ahh!!{w=1}{nw}"

            debbie "Jangan berhenti!!{w=1}{nw}"

        pause 1

    elif animcounter == 1 and rng <= .66:
        if slow:
            diane "Aku suka menggoda vagina kecilmu yang basah, {b}[deb_name]{/b}...{w=2}{nw}"

        else:
            diane "Apakah kamu akan melakukan cum untukku?{w=1.5{nw}"

            debbie "Ya!!!{w=1}{nw}"


    elif animcounter == 2 and rng <= .66:
        if slow:
            diane "Hmm.{w=1}{nw}"

            diane "Anda menyukainya?{w=1}{nw}"

            debbie "Y-ya.{w=1}{nw}"

            diane "Kamu suka kalau memek kita bergesekan?{w=2}{nw}"

            debbie "Ya.{w=1}{nw}"

            pause 1
            diane "Katakan padaku kamu menyukainya!{w=1.5{nw}"

            debbie "Saya menyukainya!{w=1}{nw}"

            diane "Ayo sayang... kamu bisa melakukan yang lebih baik dari itu...{w=2}{nw}"

            debbie "Ahh, aku suka kalau memek kami bergesekan, {b}Diane{/b}!{w=2}{nw}"

            diane "Sial, aku juga!{w=1}{nw}"

        else:
            debbie "Ngh, tuhan!{w=1}{nw}"

            debbie "Saya semakin dekat, {b}Diane{/b}!{w=1.5{nw}"

            diane "Saya juga!{w=1}{nw}"

            pause
            debbie "Fuuuuck!!{w=1}{nw}"

        pause 1

    return


label scene_debbie_diane_bedroom.cum:
    debbie "Ahh, {b}Diane{/b}!!"

    debbie "aku akan keluar!!"

    diane "Sperma denganku!!"

    pause
    diane "Aku cinta kamu, {b}[deb_name]{/b}!"

    diane "Anda adalah sahabat saya di seluruh dunia!"

    debbie "aku juga mencintaimu!!"

    show debbie_body_b_sex_lesb_cum as animation
    diane "NGGHHH!!!" with flash
    debbie "NGGHHH!!!"

    pause
    show debbie_body_b_sex_lesb_fall as animation with dissolve
    diane "Haah... Haah..."

    pause
    diane "Yah, itu tadi-"

    pause
    debbie "Berat?"

    diane "Hehe, ya."

    debbie "Hehehe!"

    return


label scene_debbie_diane_bedroom.repeat:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_debbie.set('sex speed', 1 / 8.)

    scene location_home_debbiesidebed_lesb
    call scene_debbie_diane_bedroom.animate
    with fade
    call scene_debbie_diane_bedroom.loop
    call scene_debbie_diane_bedroom.cum
    return


label scene_debbie_diane_bedroom.replay:
    jump scene_debbie_diane_bedroom.repeat


screen scene_debbie_diane_bedroom_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Climax') action Return(True)

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_debbie.set, 'sex speed',
                                 1 / (1 / M_debbie.get('sex speed') - 2)),
                        Return(False))
                sensitive M_debbie.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_debbie.set, 'sex speed',
                                 1 / (1 / M_debbie.get('sex speed') + 2)),
                        Return(False))
                sensitive M_debbie.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
