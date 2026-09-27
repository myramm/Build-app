screen erimom_private_pos1_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_private_yoga_pos1_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/johnson_01.png"
        hover HoverImage("buttons/johnson_01.png")
        action Jump("erimom_private_pos1_switch")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("erimom_private_pos1_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("erimom_private_pos1_faster_sex")
            xpos 450
            ypos 735

screen erimom_private_pos2_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_private_yoga_pos2_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Jump("erimom_private_pos2_cum")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("erimom_private_pos2_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("erimom_private_pos2_faster_sex")
            xpos 450
            ypos 735

screen mrsj_3some_pos1_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_3some_pos1_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/johnson_01.png"
        hover HoverImage("buttons/johnson_01.png")
        action Jump("mrsj_3some_pos1_switch")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .4:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("mrsj_3some_pos1_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .21:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("mrsj_3some_pos1_faster_sex")
            xpos 450
            ypos 735

screen mrsj_3some_pos2_sex_options():
    tag quick_menu

    imagebutton:
        focus_mask True
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Jump("mrsj_3some_pos2_repeat")
        xpos 250
        ypos 700

    imagebutton:
        focus_mask True
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Jump("mrsj_3some_pos2_cum")
        xpos 450
        ypos 700

    if M_mrsj.get('sex speed') < .3:
        imagebutton:
            focus_mask True
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Jump("mrsj_3some_pos2_slower_sex")
            xpos 250
            ypos 735

    if M_mrsj.get('sex speed') > .11:
        imagebutton:
            focus_mask True
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Jump("mrsj_3some_pos2_faster_sex")
            xpos 450
            ypos 735
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
