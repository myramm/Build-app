label ano26_talk_liu:
    show liu f_worried a_holdup
    show anon of_ski_mask f_angry a_tiny_gun with dissolve
    anon "Kamu yang di sana!"

    anon f_worried "Umm... gadis cantik, di belakang konter!"

    liu f_confused "Y-ya?"

    anon a_behind_head "aku uhh..."

    pause
    anon a_tiny_gun f_angry "... Saya ingin Anda melakukan apa yang saya katakan, mengerti?"

    liu f_wincing @ -m_talk "!!!"
    liu f_frightened "Ya, tuan!"

    anon a_tiny_gun_move "Anda bisa memulainya dengan keluar dari balik meja itu!"

    show anon a_tiny_gun
    show liu f_ashamed_down
    with {'master': dissolve}
    liu "Oh, um..."

    pause
    anon "Ayolah, aku tidak punya waktu seharian!"

    liu f_worried "O-oke."

    show anon f_surprised
    show liu b_dressed_desk_jump1
    with dissolve
    anon @ -m_talk "!!!"
    hide liu
    show liu b_dressed_desk_jump2 f_worried_down
    with {'master': dissolve}
    anon f_surprised "Wah, jangan lakukan itu... kamu akan-"

    show liu b_dressed_desk_jump3 f_nervous_down with dissolve
    pause .3
    show anon f_shock_low
    show liu b_dressed_jump_fall
    with fastdissolve
    liu "!!!"
    hide liu
    show anon f_hurt
    with hpunch
    pause
    anon a_tiny_gun_down f_worried_low "... Jatuh."

    pause
    anon "Apakah kamu baik-baik saja?"

    show liu b_dressed_bend
    with dissolve
    liu "Y-ya, menurutku begitu."

    show anon f_confused
    show liu a_hold_arm b_dressed f_ashamed_down o_blush
    with dissolve
    anon "Anda bisa saja berjalan-jalan..."

    liu f_annoyed "Ya, saya ingin tampilannya meyakinkan di depan kamera!"

    anon f_worried "Oh benar."

    anon "I-itu masuk akal, menurutku..."

    pause
    show liu f_confused
    anon "Erm... ngomong-ngomong..."

    show anon a_tiny_gun f_angry
    show liu a_holdup f_frightened -o_blush
    with dissolve
    pause
    liu "Apakah kamu harus mengarahkannya tepat ke arahku?"

    anon f_worried "Jangan khawatir, itu tidak dimuat."

    liu f_worried "Oh."

    liu "Baiklah... o-baiklah kalau begitu."

    anon f_normal "Kamu terlihat cantik hari ini."

    liu f_happy "Hehe, terima kasih."

    anon f_angry "Sekarang, di mana brankasnya?!"

    liu f_worried "D-di bawah!"

    anon f_skeptical "Anak yang baik."

    anon a_tiny_gun_move m_talk "Bawa aku ke sana..."

    show liu f_wincing
    anon a_tiny_gun f_angry -m_talk "... Dan bukan hal yang lucu, Anda mengerti?!"

    liu f_frightened "Ya, tentu saja!"

    hide liu
    show anon f_flirt:
        xoffset -500
        xzoom -1
    with {'master': dissolve}
    anon "Mmm, kamu juga wangi."

    liu "hehe."

    hide anon with {'master': dissolve}
    anon "Bagaimana kabarmu di sana, {b}Tony{/b}?"


    scene expression background(256, 576, 8., l=L_bank_lobby) as stage
    show bankguard b_dressed_sleep
    show tony b_casual a_gun_lower o_ski_mask f_angry
    with fade
    tony "Ini menyedihkan."

    show tony a_gun_poke with dissolve
    show tony a_gun_lower with dissolve
    show tony a_gun_poke with dissolve
    show tony a_gun_lower with dissolve
    pause
    show tony a_gun_down f_sad with {'master': dissolve}:
        xoffset 500
        xzoom -1
    tony "Anda tahu, saya pikir orang ini mungkin sudah mati."

    liu "Tidak, dia hanya tua."

    liu "Dia akan seperti itu sampai waktu makan siang."

    tony "Haruskah aku repot-repot mengikatnya?"

    anon "Lebih baik aman daripada menyesal, bukan begitu?"

    tony "{i}*Huh*{/i} Ya, saya kira."

    show tony with dissolve:
        xoffset 0
        xzoom 1
    pause
    tony "Astaga, aku merasa seperti orang brengsek."

    show tony with {'master': dissolve}:
        xoffset 500
        xzoom -1
    tony "Kalian berdua pergi duluan."

    tony "Aku akan menemuimu di sana sebentar lagi."

    anon "Baiklah."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
