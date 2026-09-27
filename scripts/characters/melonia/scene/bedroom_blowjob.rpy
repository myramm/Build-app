label scene_melonia_bedroom_blowjob:

    return


label scene_melonia_bedroom_blowjob.stage:
    scene location_rump_bedroom_bed_sex_bj
    show melonia_body_b_sex_bj_base as anim
    show melonia_body_b_sex_bj_base_face_talk_pre as face
    show melonia_body_b_sex_bj_base_dick as dick
    return


label scene_melonia_bedroom_blowjob.insert:
    hide face
    hide dick
    show melonia_bedroom_blowjob 1 as anim
    return


label scene_melonia_bedroom_blowjob.animate:
    show melonia_bedroom_blowjob as anim
    return


label scene_melonia_bedroom_blowjob.loop:
    call screen scene_melonia_bedroom_blowjob_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_melonia_bedroom_blowjob.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_melonia_bedroom_blowjob.loop


label scene_melonia_bedroom_blowjob.dialogue(opt, rng=-1):

    if opt == 1:
        melonia "{i}*Suara kacau*{/i}"


        if rng < .5:
            anon "Apa itu?"

            melonia "{i}*Suara kacau semakin intensif*{/i}"


        if rng < .3:
            anon "Anda menginginkannya lebih dalam?"

            melonia "{i}*Erangan yang menantang*{/i}"


        anon "Maksudku, itu sudah cukup dalam tetapi jika kamu memaksa..."

        $ M_melonia.set('sex speed', 1 / (
            20. if rng < 0 else (1 / M_melonia.get('sex speed') + 4)))
        melonia "{i}*Gllllckk* *Gllllckk* *Gllllckk*{/i}"


        if rng < .5:
            anon "... Benar, ambillah!"


    elif opt == 2:
        anon "Ya, begitu saja."

        melonia "{i}* Merengek*{/i}"

        anon "Hati-hati dengan gigi."


    elif opt == 3:
        anon "Ya ampun..."

        anon "... Aku tidak akan berbohong, sejauh ini ini adalah seks paling menyenangkan yang pernah kulakukan denganmu."


        if rng < .4:
            anon "Mungkin aku harus memasukkan penisku ke tenggorokanmu lebih sering?"

            melonia "{i}*Mendengus tak jelas*{/i}"


    elif opt == 4:
        if rng < .6:
            melonia "MM."


        melonia "{i}*Pernapasan meningkat*{/i}"

        anon "Anda mulai melakukan hal ini, bukan?"

        melonia "{i}*erangan antusias*{/i}"


        if rng < .4:
            anon "Aku mengetahuinya!"


    elif opt == 5:
        melonia "{i}*Gllllckk* *Gllllckk* *Gllllckk*{/i}"


        if rng < .6:
            melonia "{i}*Meneguk*{/i}"


        if rng < .3:
            melonia "{i}*Gllllckk* *Gllllckk* *Gllllckk*{/i}"


    return


label scene_melonia_bedroom_blowjob.switch:
    $ M_melonia.set('sex speed', 1. / 8)

    hide anim
    call scene_melonia_bedroom_press.pre
    show melonia f_annoyed
    with {'master': dissolve}
    melonia "Hei..."

    melonia f_confused "... Kenapa kamu berhenti?!"

    anon "Aku tidak bisa mendengarkan mulutmu lagi!"


    call scene_melonia_bedroom_blowjob.stage
    with fade
    melonia "A-apa yang kamu lakukan?!"

    show melonia_body_b_sex_bj_base_face_pre as face
    anon "Membungkammu untuk selamanya."

    show melonia_body_b_sex_bj_base_face_talk_pre as face
    melonia "Apa-"

    call scene_melonia_bedroom_blowjob.insert
    melonia "{i}*Gaaaum*{/i}" with hpunch
    call scene_melonia_bedroom_blowjob.animate
    with {'master': dissolve}
    melonia "!!!"
    pause
    anon "Ini dia..."

    melonia "{i}*Gllllckk*{/i}"

    anon "... Itu jauh lebih baik!"

    pause
    call scene_melonia_bedroom_blowjob.dialogue (1)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (2)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (3)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (4)
    pause
    call scene_melonia_bedroom_blowjob.dialogue (5)
    pause
    call scene_melonia_bedroom_blowjob.loop

    show melonia_body_b_sex_bj_cum as anim
    anon "HNNGGG!!!" with flash
    melonia "!!!"
    melonia "{i}*Meneguk* *Meneguk* *Meneguk*{/i}"

    anon "Oh, ambillah semuanya... Dasar gadis kotor!"

    show melonia_body_b_sex_bj_cum_drip1 as cum
    melonia "{i}*Splurrrt*{/i}" with flash
    show melonia_bedroom_blowjob_cum as cum
    melonia "{i}*Cough* *Sputter* *Cough*{/i}" with flash
    show melonia_body_b_sex_bj_base as anim
    show melonia_body_b_sex_bj_base_face_after
    show melonia_body_b_sex_bj_base_dick
    show melonia_body_b_sex_bj_base_dick_wet
    with {'master': dissolve}
    pause
    return 'blowjob'


screen scene_melonia_bedroom_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_melonia.set, 'sex speed',
                                 1 / (1 / M_melonia.get('sex speed') - 2)),
                        Return(False))
                sensitive M_melonia.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_melonia.set, 'sex speed',
                                 1 / (1 / M_melonia.get('sex speed') + 2)),
                        Return(False))
                sensitive M_melonia.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
