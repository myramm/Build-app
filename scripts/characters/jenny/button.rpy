label jenny_button_dialogue:
    if player.location == L_home_diningroom:
        $ M_jenny.set('sit', 1)
    else:
        $ M_jenny.set('sit', 0)
    scene expression player.location.background_closeup

    if M_jenny.pregnancy.character_bedridden:
        call jenny_hospital_bed_dialogue
        $ game.main()

    if M_jenny.preg_afterglow:
        call jenny_button_afterglow
        $ game.main()

    if M_eve.is_state(S_eve_party_speak_to_jenny) and L_tattooparlor_roof.is_here(M_jenny):
        call expression game.dialog_select("button_jenny_eve_party_speak_to_jenny")
        $ M_eve.trigger(T_eve_party_spoke_to_jenny)
        $ game.main()
    elif player.location == L_tattooparlor_roof:
        $ game.main()
    elif M_jenny.is_state(S_jenny_talked_to_cedric) and game.timer.is_day():
        call expression game.dialog_select("jenny_button_talked_to_cedric")
        $ M_jenny.trigger(T_jenny_cedric_didnt_call)
        $ game.timer.tick()
        $ game.main()
    elif M_jenny.is_state(S_jenny_go_to_her_room) and L_home_sisbedroom.is_here(M_jenny):
        if M_jenny.get("dominance") > 0:
            call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant")
            if player.has_money(200):
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_has_money")
                $ player.spend_money(200)
                $ game.timer.tick()
                $ M_jenny.trigger(T_jenny_pay_for_favors)
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_dominant_no_money")
        else:
            call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive")
            if player.has_money(200):
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_has_money")
                $ player.spend_money(200)
                $ game.timer.tick()
                $ M_jenny.trigger(T_jenny_pay_for_favors)
            else:
                call expression game.dialog_select("jenny_bedroom_jenny_go_to_her_room_submissive_no_money")
        $ game.main()
    elif M_jenny.is_state(S_jenny_have_breakfast_2) and L_home_diningroom.is_here(M_jenny):
        call expression game.dialog_select("dining_room_jenny_have_breakfast_2")
        menu:
            "Kamu seksi. {color=7ff7}[[Submissive]{/color}":
                call expression game.dialog_select("dining_room_jenny_have_breakfast_2_youre_hot")
                $ M_jenny.decrement("dominance")
            "Tidak.{color=f77b}[[Dominant]{/color}":
                call expression game.dialog_select("dining_room_jenny_have_breakfast_2_no")
                $ M_jenny.increment("dominance")
        $ M_jenny.trigger(T_jenny_had_breakfast_2)
        $ game.main()
    elif M_jenny.is_state(S_jenny_get_a_mask, S_jenny_buy_mask) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_get_mask")
        $ game.main()
    elif M_jenny.is_state(S_jenny_bought_mask) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_bought_mask")
        $ M_jenny.trigger(T_jenny_delivered_mask)
        $ game.main()
    elif M_jenny.is_state(S_jenny_start_camshow_handjob) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("button_jenny_start_camshow_handjob")
    elif M_jenny.is_state(S_jenny_pool_talk) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("button_jenny_pool_talk")
        $ M_jenny.trigger(T_jenny_stalked)
        $ player.go_to(L_home)
        $ game.main()
    elif M_jenny.is_state(S_jenny_ask_movie_date) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_ask_movie_date")
        $ M_jenny.trigger(T_jenny_movie_date)
        $ game.main()
    elif M_jenny.is_state(S_jenny_movie_date) and L_home_sisbedroom.is_here(M_jenny):
        call expression game.dialog_select("jenny_button_movie_date")
        $ game.main()
    elif M_jenny.pregnancy.stage >= 1:
        if M_jenny.pregnancy.stage <= 1:
            call expression game.dialog_select("jenny_button_pregnancy_stage_1")
            jump jenny_pregnancy_menu
        elif M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_button_pregnancy_stage_2")
            jump jenny_pregnancy_menu
        elif M_jenny.pregnancy.stage in (3, 4):
            call expression game.dialog_select("jenny_button_pregnancy_stage_3")
            jump jenny_pregnancy_menu
        else:
            call expression game.dialog_select("jenny_button_pregnancy_holding_baby")
            jump jenny_pregnancy_baby_menu
    else:
        if L_home_diningroom.is_here(M_jenny):
            if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                call expression game.dialog_select("jenny_button_intro_diningroom_j8")
                $ game.main()
            elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_intro_diningroom_j16")
            elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                call expression game.dialog_select("jenny_button_intro_diningroom_j20")
            else:
                call expression game.dialog_select("jenny_button_intro_diningroom_j21")
        elif L_home_backyard.is_here(M_jenny):
            if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                call expression game.dialog_select("jenny_button_intro_backyard_j8")
                $ game.main()
            elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_intro_backyard_j16")
            elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                call expression game.dialog_select("jenny_button_intro_backyard_j20")
            else:
                call expression game.dialog_select("jenny_button_intro_backyard_j21")
        elif L_home_sisbedroom.is_here(M_jenny):
            if game.timer.is_afternoon():
                if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j8")
                    $ player.go_to(L_home_hallway)
                    $ game.main()
                elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j16")
                elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                    call expression game.dialog_select("jenny_button_intro_bedroom_j20")
                else:
                    call expression game.dialog_select("jenny_button_intro_bedroom_j21")
            elif game.timer.is_evening():
                if M_jenny.between_states(S_jenny_start, S_jenny_caught_snooping):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j8")
                    $ player.go_to(L_home_hallway)
                    $ game.main()
                elif M_jenny.between_states(S_jenny_caught_snooping, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j16")
                elif M_jenny.between_states(S_jenny_caught_talking_to_camslut, S_jenny_end):
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j20")
                else:
                    call expression game.dialog_select("jenny_button_intro_bedroom_evening_j21")
    menu sis_bedroom_menu:
        "Aku punya sesuatu untukmu." if player.has_item('picture2') and L_home_sisbedroom.is_here(M_jenny):
            show jenny b_dressed
            call jenny_button_old_photo
            $ player.remove_item('picture2')
            $ M_jenny.set('photo_reaction', game.timer._game_day * 4 + game.timer._tod)

        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Membayar." if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Jangan membayar.":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")

        "Aku punya kejutan untukmu!" if M_jenny.is_state(S_jenny_diary_clue) and player.has_item("\w+_necklace", regex=True) and game.timer.is_tick(1, 2):
            call expression game.dialog_select("button_jenny_have_a_surprise_necklace")
            menu:
                "Ya.":
                    call expression game.dialog_select("button_jenny_have_a_surprise_yes")
                "Tidak, aku ingin yang asli!":
                    call expression game.dialog_select("button_jenny_have_a_surprise_no")
            $ M_jenny.trigger(T_jenny_give_necklace)
            jump sis_bedroom_menu

        "Buatlah kesepakatan." if M_jenny.finished_state(S_jenny_go_to_her_room):
            if L_home_diningroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny):
                call expression game.dialog_select("jenny_dialogue_make_a_deal_breakfast")
            else:
                call expression game.dialog_select("jenny_dialogue_make_a_deal")
            $ game.main()

        "Mainan." if M_jenny.is_state(S_jenny_get_a_toy, S_jenny_go_to_pink, S_jenny_bring_toy_back) and L_home_sisbedroom.is_here(M_jenny):
            if M_jenny.is_state(S_jenny_bring_toy_back):
                call expression game.dialog_select("button_jenny_has_toy_electroclit")
                if M_jenny.get("dominance") <= 0:
                    call expression game.dialog_select("button_jenny_has_toy_electroclit_submissive")
                else:
                    call expression game.dialog_select("button_jenny_has_toy_electroclit_dominant")
                $ M_jenny.trigger(T_jenny_brought_back_toy)
                $ game.timer.tick()
                $ game.main()
            else:
                call expression game.dialog_select("button_jenny_get_toy_electroclit")
                jump sis_bedroom_menu

        "{b}Cedric{/b}." if M_jenny.is_state(S_jenny_talk_to_cedric) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("button_jenny_talk_to_cedric")

        "Pertunjukan kamera." if M_jenny.is_state(S_jenny_come_back_camshow) and not M_jenny.pregnancy and game.timer.is_day():
            call expression game.dialog_select("button_jenny_come_back_camshow")

        "Pertunjukan kamera." if M_jenny.finished_state(S_jenny_start_camshow_handjob) and L_home_sisbedroom.is_here(M_jenny) and not M_jenny.pregnancy and game.timer.is_day():
            $ M_jenny.set('teasin_before_sex', False)
            call expression game.dialog_select("button_jenny_camshow")
            menu jenny_camshow_options:
                "pekerjaan tangan.":
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_hj")
                    else:
                        call expression game.dialog_select("jenny_hj_intro_repeat")

                "Lisan." if M_jenny.finished_state(S_jenny_start_camshow_blowjob):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_bj")
                    else:
                        call expression game.dialog_select("jenny_bj_intro_repeat")

                "cunnilingus." if M_jenny.finished_state(S_jenny_give_cunni):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_cunni")
                    else:
                        call expression game.dialog_select("jenny_cunni_intro_repeat")

                "Seks." if M_jenny.finished_state(S_jenny_cheerleader_sex):
                    if M_jenny.get('teasin_before_sex'):
                        call expression game.dialog_select("finger_blasting_sex")
                    else:
                        call expression game.dialog_select("jenny_sex_intro_repeat")

        "Hanya ingin tahu." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_just_curious")
            jump sis_bedroom_menu

        "Kamu dan telepon itu." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_you_and_phone")
            jump sis_bedroom_menu

        "Hanya menyapa." if L_home_sisbedroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_just_saying_hi")
            jump sis_bedroom_menu

        "Tidak berenang?" if L_home_backyard.is_here(M_jenny) and M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("button_jenny_not_swimming")
            jump sis_bedroom_menu

        "Akhirnya bersikap hangat padaku?" if game.timer.is_morning() and M_jenny.finished_state(S_jenny_catch_her_jilling):
            call expression game.dialog_select("jenny_button_warming_up")
            jump sis_bedroom_menu

        "Apa yang kamu tulis?" if game.timer.is_evening() and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_what_are_you_writing")
            elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_what_are_you_writing_2")
                jump sis_bedroom_menu

        "Apakah kamu benar-benar tinggal?" if M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy.had_baby:
            call expression game.dialog_select("jenny_button_really_staying")
            jump sis_bedroom_menu

        "Anda ingin menonton film porno bersama?" if M_jenny.finished_state(S_jenny_catch_her_jilling) and game.timer.is_afternoon():
            call expression game.dialog_select("button_jenny_wanna_watch_porn")
            $ M_jenny.set("force_couch_sex", True)

        "Ingin bermain-main?" if game.timer.is_day() and L_home_diningroom.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy:
            $ player.go_to(L_home_diningroom)
            if M_jenny.get("first_sex_dining"):
                call expression game.dialog_select("button_jenny_fool_around_diningroom_first")
            else:
                call expression game.dialog_select("button_jenny_fool_around_diningroom_repeat")
            jump jenny_dining_room_sex_intro

        "Ingin bermain-main?" if game.timer.is_day() and L_home_backyard.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy:
            if M_jenny.get("first_sex_pool"):
                $ M_jenny.set("first_sex_pool", False)
                call expression game.dialog_select("button_jenny_fool_around_pool_first")
            else:
                call expression game.dialog_select("button_jenny_fool_around_pool_repeat")

        "Ingin bermain-main?" if L_home_sisbedroom.is_here(M_jenny) and M_jenny.finished_inclusive(S_jenny_end) and not M_jenny.pregnancy and game.timer.is_afternoon():
            call expression game.dialog_select("jenny_button_fool_around")
            menu:
                "Oke.":
                    $ M_jenny.set('teasin_before_sex', True)
                    jump jenny_camshow_options
                "Tidak hari ini.":
                    call expression game.dialog_select("jenny_button_fool_around_not_today")
                    $ player.go_to(L_home_hallway)
                    $ game.main()

        "Ingin bermain-main?" if game.timer.is_evening() and M_jenny.finished_inclusive(S_jenny_end):
            call expression game.dialog_select("jenny_button_fool_around_evening")
            jump sis_bedroom_menu

        "Datanglah ke kamarku malam ini." if M_jenny.finished_state(S_jenny_night_time_sex) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_button_come_to_my_room")
            $ M_jenny.set("forced_sneak_in_chance", 60)
            jump sis_bedroom_menu

        "Pengalaman pacar." if M_jenny.finished_inclusive(S_jenny_necklace_rebutal):
            if game.timer.is_day():
                call expression game.dialog_select("jenny_button_gf_experience_day")
                jump sis_bedroom_menu
            elif game.timer.is_evening():
                call expression game.dialog_select("jenny_button_gf_experience_evening")
                menu:
                    "Ya.":
                        jump expression game.dialog_select("jenny_button_gf_experience_yes")
                    "Sudahlah.":
                        call expression game.dialog_select("jenny_button_gf_experience_nevermind")
                        jump sis_bedroom_menu

        "Tidak ada apa-apa." if L_home_diningroom.is_here(M_jenny) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_nothing")
            elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                call expression game.dialog_select("jenny_button_nothing_2")

        "Sudahlah." if (L_home_sisbedroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny)) and not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            if game.timer.is_day():
                if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nevermind")
                elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nervermind_2")
            else:
                if not M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nevermind_evening_2")
                elif M_jenny.between_states(S_jenny_start, S_jenny_caught_talking_to_camslut):
                    call expression game.dialog_select("jenny_button_nervermind_evening")

        "Saya harus pergi." if (L_home_diningroom.is_here(M_jenny) or L_home_backyard.is_here(M_jenny)) and M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_leave_final_morning")

        "Tidak, aku sedang sibuk." if L_home_sisbedroom.is_here(M_jenny) and M_jenny.finished_state(S_jenny_caught_talking_to_camslut):
            call expression game.dialog_select("jenny_button_leave_final_bedroom")

    hide anon
    hide jenny
    $ game.main()

