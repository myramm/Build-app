label eriksroom_erik_bully_coax:
    scene expression game.timer.image("eriks_room{}_c")
    show player 13 at left with dissolve
    show old_erik 5 at right with dissolve
    erik "Hai, {b}[firstname]{/b}."

    erik "How've you been?"

    show old_erik 1
    show player 14
    player_name "I've been doing pretty good."

    show player 12
    player_name "How about you?"

    player_name "Have you been missing classes lately or something?"

    show player 5
    show old_erik 2 with dissolve
    erik "..."
    show player 10
    player_name "Apakah semuanya baik-baik saja?"

    show player 5
    show old_erik 5 with dissolve
    erik "{b}Mrs. Johnson{/b} sent you up here, huh?"

    show old_erik 3b
    show player 10
    player_name "Just checking up on you, that's all."

    show player 5
    show old_erik 5
    erik "Well... {b}Dexter{/b} has been on my case ever since you left..."

    erik "It's just been hard to attend school knowing he'll be there too. Waiting..."

    show old_erik 3b
    show player 12
    player_name "What happened while I was away?"

    show player 5
    show old_erik 5
    erik "A few weeks ago, I was sitting in the cafeteria, and he came up to me..."

    show old_erik 3
    erik "... He said he wanted a copy of my homework for {b}Miss Bissette{/b}'s class."

    show player 12
    player_name "What did you do?"

    show player 11
    show old_erik 5
    erik "I told him no!"

    erik "But, he said he'd stick me into a locker if I didn't do what he asked..."

    show old_erik 3b
    player_name "..."
    show old_erik 5
    erik "Anyway, I ended up giving him my homework and have been until recently."

    show old_erik 3b
    show player 38 with dissolve
    player_name "Apa yang telah terjadi?"

    show player 11 with dissolve
    show old_erik 5
    erik "I told him he can't push me around all the time."

    erik "And then... He hit me in front of everyone..."

    show old_erik 2 with dissolve
    show player 16
    pause
    show player 12
    player_name "Hey, {b}Erik{/b}..."

    show old_erik 3 with dissolve
    show player 10
    player_name "I'm glad you told me."

    show player 30
    player_name "Let me know if he bothers you again."

    player_name "And hopefully he can focus his attention on someone else!"

    show player 13
    show old_erik 5
    erik "Alright, thanks, {b}[firstname]{/b}."

    show old_erik 3b
    show player 14
    player_name "You gonna be okay?"

    show player 13
    show old_erik 5
    erik "Ya, menurutku..."

    erik "But, can you please not tell {b}Mrs. Johnson{/b} I'm being bullied at school?"

    erik "I don't want her to worry so much..."

    show old_erik 3b
    show player 2
    player_name "Oke."

    hide player
    hide old_erikl
    hide old_erik
    with dissolve
    return

label eriksroom_erik_vr_ready:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 30 with dissolve
    player_name "Hah?"

    player_name "( {b}Erik{/b} is usually at his computer. )"

    show player 12
    player_name "( He must be in the basement... )"

    hide player with dissolve
    return

label eriksroom_erik_feed_missing:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 12 with dissolve
    player_name "( No one here? )"

    show player 14
    player_name "( He must be in the basement... )"

    show player 11
    pause
    show player 10
    player_name "Hah?"

    player_name "( I think I can hear some voices coming from {b}Mrs. Johnson{/b}'s room. )"

    show player 12
    player_name "( I should ask her where {b}Erik{/b} is... )"

    hide player with dissolve
    return

