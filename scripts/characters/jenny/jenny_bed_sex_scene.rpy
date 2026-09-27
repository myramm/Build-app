label jenny_bed_night_button:
    $ player.go_to(L_home_sisbedroom)
    if not M_jenny.finished_state(S_jenny_give_cunni):
        call expression game.dialog_select("jenny_bed_night_pre_j17")
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.between_states(S_jenny_give_cunni, S_jenny_night_time_sex):
        call expression game.dialog_select("jenny_bed_night_j17_j20")
        $ player.go_to(L_home_hallway)
        $ game.main()
    elif M_jenny.pregnancy:
        call jenny_bed_night_pregnant
    else:
        call expression game.dialog_select("jenny_bed_night_sex_intro")
    $ game.main()

label jenny_bed_night_pre_j17:
    scene expression player.location.background_blur with None
    show anon f_surprised_teeth with dissolve
    anon "(Tidak mungkin aku mengganggunya!)"

    anon "(Dia akan membunuhku!)"

    hide anon with dissolve
    return

label jenny_bed_night_j17_j20:
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "(Kamu tahu, akhir-akhir ini hubungan kita menjadi lebih baik...)"

    anon @ -m_talk "(Mungkin dia tidak keberatan?)"

    show anon f_grin
    menu:
        "Lakukan itu.":
            call expression game.dialog_select("jenny_bed_night_do_it_j17")
        "Sebaiknya aku tidak melakukannya.":
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_do_it_j17:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg" with None
    show jenny b_sleep_side o_sleep_blanket a_side f_sleep_side_rolleye with None
    show anon b_sleep_climb
    with dissolve
    pause
    show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers
    show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
    show jenny o_empty
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
    with dissolve
    pause
    show anon b_sleep_cuddle o_empty
    hide expression "characters/anon/anon_arms_sleep_side_a_normal.png"
    with dissolve
    pause
    show jenny f_sleep_side_wake
    jenny "Hmm?"

    show jenny b_sleep_turn a_turn f_sleep_turn_angry o_sleep_panties with dissolve
    jenny "Apa yang-"

    anon "H-hai."

    pause
    show jenny a_turn_push
    show anon b_sleep_side o_sleep_side_boxers a_react f_sleep_side_shock
    jenny "WHAT THE FUCK?!" with hpunch
    scene expression player.location.background_blur
    show anon f_surprised_teeth b_underwear
    show jenny f_angry a_crossed
    with fade
    jenny "Serius, ada apa denganmu?!"

    anon f_sad "maafkan aku... aku-"

    jenny "Anda tidak boleh begitu saja menyelinap ke tempat tidur wanita saat dia sedang tidur, {b}[firstname]{/b}!"

    jenny "Itu sangat menyeramkan!"

    anon "Aku hanya berpikir mungkin-"

    show anon f_depressed
    jenny "Tidak, Anda jelas tidak berpikir!"

    jenny "Eugh, keluar saja!"

    anon f_sad @ -m_talk "..."
    hide anon with dissolve
    show jenny f_eyeroll
    jenny "pecundang sialan..."

    scene black with fade
    pause
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_sad_down with dissolve
    anon @ -m_talk "(Yah, itu mengerikan...)"

    anon @ -m_talk "(Mengapa menurutku itu ide yang bagus?)"

    anon @ -m_talk "( {i}*Sigh*{/i} Saya harap dia tidak memberi tahu {b}[deb_name]{/b} tentang ini... )"

    hide anon with dissolve
    return

label jenny_bed_night_better_not:
    show anon f_worried a_idle with dissolve
    anon @ -m_talk "(Ya, tidak...)"

    anon @ -m_talk "(Tidak ada gunanya membuatnya kesal.)"

    hide anon with dissolve
    return

label jenny_bed_night_sex_intro:
    if store._in_replay is not None:
        $ player.location = L_home_sisbedroom
        $ game.timer.tick(3)
    scene expression player.location.background_blur with None
    show anon f_thinking a_thinking with dissolve
    anon @ -m_talk "(Tentunya dia tidak akan marah padaku sekarang, kan?)"

    anon @ -m_talk "(Maksudku, dia naik ke tempat tidurKU di tengah malam... Kenapa aku tidak bisa melakukan hal yang sama? )"

    show anon f_grin
    menu:
        "Lakukan itu.":
            call expression game.dialog_select("jenny_bed_night_sex_do_it")
        "Sebaiknya aku tidak melakukannya." if store._in_replay is None:
            call expression game.dialog_select("jenny_bed_night_better_not")
    return

