label consuela_button_floor:
    consuela "Hola, papi."
    anon "Hey, {b}Consuela{/b}."

    menu consuela_button_floor.choice:
        "Let me help you up.":
            jump consuela_button_floor.help
        "Sex.":

            jump consuela_button_floor.sex
        "Never mind.":

            pass

    anon f_normal "Never mind."
    consuela "I clean."
    anon @ a_point "Yup, you clean."
    return


label consuela_button_floor.help:
    anon "Let me help you up..."

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
    anon "I could watch you clean that floor all day..."
    consuela f_smirk "You like?"
    anon "Yes, very much!"
    pause
    consuela "You want make sex now?"
    anon "Si."
    consuela "Hehe!"
    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon "I want you just like this!"
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
    anon "Good?"
    consuela "Si, {b}Mister [firstname]{/b}."
    consuela "Good."
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
    consuela "Anal."
    consuela "You do for me?"
    anon @ a_behind_head "Uhh, sure..."
    consuela "Good boy."
    consuela "I like the anal."
    anon "Heh, I'm glad we tried it then."
    consuela "Si, glad."
    pause
    consuela "Okay, I clean now."
    anon "S-sure."
    hide consuela with dissolve
    pause
    anon f_grin @ -m_talk "( Wow! )"
    anon @ -m_talk "( {b}Consuela{/b} likes anal. )"
    anon f_laugh "( Best maid ever! )"
    hide anon with dissolve

    $ game.timer.tick()
    return

label consuela_button_floor.sex_anal:
    show anon f_flirt
    show consuela f_smirk a_hips
    with fade
    consuela "Heh, I can barely stand..." (show_native="Heh, apenas puedo soportar...")
    anon "How was that?"
    consuela "Good, papi."
    consuela "I cum hard."
    anon "Yeah, me too."
    show consuela b_kiss
    hide anon
    with dissolve
    pause
    show anon f_flirt
    show consuela b_magic:
        xoffset -200
    with dissolve
    consuela "Okay, I clean now."
    anon "Alright."
    anon "I'll see you later."
    consuela "Si, later."
    hide anon with dissolve

    $ game.timer.tick()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
