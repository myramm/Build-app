label scene_svetlana_furnace_cowgirl:
    $ M_svetlana.set('sex speed', 1 / 8.)
    $ renpy.dynamic(variant='first')

    call scene_svetlana_furnace_cowgirl.stage
    with fade
    anon @ -m_talk "!!!"
    anon "Ya Tuhan..."

    anon "... Ini benar-benar akan terjadi, ya?"

    svetlana "Ya."

    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana "Mmm, a perfect fit." (show_native="Mmm, ideal'no podkhodit.")
    anon "Ya Tuhan, ya Tuhan, ya Tuhan!"

    call scene_svetlana_furnace_cowgirl.animate
    with {'master': dissolve}
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (1)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (2)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (3)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (4)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (5)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (6)
    pause

    label scene_svetlana_furnace_cowgirl.resume:
    call scene_svetlana_furnace_cowgirl.loop

    if _return == 'switch':
        jump scene_svetlana_furnace_doggy.switch

    svetlana "Selesaikan di dalam!"

    anon "Benar-benar?"

    svetlana "Ya!"


    if variant == 'first':
        anon "A-bagaimana jika kamu ?!"

        svetlana "Saya tidak bisa!"

        anon "Kamu tidak bisa?!"


    svetlana "Cum in me!" (show_native="Konchi v menya!!")

    if variant == 'first':
        anon "Bagaimana Anda bisa yakin-"

    else:
        pause

    svetlana "aku keluar!"

    svetlana "Oh, aku keluar!!!"

    anon "Sialan!"

    svetlana "NGGHHH!!!"

    hide anim
    show svetlana furnace_cowgirl b_cum
    anon "HNNGGG!!!" with flash
    show xray_front_top as xray:
        anchor (.5, .5)
        pos (250 + 358, 250 + 168)
        rotate -110
        rotate_pad False
        xzoom -1
        zoom .68
    with {'master': fastdissolve}
    pause
    hide xray
    show svetlana b_insert o_pullout
    show anon svet_furnace_cowgirl
    with {'master': dissolve}
    svetlana "I feel it!" (show_native="Ya chuvstvuyu eto!")
    show svetlana b_base d_after o_after
    with {'master': dissolve}
    svetlana "What a torrent!" (show_native="Kakoy torrent!")
    anon "Haah... Haah..."

    pause
    anon "... Yesus Kristus."

    svetlana "Haah... Haah..."

    anon "Itu sangat intens!"

    svetlana "Ya."


    if variant == 'repeat':
        return

    svetlana "Sudah lama sekali sejak seorang pria membuatku cum jadi..."

    anon "Oh?"

    svetlana "... Aku butuh waktu sebentar."

    anon "Ya, tentu saja!"

    anon "T-luangkan waktumu."

    return


label scene_svetlana_furnace_cowgirl.stage:
    scene location_warehouse_furnace_convey_side_any
    show svetlana furnace_cowgirl
    show anon svet_furnace_cowgirl
    return


label scene_svetlana_furnace_cowgirl.insert:
    show svetlana furnace_cowgirl b_insert
    show anon svet_furnace_cowgirl
    return


label scene_svetlana_furnace_cowgirl.animate:
    hide anon
    hide svetlana
    show svetlana_furnace_cowgirl_body_b_anim as anim
    return


label scene_svetlana_furnace_cowgirl.loop:
    call screen scene_svetlana_furnace_cowgirl_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_svetlana_furnace_cowgirl.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_svetlana_furnace_cowgirl.loop


