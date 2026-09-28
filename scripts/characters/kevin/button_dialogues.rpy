label k01_intro:
    scene cafeteria_b
    show player 2 at left with dissolve
    show old_kevin 1 at right with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show player 1 at left
    show old_kevin 2 at right
    kevin "Hey, dude..."
    show old_kevin 1 at right
    show player 10 at left
    player_name "You're on cafeteria duties huh..."
    show old_kevin 2 at right
    show player 13 at left
    kevin "Yep! I got two more months of this crap."
    show old_kevin 1 at right
    show player 17 at left
    player_name "That sucks."
    show old_kevin 2 at right
    show player 1 at left
    kevin "Yeah, but what can I do?"
    kevin "By the way, was {b}Dexter{/b} giving you guys a hard time in the hallway?"
    show old_kevin 1 at right
    show player 24 at left
    player_name "Yeah, he and {b}Roxxy{/b} are always on our case..."
    show player 26 at left
    player_name "But it's nothing. I don't really care about what they say."
    show old_kevin 3 at right
    show player 11 at left
    kevin "Dude. You gotta stand up for yourself."
    show old_kevin 1 at right
    show player 10 at left
    player_name "I'd rather just avoid him, you know?"
    player_name "There's no point in getting into a fight with a guy twice my size."
    show old_kevin 3 at right
    show player 11 at left
    kevin "You can't let him walk all over you. How're you going to survive college like that?"
    show old_kevin 1 at right
    show player 24 at left
    player_name "Well, I'm just too weak to do anything about it."
    show old_kevin 4 at right
    show player 11 at left
    kevin "Hmm... Maybe we could work something out."
    show old_kevin 1 at right
    show player 10 at left
    player_name "What do you mean?"
    show old_kevin 4 at right
    show player 1 at left
    kevin "Well, I could {b}help you work out at the Gym{/b}..."
    kevin "Like spotting you when you're lifting, and show you some tricks."
    show player 13
    show old_kevin 2
    kevin "Aww man, this is gonna get me all depressed..."
    kevin "You know I wanna be in there helping my bro get ripped!"
    show old_kevin 1
    pause
    show old_kevin 4
    kevin "Tsk, you know what..."
    show old_kevin 2
    kevin "I wonder if I could sneak outta here?"
    show old_kevin 1
    show player 5
    player_name "Hmm?"
    show old_kevin 2
    kevin "I mean, if we could {b}find someone to split the work{/b}..."
    kevin "... I could squeeze the gym in, in the mornings."
    kevin "It could totally work, bro!"
    show old_kevin 1
    show player 10
    player_name "What do you mean?"
    show player 5
    show old_kevin 2
    kevin "Well, {b}Mrs. Smith{/b} never comes in here in the morning."
    kevin "So as long as the work got done, it wouldn't really matter who was doing it."
    show old_kevin 1
    show player 14
    player_name "So we just need to {b}find someone to split the work with you{/b}?"
    show player 13
    show old_kevin 2
    kevin "Yeah, you got any ideas?"
    show old_kevin 1
    show player 4
    pause
    show player 14
    player_name "Hmm, I might be able to convince {b}Erik{/b} to do it."
    show player 13
    show old_kevin 2
    kevin "Oh, that would be awesome, bro!"
    show old_kevin 1
    show player 14
    player_name "I'll {b}ask him{/b} about it."
    show player 13
    show old_kevin 2
    kevin "Hell yeah!"
    show old_kevin 1
    return

label k01_prompt:
    show old_kevin 2
    kevin "You {b}talk with Erik{/b} about helping me out yet?"
    show old_kevin 1
    show player 29 with dissolve
    player_name "No, not yet."
    show player 3
    show old_kevin 2
    kevin "Ugh, you gotta hurry, bro!"
    show old_kevin 2b with dissolve
    kevin "My muscles are wasting away in here!"
    show old_kevin 1 with dissolve
    show player 14 with dissolve
    player_name "Heh, just relax."
    player_name "I'll talk with him."
    show player 13
    return

