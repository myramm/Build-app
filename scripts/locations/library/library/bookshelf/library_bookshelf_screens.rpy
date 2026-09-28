screen library_bookshelf():
    add "library_shelf"

    imagebutton:
        focus_mask True
        pos (742,416)
        idle "buttons/book_01.png"

        action NullAction()

    if M_bissette.get_state() == S_bissette_get_dictionary and not player.has_item("french_dictionary"):
        imagebutton:
            focus_mask True
            pos (190,453)
            idle "buttons/book_04.png"
            hover HoverImage("buttons/book_04.png")
            action Hide("library_bookshelf"), Jump("french_dictionary")

    if M_diane.is_state(S_diane_check_bookshelf):
        imagebutton:
            focus_mask True
            pos (234,110)
            idle "buttons/book_02.png"
            hover HoverImage("buttons/book_02.png")
            action Hide("library_bookshelf"), Jump(game.dialog_select("breeding_guide"))

    if M_erik.is_state(S_erik_learn_fetch, S_erik_learn_get_kamasutra):
        imagebutton:
            focus_mask True
            pos (406,440)
            idle "buttons/book_03.png"
            hover HoverImage("buttons/book_03.png")
            action Hide("library_bookshelf"), Jump("kamasutra")

    if not player.has_item("old_book"):
        imagebutton:
            focus_mask True
            pos (836,108)
            idle "buttons/book_05.png"
            hover HoverImage("buttons/book_05.png")
            action Hide("library_bookshelf"), Jump("library_old_book")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_04.png"
        hover HoverImage("boxes/auto_option_04.png")
        action ExitLocation()

    use mods_screens_hook("library_bookshelf")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
