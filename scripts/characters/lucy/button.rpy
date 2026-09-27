label lucy_button_dialogue:
    scene expression player.location.background_blur with None

    if game.timer.is_day():
        call expression game.dialog_select("lucy_button_intro_day")
    else:
        call expression game.dialog_select("lucy_button_intro_night")

    menu button_lucy_menu:
        "Bagaimana kabarmu?":
            call expression game.dialog_select("button_lucy_how_are_you")
            jump button_lucy_menu

        "That milk working out for you?" if M_diane.finished_state(S_diane_delivery_2):
            call expression game.dialog_select("button_lucy_hows_the_milk")
            jump button_lucy_menu
        "{b}Annie{/b} around?":

            if game.timer.is_day():
                call expression game.dialog_select("button_lucy_annie_around_day")
            else:
                call expression game.dialog_select("button_lucy_annie_around_night")
            jump button_lucy_menu

        "How's my rugrat doing?" if PregnancyManager.total_babies() == 1 and L_annie_daycare.is_here(M_lucy):
            call expression game.dialog_select("button_lucy_baby_dialogue")
            jump button_lucy_menu

        "How are my rugrats doing?" if PregnancyManager.total_babies() > 1 and L_annie_daycare.is_here(M_lucy):
            call expression game.dialog_select("button_lucy_baby_dialogue_multiple")
            jump button_lucy_menu

        "How are the little ones?" if PregnancyManager.total_babies() > 1 and L_annie_daycare.is_here(M_lucy):
            call expression game.dialog_select("button_lucy_how_are_the_little_ones")
            jump button_lucy_menu
        "Saya harus pergi.":

            call expression game.dialog_select("button_lucy_leave")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
