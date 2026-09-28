label mar01_help_maria_lounge:
    scene expression background(800, 360, 4.) as stage
    show maria b_casual_magic:
        xoffset -200
    show anon a_grocery_bags behind maria with dissolve:
        flip
        xoffset 100
    maria "Don't mind the mess."
    show maria with dissolve:
        xoffset -400
    maria "We've been so busy down at the pizzeria lately..."
    show maria f_sad with dissolve:
        flip
        xoffset 0
    maria "... I'm just too tired to clean when I get home."
    anon "It looks clean to me."
    maria f_normal "Oh, you're just bein' nice..."
    maria @ a_point "You can put the bags down over there."
    show anon with dissolve:
        unflip
        xoffset 500
    maria "I'll put everything away once I get settled."
    anon "Yeah, okay."
    hide anon with dissolve
    pause
    maria "Thanks for the help, {b}[firstname]{/b}."
    anon "Not a problem!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
