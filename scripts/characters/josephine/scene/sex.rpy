image josie_sex_slow_anon = AnimatedImage('josephine_office_sex_mc_slow', (7,8,9,10,1,2,3,4,5,6), M_josie)
image josie_sex_slow_josie = AnimatedImage('josephine_office_sex_josephine_slow', (7,8,9,10,1,2,3,4,5,6), M_josie)

image josie_sex_fast_anon = AnimatedImage('josephine_office_sex_mc_fast', (6,7,8,1,2,3,4,5), M_josie)
image josie_sex_fast_josie = AnimatedImage('josephine_office_sex_josephine_fast', (6,7,8,1,2,3,4,5), M_josie)


label scene_josie_sex:
    call scene_josie_sex.stage ('office')
    with fade
    anon "Wow, you're really wet!"
    josephine "Heh, what can I say... Nerdy little white boys turn me on..."
    anon "Really?"
    josephine "Ugh, just shut up and put it inside me already!"
    call scene_josie_sex.insert ('fast')
    with fastdissolve
    josephine f_shy @ f_moan "Oh, wow!!"
    anon "You alright?"
    josephine "Y-yeah, just-"
    josephine "Ngh, you're really big!"
    anon "Do you need me to go slow or something?"
    josephine f_normal "No, screw that!"
    josephine "I can take it."
    pause
    josephine "Fuck me hard, {b}[firstname]{/b}!"
    anon "Alright."
    call scene_josie_sex.animate ('fast')
    josephine "!!!"
    josephine "FUUUUUUCK!"
    pause
    anon "You good?"
    josephine "Yes!!"
    pause
    josephine "This is amazing!"
    pause
    josephine "Oh, {b}[firstname]{/b}!"
    pause
    josephine "Fuck me!!"
    josephine "FUCK ME HARDER!!"
    anon "Shh!"
    josephine "Don't shush me!"
    pause
    josephine "AHH!!"
    josephine "IT'S SO FUCKING DEEP!"
    anon "Someone is gonna hear you!"
    josephine "I DON'T CARE!"
    pause
    josephine "I'M CUMMING!!"
    josephine "I'M CUM-"
    sato "What in the hell is going on in-"
    return


label scene_josie_sex.stage(venue):
    if venue == 'lounge':
        scene location_dealership_lounge_sex
        show josephine_sex_table2 as table
        show josephine b_sex_pre_top
        show josephine_body_b_sex_overlay_leg_fix as leg
    else:
        scene location_dealership_office_sex
        show josephine_sex_table1 as table
        show josephine b_sex_pre_top_no_phone
    show mc_josephine_sex pre behind table
    return


label scene_josie_sex.insert(speed):
    hide animation1
    hide animation2
    show mc_josephine_sex insert behind table
    if speed == 'slow':
        show josephine b_sex_insert_top f_moan
    else:
        show josephine b_sex_insert_top_no_phone f_moan
    return


label scene_josie_sex.animate(speed):
    python:
        anim_toggle = True
        animated = True
        M_josie.set('sex speed', .12)
    hide josephine
    hide leg
    hide mc_josephine_sex
    show expression 'josie_sex_{}_anon'.format(speed) as animation1 behind table
    show expression 'josie_sex_{}_josie'.format(speed) as animation2
    with dissolve
    return


label scene_josie_sex.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show josie_sex_fast_anon as animation1 behind table
                show josie_sex_fast_josie as animation2
                with dissolve
                $ animated = True
            pause 5
            call scene_josie_sex.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [6,7,8,1,2,3,4,5]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "josephine_office_sex_mc_fast {}".format(pose_list[pose_counter]) as animation1 behind table
                show expression "josephine_office_sex_josephine_fast {}".format(pose_list[pose_counter]) as animation2
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_josie_sex.dialogue
        $ animcounter += 1
    call screen scene_josie_sex_controls()
    if not _return:
        jump scene_josie_sex.loop
    return _return


label scene_josie_sex.dialogue:
    if animcounter == 0 and randomizer() > 50:
        josephine "AHH!!{p=1}{nw}"
    if animcounter == 1 and randomizer() > 50:
        josephine "FUCK ME!!{p=1}{nw}"
        anon "Shh, your dad is gonna hear you!{p=2}{nw}"
        josephine "I DON'T CARE!{p=1}{nw}"
    if animcounter == 2 and randomizer() > 50:
        josephine "Oh, god!{p=1}{nw}"
    elif animcounter == 2 and randomizer() > 75:
        josephine "Don't!{p=1}{nw}"
        josephine "Stop!{p=1}{nw}"
    return


