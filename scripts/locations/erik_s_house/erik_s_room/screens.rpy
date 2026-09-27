screen eriks_room():
    use mods_screens_hook("eriks_room")

    add game.timer.image("backgrounds/location_erik_house_bedroom_day{}.jpg")

    if M_bissette.is_set("eriks book search") and not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (0,556)
            idle "objects/object_bed_08.png"
            hover HoverImage("objects/object_bed_08.png")
            action Hide("eriks_room"), Jump("under_bed_book_search")

    if M_bissette.is_set("eriks book search"):
        imagebutton:
            focus_mask True
            pos (446,667)
            idle game.timer.image("objects/object_socks_01{}.png")
            hover HoverImage(game.timer.image("objects/object_socks_01{}.png"))
            action Hide("eriks_room"), Jump("sock_pile_book_search")

        imagebutton:
            focus_mask True
            pos (390,530)
            idle game.timer.image("objects/object_dresser_01{}.png")
            hover HoverImage(game.timer.image("objects/object_dresser_01{}.png"))
            action Hide("eriks_room"), Jump("dresser_book_search")

    imagebutton:
        focus_mask True
        pos (559,361)
        idle game.timer.image("objects/object_desk_08{}.png")
        hover HoverImage(game.timer.image("objects/object_desk_08{}.png"))
        action ShowPopup('alpha')

    if player.location.is_here(M_erik):
        if M_erik.between_states(S_erik_cards_lost, S_erik_cards_found):
            imagebutton:
                focus_mask True
                pos (229,498)
                idle game.timer.image("objects/character_erik_02{}.png")
                hover HoverImage(game.timer.image("objects/character_erik_02{}.png"))
                action Hide("eriks_room"), Jump("erik_button_dialogue")

        else:
            imagebutton:
                focus_mask True
                pos (559,358)
                idle game.timer.image("objects/object_desk_08_erik{}.png")
                hover HoverImage(game.timer.image("objects/object_desk_08_erik{}.png"))
                action Hide("eriks_room"), Jump("erik_button_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action MoveTo(L_erikhouse_entrance)


screen under_eriks_bed():
    use mods_screens_hook("under_eriks_bed")

    imagebutton:
        focus_mask True
        pos (431,425)
        idle game.timer.image("objects/object_book_03{}.png")
        hover HoverImage(game.timer.image("objects/object_book_03{}.png"))
        action Hide("under_eriks_bed"), Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
