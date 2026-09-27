init python hide:
    blink = Blink(4.)

    renpy.image('ano12_oops_knockout_slit_open', blink(
        time_warp=renpy.partial(util.lerp, max=.3),
        old_widget=renpy.displayable('black'),
        new_widget=renpy.displayable('location_warehouse_wakeup_04')))

    renpy.image('ano12_oops_knockout_slit_shut', blink(
        reverse=True,
        time_warp=renpy.partial(util.lerp, min=.7),
        new_widget=renpy.displayable('black'),
        old_widget=renpy.displayable('location_warehouse_wakeup_04')))

    renpy.image('ano12_oops_knockout_blur', blink(
        time_warp=renpy.partial(util.lerp, max=.3),
        old_widget=renpy.displayable('black'),
        new_widget=renpy.displayable('location_warehouse_wakeup_01')))

    renpy.image('ano12_oops_knockout_wide', blink(
        time_warp=renpy.partial(util.lerp, min=.2),
        old_widget=renpy.displayable('location_warehouse_wakeup_01'),
        new_widget=renpy.displayable('location_warehouse_wakeup_02')))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