label jenny_bed_night_sex_do_it:
    if store._in_replay is not None or M_jenny.get("bed_sex_first_time"):
        $ M_jenny.set("bed_sex_first_time", False)
        scene expression "backgrounds/location_home_jennybedroom_bed.jpg" with None
        show jenny b_sleep_side o_sleep_blanket a_side f_sleep_side_sleeping with None
        show anon b_sleep_climb
        with dissolve
        pause
        show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers
        show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        pause
        show anon b_sleep_cuddle f_sleep_side_shy o_empty
        hide expression "characters/anon/anon_arms_sleep_side_a_normal.png"
        with dissolve
        pause
        show jenny f_sleep_side_wake
        jenny "Hmm?"

        show jenny b_sleep_turn a_turn f_sleep_turn_angry o_sleep_panties with dissolve
        jenny "{b}[firstname]{/b}?"

        anon "H-hai."

        pause
        jenny "Apa yang kamu lakukan?"

        anon "Uhh, mau tidur?"

        jenny "Pergilah ke tempat tidurmu sendiri, pecundang!"

        anon "Aduh, ayolah {b}[jen_name]{/b}... Kamu selalu naik ke tempat tidurku!"

        jenny "Ya, karena aku ingin bercinta... Bukan untuk berpelukan dan berliur di sekujur tubuhmu saat kamu mencoba untuk tidur."

        anon "aku tidak berliur..."

        show jenny b_sleep_side a_side f_sleep_side_tired with dissolve
        jenny "Ya benar."

        show jenny f_sleep_side_sleeping
        pause
        show jenny b_sleep_turn a_turn f_sleep_turn_normal with dissolve
        jenny @ -m_talk "..."
        jenny "Baiklah, cepatlah!"

        anon @ -m_talk "Hmm?"

        jenny "Saya lelah, {b}[firstname]{/b}!"

        jenny "Jadi, kalau kau ingin meniduriku, cepatlah lakukan itu... Kalau tidak, pergilah!"

        show jenny b_sleep_side a_side f_sleep_side_sleeping with dissolve
        show anon f_sleep_side_shock
        menu:
            "Oke.":
                anon f_sleep_side_shy "O-oke."

                pause
                anon "Hmm..."


                label jenny_bed_night_grope_in_bed:
                    show anon f_sleep_side_kiss b_empty_sleep_cuddle
                    show jenny b_empty
                    show jenny_arms_a_sleep_side_grope as anim_arms
                    show jenny b_sleep_side_grope a_empty f_empty as anim_body behind jenny
                    with dissolve
                    pause
                    jenny "MM."

                    show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
                    show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
                    hide anim_arms
                    hide anim_body
                    show jenny b_sleep_turn a_turn_remove_top1 f_sleep_turn_normal
                    with dissolve
                    pause
                    show jenny b_sleep_turn_shirtup a_turn_remove_top2
                    with dissolve
                    anon "..."
                    show jenny b_sleep_side_shirtup a_side f_sleep_side_normal with dissolve
                    pause
                    show anon f_sleep_side_kiss b_empty_sleep_cuddle o_empty
                    hide expression "characters/anon/anon_arms_sleep_side_a_normal.png"
                    show jenny b_empty f_sleep_side_enjoy
                    show jenny_arms_a_sleep_side_grope as anim_arms
                    show jenny b_sleep_side_grope_shirtup a_empty f_empty as anim_body behind jenny
                    with dissolve
                    pause
                    jenny "Oke, rasanya enak sekali..."

                    show jenny f_sleep_side_rolleye
                    show jenny_arms_a_sleep_side_grope as anim_arms
                    show jenny b_sleep_side_grope_hump_shirtup as anim_body
                    with dissolve
                    jenny "Ngghhh!"

                    pause
                    anon f_sleep_side_shy "Kamu senang aku sudah membangunkanmu?"

                    show jenny f_sleep_side_tired
                    jenny "Diam..."

                    show anon f_sleep_side_kiss
                    show jenny f_sleep_side_enjoy
                    pause
                    menu jenny_bed_night_whatcha_do:
                        "Melangkah lebih jauh.":
                            jump jenny_bed_night_go_further
                        "Melanjutkan.":
                            pause
                            jump jenny_bed_night_whatcha_do

            "Lupakan." if store._in_replay is None:
                show anon b_sleep_leave
                hide anim_arms
                hide anim_body
                show jenny b_sleep_turn a_turn f_sleep_turn_normal o_sleep_blanket
                hide expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png"
                with dissolve
                anon "Baiklah, lupakan saja..."

                hide anon with dissolve
                jenny "Dengan senang hati."

                $ player.go_to(L_home_hallway)
                $ game.main()
    else:
        scene expression "backgrounds/location_home_jennybedroom_bed.jpg" with None
        show jenny b_sleep_side o_sleep_blanket a_side f_sleep_side_sleeping with None
        show anon b_sleep_climb
        with dissolve
        pause
        show anon b_sleep_cuddle f_sleep_side_shy
        show jenny o_empty
        show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 3
        with dissolve
        show jenny f_sleep_side_wake
        jenny "Hmm?"

        show jenny b_sleep_turn a_turn f_sleep_turn_angry o_sleep_panties with dissolve
        jenny "{b}[firstname]{/b}?"

        anon "H-hai."

        pause
        jenny "Sialan ini lagi?"

        anon "Saya pikir kamu menyukainya?"

        jenny "Apa yang memberimu ide itu?"

        anon "J-jadi, kamu tidak menyukainya?"

        jenny "Itu bukan-"

        pause
        jenny "Sudahlah, cepatlah ya?!"

        show jenny b_sleep_side a_side f_sleep_side_sleeping with dissolve
        jump jenny_bed_night_grope_in_bed


