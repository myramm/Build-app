label mel03_init_net:
    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon f_worried_low a_backpack with dissolve:
        flip
    pause
    show anon a_hammock with dissolve
    pause
    anon @ -m_talk "( {i}*Sigh*{/i} Here we go again. )"

    show anon f_surprised
    pause
    show anon f_surprised_left
    pause
    show anon b_dressed_changing3 with dissolve
    pause
    show anon b_dressed_changing2 with dissolve
    anon "( This is so embarrassing... )"

    show anon b_naked_undress_bottom with dissolve
    pause
    show anon b_hammock_pickup with dissolve
    pause
    show anon b_hammock f_worried_low a_net with dissolve
    anon @ -m_talk "( Maybe if I hurry, nobody will see me. )"


    call minigame_hottub (3, 8)

    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon b_hammock f_tired a_net
    with fade
    anon @ -m_talk "( Alright, that's the last step. )"

    anon a_net_sides @ f_disgusted_wince a_net_wipe "( Phew, I'm melting out here in this sun! )"

    pause
    show anon f_surprised_forward
    show melonia b_swimsuit f_smirk_low a_glass behind anon:
        flip
        xoffset -100
    with {'master': dissolve}
    melonia "Well, look who decided to come on time today."

    show anon f_surprised a_cover:
        flip
        xoffset -500
    show melonia a_glass_drink f_drink:
        xoffset 250
    with {'master': dissolve}
    anon "!!!"
    show anon f_unimpressed
    show melonia a_glass f_smirk:
        unflip
        xoffset 0
    with {'master': dissolve}
    anon @ -m_talk "..."
    show anon with {'master': dissolve}:
        unflip
        xoffset 0
    anon "H-hello, ma'am."

    show anon f_worried
    melonia "Come now, {b}Hector{/b}... I thought we were past this."

    show melonia with dissolve:
        xoffset -100
    melonia "There's no need to hide that from me."

    anon "Benar, maaf."

    show anon a_sides f_sad_down with dissolve
    melonia "Itu lebih baik."

    melonia f_smirk_down "Mmm, it looks even bigger today..."

    anon @ -m_talk "..."
    melonia f_smirk "Have you finished cleaning the water?"

    anon "Y-ya, Bu."

    melonia "Sangat bagus."

    melonia "Hold this for me, would you?"

    show melonia a_idle
    show anon a_drink f_worried
    with {'master': dissolve}
    anon f_worried "Tentu saja."

    show anon f_worried_low
    show melonia f_smirk_down a_remove_shall1
    with dissolve
    pause
    show anon f_surprised_low
    show melonia a_remove_shall2
    with dissolve
    pause
    show melonia a_remove_shall3 with dissolve
    melonia "Mmm, that sun feels lovely today, doesn't it?"

    show melonia a_hips_no_shall f_smirk
    show anon of_blush
    with {'master': dissolve}
    anon "{i}*Gulp*{/i} Y-yes, lovely..."

    show melonia b_jacuzzi_climb with dissolve:
        offset (450, 155)
    pause
    show melonia b_jacuzzi f_relax a_idle behind hottub with dissolve:
        xoffset 100
    melonia "Mmm, that's nice!"

    pause
    melonia a_give_me "I'll take that drink now."

    anon @ -m_talk "..."
    melonia f_curious_up "{b}Hektor{/b}?"

    anon @ -m_talk "Hmm?"

    melonia f_smirk_up "My drink?"

    anon f_shy_low "Oh benar!"

    anon a_drink_give "Ini dia."


    scene melonia b_jacuzzi_big f_normal
    with fade
    melonia "Your eyes seem rather fixed, {b}Hector{/b}."

    anon "Sorry, ma'am."

    melonia @ f_laugh "Hehe, you naughty boy!"

    melonia "Why don't you come in and join me?"


    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show melonia b_jacuzzi f_smirk_up a_glass:
        xoffset 100
        yoffset 155
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon b_hammock f_worried_low
    with fade
    anon "{i}*Gulp*{/i} J-join you?"

    anon "I don't think your husband would like that very much..."

    melonia @ f_laugh "Hah, don't concern yourself with my idiot husband!"

    melonia "He doesn't need to know."

    anon "Ehh, I dunno."

    melonia f_pouting_up "Oh, come now {b}Hector{/b}..."

    show anon f_surprised_low
    melonia "I'll make it worth your while, I promise."

    pause
    ricky "Hola!"

    show melonia f_annoyed_up
    show anon f_worried:
        flip
        xoffset -600
    with {'master': dissolve}
    pause
    show anon f_worried:
        unflip
        xoffset -100
    show ricky f_laugh behind anon:
        flip
        xoffset 100
    with dissolve
    ricky "Good morning, señora!"

    show ricky with {'master': dissolve}:
        unflip
        xoffset -400
    ricky "Amigo!"

    ricky f_smirk "How is work today?"

    melonia "{i}*Ahem*{/i} {b}Ricky{/b}, can't you see we're talking?"

    show anon f_worried_low
    show ricky a_up f_smirk_low:
        flip
        xoffset 100
    with {'master': dissolve}
    ricky "Oh, apologies, señora!"

    show anon f_worried
    ricky "I didn't mean to interrupt..."

    ricky a_idle "... Should I, forget the dancing today?"

    show anon f_worried_low
    melonia f_smirk_up "Oh, is it that time already?"

    show anon f_worried
    ricky "Ya, señora."

    show anon f_worried_low
    melonia "Mmm, tell me {b}Hector{/b}..."

    melonia "... Do you dance?"

    show anon f_surprised_low
    show ricky f_smirk:
        unflip
        xoffset -400
    with {'master': dissolve}
    anon "D-dance?!"

    anon f_worried_low "No, not so much..."

    melonia f_annoyed_up "Tidak?"

    ricky @ f_laugh "Hah!"

    show anon f_worried
    show ricky f_smirk_low:
        flip
        xoffset 100
    with {'master': dissolve}
    ricky "Don't be fooled, señora!"

    ricky "{b}Hector{/b}'s a marvelous dancer!"

    show anon f_surprised
    ricky f_normal_low "He's just being modest."

    show anon f_surprised_low
    melonia f_smirk_up "Benar-benar?"

    show anon f_surprised_teeth a_whisper with {'master': dissolve}
    anon "{i}*Whispers*{/i} What the hell are you doing?!"

    show anon a_sides f_surprised
    show ricky f_normal a_whisper:
        unflip
        xoffset -400
    with {'master': dissolve}
    ricky "{i}*Whispers*{/i} Trust me, amigo."

    show anon f_sad_down
    show ricky a_idle f_normal_low:
        flip
        xoffset 100
    with {'master': dissolve}
    melonia "Well, I would very much like to see that!"

    ricky "Well, perhaps he would join me in a dance?"

    ricky f_smirk_low @ f_smirk_wink_low "For the right price, of course."

    melonia "Tentu saja."

    melonia "How's an extra one hundred and fifty sound, {b}Hector{/b}?"

    show anon f_worried
    show ricky f_normal a_whisper:
        unflip
        xoffset -400
    with {'master': dissolve}
    ricky "{i}*Whispers*{/i} See?"

    ricky "{i}*Whispers*{/i} Putty in your hands, amigo!"

    ricky f_smirk a_idle "Surely, {b}Hector{/b} will not pass that up!"

    ricky "Es three times what you make for the cleaning, no?"

    anon "Ehh..."

    anon "Y-ya?"

    ricky a_flex "Yes!" (show_native="¡Toma!")
    ricky -a_flex "This will be fun."

    anon f_surprised a_whisper "{i}*Whispers*{/i} I don't know the first thing about dancing!"

    show anon a_sides
    show ricky a_whisper
    with {'master': dissolve}
    ricky "{i}*Whispers*{/i} No worries, amigo."

    ricky "{i}*Whispers*{/i} Just follow my lead."

    show ricky b_pull_pants a_idle:
        flip
        xoffset 100
    show anon f_surprised_low
    show melonia f_smirk_lipbite
    with dissolve
    pause
    show melonia f_smirk_up
    show ricky b_speedo f_smirk_low
    show anon f_worried
    with dissolve
    ricky "You just lay back and enjoy the show, eh?"

    ricky f_laugh "Come, {b}Hector{/b}."

    ricky "We dance now!"

    $ M_ricky.set('sex speed', 0.4)
    $ M_player.set('sex speed', 0.4)
    hide ricky
    show ricky_body_b_speedo_dance as animation behind anon:
        flip
        xoffset 100
    show anon f_surprised_low
    show melonia f_smirk
    with dissolve
    pause
    anon f_worried_low "Ehh."

    show anon b_hammock_thrust_worried_low:
        xoffset -100
    show melonia f_drink a_glass_drink
    with dissolve
    pause
    show melonia f_smirk a_glass with dissolve
    ricky "That's it, amigo!"

    pause
    ricky "Thrust with power!"

    pause
    melonia @ f_laugh "Oh, very nice, boys!"

    pause
    ricky "Let her feel the passion with the hips!"

    show anon b_hammock_thrust_worried_talk
    anon "Passion?"

    show anon b_hammock_thrust_worried_low
    anon "( This is so weird. )"

    pause
    ricky "You like, señora?"

    show melonia f_drink a_glass_drink with dissolve
    pause 0.5
    melonia a_glass f_smirk @ -m_talk "Mhmm."

    pause
    ricky "Now we must dazzle her!"

    show anon b_hammock_thrust_worried
    anon "Hmm?"

    $ M_ricky.set('sex speed', 0.2)
    pause
    melonia a_clap o_jacuzzi_glass @ f_laugh "Woo!!"

    show anon b_hammock_thrust_worried_talk
    anon "Ehh."

    show anon b_hammock_thrust_worried
    ricky "Finesse, amigo!"

    show melonia a_glass o_empty with dissolve
    pause
    show anon b_hammock_thrust_worried_talk
    anon "O-oke."

    $ M_player.set('sex speed', 0.2)
    show anon b_hammock_thrust_worried_low
    pause
    ricky "Ya!"

    ricky "Like your life depends on it!"

    melonia a_clap o_jacuzzi_glass @ f_laugh "Shake it boys!"

    pause
    ricky "¡Olé!"

    show melonia a_glass o_empty with dissolve
    pause
    ricky "Now the finale!"

    hide animation
    show ricky b_speedo_dance_pose f_smirk_low behind anon:
        flip
        xoffset 100
    with dissolve
    pause
    show anon b_hammock f_worried with dissolve:
        xoffset -150
    anon "Eh, benar..."

    anon f_thinking "... Umm."

    show anon b_hammock_dance_pose f_worried_low with dissolve:
        xoffset -100
    anon "Seperti ini?"

    ricky @ f_laugh "Ya!"

    melonia f_laugh "Very impressive, {b}Ricky{/b}!"

    show anon b_hammock with dissolve
    melonia "You were fantastic, as always!"

    show melonia f_smirk_up
    show ricky b_speedo f_normal_low with dissolve
    ricky "My pleasure, señora."

    melonia "{b}Hector{/b}, you were alright."

    anon f_worried_low "Oh?"

    ricky "He will only improve with time."

    melonia "I imagine his true talents lie elsewhere..."

    show melonia_overlay_o_jacuzzi_glass as glass behind melonia:
        offset (100, 155)
    show melonia a_money
    with dissolve
    melonia "There's a lot more where this came from, {b}Hector{/b}."

    melonia "Why don't you climb in here with me and we can discuss it?"

    anon f_worried @ f_worried_low "Ehh."

    ricky a_finger f_sad_low "I'm afraid this won't be possible today, señora..."

    show melonia f_annoyed_up
    show ricky -a_finger f_normal:
        unflip
        xoffset -400
    with {'master': dissolve}
    ricky "{b}Hector{/b} must go to his other job soon, yes?"

    anon f_skeptical "Ya?"

    show ricky f_smirk_low:
        flip
        xoffset 100
    with {'master': dissolve}
    ricky "Perhaps another day?"

    show anon f_worried_low
    show melonia a_money_give
    with {'master': dissolve}
    melonia "Tsk, fine!"

    show melonia a_idle
    show anon a_money
    with dissolve
    anon a_behind @ a_money "Terima kasih."

    ricky @ f_laugh "Do you require anything else, señora?"

    hide glass
    show melonia f_drink a_glass_drink
    with dissolve
    pause 0.5
    melonia a_glass f_normal_up @ -m_talk "Hmm?"

    ricky "A massage, perhaps?"

    melonia f_smirk_up "Mmm, now that you mention it... My shoulders are quite tense."

    ricky "As I thought."

    show anon f_worried
    show ricky f_smirk:
        unflip
        xoffset -400
    with {'master': dissolve}
    ricky "I will handle things from here, amigo."

    ricky @ f_smirk_wink a_whisper "{i}*Whispers*{/i} Well done, today!"

    anon "Uhh, right... Okay."

    melonia "I expect you'll be on time tomorrow, {b}Hector{/b}?"

    anon f_worried_low "Y-ya, Bu."

    melonia "Very well, that will be all."

    anon "Terima kasih."

    hide anon with dissolve

    scene expression background(480, 392, 5.) as stage with fade
    show anon b_hammock a_money f_worried_low with dissolve:
        flip
        xoffset -400
    pause
    anon @ -m_talk "( Well, that was awkward. )"

    anon f_thinking @ -m_talk "( {b}Melonia{/b} seemed to enjoy it though and I made some really good money... )"

    anon @ -m_talk "( ... {b}Ricky{/b} might be on to something after all. )"

    show anon f_worried_left
    pause
    anon @ -m_talk "( I wonder what I'll have to do next time? )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
