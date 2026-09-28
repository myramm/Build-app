label mall_dialogue:
    $ player.go_to(L_mall)
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)

    if L_mall.first_visit:
        call expression game.dialog_select("mall_first_visit")
        $ L_mall.visited()

    if M_debbie.is_state(S_debbie_mall_outing):
        call expression game.dialog_select("mall_mom_mall_outing")
        $ M_debbie.trigger(T_debbie_mall_arrival)

    if M_roxxy.is_state(S_roxxy_fake_id_ask_terry) and M_roxxy.get("take roxxy mall"):
        call expression game.dialog_select("mall_roxxy_fake_id_ask_terry")

    if M_diane.is_state(S_diane_go_to_mall):
        call expression game.dialog_select("mall_diane_get_bug_spray")
        $ M_diane.trigger(T_diane_arrived_at_mall)

    if M_jenny.is_state(S_jenny_go_shopping):
        call expression game.dialog_select("mall_jenny_go_shopping")
        $ M_jenny.trigger(T_jenny_go_at_pinks)
    elif M_jenny.is_state(S_jenny_get_a_mask):
        call expression game.dialog_select("mall_jenny_get_a_mask")

    if M_eve.is_state(S_eve_clients_mall_fliers) and game.timer.is_day():
        call expression game.dialog_select("mall_eve_clients_mall_fliers")
        $ M_eve.trigger(T_eve_mall_fliers_hung)

    elif M_eve.is_state(S_eve_make_up_go_to_mall):
        if M_eve.make_up_go_to_mall_first:
            call expression game.dialog_select("mall_eve_make_up_go_to_mall_first")
            $ M_eve.set("make_up_go_to_mall_first", False)
            if player.has_item("chocolates") and player.has_item("candle"):
                call expression game.dialog_select("mall_eve_make_up_go_to_mall_has_items")
                jump mall_eve_make_up_go_to_mall_has_chocolates_candles
        else:
            call expression game.dialog_select("mall_eve_make_up_go_to_mall_repeat")
            if player.has_item("chocolates") and player.has_item("candle"):
                call expression game.dialog_select("mall_eve_make_up_go_to_mall_has_items")
                jump mall_eve_make_up_go_to_mall_has_chocolates_candles

    $ game.main()

