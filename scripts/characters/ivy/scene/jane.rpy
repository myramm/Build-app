label scene_ivy_jane:
    call scene_ivy_jane.animation
    with fade
    ivy "Mmm, I've never had a customer offer to give {i}me{/i} the massage before..."
    jane "Does it feel good?"
    ivy "Yes, it certainly does."
    anon "( Oh wow, they're naked! )"
    pause
    anon "( And {b}Jane{/b} is fingering {b}Ivy{/b}!! )"
    ivy "You're quite skilled with your hands."
    jane "Heh, I've had a lot of practice at this."
    pause
    jane "How do you keep your pussy so tight in your line of work anyway?"
    jane "I can barely get two fingers inside you."
    ivy "Haah, it takes..."
    ivy "... A lot of work."
    jane "Yeah, I'll bet."
    pause
    ivy "Oh, that's the spot!"
    jane "Yeah, you like that?"
    ivy "Ngh, right there!!"
    pause
    anon "( Dang, {b}Ivy{/b} is close to cumming already? )"
    anon "( {b}Jane{/b} must really know what she's doing down there! )"
    pause
    jane "So how many free sessions do I get for that electro-clit?"
    ivy "I don't know, I-"
    $ M_ivy.set('sex speed', 1. / 24)
    jane "Hmm?"
    ivy "Oh, god!!"
    ivy "I-"
    pause
    ivy "Fuck, as many as you want!!"
    jane "Hehe, good answer."
    pause
    anon "( I'd best get out of here before they finish... )"
    anon "( .. don't wanna get caught. )"
    return


label scene_ivy_jane.animation:
    $ M_ivy.set('sex speed', 1. / 12)
    scene location_pink_massage_sex_spy
    show ivy_sex_jane
    return


label scene_ivy_jane.repeat:
    call scene_ivy_jane.animation
    $ M_ivy.set('sex speed', 1. / 18)
    with fade
    ivy "Too many! I can't-"
    jane "Of course you can."
    pause
    jane "Now cum for me."
    jane "Again!"
    ivy "NGGHHH!!!"
    return


label scene_ivy_jane.replay:
    jump scene_ivy_jane
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
