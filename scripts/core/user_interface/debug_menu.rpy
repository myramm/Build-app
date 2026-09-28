screen debug_menu_popup():
    style_prefix 'rr'
    modal True
    default understand_input = ""
    frame:
        xpadding 10
        ypadding 40
        xysize (1024-400, 768-400)
        align 0.5, 0.5
        has vbox
        text _("WARNING! This menu is intended for debugging purposes only!")
        text ""
        text _("Use of this menu WILL BREAK YOUR GAME/SAVE if used improperly.")
        text ""
        text _("Kompas Productions cannot give support nor can we accept bug reports from users who access this menu without clear direction from the development team.")
        text ""
        text _("Type 'I UNDERSTAND' in the text box below to confirm that you understand the risks involved and are happy to proceed.")
        text ""
        null
        hbox:
            xfill True
            input:
                allow ('abcdefghijklmnopqrstuvwxyz'
                           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                           '0123456789 ')
                color "#fefefe"
                length 60
                size 20
                value ScreenVariableInputValue("understand_input")
            textbutton _("Okay"):
                action If(understand_input.upper() == "I UNDERSTAND",
                              (ToggleField(persistent, "skip_debug_menu_popup"),
                               Hide("debug_menu_popup"),
                               Show('debug_menu', None, 'general')))
                keysym 'input_enter'

    imagebutton:
        focus_mask True
        pos (1024-200-40, 200-40)
        idle "buttons/debug_close.png"
        hover HoverImage("buttons/debug_close.png")
        action Hide("debug_menu_popup")