label cupid_store_waiting_line:
    scene expression game.timer.image('location_mall{}_closeup_comic')
    show erik:
        flip
        xoffset 100
    show karl:
        flip
        xoffset 350
    show justin:
        flip
        xoffset 600
    show player 10 behind erik at left with dissolve
    player_name "{b}Erik{/b}?"
    show player 5
    erik @ -m_talk "Hmm?"
    show erik:
        unflip
        xoffset -300
    show karl:
        unflip
        xoffset -150
    with dissolve
    erik "{b}[firstname]{/b}?"
    show justin:
        unflip
        xoffset 50
    with dissolve
    show player 14
    player_name "What's going on?"
    show player 13
    erik "I didn't know you're a wrestling fan."
    show player 10
    player_name "Wrestling?"
    show player 13
    erik "Yeah, aren't you here to pick up the new game?"
    show player 10
    player_name "What new game?"
    show player 5
    show karl f_curious
    karl "You don't know about {b}WPWF{/b}?"
    show player 10
    player_name "Excuse me?"
    show player 5
    karl "Uhh, {b}Women's Professional Wrestling Federation{/b}?"
    show karl f_angry
    karl "Psh, who is this joker?"
    show erik:
        flip
        xoffset 100
    with dissolve
    erik "Whoa, calm down {b}Brutalitops{/b}!"
    erik "{b}[firstname]{/b} is an ally."
    justin "Is he here to join our merry band?"
    karl "C'mon, we don't need this guy."
    erik "Eh, {b}[firstname]{/b} doesn't really play {b}WoO{/b}."
    karl @ f_eyeroll "Laaaaame."
    justin "That's too bad, because our guild could really use some new members."
    show karl f_embarassed
    karl "I bet he doesn't even have a class."
    erik "We could give him one."
    justin "How about a bard?"
    justin "That would suit our party's needs perfectly."
    karl "Yeah, or a druid maybe..."
    karl "... Then we'd have bark armor and thorns!"
    show player 10
    player_name "{b}Erik{/b}, who are these guys?"
    show player 5 with None
    show karl f_normal with None
    show erik:
        unflip
        xoffset -300
    with dissolve
    erik "Heh, these are my guildmates from {i}World of Orcette{/i}."
    show player 10
    player_name "Oh."
    show player 5 with None
    show erik:
        flip
        xoffset 100
    with dissolve
    erik "This here is {b}Karl{/b}."
    show karl f_angry a_fist with dissolve
    karl "Only my friends know me as {b}Karl{/b}."
    show karl f_crazy_laugh
    karl "You have to call me {b}Brutalitops{/b}!"
    karl "Master of the Seven Sided Strike and defender of goblin maidens!"
    show karl f_normal a_idle with dissolve
    show player 30
    player_name "Goblin maidens?"
    show player 5 with None
    show erik:
        unflip
        xoffset -300
    with dissolve
    erik "He's our Fury Monk."
    show erik:
        xoffset -350
    with dissolve
    erik "Hence the anger issues."
    show erik:
        xoffset -300
    with dissolve
    show player 10
    player_name "O-okay..."
    show player 5 with None
    show erik:
        flip
        xoffset 100
    with dissolve
    erik "And this is {b}Justin the Wise{/b}, our guild leader and the most talented wizard in all the lands."
    justin "Oh, please... he's exaggerating."
    karl "No way, man!"
    karl "The way you charmed that demoness the other day..."
    erik "Yeah, it was incredible!"
    show justin f_boasting a_boasting with dissolve
    justin "That was nothing."
    justin "The real magic didn't happen until we retired to my bed chambers for the night."
    show justin f_normal
    justin "If you catch my drift?"
    show justin a_idle with dissolve
    show player 10
    player_name "Ehh..."
    show player 5
    justin "Pleasure to meet you, {b}[firstname]{/b}."
    justin "Any friend of {b}Erik the Mighty{/b} is a friend to me as well."
    show erik:
        unflip
        xoffset -300
    with dissolve
    show player 14
    player_name "Y-yeah, thanks."
    player_name "So all these people are here to buy a wrestling game?"
    show player 13
    erik "Pretty much."
    justin "Not me, I'm here to meet the {b}Pink Cyclone{/b} in the flesh!"
    justin "She's always been my favorite."
    show player 14
    player_name "Who?"
    show player 13
    karl "{b}Pink Cyclone{/b}, man!"
    karl "You've seriously never heard of her?!"
    show player 14
    player_name "Nope, sorry."
    show player 13
    show karl f_curious
    karl "Sheesh, you need to get out more."
    erik "She's the undefeated champion of the {b}WPWF{/b}!"
    show player 14
    player_name "Oh, really?"
    show player 13
    justin "More like the undefeated champion of my heart."
    show karl f_eyeroll
    karl "Well, she's not exactly undefeated..."
    show karl f_normal with None
    show erik:
        flip
        xoffset 100
    with dissolve
    erik "C'mon man, {b}Nikita{/b} totally cheated!"
    erik "The commissioner even declared the match no contest."
    show karl f_curious
    karl "Doesn't matter, the {b}Pink Cyclone{/b} lost the belt."
    erik "Only because {b}Nikita{/b} shattered her knee with a chair!"
    karl "Yeah, leaving her incapable of defending the title."
    erik "She's still 34-0."
    show karl f_embarassed
    karl "You mean, 34-0-1."
    erik "It was a no contest!"
    karl "She hasn't wrestled since, man... and that was three years ago!"
    show player 14
    player_name "So this {b}Pink Cyclone{/b} lady is here today?"
    show player 13
    show karl f_normal with None
    show erik:
        unflip
        xoffset -300
    with dissolve
    erik "Yeah, she's inside signing autographs to promote the video game."
    erik "You wanna come with us and meet her?"
    show player 29 with dissolve
    player_name "Eh, sure... I guess."
    show player 13 with dissolve
    show justin f_boasting
    justin "I'm totally gonna declare my love to her."
    show erik:
        flip
        xoffset 100
    show karl:
        flip
        xoffset 350
    with dissolve
    karl "Don't you have enough women, {b}Justin{/b}?!"
    show justin f_normal
    karl "With the new demoness and those elven twins, you've basically got a harem!"
    show player 17
    justin "There's no such thing as enough women, {b}Karl{/b}..."
    show player 13
    karl "I dunno, I'm happy with what I've got."
    justin "Hah, you and your goblin maidens..."
    justin "... I just don't see the appeal."
    erik "I think he's got a midget fetish!"
    show player 11
    show karl f_crazy_laugh
    karl "What?!"
    show karl f_angry
    karl "That's not it at all, you guys!"
    player_name "..."
    scene black with fade
    pause
    scene expression "backgrounds/location_mall_closeup_comic.jpg" with None
    show player 9 at left
    show erik:
        flip
        xoffset 100
    show karl:
        flip
        xoffset 350
    show justin:
        flip
        xoffset 600
    with dissolve
    karl "Alright, we're next!"
    show karl f_normal
    show justin f_boasting
    justin "Wish me luck, fellas."
    hide karl
    hide justin
    with dissolve
    erik "That crazy bastard."
    show player 14 with dissolve
    player_name "You definitely have some colorful friends, {b}Erik{/b}."
    show player 13
    erik "Yeah, we get along pretty well."
    show erik:
        unflip
        xoffset -300
    with dissolve
    erik "You really can join our guild, you know?"
    show player 14
    player_name "Eh, I'm not sure I would fit in with those guys."
    show player 13
    erik "Dude, what are you talking about?!"
    erik "You're awesome!"
    erik "We'd all be ecstatic if you joined."
    show player 14
    player_name "Heh, thanks for saying that {b}Erik{/b}."
    player_name "I'll think about it."
    show player 13
    erik "Okay."
    karl "HAHAHAAH!"
    show justin a_neck f_wincing:
        xoffset -120
    show karl f_embarassed a_game:
        xoffset 100
    show erik:
        flip
        xoffset 100
    with dissolve
    karl "Dude, that was hilarious!"
    justin "Shut up, {b}Karl{/b}!"
    justin "It wasn't funny!"
    karl "Pfft, hahahaha!!"
    erik "What happened?"
    karl "Romeo over here confessed his undying love to the {b}Pink Cyclone{/b} and then tried to hug her."
    show player 14
    player_name "So, what's funny about that?"
    show player 13
    karl "Before he got within two steps, she lashed out and put him in a headlock!"
    show player 11
    show erik f_surprised
    erik "Really?!"
    karl "Haha, yeah, and she wouldn't let him go until he apologized!"
    show erik f_normal
    erik "You okay, {b}Justin{/b}?"
    show justin f_boasting a_boasting with dissolve
    justin "Are you kidding?"
    show justin f_wincing a_neck with dissolve
    justin "I've never been better!"
    show player 10
    player_name "Huh?"
    show player 5
    show justin f_boasting
    justin "She smelled so good, man!"
    show player 37 with dissolve
    justin "I would have stayed in that headlock all day if they had let me."
    show player 13
    karl "Dude, you almost passed out..."
    show justin f_normal
    justin "All part of the act, my friend."
    karl "Yeah, right!"
    justin "She was crazy strong though!"
    show karl f_normal a_game_up with dissolve
    karl "Welp, I got my game and my autograph."
    karl "I can't wait to crack this sucker open and PWN some noobs!"
    karl "C'mon, let's go {b}Justin{/b}."
    show karl a_game with dissolve
    justin "Yeah okay, I might need to pay my chiropractor a visit..."
    karl "Later, {b}Erik{/b}."
    hide karl
    hide justin
    with dissolve
    erik "Cya online, guys!"
    show player 14
    player_name "I guess we're next, huh?"
    show player 13
    erik "This is going to be awesome!"
    scene black with fade
    pause

    $ player.go_to(L_comicstore)
    scene expression player.location.background_blur with None
    show player 13 at left
    show erik f_surprised:
        flip
        xoffset 100
    show lily zorder 1:
        xoffset 100
    show bridget b_lucha o_mask a_sides zorder 0:
        flip
        xoffset 400
    with dissolve
    lily "Are you sure you don't want me to call the cops?"
    pink "Oh, there's no reason to get the cops involved."
    pink "I took care of it."
    lily "O-okay."
    pink "Besides, he's long gone by now."
    pink "How many more copies are left?"
    lily "Just the one."
    pink "Good, my time is almost up here."
    show player 29 with dissolve
    player_name "H-hello?"
    show player 13
    show bridget a_hips zorder 2:
        unflip
        xoffset -100
    with dissolve
    pink "Nice to mee-"
    show bridget f_surprised
    pause
    pink f_angry "W-what are you two doing here?!"
    show player 5
    player_name "Hmm?"
    pink "Did somebody put you up to this?"
    pink "'Cause I'm not laughing!"
    show player 10
    show erik f_faint
    player_name "N-nobody pu-"
    show erik:
        xoffset -100
    hide player
    show bridget a_hold_mc1
    with dissolve
    pink "You better start talking, right now!"
    show erik a_faint with dissolve
    pause
    show erik b_dressed_falling with dissolve
    show erik b_dressed_ground with dissolve
    hide erik with dissolve
    pink f_surprised "!!!"
    show bridget a_hold_mc2
    player_name "W-we just want an autograph!"
    show bridget a_hold_mc1
    pause
    show bridget f_normal a_sides
    show player 22 at left
    with dissolve
    pink "Oh."
    pink "Sorry about that, I guess I mistook you for someone else..."
    show player 10
    player_name "{i}*Gulp*{/i} S-sure, no problem."
    show player 5
    pink "Is he alright?"
    show player 10
    player_name "{b}Erik{/b}?"
    show player 184 with dissolve
    pause
    hide player
    show erik b_dressed_pickup:
        flip
    with dissolve
    pause
    show player 5 at left
    show erik b_dressed a_idle f_woozy:
        unflip
        xoffset -300
    with dissolve
    erik "W-what happened?!"
    show player 10
    player_name "You fainted, dude."
    show player 5
    erik "I did?"
    show erik a_faint:
        flip
        xoffset 100
    with dissolve
    lily @ f_laugh "Hehe, that's so adorable!"
    show player 13
    pink a_hips "You boys are big fans, huh?"
    show erik f_normal a_idle with dissolve
    erik "Oh, totally!"
    erik "That time you knocked out {b}Lioness{/b} in the royal rumble!"
    erik "Or when you tapped out {b}Rebecca Savage{/b} in that cage match!"
    erik "Oh and your moonsault off the top rope onto-"
    pink "Okay, okay, I get it..."
    pink @ f_laugh "Hah, you two really ARE big fans."
    erik "The BIGGEST!"
    pink "Well, I've got something special for you two then."
    erik "R-really?!"
    show bridget b_lucha_bend o_empty with dissolve
    pink "Mmhmm."
    show bridget f_normal o_mask a_poster b_lucha with dissolve
    pink "Here you go."
    show bridget a_poster_show with dissolve
    show erik f_surprised
    erik "WHOA!!!"
    show player 735
    show bridget a_hips
    show erik f_normal a_poster
    with dissolve
    erik "{b}Justin{/b} is going to be so jealous..."
    erik "... This is like, the coolest thing ever!"
    show player 14 with dissolve
    player_name "Thank you, miss... uhh, {b}Pink Cyclone{/b}."
    show player 13
    pink "You're very welcome, boys."
    show bridget zorder 0:
        flip
        xoffset 400
    with dissolve
    pink "Now, unless there's anything else?"
    pink "I should really head out."
    lily "Nope, you've already done so much."
    show lily a_mask_point with dissolve
    lily "These replica masks are going to be a huge hit with our cosplay community!"
    show player 11
    lily "I might even grab one for myself."
    show lily a_idle with dissolve
    pink "Oh, you'll have to e-mail me a picture of that."
    show lily f_laugh
    lily "Will do!"
    show lily f_normal
    show player 29 with dissolve
    player_name "E-excuse me?"
    show bridget:
        unflip
        xoffset -90
    with dissolve
    player_name "A-are you selling those?"
    show player 3
    lily "Yup, starting today, {b}you can pick one of these up{/b} from our {b}Cosplay Section{/b}."
    show player 4 with dissolve
    player_name "( Hmm, I bet that would work for {b}[jen_name]'s camshows{/b}... )"
    show bridget b_empty f_lily_lucha_hug_normal o_lily_lucha_hug_mask zorder 2:
        xoffset 0
    show lily b_hug:
        xoffset 90
    with dissolve
    show player 13
    lily "Thanks again for coming out."
    pink "My pleasure, sweetie."
    show bridget f_normal b_lucha a_hips o_mask:
        xoffset -90
    hide lily
    with dissolve
    pink "I'll see you two at schoo-"
    show bridget f_surprised
    show player 10
    player_name "Huh?"
    show player 5
    pink f_normal a_rubbing_hands "I err, meant to say..."
    pink "Stay in school!"
    pink @ f_laugh "Heh, you know... don't be a fool, stay in school!"
    pink "That's what... I was..."
    pink "... {i}*Ahem*{/i} Goodbye boys."
    hide bridget with dissolve
    show erik f_normal
    erik "Bye, {b}Pink Cyclone{/b}!"
    show erik:
        unflip
        xoffset -100
    with dissolve
    show player 10
    player_name "That was weird."
    show player 13
    erik "That was awesome!"
    erik "Check out this poster, dude!"
    erik "She's so hot!"
    show player 14
    player_name "Heh, yeah."
    show player 13
    erik "Alright, time to snag that last copy of the game."
    show player 14
    player_name "Heh, you'd better hurry."
    hide erik with dissolve
    show player 4 with dissolve
    player_name "( Hmm. )"
    player_name "( I should see about {b}buying{/b} one of those {b}replica masks{/b} for {b}[jen_name]'s camshows{/b}. )"
    hide player with dissolve
    $ player.go_to(L_comicstore)
    $ M_jenny.trigger(T_jenny_buy_mask)
    $ game.main()

label mall_eve_make_up_go_to_mall_has_chocolates_candles:
    $ player.go_to(L_mall)
    scene expression player.location.background_blur with None
    show anon
    show eve f_happy
    with dissolve
    anon "So that's candles and chocolates taken care of..."
    anon "Where to now?"
    eve @ f_sexy "Well, a romantic dinner needs wine, don't you think?"
    eve "Any idea where we can get some?"
    anon a_thinking f_thinking @ -m_talk "Hmm."
    pause
    anon "{b}Tuuku{/b}?"
    eve f_surprised "{i}*Gasp*{/i} That's a great idea, {b}[firstname]{/b}!"
    show anon f_normal a_idle with dissolve
    eve "I can talk him into it, especially after that whole drug debacle at the party!"
    anon "Alright, let's go see him."
    hide anon
    hide eve
    with dissolve
    $ M_eve.trigger(T_eve_bought_candles_chocolate)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
