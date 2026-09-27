label mias_bedroom_mia_tattoo_help:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Hei!"

    mia "I'm so happy you could make it."

    show old_mia 7
    show player 17
    player_name "Tidak apa-apa. Sepertinya ada sesuatu yang penting untuk dibicarakan."

    show player 14
    player_name "Anda ingin menanyakan sesuatu kepada saya?"

    show player 13
    show old_mia 10
    mia "Yah, itu tidak {i}itu{/i} penting..."

    mia "... Saya berharap bisa mendapatkan pendapat Anda tentang sesuatu, dan mungkin Anda bisa membantu saya."

    show old_mia 7
    show player 10
    player_name "Uhh... kurasa begitu. Tentang apa ini?"

    show player 11
    show old_mia 10
    mia "Tahukah Anda tentang tato?"

    show old_mia 7
    show player 10
    player_name "Tato?!"

    show player 12
    player_name "Mengapa? Apakah Anda berpikir untuk mendapatkannya?"

    show player 11
    show old_mia 12
    mia "Aku tahu itu buruk..."

    mia "... Tapi, aku bosan disuruh apa yang harus kulakukan!"

    mia "Saya hanya ingin melakukan sesuatu... Spontan dan bersenang-senang!"

    mia "Untuk merasa bebas..."

    show old_mia 8
    show player 10
    player_name "Apakah ibumu akan baik-baik saja dengan ini?"

    show player 5
    show old_mia 12
    mia "Saya tidak peduli lagi."

    show old_mia 8
    show player 11
    player_name "..."
    show player 14
    player_name "Tato itu cukup keren. Aku hanya tidak ingin kamu mendapat masalah."

    show player 13
    show old_mia 12
    mia "Apakah kamu akan membantuku?"

    show old_mia 8
    show player 14
    player_name "Tentu, tapi bagaimana caranya?"

    show player 13
    show old_mia 10
    mia "Saya tahu Anda suka menggambar sesuatu di kelas sepanjang waktu, dan saya telah melihat karya seni Anda..."

    mia "... Saya berharap Anda akan menggambar sesuatu untuk tato saya!"

    show old_mia 7
    show player 22
    player_name "!!!" with hpunch
    show player 29 at Position(xoffset=8)
    player_name "Apa kamu yakin?"

    show player 13 with dissolve
    show old_mia 10
    mia "Ya! Kamu sangat ahli dalam hal itu."

    show old_mia 7
    show player 21
    player_name "Terima kasih, tapi saya bahkan tidak tahu apa yang Anda inginkan!"

    show player 13
    show old_mia 10
    mia "Hmm... Aku ingin sesuatu yang lucu!"

    show old_mia 9
    mia "Dengan warna-warna cantik!"

    show old_mia 7
    show player 24
    player_name "Bagaimana jika itu buruk dan Anda akhirnya membencinya?"

    show player 13
    show old_mia 10
    mia "Saya yakin semuanya akan baik-baik saja!"

    show old_mia 7
    show player 14
    player_name "Jika kamu berkata begitu..."

    show player 13
    show old_mia 10
    mia "Datang menemui saya ketika Anda memiliki sesuatu."

    show old_mia 7
    show player 14
    player_name "Baiklah."

    show player 13
    show old_mia 10
    mia "Saya harus tidur. Sampai jumpa di sekolah!"

    show old_mia 7
    show player 36 with dissolve
    player_name "Selamat malam!"

    hide player
    hide old_mia
    with dissolve
    return

label mias_bedroom_mia_midnight_help:
    scene expression game.timer.image("mia_bedroom{}")
    player_name "{b}Mia{/b}'s not here... And I don't see any keys."

    return

label mia_study:
    $ game.timer.tick()
    call expression game.dialog_select("mia_study_intro")
    menu:
        mia "Do you... Also like me?"

        "Ya.":
            call expression game.dialog_select("mia_study_like_mia")
            menu:
                "Close your eyes.":
                    call expression game.dialog_select("mia_study_like_mia_kiss")
                    $ M_player.set("jerk mia", True)
                    $ M_mia.trigger(T_mia_kiss)
        "Tidak.":

            call expression game.dialog_select("mia_study_dislike_mia")
    $ player.go_to(L_miahouse)
    $ game.main()

label mia_study_intro:
    scene mia_bedroom_closeup
    show old_mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "So... I don't really know how to say this..."

    show old_mia 18
    show player 143
    mia "... And I'm so shy in front of people, especially boys..."

    mia "... But, I didn't really want to study."

    show player 145
    show old_mia 19
    player_name "Hah?"

    show old_mia 18
    show player 143
    mia "I couldn't come up with a better excuse to hang out..."

    mia "... And I kind of like you!"

    show player 145
    show old_mia 14
    player_name "Why didn't you just tell me before?"

    show old_mia 18
    show player 143
    mia "Well, I wanted to spend time together, but my mom would never allow it, so..."

    show old_mia 13
    show player 145
    player_name "It's okay. I understand!"

    show player 142
    player_name "It's nice of you to invite me. I like this..."

    show old_mia 16
    show player 141
    mia "Bagaimana denganmu?"

    show old_mia 13
    show player 145
    player_name "Hah?"

    show old_mia 18
    show player 143
    return

