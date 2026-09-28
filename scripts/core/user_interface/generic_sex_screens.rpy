screen machine_sex_options(machine):
    if machine.get("sex speed") < .175:
        imagebutton:
            focus_mask True
            pos (250,615)
            idle "sexb_slower_n"
            hover "sexb_slower_h"
            action Hide("machine_sex_options"), Function(machine.set, "sex speed", machine.get("sex speed") + 0.05)

    if machine.get("sex speed") > .076:
        imagebutton:
            focus_mask True
            pos (450,615)
            idle "sexb_faster_n"
            hover "sexb_faster_h"
            action Hide("machine_sex_options"), Function(machine.set, "sex speed", machine.get("sex speed") - 0.05)

screen xray_scr():
    imagebutton:
        focus_mask True
        pos (940,600)
        if xray:
            idle "buttons/anim_03.png"
            hover HoverImage("buttons/anim_03.png")
        else:
            idle "buttons/anim_04.png"
            hover HoverImage("buttons/anim_04.png")
        action If(xray, SetVariable("xray", False), SetVariable("xray", True))

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

screen sex_screen(machine, loop_label, buttons=[], n_frames=8, **kwargs):
    $ speed_bounds = kwargs.get("speed_bounds", None)
    $ is_init = kwargs.get("is_init", False)
    $ n_increments = kwargs.get("n_increments", 2)
    if speed_bounds is None:
        $ slow, fast = get_sex_speeds(n_frames)
    else:
        $ slow, fast = speed_bounds
    if is_init:
        $ machine.set('sex speed', get_average_sex_speed(n_frames, n_increments))
    $ speed_increment = get_sex_speed_increment(n_frames, n_increments)
    if machine.get("sex speed") < fast:
        imagebutton:
            focus_mask True
            xpos 180
            ypos 735
            idle "sexb_slower_n"
            hover "sexb_slower_h"
            action Hide("sex_screen"), Function(machine.set, "sex speed", machine.get("sex speed") + speed_increment), Jump(loop_label)

    imagebutton:
        focus_mask True
        xpos 380
        ypos 735
        idle "sexb_keepgoing_n"
        hover "sexb_keepgoing_h"
        action Hide("sex_screen"), Jump(loop_label)

    if machine.get("sex speed") > slow:
        imagebutton:
            focus_mask True
            xpos 580
            ypos 735
            idle "sexb_faster_n"
            hover "sexb_faster_h"
            action Hide("sex_screen"), Function(machine.set, "sex speed", machine.get("sex speed") - speed_increment), Jump(loop_label)

    hbox:
        spacing -100
        align 0.5, 0.96
        for btn in buttons:
            $ btn_name, btn_action = btn
            imagebutton:
                focus_mask True
                idle "sexb_" + btn_name + "_n"
                hover "sexb_" + btn_name + "_h"
                if isinstance(btn_action, Jump):
                    action Hide("sex_screen"), btn_action
                else:
                    action btn_action
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