label jenny_hospital_bed_dialogue:
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    scene expression game.timer.image("location_hospital_baby_bed{}")
    show jenny a_baby b_gown_bed f_happy_down
    show anon with dissolve
    anon "Hei, bagaimana perasaanmu?"

    jenny "Aduh, {b}[firstname]{/b}..."

    if M_jenny.pregnancy.baby_gender == "twins":
        jenny "Bukankah mereka cantik?"

        jenny "Aku tidak bisa berhenti menatap mereka..."

    elif M_jenny.pregnancy.baby_gender == "boy":
        jenny "Bukankah dia cantik?"

        jenny "Aku tidak bisa berhenti menatapnya..."

    else:
        jenny "Bukankah dia cantik?"

        jenny "Aku tidak bisa berhenti menatapnya..."

    anon "Hehe, aneh sekali mendengarmu berbicara seperti ini..."

    jenny f_upset "Oh, diamlah!"

    anon @ f_laugh "Itulah {b}[jen_name]{/b} yang saya kenal dan sukai."

    jenny f_happy_down @ f_eyeroll "... Kontol."

    menu:
        "Aku hanya ingin memeriksamu.":
            anon "Aku hanya ingin memeriksamu."

            jenny "Ya, kami baik-baik saja."

            jenny @ f_eyeroll "Maksudku, aku kelelahan dan makanan di sini jelek tapi..."

            jenny "... Kalau tidak, kami baik-baik saja."

            anon "Heh, kamu akan segera pulang."

            if M_jenny.pregnancy.baby_gender == "twins":
                anon "Anda ingin saya meminumnya sebentar agar Anda bisa tidur?"

            elif M_jenny.pregnancy.baby_gender == "boy":
                anon "Kamu ingin aku membawanya sebentar agar kamu bisa tidur?"

            else:
                anon "Kamu ingin aku membawanya sebentar agar kamu bisa tidur?"

            jenny @ f_happy -m_talk "Hmm?"

            if M_jenny.pregnancy.baby_gender == "twins":
                jenny "Tidak, aku mendapatkannya!"

            elif M_jenny.pregnancy.baby_gender == "boy":
                jenny "Tidak, aku menangkapnya!"

            else:
                jenny "Tidak, aku mendapatkannya!"

            anon "Anda yakin?"

            show jenny f_upset
            if M_jenny.pregnancy.baby_gender == "twins":
                jenny "Saya bilang, saya punya, {b}[firstname]{/b}!"

            elif M_jenny.pregnancy.baby_gender == "boy":
                jenny "Aku bilang, aku punya dia, {b}[firstname]{/b}!"

            else:
                jenny "Aku berkata, aku mendapatkannya, {b}[firstname]{/b}!"

            show jenny f_happy_down
            anon f_worried "O-oke."

            hide anon with dissolve
    $ game.main()

