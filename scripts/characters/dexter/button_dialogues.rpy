label button_dexter_talent_show:
    show old_dexter 1
    show player 10
    player_name "Hey {b}Dexter{/b}, you play any instruments?"
    show player 5
    show old_dexter 2
    dexter "Huh?"
    show player 12
    player_name "I-N-S-T-R-U-M-E-N-T-S. You know, like for music... Do you play any?"
    show player 5
    show old_dexter 8
    dexter "Do I look like some kinda band geek to you?!"
    show old_dexter 2
    show player 12
    player_name "Ehh, no? I just thought maybe you had a hidden talent for banging the drums or something?"
    show player 5
    show old_dexter 6 with dissolve
    dexter "I'd like to bang on your stupid face with my fists..."
    dexter "You think that would make some music?"
    show old_dexter 5
    show player 29 with dissolve
    player_name "Heh, I was just leaving..."
    show player 3
    show old_dexter 4 with dissolve
    dexter "Yeah, you better!"
    return

label button_dexter_challenge:
    show player 12
    player_name "I'm here to challenge you, {b}Dexter{/b}."
    show player 5
    show old_dexter 3
    dexter "Haha!"
    dexter "To what?!"
    show old_dexter 1
    show player 10
    player_name "To uh..."
    show player 5
    show old_dexter 3
    dexter "You know I'd beat you at anything."
    show old_dexter 4 with dissolve
    dexter "Now fuck off before I decide to beat the shit out of you."
    return

label button_dexter_library_book:
    show player 10
    player_name "Hey, umm, {b}Dexter{/b}..."
    show player 5
    show old_dexter 3
    dexter "What do you want, twerp?"
    show old_dexter 1
    show player 10
    player_name "Did you remember where you left the library book you checked out..."
    show player 5
    show old_dexter 8
    dexter "Library book?"
    show old_dexter 4 with dissolve
    dexter "Didn't I tell you to get outta here, {b}[firstname]{/b}?"
    dexter "Or do you want a knuckle sandwich!"
    show old_dexter 2 with dissolve
    show player 12
    player_name "Alright, alright, I'm going!"
    hide old_dexter with dissolve
    show player 10f at center with dissolve
    player_name "I wonder if the librarian made a mistake?"
    show player 5f
    player_name "..."
    show player 12f
    player_name "He could be lying. {b}I should check his locker{/b}!"
    player_name "Hopefully it's in there, otherwise, I dunno what I'm gonna do..."
    return

label button_dexter_nothing:
    show player 10
    player_name "I... Uhh... Didn't mean to bother you."
    player_name "I need to get to class."
    show player 5
    show old_dexter 3
    dexter "Run along, loser."
    return

label dexter_button_pushups:
    show player 16 at left
    show old_dexter 12 at right
    with dissolve
    dexter "Oh, you want a rematch huh?"
    dexter "No problem, nerd!"
    dexter "I'll show you how it's done!"
    show old_dexter 11
    scene gym
    show player 16 at left
    show old_dexter 11 at right
    with dissolve
    bridget "Alright, boys. You know the drill!"
    bridget "Last man standing wins!"
    show old_dexter 12
    dexter "Hahaha, watch and learn... NERD!"
    hide player
    hide old_dexter
    with dissolve
    bridget "GO!"
    return

label dexter_button_pushups_rematch:
    show player 5 at left
    show old_dexter 15 at right
    with dissolve
    dexter "How about a rematch, nerd?!"
    show old_dexter 14
    show player 12
    player_name "What?! C'mon, man... You lost."
    player_name "Just move on."
    show player 5
    show old_dexter 12 with dissolve
    dexter "Psh, you scared you're gonna lose?"
    show old_dexter 11
    show player 12
    player_name "No."
    show player 90
    show old_dexter 28 with dissolve
    dexter "{b}[firstname]{/b}'s a chicken, everybody!"
    show old_dexter 11 with dissolve
    show player 12
    player_name "... Tch, fine."
    player_name "Let's do it!"
    hide player
    hide old_dexter
    with dissolve
    return

label button_dexter_intro_beginning:
    show anon f_worried
    show dexter
    with dissolve
    dexter "What are you looking at, loser?!"
    anon "Nothing."
    dexter "Yeah, that's right!"
    dexter "Keep on walkin', bitch!"
    dexter @ f_laugh "Hahahaha!"
    hide dexter with dissolve
    anon f_angry "Ugh, he's such an asshole..."
    hide anon with dissolve
    return

