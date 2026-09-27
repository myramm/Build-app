screen police_office():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (669,425)
        idle "objects/character_harold_01_empty.png"
        if M_mia.get_state() == S_mia_search_desk:
            alt "Harold's desk"

            hover HoverImage("objects/character_harold_01_empty.png")
            action Hide("police_office"), Jump("police_harolds_desk")

    if player.location.is_here(M_harold):
        imagebutton:
            focus_mask True
            pos (670,384)
            alt "Talk to harold"

            idle "objects/character_harold_01.png"
            hover HoverImage("objects/character_harold_01.png")
            action TalkTo(M_harold)

    if player.location.is_here(M_earl):
        imagebutton:
            focus_mask True
            pos (280,350)
            alt "Talk To Earl"

            idle "objects/character_earl_01.png"
            hover HoverImage("objects/character_earl_01.png")
            action TalkTo(M_earl)

    imagebutton:
        focus_mask True
        pos (350,700)
        alt "Exit Police Station Office"

        idle "boxes/auto_option_13.png"
        hover HoverImage("boxes/auto_option_13.png")
        action MoveTo(L_police_lobby)

    use mods_screens_hook("police_office")

screen harolds_desk():
    imagebutton:
        focus_mask True
        pos (896,628)
        alt "Desk Picture"

        idle PulseHoverImage("objects/object_picture_05.png", delay = 0.5)
        hover HoverImage("objects/object_picture_05.png")
        action Hide("harolds_desk"), Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