label scene_josie_sex.cum(venue, where):
    hide animation1
    hide animation2
    show josephine b_sex_cum_top
    show mc_josephine_sex cum behind table

    if where != 'inside':
        show josephine_sex_cum_cumshot

    anon "HNNGGG!!!" with flash
    if where == 'inside':
        show xray_josephine_top with fastdissolve:
            align (0, 0)
    josephine "NGGHHH!!!"
    if venue == 'lounge':
        show josephine_body_b_sex_overlay_leg_fix as leg
    hide xray_josephine_top
    if where != "inside":
        hide josephine_sex_cum_cumshot
        show josephine b_sex_pre_top_no_phone o_sex_after_cumshot_no_phone f_moan
        show mc_josephine_sex pre
    else:
        show mc_josephine_sex pullout
        show josephine b_sex_pullout_top_no_phone f_moan
    with dissolve
    pause
    anon "Haah... Haah..."
    if where == 'inside':
        show josephine b_sex_after_top_no_phone f_normal
        show mc_josephine_sex after
    else:
        show josephine f_normal
    with dissolve
    return where


label scene_josie_sex.morning:
    call scene_josie_sex.stage ('lounge')
    with fade
    anon "What are you doing today?"
    josephine "Just chatting with some people."
    anon "What about?"
    josephine "Oh, just boring stuff..."
    josephine "Video games, snacks, bad mo-"
    call scene_josie_sex.insert ('slow')
    with fastdissolve
    josephine f_normal @ f_moan "MOOOOOVVVIESS!"
    anon "Hehe."
    josephine "Asshole!"
    call scene_josie_sex.animate ('slow')
    pause
    josephine "Fuck, that's deep!!"
    anon "Mmhmm."
    pause
    josephine "These guys have the worst taste in movies, I swear..."
    anon "Oh, yeah?"
    josephine "They keep bringing up this one, about futuristic marines battling giant space bugs..."
    anon "You mean, Galaxyship Startroopers?"
    josephine "Yeah, that's the one."
    anon "I love that movie!"
    josephine "Ugh, you too?"
    anon "Yeah, it's awesome!"
    pause
    josephine "Maybe it's just a guy thing..."
    anon "What is?"
    josephine "Liking bad movies."
    anon "Oh."
    josephine "I mean, nothing against sci-fi but I-"
    call scene_josie_sex.animate ('fast')
    $ M_josie.set('sex speed', .09)
    josephine "Haah, shit!!!"
    pause
    anon "What were you saying?"
    josephine "Hmm?"
    josephine "Oh, I don't know... Just keep doing that!"
    anon "Heh, alright."
    call scene_josie_sex.loop
    josephine "FUCK, I'M GONNA CUM!"
    anon "Me too!"
    pause
    call scene_josie_sex.cum ('lounge', _return)
    if _return == "inside":
        josephine "Mmm, I'm gonna be feeling that tomorrow..."
    else:
        josephine "Mmm, that's a lot of cum..."
    anon "Better than chatting online, yeah?"
    josephine "Hehe, yes..."
    pause
    josephine "Help me up."

    if _return == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return


