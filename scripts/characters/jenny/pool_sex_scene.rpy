label jenny_pool_sex_intro:
    scene expression "backgrounds/location_home_backyard_pool_sex.jpg"
    show jenny_pool_sex pre
    show jenny_pool_sex_face normal_talk_down
    show overlay_o_water zorder 100
    with fade
    jenny "Pastikan saja kamu tetap menundukkan kepala, aku tidak ingin {b}[deb_name]{/b} melihat kita!"

    show jenny_pool_sex_face normal_down
    anon "Saya akan!"

    show jenny_pool_sex insert with dissolve
    anon "Wah, rasanya aneh di dalam air.."

    show jenny_pool_sex_face normal_talk_down
    jenny "Diam dan turun lebih rendah, bodoh!"

    show jenny_pool_sex_face normal_down
    anon "Aku tidak bisa turun lebih rendah, airnya-"

    hide jenny_pool_sex_face normal_down
    show jenny_pool_sex 1
    anon "!!!" with hpunch
    $ M_jenny.set('pool_clothes', True)
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_pool_sex", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0) with dissolve
    pause
    jenny "Hmm, sial!"

    anon "Berhenti, kamu mendorongku ke bawah!"

    jenny "Ssst!!"

    anon "{i}*Bllgggh*{/i}"

    pause
    anon "{b}[jen_name]{/b} Anda berangkat-"

    anon "{i}*Bllgghhrrghhh*{/i}"

    jenny "Berhentilah membuat banyak keributan!"

    anon "Anda menenggelamkan saya!"

    jenny "Oh, aku bukan kamu sayang besar!"

    pause
    anon "{i}*Bllggh*{/i}"

    anon "{i}*Batuk* *Batuk*{/i}"

    jenny "Mm, aku sangat menyukai penis besar ini... Sangat!!"

    pause
    jenny "Ayo, setubuhi aku lebih cepat, {b}[firstname]{/b}!"

    anon "saya sedang mencoba!"

    pause
    jenny "Sialan!!"

    jenny "Aku akan keluar!"

    anon "aku ke-"


label jenny_pool_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get('pool_clothes'):
                    show expression AnimatedImage("jenny_pool_sex", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_pool_sex_naked", [1,2,3,4,5,6,7,8,9,10], M_jenny) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_pool_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get('pool_clothes'):
                    show expression "jenny_pool_sex {}".format(pose_list[pose_counter]) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_pool_sex_naked {}".format(pose_list[pose_counter]) as jenny_pool_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_pool_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_pool_sex_options

label jenny_pool_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!!{p=1}{nw}"

        anon "{i}*Blghrghhh*{/i}!!!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        anon "{i}*Bllgggh*{/i}{p=1}{nw}"

        jenny "Sangat dalam!{p=1}{nw}"

        jenny "Oh, persetan denganku!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUUUCK!!!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        anon "{i}*Bllgghhrrghhh*{/i}{p=1}{nw}"

    return

label jenny_pool_sex_cum_inside:
    jenny "Ya Tuhan, ya Tuhan, Ya Tuhan!!"

    jenny "Jangan berhenti!!"

    jenny "NGGHHH!!!"

    show jenny_pool_sex cum
    anon "HNNGGG!!!" with flash
    show jenny_pool_sex cum2
    show xray_jenny_pool:
        align (0,0)
    pause
    hide xray_jenny_pool
    show jenny_pool_sex pullout1
    show jenny_pool_sex_face normal_down
    with dissolve
    pause
    show jenny_pool_sex after
    show jenny_pool_sex_face normal_talk_down
    show player_jenny_pool pullout2
    with dissolve
    jenny "Haah... Haah..."

    jenny "Itu luar biasa!"

    call call_pregnancy_minigame ("jenny_pool_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_pool_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_backyard_pool_day_closeup.jpg"
    show anon f_tired b_pool
    show jenny b_pool f_upset_down
    with fade
    anon "Saya pikir saya akan pingsan..."

    show jenny f_angry
    jenny "Apakah kamu masuk ke dalam diriku?!"

    anon "Aku bahkan tidak tahu, {b}[jen_name]{/b}... Hidupku berkelebat di depan mataku!"

    show jenny f_eyeroll
    jenny "Oh, berhentilah bersikap dramatis..."

    show jenny f_angry
    jenny "Aku bersumpah, jika aku hamil, aku akan membunuhmu!"

    anon "{b}[jen_name]{/b}, aku bahkan tidak bisa-"

    anon "Aku perlu berbaring atau apalah..."

    hide anon with dissolve
    pause
    show jenny f_angry
    jenny "Pakai celanamu sebelum masuk ke dalam, tolol!"

    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["16_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ game.main()

label jenny_pool_sex_cum_outside:
    jenny "Ya Tuhan, ya Tuhan, Ya Tuhan!!"

    jenny "Jangan berhenti!!"

    jenny "NGGHHH!!!"

    show jenny_pool_sex pullout1
    show jenny_pool_sex_face normal_down
    with dissolve
    pause
    show jenny_pool_sex after
    show jenny_pool_sex_face normal_down
    show player_jenny_pool flying_cum
    anon "HNNGGG!!!" with flash
    show player_jenny_pool pullout3 with dissolve
    pause
    show jenny_pool_sex_face normal_talk_down
    jenny "Haah... Haah..."

    jenny "Itu luar biasa!"

    scene expression "backgrounds/location_home_backyard_pool_day_closeup.jpg"
    show anon f_tired b_pool
    show jenny b_pool f_upset_down
    with fade
    anon "Saya pikir saya akan pingsan..."

    show jenny f_gross
    jenny "Eww, air manimu melayang di sekitarku!"

    anon "Y-ya, maaf... Hidupku berkelebat di depan mataku!"

    jenny "Oh, berhentilah bersikap dramatis..."

    jenny "Akulah yang merendam jus bolamu di sini!"

    anon "{b}[jen_name]{/b}, aku bahkan tidak bisa-"

    anon "Aku perlu berbaring atau apalah..."

    hide anon with dissolve
    pause
    show jenny f_gross
    jenny "Pakai celanamu sebelum masuk ke dalam, tolol!"

    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["16_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
