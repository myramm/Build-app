screen helens_bedroom():
    if M_helen.is_state(S_helen_master_servant_fun, S_helen_end) and player.location.is_here(M_helen):
        add 'mia_house_helen_window0'
    else:
        add player.location.background

    if M_mia.is_state(S_mia_midnight_help):
        imagebutton:
            focus_mask True
            pos (864,436)
            idle "objects/object_statue_01.png"
            hover HoverImage("objects/object_statue_01.png")
            action Hide("helens_bedroom"), Jump("helens_mary_statue")

    if player.location.is_here(M_helen):
        imagebutton:
            focus_mask True
            if not M_mia.is_set('helen button change'):
                pos (170,400)
                if M_helen.is_state(S_helen_master_servant_fun, S_helen_end):
                    idle "objects/character_helen_02.png"
                    hover HoverImage("objects/character_helen_02.png")
                else:
                    idle game.timer.image("objects/character_helen_01{}.png")
                    hover HoverImage(game.timer.image("objects/character_helen_01{}.png"))
            else:
                pos (340,470)
                idle game.timer.image("objects/character_helen_03{}.png")
                hover HoverImage(game.timer.image("objects/character_helen_03{}.png"))
            action TalkTo(M_helen)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_miahouse_upstairs)

    use mods_screens_hook("helens_bedroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
