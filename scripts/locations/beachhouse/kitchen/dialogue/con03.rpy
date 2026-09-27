label con03_sing_condo_kitchen:
    scene expression player.location.background_blur
    show consuela b_bending:
        xoffset -500
    show anon f_flirt_low with dissolve:
        flip
    consuela "♪ But today I have finally truly decided ♪" (show_native="♪ Pero hoy por fin me he decidido de veras ♪")
    consuela "♪ To confess my love to him ♪" (show_native="♪ Todo mi amor a confesarle ♪")
    anon "Whoa."

    consuela "♪ I knock on his door and I get goose bumps ♪" (show_native="♪ Toco su puerta y se me enchina la piel ♪")
    anon @ -m_talk "..."
    consuela "♪ A blonde answers the door ♪" (show_native="♪ Y me contesta una güera ♪")
    show consuela b_lift_back with dissolve
    consuela "♪ And my heart breaks ♪" (show_native="♪ Y mi corazón se quiebra ♪")
    show consuela b_dressed a_lift f_singing with dissolve
    consuela "♪ The guy from apartment 512 ♪" (show_native="♪ El chico del apartamento 512 ♪")
    show consuela a_sing with dissolve
    consuela "♪ The one who makes my poor heart jump- ♪" (show_native="♪ Él que hace a mi pobre corazón salt- ♪")
    show consuela -b_bending a_work3 f_normal with dissolve:
        flip
        xoffset 0
    show anon f_shy a_behind_head with dissolve
    pause
    consuela "Buenas tardes, {b}Tuan [firstname]{/b}."

    anon "H-hai."

    consuela "I too loud?"

    anon @ -m_talk "Hmm?"

    anon "Oh tidak!"

    anon a_idle "Not at all!"

    anon "It's a really pretty song."

    anon "Please, uhh..."

    anon "{i}*Ahem*{/i} Keep going."

    consuela f_smirk "Oh, do you like to see me dance?" (show_native="Oh, ¿te gusta verme bailar?")
    show consuela b_back f_normal with dissolve:
        unflip
        xoffset -500
    consuela "You want me to shake my butt for you?" (show_native="¿Quieres que sacuda mi trasero por ti?")
    anon f_shy_low "{i}*Gulp*{/i} I umm, don't understand."

    consuela "kamu suka?"

    show consuela b_back_shake with dissolve
    anon "Y-ya."

    consuela @ f_laugh "Hehehe!"

    consuela "Men have always liked my butt." (show_native="A los hombres siempre les ha gustado mi trasero.")
    anon "S-sorry, I don't mean to stare..."

    consuela @ -m_talk "Hmm?"

    consuela "Tidak apa-apa."

    consuela "I dance for you, {b}Mister [firstname]{/b}."

    pause
    show consuela b_dressed f_smirk with dissolve:
        flip
        xoffset 0
    show anon f_shy
    consuela "{b}Camila{/b} good dancer too."

    consuela "saya mengajar."

    anon "Oh?"

    consuela "You two go dance, yes?"

    consuela "Tanggal?"

    anon @ f_laugh "Heh, yeah right."

    anon "Pretty sure your daughter hates me, {b}Consuela{/b}..."

    consuela f_sad "Hate?"

    consuela "No, no."

    consuela "She is too stupid to recognize a good man." (show_native="Ella es demasiado estúpida para reconocer a un buen hombre.")
    anon f_confused @ -m_talk "..."
    consuela "Ehh..."

    consuela "No hate, just estupido."

    anon f_surprised "Heh, you're saying she's stupid?"

    consuela "Si, stupid!"

    consuela "Pretty and stupid."

    anon f_normal @ f_laugh "Haha!"

    consuela f_normal "Es okay, I teach."

    consuela "She like soon, okay?"

    consuela "Then you go date."

    anon "Jika kamu berkata begitu..."

    consuela "Saya bersedia."

    show consuela b_back f_normal with dissolve:
        unflip
        xoffset -500
    show anon f_flirt_low
    consuela "But now, I dance for you, okay?"

    show consuela b_back_shake with dissolve
    anon "{i}*Gulp*{/i} Y-ya, oke."

    consuela @ f_laugh "Hehehe!"

    consuela "I'll keep you happy until {b}Camila{/b} comes to her senses." (show_native="Te mantendré feliz hasta que {b}Camila{/b} recupere sus sentidos.")
    show consuela b_back with dissolve
    consuela "You watch."

    show consuela b_bending with dissolve
    consuela "♪ The guy from apartment 512 ♪" (show_native="♪ El chico del apartamento 512 ♪")
    consuela "♪ The one who makes my poor heart jumps ♪" (show_native="♪ Él que hace a mi pobre corazón saltar ♪")
    pause

    scene black with dissolve
    pause 1

    $ player.go_to(L_beachhouse_entrance)
    $ game.timer.tick()
    scene expression player.location.background_blur with dissolve
    show anon f_grin with dissolve
    anon "( Man, {b}Consuela{/b} has a nice butt! )"

    anon "( She was totally putting on a show for me in there... )"

    pause
    anon "( Helping her out of that crappy situation with {b}Mayor Rump{/b} was one of the best decisions I've ever made! )"

    hide anon with dissolve
    return

