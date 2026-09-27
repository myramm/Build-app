label consuela_button_beachhouse:
    show anon with dissolve
    if game.timer.is_morning():
        if M_consuela.finished_state(S_con03_done):
            consuela "Buenos dias, ayah."

        else:
            consuela "Buenos días, {b}Tuan [firstname]{/b}."

        anon "Selamat pagi, {b}Consuela{/b}."

    else:
        if M_consuela.finished_state(S_con03_done):
            consuela "Buenas tardes, ayah."

        else:
            consuela "Buenas tardes, {b}Tuan [firstname]{/b}."

        anon "Halo, {b}Consuela{/b}."


    menu consuela_button_beachhouse.choice:
        "Bagaimana kabarmu?":
            jump consuela_button_beachhouse.check
        "Rumahnya terlihat bagus!":

            jump consuela_button_beachhouse.praise

        "Pakaian pelayan." if M_consuela.finished_state(S_con04_hint):
            if M_consuela.outfit.is_naked:
                jump consuela_button_beachhouse.dress
            else:
                jump consuela_button_beachhouse.strip

        "Seks oral." if M_consuela.finished_state(S_con03_done):
            jump consuela_button_beachhouse.blowjob

        "Seks." if M_consuela.finished_state(S_con04_hint):
            if L_beachhouse_kitchen.is_here(M_consuela):
                jump consuela_button_beachhouse.sex_kitchen
            else:
                jump consuela_button_beachhouse.sex_entrance
        "Sampai jumpa.":

            pass

    anon @ a_wave "Sampai jumpa."

    consuela "Ya, {b}Pak [firstname]{/b}."

    consuela "Aku beritahu {b}Camila{/b} \"hai\", untukmu."

    anon "Hehe, baiklah."

    hide anon with dissolve
    return


