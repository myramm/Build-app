label sploosh_button_dialogue:
    scene expression game.timer.image("backgrounds/location_pier_boxes{}.jpg")
    show sploosh 1 at right
    show anon f_worried_surprised with dissolve
    anon @ f_shy "Halo?"

    sploosh "{i}*ZZZzzzz*{/i}..."

    anon f_thinking a_thinking @ -m_talk "(Hmm... Dia pasti sedang tidur...)"


    menu:
        "Bangun {b}Laksamana Sploosh{/b}.":
            anon f_shy -a_thinking "Eh... Permisi?"

            $ sploosh.wake()
            show sploosh 2
            show anon f_surprised_teeth
            sploosh "[sploosh.message]" with hpunch
            anon "!!!"
            show anon f_surprised
            sploosh "[sploosh.author]"

            show sploosh 1 with dissolve
            sploosh "{i}*ZZZzzzz*{/i}..."

            anon @ -m_talk "(Bajak laut yang aneh...)"

        "Pergi.":

            anon -f_thinking -a_thinking @ -m_talk "(Sebaiknya aku tidak mengganggunya...)"

            sploosh "{i}*ZZZzzzz*{/i}..."


    hide anon with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
