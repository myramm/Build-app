screen kitchen():
    if M_debbie.is_set("revealing") or (M_debbie.is_set("sleep together") and not M_debbie.is_set("revealing")):
        $ mom_idle = "objects/character_debbie_02.png"
        $ mom_hover = HoverImage("objects/character_debbie_02.png")
        $ mom_x = 420
        $ mom_y = 276

    else:
        $ mom_idle = "objects/character_debbie_01.png"
        $ mom_hover = HoverImage("objects/character_debbie_01.png")
        $ mom_x = 682
        $ mom_y = 197

    add player.location.background

    imagebutton:
        focus_mask True
        pos (41,97)
        idle game.timer.image("objects/object_door_20{}.png")
        hover HoverImage(game.timer.image("objects/object_door_20{}.png"))
        action MoveTo(L_home_diningroom)

    if player.location.is_here(M_debbie):
        if M_debbie.get_state() == S_debbie_dishes_help and M_debbie.is_set("chores"):
            imagebutton:
                focus_mask True
                pos (722,196)
                idle "images/objects/character_debbie_05.png"
                hover HoverImage("images/objects/character_debbie_05.png")
                action Hide("kitchen"), Jump("dishes_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (mom_x, mom_y)
                idle mom_idle
                hover mom_hover
                action TalkTo(M_debbie)

    if (M_diane.finished_state(S_diane_milk_production_increase) and game.timer.is_dark() and
        not M_diane.pregnancy.stage > 4 and
        (M_debbie.is_state(S_debbie_sleepover, S_debbie_romance_movie, S_debbie_romance_movie_two, S_debbie_spy) or M_jenny.is_state(S_jenny_catch_her_jilling) or M_debbie.get("movie night"))):
        imagebutton:
            focus_mask True
            pos 334, 278
            idle M_diane.get_button_path('nightgown_water', use_pregnancy=True)
            hover HoverImage(M_diane.get_button_path('nightgown_water', use_pregnancy=True))
            action TalkTo(M_diane)


    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_01.png"
        hover HoverImage("boxes/auto_option_01.png")
        action MoveTo(L_home_entrance)

    use mods_screens_hook("kitchen")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
