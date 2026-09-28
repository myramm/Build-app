screen library():
    add player.location.background

    imagebutton:
        focus_mask True
        alt "Library Bookshelf"
        pos (513,354)
        idle "objects/object_shelf_03.png"
        hover HoverImage("objects/object_shelf_03.png")
        action MoveTo(L_library_bookshelf)

    if player.location.is_here(M_mia):
        imagebutton:
            focus_mask True
            pos (24,402)
            idle "objects/character_mia_05.png"
            hover HoverImage("objects/character_mia_05.png")
            action Hide("library"), If(
                                       M_bissette.get_state() == S_bissette_reference_book_search,
                                       Jump("poem_assignment_lock"),
                                       Jump("mia_library_dialogue")
            )

    imagebutton:
        focus_mask True
        pos (104,378)
        alt "Librarian Desk"
        idle "objects/object_desk_05.png"
        hover HoverImage("objects/object_desk_05.png")
        action TalkTo(M_jane)

    imagebutton:
        focus_mask True
        pos (636,349)
        alt "Library Backroom Door"
        idle "objects/object_door_29.png"
        hover HoverImage("objects/object_door_29.png")
        action Hide("library"), MoveTo(L_library_backroom)

    imagebutton:
        focus_mask True
        pos (803,324)
        alt "Library Meeting Room Door"
        idle "objects/object_door_55.png"
        hover HoverImage("objects/object_door_55.png")
        action Hide("library"), MoveTo(L_library_meetingroom)

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        alt "Exit Library"
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("library"), MoveTo(L_library_front)

    use mods_screens_hook("library")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
