label scene_roz_blowjob:
    scene location_hospital_storage_bj
    show roz_mc_body_bj
    show roz_mc_face_bj normal
    $ anim_toggle = True
    $ animated = True
    $ M_roz.set('sex speed', .12)
    show expression AnimatedImage("roz_bj", [1,2,3,4,5,6,7,8,9,10], M_roz) as roz_bj at Position(xalign = 0.0, yoffset = 0)
    with fade
    if M_consuela.is_state(S_con02_scam):
        call con02_scam_roz_blowjob_intro
    else:
        call scene_roz_blowjob.intro
    jump scene_roz_blowjob.loop

label scene_roz_blowjob.intro:
    roz "MM."

    show roz_mc_face_bj normal_talk
    anon "YA TUHAN!!!"

    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Mulutmu luar biasa!"

    anon "{i}*Sluuuuuurp*{/i}"

    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Haah!"

    show roz_mc_face_bj normal
    roz "{i}*Gllllcck*{/i}"

    pause
    show roz_mc_face_bj normal_talk
    anon "Jangan berhenti!"

    show roz_mc_face_bj normal
    return

label scene_roz_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("roz_bj", [1,2,3,4,5,6,7,8,9,10], M_roz) as roz_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call scene_roz_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roz_bj {}".format(pose_list[pose_counter]) as roz_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_roz_blowjob.dialogue
        $ animcounter += 1
    call screen scene_roz_blowjob_options
    return

label scene_roz_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 50:
        show roz_mc_face_bj normal_talk
        anon "Sialan!{p=1}{nw}"

        show roz_mc_face_bj normal
    if animcounter == 1 and randomizer() > 50:
        roz "{i}*Menyeruput*{/i}{p=1}{nw}"

    if animcounter == 2 and randomizer() > 50:
        roz "{i}*Gllllcck*{/i}{p=1}{nw}"

    if animcounter == 3 and randomizer() > 50:
        show roz_mc_face_bj normal_talk
        anon "Saya semakin dekat...{p=2}{nw}"

        if M_roz.get("sex speed") > 0.061:
            $ M_roz.set("sex speed", M_roz.get("sex speed") - 0.03)
        anon "Ya Tuhan!{p=1}{nw}"

        show roz_mc_face_bj normal
    return

label scene_roz_blowjob.finish:
    show roz_mc_face_bj normal_talk
    anon "Haah!"

    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "aku akan-"

    anon "OH, AKU AKAN-"

    show roz_mc_face_bj normal
    pause
    hide roz_bj
    hide roz_mc_face_bj
    show roz_mc_body_bj cum
    anon "HNNGGG!!!" with flash
    pause
    roz "{i}*Meneguk*{/i}"

    pause
    if randomizer() > 50:
        roz "Hehe, anak baik."

    else:
        roz "Hehe, enak."

    return


label con02_scam_roz_blowjob_intro:
    roz "{i}*Sluuuuuurp*{/i}"

    show roz_mc_face_bj normal_talk
    anon "YA TUHAN!!!"

    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Kita tidak seharusnya-"

    anon "Ini bukan-"

    show roz_mc_face_bj normal
    roz "{i}*Gllllcck*{/i}"

    pause
    show roz_mc_face_bj normal_talk
    anon "Ini-"

    anon "INI TERASA LUAR BIASA!"

    show roz_mc_face_bj normal
    pause
    roz "MM."

    show roz_mc_face_bj normal_talk
    anon "WOW!!"

    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Ya Tuhan, terus lakukan itu!"

    anon "Terus lakukan itu!!"

    show roz_mc_face_bj normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
