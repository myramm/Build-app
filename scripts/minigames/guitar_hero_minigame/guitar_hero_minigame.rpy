label guitar_hero_minigame_karaoke_fail:
    scene expression player.location.background_blur
    show old_erik 3f at Position (xpos=400)
    show player 5 at left
    show eve f_happy a_bottle with dissolve
    eve "Boo! You guys suck!"

    eve "Ha ha ha!"

    show player 10
    player_name "I didn't know the words to that song!"

    show player 12
    player_name "{b}Erik{/b}, pick another!"

    show player 5
    show old_erik 3bf
    erik "Baiklah..."

    show old_erik 3f
    show player 14
    player_name "Ini dia!"

    hide player
    hide old_erik
    with dissolve
    if M_dewitt.get("failcount") >= 3 or game.cheat_mode:
        menu:
            "Play minigame.":
                call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
            "Skip minigame. (Cheat)":
                jump guitar_hero_minigame_karaoke_pass
    else:
        call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")

label guitar_hero_minigame_karaoke_pass:
    if _in_replay:
        $ player.go_to(L_erikhouse_basement)
    $ M_dewitt.set("failcount", 0)
    $ persistent.cookie_jar["Eve"]["unlocked"] = True
    $ persistent.cookie_jar["Eve"]["gallery"]["01_unlocked"] = True
    scene expression player.location.background_blur
    show old_erik 1f at Position (xpos=400)
    show player 13 at left
    show eve f_sexy a_point
    with dissolve
    eve "I'll show you amateurs how it's done!"

    eve b_topless a_remove @ b_dressed a_up "Out of my way, boys!"

    show old_erik 5f
    show player 11
    pause
    hide eve with dissolve

    scene erik_basement_cs2
    show text _ ("I guess the booze did its job because {b}Eve{/b} rocked that mic with some serious confidence!\nShe was amazing! I was completely blown away by how beautiful her voice was!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Perhaps I should have stopped her at three glasses though...\n... As it ended up being quite the show!") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show old_erik 57f at Position (xpos=400)
    show player 83c at left
    show eve f_laugh b_topless a_surprised
    with fade
    eve "WHOOOOO!!!"

    show eve f_sexy a_idle with dissolve
    show player 83b
    player_name "Damn girl, you rock!"

    show player 83c
    eve "Thanks! I guess- {i}*Hic*{/i} I guess it isn't that bad singing in front of others."

    show player 83b
    player_name "Does that mean you'll sing in the talent show?!"

    show player 83c
    eve f_sad_thinking "..."
    eve f_sexy @ f_laugh "Sure, why not!"

    show player 83b
    player_name "You're awesome!"

    player_name "Maybe keep your clothes on for the talent show though."

    show player 83c
    eve f_nervous_down a_surprised "Hmm?"

    eve f_laugh "Oh! Pfft!"

    eve "Hahahahaha!"

    eve f_sexy "Whoopsie. Guess I- {i}*Hic*{/i} Guess I got carried away..."

    show old_erik 58f
    show eve a_remove with dissolve
    erik "Heh, it's okay. We don't mind."

    show old_erik 57f
    eve b_dressed a_idle f_surprised "Oh right, {i}*Hic*{/i} {b}Erik{/b}'s here..."

    eve f_sexy @ f_laugh "I completely forgot, hehehe."

    erik "..."
    show player 79 with dissolve
    player_name "I should probably help you get home."

    show player 83c
    with dissolve
    eve @ f_laugh "Aww, such a- {i}*Hic*{/i} such a gentleman!"

    eve "I'll just text my sis- {i}*Hic*{/i} She'll pick me up."

    show eve a_rossed with dissolve
    show old_erik 58f
    erik "I'll see you guys later."

    show old_erik 57f
    show player 83b
    player_name "Thanks for the party {b}Erik{/b}."

    show player 83c
    eve a_sides @ f_laugh a_wtf "Yeah, party! Whooooo!"

    show player 83b
    player_name "Heh, c'mon drunkie. Let's go home!"

    show player 83c
    eve "I was really good wasn't- {i}*Hic*{/i} wasn't I, {b}[firstname]{/b}?"

    show player 83b
    player_name "You sure were."

    show player 83c
    eve @ f_laugh "Hehehe."

    hide eve
    hide player
    hide old_erik
    with dissolve
    $ renpy.end_replay()
    $ game.timer.tick()
    if M_dewitt.is_set("talent ask kevin"):
        $ M_dewitt.trigger(T_dewitt_find_last_talent)
    else:
        $ M_dewitt.trigger(T_dewitt_karaoke_jam)
    $ game.main()

