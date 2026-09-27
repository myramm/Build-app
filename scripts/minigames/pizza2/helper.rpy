label minigame_pizza2(quota):
    $ renpy.dynamic(count=0)

    label minigame_pizza2.retry:
    show screen minigame_pizza2(quota=quota) with fade
    call screen empty()
    hide screen minigame_pizza2

    $ count += 1

    if count > 2:
        scene expression background(320, 664, 3.8, l=L_pizzeria_kitchen)
        with fade
        menu:
            "I can do this! {color=7ff7}[[Continue]{/color}":
                $ count = 0
            "Please let me skip it! {color=f77b}[[Cheat]{/color}":

                $ _return = Pizza2Minigame.PASS


    if _return:
        scene expression background(720, 400, 3.2, l=L_pizzeria_kitchen)
        show anon f_worried:
            xoffset 550
        with fade
        if _return == Pizza2Minigame.FAIL:
            anon @ -m_talk "( Crap, this is a mess... )"

            anon @ -m_talk "( I'd better start over before {b}Maria{/b} catches a glimpse of this. )"

        else:
            anon @ -m_talk "( I'll never keep up with orders at this rate. )"

            anon @ -m_talk "( I need to work faster before {b}Maria{/b} notices. )"

        jump minigame_pizza2.retry

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
