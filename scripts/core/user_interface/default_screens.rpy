screen gui_tooltip():
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

screen button(Image, Label):
    imagebutton:
        align (0.5,0.97)
        idle str(Image) + ".png"
        hover HoverImage(str(Image)+".png")
        action Hide("button"), Jump(Label)

screen sex_anim_buttons():
    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover HoverImage("buttons/anim_02.png")
        else:
            idle "buttons/anim_01.png"
            hover HoverImage("buttons/anim_01.png")
        action [
            If(
                anim_toggle,
                [SetVariable("anim_toggle", False),SetVariable("animated", False)] ,
                SetVariable("anim_toggle", True)
            ),
            Return()
        ]

screen sex_xray_anim_buttons():
    imagebutton:
        focus_mask True
        pos (10,600)
        if anim_toggle:
            idle "buttons/anim_02.png"
            hover HoverImage("buttons/anim_02.png")
        else:
            idle "buttons/anim_01.png"
            hover HoverImage("buttons/anim_01.png")
        action [
            If(
                anim_toggle,
                [SetVariable("anim_toggle", False),SetVariable("animated", False)],
                SetVariable("anim_toggle", True)
            ),
            Return()
        ]

    imagebutton:
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover HoverImage("buttons/anim_03.png")
        else:
            idle "buttons/anim_04.png"
            hover HoverImage("buttons/anim_04.png")
        action [
            If(
                xray,
                SetVariable("xray", False),
                SetVariable("xray", True)
            )
        ]

label deb_name_input_label(ret=False):
    call screen popup_rename('debbie', deb_name)
    python:
        deb_name = _return
        config.replay_scope['deb_name'] = deb_name
        persistent.deb_name = deb_name
        if not ret:
            game.main()
    return

label jen_name_input_label(ret=False):
    call screen popup_rename('jenny', jen_name)
    python:
        jen_name = _return
        config.replay_scope['jen_name'] = jen_name
        persistent.jen_name = jen_name
        if not ret:
            game.main()
    return

label cat_name_input_label(ret=False):
    if cat_name == 'Cat' and not M_player.get("pet cat"):
        $ cat_name = 'Pussywillow'
    call screen popup_rename('cat', cat_name)
    python:
        cat_name = _return
        config.replay_scope['cat_name'] = cat_name
        persistent.cat_name = cat_name
        M_player.set("pet cat", True)
        if not ret:
            game.main()
    return

screen talk_to_option(machine):
    imagebutton:
        idle "ground.png"
        action Hide("talk_to_option")

    imagebutton:
        focus_mask True
        pos (350,600)
        idle BoxButton('Talk to {}.'.format(machine._name.capitalize()), image='boxes_icons/talk.png')
        hover HoverBoxButton('Talk to {}.'.format(machine._name.capitalize()), image='boxes_icons/talk.png')
        action Hide("talk_to_option"), TalkTo(machine)

screen talk_to(machine, position, button_id=1, use_day_timer=False, use_old_path=False):
    if player.location.is_here(machine):
        imagebutton:
            focus_mask True
            pos position
            idle machine.get_button_path(button_id, use_day_timer, use_old_path)
            hover HoverImage(machine.get_button_path(button_id, use_day_timer, use_old_path))
            action Show("talk_to_option", machine)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