label k01_outro:
    show old_kevin 2
    kevin "You {b}talk with Erik{/b} about helping me out yet?"
    show old_kevin 1
    show player 17
    player_name "I did."
    player_name "He's gonna do it."
    show player 13
    show old_kevin 2b with dissolve
    kevin "HELL!"
    kevin "YEAH!"
    kevin "BRO!"
    show old_kevin 2c with dissolve
    kevin "You are the freaking man!"
    show old_kevin 6 with dissolve
    kevin "Finally, I can get back to my two-a-days!"
    show old_kevin 5
    show player 14
    player_name "Heh, so I guess I'll see you at the gym in the {b}Morning{/b}?"
    show player 13
    show old_kevin 9b with dissolve
    kevin "You know it, bro!"
    hide old_kevin
    hide player
    with dissolve
    return

label kevin_greeting_sad:
    scene expression player.location.background_blur with None
    show player 13 at left
    show old_kevin 2 at right
    with dissolve
    kevin "Sup, bro?!"
    show old_kevin 1
    show player 14
    player_name "Hey, {b}Kevin{/b}."
    show player 13
    show old_kevin 2
    kevin "You here to scrub some pots?"
    show old_kevin 1
    show player 17
    player_name "Heh, no way man!"
    show player 13
    show old_kevin 2
    kevin "Ugh, this cafeteria duty sucks dick, bro!"
    show old_kevin 1
    pause
    show old_kevin 2
    kevin "... And not the cool kind, either."
    show old_kevin 1
    show player 29 with dissolve
    player_name "Eh, right..."
    show player 5 with dissolve
    return

label kevin_greeting_happy:
    show old_kevin magic 1 at right
    show player 14 at left
    with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show player 13
    show old_kevin magic 2
    kevin "Hello, {b}[firstname]{/b}."
    show old_kevin magic 1
    show player 14
    player_name "What's up?"
    show player 13
    show old_kevin magic 2
    kevin "Not much. Yesterday was glutes day for me."
    kevin "My ass is sore!"
    kevin "Feel how tight it is though!"
    show old_kevin magic 1
    show player 10
    player_name "Uhhh... No thanks dude."
    show player 13
    show old_kevin magic 2
    kevin "Your loss!"
    return

label kevin_somrak_first:
    show player 10 at left
    show old_kevin magic 1 at right
    player_name "So I met that new {b}Muay Thai{/b} trainer you were going on about."
    show player 5
    show old_kevin magic 2
    kevin "Right on, bro!"
    kevin "He's pretty awesome, right?!"
    show old_kevin magic 1
    show player 12
    player_name "He's a total crackpot!"
    show player 5
    show old_kevin magic 2
    kevin "Huh?"
    show old_kevin magic 1
    show player 12
    player_name "Yeah, he said he won't teach me unless I bring him {b}used panties{/b}!"
    show player 5
    show old_kevin magic 2
    kevin "Oh, that..."
    show old_kevin magic 3 with dissolve
    kevin "Umm."
    show old_kevin magic 4
    show player 10
    player_name "Wait a second..."
    show player 14
    player_name "You brought him a pair, didn't you?!"
    show player 13
    show old_kevin magic 3
    kevin "Eh, yeeeeah."
    show old_kevin magic 4
    show player 14
    player_name "Dude, seriously?"
    show player 13
    show old_kevin magic 2 with dissolve
    kevin "Well, I heard all this awesome stuff about him, and I was curious..."
    kevin "Once you get past the panties thing, he's like totally legit!"
    show old_kevin magic 1
    show player 11
    player_name "..."
    show old_kevin magic 2
    kevin "I'm serious!"
    kevin "He really knows his shit, bro."
    show old_kevin magic 1
    show player 14
    player_name "Where did you get a pair of {b}used panties{/b}?"
    show player 13
    show old_kevin magic 3 with dissolve
    kevin "Oh, eh... I kinda... Snatched a pair of my mom's, outta the dirty clothes basket."
    show old_kevin magic 4
    show player 12
    player_name "Dude..."
    show player 5
    show old_kevin magic 2 with dissolve
    kevin "What?!"
    kevin "It's not THAT weird."
    kevin "I just took one pair and it's not like I was taking them for me."
    kevin "I gave them to {b}Master Somrak{/b}."
    show old_kevin magic 1
    show player 14
    player_name "It's pretty weird {b}Kevin{/b}."
    show player 13
    show old_kevin magic 2
    kevin "Nah, bro."
    kevin "You're getting hung up on trivial stuff..."
    kevin "You've got a couple girls at your house, don't you?"
    show old_kevin magic 1
    show player 10
    player_name "Yeah, but-"
    show player 11
    show old_kevin magic 2
    kevin "Well, there ya go! Just snag one pair and you're in!"
    kevin "It's really not a big deal, bro."
    show old_kevin magic 1
    show player 35
    player_name "Hmm, I dunno..."
    show player 34
    show old_kevin magic 2
    kevin "Just do it, {b}[firstname]{/b}."
    kevin "{b}Master Somrak{/b}'s teachings will change your life, I'm telling ya!"
    show old_kevin magic 1
    show player 33
    player_name "I guess I could take one pair..."
    show player 13
    show old_kevin magic 2
    kevin "See, there ya go!"
    show old_kevin magic 1
    show player 14
    player_name "I'll {b}check around my house{/b} and see if I can {b}find a pair of [deb_name]'s or [jen_name]'s panties{/b}."
    show player 13
    return