label jenny_pregnancy_menu:
    menu:
        "{b}Roxxy{/b}." if M_bissette.is_state(S_bissette_jenny_mentoring_payment) and L_home_sisbedroom.is_here(M_jenny):
            call expression game.dialog_select("jenny_dialogue_roxxy_pre")
            menu:
                "Membayar." if player.has_money(500):
                    $ player.spend_money(500)
                    call expression game.dialog_select("jenny_dialogue_roxxy_pay")
                    $ M_bissette.trigger(T_bissette_jenny_paid)
                "Jangan membayar.":

                    call expression game.dialog_select("jenny_dialogue_roxxy_do_not_pay")
        "Kamu baik-baik saja?" if game.timer.is_morning() and M_jenny.pregnancy.stage == 1:
            call expression game.dialog_select("jenny_pregnancy_you_doing_ok_1")
            jump jenny_pregnancy_menu
        "Apakah kamu masih marah?" if M_jenny.pregnancy.stage == 1:
            call expression game.dialog_select("jenny_pregnancy_are_you_still_mad")
            jump jenny_pregnancy_menu
        "Kamu baik-baik saja?" if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_you_doing_ok_2")
            jump jenny_pregnancy_menu
        "Bolehkah aku memberimu sesuatu?" if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_can_i_get_you_something")
            jump jenny_pregnancy_menu
        "Tentang {b}[deb_name]{/b}..." if M_jenny.pregnancy.stage == 2:
            call expression game.dialog_select("jenny_pregnancy_about_debbie")
            jump jenny_pregnancy_menu
        "Bolehkah aku memberimu sesuatu?" if game.timer.is_afternoon() and M_jenny.pregnancy.stage == 4:
            call expression game.dialog_select("jenny_pregnancy_can_i_get_you_something_3")
            jump jenny_pregnancy_menu
        "{b}[deb_name]{/b} membuat Anda gila?" if M_jenny.pregnancy.stage in (3,4):
            call expression game.dialog_select("jenny_pregnancy_debbie_driving_crazy")
            jump jenny_pregnancy_menu
        "Pertunjukan kamera?" if M_jenny.pregnancy.stage in (3,4) and game.timer.is_afternoon() and M_jenny.finished_state(S_jen0m_food):
            call jenny_button_pregnant.sex
            $ M_jenny.set('preg_afterglow', True)
            $ player.go_to(L_home_hallway)
            $ game.timer.tick()
            $ game.main()
        "Aku akan meninggalkanmu.":

            call expression game.dialog_select("jenny_pregnancy_leave")
            $ game.main()

