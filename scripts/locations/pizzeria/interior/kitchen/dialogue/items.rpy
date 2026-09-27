label pizzeria_kitchen_eotm_dialogue:
    scene
    show screen pizzeria_kitchen_eotm()
    pause
    hide screen pizzeria_kitchen_eotm
    return


screen pizzeria_kitchen_eotm():
    layer 'master'
    sensitive False

    default alpha = 4 - (game.timer._tod > 1 and game.timer._tod)
    default paper = 'fff{}'.format(alpha)
    default metal = 'ff7{}'.format(alpha)

    add game.timer.image('location_pizza_kitchen_closeup_plaque{}')

    text _('EMPLOYEE OF THE MONTH'):
        anchor .5, .5
        bold True
        color '234c'
        outlines ((1, paper, 1, 1),)
        pos 505, 58
        size 35

    frame:
        anchor .5, .5
        pos 496, 705
        has transform
        maxsize (270, 45)
        frame:
            minimum (270, 45)
            text '[firstname]':
                align .5, .5
                bold True
                color '0007'
                outlines ((1, metal, 1, 1),)
                xmaximum 400
                text_align .5
                size 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
