label basketball_court_dexter_start:
    scene basketball_b
    show player 5 at left
    show old_dexter 3 at right
    with dissolve
    dexter "Apa yang kamu lakukan di sini?"

    show old_dexter 1
    show player 12
    player_name "Why do you care? Maybe I'm just here to practice."

    show player 11
    show old_dexter 3
    dexter "Hah!"

    dexter "That's a good one!"

    show old_dexter 1
    show player 25
    player_name "{i}*Huh*{/i}"

    show player 12
    player_name "What do you want, {b}Dexter{/b}?"

    show player 5
    show old_dexter 6 with dissolve
    dexter "Just stay away from my court, understood?"

    hide old_dexter with dissolve
    show player 24
    player_name "..."
    hide player with dissolve
    return

label basketball_court_roxxy_dexter_argument:
    scene basketball_b
    show old_roxxy 3f at left
    show old_dexter 2 at right
    with dissolve
    roxxy "How can you be so stupid?!"

    show old_roxxy 3bf
    show old_dexter 6 with dissolve
    dexter "Don't call me stupid!"

    show old_dexter 2
    show old_roxxy 3f
    roxxy "You had one job to do."

    roxxy "I said, \"Get me his homework.\""

    roxxy "Isn't that what I said?"

    show old_roxxy 3df
    show old_dexter 8
    dexter "Ya, tapi..."

    show old_dexter 2
    show old_roxxy 3f
    roxxy "Shut up, stupid! I'm talking!"

    roxxy "So you find him."

    roxxy "You beat the crap out of him."

    roxxy "... And then you leave without getting the homework!"

    show old_roxxy 3df
    show old_dexter 4 with dissolve
    dexter "Well, I punched him and his glasses broke."

    show old_dexter 3 with dissolve
    dexter "It was funny..."

    dexter "So I was laughing, and he was crying, and I guess... I just sorta forgot."

    show old_dexter 1
    show old_roxxy 3f
    roxxy "Well, what am I supposed to do?!"

    roxxy "I don't have anything to turn for the {i}French bitch{/i}'s class!"

    show old_roxxy 3bf
    show old_dexter 3
    dexter "That's not my problem!"

    dexter "Why don't you steal the homework yourself?!"

    show old_dexter 1
    show old_roxxy 30f
    roxxy "Grr, I told you, I can't do it myself!"

    roxxy "You never listen!"

    show old_roxxy 3f
    show old_dexter 2
    roxxy "You're so STUPID!"

    show old_roxxy 3bf
    show old_dexter 8
    dexter "Stop calling me stupid, {b}Roxxy{/b}!"

    show old_dexter 2
    show old_roxxy 31f
    roxxy "... YOU'RE STUPID!"

    show old_roxxy 3bf
    show old_dexter 4
    dexter "THAT'S IT!!!" with hpunch
    dexter "I'm done with this!"

    show old_dexter 6 with dissolve
    dexter "It's always, \"{b}Dexter{/b} do this.\" or \"{b}Dexter{/b} do that.\""

    dexter "... And what do I get?"

    dexter "Called stupid."

    dexter "Well, screw you {b}Roxxy{/b}!"

    dexter "No more favors!"

    dexter "No more car rides!"

    dexter "No more beer!"

    show old_dexter 8 with dissolve
    dexter "... And no more favors!"

    show old_dexter 2
    show old_roxxy 3cf
    roxxy "You said that one already..."

    show old_roxxy 3f
    roxxy "... Stupid."

    show old_roxxy 3bf
    show old_dexter 6 with dissolve
    dexter "Rrraahhh, FUCK YOU!"

    dexter "I'm leaving!"

    hide old_dexter with dissolve
    show old_roxxy 3f
    roxxy "... Yeah, well, see if I care!"

    hide old_roxxy with dissolve
    pause 1
    show player 13 at left
    show eve f_happy
    with dissolve
    eve "Wah!"

    eve "That was a good show!"

    show player 10
    player_name "Hehe, ya."

    show player 5
    player_name "..."
    eve f_normal "Ada apa?"

    show player 10
    player_name "I can't believe I'm about to say this but..."

    player_name "I kinda feel sorry for {b}Dexter{/b}."

    show player 5
    eve f_confused "eh..."

    eve "Don't say that."

    eve "He's an asshole!"

    show eve f_normal
    show player 10
    player_name "Ya, saya tahu."

    show player 5
    eve "Did you miss the part where he broke some poor kids glasses for no reason other than he thought it was funny?"

    show player 14
    player_name "... You're right."

    player_name "He deserves a bit of misery, doesn't he?"

    show player 13
    eve "Yeah, he does."

    eve "C'mon, we should get to class."

    hide player
    hide eve
    with dissolve
    return

