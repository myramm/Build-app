label photo_booth_roxxy_take_picture:
    scene expression player.location.background
    show old_roxxy_booth 1 at right
    show old_roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "Have you ever used this thing before?"

    show player 13
    show old_roxxy 2
    roxxy "Tidak..."

    show old_roxxy 1
    roxxy "..."
    show old_roxxy 1h
    roxxy "Bagaimana penampilanku?"

    show old_roxxy 1g
    show player 29 with dissolve
    player_name "... You look pretty."

    show player 13 with dissolve
    show old_roxxy 1b
    roxxy "Saya bersedia?"

    show old_roxxy 1
    show player 14
    player_name "Ya!"

    show player 26
    player_name "You always look pretty!"

    show player 13
    show old_roxxy 4
    roxxy "..."
    roxxy "Oh, diamlah!"

    show old_roxxy 1h
    roxxy "I don't always look pretty..."

    show old_roxxy 1g
    show player 26
    player_name "Yeah, you do."

    show player 13
    show old_roxxy 1h
    roxxy "Apa pun."

    show old_roxxy 1g
    show player 5
    player_name "..."
    roxxy "..."
    show old_roxxy 1h
    roxxy "Alright, I'm getting in."

    hide old_roxxy_booth
    show old_roxxy booth 2
    with dissolve
    show player 14
    player_name "... Oke."

    show player 13
    hide old_roxxy
    show old_roxxy_booth 1 at right with dissolve
    pause
    show player 5
    player_name "..."
    show player 10
    player_name "You sure you know how to work everything?"

    show player 5
    roxxy "It's not rocket science!"

    roxxy "You just put the money in and push the button."

    show player 14
    player_name "Hehe, baiklah."

    show player 13
    show old_roxxy_booth 1 with flash
    pause
    show player 9 with dissolve
    show old_roxxy_booth 1 with flash
    pause
    show old_roxxy_booth 1 with flash
    pause
    player_name "..."
    show player 10 with dissolve
    player_name "... Are you done?"

    player_name "Did you get everything you needed?"

    show player 5
    roxxy "I just need one more picture."

    show player 10
    player_name "... Oke."

    show player 11
    hide old_roxxy_booth
    show old_roxxy booth 2 at right
    with dissolve
    roxxy "Get in here!"

    hide player
    show old_roxxy booth 3
    player_name "!!!" with hpunch
    show old_roxxy booth 4
    pause
    scene location_mall_upstairs_booth_inside
    show old_roxxy booth 5 at right with dissolve
    roxxy "Say cheese, {b}[firstname]{/b}!"

    show old_roxxy booth 6 with dissolve
    player_name "Whoa, whoa, whoa!!!"

    show old_roxxy booth 7 with dissolve
    roxxy "!!!" with hpunch
    show old_roxxy booth 7 with flash
    roxxy "What the fuck, {b}[firstname]{/b}!!"

    scene black with fade
    scene expression player.location.background
    show old_roxxy_booth 1 at right
    show old_roxxy 1 at right
    show player 10 at left
    with dissolve
    player_name "... Maaf."

    player_name "I slipped!"

    show player 5
    show old_roxxy 2
    roxxy "... Yeah, right."

    roxxy "I was just trying to give you a little reward you know..."

    show old_roxxy 68 with dissolve
    pause
    hide player
    hide old_roxxy
    show old_roxxy_picture 1
    with dissolve
    roxxy "..."
    pause
    hide old_roxxy_picture
    show old_roxxy 69 at right
    show player 5 at left
    with dissolve
    roxxy "Ha ha ha!"

    show player 13
    show old_roxxy 72
    roxxy "I guess you're getting a bigger reward than I intended..."

    show old_roxxy 1g
    show player 645
    with dissolve
    player_name "!!!"
    show player 646
    player_name "... Umm, thanks, I guess?"

    show player 645
    show old_roxxy 1h
    roxxy "Oh, c'mon..."

    roxxy "You just got a photo of your face buried in my tits."

    roxxy "What more could a nerd like you ask for?"

    show old_roxxy 1g
    show player 4 with dissolve
    player_name "..."
    show old_roxxy 2
    roxxy "Just don't hurt yourself jerking off to it..."

    show old_roxxy 1g
    show player 10 with dissolve
    player_name "I'm not gonna... I mean, I don't-"

    show player 5
    show old_roxxy 2
    roxxy "Whatever, perv!"

    show old_roxxy 3c
    roxxy "Don't show it to anybody either!"

    roxxy "If {b}Dexter{/b} finds out about that he'll kill us both!"

    show old_roxxy 1
    show player 14
    player_name "Yeah, yeah... I won't."

    show player 645 with dissolve
    show old_roxxy 1g
    roxxy "..."
    show old_roxxy 68 with dissolve
    pause
    show old_roxxy 72 with dissolve
    roxxy "Di Sini."

    show old_roxxy 1b with dissolve
    roxxy "Think that one will work for me?"

    show old_roxxy 1
    show player 646
    player_name "Yeah, I think so..."

    show player 13 with dissolve
    show old_roxxy 1b
    roxxy "Bagus."

    roxxy "Gimme a call when the ID is ready."

    show old_roxxy 1
    show player 14
    player_name "Ya baiklah."

    show player 13
    hide old_roxxy with dissolve
    player_name "( ... )"
    show player 5
    player_name "( Well, that was weird. )"

    player_name "( I fell face-first into {b}Roxxy{/b}'s boobs, and she didn't even get mad... )"

    player_name "( I should {b}get this photo to Captain Terry at the pier{/b}. )"

    hide player with dissolve
    return

label photo_booth_generic_dialogue:
    scene expression player.location.background
    show player 2
    player_name "Hmm, I don't need to take any photos right now..."

    hide player
    return

label photo_booth_first_visit:
    scene expression player.location.background
    show player 2
    player_name "Hey, I've never noticed this photo booth here before..."

    player_name "... It must be new!"

    show player 17
    player_name "Dingin!"

    hide player
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
