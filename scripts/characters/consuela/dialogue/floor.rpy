label consuela_button_floor:
    consuela "Halo, ayah."

    anon "Hai, {b}Consuela{/b}."


    menu consuela_button_floor.choice:
        "Biarkan saya membantu Anda berdiri.":
            jump consuela_button_floor.help
        "Seks.":

            jump consuela_button_floor.sex
        "Sudahlah.":

            pass

    anon f_normal "Sudahlah."

    consuela "saya membersihkan."

    anon @ a_point "Yup, kamu bersih-bersih."

    return


label consuela_button_floor.help:
    anon "Biarkan aku membantumu berdiri..."


    call consuela_button_stage
    hide consuela
    show anon b_dressed_pickup
    with fade
    show consuela b_bend a_idle:
        xoffset 180
    show anon -b_dressed_pickup a_handshake f_flirt_low
    with dissolve
    show consuela b_magic a_hips:
        xoffset 0
    show anon -a_handshake -f_flirt_low
    with {'master': dissolve}
    consuela "Thank you, {b}Mister [firstname]{/b}!" (show_native="¡Gracias, {b}Mister [firstname]{/b}!")
    jump consuela_button_beachhouse.choice


label consuela_button_floor.sex:
    anon "Aku bisa melihatmu membersihkan lantai itu sepanjang hari..."

    consuela f_smirk "kamu suka?"

    anon "Ya, sangat banyak!"

    pause
    consuela "Anda ingin berhubungan seks sekarang?"

    anon "Ya."

    consuela "hehe!"

    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon "Aku ingin kamu seperti ini!"

    consuela f_confused "You want to fuck me on the floor?" (show_native="¿Quieres cogerme en el piso?")

    call scene_consuela_sex_floor.repeat from consuela_button_floor.resume
    python:
        persistent.cookie_jar['Consuela']['unlocked'] = True
        persistent.cookie_jar['Consuela']['gallery']['04_unlocked'] = True

    call consuela_button_stage
    if M_consuela.get('sex_location') == 'floor_anal':
        if not M_consuela.once('done_anal'):
            jump consuela_button_floor.sex_anal_virgin
        jump consuela_button_floor.sex_anal
    jump consuela_button_beachhouse.sex


label consuela_button_floor.sex_anal_virgin:
    show anon f_flirt
    show consuela f_smirk a_hips
    with fade
    consuela "I had no idea!" (show_native="¡No tenía ni idea!")
    anon "Bagus?"

    consuela "Ya, {b}Pak [firstname]{/b}."

    consuela "Bagus."

    show consuela b_kiss
    hide anon
    with dissolve
    anon "!!!"
    pause
    show anon f_flirt
    show consuela b_magic:
        xoffset -200
    with dissolve
    consuela "We have to do that again!" (show_native="¡Tenemos que hacer eso otra vez!")
    anon @ -m_talk "Hmm?"

    consuela "Dubur."

    consuela "Anda melakukannya untuk saya?"

    anon @ a_behind_head "Uhh, tentu saja..."

    consuela "Anak baik."

    consuela "Aku suka analnya."

    anon "Heh, aku senang kita mencobanya."

    consuela "Ya, senang."

    pause
    consuela "Oke, aku bersih-bersih sekarang."

    anon "T-tentu saja."

    hide consuela with dissolve
    pause
    anon f_grin @ -m_talk "(Wah!)"

    anon @ -m_talk "( {b}Consuela{/b} suka anal. )"

    anon f_laugh "(Pembantu terbaik yang pernah ada!)"

    hide anon with dissolve

    $ game.timer.tick()
    return

label consuela_button_floor.sex_anal:
    show anon f_flirt
    show consuela f_smirk a_hips
    with fade
    consuela "Heh, I can barely stand..." (show_native="Heh, apenas puedo soportar...")
    anon "Bagaimana tadi?"

    consuela "Bagus, ayah."

    consuela "Aku cum keras."

    anon "Ya, aku juga."

    show consuela b_kiss
    hide anon
    with dissolve
    pause
    show anon f_flirt
    show consuela b_magic:
        xoffset -200
    with dissolve
    consuela "Oke, aku bersih-bersih sekarang."

    anon "Baiklah."

    anon "Sampai jumpa nanti."

    consuela "Ya, nanti."

    hide anon with dissolve

    $ game.timer.tick()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
