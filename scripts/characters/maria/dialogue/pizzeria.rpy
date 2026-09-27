label maria_button_pizzeria:
    if game.timer.is_day():
        show anon behind maria with dissolve
        anon "Hey, {b}Maria{/b}."

        show maria a_spoon_hips f_normal with dissolve:
            unflip
            xoffset 0
        maria @ -m_talk "Hmm?"

        if M_anon.finished_state(S_ano11_bone):
            maria "Oh, hey there, handsome."

            maria f_sexy "You come back here lookin' for trouble?"

        else:
            maria "Oh, hey there, {b}[firstname]{/b}."

            maria "What can I do for ya?"

    else:
        show anon f_flirt_low behind maria with dissolve
        pause
        show maria b_dressed f_confused with dissolve
        maria "{b}[firstname]{/b}?"

        show anon f_flirt
        if M_anon.finished_state(S_ano11_bone):
            maria "Oh, hey there, handsome."

            maria f_sexy "You lookin' for trouble?"

        else:
            maria "Isn't it past your bedtime?"

            anon @ f_unimpressed "Sangat lucu."


    menu maria_button_pizzeria.choice:

        "Do you need any help?" if game.timer.is_day():
            jump maria_button_pizzeria.help

        "It smells amazing in here!" if game.timer.is_day():
            jump maria_button_pizzeria.smell

        "You want me to do that?" if game.timer.is_dark():
            jump maria_button_pizzeria.stock
        "You and {b}Tony{/b}.":

            jump maria_button_pizzeria.tony

        "Adopsi?" if M_anon.between_states(S_ano08_work, S_ano10_tony):
            jump maria_button_pizzeria.adoption

        "Sperm donor?" if M_anon.between_states(S_ano08_work, S_ano10_tony):
            jump maria_button_pizzeria.donor

        "Seks." if M_anon.finished_state(S_ano11_bone):
            jump maria_button_pizzeria.suggest

        "Hanya menyapa." if game.timer.is_day():
            pass

        "Selamat malam." if game.timer.is_dark():
            pass

    if game.timer.is_day():
        anon f_normal "Hanya menyapa."

        if M_anon.finished_state(S_ano11_bone):
            maria f_normal "Alright, handsome."

            show anon b_empty f_laugh
            show maria b_dressed_kiss_mc_cheek behind anon
            with dissolve
            pause
            show anon b_dressed f_normal
            show maria b_dressed
            with dissolve
        else:
            maria f_normal "Alright, kid."

        maria "Be careful out there."

        anon @ a_wave "Aku akan menjadi."

    else:
        anon f_normal "Selamat malam."

        if M_anon.finished_state(S_ano11_bone):
            maria f_normal "Oh baiklah."

            maria "Be careful out there."

            show anon b_empty
            show maria b_dressed_kiss_mc_cheek behind anon
            with dissolve
            pause
            show anon b_dressed
            show maria b_dressed
            with dissolve
        else:
            maria f_normal "Good night, kid."

        maria "Be careful goin' home, yeah?"

        anon @ a_wave "Aku akan menjadi."


    hide anon with dissolve
    return


