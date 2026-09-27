label scene_ivy_vera:
    call scene_ivy_vera.animation
    with fade
    ivy "Apakah ini membantu meredakan ketegangan Anda?"

    vero "Tentu saja!"

    anon "(Wah, lihatlah!)"

    pause
    ivy "Hati-hati, jangan menjatuhkanku dari meja kali ini!"

    vero "Oke, itu terjadi sekali..."

    vero "... Dan itu karena Anda menggunakan {i}cara{/i} terlalu banyak pelumas!"

    ivy "Yah, maaf, tapi aku menyukainya ekstra lubey!"

    vero "Hehe!"

    pause
    anon "( Apakah mereka menggunakan dildo dua sisi? )"

    anon "(Itu sangat panas!)"

    pause
    vero "Ahh, sial!"

    ivy "Menikmati?"

    vero "Ya!!"

    pause
    ivy "Jadi, apakah kamu..."

    ivy "... Membuat-"

    $ M_ivy.set('sex speed', 1. / 14)
    ivy "Tidak!!"

    ivy "Keputusan belum?!"

    pause
    vero "Tidak, menurutku..."

    vero "... Kita perlu melakukan..."

    $ M_ivy.set('sex speed', 1. / 18)
    ivy "Sial!"

    vero "...Sedikit lagi..."

    $ M_ivy.set('sex speed', 1. / 22)
    ivy "Astaga!!"

    vero "... PENGUJIAN!!!"

    anon "(Wow, lihat mereka pergi...)"

    pause
    anon "(Saya sangat ingin tinggal di sini dan menonton...)"

    return


label scene_ivy_vera.animation:
    $ M_ivy.set('sex speed', 1. / 10)
    scene location_pink_massage_sex_spy
    show ivy_sex_vera
    return


label scene_ivy_vera.repeat:
    call scene_ivy_vera.animation
    $ M_ivy.set('sex speed', 1. / 18)
    with fade
    anon "(Saya yakin {b}Diane{/b} tidak akan keberatan jika saya meluangkan waktu... )"

    anon "(... Sedikit lebih lama lagi tidak ada salahnya.)"

    ivy "Haah! Haah!!"

    pause
    ivy "Tetap saja..."

    ivy "... Belum diputuskan?"

    vero "Anda tidak bisa terburu-buru-"

    vero "Hng!"

    vero "... pengujian semacam ini!"

    pause
    anon "(Sepertinya itu akan memakan waktu cukup lama.)"

    return


label scene_ivy_vera.replay:
    jump scene_ivy_vera
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
