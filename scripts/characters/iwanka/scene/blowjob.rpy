label scene_iwanka_blowjob(venue='basement', outfit='dress'):
    call scene_iwanka_blowjob.stage
    anon "Haah!"

    call scene_iwanka_blowjob.animate
    iwanka "{i}*Sluuuurp*{/i}"

    pause
    erik "Bung, ini gila sekali!"

    erik "Aku sedang mengadakan pesta di rumahku sekarang, dan sahabatku di seluruh dunia, {b}[firstname]{/b}..."

    erik "... Apakah penisnya dihisap oleh putri walikota!"

    pause
    erik "Lihat, itu {b}[firstname]{/b} itu kontol!"

    pause
    erik "Dan itu adalah {b}Iwanka{/b}."

    erik "Sapa guildku, {b}Iwanka{/b}."

    iwanka "Baiklah!"

    iwanka "{i}*Gllllcck*{/i}"

    pause
    anon "{b}Erik{/b}, bisakah kamu menyimpannya?"

    anon "Ini sudah cukup canggung tanpamu-"

    anon "!!!"
    anon "Ya Tuhan, di sana!"

    pause
    erik "Tidak mungkin, kawan!"

    erik "Setiap juru kamera yang baik tahu bahwa Anda tidak akan berhenti merekam sampai Anda mendapatkan uang!"

    anon "Grr!"

    pause
    iwanka "MM."

    erik "Matamu sungguh indah, {b}Iwanka{/b}!"

    erik "Saya tidak menyadarinya sampai saat ini."

    iwanka "Terima kasih!"

    pause
    call scene_iwanka_blowjob.loop
    anon "Aku semakin dekat!"

    erik "Anda dengar itu, {b}Iwanka{/b}?"

    erik "Saatnya menghasilkan uang!"

    iwanka "Mhmm."

    pause
    anon "Ini dia!"

    hide animation
    show iwanka b_bj f_cum a_cum
    anon "HNNGGG!!!" with flash
    pause
    show iwanka f_normal o_cum a_after with dissolve
    erik "Wow, kamu terlihat seperti Hamako setelah sesi pertamanya dengan gurita..."

    iwanka @ f_laugh "hehe!"

    erik "... Hanya saja, sperma ini berwarna putih dan bukan biru."

    iwanka "Dan dia mengisi semua lubangnya..."

    iwanka "... Sejauh ini saya hanya mendapatkan satu."

    return


label scene_iwanka_blowjob.stage:
    if venue == 'basement':
        scene location_erik_basement_back_bj
        show iwanka b_bj a_pre
        show rec zorder 1
    else:
        if venue == 'yacht':
            scene location_boat_interior_evening_bed_bj
        else:
            scene location_rump_iwanka_day_bj
        show iwanka b_bj_naked a_pre
    with fade
    return


label scene_iwanka_blowjob.animate:
    python:
        anim_toggle = True
        animated = True
        M_iwanka.set('sex speed', .10)
    hide iwanka
    show expression 'iwanka_blowjob_{}'.format(outfit) as animation
    with dissolve
    return


label scene_iwanka_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show expression 'iwanka_blowjob_{}'.format(outfit) as animation with dissolve
                $ animated = True
            pause 5
            call scene_iwanka_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'iwanka_sex_bj_anim_{} {}'.format(outfit, pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_iwanka_blowjob.dialogue
        $ animcounter += 1
    call screen scene_iwanka_blowjob_controls
    if not _return:
        jump scene_iwanka_blowjob.loop
    return _return


label scene_iwanka_blowjob.dialogue:
    if animcounter == 0 and randomizer() > 75:
        anon "Oh, rasanya menyenangkan...{p=2}{nw}"

    if animcounter == 1 and randomizer() > 75:
        anon "Saya suka cara Anda menggunakan tangan Anda.{p=2}{nw}"

    elif animcounter == 1 and randomizer() > 75 and venue == 'basement':
        erik "Ini LUAR BIASA!{p=1}{nw}"

    if animcounter == 2 and randomizer() > 75:
        iwanka "Mmhmm.{p=1}{nw}"

    elif animcounter == 2 and randomizer() > 75:
        anon "Haah, mulutmu terasa luar biasa!{p=2}{nw}"

        iwanka "{i}*Gllllcck*{/i}{p=1}{nw}"

    return


label scene_iwanka_blowjob.repeat(venue, outfit='naked'):
    call scene_iwanka_blowjob.stage
    iwanka "Anda tahu, Anda beruntung saya sudah banyak berlatih melakukan ini di perguruan tinggi."

    iwanka "Belum pernah yang sebesar ini, ingatlah."

    anon "Oh?"

    iwanka "Ini sangat mengesankan."

    call scene_iwanka_blowjob.animate
    pause
    iwanka "MM."

    anon "Oh, rasanya luar biasa."

    pause
    anon "Haah!"

    iwanka "{i}*Sluuuurp*{/i}"

    pause
    anon "Anda tahu, {b}Erik{/b} benar tentang mata Anda..."

    anon "... Mereka sangat cantik."

    iwanka "Terima kasih!"

    pause
    iwanka "{i}*Gllllcck*{/i}"

    anon "Wow, saya tidak tahu bagaimana Anda memahaminya begitu dalam!"

    call scene_iwanka_blowjob.loop
    anon "Aku semakin dekat!"

    iwanka "MM."

    pause
    anon "Apakah Anda menginginkannya di wajah Anda lagi?"

    iwanka "Mhmm!!"

    hide animation
    show iwanka b_bj_naked f_cum a_cum
    anon "HNNGGG!!!" with flash
    pause
    show iwanka f_normal o_cum a_after with dissolve
    anon "Haah... Haah..."

    iwanka "Nah, bagaimana penampilanku?"

    anon "Berantakan."

    iwanka "hehe!"

    iwanka "Andai saja ayahku bisa melihatku sekarang."

    iwanka "Dia akan sangat marah."

    anon "Ya, dia mungkin akan membunuhku."

    iwanka "Oh, dia pasti akan membunuhmu."

    return


label scene_iwanka_blowjob.basement:
    call scene_iwanka_blowjob
    return

label scene_iwanka_blowjob.yacht:
    call scene_iwanka_blowjob.repeat ('yacht')
    return

label scene_iwanka_blowjob.bedroom:
    call scene_iwanka_blowjob.repeat ('bedroom')
    return


label scene_iwanka_blowjob.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['iwanka']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_boat_bridge) with fade
        menu:
            "Ruang bawah tanah (Video)" if 'basement' in variants:
                jump scene_iwanka_blowjob.basement

            "kapal pesiar" if 'yacht' in variants:
                jump scene_iwanka_blowjob.yacht

            "Kamar tidur" if 'bedroom' in variants:
                jump scene_iwanka_blowjob.bedroom
    else:

        jump expression 'scene_iwanka_blowjob.{}'.format(next(iter(variants)))

    return


screen scene_iwanka_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('cum')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_iwanka.set,
                                 'sex speed',
                                 M_iwanka.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_iwanka.get('sex speed') < .10
            textbutton _('Faster »'):
                action (Function(M_iwanka.set,
                                 'sex speed',
                                 M_iwanka.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_iwanka.get('sex speed') > .041
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
