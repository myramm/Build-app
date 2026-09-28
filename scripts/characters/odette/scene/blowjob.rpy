label scene_odette_blowjob(variant='_naked'):
    scene location_tattoo_rooftop_sex_bj
    call scene_odette_blowjob.animation
    with fade
    anon "Ack!"
    odette "{i}*Giggles*{/i}"
    pause
    anon "Okay, wow!"
    anon "Is this really happening?"
    odette "Mhmm!"
    anon "I mean, we barely know each other and you're..."
    odette "{i}*Sluuuuuurp*{/i}"
    anon "... Oh geez!"
    pause
    anon "Careful with the balls, you're squeezing a little-"
    $ M_odette.set('sex speed', 1. / 12)
    anon "!!!" with hpunch
    anon "Owww!!!"
    odette "{i}*Giggles*{/i}"
    anon "Oh kay... that was a bit unexpected, just-"
    $ M_odette.set('sex speed', 1. / 16)
    anon "!!!" with hpunch
    anon "Ah, god!!"
    pause
    anon "I'm getting close!"
    anon "Really, REALLY close, I-"
    anon "I-"
    grace "{b}Odette{/b}!"
    show odette_sex_bj_naked_surprised as animation
    odette "( !!! )" with hpunch
    grace "{b}Odette{/b}, where are you?!"
    show odette_sex_bj_naked_look as animation with {'master': dissolve}
    odette "{i}*Ahem*{/i} I'm up on the roof with {b}[firstname]{/b}, umm... talking..."
    odette "... J-just talking!"
    grace "{b}Odette{/b}, quit screwing around and get down here!"
    grace "I need your help!"
    odette "Yeah, sure... okay!"
    odette "I'll be right there!"
    return


label scene_odette_blowjob.animation:
    python:
        anim_toggle = True
        animated = True
        M_odette.set('sex speed', 1. / 8)
    show expression 'odette_blowjob{}'.format(variant) as animation
    return


label scene_odette_blowjob.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show expression 'odette_blowjob{}'.format(variant) as animation with dissolve
                $ animated = True
            pause 5
            call scene_odette_blowjob.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8,9,10,11]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "odette_blowjob{} {}".format(variant, pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_odette_blowjob.dialogue
        $ animcounter += 1
    call screen scene_odette_blowjob_controls
    if not _return:
        jump scene_odette_blowjob.loop
    return _return


label scene_odette_blowjob.dialogue:
    $ renpy.dynamic(rng=randomizer())
    if animcounter == 0 and rng > 85:
        odette "Mmm."
        odette "{i}*Sluuuuurp*{/i}"
    if animcounter == 1 and rng > 85:
        anon "Oh, geez..."
        anon "... You're really good at this!"
        odette "Mhmm!"
    if animcounter == 2 and rng > 92:
        odette "{i}*Humming noises*{/i}"
        anon "Oh, {b}Odette{/b}... Wow!"
    elif animcounter == 2 and rng > 85:
        odette "{i}*Gluullggh*{/i}"
        anon "Don't stop!"
        odette "Hehe!"
    return


label scene_odette_blowjob.repeat(variant=''):
    scene location_tattoo_indoor_sex_bj
    call scene_odette_blowjob.animation
    with fade
    anon "{b}Odette{/b}!!!"
    anon "What if somebody comes in?!"
    odette "Ohm orey abubit!"
    anon "Huh?"
    pause
    anon "This is such a bad idea..."
    odette "Hehehe!"
    pause
    odette "Mmm."
    odette "{i}*Sluuuuurp*{/i}"
    pause
    anon "Oh, geez..."
    anon "... You're really good at this!"
    odette "Mhmm!"
    pause
    odette "{i}*Humming noises*{/i}"
    anon "Oh, {b}Odette{/b}... Wow!"
    pause
    odette "{i}*Gluullggh*{/i}"
    anon "Don't stop!"
    odette "Hehe!"
    call scene_odette_blowjob.loop
    anon "I'm getting close!"
    odette "Gilb id eww mmeeh, iig alla!"
    anon "{b}Odette{/b}, I-"
    odette "{i}*Humming noises*{/i}"
    show odette_sex_bj_cum as animation
    anon "HNNGGG!!!" with flash
    odette "{i}*Gulp* *Gulp*{/i}"
    anon "Holy crap!"
    odette "{i}*Gulp*{/i}"
    show odette_sex_bj_show as animation
    with {'master': dissolve}
    odette "{i}*Smack*{/i} Maahh!"
    anon "You're incredible!"
    odette "Hehe!"
    return


label scene_odette_blowjob.roof:
    jump scene_odette_blowjob


label scene_odette_blowjob.shop:
    jump scene_odette_blowjob.repeat


label scene_odette_blowjob.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Odette']['variants']['04_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_tattooparlor_roof, t=3) with fade
        menu:
            "Roof (Topless)" if 'roof' in variants:
                jump scene_odette_blowjob.roof

            "Sugar Tats" if 'shop' in variants:
                jump scene_odette_blowjob.shop
    else:

        jump expression 'scene_odette_blowjob.{}'.format(next(iter(variants)))

    return


screen scene_odette_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_odette.set, 'sex speed',
                                 1 / (1 / M_odette.get('sex speed') - 2)),
                        Return(False))
                sensitive M_odette.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_odette.set, 'sex speed',
                                 1 / (1 / M_odette.get('sex speed') + 2)),
                        Return(False))
                sensitive M_odette.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
