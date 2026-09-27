label eriks_basement_dialogue:
    if M_dewitt.is_state(S_dewitt_eve_karaoke) and game.timer.is_dark():
        call expression game.dialog_select("eriks_basement_dewitt_eve_karaoke")
        if game.cheat_mode:
            menu:
                "Play minigame.":
                    call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")
                "Skip minigame. (Cheat)":
                    jump guitar_hero_minigame_karaoke_pass
        else:
            call screen guitar_hero(1, "guitar_hero_minigame_karaoke_pass", "guitar_hero_minigame_karaoke_fail")

    elif player.location.is_here(M_erik):
        if M_erik.is_state(S_erik_cards_ready):
            call eriks_basement_first_time
            $ M_erik.trigger(T_erik_cards_lost)

        if M_erik.is_state(S_erik_orc_ready):
            call eriks_basement_orcette
            $ M_erik.trigger(T_erik_orc_request)

        if M_erik.is_state(S_erik_vr_ready):
            call eriks_basement_vr
            $ M_erik.trigger(T_erik_vr_request)
            if player.has_item('game02') and player.has_item('virtualsaga'):
                jump erik_vr_done

    $ game.main()

label eriks_basement_dewitt_eve_karaoke:
    scene expression player.location.background_blur
    show player 13 at left
    show eve:
        xoffset -200
    show old_erik 1 at right
    with dissolve
    eve "Hey, it's about time! I was starting to think you flaked on me!"

    show eve f_happy
    show player 29 with dissolve
    player_name "Sorry, I got held up! Hey {b}Erik{/b}!"

    show player 13 with dissolve
    show old_erik 4
    erik "Hey, {b}[firstname]{/b}! I was just telling {b}Eve{/b} about my guild on {i}World of Orcette{/i}."

    show old_erik 1
    eve f_eyeroll "Yeah, it was riveting."

    show player 14
    player_name "Heh, I see."

    player_name "Thanks for letting us come over tonight, {b}Erik{/b}."

    show player 13
    show old_erik 4
    erik "Yeah, no problem, dude! You're lucky my guild canceled the raid tonight."

    show old_erik 1
    show player 10
    player_name "Raid?"

    show player 13
    eve f_surprised "No, don't ask!"

    show player 11
    show old_erik 51
    erik "..."
    eve f_happy @ f_normal "Is that booze over there?"

    show player 13
    show old_erik 53
    erik "Y-yeah, why?"

    show old_erik 52
    eve @ f_laugh "'Cause I have a feeling I'm gonna need some tonight!"

    show player 14
    player_name "That's not a bad idea. It'll loosen us up for the karaoke."

    show player 13
    show old_erik 54
    erik "Oh yeah, I guess that makes sense."

    show old_erik 52 with dissolve
    eve "Hey, you've got bourbon, very classy!"

    eve "Why don't you go and grab us some glasses while {b}[firstname]{/b} and I get comfortable on the couch."

    show old_erik 54
    erik "... Sure, okay!"

    hide old_erik with dissolve
    pause
    show eve b_dressed_surprised:
        xoffset -250
    with dissolve
    eve "Can you believe {b}Erik{/b}'s basement is sooo cool?"

    hide player
    hide eve
    show eve b_dressed a_grab_mc f_happy
    show anon a_empty b_empty f_surprised_left:
        flip
        xoffset -343
    with dissolve
    eve "C'mon {b}[firstname]{/b}, let's look at the other room!"

    scene black with fade
    pause

    scene erik_basement_back_b_01 with None
    show player 13 at left
    show eve f_surprised:
        xoffset -200
    with dissolve
    eve "Wow... This is so awesome..."

    show player 14
    player_name "I know right? This is the perfect party house."

    show player 13
    eve f_happy "So have you ever had bourbon before?"

    show player 10
    player_name "Saya kira tidak demikian..."

    show player 5
    eve @ f_laugh "Get ready to have your mind blown!"

    show player 13

    show old_erik 15f at right with dissolve
    erik "I was wondering where you guys went."

    erik "Will these work?"

    show old_erik 15bf

    show eve f_nervous_down:
        flip
        xoffset 300
    with dissolve
    pause
    eve "Tentu."

    show eve f_happy
    show old_erik 16f with dissolve
    pause
    show old_erik 17f with dissolve
    show player 185
    show eve a_bottle
    with dissolve
    eve "Bottoms up!"

    show player 189
    show old_erik 19f
    show eve a_bottle_drink f_drink
    with dissolve
    pause
    show player 190
    show eve a_bottle f_nervous_down
    show old_erik 18f
    with dissolve
    erik "{i}*Cough* *Cough*{/i} It went down the wrong throat! {i}*Cough*{/i}"

    show old_erik 17f
    eve f_happy @ f_laugh "Mmmhmm, that's some good shit right there!"

    show player 191
    player_name "Wow!!! That's really strong!"

    show player 190
    eve "Don't puss out on me yet, boys!"

    show old_erik 18f
    erik "Tentu..."

    show eve a_idle
    show player 13
    with dissolve
    show old_erik 16f with dissolve
    pause
    show old_erik 17f with dissolve
    show player 188
    show eve a_bottle
    with dissolve
    eve "Drink!"

    show player 189
    show eve a_bottle_drink f_drink
    show old_erik 19f
    with dissolve
    pause
    show old_erik 17f with dissolve
    show eve f_laugh a_bottle with dissolve
    eve f_happy @ f_laugh "Whooooo!"

    show player 191 with dissolve
    player_name "Damn!"

    show player 190
    player_name "..."
    show player 187
    player_name "Alright, we should probably get this karaoke machine started up."


    scene erik_basement_back_b_03
    show eve a_bottle f_happy:
        flip
        xoffset 100
    show old_erik 18f at right
    with dissolve
    erik "It's hot in here, is anybody else hot?"

    show old_erik 17f
    eve "Heh, it's the booze, it warms up your insides..."

    player_name "{b}Erik{/b}, how the heck do you work this thing?"

    show eve a_bottle_drink f_drink with dissolve
    show old_erik 18f
    erik "I'll do it, move."


    scene erik_basement_back_b_02
    show eve a_bottle f_happy
    show player 14 at left
    with dissolve
    player_name "You ready to stretch those pipes of yours?"

    show player 13
    eve @ f_laugh "Yeah, I'm gonna need a lot more booze before I'm ready to sing."

    eve "Why don't you guys get started without me?"

    show player 14
    player_name "... Oh, ehh. Alright."

    show player 13
    erik "It's ready!"

    show player 14
    player_name "Let's get this party started!"

    hide player
    hide eve
    with dissolve
    return

