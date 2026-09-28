label bridget_dialogue_eve_dress_code_intro_repeat:
    anon f_worried "Actually, I was hoping you could talk to {b}Mrs. Smith{/b} about the new dress code policy..."
    bridget a_crossed "Ah, ah, ah!"
    bridget f_sexy "You remember our deal?"
    show bridget b_pickup with dissolve
    show anon f_worried_low
    pause
    show bridget b_dressed a_ropes with dissolve
    show anon f_unimpressed
    bridget "You help me..."
    show bridget a_ropes_throw with dissolve
    pause
    show bridget a_idle
    show anon a_ropes_bunch
    with dissolve
    bridget "... And I help you."
    anon f_tired "{i}*Sigh*{/i} Yeah, I remember."
    bridget a_hips "Untangle those and then we'll talk."
    hide bridget with dissolve
    anon f_sad_down "..."
    scene black with fade
    pause
    return

label bridget_dialogue_eve_dress_code_failure_first:
label bridget_dialogue_eve_dress_code_failure_repeat:
    scene expression player.location.background_closeup
    show anon a_ropes_tangled f_hurt
    show bridget
    with fade
    bridget "Well, how are things progressing in-"
    show bridget f_surprised
    anon f_tired "Ehh, it's not going so well..."
    bridget f_normal @ f_laugh a_laugh "Hahahaah!"
    bridget "How did you even-"
    anon f_unimpressed "I have no idea!"
    bridget "Here, let me help you."
    scene black with fade
    pause
    scene expression player.location.background_closeup
    show anon a_rub
    show bridget a_ropes
    with dissolve
    bridget "There."
    anon f_worried "Sorry, {b}Coach Bridget{/b}."
    bridget @ f_sexy "Heh, no worries..."
    bridget "You can just try again tomorrow."
    anon f_sad_down "..."
    bridget "Unless you no longer need my help with whatever it is you were whining about earlier?"
    anon f_tired "The dress code policy."
    bridget "Yeah, that..."
    pause
    bridget a_crossed "See you tomorrow?"
    anon f_sad_down "Yeah, okay."
    hide bridget with dissolve
    anon f_thinking a_thinking @ -m_talk "( Hmm, if only I wasn't so clumsy... )"
    anon @ -m_talk "( Maybe {b}I should speak with that Muay Thai trainer at the Gym{/b}? )"
    hide anon with dissolve
    return


label bridget_dialogue_eve_dress_code_success_first:
label bridget_dialogue_eve_dress_code_success_repeat:
    scene expression player.location.background_closeup
    show anon a_ropes f_grin
    show bridget
    with fade
    bridget "Well, how are things progressing in-"
    show bridget f_surprised
    anon @ f_laugh "I just got the last one untangled!"
    bridget f_sexy "Wow, nice work {b}[firstname]{/b}!"
    bridget f_normal a_hips "I figured that was going to take you weeks to sort out..."
    anon f_normal "Well, I'm sure glad it didn't!"
    anon "Will you help me out with the dress code thing now?"
    bridget "That depends on what exactly you want me to do?"
    bridget "You should know that I don't really give a damn what you kids wear while you're here at school."
    anon f_worried "That's not the part that bothers me..."
    anon "Did you know {b}Mrs. Smith{/b} was disallowing hair dye?"
    show bridget f_surprised
    pause
    bridget f_angry "What?!"
    anon "Yeah, for both students and faculty..."
    bridget "Over my dead body she is!"
    hide bridget with dissolve
    anon f_confused "So, you'll talk to her about-"
    anon f_worried @ -m_talk "( Whoa, she stomped off in a hurry... )"
    anon @ -m_talk "( I should probably follow her. )"
    scene black with fade
    pause
    scene expression "backgrounds/location_school_third_sideview_day.jpg" with None
    show anon b_dressed_bending1:
        flip
        xoffset -200
    with dissolve
    pause
    scene expression "backgrounds/location_school_office_spying.jpg"
    show bridget f_angry:
        flip
    show smith
    with fade
    bridget "Over my dead body you're disallowing hair dye!"
    smith "Oh, come now, {b}Bridget{/b}..."
    smith "You're too old to be dying your hair anyways!"
    bridget "My age is none of your concern!"
    bridget "I like my hair and nobody is making me change it, least of all you!"
    smith "You can't speak to me like that!"
    bridget "The hell I can't!"
    bridget "You're infringing my rights, and I'm not going to stand for it!"
    smith "Good grief, calm down!"
    smith "{i}*Sigh*{/i} I'll have {b}Annie{/b} shelf the stupid policy tomorrow, alright?!"
    smith "It was all her stupid idea anyway..."
    smith @ f_eyeroll "The girl can't even write a simple dress code policy without causing me headaches..."
    bridget "It's not like we need a dress code anyways, it's a public school!"
    smith "Yeah, yeah, you've already won, {b}Bridget{/b}..."
    smith "Just get out before I lose my patience."
    bridget "Tch, whatever."
    hide bridget
    show bridget f_eyeroll:
        xoffset -400
    with dissolve
    bridget "... You old bitch."
    hide bridget with dissolve
    smith "..."
    scene expression "backgrounds/location_school_third_sideview_day.jpg" with None
    show anon b_dressed_bending1:
        flip
        xoffset -200
    with dissolve
    anon "( Whoa, she's really laying into her! )"
    pause
    anon "( Oh crap, she's coming out! )"
    hide anon
    show anon f_surprised_teeth b_dressed a_rub:
        flip
    show bridget:
        flip
    with dissolve
    bridget @ -m_talk "..."
    anon a_idle f_worried @ a_rub "S-so... {i}*Ahem*{/i} H-how did it go?"
    bridget "It's all taken care of."
    anon f_surprised @ f_shock "Seriously?!"
    bridget "Yup."
    bridget "You can tell your friend or whatever that there's nothing to worry about."
    anon f_normal "Thanks, {b}Coach Bridget{/b}!"
    bridget @ -m_talk "Mhmm."
    hide bridget with dissolve
    anon f_grin "( Wow, {b}Coach Bridget{/b} isn't afraid of {b}Mrs. Smith{/b} at all! )"
    anon "( I can't wait to tell {b}Eve{/b} the good news tomorrow! )"
    hide anon with dissolve
    return

