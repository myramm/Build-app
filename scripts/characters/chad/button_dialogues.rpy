label button_chad_get_eve_drawing_first:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad
    with dissolve
    player_name "Hey man, I'm trying to find {b}Eve's art pad{/b}."

    player_name "She said you might have it."

    show player 1
    chad "Ya itu benar."

    show player 10
    player_name "So, could I get it from you?"

    show player 11
    chad @ a_open "Tch, not for free, yo."

    player_name "..."
    show player 10
    player_name "Apa yang kamu inginkan?"

    show player 11
    chad f_happy "Man, {b}Eve{/b}'s a pretty dope artist, you know what I'm sayin'?"

    show player 10
    player_name "Yeah, so I hear."

    show player 11
    chad "She's got this one drawin'..."

    chad "Shit is lit as fuck, man!"

    chad "I thought it would be in her art pad but no dice."

    chad @ a_open "You gotta {b}get me that drawin'{/b}, dawg!"

    show player 10
    player_name "... And if I do, you'll give me the {b}art pad{/b}?"

    show player 11
    chad @ f_laugh "Haaah, that's the deal, yo."

    chad "You down?"

    show player 10
    player_name "Sure. What's the drawing look like?"

    show player 11
    chad "Ah, it's this self-portrait she did."

    chad "S'pose to be like an anime girl or somethin'."

    chad @ a_open "All I know is... It's fuckin' sexy, yo!"

    show player 10
    player_name "Any idea where it could be?"

    show player 11
    chad f_normal "Mmm, man if I had to guess..."

    chad "I betcha she's keepin' that shit {b}in her locker{/b}."

    show player 2
    player_name "Alright, I'll go take a look."

    show player 1
    chad "Hurry back, man."

    return

label button_chad_get_eve_drawing:
    scene location_school_right_hall_day_blur
    show player 10 at left
    show chad
    with dissolve
    player_name "What did you want for that {b}art pad{/b} again?"

    show player 11
    chad "You forget or somethin'?"

    show player 10
    player_name "Yeah, kinda."

    show player 11
    chad "Tch, I want that self-portrait {b}Eve{/b} did."

    chad @ a_open "She's probably got it under wraps {b}in her locker{/b}, know what I'm sayin'?"

    show player 10
    player_name "Baiklah."

    return

label button_chad_get_eve_drawing_completed:
    scene location_school_right_hall_day_blur
    show player 1 at left
    show chad
    with dissolve
    chad "'Ey, man. Did you get it?"

    show player 612 with dissolve
    player_name "Yeah, you were right. It's pretty sexy..."

    show player 611
    chad f_happy "Lemme see that shit!"


    $ player.remove_item("eve_drawing")
    show player 1
    show chad f_happy_down a_paper
    with dissolve
    pause
    chad "Doooope!"

    chad "Damn! Now that's a woman, yo!"

    show player 2
    player_name "Can I have that {b}art pad{/b} now?"

    show player 1
    chad f_normal "Ah, yeah. My bad! I'm all over here droolin' and shit!"

    chad a_pad "Ini dia."

    show player 598
    show chad a_paper f_happy_down
    with dissolve
    player_name "Thanks, {b}Chad{/b}."

    show player 596
    chad "Pleasure doin' business with ya."

    hide chad
    hide player
    with dissolve
    call popup ('give', 'art_pad')
    return

label button_chad_generic:
    scene location_school_right_hall_day_blur
    show player 2 at left
    show chad
    with dissolve
    player_name "Hey, what's up, man?"

    show player 1
    chad @ f_angry "Damn it, {b}[firstname]{/b}! Can't you see I'm practicing my rhymes here, dawg!"

    show player 10
    player_name "Uhh, okay?"

    show player 11
    chad "What do you want anyways?"

    return

label button_chad_nothing:
    show player 2
    show chad
    player_name "Just thought I'd say hello."

    show player 1
    chad f_angry "Beat it, yo."

    show player 11
    chad "I'm struggling with some serious shit right now."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
