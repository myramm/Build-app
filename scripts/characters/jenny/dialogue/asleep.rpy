label jenny_bed_night_pregnant:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    anon "(Tidak mungkin aku mengganggunya!)"

    if M_jenny.pregnancy.stage > 5:
        anon "(Mereka butuh istirahat.)"

    else:
        anon "(Dia perlu istirahat.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
