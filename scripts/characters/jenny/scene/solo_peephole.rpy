label scene_jenny_solo_peephole:

    return


label scene_jenny_solo_peephole.stage:
    scene location_home_attic_peep_closeup
    return


label scene_jenny_solo_peephole.animate:
    show jenny_solo_peephole_anim as animation
    return


label scene_jenny_solo_peephole.daddy:
    jenny "Mmm."
    pause
    jenny "That's it, Daddy!"
    jenny "Gimme the big one!"
    pause
    jenny "Haah, twenty-four karat..."
    jenny "... Amethyst encrusted..."
    $ M_jenny.set('sex speed', 1 / 10.)
    jenny "... Ahh, fuck!"
    anon "( Hmm? )"
    pause
    jenny "What's that?"
    jenny "You wanna take me out on your new yacht?!"
    pause
    jenny "Mmm, champagne in the hot tub?!"
    $ M_jenny.set('sex speed', 1 / 12.)
    jenny "Oh, yes..."
    jenny "... Fill me up!"
    anon "( This is what she thinks about when she's masturbating?! )"
    pause
    jenny "Ahh, but I can't decide between the red convertable and the black-"
    jenny "Oh, really?"
    jenny "You're gonna buy them both for me?!"
    $ M_jenny.set('sex speed', 1 / 16.)
    jenny "Ngh, you're the best!"
    pause
    return


label scene_jenny_solo_peephole.anon:
    jenny "Mmm."
    pause
    jenny "That's it!"
    jenny "Call me princess!!"
    pause
    jenny "Don't talk back to me..."
    jenny "... You know you want it!"
    $ M_jenny.set('sex speed', 1 / 10.)
    jenny "Ahh, fuck!"
    anon "( Hmm? )"
    pause
    jenny "Shut up and eat my pussy!"
    pause
    jenny "Mmm, just like that."
    jenny "Oh, I bet you wanna fuck me, don't you?"
    jenny "Say it, {b}[firstname]{/b}!"
    anon "( !!! )"
    $ M_jenny.set('sex speed', 1 / 12.)
    jenny "Ngh, that's right!"
    anon "( She's imagining me! )"
    jenny "Get on your knees!"
    pause
    jenny "Now lick my feet and beg me!"
    $ M_jenny.set('sex speed', 1 / 14.)
    jenny "Mhmm..."
    $ M_jenny.set('sex speed', 1 / 16.)
    jenny "... All my toes."
    pause
    jenny "Ahh, fuck!"
    pause
    return


label scene_jenny_solo_peephole.repeat(subject='daddy'):
    python hide:
        M_jenny.set('sex speed', 1 / 8.)

    call scene_jenny_solo_peephole.stage
    call scene_jenny_solo_peephole.animate
    with fade

    if subject == 'daddy':
        jump scene_jenny_solo_peephole.daddy

    jump scene_jenny_solo_peephole.anon


label scene_jenny_solo_peephole.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Jenny']['variants']['20_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_home_attic) with fade
        menu:
            "Daddy" if 'daddy' in variants:
                call scene_jenny_solo_peephole.repeat ('daddy')

            "[firstname]" if 'anon' in variants:
                call scene_jenny_solo_peephole.repeat ('anon')
    else:

        call scene_jenny_solo_peephole.repeat (next(iter(variants)))

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
