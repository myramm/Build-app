label ano22_init_pizzeria_interior:

    python hide:
        if M_maria.outfit.get == 'casual':
            renpy.dynamic(M_maria=util.struct(
                outfit='apron' if 3 <= M_maria.pregnancy.stage < 5 else 'dressed',
                pregnancy=M_maria.pregnancy))

    call tony_button_stage

    show tony a_idle f_normal
    show anon f_worried a_sides with dissolve:
        xzoom -1
    tony "Well, look who finally showed up."
    anon "Hey, {b}Tony{/b}."
    tony "We was startin' to worry about ya, champ."
    anon f_sad_down "Y-yeah, sorry... I-"
    show tony f_suspicious a_whisper with {'master': dissolve}:
        xoffset -400
        xzoom 1
    tony "'Ey, {b}Maria{/b}!"
    tony "The kid's here!"
    show tony f_smirk a_idle:
        xoffset 0
        xzoom -1
    with {'master': dissolve}
    tony "We saw the cops leadin' {b}Mayor Rump{/b} away in handcuffs on the TV the other night..."
    tony f_suspicious "... Did you have somethin' to do with that?"
    anon f_unimpressed "Yeah, but the cops are taking all the credit."
    tony f_normal "Heh, of course... The cops can't have people knowin' how incompetent they are."
    anon "I guess."
    pause
    tony "How'd you do it anyways?"
    anon @ -m_talk "Hmm?"
    anon f_worried "Oh, umm..."
    anon "... I convinced his wife and daughter to help me."
    tony f_smirk @ f_surprised "!!!"
    tony "His wife AND daughter?!"
    anon "Yeah?"
    tony "Don't tell me you honeydicked 'em?"
    anon f_confused "Ehh?"
    tony a_point "You charmed the pants right off 'em, didn't ya?!"
    anon f_shy "Oh, umm... yeah, kinda... I guess..."
    tony "Ahh, c'mere you!"
    show tony a_sides with dissolve:
        xoffset -550
        xzoom 1
    hide tony with dissolve
    pause .4
    show tony a_frustrated f_laugh behind anon:
        xzoom -1
    show anon f_surprised a_up
    with {'master': dissolve}
    anon "W-wait a second, I-"
    show tony a_scrub f_normal_down:
        xoffset 200
    hide anon
    with dissolve
    anon "!!!"

    if M_tony.watches:
        tony "I knew ya could do it, ya little lady killer!"
        tony "I'm so damn proud of ya!"
    else:
        tony "You're like a spindly little James Bond, you know that?!"
        tony "I guess I'd better keep my eye on you, eh?!"
        tony @ f_laugh "Hahaha!"

    show tony a_idle f_normal:
        xoffset 132
    show anon a_rub f_shy:
        xoffset 25
        xzoom -1
    with dissolve
    anon "Heh, thanks {b}Tony{/b}."
    show tony f_normal_right
    show maria a_mouth b_magic f_surprised:
        xoffset -200
        xzoom -1
    show anon f_surprised
    with {'master': fastdissolve}
    maria "Oh my gawd!"
    show tony f_surprised_down
    show maria b_magic_hug_boobs1 f_surprised_down:
        xoffset 232
    hide anon
    maria "We was so worried about you!" with hpunch
    show maria b_magic_hug_boobs2
    with {'master': dissolve}
    anon "{i}*Mmmrrphhhl*{/i}"
    show tony f_eyeroll with {'master': dissolve}:
        xoffset -400
        xzoom 1
    tony "I told ya he was gonna be fine, {b}Maria{/b}..."
    show tony f_smirk:
        xoffset -50
        xzoom -1
    with {'master': dissolve}
    tony "... More than fine, actually."
    tony "From the sounds of it, he took {b}Rump{/b} down all by himself."
    show tony a_idle
    show anon f_shy behind maria:
        xoffset 100
        xzoom -1
    show maria b_magic f_sad:
        xoffset 200
    with dissolve
    maria "So you {i}were{/i} involved in that mess?!"
    anon "It wasn't a mess, everything went fine."
    anon "I had help from-"
    show tony a_quiet f_suspicious with {'master': dissolve}
    tony "{i}*Ahem*{/i}"
    show anon f_worried
    pause
    show tony a_idle with {'master': dissolve}
    anon "F-from the..."
    anon "... Staff... people."
    maria a_idle f_confused "{b}Rump{/b}'s staff turned on him?"
    anon "Err, yeah."
    anon "You know, cause he treated them so poorly and all."
    maria f_normal @ f_eyeroll "Oh, I can just imagine."
    pause
    tony "So what all did you find in his safe?"
    anon "Some off-shore accounts full of mob money, the deeds to several properties here in Summerville, and a recording of him and {b}Raz{/b} discussing my father's murder."
    show maria f_surprised a_mouth m_talk
    show tony f_surprised
    with {'master': dissolve}
    maria "{i}*Gasp*{/i}"
    tony "No kiddin'?"
    show maria b_magic_hug_boobs1 f_surprised_down -m_talk:
        xoffset 232
        xzoom -1
    hide anon
    with {'master': dissolve}
    maria "Oh, you poor thing!"
    maria "That's just awful."
    show tony a_frustrated f_angry_down with {'master': dissolve}:
        xoffset 132
    tony "That son of a bitch deserves worse than what he got, if you ask me!"
    tony a_idle "I still know some fellas on the inside, I could pay 'em a visit if you'd like?"
    tony "See how much it'll cost us to get our beloved mayor a little prison yard justice."
    show tony f_angry
    show maria b_magic f_annoyed a_idle:
        xoffset -100
    show anon f_worried:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    maria "{b}Tony{/b}!"
    show anon f_surprised
    show tony a_sides f_surprised:
        xoffset -268
        xzoom 1
    with {'master': dissolve}
    maria "Now ain't the time... Can't ya see {b}[firstname]{/b} is hurtin'?"
    anon f_worried @ -m_talk "..."
    show maria f_sad
    show tony:
        xoffset 132
        xzoom -1
    with {'master': dissolve}
    tony f_sad "I'm sorry, champ."
    tony "I don't mean ta-"
    anon "N-no, it's okay."
    anon "{b}Rump{/b} was just a pawn in all of this anyways..."
    anon "... {b}Raz Chernyshevsky{/b} and his goons are the ones responsible for my father's murder."
    show tony a_mc_hip_single f_normal
    show tony_arms_dressed_a_mc_shoulder_single as arms:
        xoffset 132
        xzoom -1
    with {'master': dissolve}
    tony "Well, then let's go get 'em!"
    anon @ -m_talk "Hmm?"
    tony "Did the cops drop any hints about when they might make their move on the warehouse?"
    anon f_unimpressed "No."
    anon "From what {b}Harold{/b} said, I'm not sure they'll go after them at all."
    hide arms
    show tony f_surprised a_idle
    with {'master': dissolve}
    tony "Huh?!"
    anon "They think the mob will pull out of Summerville and disappear now that {b}Rump{/b}'s in custody."
    tony f_angry "What a bunch of pussies!"
    show tony:
        xoffset -268
        xzoom 1
    show anon f_worried
    with {'master': dissolve}
    tony "See, {b}Maria{/b}... I told you they weren't gonna do nothing!"
    maria f_annoyed "Well, they're probably just bein' honest about the reality of the situation."
    maria "Who knows how many men they've got in that warehouse?"
    maria "This {b}Chernyshevsky{/b} guy could have an army sittin' in there!"
    tony @ f_eyeroll "Pfft, yeah... an army of Russian whores and ladyboys!"
    tony "He's got ten to twelve guys in there, tops."
    maria "You don't know that!"
    tony "Well, I'm going out there tonight to find out."
    maria f_angry "Oh, no you are not!"
    tony "I'll be fine, {b}Maria{/b}..."
    tony "... In and out... they won't even know I'm there."
    maria "Damnit, {b}Tony{/b}... I said no!"
    pause
    tony a_crossed "You know you ain't the boss of me, woman."
    maria "Maybe it's time for both of you accept that this man is out of your reach and move on."
    tony a_idle "Move on?!"
    maria "Gettin' yourself killed ain't gonna bring the kid's father back!"
    show anon f_sad_down
    show maria f_sad

    if M_tony.watches:
        maria "You got two people who love ya right here, {b}[firstname]{/b}..."
    else:
        maria "I love ya, {b}[firstname]{/b}..."

    maria "... And I know your friends at home love ya too."
    maria "Would your father really want you to risk all that for the sake of vengeance?"
    pause
    tony "Jesus, you're layin' the guilt trip on him pretty thick, ain't ya?!"
    show maria a_crossed f_angry with dissolve
    pause
    anon "N-no, he wouldn't."
    show maria a_idle f_sad
    show tony f_sad:
        xoffset 132
        xzoom -1
    with {'master': dissolve}
    tony @ f_eyeroll "Oh, for fucks sake."
    maria "I mean, you did put {b}Rump{/b} behind bars..."
    maria "... and crippled the mob to the point that they're likely fleein' the country."
    maria "Maybe that's enough, huh?"
    anon @ -m_talk "..."
    maria "Have you even been to visit your father since the funeral?"
    anon "No."
    pause
    maria "How come?"
    anon "I dunno... I just-"
    pause
    anon f_worried "I always looked up to him, you know?"
    anon "He was like my hero growing up and now I find out he was keeping all these secrets and working with horrible people."
    anon "I feel like maybe I didn't even know the real him..."
    show tony a_mc_hip_single
    show tony_arms_dressed_a_mc_shoulder_single as arms:
        xoffset 132
        xzoom -1
    with {'master': dissolve}
    tony "Ah, c'mon champ... You can't let this nastiness taint the good memories you made with your father."
    tony "We all got skeletons in our closet but that's not what defines us."
    tony "From everything you've told me, it sounds like he was a good dad."
    anon @ f_sad_down "{i}*Sniff*{/i} He was."
    tony f_normal "And if you're anything like him, then I know he musta had a damn good reason for gettin' in bed with those Russian animals."
    maria "You should go and pay him a visit, {b}[firstname]{/b}."
    maria "I think it will go a long way in making you feel better."
    anon "Y-yeah, maybe you're right."
    tony "And if you still feel like stormin' that warehouse and kickin' some ass, you know where to find me."
    show maria a_crossed f_angry with dissolve
    pause
    hide arms
    show tony a_frustrated:
        xoffset -268
        xzoom 1
    with {'master': dissolve}
    tony "What?!"
    show tony a_idle with {'master': dissolve}
    maria @ f_eyeroll "Ugh."
    hide maria
    show tony f_angry
    with {'master': dissolve}
    tony "{b}Maria{/b}?!"
    hide tony with {'master': dissolve}
    tony "Stop walkin' away when I'm talkin' to ya!"
    pause
    show anon f_sad_down with {'master': dissolve}:
        xoffset 600
        xzoom 1
    anon "( {i}*Sigh*{/i} I guess there's no reason to put it off any longer... )"
    anon "( ... It's time I go and {b}visit my father{/b}. )"
    anon "( {b}I'll find his headstone in the town graveyard{/b}. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