label eriks_basement_dewitt_get_beer:
    scene expression player.location.background_blur
    show player 571 with dissolve
    player_name "Yeah, this should be plenty."

    hide player with dissolve
    call popup ('give', 'beer')
    $ player.get_item("beer")
    $ game.main()

label eriks_basement_dewitt_replace_guitar:
    scene expression player.location.background_blur
    show player 575 at right with dissolve
    player_name "(Hmm.)"

    show player 574
    player_name "( It's not that noticeable. )"

    show player 575
    player_name "( ... Yeah, I think this might actually work! )"

    show player 577 with dissolve
    pause
    show mrsj 50f at left with dissolve
    player_name "( Now, I just need to get the real guitar out of here without {b}Mrs. Johnson{/b} seeing me. )"

    show player 576
    show mrsj 52f
    mrsj "What the hell is that?"

    show mrsj 38f
    show player 577df with hpunch
    player_name "!!!"
    show player 577cf
    player_name "H-hey, {b}Mrs. Johnson{/b}..."

    player_name "I didn't hear you come down."

    show player 577bf
    show mrsj 52f
    mrsj "Did you make that thing, {b}[firstname]{/b}?"

    show mrsj 38f
    show player 577cf
    player_name "Y-yeah. Do you like it?"

    show player 577bf
    show mrsj 49f
    mrsj "Hehehe, is this so I won't notice you walking off with my ex-husband's guitar?"

    show mrsj 50f
    show player 577cf
    player_name "... I just need to borrow it for the school talent show and {b}Erik{/b} thought you might get upset."

    show player 577bf
    show mrsj 18f
    mrsj "Did he?"

    show mrsj 49f
    mrsj "Aww, he's such a sweet young man to care about my feelings so much."

    show mrsj 50f
    show player 577cf
    player_name "So, would you mind if I borrowed this guitar for a little while?"

    show player 577bf
    show mrsj 18f
    mrsj "Pfft, not at all, honey."

    show mrsj 49f
    mrsj "I never understood why that good for nothing ex of mine loved them so much. He wasn't even very good at playing them."

    mrsj "You can keep the thing for all I care!"

    mrsj "It's just sitting down here gathering dust after all."

    show mrsj 50f
    show player 577f
    player_name "Benar-benar?"

    show player 576f
    show mrsj 49f
    mrsj "Well, sure! You've been such a good friend to {b}Erik{/b}!"

    mrsj "It's the least I can do!"

    show mrsj 50f
    show player 577f
    player_name "Thank you so much, {b}Mrs. Johnson{/b}!"

    show player 576f
    show mrsj 49f
    mrsj "No problem, honey!"

    mrsj "Just come back real soon and tell me all about this talent show of yours!"

    show mrsj 50f
    show player 577f
    player_name "Yeah, okay! See you soon {b}Mrs. Johnson{/b}!"

    hide player
    hide mrsj
    with dissolve
    $ player.remove_item("fake_guitar")
    $ player.get_item("guitar")
    $ M_dewitt.trigger(T_dewitt_get_fender_guitar)
    $ game.main()