label jenny_bed_night_go_further:
    show anon b_sleep_side f_sleep_side_shy o_sleep_side_boxers_boner
    show expression "characters/anon/anon_arms_sleep_side_a_normal.png"
    hide anim_arms
    hide anim_body
    show jenny b_sleep_turn_shirtup o_sleep_panties f_sleep_turn_normal a_turn
    with dissolve
    jenny "Baiklah, pemanasannya sudah cukup."

    show jenny a_turn_remove1 o_empty with dissolve
    pause
    show anon a_remove1_boner f_sleep_side_normal o_empty zorder 1
    show jenny a_turn_remove2 zorder 2
    with dissolve
    pause
    show anon b_sleep_side a_remove2
    show jenny a_turn o_sleep_panties_down
    with dissolve
    pause
    show anon a_insert o_sleep_side_boxers_down with dissolve
    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_sleep.jpg"
    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal_talk
    show player_jenny_sleeping_sex pre
    show jenny_sex_sleep_blanket
    with fade
    jenny "Masukkan ke dalam diriku."

    hide jenny_sleeping_sex_face
    show jenny_sleeping_sex insert
    hide player_jenny_sleeping_sex
    with dissolve
    anon "Baiklah."

    show jenny_sleeping_sex 1 with dissolve
    jenny "Fuuuuck..."

    $ anim_toggle = True
    $ animated = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
    jump jenny_jenny_bed_sex_loop

label jenny_jenny_bed_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_sleeping_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_sleeping_sex {}".format(pose_list[pose_counter]) as jenny_sleeping_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_jenny_bed_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_jenny_bed_sex_options

label jenny_jenny_bed_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        jenny "Mmm, rasanya menyenangkan...{p=1}{nw}"

    if animcounter == 1 and randomizer() < 25:
        anon "Mmhmm.{p=1}{nw}"

    if animcounter == 2 and randomizer() < 25:
        jenny "Ahhh!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 25:
        jenny "Oh, itu dia!{p=1}{nw}"

        jenny "Ya!{p=1}{nw}"

    return