label basketball_court_bissette_get_books:
    scene basketball_b
    show old_dexter 2 at right
    show player 10 at left
    with dissolve
    player_name "Hei, umm, {b}Dexter{/b}..."

    show player 5
    show old_dexter 3
    dexter "Apa yang kamu inginkan, twerp?"

    show old_dexter 1
    show player 10
    player_name "I was hoping you still had the library book you checked out..."

    show player 5
    show old_dexter 8
    dexter "Buku perpustakaan?"

    show old_dexter 6 with dissolve
    show player 11
    dexter "Do I look like the kinda guy who would be reading library books?"

    dexter "... What do you think I'm some kinda nerd like you and your douchebag ginger friend?"

    show old_dexter 2 with dissolve
    show player 10
    player_name "What? No, I didn't..."

    show player 11
    show old_dexter 4 with dissolve
    dexter "You better get outta here, {b}[firstname]{/b}, before I feed you a knuckle sandwich!"

    show old_dexter 2 with dissolve
    show player 12
    player_name "Baiklah, baiklah, aku berangkat!"

    hide old_dexter with dissolve
    show player 10f at center with dissolve
    player_name "Saya ingin tahu apakah pustakawan melakukan kesalahan?"

    show player 5f
    player_name "..."
    show player 12f
    player_name "Dia bisa saja berbohong. {b}Saya harus memeriksa lokernya{/b}!"

    player_name "Mudah-mudahan ada di sana, jika tidak, saya tidak tahu apa yang harus saya lakukan..."

    hide player with dissolve
    return

label basket_ball_court_take_magazines:
    if player.location.is_here(M_dexter):
        if not M_ross.get("take porno fail"):
            call expression game.dialog_select("basketball_court_ross_magazines_intro")
        else:

            call expression game.dialog_select("basketball_court_ross_magazines_retry")

        if player.has_required_dex(3):
            $ display.toast(dex_pass)
            call expression game.dialog_select("basketball_court_ross_magazines_dex_pass")
            call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining"))
            $ M_ross.set("magazine dexter", True)
        else:

            $ display.toast(dex_fail)
            call expression game.dialog_select("basketball_court_ross_magazines_dex_fail")
            $ M_ross.set("take porno fail", True)
    $ game.main()

label basketball_court_ross_magazines_intro:
    scene basketball_b
    show player 579
    with dissolve

    player_name "Looks like somebody left a few magazines sitting here..."

    show player 579c
    player_name "( Whoa!!! )"

    player_name "( These are naughty magazines! )"

    becca "What are you doin-"

    hide player
    show player 578 at left
    show old_becca 2bf zorder 1 at right
    with dissolve
    becca "EEEEWWWWW!!!"

    show old_becca 2f
    becca "Are you just walking around with those, you perv?!"

    show player 579
    show old_becca 1f
    player_name "What?! No! I just found these..."

    show player 578
    show old_becca 2bf
    becca "Whatever. You're disgusting!"

    show old_dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0) with dissolve
    dexter "What's going on over here?!"

    show old_dexter 24
    dexter "This twerp bothering you, {b}Becca{/b}?"

    show old_dexter 23
    show old_becca 2bf
    becca "He's walking around with porno mags like a total sleazeball!"

    show old_dexter 21
    show old_becca 1f
    show player 579
    player_name "No! Seriously, they were just laying here."

    show player 578
    show old_dexter 22
    dexter "You're grossing out {b}Roxxy{/b}'s friend, little man."

    hide player
    hide old_dexter
    show old_becca 2bf
    show old_dexter 25_26
    with dissolve
    dexter "I think I'd better take those away before you make her sick!"

    return

label basketball_court_ross_magazines_retry:
    scene basketball_b
    show player 578 at left
    show old_dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0)
    show old_becca 1f zorder 1 at right
    with dissolve
    dexter "Back for more, huh?!"

    show old_dexter 23
    show old_becca 2bf
    becca "So gross..."

    show old_dexter 22
    show old_becca 1f
    dexter "I guess you need another lesson."


    hide player
    hide old_dexter
    show old_becca 2bf
    show old_dexter 25_26
    with dissolve
    dexter "Hand them over, twerp!"

    return

label basketball_court_ross_magazines_dex_pass:
    show old_dexter 26b at Position(xpos=0.55, ypos=1.0) with dissolve
    player_name "Get off me you freakin' meathead!"

    hide old_dexter
    show player 38 at left
    show old_dexter 22 zorder 0 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    dexter "Hey! Get over here and let me punch you!"

    show player 15
    show old_dexter 21
    player_name "You gotta catch me first! You giant... DOUCHE-NOZZLE!"


    hide player with dissolve
    show old_becca 4f
    show old_dexter 23
    becca "Pffft, hahahaha!"

    show old_dexter 22
    dexter "You think you're smart 'cause you know big words?!"

    show old_dexter 22 at Position(xpos=0.45, ypos=1.0) with dissolve
    show old_becca 1f
    dexter "Get back here!"

    hide old_dexter with dissolve
    show old_becca 4f
    becca "... Douche-nozzle! Hahahah!"

    hide old_becca
    return

