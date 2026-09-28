label eve20_tony_lasagna:
    show anon with dissolve:
        flip
    anon "I'll take one large lasagna, please."
    tony "Now we're talkin'!"
    tony "You want breadsticks with that?"

    menu:
        "Of course!":
            jump eve20_tony_lasagna.breadsticks
        "On second thought...":
            pass

    anon @ f_thinking a_thinking "Uhh, actually... Never mind."
    anon "I don't need it right now, I'll come back later."
    tony @ f_suspicious "No?"
    tony @ f_smirk_closed a_frustrated "Alright, champ."
    pause
    tony @ a_point "Come back if you change your mind."
    hide anon with dissolve
    return

label eve20_tony_lasagna.breadsticks:
    anon @ f_snarky "You gotta have breadsticks!"
    tony @ f_laugh a_belly "Haha, attaboy!"
    tony "How's about I throw in some Parmesan cheese and peppers too?"
    anon "Oh, yes please!"
    tony "That'll be $20."

    if player.has_money(20):
        jump eve20_tony_lasagna.lasagna

    anon f_worried @ f_surprised "Oh, crap."
    anon "I don't have enough money on me."
    tony f_suspicious "Well, you can't get no lasagna without money."
    tony @ a_fists "What are you thinkin' knucklehead?"
    anon f_sad_down "Heh, sorry."
    tony f_normal @ f_smirk a_point "Just come back when you got some cash on ya, alright?"
    anon "Will do."
    hide anon with dissolve
    return

label eve20_tony_lasagna.lasagna:
    anon "Here ya go."
    show anon a_money with dissolve
    pause
    show tony f_suspicious a_whisper:
        unflip
        xoffset -400
    show anon a_idle
    with dissolve
    tony "'Ey, {b}Maria{/b}!"
    tony "We got somebody orderin' lasagna out here!"
    show tony a_idle with dissolve
    show anon f_worried
    maria "Yeah?"
    maria "Well, that ain't no excuse to be shoutin' at me!"
    tony "Tch, I ain't shoutin'..."
    tony "I'm just tryin' ta place the order!"
    maria "So turn around and do it nice like, otherwise, you can cook your own damn lasagna!"
    hide tony with dissolve
    show anon f_sad_down
    tony "Jesus, {b}Maria{/b}... You ain't gotta be like that!"
    tony "You know my lasagna can't hold a candle to yours!"
    show anon f_worried
    maria "Hah, of course I know that."
    maria "I'm just makin' sure you do too."
    tony "Oh, now that's just mean!"
    tony "Haha!"
    maria "Haha!"
    show anon f_normal
    maria "Yeah, yeah... Come gimme a kiss you big oaf."
    tony "Ah well, who could refuse that?"
    pause
    tony "Hehehe."
    show tony behind counter with dissolve:
        flip
    tony "{i}*Ahem*{/i} She'll have it right out."
    anon "No problem."
    pause
    show maria a_lasagna behind counter with dissolve:
        flip
        xoffset -150
    maria "Here's your food."
    show anon a_lasagna
    show maria a_back
    with dissolve
    anon "Thanks!"
    maria f_angry "You coulda carried that out here for me, ya know?"
    show tony f_suspicious with dissolve:
        unflip
        xoffset -200
    anon f_brag_closed @ -m_talk "( Oh, this smells really good. )"
    anon @ -m_talk "( I hope the girls like it. )"
    show anon f_worried
    tony "You didn't say nothin' about needin' help!"
    maria "Well, I shouldn't have to, should I?"
    maria "A good husband would offer to help his wife without being asked!"
    tony "Do I look like a mind reader to you?!"
    tony @ f_eyeroll "What are you busting my balls for, eh?"
    anon @ -m_talk "( Hmm, looks like they're going to be arguing for a while. )"
    maria "Maybe if you did something right every once in a while..."
    tony "Ah, don't even go there!"
    anon @ -m_talk "( I should {b}get back to Eve's place{/b}. )"
    hide anon with dissolve
    return 'lasagna'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
