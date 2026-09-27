screen backyard():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (544,365)
        idle game.timer.image("objects/object_door_65{}.png")
        hover HoverImage(game.timer.image("objects/object_door_65{}.png"))
        action MoveTo(L_home_diningroom)

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (52,537)
            idle "objects/object_chair_02.png"

            action NullAction()

    if player.location.is_here(M_debbie):
        imagebutton:
            focus_mask True
            pos (470,418)
            idle "objects/character_debbie_07.png"
            hover HoverImage("objects/character_debbie_07.png")
            action Hide("backyard"), Jump("mom_pool_dialogue")

    if player.location.is_here(M_jenny):
        imagebutton:
            focus_mask True
            pos (107, 455)
            idle "characters/jenny/buttons/character_jenny_04[M_jenny.pregnancy.to_string].png"
            hover HoverImage("characters/jenny/buttons/character_jenny_04{}.png".format(M_jenny.pregnancy.to_string))
            action TalkTo(M_jenny)

    use mods_screens_hook("backyard")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
