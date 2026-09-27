label dianes_dialogue_breastfeed:
    if store._in_replay:
        scene expression player.location.background_blur
    show player 14 at left
    show diane b_naked a_idle f_smirk
    if store._in_replay:
        with fade
    player_name "Bisakah saya mencicipi susu Anda lagi?"

    show player 13
    diane @ f_laugh "Heh, mau dosis lagi langsung dari keran?"

    show player 17
    player_name "Ya, tolong!"

    show player 13
    diane "Hmm, baiklah."

    diane "Ingatlah untuk tidak minum terlalu banyak, oke?"

    show player 14
    player_name "Ya, saya ingat!"

    hide player
    hide diane
    with dissolve
    if M_diane.is_set("first boobjob"):
        jump diane_first_breastfeed
    jump diane_repeatable_breastfeed

label diane_repeatable_breastfeed:
    if L_diane_shed.is_here(M_diane):
        scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    else:
        scene expression "backgrounds/location_barn_hay_stack.jpg"
    if M_diane.outfit.get == "shirtless":
        $ M_diane.outfit.is_naked = 0
    show diane b_hay_feeding a_stroke f_explain
    with dissolve
    diane "Mmm, mulut hangat itu terasa nikmat setelah seharian memompa."

    show diane f_lip_bite
    pause
    show diane f_explain
    diane "Ahh, bagaimana rasanya hari ini kawan?"

    show diane f_smirk_down
    player_name "Mmhmm!"

    show diane f_laugh
    diane "Hehehe!"

    show diane f_smirk_down
    pause
    show diane f_explain
    diane "Kita seharusnya tidak melakukan ini tetapi untuk beberapa alasan..."

    diane "... Itu membuatku semakin ingin melakukannya!"

    show diane f_lip_bite
    pause
    show diane b_hay_feeding1 with dissolve
    diane "Ngghh!"

    show diane f_shamed_look
    diane "Baiklah, sebaiknya kita berhenti sebelum kamu meminumku sampai kering, kawan."

    show diane f_smirk_down
    player_name "Aduh."

    show diane f_explain
    diane "saya tahu..."

    show diane f_shamed_look
    diane "Kita akan melakukannya lagi lain kali, oke?"

    show diane f_smirk_down
    player_name "Ya baiklah."

    show playersex 1 at right
    if M_diane.outfit.get == "shirtless":
        show diane f_smirk_front b_hay_undress1
    else:
        show diane f_smirk_front b_hay_sit
    with dissolve
    pause
    if M_diane.is_set("first cucumber"):
        $ M_diane.set("first cucumber", False)
        if M_diane.outfit.get == "shirtless":
            $ M_diane.outfit.is_naked = 1

        show diane f_smirk_front
        diane "Apakah kamu masih keras?"

        if M_diane.outfit.get == "shirtless":
            show diane b_hay_dressed with dissolve
        player_name "Eh ya."

        diane "Mengapa kamu tidak mengeluarkan penis sebesar itu untukku?"

        player_name "O-oke."

        show playersex 2 with dissolve
        show diane f_down_front
        pause
        show playersex 4 with dissolve
        pause 1
        show playersex 3 with dissolve
        pause
        show diane f_smirk_front
        diane "Luar biasa!"

        if M_diane.outfit.get == "shirtless":
            diane "Giliranku."

            show diane f_smirk_down b_hay_undress1 with dissolve
            pause
            show diane b_hay_undress2 with dissolve
            pause
            show diane b_hay_naked with dissolve
        diane "Sekarang biarkan aku-"

        hide playersex
        show diane b_hay_rub f_lip_bite
        player_name "!!!" with hpunch
        player_name "Ya Tuhan!"

        pause
        pause
        show diane b_hay_sit f_smirk_front
        show playersex 3
        with dissolve
        player_name "Apakah menurut Anda kita bisa melakukan hal itu lagi?"

        player_name "Kau tahu, dengan payudaramu dan... Uhh..."

        diane "Anda ingin pekerjaan payudara yang lain?"

        player_name "Ya, payudara!"

        diane @ f_laugh "hehe."

        diane "Ya, kita bisa..."

        pause
        diane "... Atau, mungkin, Anda bisa memenuhi kebutuhan saya hari ini?"

        player_name "Hah?"

        player_name "O-oke, tentu saja."

        diane "Anak baik!"

        player_name "Apa yang perlu saya lakukan?"

        diane "Baiklah, mari kita lihat..."

        show diane f_thinking
        pause
        show diane f_smirk_front
        diane "Oh, aku tahu!"

        show diane b_hay_cucumber1 with dissolve
        player_name "Uhh, mentimun?"

        diane "Oh, ayolah, jangan berpura-pura bodoh."

        diane "Saya tahu Anda melihat saya di dapur hari itu."

        player_name "Y-ya, tapi kamu ingin aku-"

        diane @ f_laugh "Mmhmm!"

        pause
        player_name "Baiklah."

        show diane b_hay_cucumber2 with dissolve
        pause
        show diane b_hay_behind_talk
        show playersex 18
        with dissolve
        diane "Bersikaplah lembut, oke?"

        show diane b_hay_behind
        player_name "Oke."

        show diane b_hay_behind_pre with dissolve
        pause
        hide playersex
        show diane b_hay_insert1
        with dissolve
        player_name "Seperti ini?"

        diane "Hmm, begitu saja!"

        hide diane
        jump diane_cucumber_start
    else:

        if M_diane.outfit.get == "shirtless":
            show diane b_hay_dressed with dissolve

        menu:
            "pekerjaan payudara.":
                show playersex 1 at right
                show diane f_smirk_front
                with dissolve
                player_name "Apa menurutmu kita bisa melakukan hal boobjob itu lagi?"

                diane "Tentu, kita bisa melakukan itu."

                diane "Lepaskan celana itu dan duduklah di sini."

                show playersex 2
                if M_diane.outfit.get == "shirtless":
                    show diane f_smirk_down b_hay_undress1
                with dissolve
                pause
                show playersex 4 with dissolve
                pause 1
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_undress2 f_down_front
                show playersex 3
                with dissolve
                pause
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_naked with dissolve
                    pause
                hide diane
                hide playersex

                scene expression "backgrounds/location_barn_floor_boobjob.jpg"
                if M_diane.outfit.get == "shirtless":
                    $ M_diane.outfit.is_naked = 1
                show diane_sex_boobjob 2
                show diane_sex_boobjob_look talk
                with dissolve
                diane "Anda sangat menyukai ini, ya?"

                hide diane_sex_boobjob_look

                jump diane_boobjob_start
            "Timun.":

                show playersex 1 at right
                show diane f_smirk_front
                with dissolve
                player_name "Apakah Anda ingin menggunakan mentimun lagi?"

                diane "Tentu saja!"

                show playersex 2
                if M_diane.outfit.get == "shirtless":
                    show diane f_smirk_down b_hay_undress1
                else:
                    show diane f_down_front
                with dissolve
                pause
                show playersex 4 with dissolve
                pause 1
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_undress2 f_down_front
                show playersex 3
                with dissolve
                pause
                if M_diane.outfit.get == "shirtless":
                    show diane b_hay_naked with dissolve
                    pause
                    $ M_diane.outfit.is_naked = 1
                show diane f_smirk_front b_hay_cucumber1 with dissolve
                diane "Bersikaplah lembut saja, oke?"

                show playersex 18
                show diane b_hay_behind
                with dissolve
                player_name "Saya akan."

                show diane b_hay_behind_pre with dissolve
                player_name "Ini dia..."

                hide playersex
                show diane b_hay_insert1
                with dissolve
                pause
                hide diane
                jump diane_cucumber_start
            "Sebaiknya aku kembali bekerja.":

                if store._in_replay is None:
                    scene expression player.location.background_blur with None
                else:
                    scene expression L_diane_shed.background_blur with None
                if M_diane.outfit.get == "shirtless":
                    $ M_diane.outfit.is_naked = 1

                    show diane b_shirtless f_smirk
                else:
                    show diane b_naked f_smirk
                show player 13 at left
                with dissolve
                diane "Sekarang kembalikan pantat imutmu!"

                show player 14
                player_name "Ya, Bu!"

                hide player
                hide diane
                with dissolve
                $ renpy.end_replay()
    $ game.main()