label mia_study_like_mia:
    show old_mia 19
    show player 145
    player_name "I do..."

    show old_mia 15
    show player 141
    mia "Really??"

    show old_mia 16
    show player 143
    mia "So... What do you like about me?"

    show old_mia 19
    show player 145
    player_name "I think you're really nice... You know..."

    player_name "... Like when you talk to me at school and stuff!"

    show old_mia 18
    show player 141
    mia "That's sweet!"

    show old_mia 19
    show player 142
    player_name "I also think that you're really pretty!"

    show player 141
    mia "..."
    show old_mia 18
    mia "Benar-benar?"

    return

label mia_study_like_mia_kiss:
    show player 142
    show old_mia 19
    player_name "Close your eyes..."

    show old_mia 18
    show player 141
    mia "Mengapa?"

    show old_mia 19
    show player 142
    player_name "... Just do it."

    show old_mia 17
    show player 147
    mia "Hmm..."

    show old_mia 18
    mia "..."
    show player 148
    show old_mia 20 at Position (xpos = 647, ypos = 574) with hpunch
    mia "!!!"
    show old_mia 18 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 143
    mia "... I can't do that... Yet!"

    show old_mia 14
    show player 146
    player_name "... Sorry, I thought-"

    show old_mia 22
    show player 144
    mia "No! It's fine! I'm sorry. I just can't, right now..."

    mia "... If my mom saw us, we'd be dead."

    show old_mia 14
    show player 146
    player_name "Oh, sorry..."

    show player 143
    show old_mia 18
    mia "It's alright..."

    mia "My dad probably wouldn't flip out as bad as my mom would..."

    mia "He's actually really cool when {b}Mom{/b} is not around."

    show old_mia 22
    mia "{b}Mom{/b}'s just... Very religious. I'd probably be locked away and forced to study the Bible."

    show old_mia 14
    show player 145
    player_name "Wow. Really?"

    show player 141
    show old_mia 18
    mia "She's all about sins and that stuff."

    show old_mia 22
    mia "She'd think you'd corrupt me and make me do naughty things..."

    show old_mia 14
    show player 143
    player_name "..."
    show player 145
    player_name "I... I wouldn't do that!"

    show player 143
    show old_mia 15
    mia "Haha, I know silly."

    show player 144
    show old_mia 16
    mia "Anyway, it's getting late and {b}Mom{/b} will be checking in on me."

    mia "So I should get to bed."

    show old_mia 13
    show player 142
    player_name "Alright, {b}Mia{/b}."

    player_name "I'll see you at {b}school{/b}!"

    scene expression game.timer.image("backgrounds/location_mia_bedroom{}.jpg")
    show old_mia 7 at right
    show player 21 at left
    with dissolve
    player_name "I'll see you later, then?"

    show old_mia 10
    show player 13
    mia "Ya..."

    mia "Thanks for coming."

    show old_mia 7
    show player 21
    player_name "Selamat malam!"

    return

label mia_study_dislike_mia:
    show old_mia 14
    show player 146
    player_name "I see you more like... A friend."

    show old_mia 22
    show player 144
    mia "Ohh... I see."

    show old_mia 14
    show player 145
    player_name "But, this is the first time we've ever hung out!"

    player_name "Give it some time. Maybe we can get to know each other better!"

    show old_mia 22
    show player 144
    mia "Ya baiklah..."

    scene expression game.timer.image("backgrounds/location_mia_bedroom{}.jpg")
    show old_mia 8 at right
    show player 21 at left
    with dissolve
    player_name "I'll see you later, then?"

    show player 13
    show old_mia 12
    mia "Ya..."

    mia "Thanks for coming."

    show old_mia 8
    show player 21
    player_name "Selamat malam!"

    return

label mia_strip_show:
    call expression game.dialog_select("mia_strip_show_dialogue")
    $ game.timer.tick()
    $ M_mia.trigger(T_mia_strip_tease)
    $ player.go_to(L_miahouse)
    $ game.main()