label guitar_hero_minigame_talent_show_fail:
    scene assembly_hall_cs03
    show text _ ("It was not a good start and the crowd was growing restless...\n{b}Eve{/b} and {b}Kevin{/b} looked worried but I knew we could still save it!\nI gave them both a reassuring nod and started it over from the top.\nWe'll win them over this time for sure!") as caption
    with fade
    pause

    if M_dewitt.get("failcount") >= 3 or game.cheat_mode:
        scene black with dissolve
        menu:
            "Play minigame.":
                call screen guitar_hero(0, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")
            "Skip minigame. (Cheat)":
                jump guitar_hero_minigame_talent_show_pass
    else:
        call screen guitar_hero(1, "guitar_hero_minigame_talent_show_pass", "guitar_hero_minigame_talent_show_fail")
    return

label guitar_hero_minigame_talent_show_pass:
    if M_dewitt.get("failcount") == 0:
        $ A_smooth_mcgroove.unlock()
    $ M_dewitt.set("failcount", 0)
    $ persistent.cookie_jar["Dewitt"]["gallery"]["02_unlocked"] = True

    scene assembly_hall_cs02
    show text _ ("The crowd was transfixed as we played our hearts out!\n{b}Kevin{/b} shredded on his guitar and {b}Eve{/b}'s angelic voice lulled them into submission!\n... I finished it all off with a whimsical flute solo that left the crowd reeling!") as caption
    with fade
    pause

    scene assembly_hall_paint02_c
    show old_kevin 17f at Position (xpos=600)
    show player 554 at left
    show eve b_music a_music_sides f_happy
    with fade
    eve "Awesome job guys!"

    show player 555
    player_name "Yeah, that was really amazing!"

    show player 554
    show old_kevin 18f
    kevin "Where the heck is {b}Miss Dewitt{/b}?!"

    show old_kevin 17f
    show player 553
    player_name "... Hah?"

    show player 552
    show old_kevin 18f
    kevin "Bro, she's gone!"

    show old_kevin 17f
    eve "He's right! She was right here a second ago..."

    show player 553
    player_name "She's supposed to close out the show with a speech."

    show player 552
    player_name "..."
    show old_kevin 18f
    kevin "Well, somebody has to go up and say something!"

    show old_kevin 17f
    eve "{b}[firstname]{/b} should do it!"

    show player 553
    player_name "... Why do I always have to do everything?!"

    show player 552
    show old_kevin 18f
    kevin "You got this, bro!"

    show old_kevin 17f
    show player 553
    player_name "{i}*Huh*{/i} Baik."

    show player 551c with dissolve
    player_name "( Think I'll put my hair back down. )"

    show player 551b at Position (xoffset=6) with dissolve
    eve "Aww... I liked your hair like that though!"

    show player 551d with dissolve
    pause
    show player 14 at Position (xoffset=52) with dissolve
    player_name "Sorry! Maybe you can fix my hair another time."

    show player 13 at Position (xoffset=52)
    eve "Alright! Now get out there!"

    hide player with dissolve

    scene assembly_hall_cs04
    show text _ ("The crowd was waiting with bated breath as I made my way to the podium.\nI had no idea what to say to these people!\nWhere the heck had {b}Miss Dewitt{/b} gotten off to?") as caption
    with fade
    pause

    scene assembly_hall_podium_c
    show player podium 3 at Position (xoffset=-120)
    show xtra 44
    with fade
    player_name "H-hey, so uh..."

    player_name "That was really something, huh?"

    show player podium 4 at Position (xoffset=-120)
    player_name "We just want to say we appreci-"

    show player podium 2 zorder 1 with dissolve
    player_name "!!!"
    player_name "Apa yang-"


    scene under_podium
    show dewitt under 1
    with dissolve
    dewitt "Well, hello there, sugar."

    show dewitt under 2
    player_name "What are you doi-"

    show dewitt under 3 with dissolve
    dewitt "Shhhh..."

    show dewitt under 1 with dissolve
    dewitt "I know what you did."

    dewitt "How you risked expulsion to make sure this talent show went off without a hitch."

    show dewitt under 2
    player_name "It's no big deal, ma'am."

    player_name "You should really come up here and close out the show!"

    show dewitt under 1
    dewitt "Nu uh! Not until I've had a chance to properly thank you, sugar!"

    show dewitt under 4 with dissolve
    player_name "Apa yang kamu-"

    $ M_dewitt.set("sex speed", 0.175)
    scene dewitt_podium_bj
    show dewitt bj 1 at left
    with dissolve
    player_name "!!!"
    show dewitt bj 2
    pause
    show dewitt bj 3
    dewitt "Keep talking, {b}[firstname]{/b}!"

    dewitt "Your adoring crowd is waiting!"


    scene assembly_hall_podium_c
    show player podium 2
    show xtra 44
    with dissolve
    player_name "{i}*Ahem*{/i} Sorry... Where was I?"

    player_name "..."
    player_name "Oh benar!"


    $ M_dewitt.set("sex speed", 0.175)
    scene dewitt_podium_bj
    show dewitt bj 4
    with dissolve
    player_name "We just wanted to say that we appre-"

    hide dewitt
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    with dissolve
    player_name "Sialan!"

    show screen dewitt_bj_options
    player_name "... Oh, wow!"

    player_name "W-we really appreciate..."

    player_name "... You all coming out to..."

    player_name "Oh man!!"

    player_name "... Coming out to support us!"

    player_name "Let's hear it one more time for-"

    player_name "Mmmm!"

    player_name "{b}Kevin{/b} on guitar!"


    player_name "{b}Eve{/b} on vocals!"

    player_name "... And I'm-"

    player_name "Oh, Jesus!"

    player_name "Haaah!"

    player_name "I'm {b}[firstname]{/b}!"

    dewitt "MM."

    player_name "..."
    player_name "Also, a special thanks to-"

    player_name "Fuuuuuu..."

    player_name "... {b}MC Tyrone{/b}!"

    player_name "... And of course, {b}Miss Dewitt{/b}!"

    player_name "Who-"

    player_name "Haaah!"

    player_name "Ya Tuhan!"

    player_name "{b}Miss Dewitt{/b}, who never fails..."

    player_name "... To suck every..."

    player_name "... Last... Drop..."

    dewitt "{i}*Menyeruput*{/i}"

    player_name "... Of talent..."

    player_name "... Out of her students!"

    player_name "I'm gonna..."

    player_name "I'M GONNA!!!"

    hide screen dewitt_bj_options

    scene assembly_hall_podium_c
    show player podium 1
    show xtra 44
    with dissolve
    player_name "HNNGGG!!!"

    player_name "Ooohhh, take it all!"

    player_name "Yeeaaaahhh..."


    $ M_dewitt.set("sex speed", 0.075)
    scene dewitt_podium_bj
    show expression AnimatedImage("dewitts_bj", [1,2,3,4,5,6,7,8,9,10,11,12], M_dewitt) as dewitts_bj
    with dissolve
    pause
    pause
    hide dewitts_bj
    show dewitt bj 5 at left
    with flash
    pause
    show dewitt bj 6
    pause
    show dewitt bj 7
    pause
    dewitt "Hmm, enak!"

    dewitt "Thanks again, sugar!"

    dewitt "Muah!"


    scene assembly_hall_podium_c
    show player podium 2
    show xtra 44
    with dissolve
    player_name "Fiuh..."

    show player podium 3 zorder 0 at Position (xoffset=-120) with dissolve
    player_name "Sorry, I meant to say."

    player_name "I'm gonna call it all to the close now."

    show player podium 4 at Position (xoffset=-120)
    player_name "Thanks again for coming out!"

    player_name "... And be sure to sign up for next year's show!"

    player_name "We love you Summerville!"

    player_name "Goodnight!"

    show player podium 5 at Position (xoffset=-56) with dissolve
    pause

    scene assembly_hall_cs07
    show text _ ("As I finished my speech, I spotted a very peculiar pair entering the auditorium.\nIt seems {b}Mrs. Smith{/b} and {b}Annie{/b} had managed to get themselves free after all.\nJudging by the state of them, it hadn't been easy!\nThey didn't stay long... Turning to leave the instant they realized they'd been beaten.") as caption
    with fade
    pause

    scene assembly_hall_paint02_c
    show old_kevin 17f at Position (xpos=600)
    show player 13 at left
    show eve b_music a_music_sides f_laugh:
        xoffset -350
    with fade
    eve "Hahahaha!! Did you see that cushion stuck to {b}Annie{/b}?!"

    eve f_happy "That might be the funniest thing I've ever seen in my life!"

    show old_kevin 18f
    kevin "Yeah, and {b}Mrs. Smith{/b}'s clothes were in tatters!"

    kevin "They really wanted to stop this show, huh?"

    show old_kevin 17f
    show player 14
    player_name "Heh, yeah. I can't believe they managed to get loose on their own!"

    show player 13
    show dewitt 9bf at right
    show dewitt 9bf at Position (xoffset=-73)
    with dissolve
    $ renpy.end_replay()
    dewitt "Oh my goodness, you guys were so great!"

    show eve:
        flip
        xoffset 250
    show old_kevin 17 at Position (xpos=700)
    with dissolve
    show dewitt 3bf at Position (xoffset=-73)
    dewitt "I've never been more proud!"

    show dewitt 1bf at Position (xoffset=-73)
    eve "Thanks, ma'am!"

    show old_kevin 18
    kevin "... Where did you get off to?"

    show old_kevin 17
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "Oh, I was just tending to a little something."

    show dewitt 1bf at Position (xoffset=-73)
    show old_kevin 18
    kevin "A little something?"

    show old_kevin 17
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "... Hmm, well. A big something actually!"

    show dewitt 1bf at Position (xoffset=-73)
    player_name "..."
    show dewitt 19f with dissolve
    dewitt "Great speech by the way, {b}[firstname]{/b}."

    dewitt "You have quite a talent..."

    dewitt "... For public speaking."

    show dewitt 18f
    eve "Hey, you guys wanna celebrate?! ... Grab a bite to eat or something?"

    show old_kevin 18
    kevin "I'm down!"

    show old_kevin 17
    show dewitt 19f
    dewitt "Oh, no thanks, sweetie. I'm afraid I'm full..."

    show dewitt 18f with None
    show eve:
        unflip
        xoffset -400
    with dissolve
    eve "{b}[firstname]{/b}?"

    show player 14
    player_name "I'm going to have to pass too. I'm pretty tired."

    show player 13
    eve "Awww! Come on!"

    show dewitt 19f
    dewitt "Actually would you mind giving {b}[firstname]{/b} and I a moment alone real quick?"

    show dewitt 18f with None
    show eve:
        flip
        xoffset 250
    with dissolve
    show old_kevin 18
    kevin "Hey, if you change your mind, shoot us a text."

    show old_kevin 17
    show player 14
    player_name "Alright. Later!"

    show player 13
    hide old_kevin
    hide eve
    with dissolve
    show dewitt 9bf at Position (xoffset=-73) with dissolve
    dewitt "I just wanted to thank you one more time for everything, {b}[firstname]{/b}."

    show dewitt 9df at Position (xoffset=-73)
    dewitt "This talent show never would have happened without your help."

    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "It was my pleasure, {b}Miss Dewitt{/b}."

    show player 13
    show dewitt 9bf at Position (xoffset=-73)
    dewitt "I've decided to give you an A+ in my class."

    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "Benar-benar?!"

    show player 13
    show dewitt 3bf at Position (xoffset=-73)
    dewitt "That's right, sugar."

    show dewitt 1bf at Position (xoffset=-73)
    show player 14
    player_name "Oh, thank you!"

    show player 13
    show dewitt 19f with dissolve
    dewitt "... And I have one more surprise for you."

    show dewitt 18f
    show player 10
    player_name "Hmm?"

    hide player
    show dewitt 6f at left
    with dissolve
    dewitt "Anda harus datang ke kantor saya {b}besok{/b} sepulang sekolah jika Anda menginginkannya..."

    show player 29 at left
    show dewitt 18f at Position (xpos=300)
    with dissolve
    player_name "O-oke..."

    player_name "Saya akan berada di sana."

    show player 13 with dissolve
    show dewitt 19f
    dewitt "Hmm, aku tidak sabar!"

    dewitt "Sampai jumpa, {b}[firstname]{/b}."

    hide dewitt with dissolve
    show player 18
    player_name "..."
    hide player with dissolve
    $ renpy.end_replay()

    $ game.timer.tick()
    $ M_dewitt.trigger(T_dewitt_talent_show_success)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