label diane_cucumber_start:
    $ animated = True
    $ anim_toggle = True
    $ M_diane.set('sex speed', .4)
    show expression AnimatedImage("diane_hay_insert", [1,2], M_diane) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
    diane "Ahhh!!"

    player_name "Wah, kamu basah banget, {b}Diane{/b}!"

    jump diane_cucumber_loop

label diane_cucumber_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("diane_hay_insert", [1,2], M_diane) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_cucumber_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_hay_insert {}".format(pose_list[pose_counter]) as diane_hay_insert at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_cucumber_hscene_dialog")
        $ animcounter += 1
    call screen diane_cucumber_options

label diane_cucumber_cum:
    diane "Saya hampir sampai!"

    if randomizer() < 50:
        diane "Jangan berhenti!"

    else:
        diane "Persetan denganku!"

    pause
    diane "NGGHHH!!!" with flash
    hide diane_hay_insert
    show diane b_hay_insert1
    with dissolve
    diane "Haah... Haah..."

    show playersex 18
    show diane b_hay_behind_pre
    with dissolve
    pause
    show diane b_hay_behind_talk with dissolve
    diane "Oh, itu luar biasa {b}[firstname]{/b}!"

    show diane b_hay_behind
    if randomizer() < 50:
        player_name "Hehe, kamu datang dengan sangat keras!"

        show diane b_hay_behind_talk
        diane "Benar, hehe!"

    else:
        player_name "Hehe, ya, itu menyenangkan!"

        player_name "Anda gemetar seperti orang gila di ujung sana."

        show diane b_hay_behind_talk
        diane "hehe!"

    diane "Itu karena kamu merawatku dengan baik."

    show diane b_hay_behind
    pause
    show diane b_hay_behind_talk
    diane "Terima kasih untuk itu."

    show diane b_hay_behind
    player_name "Tidak masalah."

    show diane b_hay_behind_talk
    diane "Haah... aku perlu istirahat sejenak."

    diane "Anda baik-baik saja kembali bekerja?"

    show diane b_hay_behind
    player_name "T-tentu saja."

    show diane b_hay_behind_talk
    diane "Anak baik."

    show diane b_hay_behind
    hide playersex with dissolve
    pause
    show diane b_hay_behind_pre with dissolve
    diane "Fiuh!"

    diane "Itu sangat intens!"

    hide diane with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ renpy.end_replay()
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        if player.location is L_diane_barn_interior:
            $ player.go_to(L_diane_barn)
        else:
            $ player.go_to(L_diane_garden)
    $ game.main()

label diane_cucumber_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        diane "Ya Tuhan!{p=1}{nw}"

    if animcounter == 0 and randomizer() < 25:
        diane "Ahh!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 75:
        diane "Ya!{p=1}{nw}"

    if animcounter == 1 and randomizer() > 75:
        diane "Mmm, itu saja {b}[firstname]{/b}!{p=1}{nw}"

        diane "Persetan aku dengan mentimun itu!{p=2}{nw}"

    if animcounter == 2 and randomizer() < 25:
        diane "Lebih dalam, {b}[firstname]{/b}!{p=1}{nw}"

    if animcounter == 2 and randomizer() < 25:
        diane "Dasar anak nakal!{p=1}{nw}"

        player_name "Heh.{p=1}{nw}"

    if animcounter == 3 and randomizer() > 75:
        diane "Ahhh!!{p=1}{nw}"

        diane "Saya hampir sampai...{p=2}{nw}"

    if animcounter == 3 and randomizer() > 75:
        diane "Lebih cepat!{p=1}{nw}"

        if M_diane.get("sex speed") > 0.21:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.1)
        diane "Ahh!!{p=1}{nw}"

    return