label maria_button_pizzeria.adoption:
    anon f_normal "Jadi, Anda sedang memikirkan tentang adopsi?"

    maria f_normal "Yeah, I think it's the best option."

    maria "I mean, {b}Tony{/b} and I both got lots of experience with orphans but he don't wanna hear nothin' about it."

    pause
    maria @ f_laugh "Heh, he can be a real stubborn bastard when he wants to be."

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.cooking:
    anon "Saya ikut!"


    call minigame_pizza2 (6)

    call maria_button_stage
    show maria a_idle b_magic f_normal:
        flip
        xoffset -100
    show anon behind maria:
        flip
        xoffset 50
    with fade
    maria "How's ya doin' over here?"

    anon "Everything is fine."

    pause
    maria @ f_surprised "Wow, these are lookin' real good, {b}[firstname]{/b}!"

    maria "I'm startin' to think you got a real aptitude for this!"

    anon @ f_laugh "Nah, I just had a good teacher..."

    show anon m_talk
    show maria o_blush with {'master': dissolve}
    anon -m_talk "Itu saja."

    maria "Ahh, you sweet talker you..."

    show maria o_empty with {'master': dissolve}
    pause
    maria f_sexy "You just earned yourself a very special reward!"

    anon "Oh?"

    maria a_cannoli_hold "One of my famous {b}cannolis{/b}!"

    anon f_unimpressed "Oh."

    maria @ f_laugh "hehe!"

    anon f_worried "Maksudku-"

    show maria a_idle
    show anon a_cannoli
    with dissolve
    anon "T-thank you."

    maria "You're welcome handsome."

    show anon a_cannoli_eat f_cough with dissolve
    pause
    anon a_cannoli_eaten f_surprised_shock_food @ -m_talk "!!!" with hpunch
    anon f_orgasm_food o_boner "Ya Tuhan..."

    show maria f_laugh
    pause
    show maria f_sexy_lipbite_down
    anon "These are so amazing!"

    show anon a_cannoli_gobble f_yawn with dissolve
    show maria f_sexy
    pause

    if M_anon.finished_state(S_ano11_bone):
        show anon f_orgasm_food a_idle with dissolve
        maria "I see somethin' else that looks pretty amazin' too."

        anon f_confused @ -m_talk "Hmm?"

        show anon o_empty f_flirt_low behind maria
        show maria f_normal_down b_dressed_bending a_idle:
            xoffset 50
        with dissolve
        pause
        show anon b_shirt od_dick3
        show maria a_remove2
        with dissolve
        show anon od_dick4
        maria "I think I'll have myself a cream filled treat too, what do you say?"

        anon "Tentu saja."

        maria @ f_laugh "hehe!"


        call scene_maria_blowjob.repeat
        $ unlock_scene('maria', '02_unlocked')

        call maria_button_stage
        show maria a_idle b_magic f_sexy:
            flip
            xoffset -100
        show anon f_flirt a_sides behind maria:
            flip
            xoffset 50
        with fade
        maria "Now that was a tasty treat!"

        anon "Oh, man... That was amazing!"

        pause
        anon f_normal @ f_laugh "I can barely stand."

        maria @ f_laugh "hehe!"

        maria "Well, I'm glad you enjoyed it."

        pause
        maria "Now if you'll excuse me, these pizzas aren't gonna put themselves in the oven."

        anon "Y-yeah, of course."

        anon @ a_wave "Sampai jumpa nanti."

    else:
        maria @ f_laugh "Heh, just don't tell {b}Tony{/b} I gave you last one, yeah?"

        show anon f_orgasm_food a_idle with dissolve
        anon "Tidak, aku tidak akan melakukannya."

        maria "Anak baik."


    hide anon with dissolve
    return 'afterglow'


label maria_button_pizzeria.date:
    anon "If you're up for it?"

    maria f_normal @ f_sexy "Tentu saja!"

    maria "The doctor says I should be havin' sex as often as possible during this part of my cycle."

    maria @ f_laugh "I'll have {b}Tony{/b} set up the store room for us again, okay?"

    anon "Awesome, I'll {b}see you tonight{/b} then."

    maria f_sexy "Don't keep me waitin', handsome."

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.donor:
    anon f_worried "Would you ever try a sperm donor?"

    maria f_disgusted "Ya."

    maria "Just thinkin' about puttin' a stranger's... Stuff inside me..."

    show maria f_disgusted_tongue
    pause
    maria f_disgusted "The whole thing freaks me out!"

    anon @ f_skeptical "Oh oke..."

    maria f_annoyed @ a_point "Don't look at me like that!"

    maria "Would you be okay stickin' some random guy's baby batter up inside yourself?"

    anon f_surprised "!!!"

    menu:
        "Eww, tidak!":
            anon f_disgusted "Tentu saja tidak!"

            maria "Well, why should it be any different for me?!"

            pause
            maria "Because I have a uterus?"

            anon f_worried "T-tidak, aku tidak bermaksud-"

            maria "Eh ya."

            maria "Why don't you think before you open ya mouth next time, knucklehead!"

        "Ya...":

            anon a_thinking f_thinking "Ya..."

            maria f_disgusted "Wait, are you really considering that?"

            anon a_idle f_shy "That's, umm..."

            anon f_skeptical "... Tidak?"

            maria @ a_up f_sad "Just forget I asked."


    jump maria_button_pizzeria.choice


