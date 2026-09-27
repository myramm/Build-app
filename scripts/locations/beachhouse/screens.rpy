screen beach_house_front():
    use mods_screens_hook("beach_house_front")

    add player.location.background

    if M_anon.finished_state(S_ano02_thug) and not player.has_picked_up_item("beach_house_key"):
        imagebutton:
            focus_mask True
            pos (134,498)
            idle game.timer.image("objects/object_sign_05{}.png")
            hover HoverImage(game.timer.image("objects/object_sign_05{}.png"))
            action ShowPopup('shop', 'beach_house_key',
                             buy_action=Function(A_home_sweet_home.unlock))

    imagebutton:
        focus_mask True
        pos (773,420)
        idle game.timer.image("objects/object_door_114{}.png")
        hover HoverImage(game.timer.image("objects/object_door_114{}.png"))
        action MoveTo(L_beachhouse_entrance)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