label eriksroom_erik_learn_intro:
    scene expression game.timer.image("eriks_room{}_c")
    show player 13 at left
    show old_erik 5 at right
    with dissolve
    erik "Hai, {b}[firstname]{/b}!"

    if M_erik.once('learn_limbo'):
        erik "Did you hear from {b}Mrs. Johnson{/b} yet?"

        show old_erik 1
        show player 14
        player_name "Not yet, she must still be thinking about it..."

    else:
        erik "Did you end up talking to {b}Mrs. Johnson{/b}?"

        show old_erik 1
        show player 14
        player_name "Yeah, she said she needed to think about it..."

    show player 13
    show old_erik 5
    erik "Mungkin kita seharusnya tidak mengatakan-"

    show old_erik 1b
    show player 11
    mrsj "Boys?"

    mrsj "Can you come in here, please?"

    show old_erik 1
    show player 10
    player_name "Was that {b}Mrs. Johnson{/b}?"

    show player 5
    show old_erik 5
    erik "Yeah... I think she's in her room."

    show old_erik 1
    show player 14
    player_name "She wants us to join her..."

    show player 13
    show old_erik 5
    erik "Mengapa?"

    show old_erik 1
    show player 14
    player_name "We'll have to see..."

    hide player
    hide old_erik
    with dissolve

    scene erik_house_upstairs_night_c01
    show mrsj 14 at right
    with fade
    show old_erik 5f at Position (xpos=300)
    show player 13 at left
    with dissolve
    erik "Hai, {b}Ny. Johnson{/b}!"

    erik "You... Needed something from us?"

    show old_erik 1f
    show mrsj 19
    mrsj "Listen, boys."

    mrsj "I know you two have been talking about this, so..."

    mrsj "I've thought this over, and since you two are okay with this..."

    show mrsj 49
    mrsj "I'll agree to give you two private... Sex education lessons."

    show mrsj 50
    show player 23
    player_name "!!!"
    show old_erik 5f
    erik "{b}M-Mrs. Johnson{/b}, are you sure?"

    show old_erik 1f
    show mrsj 49
    show player 18
    mrsj "Of course, pumpkin!"

    mrsj "I don't have a problem with it, as long as this stays between us!!"

    show mrsj 50
    show player 14
    player_name "I... I don't have a problem with that, {b}Mrs. Johnson{/b}..."

    show player 11
    show mrsj 52
    mrsj "But!!" with hpunch
    mrsj "Before we start with these lessons... I'll need something from you two."

    show player 5
    show mrsj 14
    show old_erik 4f
    erik "What do you need, {b}Mrs. Johnson{/b}?"

    show old_erik 1f
    show mrsj 19
    show player 13
    mrsj "... I've actually never had sex with two guys before."

    show mrsj 49
    mrsj "I'd like a book that shows sexual positions for more than two partners."

    mrsj "I've heard a book called {b}Kama Sutra{/b} describes ancient eastern positions."

    mrsj "See if you can find me that book."

    show mrsj 52
    mrsj "And there's one more thing..."

    show mrsj 14
    show old_erik 5f
    erik "Oh ya?"

    show old_erik 1f
    show mrsj 49
    mrsj "Well, if we're going to have sex, I have to make sure I don't get pregnant!"

    show mrsj 50
    player_name "..."
    show mrsj 49
    mrsj "I'll have to take {b}birth control pills{/b}..."

    show mrsj 50
    show old_erik 5f
    erik "Can't we use condoms?"

    show old_erik 1f
    show mrsj 52
    mrsj "Even with condoms, there's always a risk!!"

    show mrsj 49
    mrsj "And if I use the pill, we can do it raw..."

    show mrsj 50
    show player 83
    show old_erik 58f
    player_name "!!!"
    show player 82
    show mrsj 20
    pause
    mrsj "..."
    show mrsj 18
    mrsj "Haha!"

    show player 81
    player_name "!!!" with hpunch
    show player 78
    show mrsj 49
    mrsj "I can see you two are very excited about starting those sex lessons with me..."

    show mrsj 50
    show old_erik 56f
    erik "Sorry, {b}Mrs. Johnson{/b}."

    show old_erik 57f
    show mrsj 49
    mrsj "It's fine, pumpkin."

    show player 80
    mrsj "The sooner you two help me get what I need, the sooner we can start!"

    show mrsj 50
    show old_erik 58f
    erik "Okay, {b}Mrs. Johnson{/b}!"

    show old_erik 57f
    show player 83
    player_name "We will find you what you need, {b}Mrs. Johnson{/b}!"

    hide player
    hide old_erik
    with dissolve

    scene expression game.timer.image("erik_entrance{}_c")
    with fade
    show old_erik 4 at right
    show player 13 at left
    with dissolve
    erik "I can't believe {b}Mrs. Johnson{/b} is okay with having sex with us..."

    show old_erik 1
    show player 17
    player_name "I think we're lucky..."

    show player 13
    show old_erik 3
    erik "I've never had sex before..."

    show old_erik 3c
    show player 14
    player_name "Well, {b}Mrs. Johnson{/b} plans on teaching us how. And it's going to be awesome!"

    show player 13
    show old_erik 5
    erik "But how are we going to get that stuff she asked for?"

    show old_erik 1
    show player 34
    player_name "Hmm..."

    show player 35
    player_name "I think I got an idea."

    show player 13
    show old_erik 5
    erik "Oh ya?"

    show old_erik 1
    show player 14
    if player.has_item('birth_control_pills'):
        player_name "Well, {b}I already laid my hands on some of the contraceptive pills Mrs. Johnson talked about{/b}..."

    else:
        player_name "I'm sure {b}the hospital has the pills Mrs. Johnson talked about{/b}..."

    show player 33
    player_name "And we should be able to find the {b}Kama Sutra book at the library{/b}!"

    show player 13
    show old_erik 5
    erik "Saya harap Anda benar."

    show old_erik 1
    show player 14
    player_name "I'll come back when I find something..."

    hide player
    hide old_erik
    with dissolve
    return

