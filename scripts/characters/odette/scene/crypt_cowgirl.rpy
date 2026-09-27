label scene_odette_crypt_cowgirl:

    return


label scene_odette_crypt_cowgirl.stage:
    scene location_crypt_sex
    show odette_body_b_sex_vamp_missionary_insert as anim
    return


label scene_odette_crypt_cowgirl.insert:
    show odette_body_b_sex_vamp_missionary_anim04 as anim
    return


label scene_odette_crypt_cowgirl.animate:
    show odette_crypt_cowgirl as anim
    return


label scene_odette_crypt_cowgirl.loop:
    call screen scene_odette_crypt_cowgirl_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_crypt_cowgirl.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_crypt_cowgirl.loop


label scene_odette_crypt_cowgirl.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Ahh!!"

        anon "Ooh."


    elif opt == 2:
        anon "M'oh, bagaimana rum bisa pinnin'??"

        odette "Ssst!"


        if rng < .7:
            anon "huh!"


    elif opt == 3:
        anon "Burrb, aku tidak mau puuukey..."

        odette "Fokus saja pada sesuatu, {b}[firstname]{/b}..."


        if rng < .3:
            anon "Hmm?"


        odette "... Seperti payudaraku."


        if rng < .4:
            anon "Mmm, kamu..."

            anon "... mereka mohon, bodoh!"


    elif opt == 4:
        odette "Anda menyukai cara mereka memantul?"

        anon "Oh ya..."

        anon "... 'Oingey, 'oingey, 'oingey!"

        odette "Hehehe!"


    elif opt == 4:
        odette "Itu dia, sobat besar..."

        odette "... Benamkan saja wajahmu di sana."

        anon "Mm, ya."

        anon "{i}*Tarik napas*{/i} Bagus sekali."


    elif opt == 5:
        odette "Ahh, penis besar ini..."

        odette "... Terasa sangat enak!"


        if rng < .2:
            odette "Saya berharap saya bisa mengendarainya selamanya!"

            anon "Erniny?!"


    return


label scene_odette_crypt_cowgirl.switch:
    odette "Ayo, {b}[firstname]{/b}...lebih keras!"

    anon "Aduh!"

    anon "'misalnya tidak bekerja'..."

    call scene_odette_sex_crypt.insert
    with {'master': dissolve}
    odette "Ugh, hanya-"

    odette "Biarkan aku melakukannya!"

    anon "Murr?"


    scene location_crypt_side
    show odette b_vamp_sitting f_smirk
    show anon b_shirt f_confused od_dick4:
        xoffset -175
    with fade
    pause
    show location_crypt_side_overlay as armrest
    show odette b_naked_vamp_pull_anon:
        xoffset -200
    show anon b_empty
    with {'master': dissolve}
    odette "Duduklah di singgasana, aku akan menunggangi kemaluanmu."

    anon f_flirt "M'oh, ya-"

    hide armrest
    show odette f_laugh:
        xoffset -250
        xzoom -1
    show anon f_shock:
        xoffset -275
        xzoom -1
    with {'master': dissolve}
    pause .6
    show location_crypt_side_overlay as armrest
    show odette a_reveal b_naked_vamp:
        xoffset -75
    show anon b_onbed_shirt_falling behind armrest:
        offset (-25, 110)
        xzoom 1
    with {'master': dissolve}
    pause

    $ M_odette.set('sex speed', 1. / 8)

    call scene_odette_crypt_cowgirl.stage
    with fade
    anon "Mhmm, seperti alas lumpur."

    call scene_odette_crypt_cowgirl.insert
    with {'master': dissolve}
    odette "Besar... sial... kontol..."

    call scene_odette_crypt_cowgirl.animate
    with {'master': dissolve}
    call scene_odette_crypt_cowgirl.dialogue (1)
    pause
    call scene_odette_crypt_cowgirl.dialogue (2)
    pause
    call scene_odette_crypt_cowgirl.dialogue (3)
    pause
    call scene_odette_crypt_cowgirl.dialogue (4)
    pause
    call scene_odette_crypt_cowgirl.dialogue (5)
    pause
    anon "Ngh, tidak apa-apa!"

    anon "Mi gun puk!"

    odette "Tidak, jangan muntah!"

    odette "Ayo, aku hampir sampai!"

    anon "Murrp!"

    pause

    call scene_odette_crypt_cowgirl.loop

    if _return == 'switch':
        jump scene_odette_sex_crypt.switch

    odette "Astaga!"

    anon "Mi 'dengan halus gun puk."

    odette "Oh, persetan denganku!!"

    odette "aku akan keluar!"

    anon "MI GUN PUK, {b}ONETTE{/b}!!"

    anon "Aku akan-"

    odette "NGGHHH!!!"

    anon "Buuurb-"

    show odette_body_b_sex_vamp_missionary_cum as anim
    anon "HRRRNNGGG!!!" with flash
    show xray_side as xray:
        anchor (.5, .5)
        pos (250 + 241, 250 - 2)
        rotate 98
        rotate_pad False
        zoom .74
    with {'master': fastdissolve}
    pause
    hide xray
    call scene_odette_crypt_cowgirl.insert
    with {'master': dissolve}
    anon "Haah... Haah..."

    show odette_crypt_cowgirl_cum as cum
    odette "Hmm, hangat sekali."

    anon "Ya."

    anon "Apakah aku muntah?"

    odette "Heh, tidak, kamu tidak muntah."

    return


screen scene_odette_crypt_cowgirl_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()
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
