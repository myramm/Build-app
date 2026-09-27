label mrsjsroom_erik_feed_found:
    scene erik_house_cs01_01b
    show text _ ("This was the first time I had ever been in {b}Mrs. Johnson{/b}'s room.\nI knew her and {b}Erik{/b} had an unusual relationship...\nI didn't expect to see him... Breastfeeding...") as caption
    with fade
    pause

    scene erik_house_cs02
    show text _ ("The look on their faces said everything...\n... I was not supposed to be there. Everything would've been fine...\n... If only I had knocked first.\nInstinctively, I closed the door and decided I should leave.") as caption
    with fade
    pause

    scene expression game.timer.image("erik_entrance{}_c")
    show player 22 at left
    with fade
    show old_erik 2 at Position (xpos=750)
    show mrsj 52 at right
    with dissolve
    mrsj "{b}[firstname]{/b}?!"

    mrsj "I... What are you doing here?"

    show mrsj 38
    show player 37 with dissolve
    player_name "{b}Erik{/b}?!"

    show old_erik 3b with dissolve
    player_name "I... Um... Was just trying to find you."

    show player 24 with dissolve
    show old_erik 3
    erik "{b}[firstname]{/b}..."

    show old_erik 2 with dissolve
    show player 25
    player_name "I heard voices and I thought..."

    show player 11
    show old_erik 3b
    erik "I... I just want to be in my room right now."

    show old_erik 2
    show mrsj 19b
    mrsj "It's fine I-"

    hide old_erik with dissolve
    show mrsj 19c
    show player 22
    mrsj "..."
    show mrsj 20
    mrsj "Listen, what you saw just now is something... Normal!"

    show player 5
    show mrsj 19
    mrsj "I'm just trying to get him out of his shell, {b}[firstname]{/b}."

    show mrsj 19c
    show player 10
    player_name "It's fine, {b}Mrs. Johnson{/b}."

    player_name "I didn't mean to walk in on you guys like that..."

    show player 5
    pause
    show player 10
    player_name "Can you just tell {b}Erik{/b} that I'm sorry?"

    show player 5
    show mrsj 19
    mrsj "Don't worry about him. He'll be fine..."

    mrsj "It's just... {b}Erik{/b} doesn't seem to see or talk about many girls, so I try and..."

    show player 11
    mrsj "... I give him a little womanly attention!"

    mrsj "I thought I could get him off his computer if he could just... Have a little taste!"

    show mrsj 19c
    show player 5
    player_name "..."
    show mrsj 19
    mrsj "Can you just... You know. Keep this between us?"

    mrsj "I don't think he would want the other kids at school to find out."

    show mrsj 19c
    show player 10
    player_name "It's fine, {b}Mrs. Johnson{/b}. I won't tell anyone."

    hide player
    hide mrsj
    with dissolve
    return

label mrsjsroom_erik_learn_prep:
    scene erik_house_upstairs_night_c01
    show mrsj 14 at right
    with None
    show old_erik 4f at Position (xpos=300)
    show player 13 at left
    with dissolve
    erik "Hey, {b}Mrs. Johnson{/b}."

    show old_erik 1f
    show mrsj 17
    mrsj "Hi, boys!"

    mrsj "How are you two doing?"

    show mrsj 14
    show old_erik 4f
    erik "We found some things that may help you... With our lessons."

    show old_erik 1f
    show player 239_240 with dissolve
    pause
    show player 425 with dissolve
    player_name "Here's what I found, {b}Mrs. Johnson{/b}!"

    show player 13
    show mrsj 63
    with dissolve
    mrsj "Oh, wonderful!"

    mrsj "I'll have to prepare for our little lessons together..."

    mrsj "Maybe you two should visit me at night in my room... Or, should I call it, our classroom!"

    mrsj "Haha."

    hide player
    hide old_erik
    with dissolve

    scene expression game.timer.image("erik_entrance{}_c")
    with fade
    show player 13 at left
    show old_erik 4 at right
    with dissolve
    erik "When should we visit {b}Mrs. Johnson{/b}?"

    show old_erik 1
    show player 14
    player_name "I'll try and stop back over as soon as I can..."

    player_name "But you should do it with her whenever you want!"

    show player 13
    show old_erik 4
    erik "Saya kira Anda benar..."

    erik "Thanks for helping me with this, {b}[firstname]{/b}."

    hide player
    hide old_erik
    with dissolve
    return

