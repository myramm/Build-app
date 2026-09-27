screen park():
    add L_park.background

    if player.location.is_here(M_anna):
        imagebutton:
            focus_mask True
            pos (710,400)
            idle "objects/character_anna_01.png"
            hover HoverImage("objects/character_anna_01.png")
            action Hide("park"), Jump("anna_button_dialogue")

    imagebutton:
        focus_mask True
        pos (318,377)
        idle game.timer.image("objects/object_fountain_01{}.png")
        hover HoverImage(game.timer.image("objects/object_fountain_01{}.png"))
        action MoveTo(L_park_fountain)

    imagebutton:
        focus_mask True
        pos (104,464)
        idle game.timer.image("objects/object_bench_02{}.png")
        hover HoverImage(game.timer.image("objects/object_bench_02{}.png"))
        action ShowPopup('alpha')

    if M_larry.finished_state(S_larry_msg_given) or M_mia.finished_state(S_mia_convince_harold):
        imagebutton:
            focus_mask True
            pos (261,291)
            idle game.timer.image("objects/object_tree_01{}.png")
            hover HoverImage(game.timer.image("objects/object_tree_01{}.png"))
            action Hide("park"), Jump("park_bushes_dialogue")

    if M_roxxy.is_state(S_roxxy_meeting_buyer) and game.timer.is_evening():
        pass

    elif M_eve.is_state(S_eve_pranking_douches) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos 162, 392
            idle "characters/eve/buttons/character_eve_06.png"
            hover HoverImage("characters/eve/buttons/character_eve_06.png")
            action TalkTo(M_eve)

    elif L_park.is_here(M_eve):
        imagebutton:
            focus_mask True
            pos 297, 473
            idle M_eve.get_button_path(3, use_day_timer=True)
            hover HoverImage(M_eve.get_button_path(3, use_day_timer=True))
            action TalkTo(M_eve)

    if M_roxxy.is_state(S_roxxy_meeting_buyer) and game.timer.is_evening():
        pass

    elif M_eve.is_state(S_eve_pranking_douches, S_eve_tuuku_with_douches) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos 727, 592
            idle "objects/object_backpack_02_evening.png"
            hover HoverImage("objects/object_backpack_02_evening.png")
            action Hide("park"), Jump("park_eve_pranking_douches_backpack")

    if M_roxxy.is_state(S_roxxy_meeting_buyer) and game.timer.is_evening():
        pass

    elif M_eve.is_state(S_eve_tuuku_with_douches) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos (735, 390)
            idle M_tuuku.get_button_path(2)
            hover HoverImage(M_tuuku.get_button_path(2))
            action TalkTo(M_park_douches)

    elif L_park.is_here(M_park_douches):
        imagebutton:
            focus_mask True
            pos (724,407)
            idle game.timer.image("objects/object_bench_03{}.png")
            hover HoverImage(game.timer.image("objects/object_bench_03{}.png"))
            action TalkTo(M_park_douches)

    if game.timer.is_afternoon() and M_okita.is_state(S_okita_take_picture_judith) and player.location.is_here(M_judith):
        imagebutton:
            focus_mask True
            pos (104,430)
            idle game.timer.image("objects/character_judith_03{}.png")
            hover HoverImage(game.timer.image("objects/character_judith_03{}.png"))
            action Hide("park"), Jump("park_take_picture_judith")

    if M_ross.is_state(S_ross_find_eve_backpack) and not player.has_picked_up_item("eve_backpack") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (883,499)
            idle "objects/object_backpack_01.png"
            hover HoverImage("objects/object_backpack_01.png")
            action Hide("park"), Jump("backpack_pickup_dialogue")

    if M_roxxy.is_state(S_roxxy_meeting_buyer) and game.timer.is_evening():
        imagebutton:
            focus_mask True
            pos (104,389)
            idle "objects/character_pilly_01_evening.png"
            hover HoverImage("objects/character_pilly_01_evening.png")
            action Hide("park"), Jump("park_pilly_button")

    use mods_screens_hook("park")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