label diane_first_breastfeed:
    scene expression "backgrounds/location_diane_shed_hay_stack.jpg"
    show diane b_hay_feeding a_stroke f_explain
    with dissolve
    diane "Mmm, mulut hangat itu terasa nikmat setelah seharian memompa."

    show diane f_lip_bite
    pause
    show diane f_explain
    diane "Ahh, bagaimana rasanya hari ini kawan?"

    show diane f_smirk_down
    player_name "Mmhmm!"

    show diane f_laugh
    diane "Hehehe!"

    show diane f_smirk_down
    pause
    show diane f_explain
    diane "Kita seharusnya tidak melakukan ini tetapi untuk beberapa alasan..."

    diane "... Itu membuatku semakin ingin melakukannya!"

    show diane f_lip_bite
    pause
    show diane b_hay_feeding1 with dissolve
    diane "Ngghh!"

    show diane f_shamed_look
    diane "Baiklah, sebaiknya kita berhenti sebelum kamu meminumku sampai kering, kawan."

    show diane f_smirk_down
    player_name "Aduh."

    show diane f_explain
    diane "saya tahu..."

    show diane f_shamed_look
    diane "Kita akan melakukannya lagi lain kali, oke?"

    show playersex 1 at right
    if M_diane.outfit.get == "shirtless":
        show diane f_smirk_down b_hay_undress1
    else:
        show diane f_smirk_front b_hay_sit
    with dissolve
    player_name "Apakah tidak ada hal lain yang bisa kita lakukan?"

    if M_diane.outfit.get == "shirtless":
        show diane b_hay_dressed f_smirk_front with dissolve
    diane "Seperti apa?"

    player_name "Entahlah..."

    player_name "... Aku sangat terangsang!"

    diane @ f_laugh "Hehe, aku tahu tampan, aku juga..."

    pause
    diane "Baiklah, kenapa kamu tidak mengeluarkannya untukku?"

    diane "Biarkan saya melihatnya dengan baik."

    pause
    player_name "O-oke."

    show playersex 2 with dissolve
    show diane f_down_front
    pause
    show playersex 4 with dissolve
    pause 1
    show playersex 3 with dissolve
    pause
    show diane f_surprised_front
    diane "Hmm, baiklah tuan..."

    diane "Itu adalah sesuatu yang sangat istimewa!"

    player_name "Y-ya?"

    show diane f_smirk_front
    diane @ -m_talk "Mmmhmm."

    pause
    if M_diane.outfit.get == "shirtless":
        $ M_diane.outfit.is_naked = 1
        diane "Kurasa sekarang giliranku, ya?"

        show diane f_smirk_down b_hay_undress1 with dissolve
        pause
        show diane b_hay_undress2 with dissolve
        player_name "Wah!"

        show diane b_hay_naked f_laugh with dissolve
        diane "Hehehe, kamu suka?"

        show diane f_smirk_front
    player_name "Kamu cantik sekali, {b}Diane{/b}!"

    diane "Ah, aku tidak secantik itu..."

    player_name "Ya, benar!"

    diane "Ck, sungguh mempesona..."

    player_name "Jadi apa yang akan kita lakukan?"

    hide playersex
    show diane b_hay_rub f_lip_bite
    player_name "!!!" with hpunch
    player_name "Ya Tuhan!"

    pause
    pause
    if M_diane.outfit.get == "shirtless":
        player_name "Bisakah saya memasukkannya ke dalam, {b}Diane{/b}?"

        show playersex 3 at right
        show diane b_hay_naked f_shamed_front
        with dissolve
        diane "Tidak, tidak..."

        player_name "Kenapa?"

        diane "{b}[firstname]{/b}, Anda tahu alasannya..."

        diane "Kami tidak bisa..."

        player_name "{i}*Huh*{/i} Tapi aku sangat ingin melakukannya!"

        diane "Aku tahu, tampan..."

        pause
        show diane f_smirk_front
    else:
        show playersex 3 at right
        show diane b_hay_sit f_smirk_front
        with dissolve
    diane "Ayo duduk di sini."

    player_name "Hmm?"

    diane "Ayo."

    diane "Aku akan mengurus ini untukmu."

    player_name "O-oke..."

    hide diane
    hide playersex
    scene expression "backgrounds/location_barn_floor_boobjob.jpg"
    if M_diane.outfit.get == "shirtless":
        $ M_diane.outfit.is_naked = 1
    show diane_sex_boobjob 2
    show diane_sex_boobjob_look talk
    with dissolve
    diane "Anda menyukai payudara saya, bukan?"

    show diane_sex_boobjob_look
    player_name "Tentu saja!"

    show diane_sex_boobjob_look talk
    diane "Aku akan menunjukkanmu sesuatu yang istimewa..."

    show diane_sex_boobjob_look
    player_name "Apa yang kamu-"

    hide diane_sex_boobjob_look
    jump diane_boobjob_start

label diane_boobjob_start:
    $ animated = True
    $ anim_toggle = True
    $ M_diane.set('sex speed', .25)
    show expression AnimatedImage("diane_sex_boobjob", [1,2,3,2], M_diane) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
    player_name "Haah!" with hpunch
    diane "Anda suka itu?"

    player_name "Y-ya!!"

    label diane_boobjob_loop:
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        $ animcounter = 0
        while animcounter < 4:
            if anim_toggle:
                if not animated:
                    show expression AnimatedImage("diane_sex_boobjob", [1,2,3,2], M_diane) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
                    $ animated = True
                pause 5
                call expression game.dialog_select("diane_boobjob_hscene_dialog")
                pause 3
            else:

                $ pose_counter = 0
                $ pose_list = [1,2,3,2]
                $ poses_done = []
                while poses_done != pose_list:
                    show expression "diane_sex_boobjob {}".format(pose_list[pose_counter]) as diane_sex_boobjob at Position(xalign = 0.0, yoffset = 0)
                    pause
                    $ poses_done.append(pose_list[pose_counter])
                    $ pose_counter += 1
                call expression game.dialog_select("diane_boobjob_hscene_dialog")
            $ animcounter += 1
        call screen diane_boobjob_options