label jenny_jenny_bed_sex_cum_outside:
    $ M_jenny.set("jenny_bed_cum_inside", False)
    jenny "Jangan berhenti!"

    anon "Aku akan keluar!"

    jenny "JANGAN BERHENTI!!"

    show jenny_sleeping_sex insert with dissolve
    jenny "JANGAN-"

    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face cum
    show player_jenny_sleeping_sex cum
    anon "HNNGGG!!!" with flash
    show jenny_sleeping_sex_face angry_talk
    jenny "Oh, apa-apaan ini, {b}[firstname]{/b}!"

    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after f_sleep_turn_angry
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show anon f_sleep_side_shy b_empty_sleep_cuddle
    with fade
    anon @ -m_talk "Hmm?"

    jenny "Eugh, itu ada di mana-mana!"

    jenny "Bagaimana aku bisa tidur sekarang?"

    anon "M-maaf..."

    jenny "Demi Tuhan..."

    pause
    jenny "Keluar!"

    anon "Apa?!"

    anon "Apakah kamu serius?"

    jenny "Ya, kamu menjijikkan!"

    jump jenny_bed_sex_night_end

label jenny_jenny_bed_sex_cum_inside:
    $ M_jenny.set("jenny_bed_cum_inside", True)
    jenny "Jangan berhenti!"

    anon "Aku akan keluar!"

    jenny "JANGAN BERHENTI!!"

    jenny "NGGHHH!!!"

    show jenny_sleeping_sex cum
    anon "HNNGGG!!!" with flash
    show xray_jenny_jenny_bed at Position (align=(0,0))
    show jenny_sleeping_sex cum2
    with dissolve
    pause
    hide xray_jenny_jenny_bed
    show jenny_sleeping_sex pullout
    with dissolve
    jenny "Wah!"

    show jenny_sleeping_sex default
    show jenny_sleeping_sex_face normal
    show player_jenny_sleeping_sex after
    with dissolve
    anon "Haah... Haah..."

    call call_pregnancy_minigame ("jenny_bed_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_bed_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_bed.jpg"
    show jenny b_sleep_after f_sleep_turn_angry
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent.png" zorder 1
    show anon f_sleep_side_shy b_empty_sleep_cuddle
    with fade
    jenny "Apakah kamu benar-benar masuk ke dalam diriku?"

    anon "Ya."

    jenny "Sialan, {b}[firstname]{/b}!"

    anon "Kamu bilang jangan berhenti..."

    jenny "Anda tahu, bukan itu maksud saya!"

    anon "Yah, aku minta maaf..."

    anon "Kami benar-benar menyukainya dan semuanya terasa begitu baik, saya-"

    jenny "{i}*Huh*{/i} Astaga..."

    jenny "Keluar saja!"

    anon "Apa?!"

    anon "Apakah kamu serius?"

    jenny "Ya, kamu menjijikkan!"

    jump jenny_bed_sex_night_end

label jenny_bed_sex_night_end:
    if M_jenny.get("dominance") > 0:
        show anon f_sleep_side_normal
        anon "Maukah kamu bersantai saja?"

        if M_jenny.get("jenny_bed_cum_inside"):
            anon "Semuanya akan baik-baik saja."

        else:
            anon "Ini tidak seperti kamu belum pernah meminum air maniku sebelumnya..."

        jenny "..."
        anon "Diam saja dan tidurlah, kita bisa mengatasinya besok pagi."

        show jenny f_sleep_turn_angry
        jenny "Bagus."

        jenny "... Brengsek."

    else:
        show anon f_sleep_side_shy
        anon "Ayo, {b}[jen_name]{/b}..."

        anon "Tidak bisakah kita tidur saja?"

        show jenny f_sleep_turn_angry
        jenny "Aku tidak ingin kamu mendengkur di telingaku sepanjang malam!"

        anon "Kaulah yang mendengkur!!!"

        jenny "Persetan denganmu!"

        pause
        jenny "Bagus."

        jenny "Dasar sayang!"

        anon "Terima kasih!"

        jenny "Eh..."

    scene location_home_jennybedroom_night_sleep with fade
    if _in_replay:
        pause
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["17_unlocked"] = True
    call popup ('sleep')
    jump jenny_bed_sex_sleeping

label jenny_bed_sex_sleeping:
    call sleep_lock_check
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_jenny)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
