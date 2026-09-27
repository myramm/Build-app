label jenny_couch_sex:
    if M_jenny.get("dominance") <= 0:
        hide jenny_couch_dick_rub
        show jenny a_dick3 f_sexy
        jenny "Baiklah, aku bosan dengan ini..."

        show anon f_couch_sit_right
        anon @ -m_talk "Hmm?"

        show anon a_boner zorder 1
        show jenny b_couch_remove zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_sexy a_rest o_couch_teasing with dissolve
        jenny "Kemarilah dan persetan denganku."

        anon "Apa?!"

        jenny "Anda mendengar saya."

        anon "T-tapi, {b}[deb_name]{/b} ada di sana!"

        jenny "Saya tahu, ini mengasyikkan! Bukan?"

        anon "T-tidak?"

        show jenny f_eyeroll
        jenny "{i}*Huh*{/i} Ya, benar!"

        show jenny f_sexy
        anon @ -m_talk "..."
        jenny "Jangan jadi banci."

        show jenny f_sexy_down
        jenny "Saya ingin penis sebesar itu!"

    else:
        show jenny f_sexy_down
        jenny "Apakah kamu semakin dekat?"

        anon f_couch_sit_down "Y-ya."

        show anon f_couch_sit_right
        hide jenny_couch_dick_rub
        show jenny a_dick3 f_sexy_down
        pause
        anon "Apa yang kamu lakukan?!"

        show jenny f_sexy
        jenny "aku bosan dengan ini..."

        pause
        jenny "Ayo bercinta!"

        anon "Hah?!"

        jenny "Anda mendengar saya."

        show anon a_boner zorder 1
        show jenny b_couch_remove zorder 0
        with dissolve
        pause
        show jenny b_couch_sit f_sexy a_rest o_couch_teasing with dissolve
        jenny "Aku ingin kamu ada di dalam diriku."

        anon "T-tapi, {b}[deb_name]{/b} ada di sana!"

        jenny "Jadi?"

        jenny "Saya bisa diam."

        anon "Ya benar."

        show jenny f_upset
        jenny "Ayolah?"

        anon @ f_couch_sit_down_surprised "!!!"
        anon "Apakah Anda baru saja mengatakannya?"

        show jenny f_eyeroll
        jenny "... Mungkin."

        show jenny f_sexy
        anon "Wow, kamu benar-benar menginginkannya."

        show jenny f_sexy_down
        jenny "Mmhmm!"

    anon "Bagus."

    show anon b_couch_remove
    with dissolve
    pause
    show anon b_couch_jump
    show jenny b_couch_jump o_empty
    with dissolve
    jenny "Oh, sial!"

    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    hide jenny
    scene expression "backgrounds/location_home_livingroom_couch_sex.jpg"
    show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
    with fade
    anon "Ssst!"

    anon "{b}[deb_name]{/b} akan panik jika dia menemukan kita!"

    jenny "Aku tahu!"

    jenny "Itu sangat dalam, aku tidak bisa-"

    jump jenny_couch_sex_loop

label jenny_couch_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_sex {}".format(pose_list[pose_counter]) as jenny_couch_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_sex_options

label jenny_couch_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Aku sangat menyukai penismu!{p=2}{nw}"

        jenny "Ya Tuhan!!{p=1}{nw}"

        jenny "Saya menyukainya, saya menyukainya, saya menyukainya!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUCK, YA!{p=1}{nw}"

        anon "Ssst!!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        jenny "Ayo, {b}[firstname]{/b}!{p=1}{nw}"

        jenny "Persetan aku lebih keras!{p=1}{nw}"

        anon "Berhenti menarikku!{p=2}{nw}"

        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Oh, itu dia!{p=1}{nw}"

    return

label jenny_couch_sex_cum_outside:
    anon "Aku akan keluar!"

    jenny "Saya juga!"

    jenny "NGGHHH!!!"

    show jenny_couch_sex cumshot
    anon "HNNGGG!!!" with flash
    pause
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after3
    show anon b_couch_sit_naked f_couch_sit_right a_naked_after
    with fade
    anon "Wah..."

    show jenny b_couch_after4
    jenny "Haah... Haah..."

    show jenny b_couch_after3
    anon "Itu sangat intens!"

    show jenny b_couch_after4
    jenny "Kamu datang ke seluruh tubuhku!"

    show jenny b_couch_after3
    anon "Apakah kamu lebih suka aku punya air mani di dalam dirimu?"

    show jenny b_couch_after4
    jenny "Tidak... Tapi kamu bisa saja-"

    show jenny b_couch_after3
    pause
    show jenny b_couch_after4
    jenny "{i}*Huh*{/i} Sudahlah."

    show jenny b_couch_remove with dissolve
    jenny "Aku mau mandi."

    show jenny b_couch_transition with dissolve
    pause 1
    hide jenny with dissolve
    jenny "Nanti, pecundang."

    anon "Ya, sampai jumpa."

    pause
    anon f_couch_sit_down_surprised "(Fiuh, kurasa kita hanya bercinta kapan saja sekarang...)"

    anon "(Luar biasa!)"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["08_unlocked"] = True
    $ M_jenny.set("couch_sex_first", False)
    $ M_jenny.set("had_couch_sex", True)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_sex_cum_inside:
    anon "Aku akan keluar!"

    jenny "Saya juga!"

    anon "Lepaskan aku!"

    jenny "NGGHHH!!!"

    anon "{b}[jen_name]{/b} Saya tidak bisa-"

    show jenny_couch_sex cum
    anon "HNNGGG!!!" with flash
    jenny "AAHHHH!!!"

    show jenny_couch_sex cum 2
    show xray_jenny_couch at Position (align=(0,0))
    pause
    hide xray_jenny_couch
    show jenny_couch_sex pullout 1
    with dissolve
    anon "Sialan..."

    show jenny_couch_sex pullout 2 with dissolve
    jenny "Haah... Haah..."

    call call_pregnancy_minigame ("jenny_couch_sex_cum_inside_post_pregnancy", M_jenny)

label jenny_couch_sex_cum_inside_post_pregnancy:
    scene expression "backgrounds/location_home_livingroom_couch01.jpg"
    show jenny b_couch_after2
    show anon b_couch_sit_naked f_couch_sit_right a_naked_after
    with fade
    show jenny b_couch_after1
    jenny "Ya Tuhan, apakah kamu masuk ke dalam diriku?!"

    show jenny b_couch_after2
    anon "Aku mencoba menariknya tetapi kamu tidak mau melepaskanku!"

    show jenny b_couch_after1
    jenny "Yah, aku fokus pada cumming!"

    show jenny b_couch_after2
    pause
    show jenny b_couch_after1
    jenny "SIALAN!"

    jenny "Kamu akan mati jika aku hamil!"

    show jenny b_couch_after2
    anon "A-aku?!"

    anon "Kaulah yang menahanku di sana!"

    show jenny b_couch_after1
    jenny "Diam!"

    show jenny b_couch_remove with dissolve
    jenny "Grr, aku mau mandi!"

    show jenny b_couch_transition_mad with dissolve
    pause 1
    hide jenny with dissolve
    jenny "Brengsek..."

    anon "Oh, jadi ini semua salahku ya?!"

    pause
    anon "(Dia pergi...)"

    pause
    anon f_couch_sit_down_surprised "(Fiuh, kurasa kita hanya bercinta kapan saja sekarang...)"

    anon "(Luar biasa!)"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    $ M_jenny.set("had_couch_sex", True)
    $ M_jenny.set("couch_sex_first", False)
    $ game.timer.tick()
    $ game.main()

label jenny_shower_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_shower_sex", [1,2,3,4,5,6,7,8], M_jenny) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_shower_sex {}".format(pose_list[pose_counter]) as jenny_shower_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_shower_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_shower_sex_options

label jenny_shower_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Sangat dalam!{p=1}{nw}"

        jenny "Oh, persetan denganku!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "FUUUUUCK!!!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        anon "Uhh!{p=1}{nw}"

    return