label con03_done_condo_kitchen:
    scene expression background(576, 440, 3.) as stage at flip
    show layer master at flip
    show anon with dissolve
    anon "Hey {b}Consuela{/b}, I was thinking-"

    show anon f_surprised_down
    anon @ -m_talk "..."

    scene location_beach_house_kitchen_floor
    show consuela b_floor o_floor_undies
    with fade
    anon "!!!" with hpunch
    consuela "Si, {b}Mister [firstname]{/b}?"

    pause
    consuela "{b}Mister [firstname]{/b}?"

    pause
    consuela f_confused "Halo?"

    anon "Hmm?"

    consuela "kamu mau?"

    anon "Y-yes, I do!"

    pause
    consuela "Eh?"

    pause
    consuela f_normal_down "!!!"
    consuela f_smirk "Are you looking at my butt again?" (show_native="¿Estás mirando mi trasero otra vez?")

    scene expression background(576, 440, 3.) as stage at flip
    show layer master at flip
    show anon f_shy
    show consuela f_laugh
    with fade
    consuela "hehe!"

    consuela f_smirk "You really like it, huh?" (show_native="Realmente te gusta, ¿eh?")
    anon @ -m_talk "..."
    show consuela b_back f_normal with dissolve:
        flip
        xoffset 500
    show anon f_flirt_low
    consuela "You want, I dance?"

    anon "Ya, tolong."

    consuela "You're so cute." (show_native="Eres tan lindo.")
    pause
    consuela "Okay, I do for you."

    show consuela b_back_shake with dissolve
    pause
    anon f_grin "(Pembantu terbaik yang pernah ada!)"

    pause
    show anon f_flirt_low
    consuela "kamu suka?"

    anon "Eh ya."

    consuela @ f_laugh "hehe!"

    pause
    consuela "I talk {b}Camila{/b} for you."

    anon "You talked to {b}Camila{/b}?"

    consuela "Ya, {b}Pak [firstname]{/b}."

    consuela "She like you soon."

    anon "I very much doubt that."

    show consuela f_surprised b_dressed with dissolve:
        unflip
        xoffset 0
    show anon f_flirt
    consuela "Crap!" (show_native="¡Mierda!")
    anon f_worried "Ada apa?"

    hide consuela with dissolve
    consuela "I nearly forgot!" (show_native="¡Casi se me olvida!")
    pause
    anon "Where are you-"

    show consuela a_juice with dissolve
    consuela "I make for you."

    anon "You made that for me?"

    consuela "Ya."

    show consuela a_idle
    show anon f_thinking_down a_juice
    with dissolve
    anon "Oh, umm... Thanks, I guess..."

    pause
    anon f_worried "Apa itu?"

    consuela "It's a vegetable smoothie." (show_native="Es un licuado de verduras.")
    anon f_confused @ -m_talk "..."
    consuela "Good for you."

    consuela @ a_flex "Make strong, like bull."

    anon "Oh?"

    anon "It smells like death..."

    consuela "Hehe, you drink!"

    consuela "Good for you, {b}Mister [firstname]{/b}."

    anon "Alright, I guess I can try it."

    show anon a_juice_drink f_smoke with dissolve
    pause
    anon f_disgusted_down a_juice "Ugh, that's umm... Bitter."

    show anon f_sad
    consuela "Si, bitter."

    consuela "I'll add more lemon next time." (show_native="Agregaré más limón la próxima vez.")
    consuela "Drink more, okay?"

    anon "Do I have to?"

    consuela "Si, you drink!"

    anon "Y-ya, oke."

    show anon a_juice_drink f_smoke with dissolve
    consuela "Anak baik."

    show consuela a_pinch f_smirk behind anon with dissolve:
        xoffset -250
    consuela "It will give you strong arms to match your cute butt!" (show_native="¡Te dará brazos fuertes para combinar con tu lindo trasero!")
    anon f_surprised a_juice_drop "!!!"
    show anon f_surprised_down a_sides o_juice_spill with dissolve
    show consuela f_surprised a_shock with dissolve:
        xoffset -200
    consuela "Oh, no!" (show_native="¡Ay, no!")
    anon "Whoops."

    show anon behind consuela
    show consuela f_surprised_down b_bend a_idle with dissolve:
        xoffset 0
    consuela "I sorry, I sorry!"

    consuela a_wipe "I clean!"

    anon "It's okay, {b}Consuela{/b}."

    consuela "No, es okay!"

    consuela "I clean!"

    anon "Really, I'll just go change-"

    show anon o_empty with dissolve
    consuela "Si, change."

    show anon b_shirt a_idle od_dick1
    show consuela a_pull1
    with dissolve
    consuela "I wash for you."

    anon "!!!" with hpunch
    anon "Whoa, whoa!"

    show consuela a_pull2
    with dissolve
    anon "You don't have to-"

    consuela a_idle "!!!"
    show consuela b_dressed a_shock with dissolve
    show anon f_worried
    consuela "OH MY GOD!" (show_native="¡AY DIOS MÍO!")
    show anon f_surprised_teeth a_empty
    show anon_arms_dressed_a_cover_boner behind consuela
    with dissolve
    consuela a_cross "..."
    consuela "I've never seen one so big..." (show_native="Nunca había visto una tan grande...")
    anon f_worried "M-maaf, aku tidak bermaksud-"

    consuela "N-no, es okay."

    consuela f_sad "I was expecting something small." (show_native="Esperaba algo chiquito.")
    anon @ -m_talk "Hmm?"

    consuela a_dick_small "I think, small."

    consuela a_cross @ a_dick_big "You very big, {b}Mister [firstname]{/b}!"

    anon "Oh, umm... Thanks."

    consuela f_smirk "Show."

    anon "Show?"

    show consuela b_bend f_unsure_down a_idle with dissolve:
        xoffset 0
    show anon f_worried_low
    consuela "Si, show."

    anon "You want to see it?"

    consuela "Yes, I want to see it." (show_native="Sí, quiero verlo.")
    show anon f_shy_low
    pause
    anon "O-oke."

    hide anon_arms_dressed_a_cover_boner
    show anon a_up
    with dissolve
    consuela "I cannot believe it..." (show_native="No puedo creerlo...")
    consuela f_normal_up a_poke "Hehe, it's huge!" (show_native="Hehe, ¡está enorme!")
    anon @ -m_talk "..."
    show consuela f_unsure_down a_idle
    show anon od_dick2 with dissolve
    pause .25
    show consuela f_surprised
    show anon od_dick3 with dissolve
    show anon od_dick4
    consuela "Wow!" with hpunch
    consuela "It's like my arm!" (show_native="¡Es como mi brazo!")
    show consuela b_bend_jerk f_normal_down
    show anon od_empty
    with dissolve
    anon "!!!"
    anon "A-apa yang kamu-"

    consuela "Es okay, {b}Mister [firstname]{/b}..."

    consuela "I clean for you."

    anon "Y-you clean?"

    consuela "Ya, aku bersih-bersih dengan baik."


    call scene_consuela_blowjob from con03_done_condo_kitchen.blowjob_resume

    scene expression background(576, 440, 3.) as stage at flip
    show layer master at flip
    show consuela f_smirk
    show anon
    with fade
    consuela "Mmm, delicious too..." (show_native="Mmm, delicioso también...")
    anon "That was... Wow."

    consuela "kamu suka?"

    anon "Ya saya suka!"

    consuela "I clean good."

    anon f_flirt "Sangat bagus."

    consuela "Now I'll wash your clothes." (show_native="Ahora lavaré tu ropa.")
    anon f_worried @ -m_talk "Hmm?"

    consuela "Clothes."

    consuela "saya membersihkan."

    anon f_normal "O-oh, oke."

    anon "Umm, terima kasih untuk uh..."

    consuela "Sucking your cock?" (show_native="¿Chuparte la verga?")
    anon @ -m_talk "..."
    consuela "Tidak apa-apa, ayah."

    show anon b_empty f_flirt_low
    show consuela b_kiss5
    with dissolve
    pause
    show anon b_dressed f_flirt
    show consuela b_dressed
    with dissolve
    consuela "{b}Camila{/b}, gadis yang beruntung..."

    anon f_skeptical @ -m_talk "..."
    hide consuela with dissolve
    anon f_thinking a_thinking @ -m_talk "( Did she just do that so I would be more open about {b}dating her daughter{/b}? )"

    anon @ -m_talk "( I wonder, why is she so hell-bent on hooking us up? )"

    pause
    anon a_behind_head f_grin "( Oh well, best not to dwell on it and just enjoy. )"

    anon "( I mean, free blowjobs... Whenever I want... )"

    anon "( How awesome is that? )"

    pause
    anon f_surprised_down @ -m_talk "( Now I guess I should change my clothes so {b}Consuela{/b} can wash them... )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