label bridget_dialogue_eve_dress_code_intro_first:
    scene expression player.location.background_blur with None
    show anon f_worried_low
    show bridget b_pickup with dissolve
    bridget "Ugh, where there hell did those damn things run off to?!"
    anon "E-excuse me, ma'am?"
    bridget "Yeah, yeah... Hold on one second, will ya!"
    bridget "{i}*Sigh*{/i} I know I threw them in here somewhere!"
    anon "Can I help you find something?"
    bridget "No, I'm just looking for the jump ropes..."
    bridget "I wanna use them next class and-"
    bridget "There you are!"
    show bridget b_dressed a_ropes f_angry_down with dissolve
    show anon f_worried
    bridget "Good lord!"
    anon f_surprised_teeth "!!!"
    bridget "Look at this disaster!"
    show anon f_worried
    bridget f_angry "It's gonna take me days to unravel this mess!"
    anon "Yeah, that really sucks..."
    anon f_surprised @ f_confused "Anyways, I was really hoping you could help me with-"
    bridget f_sexy "Nu uh!"
    anon f_worried "B-but I haven't even told you what I need yet!"
    bridget "If you want my help, you're gonna help me with this first."
    anon f_unimpressed "Ah, man..."
    show bridget a_ropes_throw with dissolve
    bridget "There ya go, enjoy!"
    show bridget a_idle
    show anon f_surprised_teeth_down a_ropes_bunch
    with dissolve
    bridget f_normal "Come find me when you're finished and MAYBE I'll help you out."
    anon f_tired "Y-yes, ma'am..."
    hide bridget with dissolve
    anon f_sad_down "..."
    scene black with fade
    pause
    return

label bridget_button_dress_code_track:
    anon f_worried "Actually, I was hoping you could talk to {b}Mrs. Smith{/b} about the new dress code policy..."
    bridget "Not now, {b}[firstname]{/b}!"
    bridget "Can't you see we're in the middle of class here?!"
    hide bridget with dissolve
    anon f_confused "O-oh, sorry."
    anon f_thinking a_thinking @ -m_talk "( Hmm, I should wait and speak with her in her office {b}after school{/b}. )"
    hide anon with dissolve
    return

label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show anon f_worried
    show bridget f_angry
    with dissolve
    bridget "{b}[firstname]{/b}!"
    bridget "What are you doing in here?"
    show anon f_shock
    show bridget a_crossed with dissolve
    anon "Sorry, ma'am!!!"
    anon "I just had some questions!"
    show anon f_surprised
    bridget "Questions?!"
    bridget "Like what?"
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show anon f_worried
    show bridget f_angry
    with dissolve
    bridget "{b}[firstname]{/b}!"
    bridget "You better {b}be training your ass off at the gym{/b}, or I'm going to shove my foot up your ass!!"
    show anon f_shock
    show bridget a_crossed with dissolve
    anon "Yes, ma'am!!!"
    show anon f_surprised
    bridget "Got any questions?!"
    return

label coach_bridget_dialogue_training_advice:
    show anon f_worried
    show bridget a_crossed f_normal
    anon "I... Well, where should I train?"
    show bridget f_angry
    bridget @ -m_talk "..."
    show anon f_surprised
    bridget "I just told you!"
    bridget @ f_angry_yell "At the GYM!!!"
    anon f_worried "But... What should I train?"
    bridget "You have to work on your {b}strength{/b} and {b}dexterity{/b} if you want to make it!"
    bridget "You'll be competing in the 110-meter hurdles to qualify this school and your team into the state championship!"
    anon "That's... A lot of pressure."
    show anon f_surprised_teeth
    bridget "... And you better NOT fail me!"
    show anon f_surprised
    anon "Yes, ma'am!!!"
    hide bridget
    hide anon
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show anon f_worried
    show bridget a_crossed f_normal
    anon "I... I forgot."
    bridget f_angry "Forgot? Boy you are the saddest piece of meat I've ever seen!"
    show anon f_surprised
    bridget @ f_angry_yell "Now get out of here and get to WORK!!"
    anon f_shock "Yes, ma'am!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