label consuela_button_beachhouse.check:
    anon "Bagaimana kabarmu?"

    consuela "saya baik."

    consuela "Bagaimana kabarmu?"

    anon "Saya melakukannya dengan sangat baik, terima kasih."

    consuela "Uhh, {b}Pak [firstname]{/b}?"

    anon @ -m_talk "Hmm?"

    consuela "Putriku, {b}Camila{/b}... Kamu berkencan?"

    anon f_worried "Tanggal?"

    anon "Ehh, menurutku putrimu tidak akan begitu menyukainya..."

    consuela "Tidak, dia melakukannya!"

    consuela "{b}Camila{/b}, istri yang baik."

    consuela "saya mengajar."

    anon f_normal "Hehe, kalau kamu bilang begitu..."

    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.praise:
    anon "Rumahnya terlihat bagus!"

    consuela "Ya, aku bersih-bersih dengan baik."

    anon "Heh, kamu bersih-bersih dengan baik... Bagus sekali."

    pause
    anon "Apakah kamu yakin aku tidak bisa membayarmu untuk ini?"

    consuela @ -m_talk "Hmm?"

    consuela "Oh, tidak... {b}Pak [firstname]{/b}!"

    consuela "Anda menemukan pekerjaan."

    consuela "Tidak ada bayaran."

    consuela "Aku membersihkannya untukmu!"

    anon "Baiklah, jika kamu bersikeras..."

    consuela "Ya, bersikeras."

    consuela "I have to make sure you marry my daughter..." (show_native="Debo asegurarme de que te cases con mi hija...")
    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.dress:
    anon f_flirt "Kamu bisa memakai kembali seragam pelayanmu, jika kamu mau."

    consuela @ -m_talk "Hmm?"

    anon @ f_confused "Anda tidak perlu telanjang lagi."

    consuela f_sad "Tidak telanjang?"

    anon "Ya, kamu tahu... Kecuali kamu hanya ingin telanjang?"

    consuela f_smirk "I don't mind being naked for you, {b}Mister [firstname]{/b}." (show_native="No me importa estar desunda para ti, {b}Mister [firstname]{/b}.")
    consuela "But if you want me to get dressed, I will." (show_native="Pero si quieres que me vista, lo haré.")
    anon @ -m_talk "..."
    consuela "Oke, aku berpakaian."

    anon "Dingin."

    consuela "Probably better this way." (show_native="Probablemente mejor de esta manera.")
    consuela "{b}Camila{/b} would be upset if she saw me here naked..." (show_native="{b}Camila{/b} estaría molesta si me viera aquí desnuda...")
    anon @ a_point "Saya tidak mengerti apa yang Anda katakan..."

    show consuela b_naked_blank a_remove_bra2 f_normal_down with dissolve
    pause
    show consuela b_naked_blank a_remove_bra1 with dissolve
    pause
    show consuela b_lift2 with dissolve
    pause
    show consuela b_lift with dissolve
    pause
    show consuela b_dressed a_idle f_smirk with dissolve
    $ M_consuela.outfit.is_naked = 0
    $ M_consuela.outfit.set_default_outfit_schedule([["dressed", "dressed", "hospital", "hospital"]])
    consuela "kamu suka?"

    anon @ f_laugh "Ya, pakaian pelayan itu sangat seksi untukmu!"

    consuela "Seksi?"

    anon "Sangat seksi!"

    consuela @ f_laugh "hehe!"

    consuela "You make me feel young again!" (show_native="¡Me haces sentir joven otra vez!")
    show consuela b_kiss
    hide anon
    with dissolve
    anon "!!!"
    pause
    show anon f_flirt
    show consuela b_magic a_hips:
        xoffset 0
    with dissolve
    anon "Untuk apa itu?"

    consuela "Kamu anak baik."

    anon @ f_laugh "Hehe, baiklah."

    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.strip:
    anon f_shy "Hei, aku bertanya-tanya..."

    consuela @ -m_talk "Hmm?"

    anon "Jika saya meminta Anda untuk membersihkan rumah saya dalam keadaan telanjang, apakah Anda akan melakukannya?"

    consuela f_sad "Telanjang?"

    anon a_behind_head "Ya, kamu tahu... Tidak ada pakaian?"

    consuela f_smirk "Ahh, you want me to undress for you?" (show_native="¿Ahh, Quieres que me desnude por ti?")
    consuela "Ya, benar."

    anon f_surprised a_idle "Anda akan melakukannya?"

    consuela "Ya, untukmu, aku bersedia."

    show anon f_flirt
    consuela "Kamu anak baik."

    consuela "Tanggal {b}Camila{/b} ya?"

    anon f_worried "Maksudku, aku akan mencoba..."

    consuela "Bagus."

    consuela "Aku telanjang untukmu."

    anon f_flirt @ f_laugh "Luar biasa!"

    show consuela b_lift with dissolve
    pause
    show consuela b_lift2 with dissolve
    pause
    show consuela b_naked_blank a_remove_bra1 f_normal_down with dissolve
    pause
    show consuela b_naked_blank a_remove_bra2 with dissolve
    pause
    show consuela b_naked f_smirk a_idle with dissolve
    consuela "kamu suka?"

    anon f_flirt_low "{i}*Gulp*{/i} Y-ya, aku suka."

    show consuela b_naked_blank f_laugh a_boob1 with dissolve
    consuela "Hehe, bagus!"

    consuela f_smirk a_boob2 "You make me feel young again!" (show_native="¡Me haces sentir joven otra vez!")
    pause
    show consuela a_boob1 with dissolve
    $ M_consuela.outfit.set_default_outfit_schedule([["naked", "naked", "hospital", "hospital"]])
    show consuela b_magic a_hips with dissolve
    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.blowjob:
    anon f_flirt "Apakah kamu pikir kamu bisa um..."

    consuela @ -m_talk "Hmm?"

    anon f_worried "Ingat ketika Anda berlutut dan-"

    consuela a_idle f_smirk @ a_dick_big "Do you want me to suck your cock again?" (show_native="¿Quieres que te chupe la verga otra vez?")
    anon f_shy @ a_behind_head "Y-ya, itu."

    consuela "Hehe, oke."

    consuela "aku melakukannya untukmu."

    anon "Benar-benar?"

    show anon b_shirt od_dick1 f_shy_down behind consuela
    show consuela b_bend f_normal_up a_pull1
    with dissolve
    consuela "Ya."

    consuela a_pull2 f_unsure_down "saya suka."

    pause
    consuela a_poke "Seperti, umm... Lolipop."

    show consuela f_normal_up a_idle with dissolve
    anon "L-lolipop?"

    show anon od_dick2 with dissolve
    pause .25
    show consuela f_unsure_down
    show anon od_dick3 with dissolve
    show anon od_dick4
    consuela "Ya, lolipop!"

    show consuela b_bend_jerk f_normal_down
    show anon od_empty
    with dissolve
    consuela @ f_laugh "hehe!"

    consuela "I'll suck your dick anytime, {b}Mister [firstname]{/b}!" (show_native="¡Te la voy a chupar cuando quieras, {b}Mister [firstname]{/b}!")

    call scene_consuela_blowjob.repeat from consuela_button_beachhouse.blowjob_resume

    call consuela_button_stage
    show consuela a_hips f_smirk
    show anon b_shirt a_sides od_dick1 f_tired_happy
    with fade
    consuela "Mmm, you have a wonderful taste!" (show_native="¡Mmm, sabes bien rico!")
    anon "Fiuh."

    consuela "kamu suka?"

    anon "Ya saya suka!"

    consuela "Me too, daddy." (show_native="Yo también, papi.")
    pause
    consuela "I should go back to work now." (show_native="Debería volver a trabajar ahora.")
    anon "Hmm?"

    consuela "Saya membersihkan sekarang."

    anon "O-oh, oke."

    anon "Umm, terima kasih untuk uh..."

    consuela @ a_dick_big "Sucking your cock?" (show_native="¿Chuparte la verga?")
    anon "Ya."

    consuela "Tidak apa-apa, ayah."

    show anon b_empty f_flirt_low
    show consuela b_kiss10
    with dissolve
    pause
    show anon b_shirt f_flirt
    show consuela b_magic
    with dissolve
    consuela "{b}Camila{/b}, gadis yang beruntung..."

    anon @ -m_talk "..."
    hide anon with dissolve

    $ game.timer.tick()
    return


