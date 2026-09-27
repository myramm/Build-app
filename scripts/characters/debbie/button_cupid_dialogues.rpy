label mom_cupid_outing_choose_gift:
    show player 5 at left with dissolve
    show old_debbie 165 at Position(xpos=.75, ypos=1.0) with dissolve
    debbie "Apakah kamu menemukan sesuatu, sayang?"

    show player 10
    show old_debbie 164
    player_name "Saya masih mencari."

    show player 5
    show old_debbie 166
    debbie "Hehe, oke!"

    show old_debbie 165
    debbie "Jangan terlihat terlalu serius. Sangat mudah! Temukan saja sesuatu yang menurut Anda akan saya sukai..."

    show old_debbie 164
    pause
    hide old_debbie with dissolve
    show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
    player_name "( ... )"
    player_name "( Sesuatu yang {b}[deb_name]{/b} inginkan? )"

    player_name "(Mungkin sebuah kalung?)"

    return

label mom_cupid_outing_show_necklace:
    show player 492 zorder 0 at left
    show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
    with dissolve
    show old_debbie 164 at Position(xpos=0.75, ypos=1.0) with dissolve
    player_name "Oke, {b}[deb_name]{/b}. Bagaimana dengan ini?"

    hide xtra
    show player 1 with dissolve
    show old_debbie 170 at Position(xpos=0.7, ypos=1.0) with dissolve
    show old_debbie 172
    debbie "Oh, {b}[firstname]{/b}... Sungguh {b}kalung{/b} yang indah."

    show old_debbie 170
    show player 14
    player_name "Anda sangat menyukainya?"

    show player 13
    show old_debbie 171
    debbie "Saya bersedia! Seleramu bagus, sayang."

    show old_debbie 170
    show player 14
    player_name "Hehe, terima kasih, {b}[deb_name]{/b}!"

    show player 13
    show old_debbie 173 at Position(xpos=0.775, ypos=1.0)
    pause 1
    show old_debbie 174 at Position(xpos=0.7, ypos=1.0)
    pause 1
    show old_debbie 175
    pause 2
    show old_debbie 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
    show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
    pause
    show old_debbie 165
    debbie "Ya?"

    show player 14
    show old_debbie 164
    player_name "... Hmm?"

    show player 13
    show old_debbie 166
    debbie "Bagaimana penampilanku?"

    show player 14
    show old_debbie 164
    player_name "Kamu terlihat cantik, {b}[deb_name]{/b}!"

    show player 13
    show old_debbie 166
    debbie "Aww... Terima kasih, sayang."

    show old_debbie 164
    debbie "Hmm..."

    show old_debbie 165
    debbie "Di mana cermin saat Anda membutuhkannya?"

    show old_debbie 164
    player_name "..."
    show player 14
    player_name "Mungkin ada satu di ruang ganti..."

    show player 13
    show old_debbie 165
    debbie "Pemikiran yang bagus, sayang!"

    debbie "Saya akan segera kembali."

    hide old_debbie
    hide mneck
    with dissolve
    show player 14
    player_name "Oke."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