label mia_strip_show_dialogue:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "You're here!!"

    show old_mia 7
    show player 14
    player_name "Hey {b}Mia{/b}. Am I late?"

    show player 13
    show old_mia 10
    mia "Tidak, tidak apa-apa."

    show old_mia 12
    mia "But are you sure no one saw you come up here?"

    show old_mia 8
    show player 10
    player_name "Ehh... I'm pretty sure?"

    show player 12
    player_name "Is there something I should be worried about?"

    show player 11
    show old_mia 10
    mia "No, of course not. Just making sure no one will be disturbing us!"

    show old_mia 7
    show player 14
    player_name "Oke."

    player_name "So, what did you want to do?"

    show player 13
    show old_mia 9
    mia "I have a... Surprise for you."

    show old_mia 7
    show player 18
    player_name "..."
    show player 13
    show old_mia 10
    mia "I wanted to finally show you my tattoo..."

    mia "... But I want to make it special."

    show old_mia 7
    player_name "..."
    show old_mia 10
    mia "Sit on my bed..."

    scene black
    with fade
    hide player
    hide old_mia

    scene mia_bedroom_strip01
    show old_mia_strip 1 at Position (xpos=457,ypos=670)
    show player mia_strip 18 at right
    with fade
    pause
    show old_mia_strip 2
    mia "This is to thank you for being so nice to me..."

    show old_mia_strip 3 at Position (xoffset=39) with dissolve
    pause
    show old_mia_strip 4 at Position (xoffset=15) with dissolve
    pause
    show old_mia_strip 5 with dissolve
    player_name "..."
    show old_mia_strip 6
    mia "Do you think... I look pretty?"

    show old_mia_strip 5
    player_name "S-sure! I mean, of course!"

    show old_mia_strip 7
    mia "Haha, you're sweet..."

    show old_mia_strip 8 with dissolve
    pause
    show old_mia_strip 9 with dissolve
    pause
    show old_mia_strip 10 with dissolve
    pause
    show old_mia_strip 11 with dissolve
    pause
    show old_mia_strip 12 with dissolve
    pause
    player_name "!!!"
    show old_mia_strip 13 with dissolve
    pause
    show player mia_strip 19 with dissolve
    player_name "( WOW!!! )"

    show old_mia_strip 14 with dissolve
    pause
    show old_mia_strip 15
    mia "So? Do you like it?"

    show old_mia_strip 14
    player_name "I-I like what? Sorry?"

    show old_mia_strip 16
    show player mia_strip 20 with dissolve
    mia "My tattoo, silly! Do you like-"

    show old_mia_strip 17
    mia "!!!"
    mia "Oh, my... What's that in your pants?!"

    scene mia_bedroom_strip02
    pause
    scene mia_bedroom_strip03
    pause
    scene mia_bedroom_strip04
    helen "..."
    scene black
    with fade
    hide player
    hide helen
    hide old_mia

    scene location_mia_bedroom_closeup
    show helen 6f at Position (xpos=431)
    show player 22f at right
    show old_mia 37 at Position (xpos=674)
    with dissolve
    pause
    show old_mia 39
    mia "{b}MOM{/b}!!!"

    show old_mia 37
    show helen 5f
    helen "What's that on your leg?!"

    show helen 7f at Position (xpos=441) with dissolve
    helen "!!!"
    helen "What's this BOY doing HERE?!!"

    show helen 8f
    show old_mia 36
    mia "I can explain, {b}Mom{/b}!"

    show old_mia 35
    show helen 7f
    helen "I can't believe you're doing this to me..."

    helen "... After raising you to be a good daughter..."

    helen "... You choose to be an adulterer, a sinner, a SCAMP!!"

    show helen 8f
    show player 16f
    show old_mia 38
    mia "..."
    show player 12f
    player_name "This was my idea! {b}Mia{/b} didn't-"

    show player 22f
    show helen 7f
    helen "Who said you could speak?! OR BE HERE AT ALL! {i}IN MY HOUSE{/i}!!!"

    show helen 8f
    show old_mia 37
    show player 23f
    player_name "!!!" with hpunch
    show player 22f
    show helen 9f at left with fastdissolve
    helen "Get out of here, NOW!!"

    show old_mia 39
    mia "{b}Mom{/b}!!!"

    scene black
    with fade
    hide player
    hide old_mia
    hide helen

    scene expression L_miahouse.background_blur
    show player 24 with dissolve
    player_name "Wah!"

    show player 37 at Position (xoffset=41) with dissolve
    player_name "{b}Helen{/b} was really mad."

    show player 25 with dissolve
    player_name "I just hope {b}Mia{/b} is not in too much trouble..."

    hide player with dissolve
    return

