label park_eve_clients_park_fliers:
    scene expression player.location.background_blur with None
    show anon:
        flip
        xoffset 100
    show eve a_flyers f_happy_right:
        xoffset -200
    with dissolve
    eve "Hmm, I guess we'll just post a few on the light poles, huh?"

    anon "Yeah, that's really the only place here."

    anon @ f_worried "Unless you want to start hanging them on trees or something?"

    eve "Hehe, no... The light poles will work."

    anon "I'll get to it then."

    anna "Halo?"

    eve f_normal @ -m_talk "Hmm?"

    show anna a_flyer:
        flip
    with dissolve
    anna "You all the ones hanging these flyers?"

    eve f_happy @ f_laugh "Yup, that's us."

    anna @ f_normal_down "Are they really doing twenty percent off?"

    eve @ -m_talk "Mmhmm."

    eve @ f_normal "Only for a couple days though."

    anna "Sempurna!"

    anna "I've been thinking about getting one for a while now."

    anna "You know, like a cute little dolphin above my ankle or something?"

    eve "We can definitely do that."

    anna "Is the artist good?"

    eve @ f_laugh "Hehe, she's the best!"

    eve "I can promise you that."

    anna "Luar biasa!"

    anna "I'll head over there right away."

    anna "Thanks for the info!"

    eve "You're welcome!"

    hide anna with dissolve
    pause
    eve f_normal_right "Was it me or did she look really familiar?"

    anon f_worried "Uhh... {i}*Ahem*{/i} W-wasn't she one of the girls we saw jogging topless the other night?"

    eve f_surprised "{i}*Gasp*{/i} You're right!"

    eve f_sexy "How could I have forgotten about that?"

    pause
    eve f_happy @ f_laugh "Hehehe!"

    anon "Apa?"

    eve f_happy_right "Nothing, it's just funny is all..."

    eve @ f_confused "Who jogs topless in a park?"

    anon @ a_behind_head "Heh, no idea."

    anon "Anywhere else you wanna hang these?"

    eve f_normal_right "I dunno, there will only be a few left once we finish here..."

    show eve f_thinking_lip
    pause
    eve f_normal_right "That's probably enough, right?"

    anon f_normal "Ya, menurutku begitu."

    anon "I mean, we can always do more another day if we need to."

    eve "Ya."

    eve "Let's just finish up here and then {b}head back to the shop{/b}."

    anon "You've got it."

    hide anon
    hide eve with dissolve
    return

label park_count_night_0:
    scene expression player.location.background_blur
    show player 34 with dissolve
    player_name "..."
    show player 35
    player_name "( Didn't {b}Eve{/b} mention she liked the park? )"

    show player 14
    player_name "( She's probably around here somewhere. )"

    hide player with dissolve
    return

label park_take_picture_judith:
    call expression game.dialog_select("park_take_picture_judith_pre")
    if player.has_picked_up_item("master_key"):
        call expression game.dialog_select("park_take_picture_judith_have_master_key")
    else:

        call expression game.dialog_select("park_take_picture_judith_do_not_have_master_key")

    $ M_okita.trigger(T_okita_picture_taken)
    $ game.main()
    return

label park_take_picture_judith_pre:
    scene expression player.location.background_closeup
    show player 1 at left
    show old_judith 5 at right
    with dissolve
    judith "You really came!"

    show player 2
    show old_judith 4
    player_name "I told you I would."

    show player 1
    show old_judith 5
    judith "This is wonderful! I can't tell you how much this means to me."

    show player 2
    show old_judith 4
    player_name "It's no problem, {b}Judith{/b}."

    player_name "Apa yang perlu saya lakukan?"

    show player 1
    show old_judith 5
    judith "... Just, come sit next to me."

    show player 2
    show old_judith 4
    player_name "Baiklah."


    scene location_park_bench_closeup2
    show playerf 2 zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show old_judithf 4 zorder 0 at Position(xpos=0.695, ypos=1.0)
    show old_judithfa 3 zorder 1 at Position(xpos=0.6645, ypos=0.635)
    with fade
    player_name "Seperti ini?"

    show playerf 2b
    show old_judithf 5
    judith "No, silly."


    scene location_park_bench_closeup3
    show playerf 2f zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show old_judithf 8 zorder 0 at Position(xpos=0.665, ypos=1.0)
    show old_judithfa 4 zorder 1 at Position(xpos=0.725, ypos=0.4375)
    show old_juditho 1 zorder 4 at Position(xpos=0.5065, ypos=0.639)
    with dissolve
    judith "Like this!"

    judith "Smile!"


    scene location_park_bench_cutscene
    show text _ ("I'm not sure how this picture was supposed to help {b}Judith{/b}?") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... But it seemed like a small price to pay for the lenses {b}Miss Okita{/b} wanted, though.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Plus it made {b}Judith{/b} really happy!") as caption with dissolve
    pause

    scene location_park_bench_closeup2
    show playerf 2f zorder 2 at Position(xpos=0.4125, ypos=1.01)
    show playerfa 1 zorder 3 at Position(xpos=0.394, ypos=0.736)
    show old_judithf 6 zorder 0 at Position(xpos=0.695, ypos=1.0)
    show old_judithfa 2 zorder 1 at Position(xpos=0.67, ypos=0.7275)
    with fade
    judith "This is perfect!"

    show old_judithf 5
    judith "Thank you so much, {b}[firstname]{/b}!"

    show playerf 2
    show old_judithf 4
    player_name "Tidak masalah."

    show playerf 2c
    player_name "So about that spare set of glasses..."

    show old_judithf 2
    show old_judithfa 1 at Position(xpos=0.67, ypos=0.76) with dissolve
    show playerf 2b
    judith "Ohh, of course!"

    judith "I keep them in my locker at school."

    show old_judithf 3
    judith "I can write down the combination for you, just one second."

    show playerf 2c
    show old_judithf 1
    player_name "That's alright, I don't need the combination."

    return