label jenny_pregnancy_baby_menu:
    menu:
        "Kalian butuh sesuatu?":
            call expression game.dialog_select("jenny_pregnancy_baby_need_anything")
            jump jenny_pregnancy_baby_menu
        "Menantikan Tempat Penitipan Anak.":
            call expression game.dialog_select("jenny_pregnancy_baby_looking_forward_daycare")
            jump jenny_pregnancy_baby_menu
        "Aku akan meninggalkanmu.":
            call expression game.dialog_select("jenny_pregnancy_baby_leave")
            $ game.main()

label jenny_button_gf_experience_yes:
    if not player.has_money(500) and M_jenny.get("jenny_girlfriend_first_time"):
        call expression game.dialog_select("jenny_button_gf_experience_no_money_first")
        jump sis_bedroom_menu
    elif not player.has_money(200) and not M_jenny.get("jenny_girlfriend_first_time"):
        call expression game.dialog_select("jenny_button_gf_experience_no_money_repeat")
        jump sis_bedroom_menu
    else:
        if M_jenny.get("jenny_girlfriend_first_time"):
            $ player.spend_money(500)
        else:
            $ player.spend_money(200)
        $ M_jenny.set("girlfriend_in_progress", True)
        call expression game.dialog_select("jenny_button_gf_experience_start")
        menu:
            "Tetap di dalam.":
                call expression game.dialog_select("jenny_button_gf_experience_stay_in")
                $ game.timer.tick()
                $ player.go_to(L_home_livingroom)
                $ game.main()