label diane_boobjob_hscene_dialog:
    $ renpy.dynamic(rng=randomizer())
    if animcounter == 0:
        if rng > 90:
            player_name "Ya Tuhan, ini terasa luar biasa!{p=2}{nw}"

            diane "Hehehe!{p=1}{nw}"

    elif animcounter == 1:
        if rng > 95:
            player_name "Di mana Anda belajar melakukan hal ini?{p=2}{nw}"

            diane "Hmm?{p=1}{nw}"

            diane "Oh, umm... Sebenarnya, {b}[deb_name]{/b} yang menunjukkan padaku cara melakukan ini...{p=2}{nw}"

            diane "Dulu ketika kita masih muda dan liar.{p=2}{nw}"

            player_name "Apa?!{p=1}{nw}"

            player_name "{b}[deb_name]{/b} mengajarimu ini?!{p=2}{nw}"

            diane "Hehe, apa?{p=1}{nw}"

            diane "Kamu tidak mengira {b}[deb_name]{/b} masih perawan, bukan?{p=2}{nw}"

            player_name "Ya, tidak.{p=1}{nw}"

            player_name "Saya hanya tidak...{p=1}{nw}"

            player_name "Ahh!!{p=1}{nw}"

        elif rng > 80:
            player_name "Mmm, panas sekali!{p=2}{nw}"

    elif animcounter == 2:
        if rng > 90:
            diane "Kamu sangat suka meniduri payudaraku, bukankah kamu tampan?{p=2}{nw}"

            player_name "Y-ya!{p=1}{nw}"

            diane "Hehe!{p=1}{nw}"

        elif rng > 80:
            diane "Kamu suka bagaimana payudaraku terasa melingkari penismu?{p=2}{nw}"

            player_name "Y-ya!{p=1}{nw}"

        elif rng > 70:
            diane "Aku suka merasakan penismu yang besar dan keras di sela-sela payudaraku...{p=2}{nw}"

            player_name "Saya juga!{p=1}{nw}"

    elif animcounter == 3:
        if rng > 90:
            player_name "Saya semakin dekat...{p=2}{nw}"

    return

label diane_boobjob_cum:
    player_name "Aku semakin dekat, {b}Diane{/b}!"

    diane "Tidak apa-apa, tampan."

    diane "Biarkan keluar."

    pause
    show diane_sex_boobjob cum
    show diane_sex_boobjob_cum
    player_name "HNNGGG!!!" with flash
    show diane_sex_boobjob 2
    show diane_sex_boobjob_look talk
    with dissolve
    diane "Anak baik!"

    show diane_sex_boobjob_look
    pause
    player_name "Haah... Haah..."

    pause
    show diane_sex_boobjob_look talk
    diane "Hehehe!"

    scene black with fade
    hide diane_sex_boobjob_look
    hide diane_sex_boobjob
    scene expression player.location.background_blur with None
    if M_diane.is_set("first boobjob"):
        $ M_diane.set("first boobjob", False)
        show player 261bf at left
        show diane b_naked f_down_front o_boob_cum
        with dissolve
        pause
        show player 14 with dissolve
        show diane f_smirk
        player_name "Itu luar biasa!"

        show player 13
        diane "Anda merasa lebih baik sekarang?"

        show player 17
        player_name "Tentu saja!"

        show player 13
        show diane a_touch_cum f_down_front with dissolve
        pause
        show diane a_lick_cum f_lick_finger with dissolve
        show player 11
        player_name "!!!"
        show diane f_smirk a_idle with dissolve
        show player 10
        player_name "Apakah kamu baru saja-"

        show player 5
        show diane f_laugh
        diane "Hehehe!"

        show diane f_smirk
        diane "Kamu sudah meminum susuku, wajar saja jika aku mencoba susumu."

        show player 14
        player_name "... Dengan baik?"

        show player 13
        diane "Itu tidak buruk."

        pause
        diane "Saya tidak berpikir kita akan mendapat pesanan untuk itu..."

        show diane f_cheese
        show player 17
        player_name "Haha!"

        show player 14
        player_name "Ya, mungkin tidak."

        show player 13
        show diane f_smirk
        diane "Baiklah, kita harus kembali bekerja."

        diane "... Dan aku perlu membersihkan diriku!"

        show player 14
        player_name "Ya, oke {b}Diane{/b}."

        player_name "Saya akan berada di taman jika Anda membutuhkan saya."

        show player 13
        diane "Terima kasih, {b}[firstname]{/b}."

        hide player with dissolve
        pause
        show diane a_touch_cum f_down_front with dissolve
        pause
        show diane a_lick_cum f_lick_finger with dissolve
        diane @ -m_talk "Hmm!"

        hide diane with dissolve
    else:
        if M_diane.outfit.get == "shirtless":
            $ M_diane.outfit.is_naked = 1
        show player 261bf at left
        show diane b_naked f_down_front o_boob_cum
        with dissolve
        pause
        show player 14
        show diane f_smirk
        player_name "Fiuh!"

        player_name "Terima kasih, {b}Diane{/b}."

        player_name "Saya sangat membutuhkan itu."

        show player 13
        diane "Dengan senang hati, kawan."

        diane "Sekarang kembali bekerja, ya?"

        show player 14
        player_name "Y-ya, oke."

        hide player with dissolve
        pause
        show diane a_touch_cum f_down_front with dissolve
        pause
        show diane a_lick_cum f_lick_finger with dissolve
        diane @ -m_talk "Hmm, enak!"

        show diane a_idle f_cheese with dissolve
        diane "hehe!"

        hide diane with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["04_unlocked"] = True
    $ renpy.end_replay()
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_map)
    else:
        if player.location is L_diane_barn_interior:
            $ player.go_to(L_diane_barn)
        else:
            $ player.go_to(L_diane_garden)
    $ game.main()

label diane_sex_breed_start:
    $ diane_sex_position = "back"
    $ anim_toggle = True
    $ animated = True
    $ M_diane.set('sex speed', 0.09)
    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
    if store._in_replay:
        with fade
    jump diane_sex_breed_loop

