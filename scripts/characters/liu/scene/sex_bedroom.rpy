label scene_liu_sex_bedroom:
    $ M_liu.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_liu_sex_bedroom.stage
    with fade
    liu "Buru-buru!"

    call scene_liu_sex_bedroom.pre
    with {'master': dissolve}
    liu "{b}[firstname]{/b}... Tolong!"

    call scene_liu_sex_bedroom.insert
    with {'master': dissolve}
    liu "Ahh!!!"

    pause
    liu "Ya Tuhan!"

    liu "Kamu sangat besar!"

    pause
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    liu "Ngh!!!"

    pause
    anon "Apakah kamu baik-baik saja?"

    liu "Ya!"

    liu "Ya!!"

    pause
    liu "aku belum pernah..."

    liu "... Merasakan apa saja..."

    liu "... Seperti ini sebelumnya!"

    pause
    anon "Bagus?"

    liu "YA!!"

    pause
    liu "Saya tidak tahu..."

    liu "... Bisa jadi..."

    liu "...Seperti ini!!"

    pause
    liu "aku akan-"

    pause
    liu "Haaaah... AKU AKAN-"

    pause
    liu "{i}* Merengek*{/i}"

    pause
    show liu b_sex_bed_surprise as anim
    kim "AIYAH!!" with hpunch
    kim "APA YANG KAU LAKUKAN?!"

    anon "Hmm?"

    return


label scene_liu_sex_bedroom.stage:
    scene expression game.timer.image('location_liu_bedroom_sex{}')
    show liu b_sex_bed_pre
    return


label scene_liu_sex_bedroom.pre:
    show liu od_insert
    return


label scene_liu_sex_bedroom.insert:
    show liu b_sex_bed_base
    show anon liu_sex_bedroom
    return


label scene_liu_sex_bedroom.animate:
    hide anon
    hide liu
    show liu_sex_bed_anim as anim
    return


label scene_liu_sex_bedroom.loop:
    call screen scene_liu_sex_bedroom_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_liu_sex_bedroom.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_liu_sex_bedroom.loop


label scene_liu_sex_bedroom.dialogue(opt, rng=-1):
    if opt == 1:
        liu "{b}[firstname]{/b}!"


    elif opt == 2:
        liu "Oh, persetan denganku!"


    elif opt == 3:
        anon "Kamu meremasku begitu erat!"

        liu "Persetan denganku, {b}[firstname]{/b}!!"


    elif opt == 4:
        anon "Wah!"

        liu "Ahhh!"


    elif opt == 5:
        liu "Anda merasa luar biasa!"


    elif opt == 6:
        liu "{i}* Merengek*{/i}"


    return


label scene_liu_sex_bedroom.switch:
    show liu_bedroom_thirst 5 as anim
    with {'master': dissolve}
    liu "MM."


    $ M_liu.set('sex speed', 1. / 8)

    show liu_sex_bed_anim 1 as anim
    with {'master': dissolve}
    pause .5
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    jump scene_liu_sex_bedroom.resume


label scene_liu_sex_bedroom.cum(where):
    liu "aku akan keluar!"

    anon "Saya juga!"

    pause
    liu "Ya Tuhan!!"

    liu "Astaga!!"

    pause
    liu "{b}[firstname]{/b}!!!"

    liu "NGGHHH!!!"

    hide anim

    if where == 'inside':
        show liu b_sex_bed_cum
    else:
        show liu b_sex_bed_pre od_cumshot

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_liu_sex_bed with fastdissolve
        pause
        hide xray_liu_sex_bed with {'master': dissolve}
    else:

        show liu od_cumshot3

    anon "Haah... Haah..."

    return where


label scene_liu_sex_bedroom.first:
    $ M_liu.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='first')

    call scene_liu_sex_bedroom.stage
    with fade
    call scene_liu_sex_bedroom.pre
    with {'master': dissolve}
    liu "Ini sangat besar, aku hampir tidak bisa-"

    pause
    call scene_liu_sex_bedroom.insert
    with {'master': dissolve}
    liu "Ngh!"

    pause
    anon "Pelan-pelan saja, aku tidak ingin kamu menyakiti dirimu sendiri..."

    liu "Y-ya, oke."

    pause
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    pause
    liu "Hmm, Tuhan."

    jump scene_liu_sex_bedroom.merge


label scene_liu_sex_bedroom.repeat:
    $ M_liu.set('sex speed', 1. / 8)
    $ renpy.dynamic(variant='repeat')

    call scene_liu_sex_bedroom.stage
    with fade
    call scene_liu_sex_bedroom.pre
    with {'master': dissolve}
    pause
    call scene_liu_sex_bedroom.insert
    with {'master': dissolve}
    liu "Ngh!"

    anon "Ya Tuhan, {b}Liu{/b}..."

    pause
    call scene_liu_sex_bedroom.animate
    with {'master': dissolve}
    liu "Haah!"

    pause
    liu "Ya!!"

    label scene_liu_sex_bedroom.merge:
    call scene_liu_sex_bedroom.dialogue (1)
    pause
    call scene_liu_sex_bedroom.dialogue (2)
    pause
    call scene_liu_sex_bedroom.dialogue (3)
    pause
    call scene_liu_sex_bedroom.dialogue (4)
    pause
    call scene_liu_sex_bedroom.dialogue (5)
    pause
    call scene_liu_sex_bedroom.dialogue (6)
    label scene_liu_sex_bedroom.resume:
    call scene_liu_sex_bedroom.loop

    if _return == 'switch':
        jump scene_liu_bedroom_thirst.switch

    call scene_liu_sex_bedroom.cum (_return)

    if _return == 'inside':
        show anon liu_sex_bedroom
        show liu b_sex_bed_base
        with dissolve
        pause
        liu "Itu sungguh luar biasa!"

        anon "Hehe, terima kasih."

        liu "aku bisa merasakannya di dalam..."

        liu "... Ini sangat hangat."

        pause
        hide anon
        show liu b_sex_bed_pre o_after
        with dissolve
        pause
        show liu b_sex_bed_cuddle with {'master': dissolve}
        anon "Apakah kamu ingin aku membelikanmu sesuatu?"

        anon "Handuk atau sesuatu-"

        liu "T-tidak, tidak apa-apa."

    else:

        liu "Itu luar biasa!"

        anon "Hehe, terima kasih."

        liu "Kamu sering datang!"

        show liu b_sex_bed_cuddle with dissolve
        pause
        anon "Biarkan aku mengambilkanmu handuk atau apalah."

        liu "T-tidak, tidak apa-apa."


    liu "Bisakah kamu tetap di sini seperti ini, bersamaku, untuk sementara waktu?"

    liu "... Silakan."

    pause
    anon "Y-ya, oke."

    liu "Terima kasih, {b}[firstname]{/b}."

    pause

    if _return == 'inside':
        call call_pregnancy_minigame (None, M_liu)
    return


label scene_liu_sex_bedroom.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['liu']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_liu_bedroom) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_liu_sex_bedroom.first

            "Ulangi" if 'repeat' in variants:
                jump scene_liu_sex_bedroom.repeat

    jump expression 'scene_liu_sex_bedroom.{}'.format(next(iter(variants)))


screen scene_liu_sex_bedroom_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            if variant == 'repeat':
                textbutton _('Switch') action Return('switch')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') - 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_liu.set, 'sex speed',
                                 1 / (1 / M_liu.get('sex speed') + 2)),
                        Return(False))
                sensitive M_liu.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