label mrsjroom_mrsj_private_yoga_intro:
    show player 435 at left
    show mrsj 53 at Position(xpos=734,ypos=650)
    player_name "Could I see your private yoga lessons?"

    show mrsj 54
    show player 434
    mrsj "Well, I have a few special positions I always wanted to try."

    mrsj "I just never had anyone to do them with... Unless you think you could help me?"

    show mrsj 53
    show player 435
    player_name "Sure, {b}Mrs. Johnson{/b}, I'd love to help!"

    label mrsjroom_mrsj_private_yoga_shortcircuit:
    show mrsj 54
    show player 434
    mrsj "You think you have enough energy to keep up?"

    show mrsj 53
    show player 435
    player_name "I can try!"

    show mrsj 54
    show player 434
    mrsj "Okay. Start by taking off your clothes..."

    show mrsj 53
    show player 8 with fastdissolve
    pause
    show player 8b with fastdissolve
    pause
    show player 431b with fastdissolve
    pause
    show player 431 with vpunch
    show mrsj 54
    mrsj "Wah!"

    mrsj "I don't think I've ever seen something this excited for yoga!"

    mrsj "Why don't you lay down on the bed and get comfortable with me?"

    scene erik_upstairs_night_c2
    show mrsjsex 33 at topright
    with fade
    mrsj "You like this view?"

    show mrsjsex 34
    player_name "It's really nice..."

    show mrsjsex 33
    mrsj "Keep your eyes on me, I want to show you a neat little trick."

    show mrsjsex 35 with fastdissolve
    pause 0.05
    show mrsjsex 36 at Position(yoffset=70) with fastdissolve
    pause 0.2
    show mrsjsex 36_37
    player_name "Wah..."

    pause
    return

label mrsjroom_mrsj_private_yoga_pos1:
    show mrsjsex 37 at Position(yoffset=60)
    pause 0.2
    show mrsjsex 38 with fastdissolve
    pause 0.2
    show mrsjsex 39 at Position(yoffset=87) with fastdissolve
    mrsj "Let's move on to my next pose..."

    mrsj "... Something to help me stretch?"

    scene erik_upstairs_night_c3
    show mrsjsex 40 at Position(xpos=580,ypos=710)
    with fade
    mrsj "This position is more fun..."

    mrsj "... You just try and stay still, let me do the work..."

    show mrsjsex 40
    mrsj "You're so BIG, {b}[firstname]{/b}..."

    show mrsjsex 41 with fastdissolve
    pause 0.5
    show mrsjsex 42 at Position(xoffset=-14) with fastdissolve
    pause 0.5
    show mrsjsex 43 at Position(xoffset=-20) with fastdissolve
    pause 0.5
    show mrsjsex 44 at Position(xoffset=-30) with fastdissolve
    mrsj "Aaah... So deep..."

    player_name "{b}Mrs. Johnson{/b}, you feel so good..."

    mrsj "I'm gonna start moving now, try to hold it in for more than a few minutes, {b}[firstname]{/b}."

    show mrsjsex 45 at Position(xoffset=-23)
    pause 0.2
    show mrsjsex 46 at Position(xoffset=-19)
    pause 0.2
    show mrsjsex 42_43_44_45_46
    pause
    mrsj "Yes!! Keep going..."

    pause
    return

label mrsjroom_mrsj_private_yoga_pos2:
    hide screen erimom_private_pos2_sex_options
    show mrsjsex 42_43_44_45_46
    mrsj "Hold me tight, {b}[firstname]{/b}..."

    mrsj "... Cum inside me!"

    player_name "Apa kamu yakin?"

    mrsj "Yes, I need to feel your energy!"

    show mrsjsex 47 at Position(xoffset=-34) with vpunch
    mrsj "AAH!!!"

    show white zorder 4
    pause 0.3
    hide white with dissolve
    mrsj "Ya..."

    mrsj "I love the feeling of all that energy flowing, dripping..."

    player_name "Isn't doing it inside dangerous?"

    show mrsjsex 48 at Position(xoffset=-13) with dissolve
    mrsj "I'm on the pill, you don't have to worry about that, honey..."

    scene erik_upstairs_night_c2
    show mrsj 56 at right
    show player 426 at left
    with fade
    mrsj "You... You did great, {b}[firstname]{/b}."

    show player 429
    show mrsj 55
    player_name "Are you okay, {b}Mrs. Johnson{/b}?"

    show player 426
    show mrsj 56
    mrsj "I'm fine, just a little tired..."

    mrsj "I hope I won't be too sore to do yoga tomorrow."

    show player 427
    show mrsj 55
    player_name "Is... {b}Erik{/b} okay with us spending time together?"

    show player 428
    show mrsj 56
    mrsj "Oh, he's not thinking about this right now..."

    show player 426
    mrsj "He's far too busy spending time with his new girlfriend."

    mrsj "I think you can learn a lot if you keep coming to my lessons..."

    mrsj "... But I think I need a nap right now."

    mrsj "Feel free to come back, I'll be waiting here in the evenings."

    show player 429
    show mrsj 55
    player_name "Tentu, {b}Ny. Johnson{/b}!"

    return

