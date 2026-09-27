screen basement():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (0,308)
        idle game.timer.image("objects/object_stairs_03{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_03{}.png"))
        action MoveTo(L_home_livingroom)

    if M_debbie.is_state(S_debbie_close_valve):
        imagebutton:
            focus_mask True
            pos (394,512)
            idle game.timer.image("objects/object_pipe_01{}.png")
            hover HoverImage(game.timer.image("objects/object_pipe_01{}.png"))
            action Hide("basement"), Jump("broken_pipe")

    if player.location.is_here(M_debbie):
        imagebutton:
            focus_mask True
            pos (486,320)
            idle "images/objects/character_debbie_06.png"
            hover HoverImage("images/objects/character_debbie_06.png")
            action TalkTo(M_debbie)
    else:
        if player.has_picked_up_item("debbie_panties"):
            imagebutton:
                focus_mask True
                pos (439,552)
                idle game.timer.image("objects/object_laundry_03{}.png")
                action NullAction()
        else:
            imagebutton:
                focus_mask True
                pos (439,552)
                idle game.timer.image("objects/object_laundry_03{}.png")
                hover HoverImage(game.timer.image("objects/object_laundry_03{}.png"))
                action Hide("basement"), Show("basement_basket")

    use mods_screens_hook("basement")

screen basement_basket():
    add game.timer.image("backgrounds/location_home_debbiebedroom_basket{}_closeup.jpg")

    if not player.has_picked_up_item("debbie_panties"):
        imagebutton:
            focus_mask True
            pos (412,269)
            idle game.timer.image("objects/object_panties_02b{}.png")
            hover HoverImage(game.timer.image("objects/object_panties_02b{}.png"))
            action Hide("basement_basket"), Jump("basement_basket_debbie_panties")
    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_home_basement)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
