label iwa02_init_rump_second:
    scene expression background(288, 368, 3.5)
    show iwanka f_laugh
    show anon with dissolve:
        xoffset 250
    iwanka "Ya ampun!"

    show iwanka b_dressed_back_hug:
        xoffset 250
    show anon b_empty f_surprised
    anon "!!!" with hpunch
    anon "H-hey, what's going on?"

    iwanka "You actually did it!"

    show anon b_dressed f_normal
    show iwanka b_dressed f_excited:
        xoffset 0
    with dissolve
    iwanka "He's really gone!"

    anon "Pretty crazy, huh?"

    iwanka f_smirk "Think you can get rid of my mother next?"

    anon f_shy @ a_behind_head "Ehh..."

    iwanka f_excited @ f_laugh "Hehe, I'm just kidding!"

    pause
    iwanka "Seriously, though... Thank you!"

    anon f_normal "Terima kasih kembali."

    iwanka f_smirk "I'm heading out to the yacht, wanna join me?"

    anon f_shy "Umm, maybe later."

    iwanka "Aww, you sure?"

    iwanka "I will totally fuck your brains out."

    anon f_surprised "!!!"

    menu:
        "What are we waiting for?!":
            jump iwa02_init_rump_second.yacht
        "Rain check?":

            pass

    anon f_shy "Rain check?"

    iwanka f_bored @ f_eyeroll "Dengan serius?"

    iwanka "I thought for sure that would change your mind."

    anon "I really wanna go but I have something to take care of first."

    iwanka "Sesuaikan dirimu."

    iwanka f_smirk "Anda tahu di mana menemukan saya."

    hide iwanka
    show anon:
        flip
        xoffset -250
    with dissolve
    pause
    anon a_behind_head "Aduh, bung..."

    hide anon with dissolve
    return


label iwa02_init_rump_second.yacht:
    anon f_flirt "What are we waiting for?!"

    iwanka f_laugh "Hehe, I thought that would change your mind..."

    show iwanka b_dressed_pulling_anon:
        flip
        xoffset -250
    show anon b_empty f_surprised:
        flip
        xoffset -250
    with dissolve
    iwanka "Ayo berangkat!"

    hide iwanka
    hide anon
    with dissolve
    anon "!!!"
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
