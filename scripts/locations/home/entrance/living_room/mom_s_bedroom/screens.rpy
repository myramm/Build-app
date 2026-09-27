screen master_bedroom():
    add player.location.background

    if L_home_mombedroom.is_here(M_diane):
        imagebutton:
            focus_mask True
            pos (532,405)
            idle "characters/diane/buttons/character_diane_nightgown_bed_duo.png"
            hover HoverImage("characters/diane/buttons/character_diane_nightgown_bed_duo.png")
            action Hide("master_bedroom"), Jump("diane_debbie_3way_dialogue")

    elif M_debbie.is_set("sex available") and L_home_mombedroom.is_here(M_debbie) and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (550,400)
            idle "objects/character_debbie_03.png"
            hover HoverImage("objects/character_debbie_03.png")
            action TalkTo(M_debbie)

    elif M_debbie.is_set("panties taken") or (game.timer.is_dark() and L_home_mombedroom.is_here(M_debbie) and (M_debbie.get("sex available") or M_debbie.is_state(S_debbie_sleepover) or not M_debbie.get("bed locked"))):
        imagebutton:
            focus_mask True
            pos (435,435)
            idle game.timer.image("objects/object_bed_03{}.png")
            hover HoverImage(game.timer.image("objects/object_bed_03{}.png"))
            action Hide("master_bedroom"), Jump("mom_bed")

    if M_debbie.is_state(S_debbie_fetch_laundry):
        imagebutton:
            focus_mask True
            pos (247,517)
            idle "objects/object_laundry_01.png"
            hover HoverImage("objects/object_laundry_01.png")
            action Hide("master_bedroom"), Jump("mom_room_laundry")

    imagebutton:
        focus_mask True
        pos (0,459)
        idle game.timer.image("objects/object_desk_07{}.png")
        hover HoverImage(game.timer.image("objects/object_desk_07{}.png"))
        action Show("desk07_options")

    if not M_debbie.is_set("panties taken"):
        imagebutton:
            focus_mask True
            align (0.5,0.97)
            idle "boxes/auto_option_12.png"
            hover HoverImage("boxes/auto_option_12.png")
            action MoveTo(L_home_livingroom)

    use mods_screens_hook("master_bedroom")

screen moms_drawer():
    add game.timer.image("backgrounds/location_home_debbiedrawer_day{}.jpg")

    if M_debbie.is_set("fetch lotion"):
        if not M_debbie.is_set("retrieved lotion"):
            imagebutton:
                focus_mask True
                pos (562,295)
                idle "objects/object_lotion_01.png"
                hover HoverImage("objects/object_lotion_01.png")
                action (Function(player.get_item, "lotion"),
                        ShowPopup('give', 'lotion'),
                        Function(M_debbie.set, "retrieved lotion", True))

    elif M_debbie.is_set("panties available") and not M_debbie.is_set("panties taken") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (-4,283)
            idle "objects/object_panties_02.png"
            hover HoverImage("objects/object_panties_02.png")
            action Hide("moms_drawer"), Jump("mom_drawer_panties")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("moms_drawer"), Jump("mom_bedroom_screen")

screen desk07_options():
    imagebutton:
        idle "ground.png"
        action Hide("desk07_options")

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/desk07_option_01.png"
        hover HoverImage("boxes/desk07_option_01.png")
        action Hide("desk07_options"), Hide("master_bedroom"), Jump("mom_drawer")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
