screen living_room():
    if M_debbie.get_state() in [S_debbie_romance_movie, S_debbie_romance_movie_two] or (M_debbie.is_set("movie night") and game.timer.is_dark()):
        if Game.is_christmas():
            add "backgrounds/location_home_livingroom_christmas_night_debbie.jpg"
        else:
            add "backgrounds/location_home_livingroom_night_debbie.jpg"
    else:
        add player.location.background

    if L_home_livingroom.is_here(M_diane) and not M_debbie.is_state(S_debbie_romance_movie, S_debbie_romance_movie_two, S_debbie_spy) and not M_debbie.get("movie night"):
        if M_diane.pregnancy.gave_birth:
            imagebutton:
                focus_mask True
                pos (653,386)
                idle M_diane.get_button_path('casual', use_day_timer=True, use_baby=True)
                hover HoverImage(M_diane.get_button_path('casual', use_day_timer=True, use_baby=True))
                action TalkTo(M_diane)
        else:
            imagebutton:
                focus_mask True
                pos (331,480)
                idle "objects/object_couch_02.png"
                hover HoverImage("objects/object_couch_02.png")
                action TalkTo(M_diane)

    imagebutton:
        focus_mask True
        pos (1002,251)
        idle game.timer.image("objects/object_door_42{}.png")
        hover HoverImage(game.timer.image("objects/object_door_42{}.png"))
        action MoveTo(L_home_entrance)

    imagebutton:
        focus_mask True
        pos (809,311)
        idle game.timer.image("objects/object_door_43{}.png")
        hover HoverImage(game.timer.image("objects/object_door_43{}.png"))
        action MoveTo(L_home_basement)

    imagebutton:
        focus_mask True
        pos (108,312)
        idle game.timer.image("objects/object_door_44{}.png")
        hover HoverImage(game.timer.image("objects/object_door_44{}.png"))
        action MoveTo(L_home_mombedroom)

    imagebutton:
        focus_mask True
        pos (412,331)
        idle game.timer.image("objects/object_tv_01{}.png")
        hover HoverImage(game.timer.image("objects/object_tv_01{}.png"))
        if M_diane.is_state(S_diane_get_dirty_with_debbie):
            action MoveTo(L_home)
        else:
            action Hide('living_room'), Jump('television')

    use mods_screens_hook("living_room")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
