screen french_classroom():
    add player.location.background

    imagebutton:
        focus_mask True
        pos (384,276)
        idle game.timer.image("objects/object_door_07{}.png")
        hover HoverImage(game.timer.image("objects/object_door_07{}.png"))
        action Hide("french_classroom"), Play("audio", sfxDoor()), Jump(game.dialog_select("school_hall_dialogue"))

    if player.location.is_here(M_eve):
        imagebutton:
            focus_mask True
            pos (160,419)
            idle "characters/eve/buttons/character_eve_01.png"
            hover HoverImage("characters/eve/buttons/character_eve_01.png")
            action TalkTo(M_eve)

    if player.location.is_here(M_roxxy) and M_roxxy.give_space < game.timer._game_day:
        imagebutton:
            focus_mask True
            pos (886,351)
            idle "objects/character_roxxy_02.png"
            hover HoverImage("objects/character_roxxy_02.png")
            action TalkTo(M_roxxy)

    if player.location.is_here(M_bissette):
        imagebutton:
            focus_mask True
            pos (747,342)
            idle "objects/character_bissette_01.png"
            hover HoverImage("objects/character_bissette_01.png")
            action Hide("french_classroom"), Jump("bissette_button_dialogue")

    imagebutton:
        focus_mask True
        pos (0,280)
        idle game.timer.image("objects/object_map_02{}.png")
        hover HoverImage(game.timer.image("objects/object_map_02{}.png"))
        action Hide("french_classroom"), Jump("europe_map_dialogue")

    use mods_screens_hook("french_classroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