label kevin_somrak_repeat:
    show player 10
    player_name "I can't believe this guy has me stealing {b}used panties{/b}..."
    show player 5
    show old_kevin magic 2
    kevin "It's not that big a deal, bro!"
    kevin "Just swipe a pair from home."
    show old_kevin magic 1
    show player 37 with dissolve
    player_name "Yeah, yeah."
    player_name "I'll {b}check around my house{/b} and see if I can {b}find a pair of [deb_name]'s or [jen_name]'s{/b}."
    show player 13 with dissolve
    return

label kevin_magazines:
    show player 2 at left
    show old_kevin 29b at right
    with dissolve
    player_name "Hey, {b}Kevin{/b}!"
    show player 1
    show old_kevin 30
    kevin "What's up, {b}[firstname]{/b}?"
    show player 2
    show old_kevin 29b
    player_name "Not much. What are you reading?"
    show player 1
    show old_kevin 30b
    kevin "Oh, just some workout magazines I got from the gym."
    show player 2
    show old_kevin 29b
    player_name "Cool, you trying a new workout or something?"
    show player 1
    show old_kevin 30
    kevin "No, why?"
    show player 11
    show old_kevin 29
    player_name "..."
    show old_kevin 31 with dissolve
    kevin "Come check out this beefcake, {b}[firstname]{/b}!"
    show player 10
    show old_kevin 31b
    player_name "... Beefcake?"
    show player 11
    player_name "..."
    show player 10
    player_name "Uh, right... You think I could take some of these magazines?"
    show player 11
    show old_kevin 30 with dissolve
    kevin "Heh, I didn't know you were a fellow connoisseur of the masculine form..."
    show player 10
    show old_kevin 29
    player_name "Actually, I'm making a collage."
    show player 11
    show old_kevin 30b
    kevin "Oh, right. Collage."
    show old_kevin 31 with dissolve
    kevin "I gotcha, bro! Say no more!"
    kevin "Take all you need! This one will keep me busy for a while."
    show player 2
    show old_kevin 31b
    player_name "Awesome! Thanks, uhh, bro..."
    show player 1
    show old_kevin 31c
    kevin "Daaaamn, he's glistening..."
    show player 10
    player_name "..."
    return

label kevin_modeling:
    show player 2 at left
    show old_kevin 1 at right
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show old_kevin 2
    show player 1
    kevin "Modeling. Like I just have to stand there?"
    show player 2
    show old_kevin 1
    player_name "Yeah, you just have to stand there."
    show player 10
    player_name "Naked."
    show old_kevin 3
    show player 11
    kevin "Naked?!"
    kevin "Oh, man. I dunno, bro."
    kevin "Is it just gonna be you there drawing?"
    show player 10
    show old_kevin 1
    player_name "Well, {b}Mia{/b} and I will both be drawing."
    player_name "{b}Miss Ross{/b} will be there too."
    show player 11
    show old_kevin 4
    kevin "Ugh, pass..."
    show old_kevin 3
    kevin "I don't want girls to see me naked, bro. That's kinda gross."
    show old_kevin 1
    player_name "..."
    show player 10
    player_name "O-okay."
    return