label mia_bedroom_sex:
    call expression game.dialog_select("mia_bedroom_sex_intro")
    if not store._in_replay == None:
        call expression game.dialog_select("mia_bedroom_sex_study")
        call expression game.dialog_select("mia_bedroom_sex_sure")
        jump expression game.dialog_select("mia_strip_repeat")
    menu:
        "Belajar.":
            call expression game.dialog_select("mia_bedroom_sex_study")
            menu:
                "Mungkin nanti.":
                    call expression game.dialog_select("mia_bedroom_sex_maybe_later")
                "Tentu!":

                    call expression game.dialog_select("mia_bedroom_sex_sure")
                    label mia_strip_repeat:
                        call expression game.dialog_select("mia_bedroom_sex_strip_repeat")

                    if M_mia.get("cum 1st choice") == "":
                        call expression game.dialog_select("mia_bedroom_sex_first_intro")
                    else:

                        call expression game.dialog_select("mia_bedroom_sex_repeat_intro")
                    menu:
                        "Butt is fine.":
                            $ M_mia.set("anal sex", True)
                            call expression game.dialog_select("mia_bedroom_sex_butt_intro")

                            label mia_butt_start:
                                call expression game.dialog_select("mia_bedroom_sex_butt_start")

                            $ anim_toggle = True
                            $ animated = False
                            jump expression game.dialog_select("mia_bedroom_sex_loop")

                        "I like the other way." if store._in_replay == None and player.stats.chr() < 7:
                            $ display.toast(chr_fail)
                            $ M_mia.set("anal sex", True)
                            call expression game.dialog_select("mia_bedroom_sex_vaginal_stat_fail")
                            jump expression game.dialog_select("mia_butt_start")

                        "Just the tip!" if not store._in_replay == None or player.stats.chr() >= 7:
                            $ display.toast(chr_pass)
                            $ M_mia.set("anal sex", False)
                            if not M_mia.is_set("vaginal sex"):
                                $ M_mia.set("vaginal sex", True)
                                call expression game.dialog_select("mia_bedroom_sex_vaginal_first_intro")
                            else:

                                call expression game.dialog_select("mia_bedroom_sex_vaginal_repeat_intro")

                            call expression game.dialog_select("mia_bedroom_sex_vaginal_intro")
                            $ M_mia.set("sex speed", .125)
                            jump expression game.dialog_select("mia_bedroom_sex_loop")
    $ game.main()

label mia_bedroom_sex_intro:
    scene location_mia_bedroom_closeup
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Saya sangat senang Anda datang."

    show old_mia 7
    show player 14
    player_name "Hai, {b}Mia{/b}."

    player_name "Your parents are back watching TV together, huh?"

    show player 13
    show old_mia 10
    mia "Yeah. It feels nice that everything's back to normal again."

    mia "Jadi kamu ingin jalan-jalan?"

    mia "Atau apakah Anda di sini untuk mencoba teknik belajar baru saya?"

    show old_mia 7
    return

label mia_bedroom_sex_study:
    show player 14
    player_name "I guess we should be studying."

    show player 13
    show old_mia 10
    mia "Tentu saja!"

    mia "Let's do that then!"

    mia "Let me get all my textbooks and set up on my bed?"

    show old_mia 7
    show player 14
    player_name "Uh... Okay."

    hide player
    hide old_mia
    with dissolve

    scene mia_bedroom_closeup with fade
    show old_mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    show player 141 zorder 0 at Position (xpos = 250, ypos = 578)
    with dissolve
    mia "Now, at least it looks like we're studying!"

    show old_mia 13
    player_name "..."
    show old_mia 16
    mia "Sorry... I guess I'm just excited to hang out like we used to..."

    show old_mia 13
    show player 142
    player_name "Don't worry about that. I'm just glad you're happy again."

    show player 141
    show old_mia 16
    mia "Terima kasih, {b}[firstname]{/b}."

    show old_mia 15
    mia "Do you still think about the time I showed you my tattoo?"

    show old_mia 13
    show player 145
    player_name "Tentu saja!"

    player_name "You looked so pretty."

    show player 144
    show old_mia 15
    mia "Don't make me blush."

    show old_mia 17
    show player 141
    player_name "..."
    show player mia_bed_kiss 53
    show old_mia 52
    with dissolve
    mia "!!!"
    hide player
    show old_mia 54
    with dissolve
    pause
    mia "Hmm..."

    show player 144 zorder 0 at Position (xpos = 250, ypos = 578)
    show old_mia 16 zorder 1 at Position (xpos = 680, ypos = 574)
    with dissolve
    mia "You're really good at kissing..."

    show old_mia 13
    show player 145
    player_name "... Terima kasih."

    show player 144
    mia "..."
    show old_mia 16
    mia "Want to know about that study trick I read about?"

    show old_mia 13
    show player 142
    player_name "Tentu saja!"

    show player 141
    mia "..."
    show old_mia 16
    mia "I was hoping to try it the night my mom caught us."

    show old_mia 13
    show player 142
    player_name "Oh?"

    show player 141
    show old_mia 16
    mia "I... I've always wanted to try studying naked..."

    show old_mia 13
    show player 143
    player_name "!!!"
    show old_mia 16
    mia "Would you like to study with me... Naked?"

    show old_mia 13
    return

