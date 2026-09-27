label ano09_hint_tony:
    call tony_button_stage
    show tony a_frustrated
    show anon with dissolve:
        flip
    tony "Kamu sudah mendapatkan roda baru, jagoan?"

    anon "Tidak, saya masih mengerjakannya."

    tony f_suspicious "Yah, jangan berlama-lama di sini..."

    tony @ a_point "{b}Kunjungi dealer mobil dan lihat kisaran harga Anda{/b}!"

    anon @ f_laugh "Ya, tuan!"

    hide anon with dissolve
    return


label ano09_wage_tony:
    show anon with dissolve:
        flip
    anon "{b}Toni{/b}!"

    anon "Saya mendapat roda baru seperti yang Anda inginkan."

    tony @ a_frustrated "Oh ya?"

    show tony with dissolve:
        unflip
        xoffset -400
    tony f_suspicious @ a_whisper "'Eh, {b}Maria{/b}!!"

    tony "Ayo lihat wahana baru {b}[firstname]{/b} bersama saya!"

    maria "Dia punya yang lain?"

    maria "aku ikut!"

    show tony with dissolve:
        flip
        xoffset 0
    pause .5
    hide tony
    show anon:
        unflip
        xoffset 500
    with dissolve
    pause .5
    hide anon with dissolve

    scene expression background(712, 480, 2.0, l=L_pizzeria_exterior) as stage
    show tony f_normal_down:
        flip
    show tony_overlay_o_racer as coupe:
        flip
    with fade
    show anon behind coupe with dissolve:
        flip
        xoffset -32
    show maria f_surprised behind coupe with {'master': dissolve}:
        flip
        xoffset -200
    tony "Nah, itu mobil!"

    maria "Santa Maria, Bunda, dan Yusuf..."

    maria "Benda ini pasti menghabiskan banyak biaya!"

    show tony f_normal
    anon "Tidak, itu tidak terlalu buruk."

    anon "Gadis di dealer menjualnya kepada saya dengan setengah harga."

    maria f_normal @ f_confused "Tidak bercanda?"

    show tony a_mc_hip_single
    show tony_arms_dressed_a_mc_shoulder_single behind coupe:
        flip
    with dissolve
    tony "Heh, attaboy!"

    show tony a_idle:
        unflip
        xoffset -400
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve
    tony "Itulah hasil bimbinganku, di sana..."

    show maria f_eyeroll
    tony "Anak itu benar-benar hebat, kataku padamu."

    show maria f_normal
    show tony with dissolve:
        flip
        xoffset 0
    tony "Apa yang mereka sebut keindahan ini?"

    anon @ f_laugh "Kompensator Berlebihan."

    tony f_suspicious @ -m_talk "..."
    maria f_normal @ f_laugh "Pfft, hahahaah!"

    show anon f_worried
    maria "Ya, dia benar-benar hebat..."

    show tony with dissolve:
        unflip
        xoffset -400
    tony "Oh, berhentilah bertingkah seolah kamu tidak terkesan!"

    show tony f_normal a_frustrated with dissolve:
        flip
        xoffset 0
    tony "Ahh, jangan pedulikan dia, dia hanya mengganggu keberanianku."

    show tony a_idle with dissolve
    anon "Saya tidak mengerti leluconnya..."

    tony @ f_smirk_wink a_point "Anda mungkin ingin memberikan nama yang lebih baik untuk monster ini."

    anon "Oh?"

    tony "Anda tahu, sesuatu seperti elang biru atau kuda jantan safir."

    anon f_normal "Elang biru terdengar keren."

    tony "Ya, benar."

    show tony with dissolve:
        unflip
        xoffset -400
    tony "Anda dengar itu?"

    tony "Itu elang biru sekarang."

    maria @ f_laugh "Ya, itu tentu saja sebuah kemajuan."

    maria @ f_sexy "Kapan-kapan kamu harus mengajakku jalan-jalan, kan?"

    tony "Itu ide yang bagus!"

    show tony with dissolve:
        flip
        xoffset 0
    tony "Lihat jagoan, sudah kubilang para wanita akan menyukainya."

    anon "Ya, kapan saja, {b}Maria{/b}."

    tony "Ayo, kita rayakan dengan pizza dan cannolis!"

    maria @ f_surprised "Oh, kamu berbagi cannolis sekarang?"

    show tony a_mc_hip_single
    show tony_arms_dressed_a_mc_shoulder_single behind coupe:
        flip
    with dissolve
    tony "Dengan orang ini, pasti!"

    maria "Yah, kurasa kau sudah resmi menjadi bagian keluarga sekarang, Nak."

    maria "Ayo pergi."

    anon "Terima kasih teman-teman!"

    hide tony
    hide maria
    hide anon
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve

    $ game.timer.tick(3)
    $ player.go_to(L_pizzeria_exterior)
    scene expression background(712, 480, 2.0) as stage
    show tony_overlay_o_racer as coupe:
        flip
    with slowfade
    show anon f_disgusted_wince behind coupe with dissolve
    anon @ -m_talk "(Begitu banyak cannolis...)"

    anon f_grin @ -m_talk "(Sangat bagus...)"

    hide anon
    hide coupe
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
