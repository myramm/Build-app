label pink_dialogue:
    $ player.go_to(L_pink)
    if game.timer.is_night():
        $ player.go_to(L_map)
        $ game.main()
    if L_pink.first_visit:
        call expression game.dialog_select("pink_first_visit")
        $ L_pink.visited()

    if game.timer.now in (M_jenny.jenxx_lite_ivy, M_diane.diaxx_cowsuit_ivy):
        $ game.main()
        return

    if M_mia.is_state(S_mia_helen_outfit_request) and not player.has_item("red_corset"):
        call expression game.dialog_select("pink_mia_helen_outfit_request")

    elif M_mia.is_state([S_mia_angelicas_order, S_mia_angelicas_whip]) and not player.has_item("whip"):
        call expression game.dialog_select("pink_mia_angelicas_whip")

    if M_diane.is_state(S_diane_get_outfit_package):
        call expression game.dialog_select("pink_diane_get_outfit_package")
        $ player.get_item("package")
        call popup ('give', 'package')
        $ M_diane.trigger(T_diane_got_outfit_package)

    if M_jenny.is_state(S_jenny_shop_for_toys):
        call expression game.dialog_select("pink_jenny_shop_for_toys")
        $ M_jenny.trigger(T_jenny_buy_vibrator)
    elif M_jenny.is_state(S_jenny_buy_bad_monster):
        call expression game.dialog_select("pink_jenny_buy_bad_monster")
    $ game.main()

label electroclit_sold_out:
    scene expression player.location.background_blur with None
    show player 5
    player_name "( Sold out? )"

    player_name "( That's not good, {b}[jen_name]{/b} is gonna flip out. )"

    pause
    show player 4 with dissolve
    player_name "( Perhaps {b}I should speak with the clerk about this{/b}... )"

    hide player with dissolve
    $ game.main()

label ivy_jane_electroclit_light_dialogue:
    scene location_pink_any_closeup
    show location_pink_any_closeup_counter as counter
    show jane f_mad:
        flip
        xoffset 300
    show ivy f_shy:
        xoffset 100
    show anon with {'master': dissolve}:
        xoffset -230
    jane "Yeah, okay, but this {b}Electro Clit Light{/b} is terrible..."

    show anon a_phone f_looking_down
    with {'master': dissolve}
    jane "... I can barely feel it!"

    ivy "I'm sorry that it failed to meet your expectations, but we do have a strict \"no returns\" policy on all our sex toys."

    ivy "I hope you can understand."

    jane "No, I don't understand!"

    jane "Listen, I'm currently battling a sex addiction and it's very important to my sobriety that I have a toy capable of getting me off!"

    jane "This could cause me to relapse!"

    ivy "Aww, I really wish I could help you but it's not up to me."

    jane "You seriously can't take this piece of shit back?"

    ivy "The boss would have my head if I did..."

    jane "Well, could I get store credit or something?"

    ivy "No, I'm afraid not."

    pause
    ivy "I {i}can{/i} give you a coupon for five dollars off your next purchase..."

    ivy "... Does that help?"

    jane "No, it doesn't help!"

    pause
    jane "{i}*Sigh*{/i} Fine, give me the coupon..."

    jane "... {i}and{/i} I want a real {b}Electro Clit{/b}!"

    jane "Not this crappy 'light' version!"

    ivy "Unfortunately, we're all sold out of the original right now..."

    jane "Ugh, seriously?!"

    ivy "... Again, I'm really sorry for the inconvenience, ma'am."

    show jane f_sad
    jane "Oh my god... I am so gonna end up fucking some random guy that walks into the library, I just know it..."

    show anon a_idle f_surprised
    with {'master': dissolve}
    anon @ -m_talk "( !!! )"
    show anon a_wave f_shy
    with {'master': dissolve}
    anon @ -m_talk "( Hey, I'm a random guy who could walk into the library! )"

    show anon a_idle f_laugh
    with {'master': dissolve}
    ivy "You know, we do offer a fine selction of... {i}*Ahem*{/i} massage options, that might interest you..."

    show anon f_shy
    jane "Massage options?"

    show ivy f_normal a_flyer with dissolve
    ivy "Why don't you have a look at our flyer?"

    show ivy a_idle zorder 0
    show jane f_normal a_flyer
    with dissolve
    jane "Tsk, how exactly is a massage supposed to help me with my sex addiction-"

    jane "Oh!"

    show jane f_sexy a_idle
    with {'master': dissolve}
    jane "Oh, wow... okay!"

    pause
    jane "And will you be the one administering this \"massage?\""

    show ivy f_sexy
    ivy "Mhmm."

    ivy "Assuming that's agreeable?"

    jane f_curious "Yeeeaah, umm..."

    show jane b_dressed_look_back
    with {'master': dissolve}
    pause 1
    show anon f_confused
    show jane b_dressed
    with {'master': dissolve}
    jane "... Actually..."

    show jane a_come_closer f_sexy
    with {'master': dissolve}
    pause
    show jane a_whisper b_dressed_bend
    show ivy f_sexy_curious
    with {'master': dissolve}
    ivy @ -m_talk "Hmm?"

    show jane b_dressed_bend a_whisper
    show ivy a_listen b_dressed_bend:
        xoffset -50
    with {'master': dissolve}
    jane "..."
    ivy f_sexy "Oh?"

    jane "..."
    show jane a_idle b_dressed
    show ivy a_idle b_dressed:
        xoffset 100
    with {'master': dissolve}
    ivy "Apa kamu yakin?"

    jane "Tentu saja!"

    show ivy a_giggle
    with {'master': dissolve}
    ivy f_laugh "Hehe!"

    show ivy a_idle f_sexy
    with {'master': dissolve}
    ivy "I've never had anyone request that before!"

    hide ivy
    show jane f_sexy_lipbite
    with {'master': dissolve}
    pause
    show ivy a_towel behind counter:
        xoffset 50
    with {'master': dissolve}
    ivy "Come on back and we'll see where things go."

    show jane a_hand_out f_sexy
    with {'master': dissolve}
    jane "After you, Red."

    hide ivy with dissolve
    hide jane with dissolve
    pause
    anon f_surprised @ -m_talk "( Did that seriously just happen or am I dreaming right now? )"

    anon f_brag_closed @ f_thinking -m_talk "( {b}I wonder if I could sneak a peek{/b}? )"

    pause
    show anon f_shy
    pause
    show anon f_surprised
    anon @ -m_talk "( !!! )"
    anon @ -m_talk "( Hey look, they left that toy sitting there on the counter! )"

    hide anon with dissolve
    $ M_jenny.trigger(T_jenny_ivy_jane_leaving)
    $ game.main()