label poker_table:
    scene expression player.location.background_blur
    if not M_erik.once("poker_table_seen"):
        show player 14 at left with dissolve
        show old_erik 1 at right with dissolve
        player_name "You have a freaking {b}poker table{/b} down here?"

        show player 1
        show old_erik 4
        erik "Yeah. You wanna play?"

        menu:
            "Play poker with {b}Erik{/b}?"

            "Ya.":
                player_name "I would, but I've never played poker before..."

                show player 14
                erik "That's fine, I'll explain the rules."

                show player 1
                show old_erik 4
                player_name "In that case, let's play!"

                show player 14
                show old_erik 1

                call popup ('alpha')
                $ game.main()
            "Tidak.":

                player_name "Maybe some other time, man. I'm not in the mood right now."

                show player 14
                show old_erik 1
                erik "That's cool. No problem."

                show player 1
                show old_erik 4
                hide player
                hide old_erik
    else:

        show old_erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Let's play a game of poker!"

        show player 1
        show old_erik 5
        erik "Yeah, I guess we could try it..."

        erik "But, don't we need more players?"

        show old_erik 1
        show player 4
        player_name "Hmm..."

        player_name "Yeah. You're right."

        player_name "We should {b}find someone{/b} who'd want to play with us."

        hide old_erik
        hide player
        with dissolve
    $ game.main()

label cabinet:
    scene erik_basement_cabinet
    show old_erik 1 at right
    show player 14 at left
    with dissolve
    player_name "That's a lot of alcohol..."

    show player 1
    show old_erik 4
    erik "Yeah, {b}Mr. Johnson{/b} always kept it well stocked."

    show old_erik 1
    show player 14
    player_name "Should we try some?"

    show player 1
    show old_erik 4
    erik "I was thinking maybe we should keep it for a special occasion?"

    show old_erik 1
    show player 4
    player_name "I guess you're right."

    player_name "We should {b}find someone{/b} who'd want drink with us."

    hide old_erik
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
