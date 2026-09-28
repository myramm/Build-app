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
        anon "M'oh, way da rum iz pinnin'??"
        odette "Shh!"

        if rng < .7:
            anon "Guh!"

    elif opt == 3:
        anon "Burrb, i'nda eelin puuukey..."
        odette "Just focus on something, {b}[firstname]{/b}..."

        if rng < .3:
            anon "Hmm?"

        odette "... Like my tits."

        if rng < .4:
            anon "Mmm, ye..."
            anon "... 'em 'um beg ass 'iddies!"

    elif opt == 4:
        odette "You like the way they're bouncing?"
        anon "Oh ye..."
        anon "... 'Oingey, 'oingey, 'oingey!"
        odette "Hehehe!"

    elif opt == 4:
        odette "That's it, big fella..."
        odette "... Just bury your face in there."
        anon "Mm, yee."
        anon "{i}*Inhales*{/i} Ew mel gud."

    elif opt == 5:
        odette "Ahh, this big dick..."
        odette "... Feels so fucking good!"

        if rng < .2:
            odette "I wish I could ride it for all of eternity!"
            anon "Erniny?!"

    return


label scene_odette_crypt_cowgirl.switch:
    odette "C'mon, {b}[firstname]{/b}... harder!"
    anon "M'eye tyin'!"
    anon "'egs dun workin'..."
    call scene_odette_sex_crypt.insert
    with {'master': dissolve}
    odette "Ugh, just-"
    odette "Let me do it!"
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
    odette "Sit down in the throne, I'm gonna ride your cock."
    anon f_flirt "M'oh, yee-"
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
    anon "Mhmm, iz mud bedder."
    call scene_odette_crypt_cowgirl.insert
    with {'master': dissolve}
    odette "Big... fucking... dick..."
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
    anon "Ngh, es no wurkin'!"
    anon "Mi gun puk!"
    odette "No, don't puke!"
    odette "C'mon, I'm almost there!"
    anon "Murrp!"
    pause

    call scene_odette_crypt_cowgirl.loop

    if _return == 'switch':
        jump scene_odette_sex_crypt.switch

    odette "Oh, fuck!"
    anon "Mi 'efinely gun puk."
    odette "Oh, fuck me!!"
    odette "I'm gonna cum!"
    anon "MI GUN PUK, {b}ONETTE{/b}!!"
    anon "Iz gon-"
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
    odette "Mmm, it's so warm."
    anon "Yeah."
    anon "Id I puk?"
    odette "Heh, no you didn't puke."
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