label consuela_button_beachhouse.sex_entrance:
    anon f_flirt "Saya kira Anda tidak ingin melakukannya, umm..."

    consuela f_sad "What?" (show_native="¿Qué?")
    anon "Seks?"

    consuela f_smirk "Oh, seks..."

    consuela "Oke, benar."

    anon "Ya?"

    consuela "Ya."

    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon @ f_laugh "Manis!"


    call scene_consuela_sex_stairs.repeat from consuela_button_beachhouse.sex_entrance_resume
    python:
        persistent.cookie_jar['Consuela']['unlocked'] = True
        persistent.cookie_jar['Consuela']['gallery']['03_unlocked'] = True

    call consuela_button_stage
    jump consuela_button_beachhouse.sex


label consuela_button_beachhouse.sex_kitchen:
    anon f_flirt "Aku bisa melihatmu membersihkan lantai itu sepanjang hari..."

    consuela f_smirk "kamu suka?"

    anon "Ya, sangat banyak!"

    pause
    consuela "Anda ingin berhubungan seks sekarang?"

    anon "Ya ampun, ayo kita lakukan di sini!"

    consuela "hehe!"

    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon "Kemarilah."

    consuela "Ya, ayah."


    call scene_consuela_sex_counter.repeat from consuela_button_beachhouse.sex_kitchen_resume

    call consuela_button_stage
    jump consuela_button_beachhouse.sex


label consuela_button_beachhouse.sex:
    show anon f_flirt
    show consuela f_smirk a_hips
    with fade
    anon "Saya harap itu bagus?"

    consuela "Ya, bagus sekali!"

    consuela "saya suka!"

    show consuela b_kiss
    hide anon
    with dissolve
    pause
    show anon f_flirt
    show consuela b_magic:
        xoffset -200
    with dissolve
    consuela "Anak baik."

    consuela "Kamu ingin aku memasak untukmu?"

    anon @ -m_talk "Hmm?"

    anon "Oh tidak."

    anon "Tidak apa-apa."

    consuela @ f_laugh "Hehe, oke."

    consuela "Saya memasak untuk saya."

    consuela "Sex always makes me hungry." (show_native="El sexo siempre me da hambre.")
    anon "Baiklah."

    pause
    anon @ a_wave "Terima kasih, {b}Consuela{/b}."

    consuela "Tidak apa-apa, ayah."

    hide anon with dissolve

    $ game.timer.tick()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