label kevin_guitar_intro:
    show player 10
    player_name "I'm helping {b}Miss Dewitt{/b} find volunteers for the talent show."
    player_name "Didn't you used to play the guitar?"
    show player 5
    show old_kevin magic 2
    kevin "Yeah, I used to."
    show old_kevin magic 1
    show player 10
    player_name "What happened?"
    show player 5
    show old_kevin magic 2
    kevin "Ah, my ex kinda smashed it after I broke up with him."
    show old_kevin magic 1
    show player 12
    player_name "Him?"
    show player 11
    show old_kevin magic 3 with dissolve
    kevin "Did I say him? Sorry, I meant her."
    kevin "... Yeah, SHE smashed it to pieces."
    show old_kevin magic 1 with dissolve
    show player 14
    player_name "Huh, you got a thing for the crazy girls, huh?"
    show player 13
    show old_kevin magic 3 with dissolve
    kevin "Heh, you know it! Crazy girls, I'm waaaaay into them! Totally..."
    show old_kevin magic 1 with dissolve
label kevin_guitar_prompt:
    show player 14
    player_name "So, {b}if you had a guitar, would you play in the talent show{/b}?"
    show player 13
    show old_kevin magic 2
    kevin "Yeah, I wouldn't mind."
    kevin "Where am I gonna get a guitar though? They are super expensive!"
    show old_kevin magic 1
    if M_dewitt.is_state(S_dewitt_replace_guitar):
        show player 34
        player_name "( {b}I need to switch my custom-made guitar with one in Erik's basement{/b}! )"
    else:
        show player 35
        player_name "Hmm, maybe I can find you one..."
        show player 34
        player_name "( {b}Erik has a bunch in his basement{/b}. Maybe I can borrow one? )"
    show player 14
    player_name "I'll be back!"
    show player 13
    show old_kevin magic 2
    kevin "Alright."
    return

label kevin_guitar_outro:
    show player 14
    player_name "I found a guitar for you!"
    show player 13
    show old_kevin 24
    kevin "Really?"
    show old_kevin 23
    show player 239_240 with dissolve
    pause
    show player 577 with dissolve
    player_name "What do you think?"
    show player 13 with dissolve
    show old_kevin 16f with dissolve
    kevin "Holy crap! Where did you get this thing?"
    kevin "This thing is really high end!"
    show old_kevin 14f
    show player 10
    player_name "It is?"
    show player 5
    show old_kevin 15f
    kevin "Uhh, yeah bro!"
    kevin "I hope you didn't steal it or something."
    show old_kevin 14f
    show player 14
    player_name "Borrowed it actually, from a friend of mine. So be careful with it, yeah?"
    hide player
    show old_kevin 27 at left
    with dissolve
    kevin "No problems there!"
    kevin "I'll treat this beauty with the respect it deserves!"
    show old_kevin 28
    player_name "Cool, so you're down to play it for the talent show."
    show old_kevin 27
    kevin "I'm down!"
    show old_kevin 28
    player_name "Awesome! I'll see you in {b}Miss Dewitt{/b}'s class soon for practice then!"
    show old_kevin 27
    kevin "Sounds good, bro!"
    show player 13 at left
    show old_kevin 16 at right
    with dissolve
    kevin "I'm gonna call you... Devin."
    kevin "Would you like that beautiful?"
    show player 11
    hide old_kevin with dissolve
    player_name "..."
    return

label kevin_adhesive_prompt:
    show player 10
    player_name "What do we need for that {b}adhesive{/b} again?"
    show player 13
    show old_kevin 2
    kevin "Just {b}meet me in the science lab after class{/b}."
    kevin "I'll take care of the rest."
    show old_kevin 1
    show player 14
    player_name "Awesome! Thanks, {b}Kevin{/b}!"
    return

label kevin_goodbye:
    show old_kevin 1
    show player 14
    player_name "Anyways, I gotta go."
    if M_kevin.finished_state(S_kevin_erik_agreed):
        show player 13
        show old_kevin 2
        kevin "I'd better see you at the gym tomorrow, bro!"
        kevin "Bright and early! Am I right?"
        show old_kevin 1
        show player 14
        player_name "Maybe..."
    else:
        player_name "Keep your spirits up, man."
        show player 13
        show old_kevin 2
        kevin "Yeah, alright bro."
        kevin "See ya around."
    hide old_kevin
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
