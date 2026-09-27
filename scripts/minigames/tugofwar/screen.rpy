screen minigame_tugofwar(str=5):
    layer 'master'

    default game = TugOfWarMinigame(str)

    add 'minigames/tugofwar/tugofwar_scene.png'

    label _('Click like your life depends on it!'):
        style_prefix 'help'

    fixed:
        at Transform(xzoom=-1)

        for arc in xrange(1, 6):
            if game.swing < arc:
                add 'minigames/tugofwar/tugofwar_arc[arc]_over.png'
            else:
                add 'minigames/tugofwar/tugofwar_arc[arc]_idle.png'

        add 'minigames/tugofwar/tugofwar_char[game.frame]_[game.twist].png'

    if renpy.get_mode() != 'screen':
        pass

    elif game.phase == 'intro':
        timer .5 action Function(game.start)

    elif game.phase == 'running':
        key 'dismiss' action Function(game.pull, 'left')
        timer .2 repeat True action Function(game.pull, 'right')

    elif game.phase == 'outro':
        timer .5 action Return(game.swing < 5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
