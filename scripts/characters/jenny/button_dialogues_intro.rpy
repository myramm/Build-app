label jenny_button_intro_bedroom_evening_j8:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset a_crossed
    with dissolve
    jenny "What the fuck are you doing?!"
    anon "Hmm?"
    anon "N-nothing... I just-"
    jenny "Get the hell out of my room, you perv!"
    anon f_skeptical "Why are you always in such a foul mood?"
    show jenny f_angry
    jenny "GET OUT OF MY ROOM, {b}[firstname!u]{/b}!!!" with hpunch
    show anon f_surprised a_rub with dissolve
    anon "Okay, okay... I'm going."
    hide anon with dissolve
    return

label jenny_button_intro_bedroom_evening_j16:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    with dissolve
    jenny "Oh my god, what do you want now?!"
    anon "N-nothing... I just-"
    jenny "You had better have a good reason for bothering me!"
    show anon f_surprised_teeth a_behind_head with dissolve
    anon @ -m_talk "..."
    show anon a_idle
    return

label jenny_button_intro_bedroom_evening_j20:
    scene expression player.location.background_closeup with None
    show anon f_normal a_wave
    show jenny f_upset
    with dissolve
    anon "Hey."
    show anon a_idle
    jenny "Hey."
    show anon f_worried
    pause
    anon "So, uhh..."
    anon "W-what's up?"
    jenny @ f_eyeroll "Oh my god..."
    jenny "Stop acting weird and get to the point."
    anon f_tired @ -m_talk "..."
    return

label jenny_button_intro_bedroom_evening_j21:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show jenny
    with dissolve
    anon "Hey."
    jenny "Hey."
    pause
    anon "You busy?"
    jenny "Not really, I'm just waiting on {b}Jane{/b} to call."
    anon "Oh, ehh... Cool."
    jenny @ f_eyeroll "..."
    jenny "What do you want, {b}[firstname]{/b}?"
    return

label jenny_button_intro_backyard_j21:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset b_swimsuit a_hips
    anon "Hey, {b}[jen_name]{/b}."
    jenny "Hey."
    pause
    anon f_confused "You uhh... Want me to rub some sunscreen on you or something?"
    show anon f_worried
    show jenny f_laugh
    jenny "Pfft, you wish!"
    show jenny f_grin
    pause
    jenny "Get naked and I'll think about it."
    anon "What?!"
    jenny "C'mon, take it out."
    anon f_skeptical "No way!"
    anon "{b}[deb_name]{/b} is right there, in the kitchen!"
    show jenny f_laugh
    jenny "Hahahaah!"
    show jenny f_grin
    jenny "It would be so fucking funny if she walked out here and you were naked!"
    anon f_worried "No it wouldn't..."
    anon "She would freak out!"
    jenny "I know!"
    show jenny f_laugh
    jenny "Hahahaah!"
    show jenny f_grin
    return

label jenny_button_intro_bedroom_j21:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    anon "Hey."
    jenny "Hey."
    pause
    jenny "You ready to do a show?"
    jenny "Get those clothes off!"
    anon f_confused "Ehh..."
    jenny "C'mon {b}[firstname]{/b}, my fans are waiting!"
    return

label jenny_button_intro_diningroom_j21:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_normal zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Morning."
    show jenny a_spoon f_normal with dissolve
    jenny "Morning."
    pause
    anon "You look nice today."
    jenny @ f_eyeroll "Heh, duh."
    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_looking_down_food a_resting with dissolve
    jenny "You coming to my room later?"
    anon f_surprised_food "I dunno, maybe?"
    show anon f_surprised_food
    jenny "You'd better."
    jenny "Lots of money to be made."
    anon f_normal "Yeah, I know."
    return

label jenny_button_intro_bedroom_j20:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset
    anon "Hey."
    jenny "Hey."
    show jenny f_gross
    pause
    anon "So, uhh..."
    anon "W-what's up?"
    show jenny f_eyeroll
    jenny "Oh my god..."
    show jenny f_upset
    jenny "Stop acting weird and get to the point."
    anon f_skeptical @ -m_talk "..."
    return