label jenny_shower_sex_cum_inside:
    jenny "aku keluar! aku keluar!"

    jenny "NGGHHH!!!"

    anon "Ya, aku juga semakin dekat."

    pause
    anon "{b}[jen_name]{/b}?"

    show jenny_shower_sex cum
    anon "HNNGGG!!!" with flash
    jenny "AAAHHHH!!!"

    show jenny_shower_sex cum 2
    show xray_jenny_shower at Position (align=(0,0))
    pause
    call call_pregnancy_minigame ("jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_shower_sex_cum_inside_post_pregnancy_minigame:
    call scene_shower_with_vfx
    show anon b_naked f_tired od_naked_dick1
    show jenny b_shower_back a_push
    with fade
    anon "Haah... Haah..."

    show jenny a_butt f_surprised with dissolve
    anon f_normal "Sialan!"

    show jenny b_shower_back_creampie with dissolve
    jenny "Apakah kamu masuk ke dalam diriku?!"

    anon f_worried "Y-ya, sedikit..."

    show anon f_surprised
    show jenny b_naked a_crossed f_angry with dissolve
    jenny "SEDIKIT?!"

    jenny "ITU BANYAK, KAMU BODOH!"

    anon f_worried "Saya minta maaf."

    anon "Saya kira saya sedikit terbawa suasana di sana pada akhirnya..."

    jenny "Bagaimana jika saya hamil?!"

    anon "aku tidak-"

    jenny "Sial, {b}[firstname]{/b}!"

    jenny "Keluarlah!"

    anon "Baiklah, baiklah..."

    anon "Aku bilang aku minta maaf, sial."

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_shower_sex_cum_outside:
    jenny "aku keluar! aku keluar!"

    jenny "NGGHHH!!!"

    anon "Ya, aku juga semakin dekat."

    pause
    anon "{b}[jen_name]{/b}?"

    hide jenny_shower_sex
    show jenny b_shower_cumshot f_shower_cumshot
    show anon b_side_naked_forward od_side_naked_forward_cum1 f_side_react a_up_clench
    anon "HNNGGG!!!" with flash
    show anon od_side_naked_forward_cum2 o_side_naked_forward_cum3 with dissolve
    pause
    show anon b_naked a_idle f_tired od_naked_dick1 o_empty
    show jenny b_naked a_sides f_sexy_down
    with dissolve
    anon "Haah... Haah..."

    show anon f_normal
    show jenny f_sexy
    jenny "Haah... sial!"

    show jenny f_sexy_down
    jenny "Saya pikir-"

    jenny "Aku perlu berbaring sebentar."

    show jenny f_sexy
    anon f_worried "Kamu baik-baik saja?"

    jenny "Y-ya, itu hanya uap dan seks dan..."

    show anon f_normal
    show jenny f_laugh
    jenny "Sial, aku hampir tidak bisa berjalan!"

    show jenny f_sexy
    anon @ f_grin -m_talk "Hehe."

    anon "Di sini, saya akan membantu Anda."

    show anon f_worried
    show jenny f_upset a_hips with dissolve
    jenny "Tidak, pergilah!"

    jenny "Saya baik-baik saja!"

    anon "Baiklah, sialan."

    anon "aku hanya mencoba untuk mempertimbangkan..."

    jenny "Baiklah, hentikan!"

    hide jenny with dissolve
    pause
    anon @ -m_talk "(Terkadang dia sangat aneh...)"

    anon f_grin @ -m_talk "(Oh baiklah, itu luar biasa!)"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["14_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label bj_shower_repeat_sub:
    show anon f_worried_low
    anon "Arf!"

    show jenny f_grin
    jenny "Hehe, lebih lagi!"

    anon "{i}*Huh*{/i}"

    anon f_shock "Arf! Arf! Arf!"

    show anon f_worried_low
    show jenny f_laugh
    jenny "Hahahah!!"

    show anon b_side_naked a_react f_side_shy_down od_side_naked_dick3
    show jenny b_shower_kneeling f_shower_kneeling
    with dissolve
    if randomizer() > 50:
        jenny "Anjing yang baik!"

    else:
        jenny "Ada anak baik!"

    call scene_shower_with_vfx_zoom
    show jenny_shower_bj_mc
    show jenny_shower_bj pre_talk
    with fade
    jenny "Sekarang Anda mendapat hadiah!"


label bj_shower_repeat_dom:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .14)
    show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    anon "!!!" with hpunch

    if M_jenny.get('first_time_deep_bj'):
        $ M_jenny.set('first_time_deep_bj', False)
        anon "{i}*Terkesiap*{/i}"

        pause
        anon "Wah oke..."

        anon "Ahhh!"

        pause
        anon "Mm, rasanya enak sekali!"

        jenny "Mmhmm."

        pause
        show jenny_shower_bj_mc
        show jenny_shower_bj pre_talk
        with dissolve
        jenny "Baiklah, aku akan mencoba sesuatu sekarang..."

        show jenny_shower_bj pre_look
        anon "Hmm?"

        show jenny_shower_bj pre_talk
        jenny "Penggemar saya telah meminta sesuatu kepada saya dan saya akan mengujinya pada Anda."

        show jenny_shower_bj pre_look
        anon "Apa itu?"

        show jenny_shower_bj pre_talk
        jenny "Anda akan lihat."

        jenny "Coba saja dan tetap diam!"

        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
        anon "Anda tidak akan melakukan sesuatu yang aneh, bukan?"

        pause
        anon "{b}[jen_name]{/b}?"

    else:
        anon "MM."

        pause
        anon "Bagus sekali!"

        jenny "Shrmmup!!"

        anon "Ohh!"

        pause
        anon "Mm, rasanya enak sekali!"

        jenny "Mmhmm."

        pause

    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
    $ M_jenny.set("jenny_bj_deep", True)
    anon "!!!" with hpunch
    anon "Astaga!!"

    pause
    anon "Rasanya luar biasa!!!"

    jenny "{i}*Gllrrkkk*{/i}"

    pause
    jenny "{i}*Bllgghhh*{/i}"

    anon "{b}[jen_name]{/b}, saya tidak bisa-"


    label jenny_shower_bj_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    if M_jenny.get("jenny_bj_deep"):
                        $ M_jenny.set('sex speed', .4)
                        show expression AnimatedImage("jenny_shower_bj_deep", [1,2], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    else:
                        $ M_jenny.set('sex speed', .14)
                        show expression AnimatedImage("jenny_shower_bj", [1,2,3,4,5,6,7], M_jenny) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0) with dissolve
                    $ animated = True
                pause 5
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                if M_jenny.get("jenny_bj_deep"):
                    $ pose_list = [1,2]
                else:
                    $ pose_list = [1,2,3,4,5,6,7]
                $ poses_done = []
                while poses_done != pose_list:
                    if M_jenny.get("jenny_bj_deep"):
                        show expression "jenny_shower_bj_deep {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    else:
                        show expression "jenny_shower_bj {}".format(pose_list[pose_counter]) as jenny_shower_bj at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("jenny_shower_bj_hscene_dialog")
            $ animcounter += 1
        call screen jenny_shower_bj_options

label jenny_shower_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        anon "Hmm.{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        anon "Sangat bagus!{p=1}{nw}"

        jenny "Ayo!!{p=1}{nw}"

        anon "Ohh!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        anon "{i}*Terkesiap*{/i}"

    if animcounter == 3 and randomizer() < 10:
        anon "Wah oke..."

        anon "Ahhh!"

    if animcounter == 3 and randomizer() < 10:
        anon "Mm, rasanya enak sekali!"

        jenny "Mmhmm."

    return

label jenny_shower_bj_cum:
    anon "Aku semakin dekat!"

    jenny "{i}*Sluuuuurp*{/i}"

    pause
    anon "{b}[jen_name]{/b}!"

    pause
    show jenny_shower_bj cum
    anon "HNNGGG!!!" with flash
    jenny "!!!"
    show jenny_shower_bj after with dissolve
    pause
    call scene_shower_with_vfx
    show jenny b_naked a_hips f_cheeks_surprised
    show anon b_naked f_normal od_naked_dick1
    with fade
    if M_jenny.get("first_shower_time"):
        $ M_jenny.set("first_shower_time", False)
        anon "Fiuh, itu tadi-"

        anon "Maksudku, aku tidak mengharapkanmu untuk-"

        show anon f_surprised
        show jenny f_cheeks_swallow a_shocked with dissolve
        anon @ -m_talk "!!!"
        show jenny f_normal
        jenny "Sial, itu air mani yang banyak!"

        show jenny a_hips with dissolve
        anon f_worried "Anda menelannya!"

        show anon f_surprised
        jenny "Ya, jadi?"

        anon f_normal "Saya pikir kamu tidak suka melakukan itu?!"

        show jenny f_upset
        jenny "Kapan saya pernah mengatakan itu?"

        anon f_skeptical "Saat kau mengejutkanku saat streaming!"

        anon "Kamu bilang kamu hanya menelannya karena penggemarmu membayar ekstra untuk itu!"

        show jenny f_normal
        jenny "Oh benar..."

        anon "Mereka tidak bisa melihat kita di sini, {b}[jen_name]{/b}!"

        show jenny f_upset
        jenny "Mungkin aku tidak ingin membuat kekacauan, pernahkah kamu memikirkan hal itu?!"

        anon f_worried "Anda tidak ingin membuat kekacauan... Di kamar mandi?"

        jenny @ -m_talk "..."
        jenny "Ya Tuhan, hanya-"

        jenny "Apa pun."

        show jenny f_eyeroll
        jenny "{i}*Huh*{/i} Aku menyukainya, oke?"

        show jenny f_upset
        anon f_surprised @ -m_talk "..."
        jenny "Aku suka menelan air manimu..."

        jenny "Apakah kamu sangat bahagia sekarang?!"

        anon f_normal "Heh, aku tidak percaya kamu baru saja mengatakan itu..."

        show jenny f_eyeroll a_crossed with dissolve
        jenny "Ugh..."

        show jenny f_upset
        jenny "Jangan mendapat ide apa pun, pecundang!"

        jenny "Hanya karena aku menyukai air mani dan penis besarmu, bukan berarti aku menyukaimu!"

        anon f_worried @ -m_talk "..."
        jenny "Sekarang pergilah dan biarkan aku menyelesaikan mandiku!"

        anon "Baiklah."

        anon f_normal "Terima kasih untuk-"

        show anon f_surprised
        show jenny f_angry
        jenny "Keluar!!"

        hide anon with dissolve
        jenny "Astaga!"

        show jenny f_angry_pouting

        $ player.go_to(L_home_hallway)
        scene expression player.location.background_blur
        show anon f_grin with dissolve
        anon @ -m_talk "(Itu sangat luar biasa!)"

        anon @ -m_talk "( Apakah ini berarti {b}Saya bisa ikut mandi dengannya kapan pun saya mau{/b}? )"

        show anon f_thinking a_thinking with dissolve
        pause
        anon f_grin @ -m_talk "(Saya pikir itu benar!)"

    else:
        anon "Fiuh..."

        anon "Anda menjadi sangat ahli dalam hal itu!"

        show jenny f_cheeks_swallow a_shocked with dissolve
        pause
        show jenny f_grin
        jenny "Pfft, pernahkah aku tidak pandai dalam hal itu?"

        anon "Hehe, poin bagus."

        pause
        show jenny f_normal
        jenny "Baiklah, kalahkan supaya aku bisa menyelesaikan mandiku."

        anon "Ya baiklah."

        anon "Terima kasih atas mahasiswinya!"

        show anon f_grin
        show jenny f_eyeroll a_crossed with dissolve
        jenny "Astaga."

        show jenny f_upset
        jenny "Keluar!"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["13_unlocked"] = True
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_mc_room_sex_on_sleep:
    if store._in_replay is not None:
        $ player.location = L_home_bedroom
    $ game.timer.tick(3)
    scene expression "backgrounds/location_home_bedroom_cutscene18.jpg"
    jenny "Ssst!"

    jenny "{b}[firstname]{/b}, kamu sudah bangun?"

    scene expression "backgrounds/location_home_bedroom_cutscene17.jpg"
    anon "MM."

    pause
    scene expression "backgrounds/location_home_bedroom_sex01c.jpg"
    show anon b_visit f_visit_sleep
    show jenny b_visit_sit a_down f_visit_sexy with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        jenny "{b}[firstname]{/b}?"

        anon "Nnnhhh."

        pause
        jenny "Ayo, bangun."

        anon "NNNHHH!"

        show jenny f_visit_sexy_down a_reach with dissolve
        anon f_visit_normal "Sial, {b}[jen_name]{/b}..."

        anon "Ini tengah malam!"

        show anon b_visit_up2 f_visit_up_tired
        show jenny a_pull
        with dissolve
        jenny "Oh, diamlah."

        show jenny f_visit_sexy_down a_up with dissolve
        show jenny a_up2 with dissolve
        pause
        show jenny a_stroke with dissolve
        anon "Apa yang kamu lakukan, {b}[jen_name]{/b}?"

        anon "Aku mencoba untuk tidur-"

        show jenny f_visit_sexy_down
        jenny "Sepertinya apa yang aku lakukan?!"

        show jenny b_visit_remove1
        show jenny_arms_visit_a_dick
        with dissolve
        show anon f_visit_up_surprised
        pause
        show jenny b_visit_remove2 with dissolve
        anon f_visit_up_tired "Kita benar-benar harus melakukan ini, sekarang juga?!"

        hide jenny_arms_visit_a_dick
        show jenny b_visit_climb
        with dissolve
        jenny "Ya, aku sangat terangsang dan aku menginginkannya sekarang juga!"


        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        anon "!!!"
        anon "Sial {b}[jen_name]{/b}, aku lelah..."

        jenny "Oh, astaga... Yang harus kamu lakukan hanyalah berbaring di sana!"

        jenny "Akulah yang melakukan semua pekerjaan!"

        show jenny_mc_room_sex 1 with dissolve
        jenny "{i}*Terkesiap*{/i}"

        jenny "Ya Tuhan, aku suka penismu!"

        jump jenny_mc_room_sex_start
    else:
        jenny "Bangun, {b}[firstname]{/b}."

        show jenny f_visit_sexy
        anon f_visit_normal "{b}[jen_name]{/b}?"

        show jenny a_reach with dissolve
        jenny "Ayolah, aku membutuhkannya."

        show anon b_visit_up2 f_visit_up_tired
        show jenny f_visit_sexy_down a_pull
        with dissolve
        pause
        show jenny a_up with dissolve
        show jenny a_up2 with dissolve
        pause
        show jenny a_stroke with dissolve
        menu:
            "Sekarang?":
                anon f_visit_up_tired "Sekarang?"

                show jenny b_visit_remove1
                show jenny_arms_visit_a_dick
                with dissolve
                show anon f_visit_up_surprised
                pause
                show jenny b_visit_remove2 with dissolve
                pause
                hide jenny_arms_visit_a_dick
                show jenny b_visit_climb
                with dissolve
                jenny "Ya, aku menginginkannya sekarang."


                scene expression "backgrounds/location_home_bedroom_sex05.jpg"
                show jenny_mc_room_sex insert
                with fade
                anon "!!!"
                anon "O-oke."

                jenny "Ya Tuhan, aku tidak bisa mengeluarkan penis ini dari kepalaku!"

                anon "Wah, kamu basah banget.."

                show jenny_mc_room_sex 1 with dissolve
                jenny "{i}*Terkesiap*{/i}"

                jenny "Ohh, sial."

                jump jenny_mc_room_sex_start
            "Tidak malam ini." if store._in_replay is None:
                if M_jenny.get("dominance") <= 0:
                    anon f_visit_up_tired "Tidak sekarang, {b}[jen_name]{/b}."

                    show jenny f_visit_sexy_down
                    jenny "Ayolah, kamu tahu kamu menginginkannya..."

                    anon "Kita lakukan saja besok, oke?"

                    show jenny f_visit_sexy
                    jenny "Saya tidak menginginkannya besok, saya menginginkannya sekarang!"

                    show jenny f_visit_sexy_down
                    anon "Ahhh, aku sudah terikat..."

                    show jenny f_visit_angry a_up2 with dissolve
                    jenny "Dengan serius?!"

                    jenny "Ada cewek seksi yang sedang membelai penismu sekarang dan kamu bilang tidak?!"

                    anon "{i}*Huh*{/i} Maaf... aku tidak-"

                    jenny "Lupakan saja!"

                    anon "T-tidak, kami bisa jika kamu benar-benar ingin-"

                    jenny "Aku sedang tidak mood lagi!"

                    hide jenny
                    show jenny_arms_visit_a_dick
                    with dissolve
                    jenny "Terkadang kamu memang menyebalkan, aku bersumpah!"

                    anon "{b}[jen_name]{/b}, maaf, aku-"

                    anon @ -m_talk "..."
                else:
                    anon "Tidak sekarang, {b}[jen_name]{/b}."

                    show jenny f_visit_sexy_down
                    jenny "Ayolah, kamu tahu kamu menginginkannya..."

                    anon "Tidak, aku hanya ingin tidur... Oke?"

                    show jenny f_visit_sexy
                    jenny "Tolong, {b}[firstname]{/b}?"

                    anon "Aku bilang tidak!"

                    show jenny f_visit_angry a_up2 with dissolve
                    jenny "Dengan serius?!"

                    jenny "Aku mencoba bersikap baik di sini, sesukamu... Aku bahkan bilang tolong!"

                    anon "Aku hanya sedang tidak mood, oke?"

                    jenny @ -m_talk "..."
                    jenny "BAGUS!"

                    hide jenny
                    show jenny_arms_visit_a_dick
                    with dissolve
                    jenny "Aku tak tahu kenapa aku menyia-nyiakan waktuku untukmu..."

                    anon "Apa pun."

                jump resume_sleeping_bedroom

label jenny_mc_room_sex_start:
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    jenny "Ahhh!"

    pause
    anon "Oke, rasanya enak sekali..."

    if M_jenny.is_state(S_jenny_night_time_sex):
        jenny "Lihat, dan kalian semua mengeluh tentang hal itu!"

        anon "Ya, kita bisa melakukannya besok!"

        jenny "Ya, dan kami mungkin akan..."

        anon "B-benarkah?"

        jenny "Uhh, ya... Camshow, bodoh."

        anon "Oh benar."

        jenny "Diam saja dan biarkan aku menikmati ini!"

    else:
        jenny "Ahhh!"

        pause
        anon "Oke, rasanya enak sekali..."

        jenny "Ya, benar!"

    pause
    jenny "Ahh, sialan!"

    pause
    jenny "Mmm, aku akan mengotori penis besarmu itu, {b}[firstname]{/b}!"

    if M_jenny.get("dominance") <= 0:
        jenny "Anda pasti menyukainya, bukan?!"

        anon "Y-ya."

        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Ahhh!"

        jenny "Ayo, katakan!"

        jenny "Katakanlah kamu ingin aku cum di penis besarmu!"

        anon "Aku ingin kamu cum di penisku yang besar!"

        if not M_jenny.is_state(S_jenny_night_time_sex):
            jenny "Saya pikir Anda bisa melakukan yang lebih baik..."

            pause
            jenny "Katakan padaku aku seorang dewi seks!"

            anon "K-kamu adalah dewi seks!"

            jenny "Ayolah, jalang!"

            jenny "Aku tidak bisa mendengarmu!"

            anon "Anda seorang dewi seks!!!"

            jenny "Kamu memuja vagina ini, bukan?!"

            anon "Y-ya!"

        jenny "Hahahah!!"

    else:
        anon "Kalau begitu lakukanlah!"

        if M_jenny.get("sex speed") > 0.061:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Ahh, sial!"

        anon "Katakan padaku kamu menginginkannya!"

        jenny "Hmm, aku menginginkannya!"

        pause
        anon "Ayo {b}[jen_name]{/b}, lebih cepat!"

        jenny "Ya Tuhan!"

        pause
        if M_jenny.is_state(S_jenny_night_time_sex):
            jenny "Ahh, persetan denganku!!"

        else:
            anon "Mohon saya untuk memberikannya kepada Anda!"

            jenny "Ahhh!"

            jenny "Silakan!!"

            pause
            anon "Ayo, kamu bisa berbuat lebih baik!"

            jenny "Sial!"

            jenny "Tolong, {b}[firstname]{/b}!!"

            jenny "Berikan padaku!!!"


    anon "Ssst!"

    anon "Anda akan bangun {b}[deb_name]{/b}..."

    jenny "Aku tidak peduli!"

    pause
    jenny "Ahh, aku sangat dekat!"


label jenny_mc_room_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_mc_room_sex {}".format(pose_list[pose_counter]) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_mc_room_sex_hscene_dialog")
        $ animcounter += 1
    call screen jenny_mc_room_sex_options

