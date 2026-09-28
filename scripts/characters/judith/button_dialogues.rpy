label judith_dialogue_start:
    scene lefthall_c
    show anon
    show judith
    with dissolve
    judith "Hey {b}[firstname]{/b}!"
    anon "Hey {b}Judith{/b}, how's it going?"
    judith "Oh, I'm great!"
    judith f_sad @ f_sad_down "I... I just wanted to thank you."
    anon @ f_confused "Oh. For what?"
    judith "In the {b}boys' locker room{/b}... You made me feel... Safe."
    show judith f_normal
    anon f_shy a_behind_head "Oh..."
    judith "And, you know... You stood up to {b}Annie{/b}. I think that was very brave."
    anon a_idle "It's fine, {b}Judith{/b}. I was just trying to do the right thing."
    anon f_worried_low "I should be the sorry one... For showing you my... You know..."
    judith "Oh that's fine!! I enjoyed-"
    judith f_sad "I mean... I didn't mind, at all."
    show anon f_normal
    judith f_normal "We just got to... Know each other a little better!"
    anon @ f_laugh "Haha. Yeah. I suppose so..."
    judith "I have to go! I'll see you in class then!"
    anon a_wave "See you later!"
    return

label judith_dialogue_left_hallway_intro:
    scene lefthall_c
    show judith
    show anon with dissolve
    anon "Hey, {b}Judith{/b}!"
    judith "Oh, hey, {b}[firstname]{/b}."
    judith "How are you doing?"
    anon "Pretty good. How are you?"
    judith f_sad @ f_sad_down -m_talk "..."
    judith "Alright I guess."
    return

label judith_dialogue_art_classroom_intro:
    scene art_classroom_c
    show old_judith 1 at right
    show player 14 at left
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    player_name "Enjoying art, {b}Judith{/b}?"
    show player 13
    show old_judith 5
    judith "Yeah!"
    judith "It's one of my favorite subjects."
    show old_judith 4
    show player 14
    player_name "Yeah, mine too!"
    show player 13
    show old_judith 5
    judith "I like it because no matter how bad my drawings are, it's still considered art!"
    show old_judith 4
    show player 17
    player_name "Heh, good one."
    show old_judith 1
    return

label judith_dialogue_bathroom_fun:
    anon f_normal "Say, would you like to sneak into the girls' locker room for a little... You know?"
    judith f_normal "... You really want to..."
    judith "... W-with me?"
    anon "I mean, yeah!"
    anon "If that's okay?"
    judith "Oh, definitely!"
    judith "Let's go!"
    return

label judith_dialogue_dictionary_return:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 14 at left
    player_name "Hey, {b}Judith{/b}! Here's your book back."
    show player 239_240 with dissolve
    pause
    show player 522 with dissolve
    player_name "Thanks again!"
    show player 13
    show old_judith 43
    with dissolve
    judith "Oh good, I was starting to worry..."
    show old_judith 4 with dissolve
    show player 14
    player_name "No need to worry. It's in tip-top shape... See."
    show player 13
    show old_judith 5
    judith "Thanks for being careful with it, {b}[firstname]{/b}."
    judith "I dunno why I worry so much..."
    show old_judith 4
    show player 14
    player_name "Thanks for letting me borrow it!"
    show player 13
    show old_judith 5
    judith "Anything for yo-"
    show old_judith 3
    judith "I mean... A-anytime!"
    show old_judith 1
    show player 10
    player_name "Okay, well, I'll see ya around."
    show player 5
    show old_judith 3
    judith "Bye, {b}[firstname]{/b}."
    return

label judith_dialogue_bissette_find_full_dictionary:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 14 at left
    player_name "Hey there, {b}Judith{/b}! Got a minute?"
    show player 13
    show old_judith 5
    judith "Sure, {b}[firstname]{/b}."
    show old_judith 4
    show player 14
    player_name "I was hoping I could {b}borrow your French dictionary{/b}."
    player_name "I need to make a quick copy of some pages and I'll return it."
    show player 13
    show old_judith 3
    judith "My {b}French dictionary{/b}?"
    show old_judith 5
    judith "Absolutely! So long as you promise to be careful with it?"
    show old_judith 4
    show player 11
    player_name "( What is with women and their French dictionaries? )"
    show player 10
    player_name "Yeah, I'll be really careful and you won't even notice it's gone."
    show player 13
    show old_judith 5
    judith "Okay, I trust you, {b}[firstname]{/b}."
    pause
    show old_judith 43 with dissolve
    judith "Here it is..."
    show old_judith 4
    show player 522
    with dissolve
    player_name "Thanks, {b}Judith{/b}! I totally owe you one!"
    hide old_judith with dissolve
    show player 13
    player_name "( Alright, now to {b}head to the computer lab and copy these missing pages{/b}. )"
    return

