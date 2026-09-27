label maze_pre:
    if game.cheat_mode:
        scene location_lair_ocean with None
        menu:
            "Skip minigame. (Cheat)":
                jump maze_pass
            "Play minigame.":

                $ pass
    call screen lair_maze
    return

label maze_fail:
    $ M_aqua.trigger(T_aqua_chase_fail)
    $ game.timer.tick()
    $ player.go_to(L_pier)

    scene location_lair_fail_maze
    show text _ ("I was completely lost and running out of air.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("There was no choice but to retreat back to the surface.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Hopefully I'll do better next time...") as caption with dissolve
    pause
    $ game.main()
    return

label maze_pass:
    $ M_aqua.trigger(T_aqua_maze_conquered)

    scene location_lair_emerge
    show text _ ("The cave was a labyrinth of twists and turns.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I pushed forward stubbornly until I felt my lungs about to burst...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... This can't be the end! This can't be-") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Wait, is that, light?!") as caption with dissolve
    pause
    jump lair_dialogue
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
