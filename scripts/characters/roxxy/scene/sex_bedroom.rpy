label scene_roxxy_sex_bedroom:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_roxxy.set('sex speed', 1 / 8.)

    scene location_trailer_bedroom_sex
    show roxxys_bed 9b at left
    with fade
    roxxy "Mmm, I can't believe I'm about to have sex with you..."

    roxxy "Not long ago, I would have laughed at the idea-"

    show roxxys_bed 10
    roxxy "!!!" with hpunch
    show roxxys_bed front 1 with {'master': dissolve}
    roxxy "HOLY SHIT!!!"

    roxxy "Nngghhh!!!"

    show roxxys_bed front 2 with {'master': dissolve}
    roxxy "It's so fucking big!!"

    roxxy "aku tidak bisa-"

    call scene_roxxy_sex_bedroom.animate
    with dissolve
    jump scene_roxxy_sex_bedroom.resume

label scene_roxxy_sex_bedroom.animate:
    show roxxys_bed front at left
    return

label scene_roxxy_sex_bedroom.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show roxxys_bed front with dissolve
                $ animated = True
            pause 5
            call scene_roxxy_sex_bedroom.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_bed front {}".format(pose_list[pose_counter]) as roxxys_bed
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_roxxy_sex_bedroom.dialogue
        $ animcounter += 1
    if M_roxxy.get("roxxy trailer sex first"):
        $ M_roxxy.set("roxxy trailer sex first", False)
    call screen scene_roxxy_sex_bedroom_controls
    if not _return:
        jump scene_roxxy_sex_bedroom.loop
    return _return

label scene_roxxy_sex_bedroom.dialogue:
    $ renpy.dynamic(random_count=renpy.random.random())

    if animcounter == 0:
        if M_roxxy.get("roxxy trailer sex first"):
            roxxy "!!!{w=1}{nw}" with hpunch
            roxxy "AAAHHHHHH!!!{w=1}{nw}"


        elif random_count <= .33:
            roxxy "Ahh!{w=1}{nw}"

            pause
            anon "Anda menyukainya?{w=1}{nw}"

            roxxy "Yess!!{w=1}{nw}"


        elif random_count <= .66:
            roxxy "Holy shit!{w=1}{nw}"

            anon "Too rough?!{w=1}{nw}"

            roxxy "NO!!!{w=1}{nw}"

            roxxy "Fuck me harder!{w=1}{nw}"

            anon "O-okay...{w=1}{nw}"


    elif animcounter == 1:
        if M_roxxy.get("roxxy trailer sex first"):
            roxxy "Oh shit!{w=1}{nw}"

            roxxy "Ooooh shit!!{w=1}{nw}"

            roxxy "AAAAHHHHH!!!{w=1}{nw}"


        elif random_count <= .33:
            roxxy "Ahhh! Fuck this is so good!!!{w=1}{nw}"


    elif animcounter == 2:
        if M_roxxy.get("roxxy trailer sex first"):
            roxxy "Mmmm, fuck!{w=1}{nw}"

            roxxy "Nngghhh!!!{w=1}{nw}"


        elif random_count <= .25:
            roxxy "Fuuuck meeee!!!{w=1}{nw}"


        elif random_count <= .50:
            roxxy "AAAAAHHHH!!!"


        elif random_count <= .75:
            roxxy "AAAHHHH!!! FUCK YES!!!{w=1}{nw}"

            roxxy "God, your dick is so good, {b}[firstname]{/b}!!!{w=2}{nw}"

        else:

            roxxy "{b}[firstname]{/b}!!!{w=1}{nw}"


    elif animcounter == 3:
        if M_roxxy.get("roxxy trailer sex first"):
            anon "You like me pulling your hair?!{w=2}{nw}"

            pause 1
            roxxy "YESSSS!{w=1}{nw}"

            roxxy "Ahh, call me a bitch!{w=2}{nw}"

            anon "Hmm?{w=1}{nw}"

            roxxy "Tell me I'm your bitch!{w=2}{nw}"

            anon "... You're my bitch?{w=2}{nw}"

            roxxy "Fuck yesss!!!{w=1}{nw}"


        elif random_count <= .33:
            roxxy "Ngghhh!! It's so fucking good!!!{w=1}{nw}"


        elif random_count <= .66:
            roxxy "Ngghhh!!! Fuuuuck!!!{w=1}{nw}"


    return


