label odette_repeat_sex_couch:
    anon "Di sofa. Telanjang."

    odette f_pouting "Hmm, membosankan sekali ya?"

    show anon f_worried

    if M_odette.once('couch_sex') and not M_odette.once('couch_anal'):
        jump odette_repeat_sex_couch.second

    jump odette_repeat_sex_couch.repeat


label odette_repeat_sex_couch.repeat:
    pause
    odette f_normal "Oh baiklah."

    show anon f_normal
    odette f_smirk "Kurasa aku tidak bisa menyalahkanmu karena ingin melihat si kembar melompat-lompat."

    anon f_confused "Si kembar?"

    show odette b_skirt f_happy_down a_remove1
    with dissolve
    pause
    show anon f_flirt_low
    show odette b_skirtblank a_remove2
    with dissolve
    pause
    show odette a_remove3
    with dissolve
    show odette a_remove4
    with dissolve
    show odette f_smirk b_skirt a_reveal
    with {'master': dissolve}
    odette "Ta-da!!"

    anon f_flirt "Oh benar."

    show anon f_flirt_low
    show odette f_happy_down a_remove5
    with dissolve
    pause
    show odette b_remove6
    with dissolve
    pause
    show odette a_hips b_panties f_smirk
    with {'master': dissolve}
    anon f_happy "Ya ampun, tubuhmu konyol!"

    odette f_shy "Hehe, terima kasih."

    show anon f_shy_low
    show odette b_remove7 f_happy_down
    with dissolve
    pause
    show anon f_shy
    show odette b_naked f_smirk
    with {'master': dissolve}
    odette "Sekarang, ayo kawan..."

    hide odette
    with {'master': dissolve}
    odette "... Memekku sangat ingin diaduk!"

    anon f_confused "Mendambakan apa sekarang?!"

    odette "Kemarilah dan persetan denganku!"

    hide anon
    with {'master': dissolve}
    anon "Ya, Bu."


    call scene_odette_couch_back.repeat (M_odette.get('couch_anal', False))
    $ unlock_scene('Odette', '06_unlocked', variant='back')

    if 'anal' in _return:
        jump odette_repeat_sex_couch.recovery

    scene expression background(l=L_tattooparlor_garage) as stage
    show odette a_grab_top b_wakeup f_tired_down:
        xoffset 100
        xzoom -1
    show anon b_dressed_changing at flip
    with fade
    pause
    show odette a_pull_top
    show anon a_sides b_dressed
    with {'master': dissolve}
    pause
    show odette a_sides b_dressed f_surprised
    with {'master': dissolve}
    odette @ -m_talk "!!!"
    show anon f_surprised
    odette "Astaga, apa ini sudah larut?!"

    odette f_sad "Aku harus pergi ke toko atau {b}Grace{/b} akan membunuhku!"

    show anon f_worried
    anon "Ya baiklah."

    anon "Sampai jumpa lagi?"

    show anon f_normal
    odette f_smirk "Nanti, kawan."

    show odette a_kiss f_kiss
    with {'master': dissolve}
    odette @ -m_talk "Muah!"

    hide odette
    show anon a_wave f_flirt_grin
    with {'master': dissolve}
    odette "Beritahu {b}Evie{/b} Aku menyapa!!"

    anon f_happy "Akan berhasil!"

    hide anon with dissolve
    return 'afterglow'


label odette_repeat_sex_couch.second:
    pause
    show odette f_thinking
    pause
    show anon f_confused
    odette f_smirk "Atau mungkin tidak!"

    show anon f_surprised
    odette "Anda ingin memasukkan benda besar itu ke pantat saya?"

    show anon f_brag
    anon "Maksudku, apakah kamu pikir kamu bisa mengatasinya?"

    odette f_smirk_lip_down @ -m_talk "Hmm."

    pause
    odette f_smirk "Ya, hanya ada satu cara untuk mengetahuinya!"

    show odette b_skirt f_happy_down a_remove1
    with dissolve
    pause
    show anon f_flirt_low
    show odette b_skirtblank a_remove2
    with dissolve
    pause
    show odette a_remove3
    with dissolve
    show odette a_remove4
    with dissolve
    show anon f_flirt
    show odette f_normal b_skirt a_hips
    with {'master': dissolve}
    anon "Apakah itu ya?"

    odette f_smirk "Itu tentatif ya..."

    odette "... Hanya saja, pelan-pelan dulu, ya?"

    odette "Sudah lama tidak bertemu."

    show anon f_flirt_low
    show odette f_happy_down a_remove5
    with dissolve
    pause
    show odette b_remove6
    with dissolve
    pause
    show odette a_hips b_panties f_smirk
    with {'master': dissolve}
    anon f_shy "Lambat, benar."

    anon f_brag "Ya, saya bisa melakukan itu."

    show anon f_shy_low
    show odette b_remove7 f_happy_down
    with dissolve
    pause
    show anon f_brag
    show odette b_naked f_smirk
    with {'master': dissolve}
    odette "Ayolah!"

    hide odette
    with {'master': dissolve}
    anon f_happy "Luar biasa."


    call scene_odette_couch_anal
    $ unlock_scene('Odette', '06_unlocked', variant='anal')

    label odette_repeat_sex_couch.recovery:
    scene expression background(l=L_tattooparlor_garage) as stage
    show odette a_grab_top b_wakeup f_tired_down:
        xoffset 100
        xzoom -1
    show anon b_dressed_changing at flip
    with fade
    pause
    show odette a_pull_top
    show anon a_sides b_dressed
    with {'master': dissolve}
    pause
    show odette a_butthurt b_dressed f_pouting_right
    with {'master': dissolve}
    odette "Ya ampun, aku akan berjalan-jalan dengan lucu sepanjang hari ini..."

    anon f_confused "Ya?"

    show odette a_hips f_pouting
    with {'master': dissolve}
    odette "... Kamu benar-benar melakukan sesuatu padaku."

    anon f_worried "Menurutmu {b}Grace{/b} akan menyadarinya?"

    odette f_smirk "Jangan khawatir."

    odette "Aku hanya akan bilang padanya aku terlalu keras dengan salah satu mainanku."

    anon f_brag "Sering-seringlah melakukannya, bukan?"

    odette @ f_wink "Kadang-kadang."

    pause
    odette "Hehe, nanti, kawan."

    show odette a_kiss f_kiss
    with {'master': dissolve}
    odette @ -m_talk "Muah!"

    hide odette
    show anon a_wave f_happy
    with {'master': dissolve}
    anon "Nanti, {b}Odette{/b}."

    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
