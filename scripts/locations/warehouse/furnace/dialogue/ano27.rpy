label ano27_peek_bazooka:
    scene expression background(912, 400, 5) as stage
    show anon f_surprised_low a_bazooka_look with dissolve
    anon @ -m_talk "( Holy crap, is that one of those explodey things?! )"
    anon @ -m_talk "( What are they called? )"
    anon @ -m_talk "( Bazookas or something... )"
    pause
    anon @ -m_talk "( ... Seems like a pretty dangerous thing to leave lying around. )"
    hide anon with dissolve
    return


label ano27_yolo_bazooka:
    scene expression background(912, 400, 5) as stage
    show anon f_worried_low a_bazooka_look with dissolve
    anon @ -m_talk "( Hmm, do I dare? )"
    show anon f_thinking
    pause
    anon f_normal_low @ -m_talk "( No guts, no glory... as they say. )"
    anon f_angry a_bazooka @ -m_talk "( Let's see what these jerks think of this! )"

    scene location_warehouse_attack_cutscene01a with fade
    pause

    scene location_warehouse_attack_cutscene01b
    anon "Alright you Russian assholes!!!" with hpunch

    scene location_warehouse_attack_cutscene02a with fastfade
    goon "What the hell?!"
    goon "Who let child into warehouse?!"
    goon "He looks like the kid boss is wanting dead..."

    scene location_warehouse_attack_cutscene01c with fastfade
    anon "Yeah, that's right."
    anon "I'm the one your boss wants dead."
    pause
    anon "And I'm also the one pointing a bazooka at your big ugly melon..."
    anon "... So you should really be asking yourself, \"Do I wanna go home original style or extra crispy?!\""

    scene location_warehouse_attack_cutscene02b with fastfade
    goon "Is this joke?"
    goon "Smells like he shit himself..."
    goon "Pfft, hahahahaaah!!"

    scene location_warehouse_attack_cutscene01c with fastfade
    anon "This is no joke!"
    anon "Drop your guns and get on the floor or I'll blow this place sky high!"

    scene location_warehouse_attack_cutscene02b with fastfade
    goon "I didn't know this was bring daughter to work day!"
    goon "Why nobody tell me?!"
    goon "Hahahaah!"

    scene location_warehouse_attack_cutscene03a with fastfade
    anon "Alright, have it your way."

    scene location_warehouse_attack_cutscene03b with dissolve
    "{i}*Click*{/i}"

    scene location_warehouse_attack_cutscene04
    show text _ ("Yeah, I know what you're gonna say...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("... Total idiot, right?") as caption with dissolve
    pause

    scene location_warehouse_attack_cutscene05
    show text _ ("To be honest, it's hard to argue.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("But in my defense, I had never seen a rocket propelled grenade before!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("So much for my career as an action hero...") as caption with dissolve
    pause

    scene location_warehouse_attack_cutscene06a with fade
    anon "Ngh."
    pause
    anon "W-what happened?"
    pause

    scene location_warehouse_attack_cutscene06b with dissolve
    anon "Whoa."
    anon "I did not see that coming..."
    goon "You stupid little shit!"

    scene location_warehouse_attack_cutscene06c with dissolve
    anon "Huh?!"
    goon "I'll rip out your eyes and shove them up your ass!"

    scene location_warehouse_attack_cutscene06d with dissolve
    anon "H-hold on a second fellas..."
    anon "... I was just joking about the extra crispy thing... seriously you don't have to-"

    scene location_warehouse_attack_cutscene06e
    "!!!" with hpunch
    goon "Arrgghh!!!"

    scene location_warehouse_attack_cutscene06f with dissolve
    anon "Huh?!"
    pause
    anon "What the-"

    scene location_warehouse_attack_cutscene07a with fastfade
    anon "{b}Father Keeves{/b}?!"
    pause

    scene location_warehouse_attack_cutscene08a with fastfade
    anon "( Wow, I'm really glad he's on my side... )"

    scene location_warehouse_attack_cutscene07b with fastfade
    keeves "Don't just sit there, kid!"
    keeves "Get to cover!!"

    scene location_warehouse_attack_cutscene08a with fastfade
    anon "Oh, right."
    anon "Cover."
    anon "G-good idea!"

    scene location_warehouse_attack_cutscene08b with dissolve
    anon "Hmm?"

    scene location_warehouse_attack_cutscene08c with dissolve
    anon "Oh, crap!"
    pause
    anon "Umm..."
    anon "... Could either of you point me in the direction of some cover?"
    anon "I'm feeling a little exposed here."
    goon "You die now!"

    scene location_warehouse_attack_cutscene09a with fastfade
    anon "S-say, have you met my friends, {b}Tony{/b} and {b}Harold{/b}?"
    goon "Huh?!"

    scene location_warehouse_attack_cutscene09b with dissolve
    tony "I'm comin' champ!"
    harold "Get out of there, {b}[firstname]{/b}!"

    scene location_warehouse_attack_cutscene10 with fastfade
    "{i}*Bonk*{/i}"
    tony "How do you like that, ya cabbage eatin' Ruskie bastard!"
    goon "Hurk!!"
    harold "Get behind me, son!"

    scene location_warehouse_attack_cutscene11
    show text _ ("The scene had turned into complete chaos!!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("{b}Harold{/b} and {b}Father Keeves{/b} were dropping goons left and right...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... And {b}Tony{/b} was charging about, bellowing like a mad man!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The Russians didn't stand a chance.") as caption with dissolve
    pause

    scene location_warehouse_attack_cutscene17
    show text _ ("And then it was over... just like that.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("An entire warehouse full of armed men, laid to waste in seconds.") as caption with dissolve
    pause

    scene expression background(712, 480, 5, l=L_warehouse_depot) as stage
    show harold b_tanktop a_gun_down f_angry:
        xoffset 300
        xzoom -1
    show tony b_casual_exhausted:
        xoffset -100
        xzoom -1
    with fade
    tony "{i}*Huff*{/i} {i}*Puff*{/i}"
    tony "Jesus."
    harold "I think we got them all."
    tony "I gotta... lay off the pizza rolls..."
    tony "{i}*Huff*{/i} {i}*Puff*{/i}"
    show harold a_gun_side f_worried_down with {'master': dissolve}:
        xoffset -200
        xzoom 1
    harold f_worried_down "You alright?"
    show harold f_worried
    show tony a_pipe_hold_shoulder b_casual
    with {'master': dissolve}
    tony "Are you kiddin'?!"
    tony "I feel great!"
    show harold f_suspicious
    tony "Been too long since I had action like this!"
    harold f_concerned "I'm sorry I doubted you earlier."
    harold "That was a hell of a show you put on back there."
    tony f_smirk "Heh, you weren't too bad yourself, cupcake."
    tony "They teach you to shoot like that at the academy?"
    harold f_smirk "Damn right."
    tony "Well, color me impressed."
    show harold f_worried with {'master': dissolve}:
        xoffset 300
        xzoom -1
    harold "What about you, son?"
    harold "You okay?"
    show anon f_worried a_sides with {'master': dissolve}:
        xoffset 100
        xzoom -1
    anon "Y-yeah, I think so..."
    tony "How in the hell did you blow the door?"
    anon f_confused @ -m_talk "Hmm?"
    tony @ f_laugh "We was startin' to worry they'd got ya, champ..."
    show anon f_worried
    show harold f_normal
    tony "... But then BOOM!"
    harold "Yeah, it was good thinking."
    harold "Orchestrated chaos."
    anon f_shy a_behind_head "Yeah, uhh..."
    pause
    anon a_sides "... I totally meant to do that!"
    anon "A-all part of the plan."
    show tony f_thinking with {'master': dissolve}:
        xoffset -500
        xzoom 1
    tony "Where'd {b}Silverdick{/b} go?"
    show harold f_eyeroll
    anon f_worried_high "Huh?"

    scene location_warehouse_attack_cutscene07c with fade
    anon "Whoa, he's gone!"
    tony "Yeah, that's what I was getting at..."

    scene expression background(712, 480, 5, l=L_warehouse_depot) as stage
    show harold b_tanktop a_gun_side:
        xoffset 300
        xzoom -1
    show tony b_casual a_pipe_hold_shoulder:
        xoffset -100
        xzoom -1
    show anon a_sides f_confused:
        xoffset 100
        xzoom -1
    with fade
    anon "B-but where did he go?!"
    harold f_worried "Let's worry about that later, huh?"
    harold "We still need to find {b}[deb_name]{/b} and {b}[jen_name]{/b}."
    show tony f_sad
    anon f_worried "Yeah, you're right."
    anon "{b}Nadya{/b} said that {b}Raz{/b}'s office is on the second floor..."
    anon "... So the girls are probably down here somewhere."
    tony "Well, let's clear it out!"
    tony @ a_pipe_point_forward "Startin' with that room there."
    anon "Y-yeah, okay."
    harold "Right behind ya."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
