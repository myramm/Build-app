label scene_svetlana_furnace_doggy:

    return


label scene_svetlana_furnace_doggy.stage:
    scene location_warehouse_furnace_convey_top_any
    show svetlana furnace_doggy
    return


label scene_svetlana_furnace_doggy.animate:
    hide svetlana
    show svetlana_furnace_doggy_body_b_anim as anim
    return


label scene_svetlana_furnace_doggy.loop:
    call screen scene_svetlana_furnace_doggy_controls

    if _return:
        return _return

    python hide:
        blocks = 5
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_svetlana_furnace_doggy.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_svetlana_furnace_doggy.loop


label scene_svetlana_furnace_doggy.dialogue(opt, rng=-1):

    if opt == 1:
        svetlana "Ngh!"


    elif opt == 2:
        anon "Anda suka itu?"

        svetlana "Ya!"


        if rng < .4:
            anon "Kamu suka saat aku memukul vaginamu dengan penisku yang besar dan gemuk?!"

            svetlana "Ya, pukul!"


        if rng < .5:
            anon "Ini luar biasa!"


    elif opt == 3:
        svetlana "Hancurkan vaginaku, {b}[firstname]{/b}!"


        if rng < .6:
            anon "Oh, ya... aku akan merusaknya!"


        svetlana "Fuck me harder!" (show_native="Trakhni menya sil'neye!")

    elif opt == 4:
        anon "Omong-omong, pantatmu terlihat luar biasa dari sudut ini..."

        svetlana "Kurangi bicara, perbanyak bicara!"

        anon "Ya, Bu."


    elif opt == 5:
        svetlana "Ahhh!"


        if rng < .2:
            svetlana "I'm so jealous that {b}Nadya{/b} gets you whenever she desires!" (show_native="Ya tak zaviduyu, chto{b}Nadya{/b} poluchayet tebya, kogda khochet!")
            svetlana "This penis is truly magical!" (show_native="Etot penis deystvitel'no volshebnyy!")

        anon "Aku semakin dekat!"

        svetlana "Da, aku juga akan segera cum!"


    return


label scene_svetlana_furnace_doggy.switch:
    anon "Hei, bolehkah aku mengemudi sebentar?"

    hide anim
    call scene_svetlana_furnace_cowgirl.insert
    with {'master': dissolve}
    svetlana @ -m_talk "Hmm?"

    anon "Mungkin kita bisa mencoba gaya doggy atau apalah?"

    call scene_svetlana_furnace_cowgirl.stage
    with {'master': dissolve}
    svetlana "Kamu ingin meniduriku seperti anjing?"

    anon "Maksudku... doggie style, itu posisi..."

    anon "Kita tidak perlu-"

    svetlana "Saya ingin ini..."

    anon "Oh."

    anon "Persetan ya!"


    $ M_svetlana.set('sex speed', 1 / 8.)

    call scene_svetlana_furnace_doggy.stage
    with fade
    anon "Anda siap?"

    svetlana "Cepat dan persetan denganku, dasar pria kecil yang konyol!"

    anon "!!!"
    anon "Baiklah."

    call scene_svetlana_furnace_doggy.animate
    with {'master': dissolve}
    call scene_svetlana_furnace_doggy.dialogue (1)
    pause
    call scene_svetlana_furnace_doggy.dialogue (2)
    pause
    call scene_svetlana_furnace_doggy.dialogue (3)
    pause
    call scene_svetlana_furnace_doggy.dialogue (4)
    pause
    call scene_svetlana_furnace_doggy.dialogue (5)
    pause

    call scene_svetlana_furnace_doggy.loop
    jump scene_svetlana_furnace_cowgirl.switch


screen scene_svetlana_furnace_doggy_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Switch') action Return()

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
