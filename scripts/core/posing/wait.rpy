label wait:
    $ renpy.dynamic(quick_menu=False)
    scene black
    show text "{size=30}.{space=5}.{space=5}.{/size}" at truecenter
    with dissolve
    pause
    show text "{size=30}.{space=5}.{color=0000}{space=5}.{/color}{/size}"
    pause
    show text "{size=30}.{color=0000}{space=5}.{space=5}.{/color}{/size}"
    pause
    hide text with None
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
