label scene_maria_sex_tony:
    show maria b_sex_side_after_back f_closed
    show anon b_maria_sex_side_back f_confused_back_low
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    show maria b_sex_side_after_up f_confused
    show anon maria_sex_side f_confused
    with {'master': dissolve}
    maria "You still okay with him joinin' us?"

    anon f_shy "Y-ya, menurutku begitu."

    show maria b_sex_side_after_back
    show anon b_maria_sex_side_back f_worried_low
    with {'master': dissolve}
    anon "But I'm still a little confused on the mechanics here..."

    show anon f_worried_back_low
    show maria f_skeptical_down
    pause
    tony "Oh, it's real simple..."

    tony "... You just roll over on your back and relax, while {b}Maria{/b} gets on top."

    tony "Then you can work the pussy while I work the ass, capiche?"

    show anon f_confused_low
    maria f_unimpressed_down "Jesus, {b}Tony{/b} don't say it like that!"

    show anon f_confused_back_low
    tony "Apa?!"

    show anon f_confused_low
    maria "You shouldn't be talkin' crass like that while we're tryin' to make a baby, ya big galoot!"

    show anon f_confused_back_low
    tony "Well, I'm sorry darlin' but what do you want me to call 'em?"

    show anon f_confused_low
    maria "Saya tidak tahu..."

    maria "... But somethin' else, please."

    show anon f_confused_back_low
    tony "Baiklah."

    pause
    show anon f_worried_back_low
    tony "You work the vanilla while I work the chocolate, capiche?"

    show anon f_surprised_low
    maria f_surprised_down "{b}TONY{/b}!!!"

    maria "That's not any better!"

    show anon f_surprised_left_low
    show maria f_unimpressed_down
    tony "Well, I'm running outta ideas here, darlin'!"

    pause
    show anon f_worried_back_low
    tony "Just get on top of the kid already, would ya?!"

    show anon f_worried_low
    maria @ -m_talk "Grr..."

    hide anon
    show maria b_sex_3some_insert_anon
    with {'master': dissolve}
    tony "Itu dia..."

    tony ".. Now go ahead and put him in."

    maria "saya!"

    tony "Baiklah, baiklah..."

    show maria b_sex_3some_base
    with {'master': dissolve}
    tony "... Don't get all worked up."

    pause
    show maria_body_b_sex_3some_tony as tony_torso
    show maria_body_b_sex_3some_tony_oil01 as tony_arm
    with {'master': dissolve}
    tony "Now then, I'm gonna use this olive oil to lube ya up, okay?"

    show maria b_sex_3some_talk f_surprised_back
    with {'master': dissolve}
    maria "I dunno about this {b}Tony{/b}..."

    maria f_worried_back "... Ya know, I ain't never had nothin' up there..."

    maria "... A-and you ain't exactly little."

    tony "Relax, darlin'."

    show maria f_surprised_back
    tony "That's why I got the {i}extra virgin{/i} olive oil."

    show maria_body_b_sex_3some_tony_oil02 as tony_arm
    with {'master': dissolve}
    pause
    show maria f_lipbite_back
    tony "A few squirts of this and it's gonna slide right in, I promise."

    maria @ -m_talk "{i}* Merengek*{/i}"

    hide tony_torso
    hide tony_arm
    show maria b_sex_3some_insert_tony
    with {'master': dissolve}
    tony "Now here we go, brace ya self."

    call scene_maria_sex_tony.insert
    with dissolve
    tony "Ngh!"

    maria "Ahh!!"

    tony "Phew, now that is a snug!"

    maria "Oh, entahlah..."

    maria "... This feels weird, {b}Tony{/b}!"

    tony "Just give it a second, {b}Maria{/b}."

    pause
    call scene_maria_sex_tony.animate
    maria "Oh, gawd!"

    maria "Oh, my gawd!!"

    pause
    maria "This is..."

    maria "... So-"

    maria "OH, GAWD!!!"

    tony "Heh, that's it, darlin'!"

    pause
    tony "How ya doin' down there, champ?"

    anon "She's squeezing me really hard!"

    tony "Heh, I bet she is."

    maria "AHH, JESUS!!!"

    maria "I'M GONNA CUM!!"

    tony "Sudah?"

    pause
    anon "Okay, that's like... {i}REALLY{/i} hard now..."

    maria "OH, {b}TONY{/b}!!"

    anon "OW, OW, OW!!"

    tony "Hey, hey... you gotta breathe, darlin'!"

    maria "I'm trying... I'm trying..."

    tony "You don't wanna snap the kid's dick off."

    maria "NGGHHH!!!"

    anon "!!!"
    tony "You alright, champ?"

    anon "Y-ya, menurutku begitu."

    maria "Haah... Haah..."

    maria "This feels incredible!"

    tony "Heh, see... I told ya you'd like it."

    pause
    jump scene_maria_sex_tony.resume