label maria_button_pizzeria.family:
    anon "Have you ever been?"

    maria "Tentu saja."

    maria "{b}Tony{/b} and I try to go every few years."

    anon "Oh?"

    maria "My ma moved back there after my father died."

    maria "I've got an aunt, two uncles, and a dozen or so cousins out there."

    anon "Big family, huh?"

    maria "Big families are an Italian tradition."

    maria "When you love cookin' as much as we do, you gotta make sure there's lots of mouths around to feed."

    anon @ f_laugh "Hehe, itu lucu!"

    maria "Yeah, but it's also true."

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.flirt:
    anon f_flirt "Are they all as pretty as you?"

    maria @ f_laugh a_spoon_heart "Heh, what did you say?"

    pause
    maria f_sexy "Are you making a pass at me, {b}[firstname]{/b}?"

    anon f_normal "N-no, I was just-"

    maria "You silver-tongued little devil..."

    maria f_confused "I'm old enough to be your mother, ya know?"

    anon "Maaf."

    maria f_normal "Heh, it's fine."

    maria "I ain't never met a girl who didn't like a compliment."

    maria "You should be careful hittin' on married broads though..."

    maria f_confused "I mean, unless you like gettin' your teeth knocked out?"

    anon f_worried "I do not."

    maria f_normal @ f_laugh "Haha!"

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.help:
    anon f_normal "Do you need any help?"


    if M_anon.finished_state(S_ano06_cook):
        maria f_normal @ f_laugh "You remember how to work the prep station?"

        anon "Tentu saja."

        maria "Well, you're more than welcome to do that, if you'd like."

        maria "Do a good job and there might be a reward waitin' for ya..."


        menu:
            "Tentu saja!":
                jump maria_button_pizzeria.cooking
            "Mungkin nanti.":

                pass

        anon "Mungkin nanti."

        maria "Oh, no worries."

        maria "I'm sure {b}Tony{/b} has lots of deliveries you can help with..."

    else:
        maria f_normal @ f_laugh a_spoon_heart "Oh, you're a cook now?"

        anon "T-tidak?"

        maria @ f_laugh "Relax, kid."

        maria "Aku hanya ingin menghancurkanmu."

        pause
        maria "I got it all under control back here."

        maria "You just focus on makin' those deliveries, eh?"

        anon "Ya, Bu."


    jump maria_button_pizzeria.choice


label maria_button_pizzeria.italy:
    anon "I'd love to see Italy."

    maria "It's a beautiful place, full of rich history and culture."

    maria @ f_eyeroll "And the food, oh my god!"

    anon "That good, huh?"

    maria @ a_spoon_heart "Phew, {b}[firstname]{/b}... I'm tellin' ya."

    maria "You'll think you died and went to heaven."

    pause
    maria "Nobody ever left a table hungry in Italy."

    maria "I promise you that."

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.sex:
    anon f_flirt "Why not here and now?"

    if not M_maria.once('sex_kitchen'):
        maria f_confused "What, here in the kitchen?"

        anon "Ya."

        maria f_sexy_lipbite_down @ -m_talk "..."
        anon f_worried "{b}Tony{/b} wouldn't mind, would he?"

        maria f_sexy "Hmm, oke."

    else:
        maria f_sexy "Lagi?"

        anon "Ya."

        maria @ f_sexy_lipbite_down -m_talk "..."

    call scene_maria_sex_kitchen.normal
    $ unlock_scene('maria', '03_unlocked', variant='normal')

    call maria_button_stage
    show maria a_idle f_normal:
        unflip
        xoffset 0
    show anon
    with fade
    maria "Alright, I should get back to cookin'."

    anon "Ya baiklah."

    show anon b_empty f_laugh
    show maria b_magic_kiss_mc_cheek behind anon
    with dissolve
    pause
    show anon b_dressed f_normal
    show maria b_magic
    with dissolve
    maria "That was wonderful, {b}[firstname]{/b}."

    maria "Terima kasih."

    anon @ f_laugh "Heh, no problem!"

    hide anon with dissolve
    return 'afterglow'


label maria_button_pizzeria.smell:
    anon f_normal "It smells amazing in here!"

    maria f_confused "Yah, aku harap begitu!"

    maria "I've been cooking since before I could walk."

    anon "Benar-benar?"

    maria "Ah, yeah."

    maria f_normal "Didn't {b}Tony{/b} tell you?"

    maria "My parents owned the best Italian restaurant in Brooklyn!"

    anon "What was it called?"

    maria "{i}La Bottega Dei Sapori{/i}."

    anon f_confused "La boatle de Sa- Huh?!"

    maria @ f_laugh "Hahahaah!"

    show anon f_shy
    pause
    maria "It means {i}The Shop of Flavors{/i} in Italian."

    anon f_normal "The shop of flavors, huh?"

    maria "Yeah, my father was a very uncreative old bastard."

    maria "It's how I ended up with the name {b}Maria{/b}."

    anon "I like your name."

    maria "Heh, you should fly over to Italy then..."

    maria "... You'll find a million girls named {b}Maria{/b}."


    menu:
        "Are they all as pretty as you?":

            jump maria_button_pizzeria.flirt
        "Have you ever been?":

            jump maria_button_pizzeria.family
        "I'd love to see Italy.":

            jump maria_button_pizzeria.italy

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.stock:
    anon f_normal "You want me to do that?"

    maria f_normal @ f_laugh "Oh, you're the stock boy now?"

    anon f_worried "T-tidak?"

    if M_anon.finished_state(S_ano11_bone):
        maria @ f_laugh "Relax, handsome."

    else:
        maria @ f_laugh "Relax, kid."

    maria "Aku hanya ingin menghancurkanmu."

    show anon f_normal
    pause
    maria "I got it all under control back here."

    maria "Get your butt home and take care of your ma."

    jump maria_button_pizzeria.choice