label mia_bedroom_sex_maybe_later:
    show player 146
    player_name "I mean... I'd really like to but I have to get back home."

    show player 141
    show old_mia 18
    mia "Oh? Does {b}[deb_name]{/b} give you a spanking if you're home late?"

    show old_mia 13
    show player 145
    player_name "Heh... Heh... No..."

    show player 141
    show old_mia 18
    mia "I'm just kidding. It is pretty late... And I'm getting tired too."

    hide old_mia
    hide player
    with dissolve

    scene location_mia_bedroom_closeup
    show old_mia 7 at right
    show player 14 at left
    with dissolve
    player_name "Selamat malam, {b}Mia{/b}."

    player_name "I'll see you tomorrow."

    show player 13
    show old_mia 10
    mia "Selamat malam, {b}[firstname]{/b}."

    hide player
    show old_mia 49 at left
    with dissolve
    pause
    show player 13 at left
    show old_mia 10 at Position (xpos=300)
    with dissolve
    mia "I'll be... Thinking of you tonight..."

    hide player
    hide old_mia
    with dissolve
    return

label mia_bedroom_sex_sure:
    show player 142
    player_name "I'd love to help you out!"

    show player 141
    show old_mia 16
    mia "Besar!"

    mia "Hmm..."

    show old_mia 16
    mia "How about you sit on the bed while I undress again."

    mia "My parents said they won't interrupt us again."

    mia "So just relax..."

    mia "... And enjoy the show."

    hide player
    hide old_mia
    with dissolve
    return

label mia_bedroom_sex_strip_repeat:
    scene mia_bedroom_strip01 with fade
    show player mia_strip 18 at right
    show old_mia_strip 1 at Position (xpos=457,ypos=670)
    pause
    show old_mia_strip 3 at Position (xoffset=39) with dissolve
    pause
    show old_mia_strip 4 at Position (xoffset=15) with dissolve
    pause
    show old_mia_strip 5 with dissolve
    pause
    show old_mia_strip 6
    mia "Do you think... I look pretty?"

    show old_mia_strip 5
    player_name "S-sure! I mean, of course!"

    show old_mia_strip 7
    mia "Haha, you're sweet."

    show old_mia_strip 8 with dissolve
    pause
    show old_mia_strip 9 with dissolve
    pause
    show old_mia_strip 10 with dissolve
    pause
    show old_mia_strip 11 with dissolve
    pause
    show old_mia_strip 12 with dissolve
    pause
    player_name "!!!"
    hide player
    show player mia_strip 18 at right
    show old_mia_strip 13
    with dissolve
    pause
    show player mia_strip 19 with dissolve
    player_name "( WOW!!! )"

    hide old_mia_strip
    show old_mia_strip 14 at Position (xpos=457,ypos=670)
    with dissolve
    pause
    show old_mia_strip 17
    mia "!!!"
    show old_mia_strip 16
    mia "I guess you really do think I look pretty."

    show old_mia_strip 15
    mia "Does my tattoo still look good?"

    show old_mia_strip 14
    player_name "It looks really pretty on you."

    show old_mia_strip 15
    mia "Oh ya?"

    mia "... What about my butt?"

    show old_mia_strip 14
    player_name "{i}*Meneguk*{/i}"

    player_name "Uhhh... Yeah... I mean... Of course!"

    player_name "You're an all around sexy girl!"

    show old_mia_strip 16
    mia "Ha ha ha."

    show old_mia_strip 15
    mia "Don't tell me you're... Nervous, {b}[firstname]{/b}."

    player_name "Mungkin sedikit..."

    show old_mia_strip 22 with dissolve
    mia "Me too..."

    show old_mia_strip 21
    show player mia_strip 20 with dissolve
    pause
    show old_mia_strip 22
    mia "Let me get my homework."

    show old_mia_strip 23 with dissolve
    pause
    show old_mia_strip 26 with dissolve
    mia "Ini dia!"

    show old_mia_strip 25
    mia "Apakah kamu siap?"

    show old_mia_strip 24
    player_name "Ya!"

    show old_mia_strip 25
    mia "Wah..."

    mia "I had no idea they got that big..."

    show old_mia_strip 24
    player_name "Oh... Yeah..."

    show old_mia_strip 25
    mia "Ummm... Okay, let me lay down on the bed..."

    mia "... And you join me..."

    show old_mia_strip 27 with dissolve
    pause
    scene black with fade
    hide player
    hide old_mia
    pause
    scene mia_bed_sex with fade
    return

