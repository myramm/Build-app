screen hospital_storage_cabinet():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (98,173)
        idle "objects/object_pharmacy_01.png"
        hover HoverImage("objects/object_pharmacy_01.png")
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos (486,207)
        idle "objects/object_pharmacy_02.png"
        hover HoverImage("objects/object_pharmacy_02.png")
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos (770,226)
        idle "objects/object_pharmacy_03.png"
        hover HoverImage("objects/object_pharmacy_03.png")
        action ShowPopup('alpha')

    if not player.has_item("birth_control_pills"):
        imagebutton:
            focus_mask True
            pos (148,469)
            idle "objects/object_pharmacy_04.png"
            hover HoverImage("objects/object_pharmacy_04.png")
            action (Function(player.get_item, "birth_control_pills"),
                    ShowPopup('give', 'birth_control_pills'),
                    Function(erik_contraceptive_pills_acquired))

    imagebutton:
        focus_mask True
        pos (596,466)
        idle "objects/object_pharmacy_06.png"
        hover HoverImage("objects/object_pharmacy_06.png")
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        pos (732,457)
        idle "objects/object_pharmacy_07.png"
        hover HoverImage("objects/object_pharmacy_07.png")
        action ShowPopup('alpha')

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_hospital_storageroom)

    use mods_screens_hook("hospital_storage_cabinet")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
