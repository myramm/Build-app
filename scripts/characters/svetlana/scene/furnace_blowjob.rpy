label scene_svetlana_furnace_blowjob:
    $ M_svetlana.set('sex speed', 1 / 8.)

    call scene_svetlana_furnace_blowjob.stage
    with fade
    svetlana "Lovely." (show_native="Prekrasnyy.")
    pause
    show svetlana f_normal_back
    with {'master': dissolve}
    svetlana "Ini adalah penis yang indah."

    anon "T-terima kasih."

    show anon f_surprised
    show svetlana a_rub f_normal
    with {'master': dissolve}
    anon "Haaah!"

    pause
    svetlana "Jarang menemukan seseorang yang begitu tinggi tetapi juga sangat gemuk..."

    show anon f_confused
    with {'master': dissolve}
    anon "F-lemak?"

    show svetlana f_sexy_back
    with {'master': dissolve}
    svetlana "Ya, gendut."

    show anon f_surprised
    show svetlana f_sexy
    with {'master': dissolve}
    pause
    svetlana "Saya yakin rasanya seperti burger keju dan minuman cola."

    show anon f_nervous
    with {'master': dissolve}
    anon "Ehh, aku tidak tahu tentang itu-"

    call scene_svetlana_furnace_blowjob.insert
    with {'master': dissolve}
    anon "Ohhh, Tuhan!"

    call scene_svetlana_furnace_blowjob.animate
    with {'master': dissolve}
    call scene_svetlana_furnace_blowjob.dialogue (1)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (2)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (3)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (4)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (5)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (6)
    pause
    call scene_svetlana_furnace_blowjob.stage
    with {'master': dissolve}
    svetlana f_sexy @ -m_talk "MM."

    show svetlana f_sexy_back
    with {'master': dissolve}
    svetlana "Aku salah, kamu merasakan kelapa."

    show anon f_confused
    with {'master': dissolve}
    anon "Oh?"

    pause
    show anon f_thinking_up
    show svetlana f_normal
    with {'master': dissolve}
    anon "Itu mungkin sabun yang aku gunakan untuk mandi..."

    anon "... Induk semang saya membelinya."

    show anon f_surprised
    show svetlana a_rub
    with {'master': dissolve}
    anon @ -m_talk "!!!"
    show anon f_nervous
    with {'master': dissolve}
    anon "... Aku tidak yakin kenapa aku baru saja memberitahumu hal itu."

    svetlana "Heh, tidak apa-apa.. kamu tidak perlu malu."

    show anon f_surprised
    with {'master': dissolve}
    pause
    show svetlana a_hold f_sexy_back
    with {'master': dissolve}
    svetlana "Baiklah, saya yakin Anda sudah siap."

    show anon f_confused
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    anon "Siap untuk apa?"

    svetlana "Diam dan berbaring."

    anon "Apa-"

    show anon f_thinking_up
    with {'master': dissolve}
    anon "Di ban berjalan?"

    show anon f_nervous
    with {'master': dissolve}
    svetlana "Ya."

    return


label scene_svetlana_furnace_blowjob.stage:
    scene location_warehouse_furnace_convey_front_any
    show svetlana furnace_blowjob
    show anon svet_furnace_blowjob
    return


label scene_svetlana_furnace_blowjob.insert:
    hide anon
    show svetlana furnace_blowjob b_anim01
    return


label scene_svetlana_furnace_blowjob.animate:
    hide svetlana
    show svetlana_furnace_blowjob_body_b_anim as anim
    return


label scene_svetlana_furnace_blowjob.loop:
    call screen scene_svetlana_furnace_blowjob_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_svetlana_furnace_blowjob.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_svetlana_furnace_blowjob.loop