label mia_bedroom_sex_first_intro:
    show mias 2 with dissolve
    mia "Silly boy. How are you going to study way back there?"

    show mias 1
    player_name "Oh... I can see everything back here."

    player_name "Aku baik-baik saja."

    show mias 2
    mia "I bet you are."

    mia "..."
    show mias 5
    mia "Um..."

    mia "{b}[firstname]{/b}?"

    show mias 1
    player_name "Yes, {b}Mia{/b}?"

    show mias 5
    mia "..."
    mia "Do you want to have sex?"

    show mias 1
    player_name "!!!"
    show mias 2
    mia "Whenever I've thought about studying naked..."

    mia "... I've kinda ended up fantasizing that I ended up having... Sex."

    show mias 5
    mia "It's my little secret fantasy..."

    show mias 2
    mia "Do you want to try it?"

    show mias 1
    player_name "Ya!"

    show mias 2
    mia "I figured you would..."

    show mias 5
    mia "But... Umm..."

    mia "I have one request."

    mia "Can you do it..."

    mia "In my butt?"

    show mias 2
    mia "My parents say I should wait 'til I get married to actually do it."

    mia "But I figure it won't hurt to do it in my butt."

    mia "Is that alright?"

    show mias 5
    mia "If you're disgusted... I understand..."

    show mias 1
    return

label mia_bedroom_sex_repeat_intro:
    show mias 2
    mia "I thought you wanted to study naked this time?"

    show mias 1
    player_name "I'm studying... You."

    show mias 2
    mia "It's going to be hard to study if you aren't relaxed."

    mia "Haha!"

    mia "Want to do it in my butt?"

    show mias 1
    return

label mia_bedroom_sex_butt_intro:
    player_name "I don't think it's disgusting."

    player_name "It's kinda of rare to hear a girl want to do it there."

    show mias 2
    mia "Haha."

    mia "I'm a rare kinda girl."

    return

label mia_bedroom_sex_butt_start:
    show mias 4
    mia "Just... Go slowly so it won't hurt."

    mia "I didn't think you'd be so... Big."

    show mias 3
    pause
    show mias 5
    player_name "Alright, here's just the tip..."

    show mias 6b
    mia "Ouch!"

    player_name "Maaf!"

    mia "Don't move... Please..."

    player_name "Alright. Tell me when I can go deeper."

    mia "..."
    mia "Okay... Go slow."

    show mias 7b
    pause
    show mias 8b
    pause
    show mias 9b
    mia "..."
    player_name "There I'm all the way in."

    player_name "Santai aja."

    mia "Ini sangat besar!"

    player_name "Yeah... It's pretty tight."

    mia "Alright. Just go slow."

    show mias 10b
    pause
    show mias 11b
    mia "It's not... Too bad..."

    player_name "Ready?"

    mia "Eh ya."

    return

label mia_bedroom_sex_vaginal_stat_fail:
    show mias 1
    player_name "But the other way is so much better {b}Mia{/b}."

    player_name "... It's not like anyone would know we did it."

    show mias 4
    mia "I would know, though."

    show mias 3
    player_name "Well... It would feel a lot bette-"

    show mias 5
    mia "No, if you want to do it with me, use my butt."

    player_name "... Baiklah."

    return

label mia_bedroom_sex_vaginal_first_intro:
    player_name "I promise I won't go all the way in."

    show mias 2
    mia "Just the tip? ... Are you sure?"

    show mias 1
    player_name "It doesn't even count if it's just the tip..."

    show mias 2
    mia "Haha!"

    mia "It might be okay, then..."

    mia "But just go slowly... It's my first time..."

    show mias 6
    mia "Oh!"

    mia "Even the tip of you is so big!"

    show mias 7
    mia "How... Does it feel?"

    player_name "Sangat bagus."

    mia "..."
    mia "... Go in a little deeper..."

    player_name "Apa?"

    mia "Can you go in a little deeper?"

    player_name "... Baiklah."

    show mias 8
    pause
    show mias 7
    pause
    show mias 8
    player_name "It's going in and out easier now."

    show mias 7_8
    pause
    mia "Oh..."

    pause
    mia "Ohhhh..."

    mia "Deeper {b}[firstname]{/b}."

    return

label mia_bedroom_sex_vaginal_repeat_intro:
    show mias 2
    mia "Your tip sure goes in pretty far."

    show mias 1
    player_name "... Ya..."

    player_name "Maaf."

    show mias 2
    mia "Don't worry. I liked it."

    mia "And I want your tip again."

    show mias 6
    mia "Oh!"

    show mias 7_8
    pause
    mia "How... Does it feel?"

    player_name "Sangat bagus."

    mia "... Go in all the way..."

    return

label mia_bedroom_sex_vaginal_intro:
    show mias 9
    mia "Ohhh!!!"

    show expression AnimatedImage("mias", [7,8,9,10,11], M_mia) as mias
    pause
    mia "Ahhh!!!"

    mia "Rasanya luar biasa!"

    pause
    mia "Faster, {b}[firstname]{/b}!"

    return

