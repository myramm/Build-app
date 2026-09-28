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
    roz "Mmm."
    show roz_mc_face_bj normal_talk
    anon "OH GOD!!!"
    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Your mouth is amazing!"
    anon "{i}*Sluuuuuurp*{/i}"
    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Haah!"
    show roz_mc_face_bj normal
    roz "{i}*Glllcck*{/i}"
    pause
    show roz_mc_face_bj normal_talk
    anon "Don't stop!"
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
        anon "Holy crap!{p=1}{nw}"
        show roz_mc_face_bj normal
    if animcounter == 1 and randomizer() > 50:
        roz "{i}*Slurp*{/i}{p=1}{nw}"
    if animcounter == 2 and randomizer() > 50:
        roz "{i}*Glllcck*{/i}{p=1}{nw}"
    if animcounter == 3 and randomizer() > 50:
        show roz_mc_face_bj normal_talk
        anon "I'm getting close...{p=2}{nw}"
        if M_roz.get("sex speed") > 0.061:
            $ M_roz.set("sex speed", M_roz.get("sex speed") - 0.03)
        anon "Oh my god!{p=1}{nw}"
        show roz_mc_face_bj normal
    return

label scene_roz_blowjob.finish:
    show roz_mc_face_bj normal_talk
    anon "Haah!"
    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "I'm gonna-"
    anon "OH, I'M GONNA-"
    show roz_mc_face_bj normal
    pause
    hide roz_bj
    hide roz_mc_face_bj
    show roz_mc_body_bj cum
    anon "HNNGGG!!!" with flash
    pause
    roz "{i}*Gulp*{/i}"
    pause
    if randomizer() > 50:
        roz "Hehe, good boy."
    else:
        roz "Hehe, delicious."
    return


label con02_scam_roz_blowjob_intro:
    roz "{i}*Sluuuuuurp*{/i}"
    show roz_mc_face_bj normal_talk
    anon "OH GOD!!!"
    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "We shouldn't be-"
    anon "This isn't-"
    show roz_mc_face_bj normal
    roz "{i}*Glllcck*{/i}"
    pause
    show roz_mc_face_bj normal_talk
    anon "This-"
    anon "THIS FEELS AMAZING!"
    show roz_mc_face_bj normal
    pause
    roz "Mmm."
    show roz_mc_face_bj normal_talk
    anon "WOW!!"
    show roz_mc_face_bj normal
    pause
    show roz_mc_face_bj normal_talk
    anon "Oh my god, keep doing that!"
    anon "Keep doing that!!"
    show roz_mc_face_bj normal
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
