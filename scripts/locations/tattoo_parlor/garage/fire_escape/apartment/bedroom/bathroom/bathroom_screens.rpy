screen tattoo_parlor_bathroom():
    add L_tattooparlor_bathroom.background

    imagebutton:
        focus_mask True
        pos 857, 89
        idle game.timer.image("objects/object_door_146{}.png")
        hover HoverImage(game.timer.image("objects/object_door_146{}.png"))
        action MoveTo(L_tattooparlor_bedroom)

    if not player.has_picked_up_item("grace_panties"):
        imagebutton:
            focus_mask True
            pos 711, 583
            idle game.timer.image("objects/object_panties_05.png")
            hover HoverImage(game.timer.image("objects/object_panties_05.png"))
            action HideAll(), Jump("tattoo_parlor_bathroom_pantie_collection")

    if L_tattooparlor_bathroom.is_here(M_eve):
        imagebutton:
            action TalkTo(M_eve)
            focus_mask True
            if M_eve.pregnancy.stage in (3, 4):
                pos 278, 188
                idle 'character_eve_21'
                hover HoverImage('character_eve_21')
            else:
                pos 188, 33
                idle 'object_shower_eve'
                hover HoverImage('object_shower_eve')

    elif L_tattooparlor_bathroom.is_here(M_grace) and M_grace.pregnancy.stage in (3, 4):
        imagebutton:
            focus_mask True
            pos 257, 177
            idle 'character_grace_12'
            hover HoverImage('character_grace_12')
            action TalkTo(M_grace)

    elif L_tattooparlor_bathroom.is_here(M_odette) and M_odette.pregnancy.stage in (3, 4):
        imagebutton:
            focus_mask True
            pos 269, 165
            idle 'character_odette_07'
            hover HoverImage('character_odette_07')
            action TalkTo(M_odette, force=True)

    use mods_screens_hook("tattoo_parlor_bathroom")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