label eriksroom_mrsj_fork_intro:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show player 1 at left
    show old_erik 4 at right
    with dissolve
    erik "Hey, man."

    erik "Did you end up talking to {b}Mrs. Johnson{/b}?"

    show player 14
    show old_erik 1
    player_name "Yeah, she thinks it might be a good idea to meet other girls..."

    show player 1
    show old_erik 5
    erik "Ah, benarkah?"

    show player 14
    show old_erik 1
    player_name "Yeah, I agree with her!"

    show old_erik 3c
    player_name "I can try and help you..."

    show player 11
    show old_erik 3b
    erik "I don't know, {b}[firstname]{/b}."

    show old_erik 3
    erik "I don't think I'll ever find someone who's right for me..."

    show player 10
    show old_erik 2
    with dissolve
    player_name "Apa?"

    show player 11
    show old_erik 3b
    with dissolve
    erik "Someone who's like me!"

    show player 10
    show old_erik 3c
    player_name "Apa maksudmu?"

    show old_erik 3b
    show player 11
    erik "I'm out of shape, I'm not good at talking to people..."

    show player 5
    erik "... Face it, man, I'm just a klutz..."

    show old_erik 3
    erik "... The only thing I'm good at is playing games!"

    show player 10
    show old_erik 3c
    player_name "Jadi?"

    show player 14
    player_name "What if we found you a gamer girl?"

    show player 1
    show old_erik 5
    erik "A gamer girl..."

    show old_erik 4
    erik "I... I guess so?"

    show player 4
    show old_erik 1
    with dissolve
    player_name "Hmm..."

    show player 14 with dissolve
    player_name "Do you know a girl at school who likes video games?"

    show player 11
    show old_erik 4
    erik "Well... There's this one girl from another class... She's kind of cute."

    show player 14
    show old_erik 1
    player_name "There's a girl at school that you like?"

    show player 1
    show old_erik 5
    erik "I don't know... She just seems... Nice!"

    show player 14
    show old_erik 1
    player_name "What's her name?"

    show player 1
    show old_erik 4
    erik "I think her name is {b}June{/b}."

    show player 14
    show old_erik 1
    player_name "Have you ever talked to her?"

    show player 1
    show old_erik 14
    erik "Well, this one time..."

    erik "... We, uh, I asked her about..."

    show player 11
    show old_erik 3
    erik "Tidak, tidak juga."

    show old_erik 3b
    erik "I think she borrowed one of my pencils, once..."

    show player 14
    show old_erik 3c
    player_name "Why don't you speak to her more?!"

    show player 11
    show old_erik 3
    erik "I can't!"

    show old_erik 3b
    erik "I'm WAY too shy..."

    erik "... And I don't even know what I would say to her."

    show player 35
    show old_erik 3c
    player_name "Okay, well, this might just be harder than I thought."

    show player 11
    show old_erik 3
    erik "Maybe we should just give up..."

    show old_erik 2 with dissolve
    erik "{i}*Huh*{/i}"

    show player 10
    player_name "Apa?!"

    show player 14
    show old_erik 3c
    with dissolve
    player_name "Come on, {b}Erik{/b}!"

    player_name "You'll see! I think she might like you..."

    player_name "Where does she usually hang out?"

    show player 1
    show old_erik 1
    erik "Hmm..."

    show old_erik 5
    erik "I've seen her in the computer lab many times before."

    show player 14
    show old_erik 1
    player_name "{b}The computer lab at school{/b}?"

    show player 1
    show old_erik 4
    erik "Yeah. It's on the second floor..."

    show player 14
    show old_erik 1
    player_name "I'll {b}go see her{/b}, maybe I can try and set something up for you."

    show player 1
    show old_erik 4
    erik "Okay, thanks, man."

    show old_erik 1 with None
    hide player
    hide old_erik
    with dissolve
    return

