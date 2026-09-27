label harold_button_office:
    return


label harold_button_office.photo:
    hide old_harold
    hide player
    show harold
    show anon
    anon f_normal "Saya menemukan foto ini."

    show anon f_looking_down a_backpack with dissolve
    harold f_normal @ -m_talk "Hmm?"

    anon f_normal a_box_attic_photo "Itu disembunyikan di dalam kotak bukti yang kalian kembalikan kepada kami."

    show anon a_idle
    show harold a_attic_box_photo f_surprised_down
    with dissolve
    pause
    harold f_normal_closed "Kamu bercanda denganku..."

    anon "Tidak."

    harold f_concerned "{i}*Huh*{/i} Bagaimana para teknisi bisa melewatkan ini?!"

    harold a_idle "Aku akan segera membawanya kembali ke sana."

    harold "Terima kasih telah memberitahukannya kepada saya."

    anon f_surprised "Tunggu, itu saja?"

    harold @ f_suspicious "Apa maksudmu?"

    anon "Saya baru saja membawakan Anda bukti keterlibatan {b}Walikota Rump{/b} dengan aktivitas mafia Rusia!"

    harold f_normal "Ehh, sebenarnya tidak banyak yang bisa dilanjutkan, Nak."

    anon f_angry a_frustrated "Apakah kamu bercanda?"

    anon "Orang di sebelah kanan itu adalah bos mafia Rusia!"

    harold @ f_suspicious "Bagaimana kamu tahu itu?"

    anon a_sides "Tidak peduli bagaimana aku mengetahuinya, aku hanya tahu!"

    anon "Sekarang apakah kamu akan melakukan sesuatu dengan ini atau tidak?!"

    harold a_hips "Wah, Nak... Tenanglah."

    harold "Bahkan jika Anda benar, dan ini adalah orang yang bertanggung jawab atas organisasi ilegal ini... Satu foto dengan dia dan walikota tidaklah cukup untuk melanjutkan."

    harold "Saya tidak bisa begitu saja menuduh politisi terhormat seperti {b}Ronald Rump{/b} tanpa bukti yang kuat."

    anon "Ini adalah lelucon."

    anon "{b}Tony{/b} benar, kepolisian ini tidak berguna."

    harold "{b}Tony{/b} siapa?"

    anon @ f_surprised "Sudahlah."

    anon a_idle "Selamat siang, detektif."

    hide anon with dissolve
    harold f_concerned "Baiklah, tunggu sebentar..."

    pause
    harold "{b}[firstname]{/b}?!"

    pause
    harold f_normal_closed a_sides "{i}*Huh*{/i}"


    $ player.go_to(L_police_front)
    scene expression player.location.background_blur with fade
    show anon f_angry with dissolve
    anon @ -m_talk "(Buang-buang waktu saja!)"

    pause
    anon @ -m_talk "(Dan sekarang saya kehilangan gambaran {b}Rump{/b} dan bos mafia!)"

    anon @ f_hurt -m_talk "( Grr! )"

    anon @ -m_talk "(Setidaknya saya masih memiliki kunci kotak kuncinya.)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
