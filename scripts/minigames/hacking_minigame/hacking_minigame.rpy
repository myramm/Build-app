label hacking_minigame_pre:
    show screen hacking_minigame_pre
    if not M_jenny.once('pc_hack_attempted'):
        anon "( Yeah, this is what I'm looking for, right here! )"

        anon "( Now I just need to work a little magic... )"

    else:
        anon "( Come on {b}[firstname]{/b}, you got it this time, just focus... )"

    hide screen hacking_minigame_pre
    jump hacking_minigame_call

label hacking_minigame_call:
    call screen hacking_minigame

label hacking_minigame_win:
    show screen hacking_minigame_win
    pause
    hide screen hacking_minigame_win
    scene expression player.location.background_closeup with None
    show player 17
    player_name "( I think I did it! )"

    player_name "( Now I should be able to {b}view her CAMslut profile on my computer{/b}. )"

    show player 403
    player_name "( I can't wait to check out those videos! )"

    hide player with dissolve
    $ M_jenny.set("pc_hacked", True)
    $ A_computer_genius.unlock()
    $ game.main()

label hacking_minigame_fail:
    show screen hacking_minigame_fail
    pause
    hide screen hacking_minigame_fail

    scene expression player.location.background_closeup with None
    show player 11 with dissolve
    player_name "( What the... It locked me out! )"

    player_name "( I almost had it too. )"

    jenny "{i}*Mendengus*{/i}"

    show player 22
    player_name "( Oh, crap! )"

    jenny "Mmm, that'll cost you... {i}*Yawn*{/i} four hundred... {i}*Zzz*{/i}..."

    player_name "( She's stirring! )"

    pause
    player_name "( I gotta get out of here! )"

    hide player with dissolve
    $ player.go_to(L_home_hallway)

    $ display.toast(int_fail)
    scene expression player.location.background_closeup with None
    show player 37 with dissolve
    player_name "( Phew, that was close! )"

    player_name "( I'll just have to {b}try again tomorrow night{/b}... )"

    player_name "( If only I knew my way around {b}computers{/b} a bit more... )"

    hide player with dissolve
    $ player.go_to(L_home_hallway)
    $ game.timer.tick()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