label scene_maria_sex_tony.insert:
    hide maria
    show expression 'maria_body_b_sex_anim_3some_{} 1'.format(
        'poly' if tony == 'plus' else 'mono') as animation
    return


label scene_maria_sex_tony.animate:
    python:
        anim_toggle = True
        animated = True
        M_maria.set('sex speed', 1 / 8.)
    show expression 'maria_3some {}'.format(
        'poly' if tony == 'plus' else 'mono') as animation
    return


label scene_maria_sex_tony.loop:
    show screen sex_anim_buttons
    pause
    hide screen sex_anim_buttons
    $ animcounter = 0
    $ renpy.dynamic(diags=random.sample(range(15), 3),
                    variant='poly' if tony == 'plus' else 'mono')
    while animcounter < 3:
        if anim_toggle:
            if not animated:
                show expression 'maria_3some {}'.format(variant) as animation with dissolve
                $ animated = True
            pause 5
            call scene_maria_sex_storage.dialogue (diags.pop(), variant)
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = range(1, 8 if tony == 'plus' else 8)
            $ poses_done = []
            while poses_done != pose_list:
                show expression 'maria_body_b_sex_anim_3some_{} {}'.format(
                    variant, pose_list[pose_counter]) as animation
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            call scene_maria_sex_storage.dialogue (diags.pop(), variant)
        $ animcounter += 1
    call screen scene_maria_sex_tony_controls(tony)
    if not _return:
        jump scene_maria_sex_tony.loop
    return _return


label scene_maria_sex_tony.switch:
    if tony == 'plus':
        tony "Who's ready for {b}Tony{/b} to join the party?"


    hide animation

    if tony == 'plus':
        if not M_maria.once('done_tony'):
            jump scene_maria_sex_tony

        jump scene_maria_sex_tony.join

    show maria b_sex_side_after_up f_closed
    show anon maria_sex_side f_confused
    with {'master': dissolve}
    anon "Phew, you think you could get on top for a little bit?"


    if tony:
        show maria b_sex_side_after_back f_skeptical_down
        show anon b_maria_sex_side_back f_worried_back_low
        with {'master': dissolve}
        tony "Heh, you wearin' out on us already, champ?"

        anon "T-tidak, aku hanya-"

        show anon f_worried_low
        maria f_unimpressed_down "{b}Tony{/b}, don't give the kid a hard time!"

        maria f_normal "It's no problem, {b}[firstname]{/b}..."

        show anon f_shy_low
        maria f_happy "... I like being on top."

        tony "Just remember to turn over on your back when he cums."

        show maria f_unimpressed_down
    else:

        maria f_confused "You gettin' tired?"

        anon f_shy "Y-ya, sedikit..."

        anon "... Maaf."

        maria f_normal "It's no problem, kid."

        maria "You just lay back and I'll ride ya for a while."

        anon f_normal "Benar-benar?"


    maria @ -m_talk "Mhmm!"

    hide anon
    show maria b_sex_3some_insert_anon
    with {'master': dissolve}
    maria "Try and give me a little warnin' before ya blow, alright?"

    show maria b_sex_3some_base
    with {'master': dissolve}
    anon "Baiklah, cukup."

    call scene_maria_sex_tony.insert
    with dissolve
    maria "Ahhh!"

    call scene_maria_sex_tony.animate
    label scene_maria_sex_tony.resume:
    call scene_maria_sex_tony.loop

    if _return == 'switch':
        jump scene_maria_sex_storage.switch

    if tony == 'plus':
        jump scene_maria_sex_tony.cum

    anon "Boy, boy, boy... Very tall boy!"

    maria "Hah?"

    maria "Apakah kamu baru saja-"

    maria "Ahhh!!!"

    maria "OH MY GAWD!"

    maria "GIVE ME A BABY, {b}[firstname!u]{/b}!!!"

    pause
    hide animation
    show maria b_sex_3some_cum
    anon "HNNGGG!!!" with flash
    show xray_maria_sex_3some as xray
    with {'master': fastdissolve}
    maria "NGGHHH!!!"

    hide xray
    pause
    show maria b_sex_3some_base
    show maria_body_b_sex_3some_pullout02_anon as anon_cum
    with {'master': dissolve}

    if tony:
        tony "C'mon, Champ, roll her over to make sure that batter gets good and deep."

    else:
        maria "Help me, {b}[firstname]{/b}, my legs aren't working so good just now."


    hide anon_cum
    show maria b_sex_side_after f_closed
    with {'master': dissolve}
    maria "{i}* Merengek*{/i}"

    jump scene_maria_sex_storage.outro