label jenny_mc_room_sex_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh, sial!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Sial!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Hahahaah!!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        anon "Ya Tuhan!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "Ahh, persetan denganku!!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        anon "Saya semakin dekat...{p=1}{nw}"

    return

label jenny_mc_room_sex_cum_inside:
    jenny "Ya Tuhan, ya Tuhan, ya Tuhan!"

    pause
    jenny "aku keluar! aku keluar!"

    anon "Saya juga!"

    jenny "AAAHHH, sial!!!"

    anon "{b}[jen_name]{/b}, turun!"

    jenny "NGGHHH!!!"

    anon "Ah, sial!"

    $ M_jenny.set('sex speed', .4)
    show expression AnimatedImage("jenny_mc_room_sex cum", [1,2], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
    anon "HNNGGG!!!" with flash
    show jenny_mc_room_sex cum 2
    show xray_jenny_mcbedroom:
        align (0,0)
    pause
    call call_pregnancy_minigame ("jenny_mc_room_sex_cum_inside_post_pregnancy_minigame", M_jenny)

label jenny_mc_room_sex_cum_inside_post_pregnancy_minigame:
    scene expression "backgrounds/location_home_bedroom_sex05.jpg"
    show jenny_mc_room_sex pullout
    with fade
    anon "Haah... Haah..."

    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_angry_down o_visit_after_creampie
    with dissolve
    jenny "Ya Tuhan..."

    pause
    show jenny f_visit_after_angry
    jenny "Apakah kamu masuk ke dalam diriku?!"

    anon "Sudah kubilang padamu, lepaskan aku!"

    jenny "Sialan, {b}[firstname]{/b}!"

    anon "Apa?!"

    jenny "Aku bisa hamil, bodoh!"

    anon "Yah, aku minta maaf tapi aku sudah memperingatkanmu..."

    jenny "Ugh, terserah."

    show jenny f_visit_after_angry_down
    pause
    show jenny f_visit_after_normal
    jenny "{i}*Huh*{/i} Persetan..."

    jenny "Heh, kakiku gemetar hebat!"

    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_cum_outside:
    jenny "Ya Tuhan, ya Tuhan, ya Tuhan!"

    pause
    jenny "aku keluar! aku keluar!"

    jenny "NGGHHH!!!"

    pause
    anon "Saya juga!"

    show jenny_mc_room_sex cumshot
    anon "HNNGGG!!!{p=1}{nw}" with flash
    show jenny o_visit_cumshot f_empty a_empty b_empty
    pause
    hide jenny_mc_room_sex
    show jenny b_visit_after f_visit_after_normal o_visit_cumshot2
    with dissolve
    anon "Haah... Haah..."

    jenny "Fiuh, itu luar biasa..."

    pause
    jenny "Hahaha, kamu benar-benar berantakan!"

    anon "Heh, aku bahkan tidak peduli... Aku sangat lelah."

    jenny "{i}*Mendengus*{/i} Hehehe!"

    jenny "Kamu harus membersihkan dirimu sendiri, kamu terlihat konyol..."

    if M_jenny.get('girlfriend_in_progress'):
        jump jenny_mc_room_sex_end_girlfriend_experience
    else:
        jump jenny_mc_room_sex_end

label jenny_mc_room_sex_end_girlfriend_experience:
    scene expression "backgrounds/location_home_bedroom_bed.jpg"
    show jenny b_sleep_side_naked a_side f_sleep_side_tired:
        flip
        xoffset 500
    show anon b_sleep_side f_sleep_side_normal a_poke o_sleep_side_dick2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_sleep_blanket_transparent2.png"
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        anon "Malam ini sangat menyenangkan!"

        show jenny f_sleep_side_tired
        jenny "Saya senang Anda menikmati diri Anda sendiri."

        anon "... Dan aku sangat senang kamu tidak terburu-buru kali ini."

        jenny "Ya, kamu sudah membayarku untuk tidak melakukannya, ingat?"

        anon "Ya."

        jenny "Hahahaah!"

        anon "Anda juga bersenang-senang, bukan?"

        show jenny f_sleep_side_rolleye
        jenny "Ya, {b}[firstname]{/b}..."

        show jenny f_sleep_side_tired
        jenny "Sekarang bisakah kamu diam dan biarkan aku tidur?"

        show jenny f_sleep_side_sleeping
        anon "Maaf..."

        show anon f_sleep_side_kiss
    else:
        anon "Hehe, aku sangat menikmati malam-malam kita melakukan ini..."

        show jenny f_sleep_side_tired
        jenny "Ya, aku juga."

        jenny "Saya senang saya mendapat ide itu."

        anon "Uhh, kamu tahu, secara teknis ini adalah ide SAYA..."

        jenny "Oh, diamlah!"

        anon "aku hanya mengatakan..."

        jenny "Ya, saya tahu apa yang Anda katakan... Sekarang zip!"

        jenny "Anda merusak kebahagiaan pasca-persetubuhan saya."

        anon "Maaf."

        show jenny f_sleep_side_rolleye
        jenny "Tidurlah."

        show jenny f_sleep_side_sleeping
        show anon f_sleep_side_kiss
    $ M_jenny.set('had_sex_bedroom', True)
    jump resume_sleeping_bedroom

label jenny_mc_room_sex_end:
    show jenny f_visit_after_normal
    if M_jenny.is_state(S_jenny_night_time_sex):
        anon "kamu tinggal?"

    else:
        anon "Kamu berangkat lagi?"

    jenny "Hmm?"

    if M_jenny.is_state(S_jenny_night_time_sex):
        anon "Maukah kamu tidur di sini bersamaku malam ini?"

        jenny "Eww, tidak!"

        jenny "Aku bukan pacarmu, doofus..."

    else:
        anon "Kamu bisa tidur di sini, tahu?"

        jenny "Demi Tuhan..."

        jenny "Bukankah kita sudah membahasnya?"


    if store._in_replay is not None:
        $ player.location = L_home_bedroom

    scene expression player.location.background_blur with None
    show jenny b_naked a_sides f_normal o_empty:
        xoffset -400
    show anon b_underwear f_skeptical at flip
    with dissolve
    if M_jenny.is_state(S_jenny_night_time_sex):
        anon "Tunggu!"

    else:
        anon "Baiklah, baiklah... Terserah."

    show anon f_worried
    hide jenny
    if M_jenny.is_state(S_jenny_night_time_sex):
        $ M_jenny.trigger(T_jenny_didnt_sleep_much)
        show jenny b_naked a_crossed f_upset at flip
        with dissolve
        jenny "Apa, {b}[firstname]{/b}?!"

        anon "Aku tidak mencoba untuk-"

        anon "{i}*Huh*{/i} Jelaskan saja padaku..."

        anon @ f_skeptical "Jadi, kita bisa berhubungan kapan pun kita mau tapi kamu tidak mau tidur di ranjangku?"

        show jenny f_eyeroll
        jenny "Umm, tidak... Kita bisa berhubungan seks kapan pun {i}Aku{/i} mau..."

        show jenny f_upset
        jenny "... Selama tidak mengganggu camshowku."

        pause
        jenny "... Dan tidak, aku tidak akan tidur di tempat tidurmu!"

        jenny "Aku bukan pacarmu, dan kamu pasti bukan pacarku!!!"

        jenny "Dapatkan itu melalui tengkorak tebalmu, bodoh!"

        anon f_skeptical "aku tidak mengerti kamu sama sekali..."

        jenny "Ya, baiklah... Anda tidak perlu {i}menangkap{/i} saya."

        jenny "Begitulah adanya."

        jenny "Tangani itu."

        anon @ -m_talk "..."
    else:
        show jenny b_naked a_crossed f_upset at flip
        with dissolve
        anon f_skeptical "Lupakan saja aku mengatakan sesuatu."

        jenny "Dengan senang hati."

        pause
    show jenny f_upset
    jenny "Sekarang tidurlah!"

    show jenny f_grin
    jenny "Penggemar saya mengharapkan pertunjukan yang bagus besok."

    hide jenny with dissolve
    pause
    anon f_worried @ -m_talk "..."
    scene black with fade
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["12_unlocked"] = True
    jump resume_sleeping_bedroom

label jenny_sex_intro_repeat:
    show anon f_worried
    anon "Seks. Silakan."

    show jenny f_upset
    jenny "Ayo cepat."

    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Ya?"

    anon @ -m_talk "Hmm?"

    jenny "Lepaskan pakaian itu!"

    show jenny b_naked f_grin_down a_panties_remove with dissolve
    anon f_worried "B-benar..."

    show anon b_dressed_changing
    show jenny b_cheer_dress1
    with dissolve
    pause
    show jenny b_cheer_dress3 f_grin_down with dissolve
    pause
    show jenny b_cheer_dress2 with dissolve
    show anon f_worried b_shorts with dissolve
    anon "Kamu akan memakainya lagi?"

    show jenny b_cheer a_hips f_sexy with dissolve
    jenny "Tentu saja!"

    jenny "Penggemar saya menyukainya."

    show anon b_dressed_changing2 with dissolve
    anon "..."
    show anon b_underwear f_worried with dissolve
    jenny "Naiklah ke tempat tidur."

    hide anon with dissolve
    pause
    jenny "... Dan kenakan topengmu!"

    label finger_blasting_sex:
    scene black with fade
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop o_naked_bed_belly_cheer b_naked_bed_bellytype f_sexy_down
    with dissolve
    pause
    jenny "Kalian siap untuk pertunjukan lainnya?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny f_laugh
    jenny "Hehehe!"

    show jenny f_sexy_down
    jenny "Baiklah, biarkan aku menyiapkan semuanya..."

    show jenny b_bed_climbing o_cheer_bed_climbing
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png" zorder 2
    show expression "characters/jenny/layeredimage/jenny_overlay_o_laptop.png"
    with dissolve
    jump jenny_cheer_sex_intro_prepare

label jenny_cheer_sex_intro_prepare:
    anon "Apakah kita benar-benar akan-"

    jenny "Ssst!"

    pause
    show jenny b_bed_back_sit o_cheer_bed_back
    show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_handcuffs.png" zorder 1
    with dissolve
    anon "Ah, ayolah {b}[jen_name]{/b}!"

    anon "Kau tahu aku benci hal-hal ini..."

    show jenny a_sit_tie
    hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_handcuffs.png"
    show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_tie.png" zorder 1
    show anon oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jenny "Tutup mulutmu!"

    if M_jenny.get("dominance") <= 0:
        anon "..."
        pause
        show jenny a_sit_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png" zorder 1
        with dissolve
        if M_jenny.finished_inclusive(S_jenny_end) or store._in_replay:
            jenny "Dan jika Anda sangat membenci mereka, berhentilah mengeluh tentang mereka dan lakukan sesuatu."

            jenny "Itu hanya plastik, saya yakin mereka akan senang melihat Anda mencoba dan {b}melepaskan diri{/b}!"

        else:
            jenny "Bagus."

        jenny "Sekarang, mohonlah."

        anon "Apa?!"

        jenny "Kau ingin aku mengajak ayam besarmu itu jalan-jalan, bukan?"

        anon "Y-ya..."

        jenny "Maka kamu akan memohon padaku untuk itu, di depan penggemarku!"

        anon "..."
        jenny "Ayo!"

        anon "Tolong..."

        jenny "Putri!"

        anon "..."
        anon "Tolong, {b}Putri [jen_name]{/b}..."

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        jenny "HAHAHAH!"

        show jenny b_bed_front_sit a_pull1 f_sexy_down o_cheer_bed_front_sit2
        hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png"
        with dissolve
        pause
        show jenny a_pull2 o_cheer_bed_front_sit3 with dissolve
        jenny "Kalian siap?"

    else:
        anon "Saya tidak menyukai mereka!"

        jenny "TAHAN TETAP!"

        anon "Grr!"

        jenny "Aku yang bertanggung jawab di sini, bukan kamu!"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        show jenny a_hips
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_tie.png"
        show expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png" zorder 1
        with dissolve
        jenny "Di sana!"

        jenny "Sheesh, aku tidak tahu apa yang kamu keluhkan..."

        show jenny b_bed_front_sit a_pull1 f_sexy_down o_cheer_bed_front_sit2
        hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
        hide expression "characters/jenny/layeredimage/jenny_arms_bed_back_a_sit_hips.png"
        with dissolve
        jenny "Inilah aku, menawarkan untuk mengacau otakmu, dan kamu mengeluh tentang borgol bodoh!"

        show jenny a_pull2 o_cheer_bed_front_sit3 with dissolve
        jenny "Kalian tidak akan melakukan perlawanan, kan?!"

    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny a_sides f_sexy_down o_cheer_bed_front_sit
    with dissolve
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Hehe, mereka bersemangat."

    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied insert
    with fade
    jenny "( Ini dia, {b}[firstname]{/b}... Momen yang kamu impikan! )"

    jenny "Ohh!"

    jenny "Sialan!"

    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .09)
    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
    jenny "Ya Tuhan, kalian..."

    jenny "Ini adalah penis yang SANGAT besar!"

    jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_loop_tied:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_jenny.get("cam show mask"):
                    show expression AnimatedImage("jenny_cheer_sex_tied_mask", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression AnimatedImage("jenny_cheer_sex_tied", [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            $ poses_done = []
            while poses_done != pose_list:
                if M_jenny.get("cam show mask"):
                    show expression "jenny_cheer_sex_tied_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                else:
                    show expression "jenny_cheer_sex_tied {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_tied")
        $ animcounter += 1
    call screen jenny_cheer_sex_options_tied

label jenny_cheer_sex_hscene_dialog_tied:
    if animcounter == 0 and randomizer() < 10:
        jenny "Ahh!{p=1}{nw}"

    if animcounter == 0 and randomizer() < 10:
        jenny "Ini sangat bagus!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Astaga!{p=1}{nw}"

        jenny "Aku akan muncrat ke seluruh penis besar itu!{p=2}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Mmm, sial!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "Enak sekali!!{p=1}{nw}"

        anon "Saya semakin dekat!{p=1}{nw}"

        jenny "SANGAT BAIK!!{p=1}{nw}"

        anon "{b}[jen_name]{/b}!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        anon "Kamu benar-benar ahli dalam hal ini!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 5:
        jenny "Anda menyukainya, bukan?!{p=1}{nw}"

        anon "Y-ya.{p=1}{nw}"

        jenny "Katakan padaku kamu menyukainya!{p=1}{nw}"

        anon "Saya menyukainya!{p=1}{nw}"

        jenny "Katakan padaku kamu menyukai vaginaku!{p=1}{nw}"

        anon "Ahh, aku menyukainya!{p=1}{nw}"

        jenny "Hahahaah!{p=1}{nw}"

        if M_jenny.get("sex speed") > 0.031:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.03)
        jenny "Mmm, ya!{p=1}{nw}"

    return

label jenny_cheer_sex_cum_inside_tied:
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        anon "Saya tidak bisa menahannya!"

    else:
        anon "Turun!"

    pause
    anon "{b}[jen_name]{/b}!!!"

    jenny "NGGHHH!!!"

    anon "aku tidak bisa-"

    pause
    show jenny_cheer_sex tied cum
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex tied cum 2
    show xray_jenny_cheer_bedroom:
        align (0,0)
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_tied_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_tied_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex tied pullout 1
    with fade
    jenny "Haah... Haaah..."

    show jenny_cheer_sex tied pullout 2 with dissolve
    jenny "Fuuuck, itu luar biasa-"

    show jenny_cheer_sex tied pullout 3 with dissolve
    jenny "!!!"
    show jenny_cheer_sex tied pullout 4 with dissolve
    if M_jenny.is_state(S_jenny_cheerleader_sex):
        jenny "Apakah kamu masuk ke dalam diriku?!"

        anon "K-kamu menyuruhku untuk tidak berhenti..."

        jenny "Ya, tapi aku tidak mengatakan untuk menyelesaikan dalam diriku, idiot!"

        anon "Maafkan aku, aku tidak bermaksud-"

        jenny "Bagaimana jika saya hamil?!"

        anon "..."
    else:
        jenny "Apakah kamu masuk ke dalam diriku?!"

        anon "Aku sudah memperingatkanmu!"

        jenny "Saya tidak mendengar apa pun!"

        anon "Nah, apa yang kamu ingin aku lakukan?!"

        anon "Aku diborgol ke tempat tidurmu!"

        jenny "Aku bisa hamil, bodoh!"

        anon "Maka kamu seharusnya turun ketika aku memperingatkanmu!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Oh, astaga..."

    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_tied:
    anon "Aku akan keluar!"

    jenny "Tahan!"

    anon "A-apa?! Ini tidak berhasil seperti itu!"

    jenny "Saya sangat dekat!"

    anon "{b}[jen_name]{/b}!!!"

    jenny "sial!!"

    show jenny_cheer_sex tied cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    anon "Haah... Haah..."

    jenny "Kamu tidak bisa bertahan sepuluh detik lagi?!"

    if randomizer() > 50:
        anon "M-maaf."

    else:
        anon "Sulit ketika saya diborgol ke tempat tidur!"

    jenny "Terserah..."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Oh, astaga..."

    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_break_free:
    if player.has_required_str(7) or store._in_replay is not None:
        $ display.toast(str_pass)
        show jenny_cheer_sex free break
        jenny "!!!" with hpunch
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .08)
        if M_jenny.get("cam show mask"):
            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        else:
            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
        jenny "OH sial!!{p=1}{nw}"

        pause 1
        jenny "OHMYGOD, OHMYGOD, OHMYGOD!!!{p=1}{nw}"

        pause 1
        jenny "AHHH!!!{p=1}{nw}"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}{p=1}{nw}"

        pause 1
        jenny "FUUUUCK MEEEE!!!{p=1}{nw}"


        label jenny_cheer_sex_loop_free:
            show screen sex_anim_buttons
            pause
            hide screen sex_anim_buttons
            $ animcounter = 0
            while animcounter < 4:
                if anim_toggle:
                    if not animated:
                        if M_jenny.get("cam show mask"):
                            show expression AnimatedImage("jenny_cheer_sex_free_mask", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression AnimatedImage("jenny_cheer_sex_free", [1,2,3,4,5], M_jenny) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        $ animated = True
                    pause 5
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                    pause 3
                else:

                    $ pose_counter = 0
                    $ pose_list = [1,2,3,4,5]
                    $ poses_done = []
                    while poses_done != pose_list:
                        if M_jenny.get("cam show mask"):
                            show expression "jenny_cheer_sex_free_mask {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        else:
                            show expression "jenny_cheer_sex_free {}".format(pose_list[pose_counter]) as jenny_cheer_sex at Position(xalign = 0.0, yoffset = 0)
                        pause
                        $ poses_done.append(pose_list[pose_counter])
                        $ pose_counter += 1
                    call expression game.dialog_select("jenny_cheer_sex_hscene_dialog_free")
                $ animcounter += 1
            call screen jenny_cheer_sex_options_free

        label jenny_cheer_sex_hscene_dialog_free:
            if animcounter == 0 and randomizer() < 30:
                jenny "OH sial!!{p=1}{nw}"

            if animcounter == 1 and randomizer() < 10:
                jenny "PERCAYA AKU!{p=.5{nw}"

                jenny "PERCAYA AKU!{p=.5{nw}"

                jenny "FUUUUCK MEEEE!!!{p=1}{nw}"

            if animcounter == 2 and randomizer() < 30:
                jenny "AHHH!!!{p=1}{nw}"

            return
    else:

        $ display.toast(str_fail)
        jenny "Ya Tuhan!{p=1}{nw}"

        pause 1
        jenny "Persetan denganku!{p=1}{nw}"

        pause 1
        jenny "PERCAYA AKU!!{p=1}{nw}"

        jump jenny_cheer_sex_loop_tied

label jenny_cheer_sex_cum_inside_free:
    anon "Aku semakin dekat!"

    pause
    jenny "Jangan berhenti!"

    anon "{b}[jen_name]{/b}, saya tidak bisa-"

    jenny "JANGAN BERHENTI!"

    pause
    jenny "NGGHHH!!!"

    show jenny_cheer_sex free cum
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex free cum 2
    show xray_jenny_cheer_bedroom:
        align (0,0)
    pause
    call call_pregnancy_minigame ("jenny_cheer_sex_cum_inside_free_post_pregnancy", M_jenny)

label jenny_cheer_sex_cum_inside_free_post_pregnancy:
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg"
    show jenny_cheer_sex free pullout 1
    with fade
    jenny "Haah... Haaah..."

    show jenny_cheer_sex free pullout 2 with dissolve
    jenny "Fuuuck, itu luar biasa-"

    show jenny_cheer_sex free pullout 3 with dissolve
    jenny "!!!"
    show jenny_cheer_sex free pullout 4 with dissolve
    jenny "Apakah kamu masuk ke dalam diriku?!"

    anon "Kamu menyuruhku untuk tidak berhenti..."

    jenny "Aku tidak bermaksud agar kamu masuk ke dalam diriku, idiot!"

    anon "Jangan mulai dengan menyebut nama..."

    jenny "Bagaimana jika saya hamil!!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Oh, astaga..."

    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_cum_outside_free:
    anon "Aku semakin dekat!"

    pause
    jenny "Jangan berhenti!"

    anon "{b}[jen_name]{/b}, saya tidak bisa-"

    jenny "JANGAN BERHENTI!"

    pause
    jenny "NGGHHH!!!"

    show jenny_cheer_sex free cumshot
    show jenny_cheer_sex_mc tied cumshot initial
    anon "HNNGGG!!!" with flash
    show jenny_cheer_sex_mc tied cumshot
    pause
    anon "Haah... Haah..."

    jenny "Apa-apaan ini, sudah kubilang jangan berhenti!!"

    anon "Apa, kamu ingin aku masuk ke dalam dirimu?!"

    jenny "T-tidak, itu hanya... Terasa sangat enak dan-"

    jenny "{i}*Huh*{/i} Sudahlah..."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Oh, astaga..."

    jenny "Pertunjukan sudah berakhir, orang mesum!"

    jenny "Saksikan lain kali!"

    jump jenny_cheer_sex_aftermath

label jenny_cheer_sex_aftermath:
    scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
    show jenny f_upset b_cheer a_hips
    show anon b_underwear
    with dissolve
    anon "Itu luar biasa!"

    show jenny f_eyeroll
    jenny "Ya, terserah."

    show jenny f_upset
    jenny "Kamu baik-baik saja."

    show anon f_worried
    jenny "Sekarang, keluar!"

    anon "Tidak bisakah kita-"

    show jenny a_hips_money
    jenny "Tidak, ambil uang bodohmu dan keluar!"

    hide jenny with dissolve
    anon "Baiklah, sial..."

    hide anon with dissolve
    $ player.go_to(L_home_hallway)
    scene expression player.location.background_blur with None
    show anon f_grin with dissolve
    anon @ -m_talk "( Saya baru saja berhubungan seks dengan {b}[jen_name]{/b}... )"

    anon @ -m_talk "( Di kamera di depan ratusan orang!)"

    pause
    anon @ -m_talk "(Betapa gilanya itu?!)"

    anon @ -m_talk "(Saya harap kita melakukannya lagi.)"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["11_unlocked"] = True
    call popup ('earn', 200)
    $ M_jenny.trigger(T_jenny_had_cheerleader_sex)
    $ player.get_money(200)
    $ game.timer.tick()
    $ player.go_to(L_home_hallway)
    $ game.main()

label jenny_cunni_intro_repeat:
    show anon f_worried
    anon "Jadi tidak ada pertunjukan kamera hari ini?"

    show jenny f_upset
    jenny "Tidak, aku sedang tidak mood..."

    anon "Apa?!"

    anon "Anda selalu bersemangat."

    jenny "Untuk dimelototi, brengsek!"

    jenny "Aku sedang tidak mood untuk dimelototi!"

    anon f_laugh "Oh heh. Mengerti."

    show anon f_normal
    jenny "aku butuh hari libur..."

    show anon f_grumpy:
        flip
        xoffset -500
    with dissolve
    anon "Aku serahkan padamu kalau begitu."

    jenny "Tunggu."

    hide anon
    show anon f_normal
    with dissolve
    anon @ -m_talk "..."
    show jenny f_grin
    jenny "Karena kamu sudah di sini..."

    anon f_worried @ -m_talk "Hmm?"

    jenny "Ayo."


    label finger_blasting_cunni:
    scene location_home_hallway_cutscene
    with fade
    anon "Kemana kita akan pergi?!"

    jenny "Saya pikir Anda perlu lebih banyak latihan..."

    anon "K-kenapa kita pergi ke kamarku?!"

    jenny "Oh, diamlah!"


    $ player.go_to(L_home_bedroom)
    scene expression player.location.background_blur
    show anon f_worried
    show jenny b_dressed_panties_remove_down
    with fade
    pause
    show jenny b_pantieless a_hips f_grin with dissolve
    anon "Apa yang sedang kamu lakukan?"

    jenny "Anda akan menjilat vagina saya."

    if M_jenny.get("dominance") <= 0:
        anon "Saya?"

        jenny "Ya."

        jenny "Ayolah, pecundang!"

        jenny "Aku akan mengotori wajah bodohmu itu!"

    else:
        anon "Ah, benarkah?"

        jenny "Ya."

        anon "Mungkin jika Anda bertanya kepada saya dengan baik."

        show jenny f_upset
        jenny "Ugh, kamu masih terpaku pada omong kosong itu?!"

        show anon f_skeptical
        if randomizer() > 50:
            anon "Jika Anda ingin kembali melakukan masturbasi, sesuaikan diri Anda..."

        else:
            anon "Aku bukan bocah pencambukmu, {b}[jen_name]{/b}..."

        jenny "Grr, kamu sungguh menyebalkan!"

        jenny "Bagus."

        show jenny f_angry_pouting a_crossed with dissolve
        pause
        show jenny f_upset
        jenny "{b}[firstname]{/b}, maukah kamu menjilat vaginaku?"

        anon @ f_laugh "Haha, tentu saja!"

        show jenny f_eyeroll
        jenny "Ayolah!"

    jump jenny_cunni_repeat


label jenny_cunni_repeat:
    scene bedroom_sex2
    if M_jenny.is_state(S_jenny_give_cunni):
        show jennysex 135 at right
    else:
        show jennysex 137 at right
    show jennysex_cunnilingus_player at right
    with fade
    if M_jenny.is_state(S_jenny_give_cunni):
        jenny "Hehe, ingat air mani yang kamu tembakkan ke seluruh selimutku?!"

        jenny "Ini waktunya balas dendam, jalang!"

        show jennysex 134
        anon "Hei, aku mencucinya untukmu!"

        show jennysex 135
        jenny "Ha ha ha!"

        show jennysex 137 with dissolve
    pause
    show jennysex 137b
    jenny "Nah, tunggu apa lagi, undangan?!"

    jenny "Jilat vaginaku-"

    $ M_jenny.set('sex speed', .3)
    show expression AnimatedImage("jenny_lick_shirt", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with fastdissolve
    jenny "Eeyyyy!!!"

    pause
    jenny "Sial!"

    pause
    jenny "Mmm, lidahmu terasa luar biasa!"

    jenny "Ahhh!"

    pause
    show jennysex 135
    show jennysex_cunnilingus_player at right
    with dissolve
    jenny "Lebih fokus pada klitorisku, bodoh!"

    jenny "... Dan mainkan payudaraku juga!"

    show jennysex 134
    if M_jenny.get("dominance") <= 0:
        anon "Baiklah."

        show jennysex 135
        jenny "{i}*Ahem*{/i} Baiklah, apa?"

        show jennysex 134
        anon "{i}*Huh*{/i} Baiklah, {b}Putri [jen_name]{/b}..."

        show jennysex 135
        jenny "Ha ha ha!"

        jenny "Itu benar, pecundang!"

    else:
        anon "Tanyakan baik-baik atau aku akan berhenti..."

        show jennysex 135
        jenny "Apa?!"

        jenny "Ya Tuhan, kamu tidak bisa berhenti sekarang!"

        show jennysex 134
        anon "Awasi aku."

        show jennysex 135
        jenny "Tidak tidak tidak!"

        show jennysex 134
        jenny "Grr!"

        show jennysex 135
        jenny "Tolong, mainkan payudaraku, {b}[firstname]{/b}..."

    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .2)
    show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
    hide jennysex_cunnilingus_player
    with dissolve
    jump jenny_lick_loop

label jenny_lick_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_lick", [1,2,3,4], M_jenny) as jennysex at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_lick_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_lick {}".format(pose_list[pose_counter]) as jennysex at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_lick_hscene_dialog")
        $ animcounter += 1
    call screen jenny_lick_options

label jenny_lick_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        jenny "!!!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        jenny "Di sana!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "Begitu saja.{p=1}{nw}"

        jenny "Ya!!{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        jenny "Mmm, aku semakin dekat!{p=2}{nw}"

    return

label jenny_lick_cum:
    jenny "aku akan-"

    jenny "Astaga!"

    pause
    show jennysex 143
    jenny "NGGHHH!!!" with flash
    show jennysex 135c
    show jennysex_cunnilingus_player at right
    with dissolve
    jenny "Haah... Haah..."

    show jennysex 134c
    anon "Sheesh, kamu membuatku basah kuyup."

    pause
    show jennysex 135c
    jenny "Psh, kamu menyukainya!"

    show jennysex 134c
    anon "Ya benar..."

    show jennysex 135c
    jenny "Hehehe!"

    hide jennysex
    hide jennysex_cunnilingus_player
    with dissolve
    scene expression player.location.background_blur with None
    show jenny f_normal b_pantieless
    show anon f_worried
    with dissolve
    jenny "Fiuh, baiklah... Itu cukup bagus."

    anon "Ya, untukmu."

    show jenny f_laugh
    jenny "Ha ha ha!"

    show jenny f_normal
    jenny "Jangan khawatir, aku akan menjagamu nanti."

    show jenny f_grin
    jenny "Mungkin..."

    pause
    jenny "... Jika kamu anak baik."

    anon "Ayo, {b}[jen_name]{/b}..."

    show jenny f_upset
    jenny "Tidak."

    show jenny f_grin
    jenny "Lagi pula, apa kamu tidak punya pakaian untuk dicuci?!"

    anon f_grumpy @ -m_talk "..."
    show jenny a_panties with dissolve
    jenny "Nanti, pecundang!"

    hide jenny with dissolve
    jenny "Hahahaah!"

    anon f_unimpressed "{i}*Huh*{/i}"

    hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["10_unlocked"] = True
    $ player.go_to(L_home_bedroom)
    $ game.timer.tick()
    $ M_jenny.trigger(T_jenny_gave_cunni)
    $ game.main()


label jenny_bj_intro_repeat:
    show anon f_worried
    anon "Lisan."

    show jenny f_upset
    jenny "Ayo cepat."

    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Ya?"

    anon @ -m_talk "Hmm?"

    jenny "Lepaskan pakaian itu!"

    show jenny f_grin_down b_naked a_panties_remove with dissolve
    anon f_worried "B-benar..."

    show jenny b_naked_panties_remove_down with dissolve
    pause

    label finger_blasting_bj:
    scene expression "backgrounds/location_home_jennybedroom_cutscene05.jpg"
    with fade
    jenny "Anda tahu latihannya."

    jenny "Pakai masker dan tutup mulut."

    anon "Ya, saya ingat."

    jenny "Aku akan menangani sisanya."


    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_bellytype f_sexy_down
    with fade
    jenny "Hai lagi, semuanya!"

    jenny "Aku membawa mainan anakku kembali untuk memberi kalian pertunjukan lagi."

    pause
    show jenny f_laugh
    jenny "Hehe, tentu saja!"

    show jenny b_bed_climbing
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X od_bed_jenny_laying_dick1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick1.png"
    with dissolve
    pause
    show jenny b_bed_back_sit a_sit_handcuffs with dissolve
    anon "Borgol lagi?!"

    show jenny a_sit_tie
    show anon oh_bed_jenny_laying_undies_handcuffs
    with dissolve
    jenny "Ssst!"

    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick1.png"
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
    with dissolve
    anon "{b}[jen_name]{/b}, aku tidak mau-"

    jenny "Diam!"

    show jenny b_bed_back_look a_up f_normal with dissolve
    jenny "Di sana."

    jenny "Mari kita lihat apakah teman kita sudah bangun, hmm?"

    show jenny b_bed_front_sit a_sides f_sexy_down with dissolve
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick7.png"
    show jenny a_pull1
    with dissolve
    pause
    show jenny a_pull2 with dissolve
    jenny "!!!"
    jenny "Halo sobat besar."

    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show anon od_bed_jenny_laying_dick6
    show jenny b_bed_front_laying
    with dissolve
    jenny "Kalian siap bersenang-senang?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    anon "Apa yang akan kita lakukan-"

    show jenny b_bed_pussy1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    anon "!!!" with hpunch
    anon "Mrphmmmmll-"

    jenny "Apa itu tadi, mainan anak laki-laki?"

    jenny "Kami tidak dapat mendengarmu... Hahahaah!"

    show anon od_empty
    show jenny b_bed_pussy
    with dissolve
    pause
    jenny "Mmm, sial ya!"

    pause
    show jenny f_nipple2
    jenny "Ahhh!"

    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Kamu sangat pandai dalam hal ini!"

    show jenny f_nipple3
    anon "Ermmhnnn!"

    show jenny f_nipple2
    jenny "Ha ha ha!"

    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Aku semakin dekat!"

    show jenny f_nipple3
    pause
    show jenny f_nipple2
    jenny "Ya Tuhan!"

    jenny "Di sana!!"

    show jenny f_nipple3
    pause
    show jenny b_bed_pussy1 f_nipple2
    jenny "NGGHHH!!!" with flash
    pause
    hide expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    show jenny b_bed_front_laying
    show anon od_bed_jenny_laying_dick6
    with dissolve
    jenny "Haah... Haaah..."

    anon "{i}*Terkesiap*{/i}"

    anon "{i}*Batuk* *Gagap* *Batuk*{/i}"

    anon "Sial, {b}[jen_name]{/b}!"

    anon "Anda tahu saya tidak bisa bernapas ketika Anda melakukan itu!"

    show jenny f_laugh
    jenny "Hehehe!"

    show jenny f_sexy_down
    anon "Itu tidak lucu!"

    jenny "Oh, diamlah..."

    jenny "Penggemarku tidak ingin mendengar keluh kesahmu."

    pause
    jenny "Ah, benarkah?"

    pause
    show jenny f_eyeroll
    jenny "{i}*Huh*{/i} Lagi?!"

    show jenny f_sexy_down
    pause
    jenny "Yah, aku tidak akan melakukannya kecuali kalian-"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny f_surprised_down
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Demi Tuhan..."

    show jenny f_sexy_down
    anon "Sekarang apa yang terjadi?"

    jenny "Penismu akan dihisap lagi."

    anon "B-benarkah?"

    anon "Itu menakjubkan-"

    show jenny b_bed_pussy1
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick6.png"
    with dissolve
    anon "Srrmmmph!"

    jenny "Diam!"

    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .12)
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
    anon "Nnnrrrmmph-" with hpunch
    jenny "{i}*Gluulggh*{/i}"

    jump jenny_bj_loop