label scene_svetlana_furnace_blowjob.dialogue(opt, rng=-1):

    if opt == 1:
        anon "Oke..."

        svetlana "{i}*Sluuuurp*{/i}"

        anon "... Oh BAIK!"


    elif opt == 2:
        anon "Wah!"

        svetlana "MM."

        anon "Oke, kamu benar-benar pandai dalam hal itu!"


    elif opt == 3:
        svetlana "{i}*Gllck* *Gllck* *Gllck*{/i}"

        anon "Sialan!"


    elif opt == 4:
        svetlana "{i}*Suara senandung*{/i}"

        anon "Ohh, apa itu?!"

        anon "Apakah kamu bersenandung?"

        svetlana "Mhmm."


    elif opt == 5:
        anon "Ahh!!"

        anon "Ya Tuhan!"


    elif opt == 6:
        svetlana "{i}*Senandung semakin intensif{/i}"

        anon "Sialan wow!"

        anon "Rasanya luar biasa!"


    return


label scene_svetlana_furnace_blowjob.first:
    jump scene_svetlana_furnace_blowjob


label scene_svetlana_furnace_blowjob.repeat:
    $ M_svetlana.set('sex speed', 1 / 8.)

    call scene_svetlana_furnace_blowjob.stage
    with fade
    svetlana "It's even larger than I remember." (show_native="Ty dazhe bol'she, chem ya pomnyu.")
    anon @ -m_talk "Hmm?"

    show svetlana f_normal_back
    with {'master': dissolve}
    svetlana "Tidak ada apa-apa."

    show anon f_surprised
    show svetlana a_rub f_normal
    with {'master': dissolve}
    anon "Haaah!"

    pause
    show svetlana f_normal_back
    with {'master': dissolve}
    svetlana "Anda suka melihat ayam Amerika Anda yang besar dan gemuk bergesekan dengan puting saya?"

    show anon f_nervous
    with {'master': dissolve}
    anon @ -m_talk "Mhmm."

    show svetlana f_sexy_back
    with {'master': dissolve}
    svetlana "Haruskah aku memasukkannya ke dalam mulutku sekarang?"

    anon "Oh, ya... tolong."

    svetlana "Heh, kamu bertanya dengan sangat sopan..."

    show svetlana f_sexy
    with {'master': dissolve}
    svetlana "... Saya suka ini."

    call scene_svetlana_furnace_blowjob.insert
    with {'master': dissolve}
    anon "Ohhh, Tuhan!"

    call scene_svetlana_furnace_blowjob.animate
    with {'master': dissolve}
    call scene_svetlana_furnace_blowjob.dialogue (1)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (2)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (3)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (4)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (5)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (6)
    pause
    svetlana "{i}*Gllck* *Gllck* *Gllck*{/i}"

    anon "Yesus!"

    anon "Aku semakin dekat!"

    svetlana "{i}*Sluuuurp*{/i}"

    pause

    call scene_svetlana_furnace_blowjob.loop

    anon "Ini dia..."

    anon "... Datang!!"

    pause
    hide anim
    show svetlana furnace_blowjob b_cum
    anon "HNNGGG!!!" with flash
    pause
    svetlana "{i}*Meneguk* *Meneguk*{/i}"

    anon "Ahhh!!!"

    pause
    show anon svet_furnace_blowjob f_surprised
    show svetlana b_base f_cum o_cum
    with {'master': dissolve}
    anon "Haah... Haah..."

    show svetlana f_sexy
    with {'master': dissolve}
    svetlana @ -m_talk "{i}*Meneguk*{/i}"

    show anon f_nervous
    show svetlana f_sexy_back
    with {'master': dissolve}
    anon "Fiuh, aku melihat bintang di sini."

    svetlana "Hehe."

    return


label scene_svetlana_furnace_blowjob.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['svetlana']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_warehouse_furnace) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_svetlana_furnace_blowjob.first

            "Ulangi" if 'repeat' in variants:
                jump scene_svetlana_furnace_blowjob.repeat

    jump expression 'scene_svetlana_furnace_blowjob.{}'.format(next(iter(variants)))



screen scene_svetlana_furnace_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('inside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_svetlana.set, 'sex speed',
                                 1 / (1 / M_svetlana.get('sex speed') - 2)),
                        Return(False))
                sensitive M_svetlana.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_svetlana.set, 'sex speed',
                                 1 / (1 / M_svetlana.get('sex speed') + 2)),
                        Return(False))
                sensitive M_svetlana.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