screen debug_menu(current_screen):
    style_prefix 'rr'
    modal True

    on 'show' action SetVariable('tainted', True)

    default items_input = ""
    default locations = store.locations.values()
    default machines = store.machines.values()

    if not renpy.variant("pc"):
        key "K_AC_BACK" action Hide("debug_menu")
    else:
        key "K_ESCAPE" action Hide("debug_menu")
        key "mouseup_3" action Hide("debug_menu")

    frame:
        xpadding 10
        ypadding 40
        xalign 0.5
        yalign 0.5
        xysize (1024-140, 768-140)
        has hbox
        vbox:
            textbutton "General" action Show("debug_menu", current_screen="general")
            textbutton "Time" action Show("debug_menu", current_screen="time")
            textbutton "Machines" action Show("debug_menu", current_screen="machines")
            textbutton "Locations" action Show("debug_menu", current_screen="locations")
            textbutton "Player" action Show("debug_menu", current_screen="player")
            textbutton "Items" action Show("debug_menu", current_screen="items")
        vbox:
            xfill True
            if current_screen == "general":
                hbox:
                    textbutton "Unlock UI" action Function(game.unlock_ui)
                    textbutton "Lock UI" action Function(game.lock_ui)
                    if game.ui_locked:
                        text "UI is locked" color "#c61f1d" size 16
                    else:
                        text "UI is unlocked" color "#28701d" size 16
                textbutton "Unlock Cookie Jar Scenes" action Function(unlock_all_scenes)
                textbutton "Set Rump Scene" action Function(game.set_rump_n_cunt)
                textbutton "Skip First Day" action Function(game.skip_first_day)
                textbutton "Unlock All locations" action Function (unlock_all_locations)
                hbox:
                    textbutton "Force Unlock Map" action Function(game.force_unlock_ui)
                    textbutton "Unforce Unlock Map" action Function(game.force_lock_ui)
                    if game.force_unlock_map:
                        text "Map is unlocked" color "#28701d" size 16
                    else:
                        text "Map is locked" color "#c61f1d" size 16
                hbox:
                    textbutton "Lock Sleep" action Function (game.lock_sleep)
                    textbutton "Unlock Sleep" action Function (game.unlock_sleep)
                    if game.sleep_lock:
                        text "Sleep is locked" color "#c61f1d" size 16
                    else:
                        text "Sleep is unlocked" color "#28701d" size 16
                hbox:
                    textbutton "Cheat Mode Toggle" action Function (game.toggle_cheat_mode)
                    if game.cheat_mode:
                        text "Cheat Mode is ON" color "#c61f1d" size 16
                    else:
                        text "Cheat Mode is OFF" color "#28701d" size 16
                hbox:
                    xfill True
                    textbutton "Toggle Label Name Notification" action ToggleField(persistent, "notify_label_name")
                    if persistent.notify_label_name:
                        text "Label name notifications are ON" color "#c61f1d" size 16
                    else:
                        text "Label name notifications are OFF" color "#28701d" size 16
                hbox:
                    xfill True
                    textbutton "Toggle Skip Intro" action ToggleField(persistent, "skip_intro")
                    if persistent.skip_intro:
                        text "Intro will be skipped" color "#c61f1d" size 16
                    else:
                        text "Intro will not be skipped" color "#28701d" size 16
                hbox:
                    xfill True
                    textbutton "Toggle Background Debug" action ToggleField(persistent, "background_debug")
                    if persistent.background_debug:
                        text "Background Debug is ON" color "#c61f1d" size 16
                    else:
                        text "Background Debug is OFF" color "#28701d" size 16
                hbox:
                    xfill True
                    textbutton "Rename Cat" action Hide("debug_menu"), Jump("cat_name_input_label")
                    textbutton "Rename Debbie" action Hide("debug_menu"), Jump("deb_name_input_label")
                    textbutton "Rename Jenny" action Hide("debug_menu"), Jump("jen_name_input_label")

            elif current_screen == "time":
                textbutton "Tick Timer" action Function(game.timer.tick)
                text "Set day to:"
                hbox:
                    textbutton "Mon." action Function(game.timer.set_time, 1, 0)
                    textbutton "Tue." action Function(game.timer.set_time, 1, 1)
                    textbutton "Wed." action Function(game.timer.set_time, 1, 2)
                    textbutton "Thur." action Function(game.timer.set_time, 1, 3)
                    textbutton "Fri." action Function(game.timer.set_time, 1, 4)
                    textbutton "Sat." action Function(game.timer.set_time, 1, 5)
                    textbutton "Sun." action Function(game.timer.set_time, 1, 6)
                text "Set time to:"
                hbox:
                    textbutton "Morning" action Function(game.timer.set_time, 0)
                    textbutton "Afternoon" action Function(game.timer.set_time, 1)
                    textbutton "Evening" action Function(game.timer.set_time, 2)
                    textbutton "Night" action Function(game.timer.set_time, 3)
                text "Skip Forward :"
                hbox:
                    textbutton "Day" action Function(game.timer.skip_forward, 1)
                    textbutton "Week" action Function(game.timer.skip_forward, 7)
                    textbutton "Month" action Function(game.timer.skip_forward, 31)
                    textbutton "Year" action Function(game.timer.skip_forward, 365)
                hbox:
                    xfill True
                    textbutton "Toggle Debug Period" action Function(Game.toggle_debug_period)
                    text "[game.get_period_str]" color "#c61f1d" size 16

            elif current_screen == "player":
                hbox:
                    xfill True
                    textbutton "Increase STR" action Function(player.increase_str)
                    textbutton "Increase INT" action Function(player.increase_int)
                    textbutton "Increase CHR" action Function(player.increase_chr)
                    textbutton "Increase DEX" action Function(player.increase_dex)
                hbox:
                    xfill True
                    textbutton "Add $1000" action Function(player.get_money, 1000)
                    textbutton "Remove $1000" action Function(player.spend_money, 1000)
                hbox:
                    xfill True
                    textbutton "Max all stats (10)" action Function(player.stats.max_all)

            elif current_screen == "machines":
                vbox:
                    vpgrid:
                        cols 1
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        xfill True
                        for machine in sorted(machines, key=lambda m: m._name):
                            hbox:
                                xfill True
                                label repr(machine):
                                    text_line_spacing 2
                                    text_size 15
                                hbox:
                                    xalign 1.
                                    textbutton "Advance" action Function(machine.advance):
                                        text_size 15
                                        xsize 100
                                    textbutton "Show Vars" action Show("debug_menu_machine_vars", machine=machine):
                                        text_size 15
                                        xsize 120
                                    textbutton "Pregnancy" action Show("debug_menu_machine_pregnancy", machine=machine):
                                        text_size 15
                                        xsize 120
            elif current_screen == "locations":
                vbox:
                    vpgrid:
                        cols 1
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        xfill True
                        for location in sorted(locations, key=lambda l: l.name):
                            hbox:
                                xfill True
                                label location.name:
                                    text_line_spacing 2
                                    text_size 15
                                hbox:
                                    xalign 1.
                                    if location.locked:
                                        textbutton "Unlock" action Function(location.unlock, False, True):
                                            text_size 15
                                            xsize 70
                                    else:
                                        textbutton "Lock" action Function(location.lock):
                                            text_size 15
                                            xsize 70
                                    if location.first_visit:
                                        textbutton "Visit" action Function(location.visited):
                                            text_size 15
                                            xsize 75
                                    else:
                                        textbutton "Unvisit" action Function(location.unvisit):
                                            text_size 15
                                            xsize 75
                                    if location.can_leave:
                                        textbutton "Can't Leave" action Function(location.set_cannot_leave, location):
                                            text_size 15
                                            xsize 120
                                    else:
                                        textbutton "Can Leave" action Function(location.set_can_leave, location):
                                            text_size 15
                                            xsize 120
                                    if location != player.location:
                                        textbutton "Move player":
                                            action (Function(renpy.scene, layer='screens'),
                                                        Function(player.go_to, location),
                                                        Function(location.call))
                                            text_size 15
                                            xsize 130

            elif current_screen == "items":
                vbox:
                    textbutton "Print items list to console" action Function (print_item_list)
                    if not renpy.mobile:
                        hbox:
                            text "Filter: " size 20
                            input color "#fefefe" length 60 size 20:
                                allow "abcdefghijklmnopqrstuvwxyz0123456789_"
                                value ScreenVariableInputValue("items_input")
                    vpgrid:
                        cols 1
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        xfill True
                        for item, in_inventory in search_item(items_input):
                            hbox:
                                xfill True
                                label item:
                                    text_line_spacing 2
                                    text_size 15
                                hbox:
                                    xalign 1.
                                    if in_inventory:
                                        textbutton "Remove" action Function(player.remove_item, item):
                                            text_size 15
                                            xsize 100
                                    else:
                                        textbutton "Add" action Function(player.inventory.get_item, item, force=True):
                                            text_size 15
                                            xsize 70
    imagebutton:
        focus_mask True
        pos (905, 80)
        idle "buttons/debug_close.png"
        hover HoverImage("buttons/debug_close.png")
        action Hide("debug_menu")
    if _console.console:
        imagebutton:
            focus_mask True
            pos 860, 80
            idle "buttons/debug_console.png"
            hover HoverImage("buttons/debug_console.png")
            action Hide("debug_menu"), Call("_console")
        textbutton "Console Hist.":
            action Function(print, console_history())
            pos 700, 80
            text_size 15

