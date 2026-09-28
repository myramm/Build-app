label consuela_button_beachhouse:
    show anon with dissolve
    if game.timer.is_morning():
        if M_consuela.finished_state(S_con03_done):
            consuela "Buenos días, papi."
        else:
            consuela "Buenos días, {b}Mister [firstname]{/b}."
        anon "Good morning, {b}Consuela{/b}."
    else:
        if M_consuela.finished_state(S_con03_done):
            consuela "Buenas tardes, papi."
        else:
            consuela "Buenas tardes, {b}Mister [firstname]{/b}."
        anon "Hello, {b}Consuela{/b}."

    menu consuela_button_beachhouse.choice:
        "How are you?":
            jump consuela_button_beachhouse.check
        "The house looks great!":

            jump consuela_button_beachhouse.praise

        "Maid outfit." if M_consuela.finished_state(S_con04_hint):
            if M_consuela.outfit.is_naked:
                jump consuela_button_beachhouse.dress
            else:
                jump consuela_button_beachhouse.strip

        "Blowjob." if M_consuela.finished_state(S_con03_done):
            jump consuela_button_beachhouse.blowjob

        "Sex." if M_consuela.finished_state(S_con04_hint):
            if L_beachhouse_kitchen.is_here(M_consuela):
                jump consuela_button_beachhouse.sex_kitchen
            else:
                jump consuela_button_beachhouse.sex_entrance
        "See you around.":

            pass

    anon @ a_wave "See you around."
    consuela "Si, {b}Mister [firstname]{/b}."
    consuela "I tell {b}Camila{/b} \"hi\", for you."
    anon "Heh, alright."
    hide anon with dissolve
    return


label consuela_button_beachhouse.check:
    anon "How are you?"
    consuela "I good."
    consuela "How you?"
    anon "I'm doing very well, thank you."
    consuela "Uhh, {b}Mister [firstname]{/b}?"
    anon @ -m_talk "Hmm?"
    consuela "My daughter, {b}Camila{/b}... You date?"
    anon f_worried "Date?"
    anon "Ehh, I don't think your daughter would like that very much..."
    consuela "No, she do!"
    consuela "{b}Camila{/b}, good wife."
    consuela "I teach."
    anon f_normal "Heh, if you say so..."
    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.praise:
    anon "The house looks great!"
    consuela "Si, I clean good."
    anon "Heh, you do clean good... Very good."
    pause
    anon "Are you sure I can't pay you for this?"
    consuela @ -m_talk "Hmm?"
    consuela "Oh, no... {b}Mister [firstname]{/b}!"
    consuela "You find job."
    consuela "No pay."
    consuela "I clean for you!"
    anon "Alright, if you insist..."
    consuela "Si, insist."
    consuela "I have to make sure you marry my daughter..." (show_native="Debo asegurarme de que te cases con mi hija...")
    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.dress:
    anon f_flirt "You can put your maid uniform back on, if you want."
    consuela @ -m_talk "Hmm?"
    anon @ f_confused "You don't have to be naked anymore."
    consuela f_sad "No naked?"
    anon "Yeah, you know... Unless you just want to be naked?"
    consuela f_smirk "I don't mind being naked for you, {b}Mister [firstname]{/b}." (show_native="No me importa estar desunda para ti, {b}Mister [firstname]{/b}.")
    consuela "But if you want me to get dressed, I will." (show_native="Pero si quieres que me vista, lo haré.")
    anon @ -m_talk "..."
    consuela "Okay, I dress."
    anon "Cool."
    consuela "Probably better this way." (show_native="Probablemente mejor de esta manera.")
    consuela "{b}Camila{/b} would be upset if she saw me here naked..." (show_native="{b}Camila{/b} estaría molesta si me viera aquí desnuda...")
    anon @ a_point "I have no idea what you're saying..."
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
    consuela "You like?"
    anon @ f_laugh "Yeah, that maid outfit is so sexy on you!"
    consuela "Sexy?"
    anon "Very sexy!"
    consuela @ f_laugh "Hehe!"
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
    anon "What was that for?"
    consuela "You good boy."
    anon @ f_laugh "Heh, alright."
    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.strip:
    anon f_shy "Hey, I was wondering..."
    consuela @ -m_talk "Hmm?"
    anon "If I asked you to clean my house naked, would you do it?"
    consuela f_sad "Naked?"
    anon a_behind_head "Yeah, you know... No clothes?"
    consuela f_smirk "Ahh, you want me to undress for you?" (show_native="¿Ahh, Quieres que me desnude por ti?")
    consuela "Si, I do."
    anon f_surprised a_idle "You will?"
    consuela "Si, for you, I do."
    show anon f_flirt
    consuela "You good boy."
    consuela "Date {b}Camila{/b}, yes?"
    anon f_worried "I mean, I'll try..."
    consuela "Good."
    consuela "I strip for you."
    anon f_flirt @ f_laugh "Awesome!"
    show consuela b_lift with dissolve
    pause
    show consuela b_lift2 with dissolve
    pause
    show consuela b_naked_blank a_remove_bra1 f_normal_down with dissolve
    pause
    show consuela b_naked_blank a_remove_bra2 with dissolve
    pause
    show consuela b_naked f_smirk a_idle with dissolve
    consuela "You like?"
    anon f_flirt_low "{i}*Gulp*{/i} Y-yes, I like."
    show consuela b_naked_blank f_laugh a_boob1 with dissolve
    consuela "Hehe, good!"
    consuela f_smirk a_boob2 "You make me feel young again!" (show_native="¡Me haces sentir joven otra vez!")
    pause
    show consuela a_boob1 with dissolve
    $ M_consuela.outfit.set_default_outfit_schedule([["naked", "naked", "hospital", "hospital"]])
    show consuela b_magic a_hips with dissolve
    jump consuela_button_beachhouse.choice


