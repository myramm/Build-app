label hospital_second_floor_room_jizz_checkup:
    scene expression "backgrounds/location_hospital_room_day_blur.jpg"
    show player 13f at right
    show diane b_casual:
        flip
    with dissolve
    diane "Brr, why are these exam rooms always so cold?!"
    show player 14f
    player_name "I know, right?"
    show diane b_casual_remove1 with dissolve
    pause 1
    show diane b_casual_remove2 with dissolve
    player_name "It's like they want you to be-"
    show player 427f
    show diane b_casual_remove3 with dissolve
    player_name "..."
    show diane b_casual_remove4 with dissolve
    pause
    show diane b_casual_remove5 with dissolve
    diane "Want you to be what?"
    show diane b_casual_remove6 with dissolve
    pause
    $ M_diane.outfit.is_naked = 1
    show diane b_naked with dissolve
    show player 429ef
    player_name "..."
    diane "{b}[firstname]{/b}?"
    player_name "Hmm?"
    diane "What were you saying?"
    show player 10f
    player_name "Was I saying something?"
    show player 5f
    show diane f_laugh a_facepalm with dissolve
    diane "Hehe, yes..."
    show diane f_normal a_idle with dissolve
    show player 14f
    player_name "I completely forgot."
    show player 13f
    pause
    show player 429f
    player_name "You look amazing!"
    show player 426f
    diane f_shamed a_touch @ f_shamed_smile_back "Oh, stop."
    show player 429f
    player_name "I'm serious!"
    show player 426f
    show diane b_gown_dress f_down_front with dissolve
    pause
    show diane b_gown a_idle f_shamed_look
    show player 13f
    with dissolve
    diane f_shamed @ f_shamed_look "Even in this ugly hospital gown?"
    show player 17f
    player_name "Even in the hospital gown!"
    show player 13f
    show diane f_laugh
    diane "Hehe, thanks, {b}[firstname]{/b}."
    show diane f_shamed_smile
    diane "Excuse me while I lay down."
    show diane f_shamed
    show player 14f
    player_name "Sure."
    scene expression "backgrounds/location_hospital_bed.jpg"
    show diane b_gown_turn:
        unflip
    show player 426 at left
    with dissolve
    pause
    show diane b_gown_bed f_normal
    show player 13
    with dissolve
    diane "Ugh, I hope they don't leave us in here waiting forever."
    show player 14
    player_name "Yeah, me too."
    show player 13
    pause
    "{i}*Knock* *Knock*{/i}"
    diane "Oh, thank goodness."
    diane "Come in."
    pause
    show micoe:
        xoffset 200
    with dissolve
    micoe "Hello."
    diane "Hi."
    micoe "What can I do for you all today?"
    show diane f_shamed_smile
    diane "I umm..."
    diane "Hehe, sorry I'm a little nervous."
    show diane f_shamed
    micoe "No problem."
    show diane f_shamed_smile
    diane "We're uhh... Gonna try and have a baby..."
    show diane f_shamed
    micoe @ f_laugh "Oh, that's wonderful!"
    show diane f_shamed_smile
    diane "... And I just wanted to get checked out, you know?"
    diane "I'm not as young as I used to be..."
    show diane f_shamed
    micoe "I completely understand."
    micoe "Is this your... Husband?"
    show diane f_laugh
    diane "Husband?!"
    diane "Hahaha, goodness no!"
    show diane f_normal
    diane "This is my-"
    show diane f_shamed_smile
    diane "My uhh..."
    show diane f_shamed
    pause
    show player 14 with None
    show micoe:
        flip
        xoffset -200
    with dissolve
    player_name "Boyfriend."
    show player 13
    show diane f_normal
    diane "Right!"
    show diane f_laugh with None
    show micoe:
        unflip
        xoffset 200
    with dissolve
    diane "Boyfriend, haha!"
    show diane f_shamed_smile
    diane "... Sorry, I'm still a little-"
    show diane f_shamed
    show player 14 with None
    show micoe:
        flip
        xoffset -200
    with dissolve
    player_name "I wanna get checked out too."
    show player 13
    show diane f_normal
    diane @ -m_talk "Hmm?!"
    show player 14
    player_name "Is that something we can do?"
    show player 13
    show micoe f_normal
    micoe "... Sure."
    micoe "If that's what you want, I'll grab a test kit."
    hide micoe with dissolve
    pause
    show player 17
    player_name "See, I'll be getting poked and prodded too."
    show player 13
    diane "Aww, {b}[firstname]{/b}..."
    pause
    diane "You are just the sweetest man, ever!"
    show micoe a_cup3:
        flip
        xoffset -100
    with dissolve
    micoe "Here you go."
    micoe "I just need you to ejaculate into this cup, and we'll take it downstairs for testing."
    show micoe a_idle
    show player 691b
    with dissolve
    player_name "Alright."
    show player 261bf with dissolve
    show micoe f_sad
    micoe "Whoa!"
    show micoe f_laugh
    micoe "Haha, in the bathroom tiger!"
    show micoe f_normal
    show player 29 with dissolve
    player_name "Oh!"
    player_name "Heh, sorry."
    show player 3
    diane @ f_laugh "Haha!"
    micoe "I'll take your girlfriend over to see the OB/GYN while you're doing that, and I'll come right back for the sample."
    show player 29
    player_name "Yeah, okay."
    show player 14 with dissolve
    player_name "Unless, you want me to come with?"
    show player 13
    diane "No, it's okay."
    hide micoe
    show micoe:
        xoffset 150
    with dissolve
    diane "I'll be fine."
    micoe "If you'll follow me, ma'am."
    show diane b_gown a_idle:
        xoffset 50
    with dissolve
    diane "S-sure."
    scene black with fade
    scene expression "backgrounds/location_hospital_room_day_blur.jpg"
    show player 14 with dissolve
    player_name "Alright, I guess I should get started {b}in the bathroom{/b}."
    hide player with dissolve
    return