label jenny_bj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_bj", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_bj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_bj {}".format(pose_list[pose_counter]) as jenny_bj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_bj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_bj_options

label jenny_bj_hscene_dialog:
    if animcounter == 0 and randomizer() < 50:
        jenny "Hmm.{p=1}{nw}"

    if animcounter == 1 and randomizer() > 50:
        jenny "{i}*Menyeruput*{/i}{p=1}{nw}"

    if animcounter == 2 and randomizer() < 50:
        anon "...{p=1}{nw}"

    if animcounter == 3 and randomizer() > 50:
        jenny "{i}*Slurrrrrp*{/i}{p=1}{nw}"

    return

label jenny_bj_cum:
    if jen_name == 'Jenny':
        anon "Jrrnnnneeeee!"

    else:
        anon "Hhhrreeeee!"

    anon "Mmy grrn krrrwwws!!"

    pause
    if jen_name == 'Jenny':
        anon "Jrrnnnneeee!!!"

    else:
        anon "Hrrmmmmmphhhh!!!"

    pause
    show jenny_bj cum
    anon "HrrrNNGGG!!!" with flash
    jenny "!!!"
    pause
    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
    show anon b_bed_jenny_laying_undies_arms of_bed_jenny_laying_undies_arms_mask_X oh_bed_jenny_laying_undies_handcuffs od_bed_jenny_laying_dick3
    show jenny b_bed_front_sit a_shocked f_cheeks_surprised o_laptop
    show expression "characters/anon/anon_overlay_dick_od_bed_jenny_laying_dick3.png"
    with dissolve
    jenny "{i}*Meneguk*{/i}"

    show jenny f_cheeks_angry
    jenny "{i}*Batuk* *Gagap* *Batuk*{/i}"

    if M_jenny.is_state(S_jenny_start_camshow_blowjob):
        show jenny b_bed_back_sit a_sit_hips with dissolve
        jenny "Sialan!!"

        jenny "Kau datang tepat ke tenggorokanku!"

        show jenny b_bed_climbing with dissolve
        jenny "Eugh, aku menelannya banyak!"

        show jenny b_bed_side f_angry a_laptop with dissolve
        anon "aku mencoba memperingatkanmu..."

        jenny "Omong kosong, aku tidak mendengar apa pun!"

        anon "Ya, mungkin karena kamu menabrak wajahku!"

        jenny "Cih, terserah..."

        show jenny b_bed_side_laptop f_gross_down with dissolve
        pause
        jenny "Grr, itu tidak lucu!"

        jenny "Itu menjijikkan!"

        pause
        jenny "Ugh, kalian semua brengsek!"

        jenny "Pertunjukan berakhir!"

        scene black with fade
        pause
        scene expression player.location.background_blur with None
        show jenny b_naked a_hips f_angry
        show anon f_surprised b_underwear
        with dissolve
        jenny "Sulit dipercaya!"

        anon f_worried "Aku benar-benar mencoba memperingatkan-"

        jenny "Aku tidak ingin mendengarnya!"

        jenny "Diam saja!"

        show jenny f_gross_down
        jenny "Eugh, aku harus pergi menyikat gigiku!"

        hide jenny with dissolve
        pause
        anon "Hei, bagaimana dengan uangku?!"

        pause
        anon @ -m_talk "(Hmm, kurasa aku akan menanyakannya saja besok.)"

        hide anon with dissolve
        $ M_jenny.trigger(T_jenny_done_camshow_blowjob)
    else:
        show jenny b_bed_back_sit a_sit_hips with dissolve
        jenny "Fiuh, senang sekarang?"

        anon "Aku sudah memperingatkanmu lagi!"

        jenny "Aku tahu."

        pause
        jenny "Aku hanya tidak berharap banyak..."

        show jenny b_bed_climbing with dissolve
        anon "T-tunggu, jadi kamu-"

        show jenny b_bed_side_laptop f_sexy_down a_laptop with dissolve
        jenny "Tunjukkan pada anak laki-laki!"

        jenny "Terima kasih telah mendengarkan!"

        pause
        jenny "Hehe, sampai jumpa lagi!"

        scene black with fade
        pause
        scene expression player.location.background_blur with None
        show jenny b_naked a_hips f_normal
        show anon b_underwear f_surprised
        with dissolve
        anon "K-kamu sengaja menelannya?"

        show jenny f_upset
        jenny "Ya?"

        anon f_surprised_teeth "!!!"
        jenny "Jangan punya ide apa pun, itu hanya apa yang ingin dilihat para penggemar..."

        anon f_worried "O-oh."

        show jenny a_money with dissolve
        jenny "Ini potonganmu."

        show jenny a_sides with dissolve
        anon f_normal "Terima kasih."

        show jenny f_angry
        jenny "Sekarang keluarlah!"

        show anon f_surprised
        hide jenny with dissolve
        jenny "Eugh, aku perlu obat kumur!"

        anon f_grin "..."
        hide anon with dissolve
        call popup ('earn', 100)
        $ player.get_money(100)
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["09_unlocked"] = True
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()

