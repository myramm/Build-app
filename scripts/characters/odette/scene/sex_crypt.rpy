label scene_odette_sex_crypt:

    return


label scene_odette_sex_crypt.stage:
    scene location_crypt_sex
    show odette b_sex_vamp_base o_pre
    show location_crypt_sex_throne_overlay as armrest
    return


label scene_odette_sex_crypt.insert:
    hide anim
    show odette b_sex_vamp_insert d_insert
    return


label scene_odette_sex_crypt.animate:
    hide odette
    show odette_body_b_sex_vamp_anim as anim behind armrest
    return


label scene_odette_sex_crypt.loop:
    call screen scene_odette_sex_crypt_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_sex_crypt.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_sex_crypt.loop


label scene_odette_sex_crypt.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Oh, aku sudah memimpikan hal ini sejak lama!"

        odette "Rasanya luar biasa!"


    elif opt == 2:
        odette "Persetan denganku, {b}[firstname]{/b}!"


        if rng < .3:
            odette "Persetan dengan vagina vampirku yang kotor!"

            anon "AMPUR?"

            anon "Wazzit-"


        odette "Lebih sulit!"


    elif opt == 3:
        if rng < .6:
            anon "Hinga akhirmu adalah iggin dan mah ack!"


        odette "Katakan padaku aku ratumu!"


        if rng < .3:
            anon "Hah?"

            odette "Katakan!"


        anon "Anda mah tertarik."

        odette "Ya!"


    elif opt == 4:
        odette "Bisakah kamu merasakan mereka memperhatikan kita?"

        anon "Hoo?"

        odette "Arwah orang yang baru saja pergi."

        odette "Itu membuatku sangat basah!"

        anon "Eh ya ampun!"


    elif opt == 5:
        odette "Ya, itu dia!{p=2}{nw}"

        odette "Ahhhh!{p=1}{nw}"


    elif opt == 6:
        odette "Anda menyukainya, {b}[firstname]{/b}?{p=2}{nw}"

        anon "Eh ya ampun!{p=1}{nw}"


    elif opt == 7:
        if rng < .2:
            odette "Sial!{p=1}{nw}"

            odette "Aku akan keluar!{p=1}{nw}"


    return


label scene_odette_sex_crypt.switch:
    call scene_odette_crypt_cowgirl.insert
    with {'master': dissolve}
    odette "Oke oke..."

    odette "... Sebaiknya kau mundur."

    anon "Hmm?"

    call scene_odette_crypt_cowgirl.stage
    with {'master': dissolve}
    odette "Anda akan merasa lebih baik, percayalah."

    anon "Ugh, oke."


    scene location_crypt_side
    show odette b_naked_vamp_pull_anon f_smirk:
        xoffset -250
        xzoom -1
    show anon b_empty f_worried:
        xoffset -275
        xzoom -1
    with fade
    odette "Apakah itu membantu?"

    anon f_shy "Mm, tawaran teka-teki."

    show odette:
        xoffset -175
        xzoom 1
    show anon f_surprised_shock_food:
        xoffset -150
        xzoom 1
    with {'master': dissolve}
    odette "Bagus..."

    show odette b_vamp_sitting:
        xoffset 0
    show anon a_cannoli_gobble b_shirt od_dick4
    with {'master': dissolve}
    odette "... Sekarang lemparkan kembali ke sana, kawan!"

    show anon f_disgusted_wince
    with {'master': dissolve}
    anon "{i}*Meneguk*{/i}"


    $ M_odette.set('sex speed', 1. / 8)

    call scene_odette_sex_crypt.stage
    with fade
    odette "Cepatlah!"

    show odette b_sex_vamp_insert d_rub f_down
    with {'master': dissolve}
    anon "Aku sedang mencoba."

    show odette b_sex_vamp_base o_pre
    with {'master': dissolve}
    odette "Ngh!"

    call scene_odette_sex_crypt.insert
    with {'master': dissolve}
    odette "Ahhh!"

    anon "Ya Tuhan!"

    call scene_odette_sex_crypt.animate
    with {'master': dissolve}
    jump scene_odette_sex_crypt.resume


label scene_odette_sex_crypt.cum(where):
    odette "Astaga!"

    odette "aku akan keluar!"

    anon "Ya ampun!"

    anon "Aku akan-"

    odette "NGGHHH!!!"

    hide anim

    if where == 'inside':
        show odette b_sex_vamp_cum behind armrest
    else:
        show odette b_sex_vamp_base o_cumshot f_down behind armrest

    anon "HNNGGG!!!" with flash

    if where == 'inside':
        show xray_odette_vamp_sex with fastdissolve:
            align (0, 0)
        pause
        hide xray_odette_vamp_sex
    else:
        show odette_overlay_sex_vamp_base_o_cumshot03
        show odette o_empty

    if where == 'inside':
        show odette b_sex_vamp_insert f_down o_pullout
        with dissolve

    anon "Haah... Haah..."


    if where == 'inside':
        show odette b_sex_vamp_base o_after with dissolve

    odette "Hmm, hangat sekali."

    show odette f_normal
    anon "Ya."

    anon "Aku tidak ada... T harr..."

    odette "Hehehe!"

    return


label scene_odette_sex_crypt.repeat:
    $ M_odette.set('sex speed', 1. / 8)

    call scene_odette_sex_crypt.stage
    with fade
    odette "Masukkan saja ke dalam diriku, {b}[firstname]{/b}!"

    show odette b_sex_vamp_insert d_rub f_down
    with {'master': dissolve}
    odette "Ahhh!"

    anon "Aku sedang mencoba."

    show odette b_sex_vamp_base o_pre
    with {'master': dissolve}
    anon "eberphing o merah dan kelinci."

    call scene_odette_sex_crypt.insert
    with {'master': dissolve}
    odette "Ngh!"

    anon "Tuhan ib."

    call scene_odette_sex_crypt.animate
    with {'master': dissolve}
    pause
    call scene_odette_sex_crypt.dialogue (1)
    pause
    call scene_odette_sex_crypt.dialogue (1)
    pause
    call scene_odette_sex_crypt.dialogue (3)
    pause
    call scene_odette_sex_crypt.dialogue (4)
    pause
    call scene_odette_sex_crypt.dialogue (5)
    pause
    call scene_odette_sex_crypt.dialogue (6)
    pause
    call scene_odette_sex_crypt.dialogue (7)
    pause

    label scene_odette_sex_crypt.resume:
    call scene_odette_sex_crypt.loop

    if _return == 'switch':
        jump scene_odette_crypt_cowgirl.switch

    call scene_odette_sex_crypt.cum (_return)
    return


label scene_odette_sex_crypt.replay:
    jump scene_odette_sex_crypt.repeat


screen scene_odette_sex_crypt_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum Inside') action Return('inside')
            textbutton _('Cum Outside') action Return('outside')
            textbutton _('Switch') action Return('switch')

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
