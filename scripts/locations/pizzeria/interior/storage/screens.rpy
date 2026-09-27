screen pizzeria_storage():
    if M_maria.sex:
        add 'location_pizza_storage_bed_night'
    else:
        add L_pizzeria_storage.background

    imagebutton:
        focus_mask True
        pos (68,226)
        idle game.timer.image("objects/object_door_128{}.png")
        hover HoverImage(game.timer.image("objects/object_door_128{}.png"))
        action ExitLocation()

    if M_anon.is_state(S_ano08_sack):
        imagebutton:
            focus_mask True
            pos 828, 553
            idle 'objects/object_flour.png'
            hover HoverImage('objects/object_flour.png')
            action HideAll(), Jump('pizzeria_storage_sack')

    if L_pizzeria_storage.is_here(M_maria):
        imagebutton:
            focus_mask True
            if M_maria.sex:
                pos 457, 365
                idle 'characters/maria/buttons/character_maria_09.png'
                hover HoverImage('characters/maria/buttons/character_maria_09.png')
            else:
                pos 711, 153
                idle 'characters/maria/buttons/character_maria_03.png'
                hover HoverImage('characters/maria/buttons/character_maria_03.png')
            action If(M_anon.is_state(S_ano11_bone),
                      Call('popup_branch', TalkTo(M_maria)),
                      TalkTo(M_maria))

    use mods_screens_hook("pizzeria_storage")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