label scene_maria_sex_tony.cum:
    tony "Jesus, I ain't gonna last much longer back here..."

    tony "... You gettin' close, kid?"

    anon "Ya!"

    tony "{b}Maria{/b}?"

    maria "I'm cumming!!"

    maria "I'M CUMMING!!!"

    tony "Heh, perfect timin'."

    tony "Let her rip, champ!"

    pause
    maria "NGGHHH!!!"

    tony "WAHOOO!!!"

    hide animation
    show maria b_sex_3some_cum
    show maria_body_b_sex_3some_cum_tony as tony_torso
    anon "HNNGGG!!!" with flash
    show xray_maria_sex_3some as xray
    with fastdissolve
    pause
    hide xray
    hide tony_torso
    show maria b_sex_3some_insert_tony
    show maria_body_b_sex_3some_pullout01_anon as anon_cum
    show maria_body_b_sex_3some_pullout01_tony as tony_cum
    with {'master': dissolve}
    tony "Nah, itu menyenangkan!"

    show maria b_sex_3some_base
    show maria_body_b_sex_3some_tony as tony_torso behind tony_cum
    show maria_body_b_sex_3some_pullout02_anon as anon_cum
    show maria_body_b_sex_3some_pullout02_tony as tony_cum
    with {'master': dissolve}
    pause
    hide tony_cum
    hide tony_torso
    with {'master': dissolve}
    tony "C'mon, Champ, roll her over already!"

    tony "You gotta make sure that cannoli's good and filled."

    hide anon_cum
    hide tony_torso
    show maria b_sex_side_after f_closed
    with {'master': dissolve}
    maria "{i}* Merengek*{/i}"


    scene location_pizza_storage_sex_front
    show maria b_sex_front_insert f_happy_closed
    show anon_maria_sex_front inside
    with fade
    anon "Are you okay, {b}Maria{/b}?"

    pause
    maria "Y-yeah, I'm just..."

    show anon_maria_sex_front pre
    show maria_sex_front_mc_after
    hide maria_sex_front_mc_pullout
    with dissolve
    maria "... Feeling very..."

    maria "... Overwhelmed, right now."

    show maria b_sex_front_open
    hide anon_maria_sex_front
    hide maria_sex_front_mc_after
    show maria_sex_front_open_after_threesome
    with dissolve
    anon "Ah, man... You're shaking!"

    tony "It's okay, champ..."

    tony "... We just gotta let the sensations die down a bit."

    pause
    tony "You're alright, ain't ya, darlin'?"

    maria "Mhmm!"

    maria "Just need..."

    maria "... Rest."

    tony "See, there you have it!"

    tony "Let's leave her to compose herself, eh?"

    anon "Y-ya, oke."

    tony "Make sure you keep those legs elevated so his little guys can get to the egg."

    maria "I know how it works, honey..."

    tony "Atta'girl."


    call call_pregnancy_minigame (None, M_maria)
    return 'plus'


label scene_maria_sex_tony.join:
    show maria b_sex_side_after_up f_surprised_down
    show anon maria_sex_side f_confused
    with {'master': dissolve}
    maria "Me!"

    maria "I'm ready!"

    maria f_confused "That's okay, isn't it?"

    anon f_normal "Y-yeah, of course."

    maria "Go ahead and roll over so I can get on top."

    hide anon
    show maria b_sex_3some_insert_anon
    with {'master': dissolve}
    tony "Man, I love this view!"

    pause
    show maria b_sex_3some_talk f_happy_back
    with {'master': dissolve}
    maria "Okay, he's in!"

    show maria_body_b_sex_3some_tony as tony_torso
    show maria_body_b_sex_3some_tony_oil01 as tony_arm
    with {'master': dissolve}
    tony "Just lemme get a few dabs of olive oil in there..."

    show maria f_surprised_back
    show maria_body_b_sex_3some_tony_oil02 as tony_arm
    with {'master': dissolve}
    maria "Oh, it's cold!"

    tony "Heh, it's room temperature!"

    maria "Well, it doesn't feel room temperature."

    tony "Relax, darlin'..."

    tony "... You're gonna get plenty of heat here in just a second, I promise."

    show maria f_lipbite_back
    pause
    maria @ -m_talk "{i}* Merengek*{/i}"

    hide tony_torso
    hide tony_arm
    show maria b_sex_3some_insert_tony
    with {'master': dissolve}
    tony "Now here we go, brace ya self."

    call scene_maria_sex_tony.insert
    with dissolve
    tony "Ngh!"

    maria "Ahh!!"

    tony "Phew, that's nice!"

    call scene_maria_sex_tony.animate
    jump scene_maria_sex_tony.resume


screen scene_maria_sex_tony_controls(tony):
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            if tony != 'plus':
                textbutton _('Roll') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_maria.set, 'sex speed',
                                 1 / (1 / M_maria.get('sex speed') - 2)),
                        Return(False))
                sensitive M_maria.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_maria.set, 'sex speed',
                                 1 / (1 / M_maria.get('sex speed') + 2)),
                        Return(False))
                sensitive M_maria.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
