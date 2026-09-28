label gamsay_button_kitchen:
    show anon f_worried with dissolve:
        xoffset -100
    show gamsay b_dressed f_angry a_pan with dissolve:
        unflip
        xoffset -100
    gamsay "Why are you in my kitchen again?!"
    anon "Sorry, Chef."
    anon "I'm just passing through, I swear!"
    gamsay "You're a first-class cunt, aren't you?"
    anon @ f_skeptical "You don't have to be rude, I'm just-"
    gamsay "Fuck right off, you donkey!"
    gamsay "I'm trying to work in here!"
    anon @ -m_talk "..."
    hide anon
    show gamsay b_dressed_back:
        flip
        xoffset 450
    with dissolve

    scene expression player.location.background_blur with fade
    show anon f_worried with dissolve
    anon @ -m_talk "( Man, that guy is a psychopath! )"
    hide anon with dissolve
    return


label gam01_gamsay_meet:
    show anon behind gamsay with dissolve:
        xoffset -100
    anon "Excuse me, sir?"
    gamsay @ -m_talk "..."
    anon "Do you work here?"
    gamsay "No, I just like to wear this getup and bake in the mayor's hot kitchen for funsies..."
    anon f_worried "Huh?"
    gamsay "Leave me alone kid, I'm busy!"
    pause
    anon "I was just hoping you could tell me where-"
    show gamsay b_dressed a_pan with {'master': fastdissolve}:
        unflip
        xoffset 0
    gamsay "Are you deaf?"
    anon "N-no."
    gamsay "Can't you see I'm trying to focus here?"
    anon "I'm sorry, I-"
    show gamsay f_angry_down a_pan_show
    show anon f_surprised_down
    with {'master': fastdissolve}
    gamsay "Look at this chicken."
    anon f_worried "What?"
    show anon f_surprised_down
    gamsay f_angry "LOOK AT IT!"
    gamsay "It's fucking RAW!!!"
    anon f_worried @ -m_talk "..."
    gamsay "And do you know why it's raw?"
    anon "No?"
    gamsay "Because you're distracting me!"
    anon "How am I distrac-"
    gamsay a_idle @ a_pan_throw "This is rubbish now!"
    anon f_surprised "!!!"
    gamsay "You've completely wasted it!"
    anon f_worried "I'm just gonna go."
    gamsay "Oh, no... Won't you stay, please?!"
    hide anon with dissolve
    gamsay "It would be a real shame if you weren't here to fuck up my next dish too!"
    show gamsay b_dressed_back with dissolve:
        flip
        xoffset 450
    pause
    gamsay "Fucking idiot sandwich, that guy..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