screen debug_menu_machine_vars(machine=None):
    style_prefix 'rr'
    modal True
    frame:
        xpadding 10
        ypadding 40
        xalign 0.5
        yalign 0.5
        xysize (1024-140, 768-140)
        has vbox
        vpgrid:
            cols 1
            draggable True
            mousewheel True
            scrollbars "vertical"
            xfill True
            for varname, varvalue in machine._vars.items():
                hbox:
                    xfill True
                    label str(varname) text_line_spacing 2
                    label str(varvalue) text_line_spacing 2 xalign 1.
        textbutton "Close" action Hide("debug_menu_machine_vars")

screen debug_menu_machine_pregnancy(machine=None):
    style_prefix 'rr'
    modal True
    frame:
        xpadding 10
        ypadding 40
        xalign 0.5
        yalign 0.5
        xysize (1024-140, 768-140)
        has vbox
        text "Name : [machine._name]" size 16
        text "Is pregnant : [machine.pregnancy.is_pregnant]" size 16
        text "Current Stage : [machine.pregnancy.stage] ([machine.pregnancy.to_full_string])" size 16
        text "Current baby gender : [machine.pregnancy.baby_gender]" size 16
        text "Announced : [machine.pregnancy.announced_pregnancy]" size 16
        text "Seen in labor : [machine.pregnancy.seen_in_labor]" size 16
        text "Character bedridden : [machine.pregnancy.character_bedridden]" size 16
        text "Gave birth : [machine.pregnancy.gave_birth]" size 16
        text "Texts : [machine.pregnancy.text_announcement_seen](announcement) [machine.pregnancy.text_labor_seen](labor)" size 16
        text "Number of babies : [machine.pregnancy.number_of_babies]" size 16
        hbox:
            xfill True
            textbutton "Get pregnant." action Function(machine.pregnancy.get_pregnant)
            textbutton "Increment Preg. (1)" action Function(machine.pregnancy._increment_pregnancy)
            textbutton "Increment Preg. (stage)" action Function(machine.pregnancy._increment_stage)
            textbutton "Re-init." action Function(machine.pregnancy.init)
        textbutton "Close" action Hide("debug_menu_machine_pregnancy")
        hbox:
            xfill True
            text "Force Baby Gender :" size 16
            textbutton "Boy" action Function(machine.pregnancy.set_debug_baby_gender, "boy")
            textbutton "Girl" action Function(machine.pregnancy.set_debug_baby_gender, "girl")
            textbutton "Twins" action Function(machine.pregnancy.set_debug_baby_gender, "twins")
            textbutton "Reset" action Function(machine.pregnancy.set_debug_baby_gender, None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
