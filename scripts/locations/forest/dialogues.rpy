label forest_first_visit:
    scene expression game.timer.image("forest{}_b")
    show player 43 with dissolve
    player_name "Wah!"

    player_name "( I've never been to the forest before... )"

    player_name "( It's so... Calm... )"

    return

label forest_anna_missing_pup_started_dark:
    scene expression game.timer.image("forest{}_b")
    show player 4 with dissolve
    player_name "( It's too dark to look for {b}Awesomo{/b}. )"

    hide player with dissolve
    return

label forest_anna_missing_pup_started_have_cookies:
    scene expression game.timer.image("forest{}_b")
    show player 4 with dissolve
    player_name "( Let's see if I can find that dog. )"

    scene forest_closeup
    show player 239 at left
    with dissolve
    player_name "( Now... )"

    show player 240
    player_name "( ... I should be able to lure him out... )"

    show player 245 at Position(xpos=8)
    player_name "( ... Using {b}this{/b}! )"

    show player 246 at left
    pause
    show player 1 with dissolve
    player_name "( Let's see if he comes out. )"

    show player 31
    player_name "( He must be around here somewhere... )"

    hide player with dissolve
    return

label forest_anna_missing_pup_started_no_cookies:
    scene expression game.timer.image("forest{}_b")
    show player 4 with dissolve
    player_name "( I should {b}find some cookies to lure Awesomo out with{/b}. )"

    hide player with dissolve
    return

label forest_okita_get_ingredients:
    scene expression game.timer.image("forest{}_b")
    show player 2 with dissolve
    player_name "Alright, so the {b}mushroom{/b} should be here somewhere."

    player_name "... And she said to look for the {b}Toad{/b} near water and the {b}flower{/b} in a cave."

    hide player with dissolve
    return

label forest_dewitt_make_new_flute:
    scene expression game.timer.image("forest{}_b")
    show player 32 with dissolve
    player_name "Huh, I don't see any fallen branches here."

    player_name "I should look around elsewhere."

    hide player with dissolve
    return

label awesomo_dialogue_intro:
    scene expression game.timer.image("forest{}_b")
    show player 177 with dissolve
    player_name "Hey there little guy..."


    player_name "What're you doing all the way out here?"

    awesomo "Bark!"

    player_name "You got your owner all worried about you!"

    awesomo "Bark!"

    player_name "You're a funny looking doggo..."

    return

label awesomo_dialogue_give_cookie:
    scene expression game.timer.image("forest{}_b")
    show player 177
    player_name "Want a cookie?"

    show player 178 at Position(xpos=517)
    player_name "Ini dia..."

    show player 179 with hpunch
    player_name "!!!"
    show player 180
    player_name "Jeez!"

    player_name "Someone's hungry..."

    show player 181
    player_name "Hmm..."

    show player 182
    player_name "I like you!"

    awesomo "Bark!"

    return

label awesomo_dialogue_check_name_tag_pre:
    scene expression game.timer.image("forest{}_b")
    show player 177
    player_name "Let's see if you're the one I'm looking for..."

    show awesomo_tag zorder 2 with dissolve
    player_name "{b}Awesomo{/b}... Yup! Must be you!"

    hide awesomo_tag with dissolve
    return

label awesomo_dialogue_check_name_tag_after:
    scene expression game.timer.image("forest{}_b")
    show player 182
    with fade
    player_name "Let's get you back to your owner."

    player_name "She's worried sick..."

    show player 181
    awesomo "Bark!"

    show player 182
    player_name "Haha! Alright, let's go then..."

    hide player with dissolve
    return


label dirt_pile:
    if player.has_item("shovel"):
        call expression game.dialog_select("forest_dirt_pile_have_shovel_intro")
        menu:
            "Dig with a shovel." if player.has_item("shovel"):
                call expression game.dialog_select("forest_dirt_pile_have_shovel_dig")
                call screen forest_worms
            "Leave it alone.":

                call expression game.dialog_select("forest_dirt_pile_have_shovel_leave")
    else:

        call expression game.dialog_select("forest_dirt_pile_no_shovel")
    $ game.main()

label forest_dirt_pile_have_shovel_intro:
    scene location_forest_dirt1
    player_name "( There's something strange about this patch of dirt... )"

    player_name "( It seems like something's moving under it. )"

    player_name "( Maybe I could dig it out? )"

    return

label forest_dirt_pile_have_shovel_dig:
    player_name "( Let's see what's in there... )"

    scene location_forest_dirt2
    pause
    scene location_forest_dirt3
    player_name "{b}Worms{/b}?!"

    player_name "( They say these make great {b}fishing bait{/b}. )"

    player_name "( Maybe I'll keep some for later... )"

    return

