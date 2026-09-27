label pc_maze:
    $ A_gamer.unlock()
    call screen maze_scr

label computer_maze_fail:
    hide screen maze_scr
    scene expression "minigames/computer_maze/location_computer_minigame03_blur.jpg"
    $ renpy.suspend_rollback(False)
    call popup ('int', False)
    $ game.timer.tick()
    $ game.main()

label computer_maze_success:
    hide screen maze_scr
    scene expression "minigames/computer_maze/location_computer_minigame03b_blur.jpg"
    $ player.increase_int()
    call popup ('int', True)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
