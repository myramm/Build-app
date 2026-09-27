label button_grace_livingroom_no_thanks:
    anon "Itu mungkin bukan ide yang bagus."

    grace f_normal @ f_surprised "Saya setuju!"

    odette f_tired "Cih, kalian berdua tidak menyenangkan..."

    pause
    anon f_normal "Apakah {b}Hawa{/b} ada di sini?"

    grace "Ya, dia ada di kamarnya, {b}[firstname]{/b}."

    anon @ f_laugh "Terima kasih!"

    odette f_smirk "Kau tahu, dia mungkin sangat sibuk di sana..."

    odette "Saya rasa dia tidak akan keberatan jika Anda tinggal dan mengawasi kami sebentar."

    grace f_angry_back "{b}Odette{/b}!"

    odette "Apa?!"

    odette "Tidak ada salahnya untuk menonton!"

    grace "Tinggalkan pacar saudara perempuanku sendirian!"

    odette @ f_eyeroll "Uh, baiklah."

    return

label button_grace_livingroom_odette_no:
    anon f_worried "Saya hanya ingin tahu bagaimana kabar Anda dan {b}Grace{/b}?"

    odette f_angry @ -m_talk "..."
    odette "Kamu serius?"

    anon @ a_behind_head "Ya?"

    pause
    odette @ f_eyeroll "Ya, keadaan mereka jauh lebih baik sebelum Anda mengganggu kami!"

    odette "Saya berada di urutan kedua dan sekarang saya harus menghangatkannya lagi!"

    anon f_sad_down "Maafkan aku, aku-"

    odette "Cih, kukira kau akan memberiku penis manis, manis, yang sudah kuidam-idamkan!"

    anon @ -m_talk "..."
    odette @ f_eyeroll "Ah, lupakan saja."

    hide odette with dissolve
    pause
    anon f_tired "Ups."

    hide anon with dissolve
    return

label button_grace_livinroom_odette_yeah:
    anon f_flirt "Y-ya."

    odette "Oh, aku selalu ingin bermain-main denganmu, kawan!"

    odette @ f_laugh "Keluarkan penis itu dan ayo lakukan ini!"

    return

label button_grace_livingroom_speak_with_odette:
    anon f_worried "Sebenarnya bolehkah saya meminjam {b}Odette{/b}?"

    show odette f_smirk
    grace f_suspicious "Pinjam dia?"

    anon "Ya, aku hanya perlu menanyakan sesuatu padanya."

    anon "Hanya butuh satu menit."

    odette "Yah, semoga lebih lama dari satu menit, kawan..."

    anon f_surprised @ -m_talk "!!!"
    grace f_tired_back "Maksudnya itu apa?"

    odette f_normal @ f_surprised -m_talk "Hmm?"

    odette "Oh, tidak ada sama sekali."

    odette f_smirk "Biarkan aku memakai pakaianku dan aku akan menemuimu di bawah, oke?"

    anon f_flirt "Terima kasih."

    pause
    grace f_tired_back "Apakah ada sesuatu yang terjadi di antara kalian berdua, {b}Odette{/b}?"

    odette f_normal @ f_laugh "Oh, jangan konyol!"

    odette "Dia mungkin hanya butuh nasihat atau semacamnya."

    grace "Nasihat macam apa yang mungkin dia butuhkan dari Anda?!"

    odette "Hmm, entahlah..."

    odette f_smirk "Mungkin dia ingin tahu cara membuat adikmu menggeliat dalam ekstasi yang sama seperti yang kuberikan padamu..."

    grace f_surprised "Menggeliat?!"

    grace f_surprised_back "I-itu bukan-"

    odette @ f_laugh "Ha ha ha!"

    odette "Tenang saja, aku akan kembali sebelum kamu menyadarinya."

    hide grace
    show odette b_massage_kiss
    with dissolve
    pause
    show grace b_massage_laying behind grace_sex_mc_foreground
    hide odette
    with dissolve
    grace f_normal_down "O-oke."

    $ player.go_to(L_tattooparlor_garage)
    scene expression player.location.background_blur
    show anon f_worried
    show odette f_smirk
    with fade
    pause
    odette @ a_point "Ingin bercinta?"

    return

