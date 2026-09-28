label hospital_storage_funtime:
    scene location_hospital_sex with fade
    show player 11f at Position(xpos=.7,ypos=1.0) with dissolve
    pause
    show old_roz 4 at left with dissolve
    show player 13f
    pause
    show old_roz 5
    roz "Surprised to see you back so soon. I must have left an impression."
    show player 14f
    show old_roz 4
    player_name "Y-yeah. You were really good!"
    show player 13f
    show old_roz 5
    roz "Hah, well, you don't get to be my age without learning a few tricks, kiddo."
    show old_roz 8 with dissolve
    pause
    show old_roz 9
    roz "Well then..."
    roz "What shall I do to you today?"

    menu:
        "Blowjob." if M_consuela.finished_state(S_con02_scam):
            hide old_roz
            hide player
            jump hospital_storage_funtime.blowjob

        "Sex." if M_roz.finished_state(S_roz_obits_collect):
            jump hospital_storage_funtime.sex

    return


label hospital_storage_funtime.blowjob:
    show anon f_worried:
        flip
    show roz f_smirk:
        flip
    with dissolve
    roz "I could really go for a snack."
    anon "A snack?"
    show roz a_teeth_take f_remove_teeth with dissolve
    pause
    show roz a_teeth_hold f_smirk_teethless with dissolve
    roz @ -m_talk "Mmhmm."
    anon @ f_sad_down "Oh god..."
    roz "Don't you worry, kiddo."
    show roz b_dressed_kneeling a_idle with dissolve
    show anon f_worried_low
    roz "{b}Old Roz{/b} will take real good care of you..."
    anon "Oh god!"

    call scene_roz_blowjob from hospital_storage_funtime.resume_blowjob

    scene location_hospital_sex
    show anon b_dressed_disheveled f_depressed a_cover_boner:
        flip
    show roz b_dressed_kneeling f_smirk_teethless:
        flip
    with fade
    anon "..."
    show roz b_dressed a_teeth_take f_remove_teeth with dissolve
    pause
    roz a_idle f_smirk "Well, I feel better."
    roz "How about you?"
    anon "Hmm?"
    pause
    anon f_tired "O-oh, yeah... Thanks."
    roz "My pleasure, kiddo."
    roz "You come back and see ol' {b}Roz{/b} again real soon. Ya hear?"
    anon f_depressed "S-sure thing."
    hide anon
    hide roz
    with dissolve
    return


label hospital_storage_funtime.sex:
    call scene_roz_sex from hospital_storage_funtime.resume_sex

    scene location_hospital_sex
    show player 1f at Position(xpos=.7,ypos=1.0)
    show old_roz 13 at left
    with fade
    pause
    show old_roz 15 with dissolve
    roz "You done good today, kiddo."
    roz "Seeing lots of improvement."
    show player 29f
    show old_roz 14
    with dissolve
    player_name "Really? Heh, thanks. I guess..."
    show player 3f
    show old_roz 15
    roz "My pleasure, {b}[firstname]{/b}."
    roz "You come back and see ol' {b}Roz{/b} again real soon. Ya hear?"
    show player 29f
    show old_roz 14
    player_name "S-sure thing."
    hide old_roz
    hide player
    with dissolve
    return


