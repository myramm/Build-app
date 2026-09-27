screen qte(level, combo, skill):
    style_prefix 'qte'

    default count = 0
    default seq = qte.seq(level + combo)
    default ttl = math.pow((skill + 3 - skill * .55) / level, 3) * level

    vbox:
        hbox:
            for k in seq[:count]:
                add 'minigames/qte/[k]_over.png' at truecenter
            for k in seq[count:]:
                add 'minigames/qte/[k]_idle.png' at truecenter

        frame:
            style_suffix 'timer'
            has bar
            style_suffix 'timer_bar'
            range 1
            if renpy.get_mode() == 'screen':
                value AnimatedValue(1, old_value=0, delay=ttl)
            else:
                value 0

    if renpy.get_mode() != 'screen':
        pass

    elif count < len(seq):
        for k in qte.keys:
            key k action Return(False)
        key seq[count] action SetScreenVariable('count', count + 1)
        timer ttl action Return(False)

    else:
        timer .5 action Return(True)


screen qte(level, combo, skill):
    style_prefix 'qte'
    variant 'touch'

    default count = 0
    default seq = qte.seq(level + combo)
    default ttl = math.pow((skill + 3 - skill * .55) / level, 3) * level * 1.55

    for i, k in enumerate(seq):
        showif i == count and renpy.get_mode() == 'screen':
            imagebutton:
                action SetScreenVariable('count', i + 1)
                at qte_cue
                pos qte.opts[k]
                idle 'minigames/qte/{}_idle.png'.format(k)
                selected_idle 'minigames/qte/{}_over.png'.format(k)

    frame:
        style_suffix 'timer'
        has bar
        style_suffix 'timer_bar'
        range 1
        if renpy.get_mode() == 'screen':
            value AnimatedValue(1, old_value=0, delay=ttl)
        else:
            value 0

    if renpy.get_mode() != 'screen':
        pass

    elif count < len(seq):
        timer ttl action Return(False)

    else:
        timer .5 action Return(True)


style qte_hbox:
    xalign .5

style qte_image_button:
    anchor (.5, .5)
    padding (175, 175)

style qte_timer:
    align (.5, .85)

style qte_timer_bar:
    right_bar '#fff9'
    xysize (450, 10)

style qte_vbox:
    align (.5, .85)
    spacing 5


transform qte_cue:
    alpha 0
    on appear:
        alpha 1
    on show:
        linear .1 alpha 1
    on hide:
        linear .1 alpha 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
