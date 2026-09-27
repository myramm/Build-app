label scene_nadya_blowjob:
    call scene_nadya_blowjob.stage
    nadya "Wow." (show_native="Ukh ty.")
    show nadya a_wiggle
    pause
    nadya "Ini ayam yang cantik."

    anon "Kamu juga sangat cantik."

    show nadya -a_wiggle
    nadya "Ya, ini benar."

    call scene_nadya_blowjob.insert
    anon "!!!"
    anon "Oh halo!"

    call scene_nadya_blowjob.animate
    pause
    anon "Hmm, rasanya menyenangkan."

    pause
    nadya "{i}*Sluuuurp*{/i}"

    anon "Haah!"

    pause
    anon "Anda benar-benar tahu apa yang Anda lakukan di bawah sana!"

    nadya "Mhmm."

    pause
    anon "Aku semakin dekat!"

    hide animation
    show nadya b_sex_bj_pre
    with {'master': dissolve}
    nadya "Tidak."

    show nadya b_sex_bj_after f_disgusted_high with {'master': dissolve}
    anon "Hmm?"

    anon "Kenapa kamu berhenti?"

    nadya "Anda belum keluar."

    nadya f_sexy_high "Aku ingin kau bercinta dulu."

    anon "Oh, benar... ya."

    anon "Saya bisa melakukan itu."

    return


label scene_nadya_blowjob.stage:
    scene location_warehouse_office_bj
    show nadya b_sex_bj_pre
    with fade
    return


label scene_nadya_blowjob.insert:
    show nadya b_sex_bj_anim01 with dissolve
    return


label scene_nadya_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_nadya.set('sex speed', .10)
    hide nadya
    show nadya_blowjob_anim as animation
    with dissolve
    return


label scene_nadya_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show nadya_blowjob_anim as animation with dissolve
                $ animated = True
            pause 5
            call scene_nadya_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'nadya_blowjob_anim {}'.format(pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_nadya_blowjob.dialogue
        $ animcounter += 1
    call screen scene_nadya_blowjob_controls
    if not _return:
        jump scene_nadya_blowjob.loop
    return _return


label scene_nadya_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 75:
        anon "Mmm, rasanya menyenangkan.{w=1}{nw}"

    elif animcounter == 1 and randomizer() > 75:
        nadya "{i}*Sluuuurp*{/i}{w=1}{nw}"

        anon "Haah!{w=1}{nw}"

    elif animcounter == 1 and randomizer() > 75:
        anon "Oh, {b}Nadya{/b}!{w=1}{nw}"

        nadya "Hmm.{w=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        anon "Ya, begitu saja.{w=1}{nw}"

        nadya "{i}*Sluuuurp*{/i}{w=1}{nw}"

        anon "Ya Tuhan!{w=1}{nw}"

    return


label scene_nadya_blowjob.repeat:
    call scene_nadya_blowjob.stage
    nadya "Wow." (show_native="Ukh ty.")
    show nadya a_wiggle
    pause
    nadya "Halo, ayam cantik."

    nadya "Senang bertemu denganmu lagi."

    anon "Hehe."

    nadya -a_wiggle "Mari kita lihat bagaimana selera Anda hari ini."

    call scene_nadya_blowjob.insert
    anon "!!!"
    anon "Oh halo!"

    call scene_nadya_blowjob.animate
    pause
    anon "Hmm, rasanya menyenangkan."

    pause
    nadya "{i}*Sluuuurp*{/i}"

    anon "Haah!"

    pause
    anon "Oh, {b}Nadya{/b}!"

    nadya "Mhmm."

    pause
    anon "Ya, begitu saja."

    nadya "{i}*Sluuuurp*{/i}"

    anon "Ya Tuhan!"

    pause
    call scene_nadya_blowjob.loop
    anon "Aku semakin dekat!"

    pause
    anon "aku tidak bisa-"

    pause
    hide animation
    show nadya b_sex_bj_cum
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."

    show nadya a_wipe b_sex_bj_after f_surprised_cum_low with {'master': fastdissolve}
    nadya @ -m_talk "!!!"
    pause
    show nadya b_sex_bj_spit with {'master': dissolve}
    nadya "{i}*Ptooey*{/i}"

    pause
    show nadya a_idle b_sex_bj_after f_disgusted_closed with {'master': dissolve}
    nadya "Berdarah!"

    nadya f_disgusted_high "aku tidak suka rasanya..."

    anon "Oh?"

    nadya "Ayam itu bagus tapi air maninya tidak begitu..."

    nadya "... Sangat menjijikkan!"

    anon "Hehe, maaf."

    nadya f_sexy_high "Tidak apa-apa."

    nadya "Aku masih menikmati menghisap ayam cantikmu."

    pause
    return


label scene_nadya_blowjob.replay:
    jump scene_nadya_blowjob.repeat


screen scene_nadya_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('cum')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_nadya.get('sex speed') < .10
            textbutton _('Faster »'):
                action (Function(M_nadya.set,
                                 'sex speed',
                                 M_nadya.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_nadya.get('sex speed') > .041
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