label jenny_couch_fj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_couch_dick_rub", [1,2,3], M_jenny) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_couch_dick_rub {}".format(pose_list[pose_counter]) as jenny_couch_dick_rub at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_couch_fj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_couch_fj_options

label jenny_couch_fj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        show jenny f_sexy_down
        jenny "Apakah rasanya enak?{p=1}{nw}"

        show anon f_couch_sit_down
        anon "Ya.{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        show jenny f_sexy_down
        jenny "Apakah kalian semakin dekat?{p=1}{nw}"

        show anon f_couch_sit_down
        anon "Y-ya.{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        show anon f_couch_sit_right
        if randomizer() > 50:
            anon "Kamu benar-benar ahli dalam hal ini!{p=2}{nw}"

        else:
            anon "Sialan!{p=1}{nw}"

        show anon f_couch_sit_down
        show jenny f_laugh
        jenny "Hehehe!{p=1}{nw}"

        show jenny f_sexy_down
    return

label jenny_couch_fj_cum:
    if M_jenny.finished_state(S_jenny_catch_her_jilling):
        show anon f_couch_sit_down_surprised
        anon "Ini dia!"

        pause
    show anon f_couch_sit_down_surprised
    hide jenny_couch_dick_rub
    show jenny a_dick3
    anon "HNNGGG!!!" with flash
    show jenny_player_couch_cum zorder 3 with dissolve
    show anon f_couch_sit_down
    pause
    show anon f_couch_sit_right
    show jenny f_laugh
    jenny "Pfft, hahaha!"

    hide jenny_player_couch_cum
    show anon a_boner
    show jenny a_after2 f_sexy_down
    with dissolve
    if M_jenny.is_state(S_jenny_catch_her_jilling):
        $ M_jenny.trigger(T_jenny_gave_footjob)
        jenny "Aku baru saja membuatmu cum dengan kakiku!"

        jenny "Aku seperti, dewi seks total!!"

        show jenny a_after1 f_sexy_down with dissolve
        anon "Itu luar biasa!"

        jenny "Saya tahu, kan?"

        jenny "Sama-sama, pecundang."

        show jenny b_couch_transition zorder 0 with dissolve
        anon "Kemana kamu pergi?"

        show jenny b_couch_sit a_rest f_sexy with dissolve
        jenny "Umm, untuk mencuci kakiku?"

        show jenny a_after2 with dissolve
        jenny "Kecuali Anda ingin membersihkannya dengan lidah Anda?"

    else:
        jenny "Sheesh, lihat kekacauan yang kamu buat pada kaki kecilku yang cantik!"

        jenny "Anda yakin tidak ingin membersihkannya dengan lidah Anda?!"

    show jenny f_sexy a_after1 with dissolve
    if M_jenny.get("dominance") <= 0:
        anon "Tolong, jangan membuatku melakukan itu..."

        show jenny f_laugh
        jenny "Ha ha ha!"

        show jenny f_sexy
        jenny "Kalau begitu, jangan ajukan pertanyaan bodoh."

    else:
        anon "Eh, tidak mungkin!"

        show jenny f_laugh
        jenny "Ha ha ha!"

        show jenny f_sexy
        jenny "Aduh, ayolah..."

        show jenny a_after2 with dissolve
        jenny "Jilat jari kakiku, {b}[firstname]{/b}!"

        anon "Lupakan!"

        show jenny f_laugh
        jenny "Ha ha ha!"

        show jenny f_sexy
        jenny "Bagus."

    jenny "Aku mau mandi."

    jenny "Sampai jumpa, mesum."

    hide jenny with dissolve
    show anon f_couch_sit_down
    anon @ -m_talk "(Fiuh, itu luar biasa!)"

    show anon b_couch_sit_watching f_couch_sit_watching_straight with dissolve
    anon "(Saya harus mematikannya dan tidur sebelum {b}[deb_name]{/b} mendengarnya. )"

    hide anon with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    $ game.main()