label consuela_button_beachhouse.blowjob:
    anon f_flirt "Do you think you could umm..."
    consuela @ -m_talk "Hmm?"
    anon f_worried "Remember when you got down on your knees and-"
    consuela a_idle f_smirk @ a_dick_big "Do you want me to suck your cock again?" (show_native="¿Quieres que te chupe la verga otra vez?")
    anon f_shy @ a_behind_head "Y-yeah, that."
    consuela "Hehe, okay."
    consuela "I do for you."
    anon "Really?"
    show anon b_shirt od_dick1 f_shy_down behind consuela
    show consuela b_bend f_normal_up a_pull1
    with dissolve
    consuela "Si."
    consuela a_pull2 f_unsure_down "I like."
    pause
    consuela a_poke "Es like, umm... Lollipop."
    show consuela f_normal_up a_idle with dissolve
    anon "L-lollipop?"
    show anon od_dick2 with dissolve
    pause .25
    show consuela f_unsure_down
    show anon od_dick3 with dissolve
    show anon od_dick4
    consuela "Si, lollipop!"
    show consuela b_bend_jerk f_normal_down
    show anon od_empty
    with dissolve
    consuela @ f_laugh "Hehe!"
    consuela "I'll suck your dick anytime, {b}Mister [firstname]{/b}!" (show_native="¡Te la voy a chupar cuando quieras, {b}Mister [firstname]{/b}!")

    call scene_consuela_blowjob.repeat from consuela_button_beachhouse.blowjob_resume

    call consuela_button_stage
    show consuela a_hips f_smirk
    show anon b_shirt a_sides od_dick1 f_tired_happy
    with fade
    consuela "Mmm, you have a wonderful taste!" (show_native="¡Mmm, sabes bien rico!")
    anon "Phew."
    consuela "You like?"
    anon "Yes, I like!"
    consuela "Me too, daddy." (show_native="Yo también, papi.")
    pause
    consuela "I should go back to work now." (show_native="Debería volver a trabajar ahora.")
    anon "Hmm?"
    consuela "I clean now."
    anon "O-oh, okay."
    anon "Umm, thanks for the uh..."
    consuela @ a_dick_big "Sucking your cock?" (show_native="¿Chuparte la verga?")
    anon "Yeah."
    consuela "De nada, papi."
    show anon b_empty f_flirt_low
    show consuela b_kiss10
    with dissolve
    pause
    show anon b_shirt f_flirt
    show consuela b_magic
    with dissolve
    consuela "{b}Camila{/b}, lucky girl..."
    anon @ -m_talk "..."
    hide anon with dissolve

    $ game.timer.tick()
    return


label consuela_button_beachhouse.sex_entrance:
    anon f_flirt "I don't suppose you'd like to, umm..."
    consuela f_sad "What?" (show_native="¿Qué?")
    anon "Sex?"
    consuela f_smirk "Oh, sexo..."
    consuela "Okay, I do."
    anon "Yeah?"
    consuela "Si."
    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon @ f_laugh "Sweet!"

    call scene_consuela_sex_stairs.repeat from consuela_button_beachhouse.sex_entrance_resume
    python:
        persistent.cookie_jar['Consuela']['unlocked'] = True
        persistent.cookie_jar['Consuela']['gallery']['03_unlocked'] = True

    call consuela_button_stage
    jump consuela_button_beachhouse.sex


label consuela_button_beachhouse.sex_kitchen:
    anon f_flirt "I could watch you clean that floor all day..."
    consuela f_smirk "You like?"
    anon "Yes, very much!"
    pause
    consuela "You want make sex now?"
    anon "Si, let's do it here!"
    consuela "Hehe!"
    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon "Come here."
    consuela "Si, papi."

    call scene_consuela_sex_counter.repeat from consuela_button_beachhouse.sex_kitchen_resume

    call consuela_button_stage
    jump consuela_button_beachhouse.sex


label consuela_button_beachhouse.sex:
    show anon f_flirt
    show consuela f_smirk a_hips
    with fade
    anon "I hope that was good?"
    consuela "Si, very good!"
    consuela "I like!"
    show consuela b_kiss
    hide anon
    with dissolve
    pause
    show anon f_flirt
    show consuela b_magic:
        xoffset -200
    with dissolve
    consuela "Good boy."
    consuela "You want I cook for you?"
    anon @ -m_talk "Hmm?"
    anon "Oh, no."
    anon "That's okay."
    consuela @ f_laugh "Hehe, okay."
    consuela "I cook for me."
    consuela "Sex always makes me hungry." (show_native="El sexo siempre me da hambre.")
    anon "Alright."
    pause
    anon @ a_wave "Thanks, {b}Consuela{/b}."
    consuela "De nada, papi."
    hide anon with dissolve

    $ game.timer.tick()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