label judith_dialogue_dewitt_find_flute:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 10 at left
    player_name "Do you still have the school's flute?"
    player_name "I need it for the talent show."
    show player 5
    show old_judith 2
    judith "Oh, umm..."
    show old_judith 1
    show player 10
    player_name "The instrument sign-out sheet had your name next to the flute."
    show player 5
    show old_judith 2
    judith "{i}*Sigh*{/i}"
    show old_judith 3
    judith "I do have it. It's in my locker."
    show old_judith 1
    show player 12
    player_name "I have a feeling there is a \"but\" coming?"
    show player 5
    show old_judith 3
    judith "BUT, I kinda broke it..."
    show old_judith 1
    show player 1
    player_name "You broke it?!"
    player_name "How did that happen?"
    show player 5
    show old_judith 5
    judith "Heh, well, I accidentally kinda..."
    show old_judith 6
    show player 11
    player_name "..."
    show old_judith 2
    judith "... Sat on it."
    show old_judith 1
    show player 10
    player_name "You sat on it?"
    show player 11
    show old_judith 3
    judith "... Yeah."
    show old_judith 5
    judith "Which sucks 'cause I was really enjoying it!"
    show old_judith 4
    show player 10
    player_name "I didn't know you could play the flute?"
    show player 5
    show old_judith 5
    judith "Oh, I can't play it."
    show old_judith 4
    show player 12
    player_name "Well then, I don't understand how you were enjoying it?"
    show player 5
    judith "..."
    show old_judith 5
    judith "Heh, never mind."
    show old_judith 2
    judith "I was hoping no one would ask about it..."
    show old_judith 1
    show player 10
    player_name "Maybe I can fix it?"
    show player 5
    show old_judith 4
    judith "..."
    show old_judith 5
    judith "You can try."
    show old_judith 4
    show player 12
    player_name "Is it still in your locker?"
    show player 5
    show old_judith 5
    judith "Yup."
    show old_judith 4
    show player 10
    player_name "Alright, thanks, {b}Judith{/b}."
    return

label judith_dialogue_talent_show_help:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 10 at left
    player_name "I was wondering if you wanted to participate in the upcoming talent show?"
    show player 5
    show old_judith 3
    judith "No thanks, {b}[firstname]{/b}. I don't really know how to play an instrument."
    show old_judith 2
    judith "... And I'm way too embarrassed to get up on stage in front of the entire school."
    show old_judith 1
    show player 10
    player_name "Well, what if we played together?"
    show player 5
    show old_judith 5
    judith "You and me?"
    show old_judith 4
    show player 14
    player_name "Sure, why not?"
    show player 13
    show old_judith 6
    judith "Hmm..."
    show old_judith 2
    judith "No, I'm sorry, {b}[firstname]{/b}."
    show old_judith 3
    judith "As much as I'd enjoy playing with you; just the thought of being in the spotlight like that..."
    show old_judith 8f at Position (xoffset=2) with dissolve
    show player 11
    judith "..."
    show old_judith 9f at Position (xoffset=-4) with dissolve
    judith "Excuse me, I need to go use the restroom!"
    hide old_judith with dissolve
    show player 12
    player_name "Dang, I thought for a second she was going to agree."
    show player 10
    player_name "Guess I'd better keep looking..."
    return

