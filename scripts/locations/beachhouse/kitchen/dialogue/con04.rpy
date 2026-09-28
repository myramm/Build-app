label con04_hint_condo_kitchen:
    scene expression background(576, 440, 3.) as stage
    show anon at flip with dissolve
    anon "Hey {b}Consuela{/b}, have you seen my-"
    show anon f_surprised_down
    anon @ -m_talk "..."

    scene location_beach_house_kitchen_floor
    show consuela b_floor f_smirk
    with fade
    anon "!!!" with hpunch
    consuela "Si, papi?"
    anon "Y-you're umm..."
    anon "... Not wearing any panties."
    consuela @ f_normal_down "I forgot my panties?" (show_native="¿Olvidé mis calzones?")
    consuela "How silly of me..." (show_native="Que tonto de mi parte...")

    scene expression background(576, 440, 3.) as stage
    show anon f_shy at flip
    show consuela f_smirk at flip
    with fade
    consuela "You like?"
    anon "{i}*Gulp*{/i} Y-yes."
    consuela "I shaved my pussy for you..." (show_native="Me afeité el coño por ti...")
    anon "Umm."
    consuela "You want?"
    anon "I uhh..."
    consuela "Es okay."
    consuela "I do for you."
    anon @ -m_talk "..."
    show anon a_empty f_surprised_low:
        xoffset -20
    show consuela a_crotch:
        xoffset 200
    with dissolve
    consuela "Feel."
    anon @ -m_talk "!!!"
    pause
    anon f_flirt_low "Y-you're really wet..."
    consuela "Si."
    consuela "Wet for you."
    show consuela b_kiss:
        xoffset 50
    hide anon
    with dissolve
    anon @ -m_talk "!!!"
    pause
    show anon f_flirt:
        flip
        xoffset 0
    show consuela b_dressed a_idle:
        xoffset 200
    with dissolve
    anon "Wow, you taste like lemons."
    consuela "Mmm, you're so cute!" (show_native="¡Mmm, eres tan lindo!")
    consuela "Take off your clothes." (show_native="Quitate la ropa.")
    anon @ -m_talk "Hmm?"
    hide anon
    show consuela a_pull_counter:
        xoffset 300
    with dissolve
    consuela "Take me, papi!"
    anon "Whoa!"

    call scene_consuela_sex_counter from con04_hint_condo_kitchen.sex_resume

    scene expression background(576, 440, 3.) as stage at flip
    show layer master at flip
    jump consuela_button_beachhouse.sex
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
