screen warehouse():
    use mods_screens_hook("warehouse")

    add L_warehouse.background

    imagebutton:
        focus_mask True
        pos 230, 427
        idle game.timer.image("objects/object_door_108{}.png")
        hover HoverImage(game.timer.image("objects/object_door_108{}.png"))
        action MoveTo(L_warehouse_depot)

    imagebutton:
        focus_mask True
        pos 822, 203
        idle game.timer.image("objects/object_bush_warehouse{}.png")
        hover HoverImage(game.timer.image("objects/object_bush_warehouse{}.png"))
        action MoveTo(L_warehouse_bushes)

    if M_anon.is_state(S_ano27_plan):
        imagebutton:
            focus_mask True
            pos 572, 576
            idle M_nadya.get_button_path('warehouse_pipe_night')
            hover HoverImage(game.timer.image(M_nadya.get_button_path('warehouse_pipe_night')))
            action TalkTo(M_nadya)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