label judith_dialogue_okita_get_bifocal_lenses:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 2 at left
    player_name "{b}Judith{/b}, are you farsighted or nearsighted?"
    show player 1
    show old_judith 2
    judith "Uhh, well."
    show old_judith 3
    judith "Both..."
    show player 2
    show old_judith 1
    player_name "Really?!"
    show player 1
    show old_judith 2
    judith "Yeah. I'm blind without my glasses..."
    show old_judith 3
    judith "Pretty dorky. I know..."
    show player 2
    show old_judith 1
    player_name "No, it's great!"
    show player 1
    show old_judith 3
    judith "It is?"
    show player 29 with dissolve
    show old_judith 1
    player_name "Well, I mean, no. It sucks that you can't see without them."
    show player 2 with dissolve
    player_name "... But it's also a good thing, 'cause I'm looking for a pair of {b}varifocal lenses{/b}."
    show player 1
    show old_judith 5
    judith "Oh. Well, you found some."
    show player 2
    show old_judith 4
    player_name "You wouldn't happen to have a spare set, would you?"
    show player 1
    show old_judith 5
    judith "Sure."
    show player 2
    show old_judith 4
    player_name "Awesome! Could I have them?"
    show player 1
    show old_judith 2
    judith "Hmm, you want me to just give you my spare set?"
    show player 10
    show old_judith 1
    player_name "... Yes?"
    show player 11
    show old_judith 3
    judith "How about a trade?"
    show player 2
    show old_judith 1
    player_name "Yeah, okay. What do you want?"
    show player 1
    show old_judith 2
    judith "Umm, it's kinda embarrassing..."
    show old_judith 1
    player_name "..."
    show old_judith 2
    judith "Well, you see, some of the other girls have been giving me a hard time..."
    show old_judith 3
    judith "... Because I've never had a boyfriend."
    show player 10
    show old_judith 1
    player_name "That sucks."
    show player 11
    show old_judith 2
    judith "Yeah."
    judith "I was kinda wondering..."
    show old_judith 3
    judith "... Well, I was hoping you would pretend to be my boyfriend."
    show player 23
    show old_judith 1
    player_name "( !!! )" with hpunch
    show player 10
    player_name "You want me to pretend to be your boyfriend?"
    show player 11
    show old_judith 3
    judith "Just long enough to take a couple pictures!"
    show player 10
    show old_judith 1
    player_name "Pictures?!"
    show player 11
    show old_judith 2
    judith "Yeah."
    show old_judith 3
    judith "You meet me in the park, we take a couple pictures like we're boyfriend and girlfriend, and then I'll give you my spare set."
    judith "Deal?"
    show player 10
    show old_judith 1
    player_name "I uhh..."
    show player 11
    show old_judith 3
    judith "Pleeeease? It would be such a huge help!"
    show player 2
    show old_judith 1
    player_name "Yeah, alright, I suppose I can do that."
    show player 1
    show old_judith 5
    judith "You will?!"
    judith "Okay, meet me at the park! I'll be there in the {b}afternoons{/b}."
    show player 2
    show old_judith 4
    player_name "{b}The park, in the afternoon{/b}. Got it!"
    show player 1
    show old_judith 5
    judith "Great! See you there!"
    return

label judith_dialogue_okita_take_picture_judith:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 2 at left
    player_name "Where did you want to take that picture again?"
    show player 1
    show old_judith 3
    judith "Oh umm, at the park."
    show player 2
    show old_judith 1
    player_name "Alright."
    show player 1
    show old_judith 3
    judith "You aren't having second thoughts, are you?"
    show old_judith 2
    judith "'Cause it's okay, we don't hav-"
    show player 2
    show old_judith 1
    player_name "No, {b}Judith{/b}. It's fine, really!"
    show old_judith 4
    player_name "I'll meet you there!"
    show player 1
    show old_judith 5
    judith "... Thanks, {b}[firstname]{/b}."
    return

label judith_dialogue_ross_ask_model:
    hide anon
    hide judith
    show old_judith 1 at right
    show player 2 at left
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 1
    show old_judith 5
    judith "You want me to model for you?"
    show player 2
    show old_judith 4
    player_name "Yeah, that would be awesome!"
    show player 10
    player_name "It's nude modeling though..."
    show player 11
    show old_judith 3
    judith "... Oh."
    show old_judith 1
    judith "..."
    show old_judith 3
    judith "... You really want me to?"
    show player 10
    show old_judith 1
    player_name "Of course!"
    show player 11
    show old_judith 5
    judith "Then I'll do it! For you, {b}[firstname]{/b}!"
    show player 2
    show old_judith 4
    player_name "Thanks, {b}Judith{/b}! That's really awesome of you!"
    player_name "Just meet me in art class."
    show player 1
    show old_judith 5
    judith "Alright."
    return

label judith_dialogue_left_hallway_leave:
    hide player
    hide old_judith
    show judith
    show anon
    anon f_worried @ -m_talk "..."
    judith f_sad_down @ -m_talk "..."
    anon a_behind_head f_normal "Well... I'd better get going!"
    judith f_normal "See you later, {b}[firstname]{/b}."
    return

label judith_dialogue_art_classroom_leave:
    hide player
    hide old_judith
    show anon
    show judith
    anon f_normal "See you later, {b}Judith{/b}."
    judith f_normal "Bye, {b}[firstname]{/b}."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