label button_dexter_intro:
    show player 5 at left
    show old_dexter 3 at right
    with dissolve
    dexter "I thought I smelled a little bitch!"
    show old_dexter 2
    show player 12
    player_name "Screw you, {b}Dexter{/b}..."
    show player 90
    show old_dexter 6 with dissolve
    dexter "WHAT DID YOU SAY?!"
    show old_dexter 4 with dissolve
    show player 11
    dexter "You want me to knock your ass out, right here?!"
    show old_dexter 2 with dissolve
    player_name "..."
    show old_dexter 3
    dexter "Yeah, that's what I thought."
    show old_dexter 6 with dissolve
    dexter "You better be staying away from my girl!"
    show old_dexter 2 with dissolve
    show player 5
    player_name "..."
    show old_dexter 4 with dissolve
    dexter "You hear me, bitch?!"
    show old_dexter 2 with dissolve
    return

label button_dexter_intro_final:
    show player 90 at left
    show old_dexter 2 at right
    with dissolve
    dexter "..."
    show player 12
    player_name "I'm sorry, did you say something, {b}Dexter{/b}?"
    show player 91
    show old_dexter 8
    dexter "No!"
    show old_dexter 2
    show player 12
    player_name "Yeah, that's what I thought."
    show player 91

    dexter "..."
    return

label button_dexter_basketball_final:
    show player 12
    player_name "Still playing basketball?"
    show player 91
    dexter "..."
    show player 12
    player_name "Have you guys managed to win a game yet?"
    show player 91
    show old_dexter 8
    dexter "I don't wanna talk about it!"
    show old_dexter 2
    show player 12
    player_name "I'm just trying to-"
    show player 11
    show old_dexter 8
    dexter "Leave me alone, {b}[firstname]{/b}!"
    hide old_dexter with dissolve
    pause
    show player 10
    player_name "Sheesh, alright."
    hide player with dissolve
    return

label button_dexter_basketball:
    show player 12
    player_name "Still playing basketball?"
    show player 90
    show old_dexter 3
    dexter "Of course, I was born to play!"
    show old_dexter 1
    show player 12
    player_name "Have you even won a game yet?"
    show player 90
    show old_dexter 3
    dexter "Psh, yeah. Like a hundred million..."
    show old_dexter 1
    show player 12
    player_name "Yeah right! You guys are awful..."
    show player 90
    show old_dexter 4 with dissolve
    dexter "HEY! You want a knuckle sandwich, loser?!"
    show old_dexter 2 with dissolve
    player_name "..."
    show old_dexter 3
    dexter "What does a little bitch like you know about basketball anyways?!"
    dexter "It's a man's sport!"
    show old_dexter 1
    show player 17
    player_name "Oh, well then, it's no wonder why you ladies can't win a game."
    show player 13
    show old_dexter 3
    dexter "Huh? I don't-"
    dexter "Oh, you think that's funny?!"
    show old_dexter 8
    dexter "How about I knock some of your teeth out?!"
    show player 5
    dexter "That would be pretty funny, wouldn't it?!"
    show old_dexter 2
    return

label button_dexter_whatever:
    show player 12
    player_name "Tch, yeah. Whatever, man..."
    hide player with dissolve
    pause
    show old_dexter 8
    dexter "Hey, I'm not kidding {b}[firstname]{/b}!"
    dexter "Stay away from {b}Roxxy{/b}!"
    dexter "She's mine!"
    hide old_dexter
    hide player
    with dissolve
    return

label button_dexter_behaving:
    show player 12
    player_name "I trust you're behaving yourself."
    show player 90
    show old_dexter 8
    dexter "... Yes."
    show old_dexter 2
    show player 12
    player_name "You do remember what happens if I catch you messing with my friends again, right?"
    show player 92
    player_name "Do you need a reminder?!"
    show player 91
    show old_dexter 8
    dexter "NO!"
    dexter "I remember..."
    show old_dexter 2
    show player 92
    player_name "Good."
    show player 91
    return

label button_dexter_run_along:
    show player 12
    player_name "Run along now, {b}Dexter{/b}."
    show player 91
    dexter "..."
    show old_dexter 8
    dexter "GRRRR!!!"
    hide old_dexter with dissolve
    pause
    show player 17
    player_name "Hahaha!"
    player_name "I like the new {b}Dexter{/b}!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
