screen minigame_combat(enemy, anon, flip=False):
    layer 'master'
    style_prefix 'combat'

    transform:
        if flip:
            xzoom -1

        fixed:
            xpos .75
            xsize config.screen_width // 2 - 40
            use minigame_combat_hp(enemy)

        fixed:
            xpos .25
            xsize config.screen_width // 2 - 40
            use minigame_combat_hp(anon, flip=True)


screen minigame_combat_hint():
    layer 'master'

    label _('Complete the combo before time runs out!'):
        style_prefix 'help'


screen minigame_combat_hp(entity, flip=False):
    layer 'master'
    style_prefix 'combat'

    window:
        if flip:
            at Transform(xzoom=-1)

        grid entity.max 1:
            for i in xrange(0, entity.max):
                showif entity.max - i <= entity.hp:
                    add hitpoint(i, entity.hue)


style combat_fixed:
    fit_first True
    xanchor .5
    yalign .95

style combat_grid:
    spacing -10
    xfill True

style combat_window:
    background 'frame_skew'
    padding (10, 6)
    ysize 42


transform hitpoint(i, hue):
    Frame(im.MatrixColor('minigames/combat/hp.png',
                         im.matrix.brightness(i * -.1) *
                         im.matrix.contrast(i * -.1 + 1) *
                         im.matrix.hue(i * -24 + hue)), 15, 3)
    on show:
        alpha 1
    on hide:
        linear .2 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