label mia_bedroom_sex_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                if M_mia.is_set("anal sex"):
                    show expression AnimatedImage("mias", ["7b","8b","9b","10b","11b"], M_mia) as mias
                else:
                    show expression AnimatedImage("mias", [7,8,9,10,11], M_mia) as mias
                $ animated = True
            pause 6
            if animcounter in [2]:
                call expression game.dialog_select("mia_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                if M_mia.is_set("anal sex"):
                    show expression "mias {}b".format(pose_list[pose_counter]) as mias
                else:
                    show expression "mias {}".format(pose_list[pose_counter]) as mias
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [2]:
                call expression game.dialog_select("mia_hscene_dialog")
        $ animcounter += 1

    player_name "Where do you want me to cum, {b}Mia{/b}?"

    mia "... Anywhere."

    call screen mia_bedroom_sex_options

label mia_hscene_dialog:
    mia "Ahhhh!!!{p=1}{nw}"

    return

label mia_bedroom_sex_cum_outside:
    call expression game.dialog_select("mia_bedroom_sex_cum_outside_intro")
    if M_mia.get("cum 1st choice") == "":
        $ M_mia.set("cum 1st choice", "Outside")
        call expression game.dialog_select("mia_bedroom_sex_cum_outside_first")
    else:

        call expression game.dialog_select("mia_bedroom_sex_cum_outside_repeat")
        if M_mia.is_set("cum 1st choice") == "Inside":
            call expression game.dialog_select("mia_bedroom_sex_cum_outside_first_inside")

    call expression game.dialog_select("mia_bedroom_sex_cum_outside_after")
    jump expression game.dialog_select("mia_bedroom_sex_end")

label mia_bedroom_sex_cum_outside_intro:
    show mias 14 with flash
    player_name "UHH!!!"

    mia "Oh!!!"

    pause
    return

label mia_bedroom_sex_cum_outside_first:
    show mias 16
    mia "So much came out of it."

    show mias 15
    player_name "Ya."

    show mias 16
    mia "I can feel it running down my back."

    show mias 15
    player_name "Maaf."

    show mias 16
    mia "Can you get me tissues?"

    mia "I don't want it to leak on the sheets..."

    return

label mia_bedroom_sex_cum_outside_repeat:
    show mias 16
    mia "Itu bagus sekali!"

    mia "You sure cum pretty fast!"

    show mias 15
    player_name "Maaf..."

    show mias 16
    mia "Saya hanya bercanda."

    return

label mia_bedroom_sex_cum_outside_first_inside:
    mia "It is easier to clean up when you just cum inside me though."

    return

label mia_bedroom_sex_cum_outside_after:
    mia "I'd better get cleaned up."

    mia "My mom might see stains on the bed sheets..."

    show mias 15
    player_name "Maaf..."

    show mias 16
    mia "Oh don't worry."

    mia "That was great, {b}[firstname]{/b}."

    show mias 15
    player_name "Ya, benar."

    return

label mia_bedroom_sex_cum_inside:
    if M_mia.get("cum 1st choice") == "":
        $ M_mia.set("cum 1st choice", "Inside")

    if M_mia.is_set("anal sex"):
        call expression game.dialog_select("mia_bedroom_sex_cum_inside_anal_intro")
        if M_mia.get("sex 1st choice") == "":
            $ M_mia.set("sex 1st choice", "Anal")
            call expression game.dialog_select("mia_bedroom_sex_cum_inside_anal_first")
        call expression game.dialog_select("mia_bedroom_sex_cum_inside_anal_after")
    else:

        call expression game.dialog_select("mia_bedroom_sex_cum_inside_vaginal_intro")
        if M_mia.get("sex 1st choice") == "":
            $ M_mia.set("sex 1st choice", "Vaginal")
            call expression game.dialog_select("mia_bedroom_sex_cum_inside_vaginal_first")
        else:

            call expression game.dialog_select("mia_bedroom_sex_cum_inside_vaginal_repeat")
    jump expression game.dialog_select("mia_bedroom_sex_end")

label mia_bedroom_sex_cum_inside_anal_intro:
    show mias 12b_13b with flash
    player_name "UHH!!!"

    mia "OHH!!!"

    show mias 18b with dissolve
    mia "Wah!"

    return

label mia_bedroom_sex_cum_inside_anal_first:
    mia "So, that's what anal sex feels like..."

    show mias 17b
    player_name "Did it hurt a lot?"

    show mias 18b
    mia "It wasn't so bad."

    return

label mia_bedroom_sex_cum_inside_anal_after:
    mia "Apakah kamu menyukainya?"

    show mias 17b
    player_name "Ya!"

    player_name "It was really... Tight."

    show mias 18b
    mia "Thanks for going slow."

    show mias 17b
    player_name "You're welcome, {b}Mia{/b}."

    show mias 18b
    mia "I'd better get cleaned up."

    mia "My mom might see stains on the bed sheets..."

    show mias 17b
    player_name "Maaf..."

    show mias 18b
    mia "Oh don't worry."

    mia "That was great, {b}[firstname]{/b}."

    show mias 17b
    player_name "Ya, benar."

    return

label mia_bedroom_sex_cum_inside_vaginal_intro:
    show mias 12_13 with flash
    player_name "UHH!!!"

    mia "OHH!!!"

    return

label mia_bedroom_sex_cum_inside_vaginal_first:
    show mias 18 with dissolve
    mia "Itu luar biasa!"

    mia "I've never felt anything like that before."

    show mias 17
    player_name "!!!"
    player_name "You mean you've never... Climaxed?"

    show mias 18
    mia "No, I've had orgasms before..."

    mia "... I meant... Like, feeling you cumming in me and stuff."

    show mias 17
    player_name "Oh..."

    show mias 18
    mia "Don't feel bad. I wanted you to."

    return

label mia_bedroom_sex_cum_inside_vaginal_repeat:
    show mias 18
    mia "That felt fantastic!"

    mia "I still can't believe that's what an orgasm feels like."

    mia "It gives me the shivers thinking about it."

    show mias 17
    player_name "Really? I... Really liked it too."

    show mias 18
    mia "I'd better get cleaned up."

    mia "My mom might see stains on the bed sheets..."

    show mias 17
    player_name "Maaf..."

    show mias 18
    mia "Oh don't worry."

    mia "That was great, {b}[firstname]{/b}."

    show mias 17
    player_name "Ya, benar."

    return

label mia_bedroom_sex_end:
    if M_mia.is_set("anal sex") and M_mia.get("butt speed") < 2:
        $ M_mia.set("butt speed", M_mia.get("butt speed") + 1)
    call expression game.dialog_select("mia_bedroom_sex_end_dialogue")
    $ persistent.cookie_jar["Mia"]["unlocked"] = True
    $ persistent.cookie_jar["Mia"]["gallery"]["03_unlocked"] = True
    $ game.timer.tick()
    if game.timer.is_night():
        $ player.go_to(L_miahouse)
    $ M_mia.trigger(T_mia_sex)
    $ game.main()

label mia_bedroom_sex_end_dialogue:
    hide mias
    scene black
    with fade
    pause
    scene location_mia_bedroom_closeup with fade
    show player 13 at left
    show old_mia 10 at right
    with dissolve
    mia "Thanks for helping me study, and spending time with me."

    show old_mia 9
    mia "It was a little hard to concentrate on studying, though."

    show player 17
    player_name "Hah hah!"

    show old_mia 7
    show player 14
    player_name "Yeah, I liked studying with you too."

    show player 17
    player_name "It's the kind of studying I can definitely get behind."

    show player 18
    show old_mia 9
    mia "Haha!"

    show old_mia 7
    pause
    show player 10
    player_name "... Does it hurt?"

    show player 5
    show old_mia 10
    mia "A little... Heh heh."

    mia "But I enjoyed it a lot."

    show old_mia 7
    show player 14
    player_name "Saya juga."

    player_name "I should get going. It's getting late."

    hide player
    show old_mia 49 at left
    with dissolve
    pause
    show player 13 at left
    show old_mia 10 at Position (xpos=300)
    with dissolve
    mia "Selamat malam, {b}[firstname]{/b}."

    mia "Come back and visit me again... If you want to study."

    show old_mia 7
    show player 14
    player_name "Akan berhasil!"

    player_name "Selamat malam, {b}Mia{/b}."

    hide player
    hide old_mia
    with dissolve
    $ renpy.end_replay()
    return

label mia_bedroom_teddy:
    if M_mia.is_set("telescope teddy seen"):
        call expression game.dialog_select("mia_bedroom_teddy_masturbation_seen")
    else:

        call expression game.dialog_select("mia_bedroom_teddy_masturbation_havent_seen")
    $ game.main()

label mia_bedroom_teddy_masturbation_seen:
    scene expression game.timer.image("backgrounds/location_mia_bedroom{}_blur.jpg")
    show player 439 with dissolve
    player_name "This is the teddy bear {b}Mia{/b} was playing with earlier."

    player_name "Seems to have a bit of an odd funk to it..."

    show player 441
    player_name "Something smells kind of..."

    show player 440 with dissolve
    player_name "{i}*Mengendus*{/i}"

    pause
    show player 441 with dissolve
    player_name "Fishy..."

    player_name "Mr. Teddy, you've seen some terrible things, haven't you?"

    player_name "I wonder why she likes him so much?"

    show player 438
    pause
    show player 439
    player_name "Looks like there's a hole in the back..."

    player_name "Huh. He has a little pouch."

    player_name "Looks like you could hide something in there."

    hide player with dissolve
    return

label mia_bedroom_teddy_masturbation_havent_seen:
    scene expression game.timer.image("backgrounds/location_mia_bedroom{}_blur.jpg")
    show player 438 with dissolve
    pause
    show player 439
    player_name "This teddy bear has been in her room since we were kids."

    player_name "I wonder why she still keeps it around..."

    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
