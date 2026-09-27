label park_lock_check:
    scene expression player.location.background_blur

    if player.location == L_park_bushesbag and not player.has_picked_up_item("treasure_key"):
        scene expression L_park_bushesbag.background
        show object_key_02:
            pos (540, 280)
        anon "( I don't think anyone will miss this key... )"

        anon "( It looks important some how. {b}I should pick it up.{/b} )"

    else:

        return

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