label scene_svetlana_furnace_cowgirl.dialogue(opt, rng=-1):

    if opt == 1:
        anon "Haaaa!!!"


        if variant == 'first':
            svetlana "Are all Americans this malleable?" (show_native="Vse li Amerikantsy takiye podatlivyye?")
        else:


            svetlana "Do all Americans make such silly noises during sex?" (show_native="Neuzheli vse amerikantsy izdayut takiye glupyye zvuki vo vremya seksa?")


        anon "Hmm?"

        anon "Saya tidak tahu apa yang Anda katakan-"

        svetlana "Diam!"

        anon "{i}*Gulp*{/i} Y-iya, Bu."


    elif opt == 2:
        svetlana "Anda suka ini?"

        anon "..."

        if rng < .15:
            svetlana "Anda suka saat saya menunggangi ayam Amerika Anda yang besar dan gemuk?"

            anon "A-apa kamu ingin aku menjawabnya, atau-"


        svetlana "Katakan!!"

        anon "Ah, ya!"


        if rng < .15:
            anon "Ya, aku suka saat kamu menunggangi ayam Amerikaku yang besar dan gemuk!!"


    elif opt == 3:
        svetlana "{b}Nadya{/b} is a fortunate woman..." (show_native="{b}Nadya{/b} schastlivaya zhenshchina...")
        svetlana "... To have claimed such a man." (show_native="... Zavoyevat' takogo muzhchinu.")

    elif opt == 4:
        anon "Ya Tuhan... Kamu seksi sekali!"


        if rng < .4:
            svetlana "Kamu suka vaginaku?"

            anon "Ya, saya menyukainya!!"


    elif opt == 5:
        if rng < .3:
            svetlana "Mmm, you're going to make me cum!" (show_native="Mmm, ty zastavish' menya konchit'!")
            anon "Apa?"


        svetlana "Aku akan segera keluar!"

        anon "Ngh, ya... aku juga!"


    elif opt == 6:
        svetlana "So fucking good!" (show_native="Tak chertovski khorosho!")
        svetlana "Ahhh!"


    return


label scene_svetlana_furnace_cowgirl.switch:
    anon "Haah... Haah..."

    anon "Aku kehabisan asap di sini."

    svetlana "Hmm?"

    call scene_svetlana_furnace_doggy.stage
    with {'master': dissolve}
    anon "Bisakah Anda kembali ke puncak untuk sementara waktu?"

    svetlana "Ya."

    svetlana "saya akan berkendara."

    anon "Terima kasih."


    call scene_svetlana_furnace_cowgirl.stage
    with fade
    anon "Tubuhmu luar biasa!"

    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana @ -m_talk "Mmmm."

    anon "Ya Tuhan!"

    call scene_svetlana_furnace_cowgirl.animate
    with {'master': dissolve}
    jump scene_svetlana_furnace_cowgirl.resume


label scene_svetlana_furnace_cowgirl.first:
    jump scene_svetlana_furnace_cowgirl


label scene_svetlana_furnace_cowgirl.repeat:
    $ M_svetlana.set('sex speed', 1 / 8.)
    $ renpy.dynamic(variant='repeat')

    call scene_svetlana_furnace_cowgirl.stage
    with fade
    anon "Ya Tuhan..."

    anon "... Tubuhmu luar biasa!"

    svetlana "Ya."

    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana "Mmm, your penis is the best." (show_native="Mmm, tvoy penis samyy luchshiy.")
    anon "Ya Tuhan, ya Tuhan, ya Tuhan!"

    call scene_svetlana_furnace_cowgirl.animate
    with {'master': dissolve}
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (1)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (2)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (3)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (4)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (5)
    pause
    call scene_svetlana_furnace_cowgirl.dialogue (6)
    pause
    jump scene_svetlana_furnace_cowgirl.resume


label scene_svetlana_furnace_cowgirl.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['svetlana']['variants']['02_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_warehouse_furnace) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_svetlana_furnace_cowgirl.first

            "Ulangi" if 'repeat' in variants:
                jump scene_svetlana_furnace_cowgirl.repeat

    jump expression 'scene_svetlana_furnace_cowgirl.{}'.format(next(iter(variants)))


screen scene_svetlana_furnace_cowgirl_controls():
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
