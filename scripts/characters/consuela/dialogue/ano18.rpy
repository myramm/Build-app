label ano18_trap_consuela:
    show consuela:
        xoffset -100
    show anon behind consuela with dissolve:
        flip
        xoffset 100
    pause
    show ricky:
        xoffset -100
    show consuela f_sad a_facepalm:
        flip
        xoffset 200
    with dissolve
    consuela "No, no, no... He has to go!" (show_native="¡No, no, no... El tiene que irse!")
    show consuela a_idle with dissolve
    ricky "You gotta go, handsome!"
    ricky "You really don't want {b}Mister Rump{/b} to catch you back here."
    show anon f_worried
    ricky "Trust me."
    anon "Y-yeah, alright."
    anon "I'm coming back though!"
    consuela @ a_point "Go!"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
