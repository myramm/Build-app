label scene_odette_blowjob(variant='_naked'):
    scene location_tattoo_rooftop_sex_bj
    call scene_odette_blowjob.animation
    with fade
    anon "Aduh!"

    odette "{i}*Terkikik*{/i}"

    pause
    anon "Oke, wah!"

    anon "Apakah ini benar-benar terjadi?"

    odette "Mhmm!"

    anon "Maksudku, kita hampir tidak mengenal satu sama lain dan kamu..."

    odette "{i}*Sluuuuuurp*{/i}"

    anon "... Ya ampun!"

    pause
    anon "Hati-hati dengan bolanya, kamu meremasnya sedikit-"

    $ M_odette.set('sex speed', 1. / 12)
    anon "!!!" with hpunch
    anon "Aduh!!!"

    odette "{i}*Terkikik*{/i}"

    anon "Oh oke... itu agak tak terduga, hanya-"

    $ M_odette.set('sex speed', 1. / 16)
    anon "!!!" with hpunch
    anon "Ya Tuhan!!"

    pause
    anon "Aku semakin dekat!"

    anon "Sungguh, SANGAT dekat, aku-"

    anon "saya-"

    grace "{b}Odette{/b}!"

    show odette_sex_bj_naked_surprised as animation
    odette "( !!! )" with hpunch
    grace "{b}Odette{/b}, kamu dimana?!"

    show odette_sex_bj_naked_look as animation with {'master': dissolve}
    odette "{i}*Ahem*{/i} Aku di atap bersama {b}[firstname]{/b}, umm... ngobrol..."

    odette "... J-hanya bicara!"

    grace "{b}Odette{/b}, berhenti main-main dan turun ke sini!"

    grace "Saya butuh bantuan Anda!"

    odette "Ya, tentu... oke!"

    odette "Saya akan segera ke sana!"

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
        odette "MM."

        odette "{i}*Sluuuuurp*{/i}"

    if animcounter == 1 and rng > 85:
        anon "Ya ampun..."

        anon "... Kamu benar-benar pandai dalam hal ini!"

        odette "Mhmm!"

    if animcounter == 2 and rng > 92:
        odette "{i}*Suara senandung*{/i}"

        anon "Oh, {b}Odette{/b}... Wah!"

    elif animcounter == 2 and rng > 85:
        odette "{i}*Gluulggh*{/i}"

        anon "Jangan berhenti!"

        odette "hehe!"

    return


label scene_odette_blowjob.repeat(variant=''):
    scene location_tattoo_indoor_sex_bj
    call scene_odette_blowjob.animation
    with fade
    anon "{b}Odette{/b}!!!"

    anon "Bagaimana jika seseorang masuk?!"

    odette "Ya ampun, abubit!"

    anon "Hah?"

    pause
    anon "Ini ide yang buruk..."

    odette "Hehehe!"

    pause
    odette "MM."

    odette "{i}*Sluuuuurp*{/i}"

    pause
    anon "Ya ampun..."

    anon "... Kamu benar-benar pandai dalam hal ini!"

    odette "Mhmm!"

    pause
    odette "{i}*Suara senandung*{/i}"

    anon "Oh, {b}Odette{/b}... Wah!"

    pause
    odette "{i}*Gluulggh*{/i}"

    anon "Jangan berhenti!"

    odette "hehe!"

    call scene_odette_blowjob.loop
    anon "Aku semakin dekat!"

    odette "Gilb id eww mmeeh, iig alla!"

    anon "{b}Odette{/b}, I-"

    odette "{i}*Suara senandung*{/i}"

    show odette_sex_bj_cum as animation
    anon "HNNGGG!!!" with flash
    odette "{i}*Meneguk* *Meneguk*{/i}"

    anon "Sialan!"

    odette "{i}*Meneguk*{/i}"

    show odette_sex_bj_show as animation
    with {'master': dissolve}
    odette "{i}*Pukulan*{/i} Maahh!"

    anon "Kamu luar biasa!"

    odette "hehe!"

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
            "Atap (Tanpa baju)" if 'roof' in variants:
                jump scene_odette_blowjob.roof

            "Gula Tat" if 'shop' in variants:
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
