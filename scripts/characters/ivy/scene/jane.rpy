label scene_ivy_jane:
    call scene_ivy_jane.animation
    with fade
    ivy "Mmm, saya belum pernah mendapat tawaran pelanggan untuk memberi {i}saya{/i} pijatan sebelumnya..."

    jane "Apakah rasanya enak?"

    ivy "Ya, tentu saja."

    anon "(Oh wow, mereka telanjang!)"

    pause
    anon "( Dan {b}Jane{/b} sedang meraba {b}Ivy{/b}!! )"

    ivy "Anda cukup terampil dengan tangan Anda."

    jane "Hehe, aku sudah banyak berlatih dalam hal ini."

    pause
    jane "Bagaimana caramu menjaga vaginamu tetap kencang saat bekerja?"

    jane "Aku hampir tidak bisa memasukkan dua jari ke dalam dirimu."

    ivy "Haah, itu perlu..."

    ivy "... Banyak pekerjaan."

    jane "Ya, aku berani bertaruh."

    pause
    ivy "Oh, itu tempatnya!"

    jane "Ya, kamu suka itu?"

    ivy "Ngh, disana!!"

    pause
    anon "( Sial, {b}Ivy{/b} sudah hampir mencapai cumming? )"

    anon "( {b}Jane{/b} pasti tahu apa yang dia lakukan di sana! )"

    pause
    jane "Jadi berapa banyak sesi gratis yang kudapat untuk klitoris elektrik itu?"

    ivy "Aku tidak tahu, aku-"

    $ M_ivy.set('sex speed', 1. / 24)
    jane "Hmm?"

    ivy "Ya Tuhan!!"

    ivy "saya-"

    pause
    ivy "Sial, sebanyak yang kamu mau!!"

    jane "Hehe, jawaban yang bagus."

    pause
    anon "(Sebaiknya aku keluar dari sini sebelum mereka selesai...)"

    anon "( ..tidak ingin ketahuan. )"

    return


label scene_ivy_jane.animation:
    $ M_ivy.set('sex speed', 1. / 12)
    scene location_pink_massage_sex_spy
    show ivy_sex_jane
    return


label scene_ivy_jane.repeat:
    call scene_ivy_jane.animation
    $ M_ivy.set('sex speed', 1. / 18)
    with fade
    ivy "Terlalu banyak! aku tidak bisa-"

    jane "Tentu saja bisa."

    pause
    jane "Sekarang cum untukku."

    jane "Lagi!"

    ivy "NGGHHH!!!"

    return


label scene_ivy_jane.replay:
    jump scene_ivy_jane
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
