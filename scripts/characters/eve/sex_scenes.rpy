label eve_sex_front_intro:
    if player.location == L_tattooparlor_tent:
        scene expression "backgrounds/location_tattoo_tent_sex_front.jpg"
    else:
        scene expression "backgrounds/location_tattoo_bedroom_sex_front.jpg"
    if _in_replay:
        $ player.go_to(L_tattooparlor_bedroom)
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
    show eve b_front_pre
    show eve_sex_front_face_mc normal_talk
    anon "Kemarilah!"

    show eve_sex_front_face_mc normal_down
    eve "!!!"
    if (not M_eve.get("sex_front_1st_time") or _in_replay) and not M_eve.get("biggus_dickus"):
        menu:
            "vagina!":
                label eve_girl_vag_front:
                $ M_eve.set("sex_front_anal", False)
                show eve b_front_insert
                show eve_sex_front_face_mc normal_down
                with dissolve
                eve "!!!"
                pause
                eve "Sial!"

                pause
                $ anim_toggle = True
                $ animated = True
                $ M_eve.set('sex speed', .12)
                hide eve
                hide eve_sex_front_face_mc
                show expression AnimatedImage("eve_sex_front", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                with dissolve
                pause
                eve "Ya Tuhan!"

                eve "Kamu begitu jauh di dalam diriku!"

                pause
                eve "Lebih sulit {b}[firstname]{/b}!"

                anon "Hmm?"

                eve "Persetan aku lebih keras!"

                jump eve_sex_front_loop
            "Dubur!":

                pass

    $ M_eve.set("sex_front_anal", not M_eve.get("biggus_dickus"))
    jump eve_anal_front

label eve_sex_back_intro:
    eve "Hehe, oke."

    label eve_sex_back_intro_replay:
    if player.location == L_tattooparlor_tent:
        scene expression "backgrounds/location_tattoo_tent_sex_back.jpg" with None
    else:
        scene expression "backgrounds/location_tattoo_bedroom_sex_back.jpg" with None
    if _in_replay:
        $ player.go_to(L_tattooparlor_bedroom)
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
    show eve b_back_pre
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_back o_pre_alt
    with dissolve
    pause
    anon "Anda siap?"

    eve "Y-ya, menurutku begitu."

    show eve b_back_insert
    hide eve_overlay_sex_back
    with dissolve
    eve "!!!"
    pause
    eve "Sial!"

    pause
    hide eve
    hide eve_overlay_sex_back
    $ M_eve.set('sex speed', .08)
    if M_eve.get("biggus_dickus"):
        show expression AnimatedImage("eve_sex_back_alt", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    else:
        show expression AnimatedImage("eve_sex_back", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    pause
    anon "Mmm, kamu sangat ketat..."

    eve "{i}* Merengek*{/i}"

    pause
    eve "Lebih sulit, {b}[firstname]{/b}..."

    anon "Hmm?"

    if M_eve.get("biggus_dickus"):
        eve "Persetan dengan pantatku lebih keras!"

    else:
        eve "Persetan aku lebih keras!"

    $ anim_toggle = True
    $ animated = True
    jump eve_sex_back_loop

label eve_anal_front:
    eve "hehe!"

    pause
    if M_eve.get("sex_front_1st_time"):
        if M_eve.get("biggus_dickus"):
            eve "Mmm, berikan padaku {b}[firstname]{/b}..."

            show eve b_front_insert
            show eve_sex_front_face_mc normal_down
            eve "{i}*Gasp*{/i}" with hpunch
            eve "Sial!"

            $ anim_toggle = True
            $ animated = True
            $ M_eve.set('sex speed', .12)
            hide eve
            hide eve_sex_front_face_mc
            show expression AnimatedImage("eve_sex_front_alt", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
            with dissolve
            pause
            eve "Astaga-"

            pause
            eve "Haah, persetan denganku!"

            eve "Persetan, {b}[firstname]{/b}!"

            pause
            eve "Ahhhh!"

            anon "Kamu sangat ketat!"

        else:
            eve "Mmm, persetan denganku, {b}[firstname]{/b}!"

            show eve b_front_insert_anal
            show eve_sex_front_face_mc normal_down
            with dissolve
            eve "T-tunggu, itu bukan-"

            hide eve
            hide eve_sex_front_face_mc
            show eve_sex_front_anal 1
            eve "{i}*Gasp*{/i}" with hpunch
            pause
            anon "{b}Malam{/b}?"

            anon "Ada apa?"

            eve "K-kamu berada di pantatku sekarang..."

            anon "Oh, sial... maafkan aku!"

            anon "aku tidak-"

            eve "Tidak apa-apa."

            eve "Terus berlanjut."

            anon "Anda yakin?"

            eve "Y-ya, aku ingin mencobanya."

            anon "Baiklah."

            pause
            $ anim_toggle = True
            $ animated = True
            $ M_eve.set('sex speed', .12)
            hide eve_sex_front_anal
            show expression AnimatedImage("eve_sex_front_anal", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
            with dissolve
            eve "!!!"
            eve "Aduh, aduh!"

            anon "Haruskah saya berhenti?"

            eve "Tidak, jangan berhenti!"

            pause
            eve "Sangat dalam, {b}[firstname]{/b}!"

            pause
            anon "Apakah sudah mulai terasa enak?"

            eve "Y-ya, menurutku begitu."

            pause
            eve "Cobalah lebih cepat."

            anon "Oke."

            $ M_eve.set('sex speed', .09)
            eve "Astaga-"

    else:
        label eve_girl_anal_front:
        if M_eve.get("biggus_dickus"):
            show eve b_front_insert
        else:
            show eve b_front_insert_anal
        show eve_sex_front_face_mc normal_down
        with dissolve
        eve "!!!"
        pause
        eve "{i}* Merengek*{/i}"

        pause
        $ anim_toggle = True
        $ animated = True
        $ M_eve.set('sex speed', .12)
        hide eve
        hide eve_sex_front_face_mc
        if M_eve.get("biggus_dickus"):
            show expression AnimatedImage("eve_sex_front_alt", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
        else:
            show expression AnimatedImage("eve_sex_front_anal", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
        with dissolve
        pause
        eve "Sial!"

        eve "Kamu begitu jauh di dalam pantatku!"

        pause
        eve "Lebih sulit {b}[firstname]{/b}!"

        anon "Hmm?"

        eve "Persetan aku lebih keras!"

    jump eve_sex_front_loop

label eve_sex_back_first_intro:
    scene expression "backgrounds/location_tattoo_bedroom_sex_back.jpg" with None
    show eve b_back_pre
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_back o_pre_alt
    with dissolve
    eve "Pelan-pelan saja, oke?"

    anon "Y-ya, oke."

    show eve b_back_insert
    hide eve_overlay_sex_back
    with dissolve
    eve "!!!"
    eve "Astaga-"

    anon "Apakah kamu baik-baik saja?"

    eve "Ya, itu hanya-"

    eve "Kamu sangat besar!"

    anon "Maaf."

    anon "Aku bisa berhenti jika kamu-"

    eve "TIDAK!"

    eve "... Beri aku waktu sebentar."

    pause
    eve "Fiuh."

    pause
    eve "Oke, kamu bisa mulai bergerak... Perlahan."

    anon "Baiklah."

    hide eve
    hide eve_overlay_sex_back
    $ M_eve.set('sex speed', .08)
    if M_eve.get("biggus_dickus"):
        show expression AnimatedImage("eve_sex_back_alt", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    else:
        show expression AnimatedImage("eve_sex_back", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    pause
    eve "{i}* Merengek*{/i}"

    pause
    anon "{b}Malam{/b}?"

    eve "saya baik-baik saja."

    if M_eve.get("biggus_dickus"):
        eve "Persetan, ini menyakitkan!"

        eve "Ooooowww!"

    else:
        eve "Anda sangat meregangkan saya!"

        eve "Ngghhh!"

    eve "Cobalah lebih cepat."

    $ M_eve.set('sex speed', .06)
    pause
    eve "{i}* Merengek*{/i}"

    pause
    anon "Apakah rasanya lebih baik?"

    eve "Y-ya, menurutku begitu."

    if M_eve.get("biggus_dickus"):
        eve "Pantatku terbakar!"

    else:
        eve "Ini sangat dalam!"

    $ M_eve.set('sex speed', .04)
    eve "!!!"
    anon "Kamu sangat ketat!"

    pause
    $ anim_toggle = True
    $ animated = True
    jump eve_sex_back_loop

label eve_sex_front_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_eve.get("biggus_dickus"):
                    show expression AnimatedImage("eve_sex_front_alt", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                elif M_eve.get("sex_front_anal"):
                    show expression AnimatedImage("eve_sex_front_anal", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("eve_sex_front", [1,2,3,4,5,6], M_eve) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_front_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                if M_eve.get("biggus_dickus"):
                    show expression "eve_sex_front_alt {}".format(pose_list[pose_counter]) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                elif M_eve.get("sex_front_anal"):
                    show expression "eve_sex_front_anal {}".format(pose_list[pose_counter]) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "eve_sex_front {}".format(pose_list[pose_counter]) as eve_sex_front at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_front_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_front_options

label eve_sex_front_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        eve "Haah, persetan denganku!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50 and (M_eve.get("sex_front_anal") or M_eve.get("biggus_dickus")):
        eve "Persetan, {b}[firstname]{/b}!{p=2}{nw}"

    if animcounter == 2 and randomizer() < 50:
        eve "Ahhhh!{p=1}{nw}"

    if animcounter == 3 and randomizer() > 50:
        eve "Saya semakin dekat...{p=2}{nw}"

    return

label eve_sex_front_cum_inside:
    eve "Jangan berhenti!"

    anon "aku tidak bisa-"

    pause
    eve "Aku akan keluar!"

    anon "Saya juga!"

    pause
    eve "{b}[firstname]{/b}!"

    eve "Jangan-"

    hide eve_sex_front
    show eve b_front_cum
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_front o_cumshot_alt
    elif M_eve.get("sex_front_anal"):
        show eve_overlay_sex_front o_cum_anal
    '{color=ff69b4}[character.eve] & [character.anon]{/color}' "NGGHHH!!!" with flash
    if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_anal"):
        show xray_eve_front:
            align (0,0)
    pause
    hide xray_eve_front
    if M_eve.get("sex_front_anal"):
        show eve b_front_after_anal
        show eve_overlay_sex_front o_pullout_anal
    else:
        show eve b_front_after
        show eve_overlay_sex_front o_pullout
    show eve_sex_front_face_mc normal
    with dissolve
    pause
    if not M_eve.get("sex_front_anal"):
        show eve_overlay_sex_front o_creampie with dissolve
    pause
    if not M_eve.get("biggus_dickus") and not M_eve.get("sex_front_anal"):
        call call_pregnancy_minigame ("eve_sex_front_cum_end", M_eve)
    jump eve_sex_front_cum_end

label eve_sex_front_cum_outside:
    eve "Jangan berhenti!"

    anon "aku tidak bisa-"

    pause
    eve "Aku akan keluar!"

    anon "Saya juga!"

    eve "{b}[firstname]{/b}!"

    eve "Jangan-"

    hide eve_sex_front
    if M_eve.get("sex_front_anal"):
        show eve b_front_after_anal
    else:
        show eve b_front_after
    show eve_sex_front_face_mc cum
    show eve_overlay_sex_front o_cumshot
    show eve_sex_front_face_mc normal_down
    anon "HNNGGG!!!" with flash
    show eve_overlay_sex_front o_cumshot3
    eve "NGGHHH!!!"

    pause
    jump eve_sex_front_cum_end

label eve_sex_front_cum_end:
    show eve_sex_front_face_mc normal_talk
    anon "Haah... Haah..."

    pause
    anon "Kamu baik-baik saja?"

    show eve_sex_front_face_mc normal
    eve "Hehehe!"

    if M_eve.get("biggus_dickus"):
        eve "aku berantakan!"

        show eve_sex_front_face_mc normal_talk
        anon "hehe!"

        show eve_sex_front_face_mc normal
    else:
        eve "Itu luar biasa!"

        show eve_sex_front_face_mc normal_talk
        anon "Y-ya, benar."

        show eve_sex_front_face_mc normal
        if M_eve.get("sex_front_1st_time"):
            eve "Kami pasti harus melakukannya lagi!"

    scene expression player.location.background_closeup
    show eve b_onbed_cuddle_naked f_happy_closed o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    pause
    if M_eve.get("sex_front_1st_time"):
        eve "Aku tidak percaya betapa nikmatnya rasanya saat kau meniduriku seperti itu..."

        anon "Saya senang Anda menyukainya."

        eve "Hehe, aku yakin begitu!"

        $ M_eve.set("sex_front_1st_time", False)
    else:
        eve "Mmm, kami sudah cukup mahir dalam hal itu."

        anon "Ya, menurutku begitu."

        eve "hehe!"

    pause
    if randomizer() > 50:
        eve "Hmm, aku tidak mau bergerak."

        anon "..."
    else:
        eve "Mmm, ini terasa luar biasa."

        anon "Memang benar."

    pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["05_unlocked"] = True
    jump eve_sex_true_end

label eve_sex_front_switcheroo:
    if M_eve.get("sex_front_anal"):
        hide eve_sex_front
        jump eve_girl_anal_front
    else:
        hide eve_sex_front
        jump eve_girl_vag_front

label eve_sex_back_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_eve.get("biggus_dickus"):
                    show expression AnimatedImage("eve_sex_back_alt", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("eve_sex_back", [1,2,3,4,5,6,7,8,9], M_eve) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_back_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                if M_eve.get("biggus_dickus"):
                    show expression "eve_sex_back_alt {}".format(pose_list[pose_counter]) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "eve_sex_back {}".format(pose_list[pose_counter]) as eve_sex_back at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_back_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_back_options

label eve_sex_back_hscene_dialog:
    if animcounter == 0 and randomizer() > 50:
        eve "Ya Tuhan!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        eve "{b}[firstname]{/b}, jangan berhenti!{p=2}{nw}"

    if animcounter == 2 and randomizer() > 50:
        eve "Haah, enak rasanya!{p=1}{nw}"

        eve "Jangan berhenti!{p=1}{nw}"

    if animcounter == 3 and randomizer() > 50:
        eve "Persetan denganku!{p=1}{nw}"

        eve "Persetan denganku, {b}[firstname]{/b}!{p=1}{nw}"

    return

label eve_sex_back_cum_inside:
    if randomizer() > 50:
        eve "Jangan berhenti!"

        anon "aku tidak bisa-"

        pause
    eve "Aku akan keluar!"

    anon "Saya juga!"

    eve "Jangan berhenti!"

    eve "Jangan-"

    eve "NGGHHH!!!"

    pause
    hide eve_sex_back
    show eve b_back_cum
    anon "HNNGGG!!!" with flash
    if not M_eve.get("biggus_dickus"):
        show xray_eve_back:
            align (0,0)
    pause
    hide xray_eve_back
    show eve b_back_insert
    show eve_overlay_sex_back o_pullout
    with dissolve
    pause
    show eve b_back_after
    if M_eve.get("biggus_dickus"):
        show eve_overlay_sex_back o_after_alt
    else:
        hide eve_overlay_sex_back
        call call_pregnancy_minigame ("eve_sex_back_end", M_eve)
    jump eve_sex_back_end

label eve_sex_back_cum_outside:
    eve "Aku akan keluar!"

    anon "Saya juga!"

    eve "Jangan berhenti!"

    eve "Jangan-"

    eve "NGGHHH!!!"

    pause
    hide eve_sex_back
    show eve b_back_cumshot
    if M_eve.get("biggus_dickus"):
        show expression "characters/eve/eve_overlay_sex_back_pre_o_alt.png"
    show eve_overlay_sex_back o_cumshot
    anon "HNNGGG!!!" with flash
    show eve_overlay_sex_back o_cumshot3
    pause
    jump eve_sex_back_end

label eve_sex_back_end:
    anon "Haah... Haah..."

    pause
    anon "Kamu baik-baik saja?"

    eve "Hehehe!"

    if M_eve.get("biggus_dickus"):
        eve "Butthole kecilku yang malang..."

    else:
        eve "Itu luar biasa!"

    anon "hehe!"

    scene expression player.location.background_closeup
    show eve b_onbed_cuddle_naked f_happy_closed o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    if M_eve.get("sex_back_1st_time"):
        eve "Mmm, kami pasti melakukannya lagi!"

        anon "Hehe, oke."

        pause
        if M_eve.get("biggus_dickus"):
            eve f_happy "Saya pikir saya akan berjalan-jalan dengan lucu besok..."

            anon "Heh, kupikir kamu menikmatinya?"

            eve "Oh, aku menyukainya!"

            eve "... Tapi kau benar-benar meniduriku dengan keras, dasar kasar!"

            anon "Baiklah, lain kali aku akan lebih berhati-hati."

            eve "Psh, kuharap tidak!"

            anon "Hmm?"

            eve "Rasanya luar biasa!"

        else:
            anon "Saya pikir seharusnya ada darah untuk pertama kalinya?"

            eve "Hmm?"

            anon "Kau tahu, di bawah sana..."

            eve "Oh benar."

            eve "Selaput dara saya pecah karena kecelakaan mobil orang tua saya."

            anon "Jadi begitu."

            eve f_happy "Maaf."

            anon "T-tidak, tidak ada yang perlu disesali!"

            anon "Aku hanya terkejut, itu saja..."

    else:
        eve "Mmm, kami sudah cukup mahir dalam hal itu."

        anon "Ya, menurutku begitu."

        eve "hehe!"

    show eve f_happy_closed
    eve "Mmm, ini terasa luar biasa."

    anon "Memang benar."

    pause
    if M_eve.get("sex_back_1st_time"):
        eve "Terima kasih telah menjadi yang pertama bagi saya, {b}[firstname]{/b}."

        anon "Hehe, tidak masalah."

        pause
        $ M_eve.set("sex_back_1st_time", False)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["06_unlocked"] = True
    jump eve_sex_true_end

label eve_sex_true_end:
    scene expression player.location.background_blur with None
    show eve b_undies f_happy
    show anon
    with dissolve
    eve "Saya berharap kamu bisa tinggal."

    anon "Ya, aku juga."

    pause
    anon "Sampai jumpa besok, oke?"

    eve "Y-ya, oke."

    hide anon
    show eve b_undies_kiss
    with dissolve
    pause
    show anon
    show eve b_undies f_happy
    with dissolve
    eve "Selamat malam, {b}[firstname]{/b}."

    anon @ a_wave "Selamat malam, {b}Malam{/b}."

    hide anon with dissolve
    $ game.timer.tick()
    $ player.go_to(L_map)
    $ game.main()

label eve_69:
    if _in_replay:
        $ player.go_to(L_tattooparlor_bedroom)
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
    if player.location == L_tattooparlor_tent:
        scene expression "backgrounds/location_tattoo_tent_sex_front.jpg"
    else:
        scene expression "backgrounds/location_tattoo_bedroom_sex_bj.jpg"
    show eve_sex_bj_mc_body
    show eve_sex_bj_mc_face pre
    if M_eve.get("biggus_dickus"):
        show eve b_sex_bj_pre o_pre_alt
    else:
        show eve b_sex_bj_pre
    with fade
    pause
    if randomizer() > 50:
        eve "Anda yakin Anda siap untuk ini?"

        anon "Saya selalu siap!"

    else:
        eve "Apakah kamu siap?"

        anon "Ya!"

    eve "Hehe, oke."

    eve "Ini aku datang."

    show eve b_sex_bj_talking o_empty
    hide eve_sex_bj_mc_body
    hide eve_sex_bj_mc_face
    with dissolve
    pause
    eve "!!!"
    if M_eve.get("biggus_dickus") and M_eve.get("69_1st_time"):
        eve "Wow, kamu mengambil semuanya!"

        anon "{b}Glllkkch{/b}!"

    elif M_eve.get("69_1st_time"):
        eve "Ya Tuhan, rasanya luar biasa!"

        anon "Dddthh entahlah?"

    else:
        eve "!!!"
        eve "{i}*Terkesiap*{/i}"

        pause
        eve "Kamu sangat pandai dalam hal ini!"

    eve "Ahhh!"

    $ anim_toggle = True
    $ animated = True
    $ M_eve.set('sex speed', .12)
    hide eve
    show expression AnimatedImage("eve_sex_bj", [1,2,3,4,5,6,7,8,9,10], M_eve) as eve_sex_bj at Position(xalign = 0.0, yoffset = 0)
    anon "!!!"
    jump eve_sex_bj_loop

label eve_sex_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("eve_sex_bj", [1,2,3,4,5,6,7,8,9,10], M_eve) as eve_sex_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "eve_sex_bj {}".format(pose_list[pose_counter]) as eve_sex_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_bj_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_bj_options

label eve_sex_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        eve "Hmm.{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        anon "{i}*Menyeruput*{/i}{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        eve "{i}*Gluulggh*{/i}{p=1}{nw}"

    if animcounter == 3 and randomizer() > 50:
        eve "{i}*Sluuurrp*{/i}{p=1}{nw}"

    return

label eve_sex_bj_cum:
    if M_eve.get("biggus_dickus"):
        anon "Hmm!"

        eve "MM."

        pause
        anon "Hmm!!"

        eve "Mmhmm."

    else:
        anon "Ya ampun!"

        anon "Mmy grrn krrrwwws!!"

        pause
        anon "Ya ampun!!!"

    pause
    anon "MMMMM!!!"

    eve "Hmm?"

    anon "HrrrNNGGG!!!" with flash
    hide eve_sex_bj
    show eve b_sex_bj_cum
    eve "!!!"
    pause
    show eve b_sex_bj_talking o_empty a_after f_after
    hide eve_sex_bj_mc_body
    hide eve_sex_bj_mc_face
    with dissolve
    pause
    eve f_swallow_after @ f_swallow -m_talk "{i}*Meneguk*{/i}"

    eve "Sial!"

    eve "NGGHHH!!!" with flash
    pause
    show eve f_normal
    eve "Haah... Itu tadi-"

    eve "Ya Tuhan..."

    anon "Hmm!!"

    pause
    eve f_after "Oh sial!"

    show eve_sex_bj_mc_body
    if M_eve.get("biggus_dickus"):
        show eve_sex_bj_mc_face after_alt
        show eve b_sex_bj_pre o_after_alt zorder 1
        with dissolve
        anon "!!!"
    else:
        show eve_sex_bj_mc_face after
        show eve b_sex_bj_pre zorder 1
        with dissolve
        anon "{i}*Terkesiap*{/i}"

    eve "Maafkan aku!"

    anon "{i}*Meneguk*{/i}"

    show eve_sex_bj_mc_face after
    anon "Haaah... Haaah..."

    eve "Apakah kamu baik-baik saja?!"

    anon "Saya kira demikian."

    if M_eve.get("biggus_dickus"):
        eve "Hehe, kamu sering datang!"

        anon "Y-ya, kamu juga melakukannya!"

    else:
        eve "Hehe, kamu berantakan!"

        anon "Y-ya, kamu juga!"


    if player.location == L_tattooparlor_tent:
        scene expression player.location.background_blur
    else:
        scene expression player.location.background_closeup
    show eve b_onbed_cuddle_naked f_happy_closed o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    if M_eve.get("69_1st_time"):
        eve "Mm, aku tidak percaya kita baru saja melakukan itu..."

    else:
        eve "Mm, itu luar biasa!"

    pause
    eve f_happy "Apakah kamu menyukainya?"

    if randomizer() > 50:
        anon "Ya, benarkah?"

        eve "Oh, aku menyukainya!"

    else:
        anon "Tentu saja!"

        eve f_happy_closed "hehe!"

    pause
    if M_eve.get("69_1st_time"):
        eve f_happy_closed "Kita harus melakukannya lagi suatu saat nanti..."

        $ M_eve.set("69_1st_time", False)
    pause
    anon "Ini sudah larut."

    anon "Aku harus segera pulang."

    eve f_happy @ f_thinking_down "Ah, aku belum mau bangun!"

    eve "Tidak bisakah kamu tinggal sedikit lebih lama lagi?"

    anon "Y-ya, oke, tapi sedikit saja."

    eve f_happy_closed "MM."

    eve "Aku suka saat kamu memelukku seperti ini..."

    pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["04_unlocked"] = True
    $ M_eve.trigger(T_eve_had_sixtynine)
    jump eve_HJ_end

label eve_sex_jerk_intro:
    $ player.go_to(L_tattooparlor_tent)
    scene expression player.location.background_blur with None
    if _in_replay:
        if persistent.eve_bulge_unlocked:
            show screen popup_trap with dissolve
            call screen empty()
            if _return:
                $ M_eve.set('biggus_dickus', '_alt')
            else:
                $ M_eve.set('biggus_dickus', '')
            hide screen popup_trap with dissolve
        else:
            $ M_eve.set('biggus_dickus', '')
        $ game.timer.tick(2)
    show anon b_onbed_sit f_laugh
    show eve b_onbed_dressed f_nervous
    with dissolve
    pause
    eve "Jadi..."

    eve f_sexy "Di sinilah kita, di tenda {b}Tuuku{/b} lagi..."

    anon f_normal @ -m_talk "Mmhmm."

    pause
    eve f_happy @ f_laugh "Saya sangat berharap {b}Odette{/b} menyelesaikan kesepakatan kali ini!"

    anon f_confused "Anda melakukannya?"

    eve "Ya."

    pause
    eve "Hehe, menurutku itu hal yang aneh untuk dikatakan, ya?"

    eve @ f_eyeroll "Astaga, aku sangat berharap {b}Odette{/b} berhasil memaku adikku malam ini..."

    anon @ f_laugh "Haha!"

    anon "Tidak, tidak apa-apa... Aku mengerti maksudmu."

    anon "Anda hanya ingin {b}Grace{/b} bahagia."

    eve "Ya, itu..."

    pause
    eve @ f_laugh "... Tapi juga, akhir dari semua ini diasingkan ke atap omong kosong!"

    anon "Hehe, tidak terlalu buruk..."

    eve "Pfft, akan jauh lebih baik di bawah, dengan TV dan tempat tidur..."

    pause
    eve "... Dan panas."

    anon f_flirt "Saya dapat memikirkan beberapa cara untuk menghangatkan Anda..."

    eve f_sexy "Oh ya?"

    anon "Ya."

    eve f_sexy @ f_laugh "Hmm, hehe!"

    pause
    eve a_remove1 "Kau tahu, itu sungguh manis, caramu membantu {b}Odette{/b} dan adikku hari ini..."

    anon "Y-ya?"

    show eve f_normal_down b_onbed_topless a_remove2 with dissolve
    eve @ -m_talk "Mmhmm."

    show eve f_sexy b_onbed_topless a_idle with dissolve
    eve "menurutku..."

    eve "Bahwa kamu, pantas mendapatkan hadiah."

    anon "{i}*Gulp*{/i} O-oke."

    show eve f_normal_down b_onbed_tanktop_remove1 with dissolve
    pause
    show eve b_onbed_tanktop_remove2 with dissolve
    show anon f_surprised
    pause
    show eve f_sexy b_onbed_tanktop with dissolve
    eve @ f_laugh "Kamu tahu, ini JAUH lebih menyenangkan sekarang karena aku tahu kamu baik-baik saja dengan semuanya."

    anon f_flirt "Uh-hah."

    anon "D-pastinya bersenang-senang..."

    eve @ f_laugh "Hehehe!"

    eve @ f_sexy "Haruskah saya melanjutkan?"

    menu:
        "Ya.":
            anon "Ya, tolong."

        "NERAKA YA!":
            anon f_skeptical "Apakah itu pertanyaan yang serius?"

            eve @ f_eyeroll "Tidak."

    show eve b_onbed_top_remove3 with dissolve
    pause
    show eve f_sexy b_onbed_panties with dissolve
    anon "!!!"
    eve "kamu suka?"

    anon "Oh, aku suka."

    anon "Saya sangat menyukainya!"

    eve @ f_laugh "hehe!"

    pause
    eve "Hmm, mungkin aku juga tidak membutuhkan celana dalam ini ya?"

    anon "Nuh-uh."

    eve "hehe!"

    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve

    if M_eve.biggus_dickus:
        anon "Hmm, apakah itu untukku?"

        eve "Ya."

        eve "Ini semua untukmu, {b}[firstname]{/b}!"

    else:
        anon "Mmm, bekas luka itu seksi sekali!"

        eve "Ya?"

        eve "Mungkin Anda harus melihat lebih dekat?"

    anon "!!!"
    anon "Beri aku waktu sebentar!"

    show anon b_onbed_sit_changing3 with fastdissolve
    pause .5
    show eve b_onbed_cuddle_naked f_happy o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "Itu tadi cepat!"

    show anon f_laugh
    pause
    hide anon
    show eve b_onbed_cuddle_naked_kiss
    with dissolve
    eve "MM."

    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "Ya Tuhan, aku suka menciummu!"

    anon "Juga."

    eve "hehe!"

    show eve b_onbed_cuddle_naked_kiss
    hide anon
    with dissolve
    pause
    pause
    show eve b_onbed_cuddle_naked
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "Anda benar."

    eve "Aku merasa jauh lebih hangat sekarang."

    anon "hehe."

    eve f_thinking_down "Hmm, saya pikir seseorang ingin keluar dan bermain..."

    anon @ -m_talk "Mmhmm."

    show eve a_jerk1 o_empty with dissolve
    eve "Besar sekali, {b}[firstname]{/b}..."

    pause
    anon "Anda masih takut akan hal itu?"

    eve "Sedikit."

    pause
    anon "Tidak apa-apa."

    anon "Mengapa kamu tidak membiarkan aku menjagamu saja?"

    eve f_happy @ -m_talk "Hmm?"

    jump eve_handjob

label eve_handjob:
    anon "Kemarilah."


    if player.location == L_tattooparlor_tent:
        scene location_tattoo_tent_sex_front
    else:
        scene expression player.location.background_closeup
    show eve b_front_pre
    show eve_sex_front_face_mc normal
    with fade
    eve "!!!"
    if M_eve.get("HJ_1st_time"):
        eve "A-apa yang kamu-"

        eve "Tidak ada seorang pun yang pernah-"

    else:
        eve "A-apa kamu yakin-"

    show eve_sex_front_face_mc normal_talk
    anon "Ssst."

    anon "Tidak apa-apa."

    show eve_sex_front_face_mc normal_down
    eve "{i}*Meneguk*{/i}"

    $ anim_toggle = True
    $ animated = True
    if M_eve.biggus_dickus:
        $ M_eve.set('sex speed', .08)
        show eve b_sex_jerk_alt
        show expression AnimatedImage("eve_sex_jerk_alt", [1,2,3,4,5,6,7,8,9,10,11], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
    else:
        $ M_eve.set('sex speed', .09)
        show eve b_sex_jerk
        show expression AnimatedImage("eve_sex_jerk", [1,2,3,4,5,6], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
    eve "{i}*Terkesiap*{/i}"

    pause
    show eve_sex_front_face_mc normal_talk
    anon "Apakah itu terasa oke?"

    if M_eve.get("HJ_1st_time"):
        anon "Haruskah saya melanjutkan?"

        show eve_sex_front_face_mc normal
        eve "Y-ya!"

    else:
        show eve_sex_front_face_mc normal
        eve "S-bagus sekali!"

    show eve_sex_front_face_mc normal_down
    jump eve_sex_jerk_loop

label eve_sex_jerk_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_eve.biggus_dickus:
                    show eve b_sex_jerk_alt
                    show expression AnimatedImage("eve_sex_jerk_alt", [1,2,3,4,5,6,7,8,9,10,11], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                else:
                    show eve b_sex_jerk
                    show expression AnimatedImage("eve_sex_jerk", [1,2,3,4,5,6], M_eve) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("eve_sex_jerk_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            if M_eve.biggus_dickus:
                $ pose_list = [1,2,3,4,5,6,7,8,9,10,11]
            else:
                $ pose_list = [1,2,3,4,5,6]
            $ poses_done = []
            while poses_done != pose_list:
                if M_eve.biggus_dickus:
                    show eve b_sex_jerk_alt
                    show expression "eve_sex_jerk_alt {}".format(pose_list[pose_counter]) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                else:
                    show eve b_sex_jerk
                    show expression "eve_sex_jerk {}".format(pose_list[pose_counter]) as eve_sex_jerk at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("eve_sex_jerk_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_jerk_options

label eve_sex_jerk_hscene_dialog:
    if animcounter == 0 and randomizer() > 75:
        eve "Nnngghh, lebih cepat!{p=1}{nw}"

    elif animcounter == 0 and randomizer() > 50:
        eve "Ya Tuhan, lebih cepat!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        eve "Ya Tuhan...{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        eve "Rasanya enak sekali, {b}[firstname]{/b}!{p=2}{nw}"

    if animcounter == 3 and randomizer() < 50:
        eve "Ahh!{p=1}{nw}"

    if animcounter == 4 and randomizer() < 50:
        eve "Nnngghh, jangan berhenti!!"

    return

label eve_sex_jerk_cum:
    eve "Astaga!"

    eve "Aku semakin dekat!"

    show eve_sex_front_face_mc normal
    anon "Sperma untukku!"

    show eve_sex_front_face_mc normal_down
    pause
    eve "{b}[firstname]{/b}!!!"

    pause
    hide eve_sex_jerk
    if M_eve.biggus_dickus:
        show eve b_sex_jerk_cum_alt
        show eve_sex_jerk_cumshot
    else:
        show eve b_sex_jerk_cum
    eve "NNGGGHHH!!!" with flash
    pause
    eve "Haah... Haah..."

    eve "Sialan."

    pause
    if player.location == L_tattooparlor_bedroom:
        scene expression player.location.background_closeup
    else:
        scene expression player.location.background_blur
    $ M_eve.set('sex speed', .4)
    if M_eve.biggus_dickus:
        show eve b_onbed_cuddle_naked f_happy o_dick
    else:
        show eve b_onbed_cuddle_naked f_surprised o_dick
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with fade
    if M_eve.biggus_dickus:
        if M_eve.get("HJ_1st_time"):
            eve "aku membuat kekacauan..."

        else:
            eve "aku membuat kekacauan lagi..."

        anon "Hehe, tidak apa-apa."

        eve "hehe!"

    else:
        if M_eve.get("HJ_1st_time"):
            eve "aku belum pernah-"

            pause
            eve "Sperma sekeras itu sebelumnya..."

        else:
            eve "I-itu tadi-"

            pause
            eve "Luar biasa..."

    show eve f_happy a_jerk1 o_empty with dissolve
    eve "Sekarang giliranku."


    if M_eve.get("HJ_1st_time") and not _in_replay:
        anon "Anda tidak perlu..."

        eve "T-tidak, aku ingin!"


        label eve_jerk_me_off_scotty:
        show eve a_jerk
        anon @ -m_talk "MM."

        pause
        eve "Apakah itu terasa enak?"

        anon "Rasanya sangat enak!"

        eve "hehe!"

        pause
        if M_eve.get("HJ_1st_time"):
            anon "Tanganmu begitu lembut dan mungil..."

            eve "Tidak, penismu sangat besar!"

            eve "Bagaimana Anda berjalan-jalan dengan benda ini?"

            pause
        else:
            eve "Aku suka bermain-main dengan penismu, {b}[firstname]{/b}."

            anon "K-kamu yakin?"

            eve "Ya, sangat banyak!"

            pause
            anon "Heh, menurutku dia juga menyukainya."

            eve "hehe!"

        show anon f_hurt
        eve "Apakah kamu semakin dekat?"

        anon @ f_disgusted_wince "Y-ya."

        pause
        eve "Sperma untukku, {b}[firstname]{/b}!"

        eve "Saya ingin melihatnya!"

        pause
        jump eve_sex_mc_jerk_loop
    else:

        menu:
            "Ya, tolong.":
                jump eve_jerk_me_off_scotty
            "Tidak, terima kasih.":

                anon "Anda tidak perlu..."

                eve "Tidak?"

                anon "Mari berpelukan sebentar."

                eve "K-kamu yakin?"

                eve "Saya suka melakukannya."

                anon "Ya, tidak apa-apa."

                anon "Hanya berbaring di sini bersamamu tidak masalah."

                eve f_happy_closed "Hmm, oke."

                jump eve_HJ_end

label eve_sex_mc_jerk_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show eve a_jerk
                $ animated = True
            pause 5
        else:
            show eve a_jerk1
            pause
            show eve a_jerk2
            pause
        call expression game.dialog_select("eve_sex_mc_jerk_hscene_dialog")
        $ animcounter += 1
    call screen eve_sex_mc_jerk_options

label eve_sex_mc_jerk_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        anon @ f_disgusted_wince "Ya Tuhan, ini terasa luar biasa!{p=2}{nw}"

    if animcounter == 1 and randomizer() > 50:
        anon @ f_disgusted_wince "Ahh!!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        anon @ f_disgusted_wince "Saya semakin dekat...{p=1}{nw}"

    return

label eve_sex_mc_jerk_cum:
    anon @ f_disgusted_wince "aku akan-"

    pause
    anon f_cough "Ini dia!"

    pause
    show eve a_jerk1 f_surprised o_cum
    anon f_disgusted_wince "HNNGGG!!!" with flash
    show anon f_flirt_low
    show eve f_happy o_cum3
    pause
    eve "Astaga..."

    anon "Haah... Haah..."

    eve "Itu air mani yang banyak..."

    anon "M-maaf."

    eve "Tidak, tidak apa-apa."

    pause
    show eve a_taste o_dick
    show expression "characters/eve/eve_overlay_onbed_cuddle_naked_o_cum3.png"
    with dissolve
    anon @ f_surprised_low "!!!"
    show eve a_chest with dissolve
    if M_eve.get("HJ_1st_time"):
        anon "A-apa kamu baru saja-"

        eve "hehe!"

        eve "Saya penasaran."

        anon "Dan?"

        show eve f_thinking_lip
        pause
        eve f_thinking_down "Ini sangat... Asin."

        anon @ f_laugh "Haha!"

        eve f_happy_closed "Haha!"

        pause
        show eve f_happy
        anon "Aku harus segera berangkat."

        eve "Mmm, kuharap kamu bisa tinggal."

        anon "Aku tahu, aku juga."

        anon "Tapi ini sudah larut."

        pause
        anon "Aku ingin tahu bagaimana kabar {b}Odette{/b} dan adikmu?"

        eve "Siapa yang peduli?"

        anon @ f_laugh "hehe!"

        anon "Oh, kamu tahu kamu penasaran!"

        eve "Mungkin sedikit..."

        pause
        eve "Tapi aku tidak mau bergerak!"

        anon @ f_laugh "hehe!"

        eve @ f_happy_closed "hehe!"

        pause
        eve f_thinking_down "{i}*Sigh*{/i} Saya kira semua hal baik harus diakhiri."

        anon "Selalu ada waktu berikutnya."

        eve f_happy "Aku menahanmu untuk itu!"

        anon "Tidak masalah."

        eve "Baiklah, ayo berpakaian dan periksa {b}Odette{/b} dan {b}Grace{/b}."

        eve "Lalu aku akan mengantarmu keluar."

        anon "Oke."

        scene black with fade
        pause
        $ M_eve.set("HJ_1st_time",False)
    else:
        anon "!!!"
        eve "hehe!"

        show eve f_thinking_lip

        label eve_HJ_end:
        pause
        scene black with fade
        pause
        if player.location == L_tattooparlor_tent:
            $ player.go_to(L_tattooparlor_roof)
        scene expression player.location.background_blur with None
        show eve f_happy
        if player.location == L_tattooparlor_bedroom and game.timer.is_dark():
            show eve b_pajamas
        show anon
        with dissolve
        anon "Itu bagus."

        eve "Sangat bagus!"

        eve "Aku berharap kamu bisa tinggal lebih lama, aku tidur seperti bayi ketika aku dalam pelukanmu."

        anon "Hehe, aku menyadarinya."

        eve @ f_laugh "hehe!"

        anon "Bagaimanapun, aku mungkin harus pergi."

        eve "Ya baiklah."

        hide anon
        if player.location == L_tattooparlor_bedroom and game.timer.is_dark():
            show eve b_pajamas_kiss:
                xoffset -400
        else:
            show eve b_dressed_kiss:
                xoffset -400
        with dissolve
        anon "!!!"
        if player.location == L_tattooparlor_bedroom and game.timer.is_dark():
            show eve b_pajamas:
                xoffset -200
        else:
            show eve b_dressed:
                xoffset -200
        show anon
        with dissolve
        eve "Kembalilah dan temui aku segera, oke?"

        anon "Saya akan."

        hide anon with dissolve
        $ renpy.end_replay()
        $ game.timer.tick()
        $ player.go_to(L_map)
        $ game.main()
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["03_unlocked"] = True
    $ renpy.end_replay()
    if M_eve.is_state(S_eve_make_up_dress_table):
        jump eve_sex_mc_jerk_cum_continued
    else:
        $ game.main()

label eve_sex_mc_jerk_cum_continued:
    $ player.go_to(L_tattooparlor_fire_escape)
    scene expression player.location.background_blur with None
    show anon
    show eve f_happy
    with dissolve
    eve "Kuharap mereka tidak sedang bercinta di tempat tidurku atau semacamnya..."

    anon @ f_surprised a_salute "!!!"
    anon "T-tidak."

    anon "Bukan di tempat tidurmu."

    eve @ f_surprised "!!!"

    scene location_tattoo_apartment_cutscene02
    show text _ ("It seemed our plan had worked, {b}Odette{/b} had finally won {b}Grace{/b}'s heart.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... Or at the very least, she'd won her way into {b}Grace{/b}'s bed for the evening.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Either way, I viewed it as a success.") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show anon f_flirt_grin
    show eve f_surprised
    with fade
    anon @ -m_talk "..."
    eve @ -m_talk "..."
    pause
    anon f_flirt "Jadi, uhh..."

    eve f_normal "Y-ya."

    anon "Kita mungkin tidak seharusnya menonton ini, ya?"

    eve f_sexy "Anda benar-benar berpikir mereka akan peduli?"

    anon @ a_thinking f_thinking "Y-yah, {b}Odette{/b} mungkin tidak akan..."

    eve @ f_eyeroll "Ya, adikku juga tidak akan melakukannya, percayalah."

    anon "Apakah ini berarti kamu tidur di tenda malam ini?"

    eve f_angry a_hip "Persetan!"

    eve f_normal "Aku akan menyelinap ke sana dan pergi ke kamarku."

    eve "Maksudku, lihat mereka... Mereka mungkin bahkan tidak akan memperhatikanku."

    anon "Y-ya."

    anon "... Lihatlah mereka."

    pause
    eve "mesum!"

    anon @ -m_talk "Hmm?"

    eve @ f_laugh "Haha!"

    anon "M-maaf."

    eve "Tidak apa-apa."

    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    anon "!!!"
    show eve b_dressed f_normal:
        xoffset 0
    show anon a_behind_head
    with dissolve
    eve "Sekali lagi terima kasih untuk semuanya hari ini."

    anon "Tidak masalah."

    eve "Sampai jumpa lagi, oke?"

    anon a_idle "Ya."

    eve f_sexy "Jangan berdiri di sini sepanjang malam sambil memperhatikan mereka juga!"

    anon "T-tidak, aku tidak akan melakukannya."

    anon "aku pergi."

    eve @ f_laugh "hehe!"

    anon @ a_wave "Selamat malam, {b}Malam{/b}."

    eve @ a_wave "Selamat malam."

    scene black with fade
    pause
    $ player.go_to(L_tattooparlor)
    scene expression player.location.background_blur with None
    show anon f_flirt with dissolve
    anon @ -m_talk "(Wow, malam yang luar biasa!)"

    anon @ -m_talk "( Begitu banyak yang terjadi dan sepertinya segalanya akan berubah menjadi lebih baik di sini. )"

    pause
    anon @ -m_talk "(Aku terlalu lelah untuk memikirkan hal itu sekarang, aku harus pulang.)"

    hide anon with dissolve
    $ M_eve.trigger(T_eve_dressed_table)
    $ game.timer.tick(3)
    $ player.go_to(L_map)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