label jenny_button_intro_backyard_j20:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show jenny f_upset b_swimsuit a_hips
    anon "Morning."
    show jenny f_normal
    jenny "Morning."
    pause
    anon f_normal "It sure is nice out here today..."
    show jenny f_eyeroll
    jenny "Yup."
    show jenny f_gross
    pause
    anon @ -m_talk "..."
    show jenny f_upset
    jenny "Spit it out already!"
    jenny "I'm trying to relax here."
    anon f_worried @ -m_talk "..."
    return

label jenny_button_intro_diningroom_j20:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Morning."
    jenny "Morning."
    pause
    anon "You looking at your comments section again?"
    jenny "Yeah, these people are fucking nuts!"
    jenny "You should read some of the things they ask me to do..."
    anon "It's good money though, right?"
    jenny "Hell yeah!"
    show jenny f_upset
    jenny "Do you want something?"
    return

label jenny_button_intro_bedroom_j16:
    scene expression player.location.background_closeup with None
    show jenny f_eyeroll
    show anon f_worried
    jenny "Oh my god, what do you want now?!"
    show jenny f_upset
    anon "N-nothing... I just-"
    jenny "You had better have a good reason for bothering me!"
    anon @ -m_talk "..."
    return

label jenny_button_intro_backyard_j16:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_hips
    show anon f_worried
    anon "H-hey."
    jenny @ -m_talk "..."
    pause
    anon "I like your swimsui-"
    show anon f_surprised
    jenny "What do you want?!"
    anon f_worried "I don't-"
    show anon f_confused
    jenny "Spit it out or piss off!"
    jenny "I'm trying to relax here."
    anon @ -m_talk "..."
    return

label jenny_button_intro_diningroom_j16:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Morning."
    jenny "Yeah, yeah..."
    pause
    anon "What are you doing?"
    jenny "Ugh, these fucking assholes..."
    anon "Huh?!"
    jenny "Nothing... Never mind!"
    show jenny f_upset
    jenny "What do you want, {b}[firstname]{/b}?!"
    return

label jenny_button_intro_bedroom_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset a_crossed
    show anon f_worried
    jenny "What the fuck are you doing?!"
    anon "Hmm?"
    anon "N-nothing... I just-"
    show jenny f_angry
    jenny "Get the hell out of my room, you perv!"
    anon f_skeptical "Why are you always in such a foul mood?"
    show anon f_surprised
    jenny "GET OUT OF MY ROOM, {b}[firstname!u]{/b}!!!" with hpunch
    anon f_worried "Okay, okay... I'm going."
    hide anon with dissolve
    return

label jenny_button_intro_backyard_j8:
    scene expression player.location.background_closeup with None
    show jenny f_upset b_swimsuit a_hips
    show anon f_worried
    anon "H-hey."
    jenny @ -m_talk "..."
    pause
    anon "I like your swimsui-"
    show anon f_surprised
    jenny "Go away."
    anon @ -m_talk "..."
    anon f_confused "I was just trying to give you a compli-"
    jenny "I said, go away, loser!"
    jenny "I'm trying to relax here."
    anon "Tch, fine."
    hide anon with dissolve
    return

label jenny_button_intro_diningroom_j8:
    scene expression game.timer.image("dining_room{}")
    show jenny b_breakfast_dressed a_phone f_upset_down zorder 1
    show anon b_dinner_sitting_look_left f_worried zorder 0
    show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
    with dissolve
    anon "Morning."
    jenny @ -m_talk "..."
    pause
    anon "I said, good morn-"
    jenny "I heard you."
    jenny "Just shut up and leave me alone, loser..."
    anon f_tired "Tch, fine."
    show anon f_looking_down_eating a_eating with dissolve
    pause
    show anon f_looking_down_food a_resting with dissolve
    pause
    scene black with fade
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