label clinic_erik_bully_fight_concussion:
    scene hospital_bed_night
    show player 392 at Position (xpos=805, ypos=665)
    show micoe f_sad
    with fade
    micoe "Hello, how-"
    micoe @ -m_talk "..."
    micoe @ -m_talk "Hum hum!!"
    player_name "Uh..."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe f_laugh
    with dissolve
    micoe "Oh good! You're starting to wake up."
    show micoe f_normal
    micoe "How are you feeling?"
    show player 398 at Position (xpos=772, ypos=664)
    player_name "I..."
    show player 397 at Position (xpos=772, ypos=660)
    player_name "I feel fine."
    show player 394 at Position (xpos=768, ypos=660) with dissolve
    player_name "A bit dizzy actually."
    pause
    show player 396 at Position (xpos=772, ypos=660) with dissolve
    player_name "Where am I?"
    show player 397
    micoe "You're in the hospital."
    show player 398 at Position (xpos=772, ypos=664)
    player_name "I am?"
    show player 397 at Position (xpos=772, ypos=660)
    micoe @ f_laugh "That's right!"
    micoe "And I'm {b}Nurse Micoe{/b}."
    if M_diane.finished_state(S_diane_jizz_checkup):
        micoe "We met, remember?"
        if M_diane.finished_state(S_diane_jizz_checkup_extra_hand):
            show micoe f_full
            show player 395 at Position (xpos=772, ypos=660)
            pause
            show micoe f_wink
            pause
            show player 393 at Position (xpos=772, ypos=660)
    show micoe f_sad
    micoe "You had a minor concussion, but you'll be fine."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe f_normal
    micoe "You can go home when you feel ready."
    micoe "Just make sure to drink plenty of water and get some rest."
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Oh, I see... Thank you."
    show player 397 at Position (xpos=772, ypos=660)
    micoe "I forgot to mention that you have a visitor!"
    hide micoe with dissolve
    pause
    show player 393
    pause
    show old_erik 4f at left with dissolve
    erik "Hey, {b}[firstname]{/b}!"
    erik "How are you doing?"
    show old_erik 1f
    show player 395
    player_name "Hey {b}Erik{/b}. I'm fine, I think!"
    show player 393
    show old_erik 5f
    erik "{b}Dexter{/b} really got you good, huh."
    show old_erik 1f
    show player 395
    player_name "Nah, {b}Dexter{/b} punches like a girl!"
    show player 393
    show old_erik 4f
    erik "Heh heh."
    erik "Thanks for standing up for me today."
    show old_erik 1f
    show player 395
    player_name "It's alright."
    show player 393
    show old_erik 5f
    erik "No one has ever stood up to {b}Dexter{/b} before."
    show old_erik 4f
    erik "Everyone in the school is talking about it."
    show old_erik 1f
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Eh... I wish it didn't have to go that way..."
    player_name "... And I still got my ass kicked!"
    show player 393 at Position (xpos=772, ypos=660)
    show old_erik 4f
    erik "Well, {b}Dexter{/b} will think twice before he does something like that again."
    show old_erik 1f
    show player 395
    player_name "Heh! We'll see about that."
    show player 393
    pause
    show old_erik 4f
    erik "Hey, I overheard the nurse say you can go home."
    erik "Ready?"
    show old_erik 1f
    show player 395
    player_name "Yeah."
    show player 393
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