label jenny_button_girlfriend_experience_bedroom:
    scene expression "backgrounds/location_home_bedroom_sex01d.jpg"
    show anon b_sit f_flirt o_sit_boner
    show jenny b_visit_sit_naked a_down f_visit_sexy_up
    with fade
    if M_jenny.get("jenny_girlfriend_first_time"):
        anon "A-wah."

        jenny "Butuh waktu cukup lama..."

        anon @ -m_talk "..."
        jenny "kamu suka?"

        anon "saya suka!"

        jenny "Hehe, bagus!"

        show jenny a_push
        show anon b_sit_falling f_empty
        with dissolve
        pause
        show jenny f_visit_sexy a_down
        show anon b_sit_laying o_visit_laying_boner
        with dissolve
        jenny "Sekarang berbaringlah dan biarkan aku menjagamu."


        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        jenny "Mmm, aku sangat senang pacar baruku punya penis yang bagus!"

        anon "Anda menyukainya?"

        show jenny_mc_room_sex 1 with dissolve
        jenny "Sial!"

        pause
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .12)
        show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
        jenny "Heh, aku tidak akan berkencan denganmu jika aku tidak..."

        anon "Wow, kamu benar-benar basah malam ini!"

        jenny "saya tahu..."

        pause
        jenny "Mmm, aku sudah memikirkan ayammu sepanjang malam!"

        anon "Bahkan saat kami sedang menonton acaramu?"

        jenny "Ya, aku pernah melihat semuanya sebelumnya..."

        anon "Oh benar."

        pause
        jenny "Aku akan tidur nyenyak setelah ini!"

        anon "Ya, aku juga!"

    else:
        anon "Kau tahu, aku sudah terbiasa melihatmu telanjang di tempat tidurku di malam hari..."

        jenny "Ya, saya yakin Anda bisa."

        show jenny a_push
        show anon b_sit_falling f_empty
        with dissolve
        pause
        show jenny f_visit_sexy a_down
        show anon b_sit_laying o_visit_laying_boner
        with dissolve
        jenny "Sekarang berbaringlah dan biarkan aku menjagamu."

        scene expression "backgrounds/location_home_bedroom_sex05.jpg"
        show jenny_mc_room_sex insert
        with fade
        jenny "Mmm, aku suka ayam ini!"

        anon "Menurutku dia juga mencintaimu."

        jenny "Hah!"

        show jenny_mc_room_sex 1 with dissolve
        jenny "Sial!"

        pause
        $ animated = True
        $ anim_toggle = True
        $ M_jenny.set('sex speed', .12)
        show expression AnimatedImage("jenny_mc_room_sex", [1,2,3,4,5,6,7,8,9], M_jenny) as jenny_mc_room_sex at Position(xalign = 0.0, yoffset = 0)
        jenny "Sangat dalam, {b}[firstname]{/b}!"

        anon "Ya..."

        pause
        anon "Saya suka melihat payudara Anda memantul dari posisi ini!"

        jenny "Ahhh!"

    jump jenny_mc_room_sex_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