label jenny_computer_video_ec:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cover f_cam_intro_normal
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jenny "Maaf kawan... Bagian selanjutnya ini hanya untuk pelanggan."

    jenny "Sebaiknya segera bayar jika tidak mau ketinggalan!!"

    pause
    show jenny a_reveal with dissolve
    jenny "Hehe, baiklah. Siapa yang siap menjadi nakal?"

    show jenny a_electro f_cam_intro_normal_left with dissolve
    jenny "Aku punya mainan baru yang bagus di sini... Hanya untuk kalian!"

    jenny "Mmm, aku tidak sabar untuk menggoda klitorisku dengan ini..."

    pause
    show jenny f_cam_intro_normal
    jenny "Mengapa kalian tidak memberi saya sedikit insentif?"

    show jenny f_cam_intro_normal_down
    "{i}*PING*{/i}"

    "{i}*PING*{/i}"

    jenny "Oh, ayolah... Kamu bisa melakukan yang lebih baik dari itu, bukan?"

    jenny "Memekku benar-benar sakit untuk mendapat perhatian..."

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Hehe, itu lebih baik!"

    pause
    show jenny b_cam_electro_talk with dissolve
    jenny "Ah, aku basah sekali..."

    hide jenny
    show expression AnimatedImage("jenny_electro", [1,2,3,4], M_jenny) as jenny_toy
    with dissolve
    jenny "Oh ya!"

    pause
    jenny "Ini sangat bagus!"

    pause
    jenny "Mmm, ayolah teman-teman, aku butuh lebih banyak cinta!"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Itu dia! Saya semakin dekat!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    hide jenny_toy
    show jenny b_cam_electro_insert
    jenny "Ahh!!" with hpunch
    pause
    show jenny b_cam_electro_talk with dissolve
    jenny "hehe! Bagaimana tadi?!"

    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    jenny "Hmm, kamu ingin aku membuat sesuatu yang lebih besar lain kali?"

    pause
    jenny "Dubur?!"

    jenny "Kamu benar-benar ingin aku melakukan sesuatu, {b}sam9{/b}?"

    jenny "Cih, kalian sangat menuntut!"

    pause
    jenny "Hmm, kalau aku dapat tiga puluh pelanggan lagi, aku akan mendapat sesuatu yang lebih besar, oke?"

    pause
    jenny "Ya saya berjanji."

    pause
    jenny "Saya tidak tahu tentang analnya, {b}sam9{/b}... Kita lihat saja..."

    pause
    anon "(Wow, panas sekali!)"

    anon "(Saya harus melihat apa lagi yang dia punya...)"

    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["03_unlocked"] = True
    return