label button_grace_livinroom_yes_please:
    anon @ f_laugh a_point "Ya, tolong!"

    grace f_sad "Uhh, aku tidak begitu yakin itu ide yang bagus..."

    odette f_smirk "Oh, jangan konyol!"

    odette "Itu hanya kesenangan kecil yang tidak berbahaya."

    grace f_sad_down "Y-ya, tapi-"

    odette "Mengapa kamu tidak melepas pakaian itu dan berbaring di sini."

    odette "Saya yakin {b}Grace{/b} sangat ingin memulai."

    grace @ -m_talk "{i}*Meneguk*{/i}"

    odette @ f_laugh "hehe!"

    return

label button_grace_livingroom_intro:
    scene location_tattoo_apartment_oil
    show odette b_massage_leaning
    show grace b_massage_laying
    show odette_arms_massage_leaning_a_rub1_2
    show grace_sex_mc_foreground
    with dissolve
    anon "Halo wanita."

    show odette f_smirk
    grace f_surprised "!!!"
    odette "Lihat {b}Grace{/b}, {b}[firstname]{/b} ada di sini!"

    show odette b_massage
    hide odette_arms_massage_leaning_a_rub1_2
    show grace b_massage f_sad a_cover
    with dissolve
    grace "H-hai {b}[firstname]{/b}..."

    odette @ f_laugh "Bukankah dia menggemaskan saat dia sedang pemalu?"

    grace f_angry_back "aku tidak-"

    odette "Kamu tidak perlu menutup-nutupi, konyol... dia sudah melihat semuanya."

    grace f_sad @ -m_talk "..."
    odette "Aku bersumpah, kamu lebih tertekan daripada adik perempuanmu!"

    odette @ f_laugh "Ha ha ha!"

    pause
    odette "Anda ingin bergabung dengan kami?"

    return

label button_grace_livingroom_intro_no_threesome:
    scene location_tattoo_apartment_oil
    show grace b_massage_odette
    show grace_sex_mc_foreground
    with dissolve
    anon "Oh sial!"

    show grace b_massage f_surprised a_surprised
    show odette b_massage_laying_back behind grace_sex_mc_foreground
    with dissolve
    grace "!!!"
    show grace a_cover with dissolve
    anon f_worried "Maafkan aku, aku tidak bermaksud-"

    odette "Hei, kenapa kamu berhenti?!"

    show odette b_situp f_smirk
    with dissolve
    odette "Mmm, halo {b}[firstname]{/b}."

    grace f_angry_back "{b}Odette{/b}, tutupi!"

    odette "Oh, jangan konyol... dia sudah dewasa."

    if randomizer() > 50:
        show odette a_pussy
    else:
        show odette a_squeeze
    with dissolve
    odette "Lagi pula, aku tidak perlu merasa malu... benarkah, kawan?"

    show grace f_tired
    anon @ -m_talk a_behind_head "{i}*Meneguk*{/i}"

    anon "aku hanya-"

    anon "Hmm."

    grace "{b}Eve{/b} ada di kamar tidurnya."

    anon f_surprised "Y-ya, itu!"

    anon f_normal "Terima kasih!"

    odette a_idle "Mau bergabung dengan kami, {b}[firstname]{/b}?"

    grace f_surprised_back "{b}Odette{/b}, itu pacar kakakku!"

    odette "Jadi?"

    odette "Mungkin adikmu juga ingin bergabung dengan kami, pernahkah kamu memikirkan hal itu?"

    grace f_tired @ f_disgusted "Jangan kotor."

    odette @ f_eyeroll "Kalian berdua sangat tertekan."

    show odette b_massage_laying_back f_normal with dissolve
    odette "Sebaiknya kau pergi, {b}[firstname]{/b} sebelum si pemalu menjadi terlalu tidak nyaman..."

    grace "Aku bukan orang yang pemalu!"

    grace "Aku hanya tidak ingin kamu merusak adikku!"

    odette "Ya benar."

    anon f_flirt_grin @ -m_talk "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
