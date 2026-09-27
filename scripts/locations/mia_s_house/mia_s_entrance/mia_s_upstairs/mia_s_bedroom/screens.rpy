screen mias_bedroom():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (245,474)
        idle game.timer.image("objects/object_laundry_02{}.png")
        hover HoverImage(game.timer.image("objects/object_laundry_02{}.png"))
        action Hide("mias_bedroom"), Show("mia_bedroom_laundry_basket")

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (300,300)
            idle "objects/character_mia_01c.png"
            hover HoverImage("objects/character_mia_01c.png")
            action TalkTo(M_mia)

    imagebutton:
        focus_mask True
        pos (3,492)
        idle "objects/object_teddy_01.png"
        hover HoverImage("objects/object_teddy_01.png")
        action Hide("mias_bedroom"), Jump("mia_bedroom_teddy")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_miahouse_upstairs)

    use mods_screens_hook("mias_bedroom")

screen mia_bedroom_laundry_basket():
    add game.timer.image("backgrounds/location_mia_bedroom_basket{}_closeup.jpg")

    if not player.has_picked_up_item("mia_panties"):
        imagebutton:
            focus_mask True
            pos (395,191)
            idle game.timer.image("objects/object_panties_04{}.png")
            hover HoverImage(game.timer.image("objects/object_panties_04{}.png"))
            action Hide("mia_bedroom_laundry_basket"), Jump("mia_bedroom_panties")

    imagebutton:
        focus_mask True
        align 0.5,0.95
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("mia_bedroom_laundry_basket"), Jump("mias_bedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
