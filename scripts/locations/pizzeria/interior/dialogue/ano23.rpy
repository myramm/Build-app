label ano23_init_pizzeria_interior:
    call tony_button_stage

    show tony a_idle
    show tony f_smirk
    show anon f_worried a_sides with dissolve:
        xzoom -1
    tony "'Ey there, champ."
    anon "{b}Tony{/b}!"
    anon "You're not going to believe what happened!"
    tony "You had that talk with your old man, like we discussed?"
    anon f_confused "Huh?"
    pause
    anon f_normal "Oh... yeah, I did."
    anon f_worried "But never mind that!"
    anon "There's been a huge development!"
    tony @ a_frustrated "Heh, alright... alright."
    tony "Calm down, would ya?"
    anon "I was walking home from the graveyard and one of those Russian goons stopped me."
    tony f_angry "Again?!"
    tony "He didn't hurt ya did he?"
    tony "'Cause I swear to god, I'll rip his fuckin'-"
    anon "No, no, no... {b}Tony{/b}, just listen!"
    anon "He picked me up and threw me into the back of this limousine..."
    anon "... And the mob boss' daughter was inside waiting to talk to me."
    tony f_surprised "Wait, what?!"
    tony "{b}Raz{/b} has a daughter?"
    anon "Yeah."
    anon "And it turns out, she wants him dead too."
    tony f_smirk "Heh, no kiddin'?"
    pause
    tony @ f_laugh "I guess the apple didn't fall far from the tree, eh?"
    anon "Yeah, I guess not."
    pause
    anon f_normal "Anyways, she offered me a deal."
    show tony a_sides f_laugh with {'master': dissolve}:
        xoffset -550
        xzoom 1
    tony "Heh, this oughta be rich..."
    hide tony with dissolve
    show tony f_smirk with {'master': dissolve}:
        xoffset 32
        xzoom -1
    tony "... Well, go on... let's hear it."
    anon "She said she knows of a secret entrance into the warehouse."
    tony f_suspicious "A secret entrance, eh?"
    anon "And she's willing to show us, if we do a job for her first."
    tony f_angry "See, now I knew there was gonna be a catch."
    anon f_worried "Apparently, {b}Raz{/b} has hidden something away down at {b}Saga Financial{/b}."
    tony f_suspicious "{b}Saga Financial{/b}?"
    tony "Ain't that {b}Tina{/b}'s bank?"
    anon @ f_laugh "Exactly!"
    anon "I figured we go and speak with {b}Tina{/b}, see if she'll let us have a peek, and then we can-"
    tony f_angry @ a_frustrated "Are you outta ya fuckin' mind?!"
    anon f_worried "Huh?"
    tony @ a_point "Didn't I tell you about my promise to Luigi?!"
    anon "Y-yeah, but-"
    tony "And now you honestly think I'm gonna let her mixed up in this mess!"
    anon "{b}Tony{/b} that's not-"
    tony a_crossed "It's out of the question, champ!"
    show anon f_sad_down
    pause
    anon "Okay, you're right."
    anon "I'm sorry."
    show tony f_sad
    pause
    tony "Look, I get it, champ."
    tony a_frustrated "I know how bad you want this... for your old man."
    anon @ -m_talk "..."
    tony "But jumpin' in bed with a Ruskie... tsk, it's a bad idea."
    tony a_idle "You ain't gotta look no further than your old man's grave for proof of that."
    anon "{i}*Sigh*{/i} I know."
    pause
    anon f_sad "But what if this is the only chance I'm gonna get?"
    show tony f_suspicious a_mc_hip_single
    show tony_arms_dressed_a_mc_shoulder_single:
        xoffset 32
        xzoom -1
    with dissolve
    tony "Aww, c'mon champ."
    show anon f_shy
    tony "We'll figure somethin' else out, I promise ya."
    show anon f_thinking
    pause
    anon f_worried "You know, there is another person who might be able to help us..."
    tony f_smirk "{i}*Snort*{/i} Alright, wise guy... who would that be?"
    anon f_normal "{b}Liu Kim{/b}."
    tony f_question "Who in the heck is {b}Liu Kim{/b}?"
    anon "She's the one who took me down to the vault last time."
    tony "Last time?"
    pause
    tony f_normal "Oh, right... when you went looking for your old man's empty lockbox!"
    anon @ -m_talk "Mhmm."
    anon "She said she was friends with my father too!"
    anon "I'm sure she'd help us if I asked her."
    tony f_suspicious "I dunno, champ..."
    anon "C'mon, we can at least go and see what {b}Raz{/b} is hiding, right?"
    anon "Aren't you curious?"
    hide tony_arms_dressed_a_mc_shoulder_single
    show tony f_angry a_crossed
    with {'master': dissolve}
    tony "Well, of course I'm curious!"
    tony "But that don't mean-"
    anon "There's no harm in taking a peek."
    anon "If anything seems suspicious, we'll just bail and pretend nothing ever happened."
    tony f_thinking a_thinking @ -m_talk "Hmm."
    pause
    tony f_smirk a_idle "Alright, fuck it."
    tony "Go talk to whatever you said her name was..."
    anon "{b}Liu Kim{/b}."
    tony @ f_eyeroll "Uh huh."
    show tony a_anon_hug1 f_surprised
    hide anon
    with {'master': dissolve}
    tony "!!!"
    anon "Thank you, {b}Tony{/b}!"

    if M_tony.watches:
        tony f_normal_down "Yeah, alright champ."
        show tony a_anon_hug2 with dissolve
        pause
        show anon b_dressed a_sides f_normal:
            xzoom -1
        show tony a_idle f_normal
        with {'master': dissolve}
    else:
        show anon b_dressed a_sides f_surprised:
            xzoom -1
        show tony a_calm_down f_smirk
        with {'master': dissolve}
        tony "C'mon, get outta here with that!"
        show anon f_normal of_blush
        show tony a_idle
        with {'master': dissolve}
        anon "S-sorry."
        anon m_talk "I'm just-"
        show anon -m_talk -of_blush with {'master': dissolve}
        anon "Seriously, thank you!"
        tony f_normal "No worries, champ..."

    tony "Just don't go expectin' me to get all buddy-buddy with this Ruskie broad, eh?"
    tony "They'll claw your fuckin' eyes out if you ain't careful."
    anon "Heh, okay."
    tony "Go on now, get."
    show anon:
        xoffset 500
        xzoom 1
    show tony f_surprised a_point_under
    with {'master': dissolve}
    tony "Oh!"
    show tony f_suspicious a_idle
    show anon f_surprised:
        xoffset 0
        xzoom -1
    with dissolve
    tony "And not a word of this to {b}Maria{/b}, capiche?"
    tony "She's got enough to worry about."
    anon f_normal "You got it."
    tony "Attaboy."
    hide anon
    show tony a_crossed f_smirk
    with dissolve
    pause
    tony "Heh."
    tony "How 'bout that..."
    maria "Who ya talkin' to up there?!"
    show tony a_idle f_suspicious with dissolve:
        xoffset -368
        xzoom 1
    tony "What?!"
    tony "Nobody."
    maria "Oh, so ya just talkin' to yourself then?"
    maria "Old man."
    tony f_smirk @ a_frustrated "Heh, ya just can't stop bustin' my balls for two seconds, can ya?"
    maria "Hehe, nope."
    hide tony with {'master': dissolve}
    maria "Now gimme some sugar."

    scene expression background(l=L_pizzeria_exterior) with fade
    show anon with dissolve
    anon @ -m_talk "( Alright, now {b}I just need to speak with Liu{/b}. )"
    anon @ -m_talk "( I'm sure she'll help us. )"
    pause
    anon @ -m_talk "( She's usually behind the front desk down at {b}Saga Financial{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
