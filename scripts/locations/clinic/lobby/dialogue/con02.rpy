label con02_job3_hospital_lobby:
    scene expression player.location.background_blur with None
    show anon with dissolve
    anon @ -m_talk "( I should {b}ask the receptionist about a job for Consuela{/b}. )"

    hide anon with dissolve
    return


label con02_ptsd_hospital_lobby:
    scene hospital_desk
    show roz_desk as desk at left
    show consuela b_casual a_crossed f_sad:
        xoffset 100
    with fade
    pause
    show anon b_dressed_disheveled a_cover_boner f_depressed:
        flip
        xoffset -100
    show roz f_smirk behind desk:
        flip
        xoffset -200
    with dissolve
    consuela "That was fast..." (show_native="Eso fue rápido...")
    show roz b_dressed_kneeling f_smirk_down with dissolve
    anon "..."
    consuela "Seragam?"

    show roz b_dressed a_uniform f_smirk with dissolve
    roz "Right here, dollface."

    show roz a_idle
    show consuela a_uniform f_normal
    with dissolve
    consuela "Ah, thank you." (show_native="Ah, gracias.")
    roz "You'll start at twelve dollars per hour." (show_native="Comienzas a doce dólares por hora.")
    consuela f_surprised @ -m_talk "!!!"
    consuela "Twelve dollars?" (show_native="Doce dolares?")
    consuela "An hour?" (show_native="¿Por hora?")
    anon f_confused "Wait a second... You speak Spanish?"

    roz "It's twenty-first century America, kiddo..."

    roz "Everyone who's anyone, speaks Spanish."

    anon f_sad_down @ -m_talk "..."
    roz "What did you get paid on your last job?" (show_native="¿Qué te pagaron en tu último trabajo?")
    consuela f_normal @ f_sad "Thirty dollars per day..." (show_native="Treinta dólares por día...")
    roz f_smirk "Her last employer only paid her thirty dollars a day?!"

    anon "Saya tidak tahu."

    roz f_normal "Where did you find this girl?"

    anon f_worried "She was working at the mayor's house."

    roz "{b}Ronald{/b} had her cleaning that big mansion of his for thirty dollars a day?"

    roz "Tsk, he always was a cheap son of a bitch..."

    anon @ f_skeptical "{b}Ronald{/b}?"

    consuela "Is this really happening?" (show_native="¿Esto realmente está sucediendo?")
    anon "The mayor's name is {b}Ronald Rump{/b}?"

    pause
    anon f_laugh "Ha ha ha!"

    roz "Go and put on your uniform." (show_native="Ve y ponte tu uniforme.")
    roz "You start immediately." (show_native="Empiezas de inmediato.")
    consuela @ f_laugh "Oh, thank you!" (show_native="¡Ay, gracias!")
    show consuela b_dressed_hug:
        xoffset 500
    show anon b_empty f_surprised_down:
        unflip
        xoffset 500
    with dissolve
    consuela "Thank you {b}Mister [firstname]{/b}!" (show_native="¡Gracias {b}Mister [firstname]{/b}!")
    anon "Y-you're welcome, {b}Consuela{/b}..."

    show consuela b_casual:
        xoffset 100
    show anon b_dressed_disheveled f_worried_left:
        flip
        xoffset -100
    with dissolve
    consuela "aku melakukannya untukmu."

    anon @ -m_talk "Hmm?"

    consuela "What you want?"

    consuela "Saya bersedia."

    anon f_normal_left "No, no!"

    anon "You don't owe me anything... I just wanted to help you."

    consuela @ -m_talk "..."
    consuela f_annoyed "What did he say?" (show_native="¿Que dijo el?")
    show anon f_normal
    roz "He says you don't owe him anything..." (show_native="Dice que no le debes nada...")
    show anon f_normal_left
    consuela f_surprised "Is he serious?" (show_native="¿Habla en serio?")
    show anon f_normal
    roz "Ya."

    roz "He is a good boy." (show_native="Es un buen chico.")
    show anon f_normal_left
    consuela f_normal @ -m_talk "..."
    anon "Ada apa?"

    hide anon
    show consuela b_casual_kiss:
        xoffset 300
    anon "!!!" with hpunch
    pause
    show consuela b_casual:
        xoffset 100
    show anon b_dressed_disheveled f_normal_left:
        flip
        xoffset -100
    with dissolve
    consuela "Thank you, {b}Mister [firstname]{/b}!" (show_native="¡Gracias {b}Mister [firstname]{/b}!")
    consuela "You good man!"

    consuela "aku melakukannya untukmu."

    consuela "Saya bersedia."

    anon f_worried_left "Eh?"

    roz "Go and change!" (show_native="Ve y cambia!")
    roz "There is much work to be done." (show_native="Hay mucho trabajo por hacer.")
    consuela "Yes, ma'am." (show_native="Sí, señora.")
    hide consuela with dissolve
    anon f_normal_left @ -m_talk "( Wow, she kissed me... )"

    show anon f_normal
    roz "I guess it's your lucky day, kiddo."

    anon @ -m_talk "Hmm?"

    roz "You wanna head back upstairs for another round?"

    anon f_surprised_teeth "!!!"
    anon f_worried "N-no thanks..."

    anon f_shy a_behind_head "I should really get going."

    roz "Eh, suit yourself."

    roz "You know where to find me if you change your mind."

    pause
    roz "Who knows, I might even let you go down on me next time..."

    anon f_surprised "!!!" with hpunch
    show anon f_surprised_teeth with MoveTransition(2):
        xoffset 500
    pause
    roz f_laugh "Ha ha ha!"


    $ player.go_to(L_hospital)
    scene expression player.location.background_blur with fade
    show anon b_dressed_disheveled a_cover_boner f_sad_down with dissolve
    anon @ -m_talk "( Okay, that might have been the most horrifying image of my entire life. )"

    anon f_disgusted_down @ -m_talk "( I might have thrown up in my mouth a little bit... )"

    anon @ -m_talk "( At least {b}Consuela{/b} has a good job now. )"

    anon f_grin @ -m_talk "( And that kiss... Man, that was something! )"

    pause
    anon f_thinking @ -m_talk "( I wonder if I'll ever see her again? )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
