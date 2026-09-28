label button_cedric_about_jenny:
    show player 10
    player_name "You know she's been trying to get a hold of you, right?"
    show player 5
    show cedric
    cedric "Yeah, believe me... I know."
    cedric "I don't want anything to do with that crazy bitch!"
    show player 12
    player_name "That's a little harsh."
    show player 5
    cedric "You know she's gotten herself into doing porn or something?"
    show player 10
    player_name "Y-yeah, I know."
    show player 5
    cedric "Now she's trying to sweet talk me into doing it too!"
    show player 10
    player_name "Uh huh?"
    show player 5
    cedric "Do I look like the kinda guy who does porn?!"
    show player 29 with dissolve
    player_name "Err, I dunno... Kinda?"
    show player 3
    cedric "Yeah, well... I ain't!"
    cedric "She just needs to find someone else to sink her talons into."
    cedric "I'm done with her."
    show player 5 with dissolve
    player_name "..."
    show player 10
    player_name "Will you at least call and tell her that?"
    show player 5
    cedric "Why, so she can yell and call me names?"
    cedric "No thanks."
    cedric "You tell her."
    hide cedric with dissolve
    pause
    show player 37 with dissolve
    player_name "{i}*Sigh*{/i} Crap."
    player_name "( {b}[jen_name]{/b} isn't going to like this... )"
    player_name "( I'd better go and let her know. )"
    hide player with dissolve
    return

label button_cedric_see_ya:
    show player 14
    player_name "I should get going."
    show player 13
    show cedric f_normal
    cedric "Yeah, alright."
    cedric "See you around, little buddy."
    hide player with dissolve
    pause
    cedric "Don't go skipping leg day now, heh!"
    hide cedric with dissolve
    return

label button_cedric_can_you_spot_me:
    show player 10
    player_name "Can you spot me?"
    show player 13
    show cedric f_normal a_reject with dissolve
    cedric "No can do, little buddy."
    show player 5
    cedric "You're not ready to workout with the big boys yet."
    show cedric a_idle with dissolve
    player_name "..."
    show cedric a_point with dissolve
    cedric "I don't wanna see you drop a nut or blow out your o-ring."
    show cedric a_idle with dissolve
    show player 10
    player_name "Uh huh, thanks for nothing."
    show player 5
    cedric "Aww, no need to get sore about it."
    cedric "You'll get there soon enough."
    cedric "Check this out!"
    show cedric a_flex with dissolve
    show player 13
    pause
    cedric "I'm getting pretty ripped, huh?"
    show player 14
    player_name "Sure, {b}Cedric{/b}..."
    show player 13
    show cedric a_idle with dissolve
    cedric "Heh, oh yeah!"
    return

label button_cedric_what_have_you_been_up_to:
    show player 14
    player_name "What have you been up to?"
    show player 13
    show cedric f_normal
    cedric "Oh, things have been great!"
    cedric "Since I finally got that harpy roommate of yours off my back, I can finally focus on my workouts."
    show player 4
    player_name "Huh."
    show player 14 with dissolve
    player_name "Well, that's good... I guess."
    show player 13
    cedric "It's real good, little buddy!"
    show cedric a_point_himself with dissolve
    cedric "You wanna come watch me do some dead lifts?"
    cedric "I'm up to four hundred and five pounds!"
    show cedric a_idle with dissolve
    show player 29 with dissolve
    player_name "Ehh, maybe some other time..."
    show player 13 with dissolve
    cedric "Suit yourself."
    return

label button_cedric_intro_repeat:
    scene expression player.location.background_closeup with None
    show player 13 at left
    show cedric
    cedric "What's up, little buddy?"
    show player 14
    player_name "Oh, hey {b}Cedric{/b}."
    show player 13
    cedric "You here to bulk up?"
    return

label button_cedric_intro_first:
    scene expression player.location.background_closeup with None
    show cedric
    show player 13 at left
    cedric "Whoa, {b}[firstname]{/b}?"
    show player 14
    player_name "Oh, hey {b}Cedric{/b}."
    show player 13
    cedric "I haven't seen you for a while, little buddy."
    show player 14
    player_name "Uh huh."
    show player 13
    show cedric a_point with dissolve
    cedric "You finally decide to hit the gym and bulk up?"
    show cedric a_idle with dissolve
    show player 29 with dissolve
    player_name "Y-yeah, something like that..."
    show player 13 with dissolve
    cedric "How's {b}[jen_name]{/b}?"
    show player 12
    player_name "Umm, I dunno... Bitchy?"
    show player 13
    cedric "Hahaha, good one!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
