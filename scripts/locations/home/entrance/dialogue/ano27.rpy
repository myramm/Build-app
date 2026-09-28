label ano27_yumi_home_lobby:
    scene location_home_entrance_cutscene05
    show text _ ("My worst fears were realized the second Yumi came into view.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The Russians had finally come to make good on their threats.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("A wave of dizzyness washed over me as a million different scenarios rushed through my head each worse than the last.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("I had to find [deb_name] and [jen_name].") as caption with dissolve
    pause

    scene location_home_entrance_floor
    show yumi b_dressed_hurt_floor f_wincing o_bruised
    with fade
    anon "{b}[deb_name]{/b}?!"
    anon "{b}[jen_name]{/b}?!"
    show yumi f_sad
    show anon b_dressed_legs:
        xoffset -50
    with {'master': dissolve}
    anon "!!!"
    show anon b_dressed_floor f_frown_down behind yumi with dissolve:
        crop (0, 0, 1024, 600)
        offset (-250, 0)
        xzoom -1
    anon "{b}Yumi{/b}... y-you're hurt..."
    show anon f_worried_low
    yumi "Ngh, the Russians-"
    show yumi f_wincing
    pause
    yumi f_sad "They came in force... I tried to-"
    anon f_surprised_low "Oh my god!"

    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        anon "{b}[jen_name]{/b}!!"
    else:
        anon "{b}[deb_name]{/b}!!"

    hide anon
    show yumi a_grab_hand f_eyeroll
    with dissolve
    yumi "It's no use!"
    show yumi a_idle f_sad
    show anon b_dressed_legs behind yumi:
        xoffset -400
    with dissolve
    anon "What do you mean?!"
    yumi "They took them."
    anon "The Russians did?!"
    show yumi f_wincing
    pause 0.5
    yumi f_sad "Yeah."
    anon "Where?!"
    yumi @ -m_talk "Hmm?"
    show anon b_dressed_floor f_worried_low with dissolve:
        crop (0, 0, 1024, 650)
        offset (-180, -20)
        xzoom -1
    anon "Where did they take them?"
    yumi "Ngh, dunno..."
    yumi "... They kept askin' about some briefcase..."
    show anon f_surprised_low
    yumi "... {b}[deb_name]{/b} said she didn't know anything about it."
    show yumi f_wincing
    pause
    yumi f_sad "Then they hauled them away, kicking and screaming."
    anon f_frown_down "Dammit!"
    show anon b_dressed_legs with dissolve:
        reset
    anon "Those sons of bitches... I'll kill them!"
    show anon with {'master': dissolve}:
        offset (490, -15)
        xzoom -1
    yumi "Stop!"
    anon "!!!"
    show anon with {'master': dissolve}:
        offset (-180, -20)
        xzoom 1
    yumi "Y-you can't-"
    yumi f_wincing @ -m_talk "Ngh!"
    pause
    yumi f_sad "I radioed backup..."
    yumi "... They should be-"
    show anon with {'master': dissolve}:
        offset (650, -60)
        xzoom -1
    harold "{b}Yumi{/b}!!!"
    show anon:
        offset (0, -50)
        xzoom 1
    show harold b_dressed_floor f_worried_down
    with {'master': dissolve}
    harold "Oh my god!"

    if M_helen.finished_state(S_helen_route_split) and not M_helen.is_state(S_helen_mia_breakdown):
        show harold b_dressed_floor_hug
        show yumi f_wincing
        with dissolve
        harold "Those fucking animals!"
        harold "I was so worried, I-"
        yumi @ -m_talk "Ngh."
        show harold b_dressed_floor
        show yumi f_sad
        with dissolve
        harold "Sorry."
        harold "L-lemme have a look."
    else:
        harold "You're bleeding!"
        yumi "Y-yeah, I know."

    show harold a_yumi_arm with {'master': dissolve}
    yumi "It all happened so fast, I didn't even get a shot off."
    show harold a_idle with {'master': dissolve}
    harold "Yeah, this is bad."
    show yumi f_wincing
    pause 0.5
    yumi f_sad "I'm sorry, I should have-."
    harold "Hey, focus!"
    harold "You need to keep pressure on it!"
    harold a_yumi_arm "Jesus, they roughed you up bad..."
    anon "Is she gonna be okay?"
    show harold f_worried_right_up
    harold "Yeah, it's nothing fatal and there's an ambulance en route."
    anon "Alright then... you stay with her, I'm going after them!"
    show harold a_grab_anon1 f_angry_right_up
    hide anon
    with dissolve
    harold "The hell you are!"
    anon "Get off me, {b}Harold{/b}!"
    harold "I'm not letting you out of my-"
    show harold a_grab_anon2 with {'master': dissolve}
    anon "I SAID GET OFF ME!" with hpunch
    show harold f_worried_right_up
    show yumi f_surprised
    anon "They've got my friends!"
    anon "Do you have any idea what they're gonna do to them?!"
    yumi f_sad "{b}[firstname]{/b}, please..."

    if False:
        show harold a_yumi
        show anon b_dressed_legs:
            offset (-50, 10)
        with dissolve
        anon "{b}Harold{/b}'s gonna wait on the ambulance with you... You're gonna be okay."
        show harold f_worried_down
        show anon b_dressed_floor_hug_yumi:
            offset (0, 0)
        show yumi f_wincing
        with dissolve
        anon "{b}[deb_name]{/b} and {b}[jen_name]{/b} need me now."
        show yumi f_down
        yumi "N-no, they'll kill you..."
        show yumi f_sad
        show anon b_dressed_legs
        show harold f_worried_right_up
        with dissolve
    else:
        show harold a_yumi
        show anon b_dressed_legs
        with {'master': dissolve}

    anon "I'm going after them."
    harold "I can't let you do that, son... it's too dangerous."
    anon "Yeah?"
    anon "Well, you better shoot me then because that's the only way you're gonna stop me."
    harold "{b}[firstname]{/b}..."
    show anon with {'master': dissolve}:
        xoffset 850
        xzoom -1
    yumi "Please, don't-"
    hide anon with dissolve
    harold f_angry_right_up "{b}[firstname!u]{/b}!!!"
    pause
    harold "Gosh darnit!"

    scene expression background(176, 400, 3., l=L_maria_lounge) as underlay:
        xoffset -400
    show tony b_casual a_phone_talk:
        xoffset -500

    $ renpy.dynamic(stage=background(584, 504, 3, l=L_home, t=3))
    show expression stage as stage
    with fade
    show anon a_phone f_worried_low with dissolve:
        xoffset 500
    anon @ -m_talk "( This is really bad... I can't leave the girls in the hands of those monsters! )"
    show anon a_phone_talk f_worried with {'master': dissolve}
    "{i}*Ring* *Ring*{/i}"
    anon @ -m_talk "( I've gotta infiltrate the place tonight! )"
    "{i}*Ring* *Ring*{/i}"
    show expression stage as stage at phoneleft with phoneleft.show
    tony f_normal "Yeah, go for {b}Tony{/b}."
    anon "{b}Tony{/b}!!"
    anon "I've got a problem, man!"
    tony f_surprised "Champ?!"
    anon "A big, big, problem!!"
    tony f_sad "Whoa, slow down..."
    anon "They took 'em, {b}Tony{/b}!"
    anon "They're gone!"
    show tony a_phone f_surprised_down with {'master': dissolve}:
        xoffset -150
        xzoom -1
    tony "Who's gone?"
    anon "My friends, {b}Tony{/b}!"
    anon "The Russians hit my house!"
    show tony f_surprised
    maria "WHAT?!"
    show maria b_casual_magic f_surprised_down behind tony with {'master': dissolve}:
        xoffset -325
    maria "I thought you said, the cops were guardin' the place?"
    show tony f_surprised_down
    anon "They were..."
    anon "... Or they are..."
    anon @ f_annoyed "Whatever... it doesn't matter."
    show maria f_sad_down
    show tony f_angry_down
    anon "They shot the cop and kidnapped my friends!"
    maria "Your landlady and her daughter?"
    tony "Those god damn Ruskie bastards!"
    anon "Yeah, we've gotta go after them!"
    show maria f_sad
    tony "Ya goddamn right we're goin' after 'em, champ!"
    tony "{b}Meet me at the pizzeria{/b}, I gotta get Vera."
    show anon f_surprised
    show tony f_question
    maria f_annoyed "Hey, I'm comin' too!"
    tony "Huh?"
    tony "Not to the warehouse, you ain't!"
    show anon f_confused
    maria f_eyeroll "Well, of course not to the warehouse!"
    maria f_angry "But you two knuckleheads ain't rushin' in there without me seein' you both off first!"
    tony f_suspicious "Alright, that's fine... but get that beautiful rear in gear..."
    show maria f_sad
    tony "... Every second counts, darlin'!"
    maria "Yeah, okay."
    show tony f_sad_down
    maria f_sad_down "We'll be right there, {b}[firstname]{/b}!"
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon f_worried_low a_phone "Okay, I guess {b}we're going to the pizzeria{/b} then..."
    show anon a_idle f_worried with {'master': dissolve}:
        xoffset 0
        xzoom -1
    anon @ -m_talk "( I should hurry. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
