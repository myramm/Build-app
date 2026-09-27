label liu_bedroom_dialogue:

    if M_anon.is_state(S_ano24_find):
        call ano24_find_liu_bedroom

    $ game.main()
    return


label liu_bedroom_bomb:
    if not M_liu.once('ano24_bomb'):
        call ano24_find_bomb
    else:
        call ano24_find_bomb.repeat

    $ game.main()
    return


label liu_bedroom_painting:
    call liu_bedroom_painting_dialogue

    $ game.main()
    return


label liu_bedroom_picture:
    if not M_liu.once('ano24_picture'):
        call ano24_find_picture
    else:
        call ano24_find_picture.repeat

    $ game.main()
    return


label liu_bedroom_stash:
    call ano24_find_stash
    $ game.timer.tick(3)
    $ player.go_to(L_police_front)
    $ M_anon.trigger(T_ano24_find)

    $ game.main()
    return


label liu_bedroom_statue:
    if not M_liu.once('ano24_statue'):
        call ano24_find_statue
    else:
        call ano24_find_statue.repeat

    $ game.main()
    return


label liu_bedroom_wardrobe:
    if not M_liu.once('ano24_wardrobe'):
        call ano24_find_wardrobe
    else:
        call ano24_find_wardrobe.repeat

    $ game.main()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