label roz02_hospital_sex:
    scene location_hospital_sex
    show player 12 at center with dissolve
    player_name "I'm pretty sure {b}Roz{/b} said the box would be here."
    show player 11 zorder 2
    player_name "But I don't see it..."
    player_name "Maybe she moved it and forgot?"
    show old_roz 5 zorder 1 at left with dissolve

    roz "Need some help?"
    show player 23f at Position(xpos=.7,ypos=1.0)
    show old_roz 4
    with fastdissolve
    player_name "Whoa!"
    show player 22f
    player_name "..."
    show player 10f
    player_name "Oh, he-hey {b}Roz{/b}... You scared me!"
    show player 11f
    show old_roz 5
    roz "Ahh, don't be so dramatic!"
    roz "I'm just here to give you a hand."
    show player 10f
    show old_roz 4
    player_name "Uhh yeah, okay."
    player_name "Are you certain the box is in here?"
    player_name "I can't seem to find it."
    show player 11f
    show old_roz 5
    roz "No?"
    roz "That's odd."
    roz "I suppose it's possible I brought the box down already and it just slipped my mind."
    roz "This old noggin ain't as sharp as it used to be."
    show old_roz 4
    player_name "..."
    show player 10f
    player_name "O-okay... No problem, I'll just run downstairs and-"
    show player 22f
    show old_roz 6

    player_name "!!!" with hpunch
    show old_roz 7
    roz "Not so fast."
    roz "Seems to me like we have a few moments of privacy here..."
    roz "... And I've just thought of something else you can do for me."
    show player 38f
    show old_roz 6
    with dissolve
    player_name "Oh uh, s-sure. What did you have in mind?"
    show player 3f
    show old_roz 7
    with dissolve
    roz "Here's the thing, {b}[firstname]{/b}."
    roz "It's been a looooong time since this old bird got some action..."
    roz "You know what I mean?"
    show player 10f
    show old_roz 6
    with dissolve
    player_name "Umm, a-action?"
    show player 11f
    show old_roz 7
    roz "That's right."
    roz "Action."
    show old_roz 10 with dissolve
    pause


    show old_roz 8 with dissolve
    pause .2
    show player 23f
    player_name "!!!" with hpunch
    show player 42f with dissolve
    player_name "Whoa! {b}Roz{/b}, what are you doing?"
    show old_roz 9
    roz "What's it look like I'm doin'?"
    roz "Get those clothes off and let's see what you're packin' down there."
    show player 10f
    show old_roz 8
    with dissolve
    player_name "Wait you wanna-"
    player_name "B-but I can't do that!"
    show player 11f
    show old_roz 9
    roz "You want those {b}records{/b} or not?"
    show player 10f
    show old_roz 8
    player_name "Well, yeah, I {i}really{/i} need them but-"
    show player 11f
    show old_roz 9
    roz "Well then, what are ya babblin' about?"
    roz "You help me and I help you, got it?"
    show player 24f
    show old_roz 8
    player_name "{i}*Sigh*{/i} I got it."
    show old_roz 9
    roz "Good!"

    call scene_roz_sex from roz02_hospital_sex.resume

    scene location_hospital_sex
    show player 5f at Position(xpos=.7,ypos=1.0)
    show old_roz 4 at left
    with fade
    pause
    show old_roz 12 with dissolve
    roz "Here's the {b}records{/b}."
    show player 12f
    show old_roz 11
    player_name "You've had them this whole time?!"
    show player 462
    show old_roz 5
    with dissolve
    roz "Of course, I told ya I knew where they were."
    show old_roz 4
    player_name "..."
    show old_roz 5
    roz "I'm not sure what name you're looking for..."
    roz "... But {b}if they're in the graveyard, then you'll find them in there{/b}."
    show old_roz 13 with dissolve
    pause
    show player 463
    show old_roz 14
    with dissolve
    player_name "Thanks, I guess."
    show player 462
    show old_roz 15
    roz "My pleasure, kiddo."
    roz "Do come back and see me again..."
    roz "... Ya know, if you need anything else."
    show old_roz 14
    pause
    show old_roz 15
    roz "Like maybe a second round?"
    show old_roz 14
    hide old_roz with dissolve
    pause
    show player 37f with dissolve
    player_name "( I... Can't believe I just had sex with {b}Roz{/b}. )"
    player_name "( She's old enough to be my grandmother! )"
    show player 24f with dissolve
    player_name "( At least I got the {b}obituary records{/b}. )"
    player_name "( I sure hope that shipwright is in there somewhere. )"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
