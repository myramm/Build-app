label generic_item_closeup(item):
    scene location_backpack_closeup
    show expression item.closeup
    pause
    return

label obituary_records(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."
    player_name "It seems like the only name under shipwright is..."
    player_name "... Ben Dover?"
    player_name "Now I just need to {b}visit the graveyard and find the right tombstone{/b}."
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label keycode_note_closeup(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This is the {b}code to Miss Okita's office{/b}. {b}6219{/b}."
    return


label scroll(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Hmm..."
    player_name "There's a strange picture on it."
    player_name "It looks like a crescent moon..."
    player_name "It must be {b}useful for something{/b}..."
    return

label treasure_map(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This is too cool!"
    player_name "An actual treasure map!"
    player_name "Hmm."
    player_name "It looks like a drawing of the coast..."
    player_name "... And that looks like our local beach?"
    player_name "Oh, and here, {b}there's an X on a small island{/b}."
    player_name "I wonder what it leads to?"
    $ M_aqua.trigger(T_aqua_obituary_records)
    return

label weird_coin(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Huh?"
    player_name "That looks like a really old coin."
    player_name "Just look at these {b}odd symbols{/b}!"
    player_name "I should keep it. Maybe it's worth something?"
    return

label old_book(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "This book looks like it would be useful decoding something."
    player_name "..."
    if not player.has_item("weird_coin"):
        player_name "Heh. Maybe some hidden pirate treasure someone tossed aside carelessly."
        player_name "But that's just wishful thinking."
    else:
        player_name "I think {b}that pirate coin had a four-digit number on it{/b}."
        player_name "I should {b}look at it again{/b}."
    return

label golden_compass(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Whoa!!"
    player_name "I can't believe it! I found the treasure!"
    player_name "This has to be the compass {b}Captain Terry{/b} was talking about."
    return

label tigger(item):
    scene location_backpack_closeup
    show expression item.closeup at Position(xalign = 0.5, yalign = 1.0)
    with None
    player_name "Whew, this mean bastard put up quite a fight."
    player_name "... And just look at those teeth!"
    player_name "It's no wonder why {b}Captain Terry{/b} wanted him dead."
    player_name "I can't wait to show him!"
    return


label cumdoom_pills(item):
    scene expression player.location.background_blur
    if player.pregnancy_chance == 0:
        show player 705b with dissolve
        player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
        player_name "( {b}Effects will last for 24 hours{/b}. )"
        player_name "( There's also a warning label: \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\" )"
        player_name "( I've already taken a dose today. )"
        player_name "( I definitely shouldn't take another. )"
        hide player with dissolve
    else:
        show player 705b with dissolve
        player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
        player_name "( {b}Effects will last until I take a Pregnax pill{/b}. )"
        player_name "( There's also a warning label: \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\" )"
        player_name "( Should I take a {b}Cumdoom{/b} pill? )"
        menu:
            "Yes.":
                show player 706b with dissolve
                player_name "( Welp, here goes nothing... )"
                show player 707b with dissolve
                pause
                $ player.pregnancy_chance = 0.0
                hide player with dissolve
            "No.":
                show player 705b
                player_name "Nah, I don't think now is the best time to take one of these."
                hide player with dissolve
    return

label pregnax_pills(item):
    scene expression player.location.background_blur
    if player.pregnancy_chance >= 40:
        show player 705 with dissolve
        player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
        player_name "( {b}Effects will last for 24 hours{/b}. )"
        player_name "( There's also a warning label: \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\" )"
        player_name "( I've already taken a dose today. )"
        player_name "( I definitely shouldn't take another. )"
        hide player with dissolve
    else:
        show player 705 with dissolve
        player_name "( Hmm, the directions say I need to {b}take one pill, orally, prior to engaging in sexual activity{/b}. )"
        player_name "( {b}Effects will last until I take a Cumdoom pill{/b}. )"
        player_name "( There's also a warning label: \"Do not use this medication if your partner is currently menstruating or has undergone menopause.\" )"
        player_name "( Should I take a Pregnax pill? )"
        menu:
            "Yes.":
                show player 706 with dissolve
                player_name "( Welp, here goes nothing... )"
                show player 707 with dissolve
                pause
                $ player.pregnancy_chance += 0.5
                hide player with dissolve
            "No.":
                show player 705
                player_name "Nah, I don't think now is the best time to take one of these."
                hide player with dissolve
    return

label condom:
    scene expression game.timer.image("jennybedroom{}")
    show expression "objects/closeup_condom.png" with dissolve
    player_name "A condom?!"
    player_name "{b}[jen_name]{/b} must be hiding them in her room."
    player_name "She probably won't notice if I only take one..."
    hide expression "objects/closeup_condom.png" with dissolve
    call popup ('give', 'condom')
    $ game.main()

label mysterious_statue_1(item):
    scene expression player.location.background_blur
    show player 688
    with dissolve
    player_name "( Hmm, it looks like the lower half a nude woman. )"
    player_name "( What's with the tail though? )"
    show player 689
    player_name "( There's something written on the bottom of it. )"
    show expression item.closeup
    hide player
    player_name "{b}\"Delmont.\"{/b}"
    player_name "Hmm, {b}Delmont{/b}..."
    player_name "It sounds familiar."
    hide expression item.closeup
    return

label attic_key:
    scene expression player.location.background_blur
    show expression "objects/closeup_key.png" with dissolve
    player_name "( I've never seen this key before. )"
    player_name "( It's rather small... )"
    hide expression "objects/closeup_key.png" with dissolve
    $ player.get_item("attic_key")
    call popup ('give', 'attic_key')
    jump entrance_dialogue

label ring:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "( That looks like an expensive ring! )"
    player_name "( What was it doing all the way up there? )"
    hide expression "objects/closeup_ring.png" with dissolve
    call popup ('give', 'ring')
    jump attic_dialogue

label cheerleader_outfit:
    scene expression game.timer.image("attic{}")
    if M_jenny.is_state(S_jenny_get_cheerleader_outfit):
        show anon with dissolve
        anon @ -m_talk "( Hmm, I don't see any dust or cobwebs... )"
        anon @ -m_talk "( I should take this to {b}[jen_name]'s room in the afternoon{/b}. )"
        hide anon with dissolve
        $ player.get_item("cheerleader_outfit")
        call popup ('give', 'cheerleader_outfit')
        $ M_jenny.trigger(T_jenny_got_cheerleader_outfit)
    else:
        show anon with dissolve
        anon @ -m_talk "( This is {b}[jen_name]'s cheerleading outfit{/b} from college. )"
        anon @ -m_talk "( I wonder what it's doing up here? )"
        hide anon with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression game.timer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "That's {b}Dad{/b}'s old fishing rod!"
    player_name "( I remember when we used to go fishing by the pier, when I was little. )"
    player_name "{i}*Sigh*{/i}"
    player_name "I miss {b}Dad{/b}..."
    hide expression "objects/closeup_rod.png" with dissolve
    call popup ('give', 'fishing_rod')
    if L_pier.locked:
        $ L_pier.unlock()
    jump attic_dialogue

label backpack_pickup_dialogue:
    scene location_park_day_blur
    show player 608
    with dissolve
    pause
    show player 608b
    player_name "This is definitely {b}Eve{/b}'s backpack."
    player_name "Hmm, I don't see her {b}art pad{/b} though."
    show player 610 with dissolve
    player_name "I should {b}ask her about it when I return this{/b}."
    hide player with dissolve
    $ player.get_item("eve_backpack")
    call popup ('give', 'eve_backpack')
    jump park_dialogue

label roxxy_homework_pickup_dialogue:
    scene mc_locker
    player_name "Ah, here it is!"
    player_name "Now I just need to {b}bring this to Roxxy{/b}."
    $ player.get_item("roxxy_homework")
    call popup ('give', 'roxxy_homework')
    $ player.go_to(L_school_hall)
    $ game.main()

label poem(item):
    scene location_backpack_closeup
    show expression item.closeup at truecenter
    anon "( \"I slip slowly under the satin sheets.\" )" (show_native="( {i}\"Je me glisse lentement sous les draps de satin.\"{/i} )")
    anon "( \"You are lying on your stomach, your back welcomes my hand.\" )" (show_native="( {i}\"Tu es allong? sur le ventre, ton dos accueil ma main.\"{/i} )")
    anon "( \"Slowly your naked body you expose.\" )" (show_native="( {i}\"Tout doucement ton corps nu tu exposes.\"{/i} )")
    anon "( \"On your breasts my mouth rests.\" )" (show_native="( {i}\"Sur tes seins ma bouche se pose.\"{/i} )")
    pause
    anon "( I need to turn this in to {b}Ms. Bissette{/b} and hope no one else ever reads this! )"
    return

label french_scans(item):
    scene location_backpack_closeup
    show expression item.closeup at truecenter
    anon "( What a weird word... I wonder what it means. I better see {b}Ms. Bissette{/b}. )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