label basketball_court_ross_magazines_dex_fail:
    show old_becca 1f
    player_name "Hey, lemme go you big lummox!"

    dexter "Hand over the magazines, twerp!"

    hide old_dexter
    show old_dexter 27 with dissolve
    player_name "Fine! Take em!"


    show player 16 at left
    show old_dexter 22 at Position(xpos=0.65, ypos=1.0)
    with dissolve
    dexter "Itulah yang saya pikirkan!"

    dexter "Now beat it before I beat you!"


    show player 15
    show old_dexter 21
    player_name "Grr, you're such an asshole!"

    hide player
    show old_dexter 28
    show old_becca 4f
    with dissolve
    dexter "Yeah, that's right, sissy boy! Run away!"

    return

label basketball_court_roxxy_dexter_alcohol_fight:
    scene basketball_b
    show old_dexter 2 at right
    show old_becca 1 at Position(xpos=315)
    show old_missy 2b at left
    show old_roxxy 30f at Position (xpos=500)
    with dissolve
    roxxy "You seriously won't get us booze?!"

    show old_roxxy 29f
    show old_dexter 8
    dexter "Not unless you apologize!"

    show old_dexter 2
    show old_roxxy 30f
    roxxy "Lupakan!"

    show old_roxxy 29f
    show old_becca 2
    becca "C'mon {b}Roxxy{/b}, just apologize..."

    becca "... The party is gonna suck without alcohol."

    show old_becca 1
    show old_roxxy 30f
    roxxy "Mustahil!"

    roxxy "He's acting like a big baby."

    show old_roxxy 29f
    show old_dexter 8
    dexter "Oh, first I'm stupid and now I'm a baby..."

    dexter "... Which is it, {b}Roxxy{/b}?"

    show old_dexter 2
    show old_roxxy 3bf
    roxxy "..."
    show old_roxxy 30f
    roxxy "Both!"

    roxxy "You're a {i}BIG STUPID BABY{/i}!"

    show old_roxxy 29f
    show old_missy 6
    missy "Pfft, hahaha!"

    show old_missy 3
    show old_dexter 8
    dexter "What the fuck are you laughing at, {b}Missy{/b}?!"

    show old_dexter 2
    show old_missy 2b
    missy "..."
    show old_missy 2
    missy "T-tidak ada."

    missy "Erm, I mean, I'm not-"

    pause
    missy "M-my bad."

    show old_missy 2b
    show old_dexter 3 with dissolve
    dexter "If you want alcohol so bad, why don't you go ask your drunk-ass mom?"

    show old_dexter 1
    show old_roxxy 2bf
    roxxy "!!!"
    show old_roxxy 30f
    roxxy "Fuck you!!"

    roxxy "Kamu tahu apa?!"

    roxxy "That's it, I'm done with you!"

    show old_roxxy 29f
    show old_dexter 8
    dexter "Yeah, well, that's fine!"

    show old_dexter 2
    show old_roxxy 3c with dissolve
    roxxy "C'mon, girls."

    roxxy "Let's ditch this stupid asshole!"

    hide old_roxxy with dissolve
    show old_becca 2b
    becca "Ugh."

    show old_becca 2f at Position(xpos=315) with dissolve
    becca "{b}Roxxy{/b}, what are we gonna do for drinks?!"

    hide old_becca
    hide old_missy
    show old_missy 3f at Position(xpos=250)
    with dissolve
    missy "..."
    show old_missy 3 with dissolve
    missy "..."
    show old_dexter 6 with dissolve
    dexter "What are you looking at, you skinny skank?!"

    show old_dexter 2
    show old_missy 4c
    with dissolve
    missy "Eep!"

    hide old_missy with dissolve
    dexter "..."
    show old_dexter 4 with dissolve
    dexter "Grr, I need to punch something!"

    hide old_dexter with dissolve
    pause
    show player 13 at left
    show eve f_laugh a_wtf
    with dissolve
    eve "Damn, that was harsh!"

    show eve f_happy a_idle
    show player 14
    player_name "Yeah, I feel bad for whoever crosses his path right now."

    show player 13
    eve "For real."

    eve "C'mon, we should get back to {b}Miss Bissette{/b}'s class."

    hide eve
    hide player
    show player 4
    with dissolve
    player_name "( ... )"
    player_name "( Yeah, it looked like {b}Roxxy{/b} was headed that way too. )"

    player_name "( Maybe I should {b}talk to her about this{/b}? )"

    scene black with fade
    return

label basketball_court_roxxy_basketball_challenge:
    scene basketball_b
    show player 90 at left
    show old_dexter 32 at right
    with dissolve
    dexter "You ready for the rematch, loser?!"

    show old_dexter 31
    show player 12
    player_name "You're going down this time, {b}Dexter{/b}."

    show player 90
    show old_dexter 3
    dexter "Ha ha ha!"

    dexter "Ya benar."

    show player 647
    show old_dexter 33
    with dissolve
    dexter "Your ball, bitch!"

    show old_dexter 11 at Position (xoffset=2) with dissolve
    show player 648 with dissolve
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
