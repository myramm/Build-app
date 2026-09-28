label scene_ivy_vera:
    call scene_ivy_vera.animation
    with fade
    ivy "Is this helping with your tension?"
    vero "Oh, definitely!"
    anon "( Whoa, check it out! )"
    pause
    ivy "Careful you don't knock me off the table this time!"
    vero "Okay, that happened once..."
    vero "... And it was because you used {i}way{/i} too much lube!"
    ivy "Well, I'm sorry but I like it extra lubey!"
    vero "Heh!"
    pause
    anon "( Are they using a double-sided dildo? )"
    anon "( That's so hot! )"
    pause
    vero "Ahh, fuck!"
    ivy "Enjoying?"
    vero "Yes!!"
    pause
    ivy "So have you..."
    ivy "... Made a-"
    $ M_ivy.set('sex speed', 1. / 14)
    ivy "Ngh!!"
    ivy "Decision yet?!"
    pause
    vero "No, I think..."
    vero "... We need to do..."
    $ M_ivy.set('sex speed', 1. / 18)
    ivy "Fuck!"
    vero "... A little more..."
    $ M_ivy.set('sex speed', 1. / 22)
    ivy "Oh, fuck!!"
    vero "... TESTING!!!"
    anon "( Wow, look at them go... )"
    pause
    anon "( As much as I'd like to stay here and watch... )"
    return


label scene_ivy_vera.animation:
    $ M_ivy.set('sex speed', 1. / 10)
    scene location_pink_massage_sex_spy
    show ivy_sex_vera
    return


label scene_ivy_vera.repeat:
    call scene_ivy_vera.animation
    $ M_ivy.set('sex speed', 1. / 18)
    with fade
    anon "( I'm sure {b}Diane{/b} won't mind me taking my time... )"
    anon "( ... Just a little longer couldn't hurt. )"
    ivy "Haah! Haah!!"
    pause
    ivy "Still..."
    ivy "... Not decided?"
    vero "You can't rush-"
    vero "Hng!"
    vero "... this sort of testing!"
    pause
    anon "( Sounds like they're going to be a while. )"
    return


label scene_ivy_vera.replay:
    jump scene_ivy_vera
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