label eriksroom_mrsj_cupid_caught:
    scene expression "backgrounds/location_erik_house_bedroom_bed_june_day.jpg" with hpunch
    player_name "!!!"

    scene expression game.timer.image("erik_inside{}_b")
    with fade
    show player 10
    with fastdissolve
    player_name "Well... I guess I should leave {b}Erik{/b} alone for a while."

    hide player with dissolve
    return

label eriksroom_june_date_confession:
    scene expression game.timer.image("erik_house_bedroom{}_b")
    show old_erik 1 at right
    show player 10 at left
    with dissolve
    player_name "Hi {b}Erik{/b}... About {b}June{/b}..."

    show player 5
    show old_erik 5
    erik "Ya?"

    show player 10
    show old_erik 2
    with dissolve
    player_name "Well, I don't think it's going to work out..."

    show player 5
    show old_erik 3b
    with dissolve
    erik "Why? What happened?"

    show player 10
    show old_erik 3c
    player_name "Well, we spoke for a while..."

    show player 5
    show old_erik 3
    erik "Dan?"

    show player 10
    show old_erik 3c
    player_name "I just don't think she's that interested..."

    show player 5
    show old_erik 3
    erik "Oh..."

    show old_erik 3b
    erik "Tidak apa-apa."

    erik "I knew she wouldn't want to anyway..."

    show player 10
    show old_erik 3b
    player_name "She, uh... She might be coming over to my house later."

    show player 5
    show old_erik 5
    erik "Apa?!"

    show player 10
    show old_erik 3c
    player_name "I'm sorry!"

    player_name "While I was talking to her, one thing led to another..."

    player_name "We're just going to hang out..."

    show player 5
    erik "..."
    player_name "..."
    show player 10
    player_name "I'll, uh, talk to you later, then."

    hide player
    with dissolve

    scene expression game.timer.image("erik_entrance{}_c")
    with fade
    show player 24 at left
    with dissolve
    pause
    show mrsj 17 at right
    show player 11
    with hpunch
    mrsj "Ooops, sorry {b}[firstname]{/b}! I didn-"

    show mrsj 19c
    show player 24
    pause
    show mrsj 19
    mrsj "What's wrong, honey?"

    show mrsj 19c
    show player 10
    player_name "I don't think it's going to work out with {b}June{/b}..."

    show player 11
    show mrsj 19
    mrsj "The girl from school?"

    show player 10
    show mrsj 19c
    player_name "Ya."

    show player 5
    show mrsj 19
    mrsj "That's such a shame..."

    mrsj "Apa yang telah terjadi?"

    show player 10
    show mrsj 19c
    player_name "She's just not interested, and..."

    show mrsj 51
    player_name "... She might be coming over to my house later to hang with me."

    show player 5
    show mrsj 52
    mrsj "Oh my..."

    mrsj "Is {b}Erik{/b} okay with this?"

    show player 10
    show mrsj 51
    player_name "Probably not? He didn't say much..."

    show player 24
    show mrsj 52
    mrsj "I have to say... I'm a little disappointed in you, {b}[firstname]{/b}."

    show mrsj 51
    player_name "..."
    show mrsj 52
    mrsj "You knew {b}Erik{/b} liked her..."

    mrsj "... I thought he was your friend!"

    show player 25
    show mrsj 51
    player_name "I'm sorry, {b}Mrs. Johnson{/b}."

    player_name "I'll head home now."

    hide player
    with dissolve
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