label scene_roxxy_sex_bedroom.switch:
    scene location_trailer_bedroom_sex
    call scene_roxxy_sex_bedroom.animate
    with fade
    roxxy "Mmm, I fucking love it when you pull my hair!"

    anon "Oh ya?"

    roxxy "Yessss!"

    anon "... Maybe I should pull it harder then!"

    pause
    roxxy "AAAHHHH!!! FUCK YES!!!"

    roxxy "God, your dick is so good, {b}[firstname]{/b}!!!"

    pause
    roxxy "Ngghhh!!! Fuuuuck!!!"

    label scene_roxxy_sex_bedroom.resume:
    call scene_roxxy_sex_bedroom.loop

    if _return == 'switch':
        jump scene_roxxy_sex_bedroom_above.switch

    call scene_roxxy_sex_bedroom.cum
    return


label scene_roxxy_sex_bedroom.cum:
    roxxy "Oooh, I'm gonna cum!"

    anon "Aku juga semakin dekat!"

    roxxy "aku akan-"

    anon "Cum for me, bitch!"

    roxxy "AAAAHHHH!!!"

    show roxxys_bed 10_10b
    anon "HNNGGG!!!{nw}{w=1.2}" with flash
    show roxxys_bed 10
    show xray_roxxy_trailer_bed at reset
    with dissolve
    pause
    hide xray_roxxy_trailer_bed
    show roxxys_bed 11 with dissolve
    pause
    return


label scene_roxxy_sex_bedroom.repeat:
    python:
        renpy.dynamic(anim_toggle=True, animated=True)
        M_roxxy.set('sex speed', 1 / 12.)

    scene location_trailer_bedroom_sex
    show roxxys_bed 9b at left
    with fade
    roxxy "Mmm, that's it {b}[firstname]{/b}... Give it to me!"

    show roxxys_bed 10
    roxxy "!!!" with hpunch
    show roxxys_bed front 1 with {'master': dissolve}
    roxxy "Sial!"

    show roxxys_bed front 2 with {'master': dissolve}
    roxxy "I swear, it gets bigger every time!"

    call scene_roxxy_sex_bedroom.animate
    with dissolve
    jump scene_roxxy_sex_bedroom.resume


label scene_roxxy_sex_bedroom_above:
    return


label scene_roxxy_sex_bedroom_above.animate:
    show roxxys_bed above
    return

label scene_roxxy_sex_bedroom_above.switch:
    scene location_trailer_bedroom_sex_back
    call scene_roxxy_sex_bedroom_above.animate
    with fade
    roxxy "Ahhh!"

    pause
    anon "Anda suka itu?"

    roxxy "Yess!!"

    pause
    anon "Who's bitch are you?"

    roxxy "I'm your bitch, {b}[firstname]{/b}!"

    anon "Lebih keras!"

    roxxy "I'm your bitch!! I'm your bitch!!! Oh god, {b}[firstname]{/b}!"

    roxxy "I'M YOUR DIRTY LITTLE BITCH!!!"

    pause
    roxxy "Fuuuck meeee!!!"

    pause
    roxxy "Ngghhh!! It's so fucking good!!!"

    pause
    roxxy "Pull my hair!!"

    anon "Hmm?"

    roxxy "PULL MY HAIR!!"

    call screen scene_roxxy_sex_bedroom_controls(angle='above')

    if _return == 'switch':
        jump scene_roxxy_sex_bedroom.switch

    anon "Don't tell me what to do."

    anon "I'll pull your hair when I feel like pulling your hair."

    roxxy "Ngh, fuck that's hot!"

    pause
    roxxy "Ya Tuhan!!"

    roxxy "I love your dick, {b}[firstname]{/b}!!"

    call scene_roxxy_sex_bedroom_above.loop

    if _return == 'switch':
        jump scene_roxxy_sex_bedroom.switch
    return


label scene_roxxy_sex_bedroom_above.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show roxxys_bed above with dissolve
                $ animated = True
            pause 5
            call scene_roxxy_sex_bedroom.dialogue
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [1,2,3,4,5,6,7,8]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "roxxys_bed above {}".format(pose_list[pose_counter]) as roxxys_bed
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_roxxy_sex_bedroom.dialogue
        $ animcounter += 1
    label scene_roxxy_sex_bedroom_above.control:
    call screen scene_roxxy_sex_bedroom_controls(angle='above')
    if not _return:
        jump scene_roxxy_sex_bedroom_above.loop
    return _return


screen scene_roxxy_sex_bedroom_controls(angle='front'):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            if angle == 'above':
                textbutton _('Pull Hair') action Return('switch')
            else:
                textbutton _('Cum Inside') action Return('inside')
                textbutton _('Let Go') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_roxxy.set, 'sex speed',
                                 1 / (1 / M_roxxy.get('sex speed') - 2)),
                        Return(False))
                sensitive M_roxxy.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_roxxy.set, 'sex speed',
                                 1 / (1 / M_roxxy.get('sex speed') + 2)),
                        Return(False))
                sensitive M_roxxy.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
