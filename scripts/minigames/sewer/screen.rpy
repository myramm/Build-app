screen minigame_sewer():
    layer 'master'

    default game = SewerMinigame()

    add 'minigames/sewer/sewer_scene.png'

    label _('Help [firstname] traverse the poop chute!'):
        style_prefix 'help'

    add game.sm:
        ypos 125

    hbox:
        align .5, .825
        spacing 50

        imagebutton:
            idle 'sewer_button_move_idle'
            insensitive 'sewer_button_move_dead'
            hover 'sewer_button_move_over'
            sensitive game.phase == 'stop'
            action Function(game.move)

        imagebutton:
            idle 'sewer_button_push_idle'
            insensitive 'sewer_button_push_dead'
            hover 'sewer_button_push_over'
            sensitive game.phase == 'poop'
            action Function(game.push)

        imagebutton:
            idle 'sewer_button_puke_idle'
            insensitive 'sewer_button_puke_dead'
            hover 'sewer_button_puke_over'
            sensitive game.phase == 'sick'
            action Function(game.puke)

    if game.phase == 'outro':
        timer 1.5 action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
