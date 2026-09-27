label pier_board_dialogue:
    scene expression game.timer.image('pier_board{}')
    anon "( These must be the {b}types of fish{/b} you can catch on the pier and {b}what bait to use{/b}. )"

    pause
    return


label pier_board_dialogue.repeat:
    scene expression game.timer.image('pier_board{}')
    pause
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
