label jenny_bed_night_pregnant:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    anon "( There's no way I'm bothering her! )"
    if M_jenny.pregnancy.stage > 5:
        anon "( They need their rest. )"
    else:
        anon "( She needs her rest. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
