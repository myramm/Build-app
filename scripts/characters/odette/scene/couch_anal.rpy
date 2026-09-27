label scene_odette_couch_anal:
    $ M_odette.set('sex speed', 1 / 8.)
    $ renpy.dynamic(rv={'anal'})

    call scene_odette_couch_anal.stage
    with fade
    anon "Jadi, apakah Anda sudah sering melakukan ini?"

    odette "Bagaimana menurutmu?"

    anon "Saya berpikir ya."

    call scene_odette_couch_anal.insert
    odette "OHH, FUCK!!" with hpunch
    show odette -f_surprised m_talk
    anon "Terlalu cepat?"

    show odette -m_talk
    odette "Ya."

    anon "Maaf!"

    odette "Haah... Haah..."

    odette "{i}*Iiith*{/i} Tidak apa-apa..."

    odette "... Hanya-"

    call scene_odette_couch_anal.animate
    with dissolve
    call scene_odette_couch_anal.dialogue (1)
    pause
    call scene_odette_couch_anal.dialogue (2)
    pause
    call scene_odette_couch_anal.dialogue (3)
    pause
    call scene_odette_couch_anal.dialogue (4)
    pause
    call scene_odette_couch_anal.dialogue (5)
    pause
    call scene_odette_couch_anal.dialogue (6)
    pause
    call scene_odette_couch_anal.dialogue (7)
    pause

    label scene_odette_couch_anal.resume:
    call scene_odette_couch_anal.loop

    if _return == 'switch':
        jump scene_odette_couch_back.switch

    anon "aku akan meledak!"

    odette "Jangan berhenti!!"

    anon "Saya tidak bisa menahannya!"

    odette "Jangan-"

    odette "NGGHHH!!!"


    show odette_sex_couch_anal_cum as anim
    anon "HNNGGG!!!" with flash
    pause

    show odette_sex_couch_anal_insert as anim
    show odette sex_couch_anal
    with {'master': dissolve}
    anon "Haah... Haah..."

    show odette_sex_couch_anal_pre as anim
    show odette_sex_couch_anal_after
    with {'master': dissolve}
    odette "Fuuuuuck."

    anon "Kamu baik-baik saja?"

    odette "Heh, itu sangat intens!"

    anon "Intens baik atau intens buruk?"

    odette "Keduanya."

    anon "Benar-benar?"

    odette "hehe!"

    return rv


label scene_odette_couch_anal.stage:
    scene location_tattoo_garage_anal_sex
    show odette_sex_couch_anal_pre as anim
    show odette sex_couch_anal
    return


label scene_odette_couch_anal.insert:
    show odette_sex_couch_anal_insert as anim
    show odette f_surprised
    return


label scene_odette_couch_anal.animate:
    hide odette
    show odette_sex_couch_anal as anim
    return


label scene_odette_couch_anal.loop:
    call screen scene_odette_couch_anal_controls

    if _return:
        return _return

    python hide:
        blocks = 7
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_odette_couch_anal.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_odette_couch_anal.loop


label scene_odette_couch_anal.dialogue(opt, rng=-1):

    if opt == 1:
        odette "Sialan!"


    elif opt == 2:
        odette "Ya Tuhan, ya Tuhan, Ya Tuhan!!"

        anon "Kamu baik-baik saja?"

        odette "Kamu benar-benar besar!"


        if rng < .5:
            anon "Haruskah saya berhenti?"

            odette "T-tidak!"


    elif opt == 3:
        anon "Aku bisa merasakan bajinganmu mengejang..."

        odette "Sial!"

        anon "... Dan kakimu gemetar juga!"


    elif opt == 4:
        if rng < .5:
            odette "aku akan keluar!"

            anon "Sudah?!"

            odette "Ya!!!"


        odette "GRAAAAAH!!!" with flash
        anon "Wah!"

        odette "Sial, sial, FUUUUCK!!"


    elif opt == 5:
        odette "Sangat dalam!"

        anon "Saya bisa masuk lebih dalam."

        odette "T-tidak, jangan-"

        odette "NGH!!"


    elif opt == 6:
        odette "Ahh!!"

        odette "Persetan denganku!"

        odette "Persetan!!"

        anon "Ini luar biasa!"


    elif opt == 7:
        anon "Pantatmu kencang sekali, {b}Odette{/b}!"

        anon "Aku tidak akan bertahan lebih lama jika terus begini."

        odette "Ahh!!"


    return


label scene_odette_couch_anal.switch:
    $ M_odette.set('sex speed', 1 / 8.)
    $ rv.add('anal')

    if 'v->a' not in rv:
        $ rv.add('v->a')
        call scene_odette_couch_back.stage
        with dissolve
        odette @ -m_talk "Hmm?"

        odette "Kenapa kamu berhenti?"

        anon "Saya tidak akan berhenti... Saya berpindah lubang."

        call scene_odette_couch_anal.stage
        with fade
        odette "Bertukar lubang?!"

        odette "Apakah itu berarti apa yang kupikirkan-"

        call scene_odette_couch_anal.insert
        with {'master': dissolve}
        odette "OHHHH KAI.."

        odette -f_surprised "... Fuuuuuuuck!"

        anon "Kamu baik-baik saja?"

        odette "Uhh, ya!"

        odette "Hanya {i}benar-benar{/i} ayam sialan besar di pantatku..."

        odette "{i}*Ahem*{/i} ... Tidak masalah."

        anon "Anda yakin?"

        odette @ -m_talk "Mhmm!"

        pause
        anon "Jadi aku bisa melanjutkan dan-"

        odette "YA!"

        call scene_odette_couch_anal.animate
        with dissolve
        anon "Dingin."

        odette "Sial, sial, sial, sial, sial..."

    else:

        call scene_odette_couch_back.stage
        with dissolve
        odette "Lagi?!"

        odette "Dengan serius?!"

        call scene_odette_couch_anal.stage
        with fade
        anon "Saya tidak bisa memutuskan lubang mana yang lebih saya sukai..."

        odette "Heh, kamu beruntung aku pelacur kotor..."

        odette "... Cukup yakin tidak ada gadis lain yang akan membiarkanmu pergi bersama-"

        call scene_odette_couch_anal.insert
        odette "Fuuuuuuuuck me!!" with hpunch
        call scene_odette_couch_anal.animate
        with {'master': dissolve}
        anon "Itu rencananya!"

        odette "Ya Tuhan, ya Tuhan, Ya Tuhan!!!"


    pause
    jump scene_odette_couch_anal.resume












screen scene_odette_couch_anal_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('inside')
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
