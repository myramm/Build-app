label church_graveyard_crypt_dialogue:
    scene
    show screen church_graveyard_crypt()
    anon "( This is a creepy looking door... )"

    anon "( ... I wonder where it leads? )"


    call screen empty()
    return


label church_graveyard_crypt_dialogue.fullmoon:
    scene
    show screen church_graveyard_crypt()
    anon "( Hmm, do I really wanna go down there again? )"

    anon "( {b}Grace{/b} said {b}Odette{/b} is just pretending for some fetish she has. )"

    anon "( So there's nothing to worry about... )"

    anon "( ... Right? )"

    anon "( Man, my heart is racing... )"


    call screen empty()

    if _return:
        return

    anon "{b}Odette{/b}?"

    anon "Are you down there?"

    "Hehehe!"

    anon "( Oh man, not this again... )"


    call screen empty()

    if _return:
        return

    anon "( Nothing ventured, nothing gained. )"

    anon "( Here we go! )"

    return 'enter'


label church_graveyard_grave_dialogue:
    scene
    show screen church_graveyard_grave()
    pause
    return


label church_graveyard_grave_dialogue.dark:
    scene expression background(360, 448, 4.) as stage
    show anon a_sides f_worried_low at flip with dissolve
    pause
    anon @ -m_talk "( Dad loved the sun. I'll visit him when it's beaming down. )"

    pause
    hide anon with dissolve
    return


label church_graveyard_grave_dialogue.wait:
    scene expression background(360, 448, 4.) as stage
    show anon a_sides f_worried_low at flip with dissolve
    pause
    anon "H-"

    pause
    anon "I ..."

    show anon f_sad_down
    pause
    anon @ -m_talk "( I can't do this right now. )"

    anon @ -m_talk "( I'm not ready. )"

    show anon a_cover_boner3 f_disgusted_wince with dissolve:
        unflip
        xoffset 550
    anon "I'll come back soon, Dad, I promise..."

    hide anon with dissolve
    return


screen church_graveyard_grave():
    layer 'master'
    sensitive renpy.get_mode() == 'screen'

    style_prefix 'grave'

    add 'backgrounds/location_church_graveyard_tombstone02.jpg'

    vbox:
        at Transform(alpha=.8, zoom=.5)
        text _('IN LOVING MEMORY OF') color '7f7f87ee' size 50
        null height 50
        text 'FRANK CUMMINGS' color '64646aee' size 85
        text '1969 - [year]' color '6f6f77ee' size 70
        null height 50
        text _('BELOVED PARTNER,')
        text _('FATHER, AND FRIEND')
        null height 40
        text _('TAKEN TOO SOON')

    if renpy.get_mode() == 'screen':
        fixed:
            textbutton 'F':
                at grave_pulse
                action Return()
                keysym 'f'


transform grave_pulse:
    alpha 0.
    subpixel True
    block:
        ease 1.5 alpha 1. zoom 1.05
        ease 1.5 alpha .8 zoom 1.
        repeat


style grave_button:
    anchor (.5, .5)
    pos (560, .8375)

style grave_button_text:
    bold True
    color 'f9d019'
    size 30
    outlines ((absolute(2), '0005', absolute(0), absolute(0)),)

style grave_vbox:
    anchor (.5, 0.)
    pos (560, 275)
    xmaximum 940

style grave_text:
    color '74747aee'
    font 'fonts/nocturneserif.otf'
    kerning 4
    outlines ((3, '1124', 2, -2),
              (2, '1122', 1, -1),
              (4, 'fff1', -4, 4),
              (2, 'eee2', -2, 2),)
    size 65
    text_align .5
    xalign .5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