label diane_sex_breed_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_diane.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression AnimatedImage("diane_sex_front", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression AnimatedImage("diane_sex_back", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                    with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_sex_breed_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                if M_diane.get("change angle"):
                    scene expression "backgrounds/location_barn_sex_front_day.jpg"
                    show expression "diane_sex_front {}".format(pose_list[pose_counter]) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                else:
                    scene expression "backgrounds/location_barn_sex_back_day.jpg"
                    show expression "diane_sex_back {}".format(pose_list[pose_counter]) as diane_sex_breed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_sex_breed_hscene_dialog")
        $ animcounter += 1
    call screen diane_sex_breed_options

label diane_sex_breed_hscene_dialog:
    if animcounter == 0 and randomizer() < 25:
        if randomizer() > 50:
            diane "Oh ya!{p=1}{nw}"

            diane "Sangat dalam!{p=1}{nw}"

        else:
            if M_diane.pregnancy.number_of_babies>0:
                diane "Oh, aku sangat menginginkan bayi lagi, {b}[firstname]{/b}.{p=2}{nw}"

            else:
                diane "Oh, aku sangat menginginkan bayimu, {b}[firstname]{/b}.{p=2}{nw}"

            diane "Tolong masukkan ke dalam diriku!{p=2}{nw}"

    if animcounter == 0 and randomizer() > 90:
        diane "Ya, {b}[firstname]{/b}!{p=1}{nw}"

        diane "Persetan aku seperti binatang!{p=1}{nw}"

    if animcounter == 1 and randomizer() < 25:
        diane "Bantengku!{p=1}{nw}"

        diane "Banteng besarku yang kuat!{p=2}{nw}"

    if animcounter == 1 and randomizer() < 25:
        if randomizer() > 50:
            diane "Oh, enak sekali!{p=1}{nw}"

        else:
            diane "Kamu besar sekali, {b}[firstname]{/b}!{p=1}{nw}"

    if animcounter == 2 and randomizer() > 75:
        if randomizer() > 50:
            player_name "Fiuh, ini terasa luar biasa {b}Diane{/b}!{p=2}{nw}"

            diane "Mmmhmm!{p=1}{nw}"

        else:
            diane "Ya!{p=1}{nw}"

            diane "Ya Tuhan, ya!{p=1}{nw}"

    if animcounter == 3 and randomizer() > 90:
        player_name "Moo untukku.{p=1}{nw}"

        diane "Apa?{p=1}{nw}"

        pause 1
        player_name "Anda ingin ditiduri seperti binatang, bukan?{p=2}{nw}"

        diane "Ya Tuhan ya!{p=1}{nw}"

        player_name "Lalu moo untukku.{p=1}{nw}"

        pause 1
        diane "... Moo?{p=1}{nw}"

        player_name "Anda bisa melakukan lebih baik dari itu...{p=2}{nw}"

        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        diane "Moo!{p=1}{nw}"

        player_name "Lebih keras, {b}Diane{/b}!{p=1}{nw}"

        diane "Moo!!{p=1}{nw}"

        player_name "Lebih keras!{p=1}{nw}"

        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        diane "Aduh!{p=1}{nw}"

        player_name "Moo untukku!{p=1}{nw}"

        diane "MOO!!!{p=1}{nw}"

        pause 1
        diane "MOOOOOOO!!!{p=1}{nw}"

    if animcounter == 3 and randomizer() > 75:
        if randomizer() > 50:
            diane "Itu dia!{p=1}{nw}"

            diane "Persetan denganku, kawan!{p=1}{nw}"

        if M_diane.get("sex speed") > 0.031:
            $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
        if randomizer() > 50:
            diane "Ohh! Oooh!!{p=1}{nw}"

            pause 1
            diane "OOOOH, TUHAN!!!{p=1}{nw}"

        else:
            diane "Aaahhh!!!{p=1}{nw}"

    if animcounter == 4 and randomizer() < 25:
        if randomizer() < 50:
            diane "Enak sekali!{p=1}{nw}"

            pause 1
            diane "Oh, enak sekali!{p=1}{nw}"

        else:
            diane "Isi aku, kawan!{p=1}{nw}"

    if animcounter == 4 and randomizer() > 75:
        if randomizer() > 50:
            player_name "Wow, {b}Diane{/b}, kamu basah sekali!{p=1}{nw}"

            pause 1
            diane "Saya tahu!{p=1}{nw}"

            diane "Tubuhku menyukai penismu!{p=1}{nw}"

        else:
            diane "Lakukan, {b}[firstname]{/b}!{p=1}{nw}"

            diane "Kembangkan aku!{p=1}{nw}"

    return

label diane_sex_breed_cum_pre:
    player_name "{b}Diane{/b} Aku akan keluar!"

    diane "Ah, aku jugauuuu!!!"

    pause
    if randomizer() < 50:
        diane "Sperma di dalam diriku, {b}[firstname]{/b}!"

        if M_diane.pregnancy.number_of_babies>0:
            diane "Aku ingin bayi lagi di dalam diriku!"

        else:
            diane "Aku ingin bayimu ada di dalam diriku!"

    else:
        diane "Air mani di dalam diriku, {b}[firstname]{/b}!"

        diane "Saya ingin semuanya!"

    player_name "Ya Tuhan!"

    pause
    if store._in_replay is None:
        $ M_diane.trigger(T_diane_brought_outfit_package)
    call screen diane_cum_breed_options

label diane_sex_breed_cum_out:
    player_name "saya tidak..."

    $ M_diane.set('sex speed', 0.09)
    pause
    player_name "saya tidak bisa..."

    pause
    diane "AAAAHHHH!!!"

    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    show diane_sex_breed after
    show diane_sex_breed_mc cumshot 2
    player_name "HNNGGG!!!" with flash
    show diane_sex_breed_mc cumshot 1
    show diane_sex_flying_cum 1
    with dissolve
    pause 1
    show diane_sex_flying_cum 2
    with dissolve
    pause
    player_name "Haah... Haah..."

    diane "Apa-"

    pause

    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 368 at left
    show diane b_naked f_sad
    with fade
    if randomizer() < 50:
        diane "... Apa yang telah terjadi?"

        diane "{b}[firstname]{/b}, kamu seharusnya masuk ke dalam diriku..."

        show player 367
        player_name "Aku tahu."

        show player 368
        pause
        show player 367
        player_name "Aku tahu."

        player_name "Saya minta maaf."

        player_name "Saatnya tiba dan aku seperti..."

        show player 368
        pause
        show player 367
        player_name "... Fiuh, entahlah."

        player_name "Aku akan masuk ke dalam dirimu lain kali, oke?"

        show player 368
        pause
        if M_diane.pregnancy.number_of_babies>0:
            show diane f_shamed_smile
            diane "Baiklah..."

        else:
            diane "Anda harus ingat, ada alasan kami melakukan ini..."

            show diane f_shamed
            show player 367
            player_name "Aku tahu."

            show player 368
        show diane f_normal
        diane "Tapi itu sungguh luar biasa!"

    else:
        diane "Anda menarik diri!"

        show player 367
        player_name "Aku tahu."

        show player 368
        diane "Mengapa kamu-"

        diane "{b}[firstname]{/b}, aku tidak bisa hamil jika kamu cum di punggungku!"

        show player 367
        player_name "Saya minta maaf."

        player_name "Aku hanya tidak bisa kali ini."

        show player 368
        pause
        diane "Oh, tidak apa-apa."

        diane "Saya tidak marah."

        if M_diane.pregnancy.number_of_babies>0:
            show player 367
        else:
            diane "Anda hanya perlu mengingat mengapa kami melakukan ini."

            pause
            diane @ f_normal "Jangan salah paham, aku SANGAT suka menidurimu, {b}[firstname]{/b}..."

            diane "...Tetapi jika saya tidak hamil maka bisnis saya akan menderita."

            show player 367
            player_name "Aku tahu."

        player_name "Saya minta maaf."

        hide player
        show diane b_kiss_both_naked:
            xoffset -217
        with dissolve
        player_name "!!!"
        pause
        show player 366 at left
        show diane b_naked f_normal
        with dissolve
        diane "Jangan meminta maaf."

        show diane f_smirk
        if M_diane.pregnancy.number_of_babies>0:
            diane "Lain kali, masukkan bayi lagi ke dalam diriku!"

        else:
            diane "Lain kali saja, masukkan bayi ke dalam diriku!"

        diane "Oke?"

        show player 365
        player_name "Oke..."

        show player 366
        diane "Sekarang, mari kita mulai memerah susu."

        show player 365
        player_name "Ya, Bu."

        show player 366
        diane "Bersikaplah lembut saja, {b}[firstname]{/b}."

        hide player
        hide diane
        with dissolve
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["05_unlocked"] = True
    $ renpy.end_replay()
    jump milking_game_pre_after_sex

label diane_sex_breed_cum_in:
    player_name "Ooh!"

    pause
    player_name "Ini dia!"

    diane "Isi aku, {b}[firstname]{/b}!!"

    pause
    diane "AAAAHHHH!!!"

    scene expression "backgrounds/location_barn_sex_back_day.jpg"
    $ M_diane.set("sex speed",0.4)
    show diane_sex_breed creampie zorder 0
    show xray_diane_back zorder 1 at Position (align=(0,0))
    player_name "HNNGGG!!!" with flash
    hide xray_diane_back
    show diane_sex_breed creampie_pullout
    with dissolve
    diane "NGGHHH!!!"

    show diane_sex_breed insert_and_pullout
    show diane_sex_dick_cum 2 zorder 3
    with dissolve
    pause
    show diane_sex_breed after
    show diane_sex_cum zorder 1
    show diane_sex_breed_mc zorder 2
    show diane_sex_dick_cum 1
    with dissolve
    pause
    show diane_sex_breed after_spread
    show diane_sex_cum spread
    with dissolve
    player_name "Haah... Haah..."

    pause
    diane "Ya Tuhan!"

    pause
    diane "Begitu banyak..."

    pause
    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["06_unlocked"] = True
    $ renpy.end_replay()
    call call_pregnancy_minigame (return_label="diane_sex_breed_cum_in_after_minigame", machine=M_diane)

label diane_sex_breed_cum_in_after_minigame:
    if M_diane.is_state(S_diane_milk_production_increase):
        $ M_diane.trigger(T_diane_breeding)

    scene expression "backgrounds/location_barn_day_blur.jpg"
    show player 366 at left
    show diane b_naked f_smirk
    with fade
    if randomizer() < 50 or M_diane.is_set("breed first time"):
        diane "Itu sangat banyak, {b}[firstname]{/b}!"

        show player 365
        player_name "M-maaf."

        show player 366
        diane "Tidak, ini luar biasa!"

    else:
        diane "Mmm, aku suka muatanmu yang besar, {b}[firstname]{/b}."

        show player 365
        player_name "Y-ya?"

        show player 366
        show diane f_laugh
        diane "They feel so wonderful!"

    show diane f_smirk
    show player 365
    player_name "Hehe."

    show player 366
    pause
    show player 365
    if M_diane.pregnancy.number_of_babies>0:
        player_name "Do you think you're, you know... pregnant again?"

    else:
        player_name "Do you think you're, you know... pregnant?"

    show player 366
    show diane f_laugh
    diane "Haha, it's too early to know."

    show diane f_smirk
    diane "Saya harap begitu."

    pause
    show player 365
    player_name "You might have my baby inside you, right now!"

    show player 366
    diane "Hehe, I know!"

    diane "It's so exciting!"

    diane "Oh, stud... You were so good!"

    jump milking_game_pre_after_sex

label diane_debbie_sex_start:
    if store._in_replay:
        scene expression "backgrounds/location_home_debbiebed_sex.jpg"
        $ M_diane.set('sex speed', 0.09)
    $ anim_toggle = True
    if not M_diane.is_set("3way first time"):
        $ M_diane.set('sex speed', 0.09)
    if not animated:
        show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0)
        $ animated = True

label diane_debbie_sex_loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("diane_debbie_sex_bed", [1,2,3,4,5,6,7,8,9,10], M_diane) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0) with dissolve
                $ animated = True
            pause 5
            call expression game.dialog_select("diane_debbie_sex_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "diane_debbie_sex_bed {}".format(pose_list[pose_counter]) as diane_debbie_sex_bed at Position(xalign = 0.0, yoffset = 0)
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call expression game.dialog_select("diane_debbie_sex_hscene_dialog")
        $ animcounter += 1
    call screen diane_debbie_sex_options

label diane_debbie_sex_hscene_dialog:
    if not M_diane.get("change partner"):
        if animcounter == 0 and randomizer() < 25:
            diane "OH MY GOD!{p=1}{nw}"

            diane "Don't stop!!{p=1}{nw}"

        if animcounter == 1 and randomizer() < 25:
            diane "Aduh!{p=1}{nw}"

            diane "Ahhh!{p=1}{nw}"

        if animcounter == 2 and randomizer() < 10:
            debbie "Hehe, I love this view!{p=2}{nw}"

            diane "Sorry, if I leak on you...{p=2}{nw}"

            debbie "It's okay, I don't mind.{p=2}{nw}"

        elif randomizer() < 25:
            diane "Oh my god, it's so deep!{p=2}{nw}"

            debbie "My boy has the best cock, doesn't he?!{p=2}{nw}"

            diane "Yes!!{p=1}{nw}"

        if animcounter == 3 and randomizer() < 25:
            player_name "Saya semakin dekat!{p=1}{nw}"

            diane "Ahh, me too!{p=1}{nw}"

            debbie "That's okay sweetie, you go right ahead!{p=2}{nw}"

    else:
        if animcounter == 0 and randomizer() < 25:
            diane "Ayo, {b}[firstname]{/b}!{p=1}{nw}"

            diane "Fuck her harder!{p=1}{nw}"

            if M_diane.get("sex speed") > 0.31:
                $ M_diane.set("sex speed", M_diane.get("sex speed") - 0.03)
            debbie "Ya Tuhan!{p=1}{nw}"

        elif randomizer() < 50:
            debbie "AHHH!!{p=1}{nw}"

            diane "That's it, stud!{p=1}{nw}"

        if animcounter == 1 and randomizer() < 25:
            debbie "Ahh!{p=1}{nw}"

        if animcounter == 2 and randomizer() < 25:
            diane "How is it so easy for you?!{p=2}{nw}"

            debbie "Hmm?{p=1}{nw}"

            diane "You take that huge cock like it's nothing!{p=2}{nw}"

            debbie "Mmm, I dunno...{p=1}{nw}"

            debbie "... It just feels so wonderful!{p=1}{nw}"

        if animcounter == 3 and randomizer() < 25:
            player_name "Saya semakin dekat!{p=1}{nw}"

            debbie "Ahh, me too!{p=1}{nw}"

            diane "Go ahead, handsome.{p=1}{nw}"

            diane "Show {b}[deb_name]{/b} how much you love her.{p=2}{nw}"

    return

label diane_debbie_sex_cum:
    player_name "Ini dia!"

    pause
    if M_diane.get("cum inside"):
        show diane_debbie_sex_bed cumpie
        if not M_diane.get("change partner"):
            show xray_diane_debbie_sex at Position (align=(0,0))
        else:
            show xray_diane_debbie_sex at Position (xpos=190,ypos=420)
    else:
        show diane_debbie_sex_bed base
        show diane_debbie_sex_bed_cumshot_mc
    player_name "HNNGGG!!!" with flash
    if not M_diane.get("change partner"):
        diane "NGGHHH!!!"

    else:
        debbie "OHHH!!!"

    hide xray_diane_debbie_sex with dissolve
    pause
    player_name "Haah... Haah..."

    hide diane_debbie_sex_bed_cumshot_mc

    if not M_diane.get("change partner"):
        show diane_debbie_sex_bed diane_after_talk
        with dissolve
        diane "Oh, wah..."

        if M_diane.get("cum inside"):
            diane "He came so much in me."

            show diane_debbie_sex_bed debbie_after_talk
            debbie "Hehe, that's my boy!"

            show diane_debbie_sex_bed diane_after_talk
            diane "MM."

        else:
            show diane_debbie_sex_bed debbie_after_talk
            debbie "There's so much!"

            show diane_debbie_sex_bed diane_after_talk
            diane "Sheesh, I'm covered!"

            diane "Haha!"

    else:
        show diane_debbie_sex_bed debbie_after_talk
        with dissolve
        debbie "Ya ampun..."

        if M_diane.get("cum inside"):
            debbie "I feel so full."

            show diane_debbie_sex_bed diane_after_talk
            diane "Hehe, that's my big sexy stud!"

            show diane_debbie_sex_bed debbie_after_talk
            debbie "MM."

        else:
            show diane_debbie_sex_bed diane_after_talk
            diane "There's so much!"

            show diane_debbie_sex_bed debbie_after_talk
            debbie "hehe!"

            debbie "Oh, I love feeling it on me!"


    if M_diane.is_set("3way first time"):
        show diane_debbie_sex_bed diane_after_talk
        diane "I'm so glad this happened!"

        show diane_debbie_sex_bed debbie_after_talk
        debbie "It was wonderful, wasn't it?"

        player_name "It was so awesome!"

        show diane_debbie_sex_bed diane_after_talk
        diane "Hehehe!"

        show diane_debbie_sex_bed debbie_after_talk
        debbie "Hehehe!"

        player_name "Can we do this again?!"

        show diane_debbie_sex_bed diane_after_talk
        diane "I'm down!"

        show diane_debbie_sex_bed debbie_after_talk
        debbie "Of course, we can do it whenever you want, {b}[firstname]{/b}."

        pause
        show diane_debbie_sex_bed debbie_after_talk
        debbie "Right now, I just want you to come and lay with us."

        show diane_debbie_sex_bed debbie_lounge_after_talk with dissolve
        debbie "I'm worn out!"

        show diane_debbie_sex_bed diane_lounge_after_talk
        diane "Hah, yeah... Me too!"

        show diane_debbie_sex_bed player_lounge_after_talk
        player_name "hehe."

        show diane_debbie_sex_bed debbie_lounge_after_talk
        debbie "C'mere sweetie!"

        debbie "Lie here between us."

        show diane_debbie_sex_bed player_lounge_after_talk
        player_name "O-oke."

    else:

        show diane_debbie_sex_bed diane_after_talk
        diane "Fiuh."

        diane "I'm so exhausted now..."

        show diane_debbie_sex_bed debbie_after_talk
        debbie "Ugh, me too."

        debbie "There's two of us, and we still can't keep up with him!"

        show diane_debbie_sex_bed diane_after_talk
        diane "Haha!"

        player_name "Apa pun."

        show diane_debbie_sex_bed player_lounge_after_talk with dissolve
        player_name "I'm tired too!"

        show diane_debbie_sex_bed debbie_lounge_after_talk
        debbie "Tidak apa-apa, sayang."

        debbie "You just lay here and rest."

        show diane_debbie_sex_bed diane_lounge_after_talk
        diane "Aww, I love you guys!"

        show diane_debbie_sex_bed debbie_lounge_after_talk
        debbie "Hehe, we love you too."


    scene black with fade
    hide diane_debbie_sex_bed

    $ persistent.cookie_jar["Diane"]["unlocked"] = True
    $ persistent.cookie_jar["Diane"]["gallery"]["07_unlocked"] = True
    $ renpy.end_replay()
    $ M_diane.trigger(T_diane_debbie_3way)
    if M_diane.get("cum inside") and not M_diane.get("change partner"):
        call call_pregnancy_minigame ("diane_debbie_sleeping", M_diane)
    jump diane_debbie_sleeping

label diane_debbie_sleeping:
    call expression game.dialog_select("diane_debbie_sleeping_pre")
    call sleep_lock_check
    if M_player.is_set("just wokeup"):
        $ renpy.call(game.dialog_select("player_just_wokeup"), woke_with = M_diane)
    $ game.main()

label diane_debbie_sleeping_pre:
    scene location_home_debbiebedroom_night_sleep_trio with fade
    call popup ('sleep')
    return

label diane_debbie_sleepover_wakeup_first:
    scene expression "backgrounds/location_home_debbiebedroom_day_blur.jpg" with fade
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 5 with dissolve
    player_name "Hmm?"

    show player 10
    player_name "Where'd everybody go?"

    show player 9 at Position (xoffset=40) with dissolve
    pause
    show player 17 with dissolve
    player_name "{i}*Sniff*{/i} Something smells great!"

    show player 14
    player_name "{b}[deb_name]{/b} must be cooking {b}in the kitchen{/b}."

    player_name "I should {b}go check it out{/b}."

    hide player with dissolve
    return

label diane_debbie_sleepover_wakeup_repeat:
    scene expression "backgrounds/location_home_debbiebedroom_day_blur.jpg" with fade
    show player 7 with dissolve
    pause
    show player 8 with dissolve
    pause
    show player 14 with dissolve
    player_name "Looks like {b}Diane{/b} and {b}[deb_name]{/b} are already up."

    hide player with dissolve
    return

label diane_debbie_pre_sex_loop:
    if not animated:
        show diane_debbie_sex_bed prev_insert
    if not M_diane.get("change partner"):
        if randomizer() > 50:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "I think it's time that {b}Diane{/b} had a turn."

            if animated:
                show diane_debbie_sex_bed debbie_talk
            debbie "If that's what you want, sweetie."

            debbie "Teruskan."

            if animated:
                show diane_debbie_sex_bed diane_talk
            diane "Mmhmm, bring that big dick over here."

            show diane_debbie_sex_bed insert with dissolve
            debbie "hehe!"

            diane "C'mon stud, show me what you got!"

            show diane_debbie_sex_bed 7
            diane "!!!" with hpunch
        else:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "{b}Diane{/b}, you're up next!"

            if animated:
                show diane_debbie_sex_bed diane_talk
            diane "Mmm, lucky me!"

            show diane_debbie_sex_bed insert with dissolve
            diane "C'mon stud, show me what you got!"

            show diane_debbie_sex_bed 7
            diane "!!!" with hpunch
    else:
        if randomizer() > 50:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "Ready, {b}[deb_name]{/b}?"

            if animated:
                show diane_debbie_sex_bed debbie_talk
            debbie "Hmm!"

            show diane_debbie_sex_bed insert with dissolve
            debbie "That's it sweetie!"

            debbie "Let me show a thing or two, {b}[firstname]{/b}!"

            player_name "Eh ya!"

            show diane_debbie_sex_bed 7
            diane "Oh!" with hpunch
        else:
            if animated:
                show diane_debbie_sex_bed player_talk
            player_name "It's {b}[deb_name]{/b}'s turn!"

            if animated:
                show diane_debbie_sex_bed diane_talk
            diane "Ahh, good idea..."

            diane "I need a break!"

            if animated:
                show diane_debbie_sex_bed debbie_talk
            debbie "hehe!"

            show diane_debbie_sex_bed insert with dissolve
            player_name "Here it comes, {b}[deb_name]{/b}."

            debbie "I'm ready!"

            show diane_debbie_sex_bed 7
            debbie "Oh! That's it sweetie!" with hpunch
    $ animated = False
    jump diane_debbie_sex_loop


label diane_cookiejar:
    return


label diane_cookiejar.paizuri:
    $ M_diane.reset()
    $ M_diane.outfit.outfits = {}
    $ player.location = L_diane_shed
    $ game.timer._tod = 2

    scene location_diane_shed_hay_stack

    menu:
        "Overalls":
            $ M_diane.outfit.set_default_outfit_schedule('shirtless')
        "pakaian sapi":

            $ M_diane.outfit.set_default_outfit_schedule('cow')
        "Telanjang":

            $ M_diane.outfit.is_naked = True

    jump dianes_dialogue_breastfeed


label diane_cookiejar.cucumber:
    $ M_diane.reset()
    $ M_diane.set('first boobjob', False)
    $ player.location = L_diane_barn_interior

    scene location_barn_hay_stack

    menu:
        "pakaian sapi":
            $ M_diane.outfit.set_default_outfit_schedule('cow')
        "Telanjang":

            $ M_diane.outfit.is_naked = True

    jump dianes_dialogue_breastfeed


label diane_cookiejar.breed:
    $ M_diane.reset()

    scene location_barn_hay_stack

    menu:
        "pakaian sapi":
            $ M_diane.outfit.set_default_outfit_schedule('cow')
        "Telanjang":

            $ M_diane.outfit.is_naked = True

    scene location_barn_sex_back_day
    jump diane_sex_breed_start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