label scene_josie_sex.afternoon:
    call scene_josie_sex.stage ('lounge')
    with fade
    anon "Wow, you're really wet!"
    josephine "Well, I've been watching an adult art stream..."
    anon "So you're watching porn on your lunch break?"
    josephine "It's not porn, stupid..."
    josephine "It's ar-"
    call scene_josie_sex.insert ('slow')
    with fastdissolve
    josephine f_normal @ f_moan "AAAAARRRTTT!!"
    anon "Hehe."
    josephine "Very funny."
    call scene_josie_sex.animate ('slow')
    pause
    josephine "Fuck, that's deep!!"
    anon "Mmhmm."
    pause
    anon "So what's he streaming today?"
    josephine "Just boring background stuff."
    anon "What, no boobs?"
    josephine "I don't watch it for the boobs, you know?!"
    anon "Sure you don't..."
    pause
    anon "Can you put the phone down?"
    josephine "Hmm?"
    josephine "No, I told you I was gonna watch my stream..."
    call scene_josie_sex.animate ('fast')
    $ M_josie.set('sex speed', .09)
    josephine "Haah, shit!!!"
    anon "That's better."
    pause
    josephine "Heh, you're such an asshole!"
    anon "You don't like it?"
    josephine "Ngh, I didn't say that!"
    call scene_josie_sex.loop
    josephine "FUCK, I'M GONNA CUM!"
    anon "Me too!"
    pause
    call scene_josie_sex.cum ('lounge', _return)
    if _return == "inside":
        josephine "Mmm, I'm gonna be feeling that tomorrow..."
    else:
        josephine "Mmm, that's a lot of cum..."
    anon "Better than some art stream, yeah?"
    josephine "Hehe, yes..."
    pause
    josephine "Help me up."

    if _return == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return


label scene_josie_sex.switch:
    $ M_josie.set('sex speed', .12)

    josephine "Haah... Haah..."
    anon "Alright, I'll take over for a bit."
    call scene_josie_sex_desk.stage
    with dissolve
    josephine "Phew, thank you!"

    call scene_josie_sex.stage ('office')
    with fade

    if 'kink' not in rv:
        $ rv.add('kink')
        anon "Wow, you're really wet!"
        josephine "I told you this really turns me on..."
        anon "You're pretty kinky, huh?"
        josephine "What?!"
        josephine "I'm not kinky, I'm just-"
        call scene_josie_sex.insert ('fast')
        with fastdissolve
        josephine f_shy @ f_moan "Ahh, fuck!!"
        anon "You were saying?"
        josephine "Fine, I'm kinky."
        josephine "Just fuck me, please!"
    else:
        anon "Better?"
        josephine "Mmm, much better."
        call scene_josie_sex.insert ('fast')
        with fastdissolve
        josephine f_shy @ f_moan "Ahh!"
        anon "Feels good?"
        josephine "Yeah, yeah!"

    call scene_josie_sex.animate ('fast')
    $ M_josie.set('sex speed', .09)
    josephine "!!!"
    josephine "FUUUUUUCK!"
    pause
    anon "You like that?"
    josephine "Yes!!"
    pause
    josephine "This is amazing!"
    pause
    josephine "Oh, {b}[firstname]{/b}!"
    pause
    josephine "Fuck me!!"
    josephine "FUCK ME HARDER!!"
    anon "Shh!"
    josephine "Don't shush me!"
    pause
    josephine "AHH!!"
    josephine "IT'S SO FUCKING DEEP!"
    anon "Someone is gonna hear you!"
    josephine "I DON'T CARE!"

    call scene_josie_sex.loop
    if _return == 'switch':
        jump scene_josie_sex_desk.switch

    josephine "I'M CUMMING!!"
    anon "Me too!"
    pause
    call scene_josie_sex.cum ('office', _return)
    if _return == 'inside':
        josephine "Oh my god, that was awesome!"
        anon "Yeah, it was."
        josephine "Hehe, I came so hard..."
    else:
        josephine "Wow, you drenched me in cum!"
        anon "Yeah, sorry about that."
        josephine "Hehe, no, it's hot!"
    pause
    josephine "Help me up."

    if _return == 'inside':
        call call_pregnancy_minigame (None, M_josie)
    return


label scene_josie_sex.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['josie']['variants']['02_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_dealership) with fade
        menu:
            "Morning" if 'morning' in variants:
                jump scene_josie_sex.morning

            "Afternoon" if 'afternoon' in variants:
                jump scene_josie_sex.afternoon
    else:

        jump expression 'scene_josie_sex.{}'.format(next(iter(variants)))

    return


screen scene_josie_sex_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')

            if renpy.showing('location_dealership_office_sex'):
                textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_josie.set,
                                 'sex speed',
                                 M_josie.get('sex speed') + 0.03),
                        Return(False))
                sensitive M_josie.get('sex speed') < .12
            textbutton _('Faster »'):
                action (Function(M_josie.set,
                                 'sex speed',
                                 M_josie.get('sex speed') - 0.03),
                        Return(False))
                sensitive M_josie.get('sex speed') > .061
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