label maria_button_pizzeria.suggest:
    anon f_flirt "Want to... Do it?"


    if game.timer.is_day():
        maria f_confused "Oh, you wanna try again tonight?"

        menu:
            "Ya.":
                jump maria_button_pizzeria.date

            "Why not here and now?" if M_anon.finished_state(S_ano11_done):
                jump maria_button_pizzeria.sex

    show maria f_sexy
    anon "If you're up for it?"

    maria "Tentu saja!"

    maria f_normal "Give Tony and I a few minutes to get the bed set up."

    maria "You can wait in the restaurant, it won't be long."

    hide anon with {'master': dissolve}
    maria "{b}Tony{/b}! Get your butt in here!"


    $ player.go_to(L_pizzeria_interior)
    $ game.timer.tick(3)
    scene expression player.location.background_blur
    show anon
    with slowfade
    maria "Everything's ready!"

    anon f_grin "( That's my cue! )"

    hide anon with dissolve
    return 'sex'


label maria_button_pizzeria.tony:
    anon f_normal "About you and {b}Tony{/b}..."

    maria f_normal "What about us?"

    anon "How did you end up together?"

    if game.timer.is_evening():
        show maria f_laugh a_point
    else:
        show maria f_laugh a_spoon_point
    with dissolve
    maria "Heh, we ended up together because {b}Tony{/b} wouldn't take no for an answer..."

    if game.timer.is_evening():
        show maria a_hips f_normal
    else:
        show maria a_spoon_hips f_normal
    with dissolve
    anon "You told him no?"

    maria f_shy "Not me, my father."

    maria "He hated {b}Tony{/b} 'til the day he died."

    anon f_worried "Kenapa?"

    if game.timer.is_evening():
        show maria a_sides
    else:
        show maria a_spoon_sides
    with dissolve
    maria "Well, it's complicated..."

    pause
    maria "Let's just say that {b}Tony{/b} used to be associated with an... Unsavory element."

    anon @ -m_talk "..."
    anon "Saya tidak mengerti."

    if game.timer.is_evening():
        show maria a_hips
    else:
        show maria a_spoon_hips
    with dissolve
    maria "Ahh, that's probably for the best."

    pause
    anon "You liked him though?"

    maria f_sexy "Tentu saja."

    maria "I fell in love with {b}Tony{/b} the moment I met him."

    if game.timer.is_evening():
        show maria a_back
    else:
        show maria a_spoon_heart
    with dissolve
    maria "He was THE quintessential bad boy."

    if game.timer.is_evening():
        show maria a_hips
    else:
        show maria a_spoon_hips
    with dissolve
    anon f_normal "Oh?"

    maria "I was always a sucker for the bad boys."

    pause
    maria f_normal "Don't get me wrong, {b}Tony{/b} was sweet too!"

    maria "A real romantic..."

    maria "... And he did everything he could to get in my father's good graces."

    maria f_annoyed "Even after the son of a bitch disowned me."

    anon f_surprised "Your father disowned you?!"

    maria "Ya."

    maria "He told me if I married {b}Tony{/b}, he would never speak to me again."

    anon f_worried "Sialan..."

    pause
    anon "So you just never spoke with him again?"

    maria f_normal "Nah, we made up twelve years later..."

    anon f_shock "Twelve years?!" with hpunch
    pause
    anon f_surprised "You guys didn't talk for twelve years?!"

    maria @ f_laugh "Heh, he was a stubborn old bastard..."

    anon f_worried "No doubt."

    if game.timer.is_evening():
        show maria f_sad_down a_sides
    else:
        show maria f_sad_down a_spoon_sides
    with dissolve
    pause
    maria "It hurt goin' through that but I still had my ma..."

    maria "... And I had my friends..."

    pause
    if game.timer.is_evening():
        show maria a_hips
    else:
        show maria a_spoon_hips
    with dissolve
    maria f_shy "... And I had {b}Tony{/b}."

    show anon f_normal
    maria f_normal "So I don't regret nothin'."

    anon "That's beautiful."

    pause
    maria f_confused "Heh, I dunno why I'm tellin' you all this..."

    anon f_worried "Sorry, I shouldn't have asked."

    maria f_normal "Nah, it's alright."

    maria "You're just easy to open up to, I guess."

    show anon f_normal
    pause
    maria @ f_laugh "Aneh."

    jump maria_button_pizzeria.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