label park_take_picture_judith_have_master_key:
    show playerf 2b
    show old_judithf 2
    judith "Kamu tidak?"

    show playerf 2c
    show old_judithf 1
    player_name "I have a master key to all the lockers."

    show playerf 2b
    show old_judithf 5
    judith "Really?! How did you manage to get that?"

    show playerf 2c
    show old_judithf 4
    player_name "Heh, I have my ways."

    show playerf 2b
    show old_judithf 5
    judith "That's so awesome!"

    judith "I had no idea you were such a bad boy!"

    show playerf 2c
    show old_judithf 4
    player_name "Uhh, yeah. Heh, I guess..."

    player_name "Thanks for the help, {b}Judith{/b}. I'll see you around."

    show playerf 2b
    show old_judithf 5
    judith "Thank you, {b}[firstname]{/b}! See you soon!"

    return

label park_take_picture_judith_do_not_have_master_key:
    show playerf 2b
    show old_judithf 2
    judith "Kamu tidak?"

    show playerf 2c
    show old_judithf 1
    player_name "I know where {b}Mrs. Smith keeps her master key{/b}..."

    show playerf 2b
    show old_judithf 5
    judith "Really?! You're going to steal the Principal's key?"

    show playerf 2c
    show old_judithf 4
    player_name "Steal?! I dunno about that... I just wanna borrow it 'til they get me a new lock."

    show playerf 2b
    show old_judithf 5
    judith "That's so awesome!"

    judith "I had no idea you were such a bad boy!"

    show playerf 2c
    show old_judithf 4
    player_name "Uhh, yeah. Heh, I guess..."

    player_name "Thanks for the help, {b}Judith{/b}. I'll see you around."

    show playerf 2b
    show old_judithf 5
    judith "Thank you, {b}[firstname]{/b}! See you soon!"

    return

label coin_dialogue:
    show expression "objects/closeup_coin_01.png" at Position(xalign = 0.5, yalign = 1.0)
    with dissolve
    player_name "Hah?"

    player_name "Itu terlihat seperti koin yang sangat tua."

    player_name "Just look at these odd {b}symbols{/b}!"

    player_name "Saya harus menyimpannya. Mungkin itu sesuatu yang berharga?"

    hide expression "objects/closeup_coin_01.png" with dissolve
    $ player.get_item("weird_coin")
    call popup ('give', 'weird_coin')
    $ player.location.call_screen(False, False)

