screen basketball_court():
    add player.location.background

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (523,358)
            idle "objects/object_basketball_01.png"
            hover HoverImage("objects/object_basketball_01.png")
            action Hide("basketball_court"), Jump("basketball_minigame_prepare_but_with_a_background_this_time")

    if player.location.is_here(M_becca):
        imagebutton:
            focus_mask True
            pos (681,431)
            idle "objects/character_becca_01.png"
            hover HoverImage("objects/character_becca_01.png")
            action TalkTo(M_missy)


    if player.location.is_here(M_dexter):
        imagebutton:
            focus_mask True
            pos (729,414)
            idle "objects/character_dexter_01.png"
            hover HoverImage("objects/character_dexter_01.png")
            action TalkTo(M_dexter)

        if M_ross.is_state(S_ross_find_magazines) and not M_ross.get("magazine dexter") and not game.timer.is_dark():
            imagebutton:
                focus_mask True
                pos (544,609)
                idle "objects/object_mags_01.png"
                hover HoverImage("objects/object_mags_01.png")
                action Hide("basketball_court"), Jump("basket_ball_court_take_magazines")

    use mods_screens_hook("basketball_court")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