label pink_get_electroclit_light:
    scene expression player.location.background_blur with None
    show player 287 with dissolve
    player_name "( Hmm, it's not exactly what {b}[jen_name]{/b} wanted but it's pretty close. )"

    player_name "( ... Maybe she won't notice the difference? )"

    show player 3 with dissolve
    pause
    show player 3f with dissolve
    pause
    show player 3 with dissolve
    player_name "( I probably shouldn't just take this thing without leaving her some money... )"

    if player.has_money(1):
        show player 638b with dissolve
        player_name "( ... She was looking for refund after all, so I think it will be fine. )"

    else:
        show player 97b with dissolve
        player_name "All I have is this lollipop..."

        show player 93 with dissolve
        player_name "Slightly used..."

    show player 17 with dissolve
    player_name "( Alright, now to get this thing home to {b}[jen_name]{/b} and claim my reward! )"

    hide player with dissolve
    $ player.spend_money(100)
    $ M_jenny.trigger(T_jenny_got_a_toy)
    $ game.main()

label pink_ultravibrator_callback:
    if M_jenny.is_state(S_jenny_buy_vibrator):
        $ renpy.scene(layer='screens')
        call expression game.dialog_select("pink_jenny_buy_vibrator")
        $ M_jenny.trigger(T_jenny_bought_vibrator)
        $ game.timer.tick()
    $ game.main()

label bad_monster_callback:
    $ renpy.scene(layer='screens')
    call expression game.dialog_select("pink_jenny_buy_bad_monster_callback")
    $ M_jenny.trigger(T_jenny_bought_bad_monster)
    $ game.main()


label pink_backroom_veronica:
    if not M_ivy.once('scene_vera'):
        call diaXX_pink_extra
    else:
        call diaXX_pink_extra.repeat
    $ game.main()
    return


label pink_backroom_jane:
    if not M_ivy.once('scene_jane'):
        call jenXX_pink_extra
    else:
        call jenXX_pink_extra.repeat
    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
