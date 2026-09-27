screen bedroom():
    add player.location.background

    if M_anon.finished_state(S_ano13_clue):
        imagebutton:
            focus_mask True
            pos 632, 350
            idle game.timer.image("objects/object_picture_03{}.png")
            hover HoverImage(game.timer.image("objects/object_picture_03{}.png"))
            action HideAll(), Jump("home_bedroom_picture3")

    imagebutton:
        focus_mask True
        pos (44,352)
        idle game.timer.image("objects/object_telescope_01{}.png")
        hover HoverImage(game.timer.image("objects/object_telescope_01{}.png"))
        if M_diane.is_state(S_diane_get_dirty_with_debbie):
            action MoveTo(L_home)
        else:
            action Hide("bedroom"), Jump("telescope")

    imagebutton:
        focus_mask True
        pos (225,187)
        idle game.timer.image("objects/object_door_01{}.png")
        hover HoverImage(game.timer.image("objects/object_door_01{}.png"))
        action MoveTo(L_home_hallway)

    imagebutton:
        focus_mask True
        pos (445,336)
        if M_debbie.get_state() == S_debbie_note:
            idle "objects/object_desk_01_note.png"
            hover HoverImage("objects/object_desk_01_note.png")

        elif M_player.get('pc_fixed'):
            idle game.timer.image("objects/object_desk_01{}.png")
            hover HoverImage(game.timer.image("objects/object_desk_01{}.png"))

        else:
            idle game.timer.image("objects/object_desk_broken_01{}.png")
            hover HoverImage(game.timer.image("objects/object_desk_broken_01{}.png"))

        if M_debbie.get_state() == S_debbie_note:
            action Hide("bedroom"), Jump("M6_note")
        elif M_diane.is_state(S_diane_get_dirty_with_debbie):
            action MoveTo(L_home)
        else:
            action If(M_player.get('pc_fixed'),
                      (Hide('bedroom'), Jump('anon_computer')),
                      Show("desk01_options"))

    if M_jenny.get("girlfriend_in_progress"):
        imagebutton:
            focus_mask True
            pos 581, 345
            idle "characters/jenny/buttons/character_jenny_girlfriend.png"
            hover HoverImage("characters/jenny/buttons/character_jenny_girlfriend.png")
            action Hide("bedroom"), Jump("jenny_button_girlfriend_experience_bedroom")

    elif game.timer.is_evening() and M_june.get('hang_time'):
        imagebutton:
            focus_mask True
            pos (670,350)
            idle "images/objects/character_june_02.png"
            hover HoverImage("images/objects/character_june_02.png")
            action Hide("bedroom"), Jump("june_bedroom_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (639,439)
            idle game.timer.image("objects/object_bed_01{}.png")
            hover HoverImage(game.timer.image("objects/object_bed_01{}.png"))
            action If(
                      M_mia.get_state() == S_mia_midnight_help,
                      [Hide("bedroom"), Jump("mia_midnight_text")],
                      Show("bed01_options")
            )

    if not player.has_picked_up_item("cookies"):
        imagebutton:
            focus_mask True
            pos (30,630)
            idle game.timer.image("objects/object_cookies_01{}.png")
            hover HoverImage(game.timer.image("objects/object_cookies_01{}.png"))
            action Function(player.get_item, "cookies"), Hide("bedroom"), Jump("cookies")

    if M_player.is_set("pet cat"):
        imagebutton:
            focus_mask True
            pos (350,670)
            idle game.timer.image("objects/character_cat_01{}.png")
            hover HoverImage(game.timer.image("objects/character_cat_01{}.png"))
            action Hide("bedroom"), Jump("pet_cat")

    if M_eve.finished_state(S_eve_voyeurism_follow_roof):
        imagebutton:
            focus_mask True
            pos 976, 216
            idle game.timer.image("objects/object_drawing_02{}.png")
            hover HoverImage(game.timer.image("objects/object_drawing_02{}.png"))
            action HideAll(), Jump("home_bedroom_drawing2")

    use mods_screens_hook("bedroom")

screen desk01_options():
    imagebutton:
        idle "ground.png"
        action [Hide("desk01_options")]

    imagebutton:
        idle "boxes/desk01_option_03.png"
        hover HoverImage("boxes/desk01_option_03.png")
        action (If(player.has_item("parts"),
                   (Function(M_player.set, 'pc_fixed', True),
                    Function(player.remove_item, "parts"),
                    ShowPopup('computer', True)),
                   ShowPopup('computer', False)),
                Hide("desk01_options"))
        xpos 350
        ypos 600

screen bed01_options():
    imagebutton:
        idle "ground.png"
        action Hide("bed01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/bed01_option_01.png"
        hover HoverImage("boxes/bed01_option_01.png")
        action If(M_debbie.is_state(S_debbie_debt_call),
                  [Hide("bed01_options"), Hide("bedroom"), Jump("bedroom_check_on_mom")],
                  If(game.sleep_lock,
                     [Hide("bed01_options"), Hide("bedroom"), Jump("bed_locked")],
                     [Hide("bed01_options"), Hide("bedroom"), Jump("sleeping")]
                  )
        )

    if player.has_jerk_available() and not game.timer.is_night():
        imagebutton:
            focus_mask True
            align (0.5,0.9)
            idle "boxes/bed01_option_02.png"
            hover HoverImage("boxes/bed01_option_02.png")
            action If(M_debbie.is_state(S_debbie_debt_call),
                      [Hide("bed01_options"), Hide("bedroom"), Jump("bedroom_check_on_mom")],
                      If(game.sleep_lock and not M_diane.is_state(S_diane_peeking_masturbate),
                         [Hide("bed01_options"), Hide("bedroom"), Jump("bed_locked")],
                         [Hide("bed01_options"), Hide("bedroom"), Jump("jerking_off_dialogue")]
                      )
            )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