label forest_dirt_pile_have_shovel_leave:
    player_name "( On second thought... )"

    player_name "( Perhaps I should leave them alone... )"

    return

label forest_dirt_pile_no_shovel:
    scene location_forest_dirt1
    player_name "( There's something strange about this patch of dirt... )"

    player_name "( It seems like something's moving under it. )"

    player_name "( I need to {b}find a shovel{/b} to dig it out. )"

    return

label forest_worms:
    call popup ('give', 'worm')
    $ player.get_item("worm")
    $ game.main()

label mushroom:
    call expression game.dialog_select("forest_mushroom_intro")
    if M_okita.is_state(S_okita_get_ingredients):
        call expression game.dialog_select("forest_mushroom_okita_get_ingredients")

    if M_aqua.is_state(S_aqua_seasucc_mushroom):
        call expression game.dialog_select("forest_mushroom_aqua_seasucc_mushroom")

    call expression game.dialog_select("forest_mushroom_take_mushroom")
    $ player.get_item("mushroom")
    $ game.main()

label forest_mushroom_intro:
    scene expression game.timer.image("forest{}_b")
    show player 498 with dissolve
    return

label forest_mushroom_okita_get_ingredients:
    player_name "Well, it certainly is... {i}Phallic{/i}."

    return

label forest_mushroom_aqua_seasucc_mushroom:
    player_name "This must be the mushroom {b}Aqua{/b} spoke of."

    player_name "I could try and feed it to {b}SeaSucc{/b}..."

    return

label forest_mushroom_take_mushroom:
    call popup ('give', 'mushroom')
    return

label altar:
    if M_aqua.is_set("altar pass"):
        scene expression game.timer.image("location_forest_puzzle_day{}")
        pause
        $ game.main()

    call expression game.dialog_select("altar_intro_pre")
    if not game.timer.is_dark():
        call expression game.dialog_select("altar_intro_day")
    else:

        call expression game.dialog_select("altar_intro_night")
        $ game.timer.tick()
        label altar_puzzle:
            call screen altar_puzzle
            if piecelist[9] == [162,143] and piecelist[18] == [382,20] and piecelist[16] == [600,139] and piecelist[14] == [383,263] and piecelist[10] == [163,385] and piecelist[12] == [603,387] and piecelist[20] == [384,516]:
                call screen altar_puzzle_finish
            jump expression game.dialog_select("altar_puzzle")
    $ game.main()

label altar_intro_pre:
    scene expression game.timer.image("forest_altar{}")
    show text _ ("A strange stone structure stands in the middle of the forest.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It looks old! Completely overgrown in moss...") as caption with dissolve
    pause
    hide caption with dissolve
    if not game.timer.is_dark():
        show text _ ("... And there's {b}sunlight{/b} shining directly down upon it.") as caption with dissolve
    else:
        show text _ ("... And there's {b}moonlight{/b} shining directly down upon it.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("This must be what I'm looking for.") as caption with dissolve
    pause
    return

label altar_intro_day:
    scene location_forest_puzzle_day
    player_name "Hmm..."

    player_name "This looks like the alter that was on the church bell..."

    player_name "... But something's not right. This just looks like a dead-end."

    player_name "Hmm, what were the clues again?"

    player_name "A stone alter, with trees around it and the {b}moon shining down{/b}."

    player_name "I should think it over."

    return

label altar_intro_night:
    scene location_forest_puzzle_night_closed
    player_name "Well, that's strange."

    player_name "It looks like the moon is affecting the alter somehow."

    player_name "These symbols must be important and it looks like I can move them around to make a picture..."

    player_name "Maybe it's some kind of puzzle?"

    return

label altar_puzzle_finish:
    call expression game.dialog_select("altar_puzzle_finish_dialogue")
    $ player.get_item("treasure_map")
    $ M_aqua.trigger(T_aqua_altar_puzzle_solve)
    $ game.main()

label altar_puzzle_finish_dialogue:
    scene expression "location_forest_puzzle_night"
    call popup ('give', 'treasure_map')
    return

label altar_puzzle_leave:
    scene expression game.timer.image("forest{}_b")
    show player 12 with dissolve
    player_name "Huh... Maybe there's something that would hint at how to solve this puzzle."

    if not player.has_item("scroll"):
        player_name "I could take another {b}look at the church bell{/b} and see if I missed something."

    else:
        player_name "Maybe that {b}scroll I found in the tree{/b} has details on this puzzle."

    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