label park_pilly_button_dialogue:
    scene park_bench
    show player 90 at Position (xpos=400)
    show player_outfit bb 638e at Position (xpos=400)
    show clyde 2 at left
    with dissolve
    clyde "Ah, dere he is!"

    clyde "You just let me do the talkin' now!"

    show clyde 1
    show pilly f_angry with dissolve
    buyer "... {b}Clyde{/b}?"

    show clyde 4 with dissolve
    clyde "Oh, uhh... How's it goin' dere, {b}Pilly{/b}..."

    show clyde 3
    show player 10
    player_name "{b}Pilly{/b}?"

    player_name "What kind of name is that?"

    show player 5
    pilly "Permisi?!"

    show clyde 22 with dissolve
    clyde "Shhhh, don't say nothin' 'bout his name..."

    clyde "He's sensitive."

    show clyde 2
    clyde "Uhh, don't mind him, {b}Pilly{/b}. How 'bout a smoke afore we get down to business?"

    show clyde 1
    pilly @ -m_talk "..."
    pilly f_normal "I quit."

    show clyde 22
    clyde "Sungguh?!"

    clyde "... You know, nobody likes a quitter, {b}Pilly{/b}."

    show clyde 21
    pilly "Yeah, well... I got an offer I couldn't refuse."

    pilly "Where's {b}Crystal{/b}?"

    show clyde 22
    clyde "I'm afraid mah auntie is otherwise occupied."

    show clyde 21
    pilly @ -m_talk "..."
    pilly "Well, that's a shame, your auntie usually offers to sweeten the deal."

    pilly f_angry "Who is this gentleman?"

    show player 11
    player_name "..."
    show clyde 2
    clyde "Ah, well... This 'ere's my newest associate."

    clyde "You can call him... Err..."

    clyde "... {b}Mr. White{/b}!"

    show clyde 1
    show player 18
    pilly @ -m_talk "..."
    pilly "Somethin' fishy is going on here and I don't like it, {b}Clyde{/b}."

    show clyde 2
    clyde "Now, now... Ain't no funny business!"

    show player 90
    show clyde 28 with dissolve
    clyde "I brought the merchandise just like we agreed..."

    clyde "Have a look fer yerself!"

    show clyde 1
    show pilly a_meth_look f_down
    with dissolve
    pilly f_normal a_meth @ a_meth_look f_down "Hmm, this is a lot more than we discussed over the phone."

    show clyde 2
    clyde "Well, ya see, I'm having a little goin' outta business sale."

    clyde "I'll give ya the entire lot for one hundred thousand dollars!"

    show clyde 1
    pilly @ -m_talk "..."
    pilly "Heh, how exactly did you arrive at that number?"

    show clyde 26
    clyde "That's five pounds of mah finest stuff right dere!"

    clyde "It's worth every penny!"

    show clyde 25
    pilly @ -m_talk "..."
    pilly "I think not."

    pilly "I'll give you sixty thousand."

    show clyde 26
    clyde "Pfft, are you outta yer damn mind?!"

    clyde "You ain't takin' advantage of me!"

    show clyde 25
    pilly f_angry "Cocokkan dirimu."

    show clyde 27
    show pilly a_idle
    with dissolve
    pilly "Semoga beruntung!"

    show clyde 28
    clyde "Well, hold on now!"

    show clyde 22
    show pilly a_meth
    with dissolve
    clyde "Don't do nuthin' drastic, we just hagglin' here!"

    show clyde 26
    clyde "Seventy-five!"

    show clyde 25
    show player 12
    player_name "We'll take the sixty thousand dollars."

    show player 90
    show pilly f_normal
    show clyde 22
    clyde "{i}WHAT{/i}?!" with hpunch
    show clyde 26
    clyde "Now you listen here!"

    show clyde 25
    show player 12
    player_name "Shut up, {b}Clyde{/b}!"

    show clyde 21
    player_name "Don't forget why we're here!"

    show player 90
    clyde "..."
    show clyde 22
    clyde "Bagus."

    show clyde 21
    pilly "Heh, nice to see your \"associate\" is a reasonable man."

    pilly @ a_money "Pleasure doing business with you, {b}Mr. White{/b}."

    show player 638b
    show player_outfit 638d
    with dissolve
    pause
    show player 638
    show player_outfit 638c
    with dissolve
    player_name "Y-yeah... Thanks."

    show player 638b
    show player_outfit 638d
    hide pilly
    with dissolve
    show clyde 22
    clyde "... Man, he just bent us over the barrel with dat deal!"

    show clyde 21
    show player 12f at Position (xpos=700)
    show player_outfit 638ef at Position (xpos=700)
    with dissolve
    player_name "C'mon, let's get out of here!"

    show player 90f
    show clyde 22
    clyde "Well, hold on now!"

    clyde "What about mah cut?"

    show clyde 21
    show player 10f
    player_name "Hah?"

    show player 5f
    show clyde 2
    clyde "We gonna split that money fifty-fifty, ain't we?!"

    show clyde 1
    show player 12f
    player_name "Tidak!"

    player_name "This is to get your aunt outta jail!"

    player_name "... Remember?!"

    show player 90f
    show clyde 2
    clyde "Well, ya but..."

    clyde "Can't we just take a lil' bit to the strip club or somethin'?"

    clyde "You could buy a whole lot of lap dances with that kind of money..."

    show clyde 1
    show player 12f
    player_name "... Get your ass home and start writing that letter!"

    show player 90f
    show clyde 26
    clyde "Baiklah baiklah."

    clyde "Sheesh, you're a real party pooper, you know dat?"

    show clyde 31 with dissolve
    clyde "Besides, I dun wrote yer stupid letter!"

    hide clyde
    hide player
    hide player_outfit
    show expression "objects/closeup_clyde_note_01.png"
    with dissolve
    pause
    hide expression "objects/closeup_clyde_note_01.png"
    show player 13f at Position (xpos=700)
    show player_outfit bb 638ef at Position (xpos=700)
    show clyde 1 at left
    with dissolve
    player_name "..."
    show player 14f
    player_name "Yeah, that should work."

    show player 13f
    show clyde 2
    clyde "Bagus."

    clyde "I'm glad dis mess is all over with!"

    show clyde 1
    show player 10f
    player_name "You'd better disappear quickly if you don't wanna end up in prison."

    player_name "{b}Roxxy{/b} and I will {b}turn this into the police tomorrow{/b}."

    show player 5f
    show clyde 4 with dissolve
    clyde "Oh, dun you worry none."

    clyde "I'll be long gone by then, buddy!"

    clyde "You just take real good care mah cousin now!"

    show clyde 3
    player_name "..."
    hide clyde with dissolve
    pause
    show player 14f
    player_name "I should {b}take the letter to Roxxy tomorrow at school{/b}."

    hide player
    hide player_outfit
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
