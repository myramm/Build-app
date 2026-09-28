label locker_check(direction, locker):
    if direction == "left":
        show expression game.timer.image("backgrounds/location_school_lefthall{}.jpg")
    else:
        show expression game.timer.image("backgrounds/location_school_right_hall{}.jpg")
    show anon with dissolve:
        xoffset 300
    if game.timer.is_day():
        if player.has_picked_up_item("master_key"):
            if not locker.is_visited:
                $ charname = locker.name.split("'")[0]
                anon "This master key is awesome! Now, let's see what's in {b}[charname]{/b}'s locker."
            $ player.location = locker
        else:
            show anon f_worried
            call expression game.dialog_select("locker_locked_{}".format(random.randint(1,2)))
            if direction == "left":
                $ player.go_to(L_school_lefthallway)
            else:
                $ player.go_to(L_school_righthallway)
            $ game.main()
    else:
        if not player.has_picked_up_item("master_key"):
            call expression game.dialog_select("locker_locked_night")
            if direction == "left":
                $ player.go_to(L_school_lefthallway)
            else:
                $ player.go_to(L_school_righthallway)
            $ game.main()
        else:
            if not locker.is_visited:
                $ charname = locker.name.split("'")[0]
                anon "This master key is awesome! Now, let's see what's in {b}[charname]{/b}'s locker."
            $ player.location = locker
    scene expression locker.background
    return

label locker_locked_1:
    anon "That's not my locker... I would need a key to open it."
    hide anon with dissolve
    return

label locker_locked_2:
    anon "It's locked and I don't have the key."
    anon "{b}Mrs. Smith{/b} probably has a key to everything."
    hide anon with dissolve
    return

label locker_locked_night:
    scene expression player.location.background_blur
    show anon f_worried with dissolve
    anon "This isn't the best time to be loitering in the hallways. I should try again during the day."
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