label jenny_computer_video_uv:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cover f_cam_intro_normal
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jenny "Maaf kawan... Bagian selanjutnya ini hanya untuk pelanggan."

    jenny "Anda masih bisa masuk dan menonton jika Anda terburu-buru!!"

    pause
    show jenny a_reveal with dissolve
    jenny "Hehe, baiklah. Aku sudah berjanji pada kalian, bukan?"

    show jenny a_vibrate f_cam_intro_normal_left with dissolve
    jenny "Apa pendapatmu tentang pria besar ini, ya?"

    jenny "Sudah kubilang semuanya, aku akan mendapatkan sesuatu yang lebih besar."

    show jenny f_cam_intro_normal_down
    pause
    show jenny a_back with dissolve
    jenny "Tidak, {b}sam9{/b}... Itu tidak akan masuk ke pantatku."

    jenny "Ya, ya... Mungkin di masa depan, kita lihat saja nanti."

    pause
    jenny "Sekarang, bagaimana dengan insentif untuk dewi seks Anda?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Hehe, itu yang ingin saya lihat!"

    jenny "Sedikit lagi!"

    pause
    show jenny a_vibrate with dissolve
    jenny "Tidakkah kamu ingin melihatku cum di seluruh mainan ini?"

    "{i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Ini dia!"

    pause
    show jenny b_cam_vibrate_talk with dissolve
    jenny "Hehe, aku tidak tahu apakah itu akan muat di dalam vagina kecilku yang ketat..."

    hide jenny
    show expression AnimatedImage("jenny_vibrate", [1,2,3,4], M_jenny) as jenny_toy
    with dissolve
    pause
    jenny "Oh, sial..."

    pause
    jenny "Haah!"

    pause
    jenny "Mmm, ayo teman-teman, tunjukkan uangnya!"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Itu dia! Rasanya enak sekali!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "aku semakin dekat!!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Oh sial ya!!"

    hide jenny_toy
    show jenny b_cam_vibrate_cum1
    jenny "Ahh!!" with hpunch
    pause
    pause
    show jenny b_cam_vibrate_cum2 with dissolve
    jenny "Hehe, sepertinya aku membuat kekacauan..."

    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    anon "(Wow, apakah dia baru saja muncrat?! )"

    jenny "Sepertinya aku harus mencuci sepraiku..."

    pause
    jenny "Apa?!"

    jenny "Aku tidak akan mengirimimu sepraiku!"

    pause
    jenny "Anda akan membayar saya berapa?"

    pause
    jenny "aku akan memikirkannya..."

    jenny "Untuk saat ini, aku hanya ingin-"

    jenny "Hmm?"

    pause
    jenny "Kalian ingin melihatku dengan penis asli?"

    pause
    jenny "Mungkin..."

    pause
    jenny "Hah, {b}sam9{/b} ingin melihatku dengan penis sungguhan, di pantatku... Kejutan besar."

    pause
    jenny "Kalian bodoh."

    anon "(Wow, saya mengerti mengapa dia menghasilkan uang dengan melakukan ini...)"

    jenny "Sampai ketemu lagi, oke?"

    anon "( Hmm, saya kira itu saja untuk video itu. )"

    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["04_unlocked"] = True
    return

