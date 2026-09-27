screen minigame_pizza(level):
    style_prefix 'pizza'

    default game = PizzaMinigame(level)

    add game.sm
    add game.schedule

    label _('Deliver pizzas to customers by clicking on the matching pizza!'):
        style_prefix 'help'

    hbox:
        for pizza, state in game.status.items():
            if state is None:
                imagebutton:
                    idle 'pizza_whole_{:02d}_idle'.format(pizza)
                    hover 'pizza_whole_{:02d}_over'.format(pizza)
                    action Function(game.attempt, pizza)
            else:
                fixed:
                    add 'pizza_whole_{:02d}_idle'.format(pizza)
                    if state:
                        add 'pizza_mark_good' align (.5, .5)
                    else:
                        add 'pizza_mark_bad' align (.5, .5)


style pizza_fixed:
    fit_first True

style pizza_hbox:
    align (.95, .95)
    spacing 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
