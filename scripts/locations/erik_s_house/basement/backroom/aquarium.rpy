label eriks_aquarium_dialogue:
    $ game.main()


label eriks_aquarium_cards:
    scene expression player.location.background_blur
    show closeup_box at truecenter with dissolve
    player_name "( Here they are! I'd better get them back to {b}Erik{/b}. )"

    hide closeup_box with dissolve
    $ player.get_item('eriks_cards')
    $ M_erik.trigger(T_erik_cards_found)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