label jenny_computer_video_bm:
    scene expression "backgrounds/location_home_jennybedroom_cam1.jpg"
    show jenny b_cam_intro a_cover f_cam_intro_normal
    show expression "characters/jenny/layeredimage/jenny_webcam_border.png"
    with dissolve
    jenny "Maaf kawan... Bagian selanjutnya ini hanya untuk pelanggan."

    jenny "Kalian harus membayar dan bergabung dengan kami hari ini!"

    jenny "Peringatan spoiler!"

    show jenny a_monster f_cam_intro_normal_left with dissolve
    jenny "Hal ini masuk ke dalam diriku hari ini!"

    jenny "Saya berharap dapat melihat Anda di sana!"

    show jenny f_cam_intro_normal_down
    pause
    show jenny a_back with dissolve
    jenny "Hehe, baiklah. Mari kita tunggu sebentar dan lihat apakah ada orang lain yang bergabung..."

    pause
    jenny "Ya, aku serius!"

    jenny "Aku akan membuat diriku bodoh pada monster ini!"

    show jenny f_cam_intro_normal
    pause
    jenny "Ugh, iya... Baiklah, {b}sam9{/b}. Aku akan memasukkannya ke dalam."

    jenny "Anda lihat itu teman-teman?"

    jenny "Saya memberikan {b}sam9{/b} apa yang dia inginkan karena dia selalu murah hati dengan tipnya!"

    pause
    jenny "Benar, beri tip lebih banyak dan Anda akan mendapatkan apa yang Anda inginkan juga."

    show jenny f_cam_intro_normal_down
    pause
    jenny "Sial, kami punya hampir dua ratus pelanggan baru untuk acara ini!"

    jenny "Sepertinya kalian haus akan dewi seks kalian, ya?"

    pause
    show jenny f_cam_intro_normal
    jenny "Oke, hal pertama yang pertama..."

    show jenny b_cam_monster_talk with dissolve
    jenny "Ini untuk {b}sam9{/b}!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    show jenny b_cam_monster_talk2 with dissolve
    jenny "NGGGHHH!!"

    jenny "Sam sialan!"

    pause
    jenny "Ya, aku tahu... Ini semakin berkembang dalam diriku."

    pause
    jenny "Aku baru saja bilang aku menyukainya, bukan?!"

    jenny "Perhatikan, bodoh!"

    pause
    jenny "Tidak, itu tidak berarti saya mendapatkan sesuatu yang lebih besar."

    pause
    jenny "Baiklah, cukup dengan hal-hal anal..."

    show jenny b_cam_monster_talk3 with dissolve
    jenny "Saatnya acara utama!"

    pause
    jenny "Apakah kalian siap?"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jenny "Aku tidak bisa mendengarmu!!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Hehe, ini dia!"

    pause
    show jenny b_cam_monster_anim1 with dissolve
    jenny "Haah..."

    show jenny b_cam_monster_anim2 with dissolve
    jenny "Ya Tuhan..."

    jenny "It's fucking huge!"

    pause
    show jenny b_cam_monster_anim3 with dissolve
    jenny "Holy shit!!!"

    pause
    jenny "Oke..."

    $ M_jenny.set("sex speed", 0.175)
    hide jenny
    show expression AnimatedImage("jenny_monster", [4,1,2,3], M_jenny) as jenny_toy
    with dissolve
    pause
    jenny "Ahh!!"

    pause
    jenny "Oh, yes, yes, YES!!!"

    pause
    jenny "Oh my god you guys, this is amazing!"

    "{i}*PING*{/i} {i}*PING*{/i}"

    pause
    jenny "AH FUCK!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "aku akan keluar!!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "YA!!"

    $ M_jenny.set("sex speed", 0.6)
    show expression AnimatedImage("jenny_monster", [2,3], M_jenny) as jenny_toy
    jenny "Ngghhh!!!" with hpunch
    pause
    hide jenny_toy
    show jenny b_cam_monster_after
    with dissolve
    pause
    jenny "Haah... Haah..."

    jenny "Wow, that was-"

    pause
    scene expression game.timer.image("backgrounds/location_home_bedroom_desk_cam{}.jpg") as cutscene
    show player 311 at Position(xpos = 672)
    with dissolve
    anon "(Sial!)"

    jenny "Oh my god, look at how much I'm shaking..."

    pause
    jenny "Phew, just give me a second."

    pause
    jenny "Hahaha! I told you guys it was gonna be worth it."

    pause
    jenny "Saya tahu, kan?"

    pause
    jenny "Yeah, I know you want to see me ride a real dick..."

    jenny "It's coming, okay?"

    jenny "Just have your wallets ready, 'cause I'm expecting a LOT of tips for that show."

    pause
    jenny "Hehe, ya."

    pause
    jenny "You're welcome, {b}sam9{/b}."

    pause
    jenny "Yeah, I'll see you all next time."

    pause
    jenny "Buh bye, boys."

    anon "( Totally worth it. )"

    anon "(Itu luar biasa!)"

    hide cutscene
    hide player
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["05_unlocked"] = True
    return

label jenny_hj_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("jenny_hj_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,4,3,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "jenny_hj {}".format(pose_list[pose_counter]) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("jenny_hj_hscene_dialog")
        $ animcounter += 1
    call screen jenny_hj_options

label jenny_hj_hscene_dialog:
    if animcounter == 0 and randomizer() < 10:
        anon "Sialan!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 10:
        anon "Ya Tuhan!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 10:
        jenny "Mmm, I can feel it throbbing...{p=2}{nw}"

        "{i}*PING*{/i} {i}*PING*{/i}{p=1}{nw}"

    if animcounter == 3 and randomizer() < 10:
        anon "Saya semakin dekat...{p=2}{nw}"

        if M_jenny.get("sex speed") > 0.051:
            $ M_jenny.set("sex speed", M_jenny.get("sex speed") - 0.025)
        anon "Ya Tuhan!{p=1}{nw}"

    return

label jenny_hj_cum:
    if M_jenny.is_state(S_jenny_start_camshow_handjob):
        jenny "I wonder what else I shou-"

        hide jenny_hj
        show jenny_hj_mc cum
        anon "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jenny "{i}*Terkesiap*{/i}"

        pause
        jenny "What the fuck!"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        anon "Fiuh..."

        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show anon b_bed_jenny_laying od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask_X
        show jenny b_bed_side f_angry o_laptop a_cum
        with dissolve
        jenny "Why didn't you warn me!"

        show jenny f_angry
        anon "You didn't tell me to warn you..."

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        jenny "Well, I thought that was fucking obvious you moron!"

        jenny "Oh my god, it's everywhere!"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        jenny "Ugh, okay... Stream's over!"

        anon "B-but they're still tipping-"

        jenny "GET THE FUCK OUT OF MY ROOM!"

        anon "Oke oke..."

        hide anon with dissolve
        show jenny f_gross_down
        jenny "Ya."

        pause
        show jenny b_bed_side_laptop f_gross_down with dissolve
        jenny "Itu tidak lucu!"

        scene black with fade
        pause
        $ game.timer.tick()
        $ M_jenny.trigger(T_jenny_gave_handjob)
        $ player.go_to(L_home_bedroom)
        scene expression player.location.background_blur with None
        show anon f_surprised with dissolve
        anon @ -m_talk "(Wah!)"

        anon f_flirt @ -m_talk "( I can't believe {b}[jen_name]{/b} just jerked me off... )"

        anon @ -m_talk "( That was so hot!! )"

        pause
        anon f_grin @ -m_talk "( Man, I hope I get to do that again! )"

        hide anon with dissolve
    else:
        anon "Ini dia!"

        jenny "Hmm?"

        hide jenny_hj
        show jenny_hj_mc cum
        anon "HNNGGG!!!{p=1}{nw}" with flash
        show jenny_hj_cum
        jenny "!!!"
        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg" with None
        show anon b_bed_jenny_laying od_bed_jenny_laying_dick3 of_bed_jenny_laying_mask_X
        show jenny b_bed_side f_angry o_laptop a_cum
        with hpunch
        jenny "Lagi?!"

        jenny "Goddamnit, you asshole!"

        anon "Aku sudah memperingatkanmu!"

        jenny "Well, I wasn't paying attention!"

        "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

        show jenny f_gross_down
        jenny "Ya."

        show jenny b_bed_side_laptop with dissolve
        jenny "Yeah, yeah... Very funny."

        jenny "Show's over pervs!"

        hide jenny
        hide anon
        with dissolve
        scene expression game.timer.image("backgrounds/location_home_jennybedroom{}.jpg")
        show anon f_surprised b_underwear
        show jenny b_naked f_upset a_hips
        with dissolve
        jenny "You're washing my sheets this time!"

        anon f_worried "Fine, whatever."

        jenny "I'm getting in the shower."

        show jenny a_money with dissolve
        jenny "Take this and get the fuck out!"

        hide jenny with dissolve
        pause
        anon f_normal "Manis!"

        hide anon with dissolve
        call popup ('earn', 50)
        $ player.get_money(50)
        $ game.timer.tick()
        $ player.go_to(L_home_basement)
        scene expression player.location.background_blur
        show anon f_normal
        with fade
        anon "Fiuh!"

        anon "Alright, that's done."

        pause
        anon f_laugh "Totally worth it!"

        hide anon with dissolve
    $ renpy.end_replay()
    $ persistent.cookie_jar["Jenny"]["unlocked"] = True
    $ persistent.cookie_jar["Jenny"]["gallery"]["07_unlocked"] = True
    $ game.main()

label jenny_hj_intro_repeat:
    show jenny f_upset
    jenny "Ayo cepat."

    show jenny f_grin_down b_pull1 with dissolve
    pause
    show jenny b_pull2 with dissolve
    pause
    show jenny b_pull3 with dissolve
    show jenny b_pull4 with dissolve
    show anon f_surprised
    pause
    show jenny b_panties a_hips f_upset with dissolve
    jenny "Ya?"

    show jenny f_grin_down b_naked a_panties_remove with dissolve
    show anon f_worried
    anon @ -m_talk "Hmm?"

    show jenny b_naked_panties_remove_down with dissolve
    pause
    show jenny b_naked a_hips f_upset with dissolve
    jenny "Lepaskan pakaian itu!"

    anon "B-benar..."


    label finger_blasting_hj:
    scene location_home_jennybedroom_cutscene05
    with fade
    jenny "Anda tahu latihannya."

    jenny "Pakai masker dan tutup mulut."

    anon "Ya, saya ingat."

    jenny "Aku akan menangani sisanya."


    scene expression "backgrounds/location_home_jennybedroom_closeup_peek.jpg"
    $ M_jenny.set('cam show mask', True)
    show anon b_bed_jenny_sit f_shy_down of_mask
    show jenny o_under_body_laptop b_naked_bed_bellytype f_sexy_down
    with fade
    jenny "Hai lagi, semuanya!"

    show jenny b_naked_bed_belly with dissolve
    jenny "Aku membawa mainan anakku kembali untuk memberi kalian pertunjukan lagi."

    pause
    show jenny f_laugh
    jenny "Hehe, tentu saja!"

    show jenny f_sexy_down
    pause
    jenny "Well, let's find out, shall we?"

    show jenny o_laptop b_bed_side a_laptop
    show anon b_bed_jenny_laying od_bed_jenny_laying_dick1 of_bed_jenny_laying_mask_X
    with dissolve
    jenny "I bet he's good and ready this time."

    show jenny a_pull1 f_sexy_down with dissolve
    pause
    show anon od_empty
    show jenny a_pull2
    with dissolve
    pause
    show jenny a_point
    show anon od_bed_jenny_laying_dick4
    with fastdissolve
    show anon od_bed_jenny_laying_dick5 with fastdissolve
    show anon od_bed_jenny_laying_dick6 with fastdissolve
    jenny "!!!"
    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    show jenny b_bed_side_laptop f_sexy_down with dissolve
    jenny "Hehe, I know it's big!"

    jenny "I wouldn't settle for anything less, would I?"

    pause
    jenny "Yeah, I think I should too."

    $ M_jenny.set("sex speed",0.4)
    show jenny b_bed_side a_jerk with dissolve
    anon "!!!"
    pause
    anon "Ya Tuhan!"

    jenny "Yeah, you like that, don't you?"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    pause
    scene expression "backgrounds/location_home_jennybedroom_sex_hj.jpg" with None
    $ animated = True
    $ anim_toggle = True
    $ M_jenny.set('sex speed', .1)
    show jenny_hj_mc
    show expression AnimatedImage("jenny_hj", [1,2,3,4,5,4,3,2], M_jenny) as jenny_hj at Position(xalign = 0.0, yoffset = 0)
    with dissolve
    jenny "C'mon, boy toy!!"

    jenny "Tell everybody how much you love me stroking your big, hard cock..."

    anon "Saya menyukainya!"

    "{i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i} {i}*PING*{/i}"

    jenny "Ha ha ha!"

    pause
    anon "{b}[jen_name]{/b}, I'm gonna-"

    jenny "You boys seeing this?!"

    jenny "Hehe, oh you like my big tits, huh?"

    "{i}*PING*{/i} {i}*PING*{/i}"

    jump jenny_hj_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