label mrsjroom_mrsj_3some_intro:
    show mrsj 39 at right
    show old_erik 1f at Position(xpos=300)
    show player 21 at left
    player_name "{b}Erik{/b} and I were wondering if you could teach us things?"

    show player 13
    show old_erik 4f
    erik "Yeah, we'd like to try... Having sex."

    show mrsj 40
    show old_erik 1f
    mrsj "I was hoping you two would come visit me for some lessons."

    show mrsj 39
    show player 21
    player_name "Benar-benar?"

    show player 13
    show old_erik 4f
    erik "What do you want us to do, {b}Mrs. Johnson{/b}?"

    show mrsj 40b
    show old_erik 1f
    mrsj "Well, I was reading this wonderful book you brought me..."

    show mrsj 40
    mrsj "... And I think I have just the right thing for us!"

    mrsj "How about I show you two a few positions?"

    show mrsj 39
    show player 21
    player_name "Se-sex positions?"

    show player 13
    show mrsj 40
    mrsj "Why don't you take off your clothes and join me in bed?"

    mrsj "You can follow my instructions..."

    show old_erik 55f at Position(xoffset=-8)
    show player 8 at Position(xoffset=-27)
    with fastdissolve
    mrsj "... And let me do the rest."

    scene erik_upstairs_night_c3
    show mrsjsex 20 at topright
    with fade
    mrsj "Let's start with this one!"

    mrsj "I'll be on top of you, pumpkin, while I use my mouth on {b}[firstname]{/b}..."

    mrsj "... Try not to cum too fast!"

    mrsj "I want to try a few positions."

    erik "Okay, {b}Mrs. Johnson{/b}..."

    show mrsjsex 21_22_23_24_25 with fastdissolve
    pause
    erik "{b}Mrs. Johnson{/b}..."

    erik "It feels so good... Inside you..."

    return

label mrsjroom_mrsj_3some_pos1:
    show mrsjsex 26
    mrsj "How about we try something different..."

    mrsj "... I'd like you boys to take me on my back."

    show mrsjsex 27 at Position(xanchor=0,xpos=200,ypos=100) with fade
    mrsj "Yes, {b}[firstname]{/b}, just like that..."

    mrsj "... I want to feel both of you at the same time."

    show mrsjsex 28 at Position(yoffset=42) with fastdissolve
    mrsj "Ahh... Yes!"

    show mrsjsex 28_29_30
    mrsj "Faster!!"

    return

label mrsjroom_mrsj_3some_pos2:
    hide screen mrsj_3some_pos2_sex_options
    show mrsjsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
    pause
    show mrsjsex 31 at Position(xoffset=60,yoffset=42) with hpunch
    mrsj "Ahhh!!!"

    show white zorder 4
    pause 0.3
    hide white with dissolve
    pause
    show mrsjsex 32 with fastdissolve
    mrsj "You've made a real mess with all that cum!"

    player_name "I came inside... Is that okay?"

    mrsj "Well, It's a good thing I started taking the pill..."

    player_name "Sorry, {b}Mrs. Johnson{/b}."

    mrsj "It's okay, honey. I love the feeling of cum dripping out of my..."

    mrsj "... Erm, I think we should take a break."

    scene erik_upstairs_night_c2
    show mrsj 56 at right
    show player 426 zorder 2 at left
    show old_erik 59f zorder 1 at Position(xpos=300)
    with fade
    mrsj "My goodness..."

    show old_erik 60f
    show mrsj 55
    erik "Are you okay, {b}Mrs. Johnson{/b}?"

    show old_erik 59f
    show mrsj 56
    mrsj "Just a little tired, pumpkin..."

    mrsj "... But you both did amazingly well."

    mrsj "I think I need a nap after all this!"

    mrsj "You boys feel free to come back another day..."

    show mrsj 55
    show old_erik 60f
    erik "Come on, we should leave and let {b}Mrs. Johnson{/b} rest."

    show old_erik 59f
    scene expression "backgrounds/location_erik_house_inside_night_blur.jpg"
    show old_erik 4 at right
    show player 1 at left
    with fade
    erik "That was amazing!!"

    show old_erik 1
    show player 17
    player_name "Yeah, {b}Mrs. Johnson{/b} is awesome..."

    show old_erik 4
    show player 1
    erik "I never thought it would feel this good..."

    show old_erik 1
    show player 14
    player_name "I think she really liked it too!"

    show old_erik 4
    show player 1
    erik "You need to come by again, so we can have more fun..."

    show old_erik 1
    show player 14
    player_name "I'll try to come by soon, I promise!"

    show old_erik 4
    show player 1
    erik "I'll go play some games in my room, talk to you later."

    show old_erik 1
    show player 14
    player_name "Cool, I'll see you then!"

    hide old_erik
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
