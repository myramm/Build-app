label jenny_pregnancy_baby_need_anything:
    show anon f_normal
    anon "Kalian butuh sesuatu?"

    show jenny f_happy_down
    jenny "Tidak, kami baik-baik saja."

    jenny "Bukankah begitu?"

    jenny "Ya, benar!"

    jenny "Kami luar biasa!"

    return

label jenny_pregnancy_baby_looking_forward_daycare:
    show anon f_normal
    anon "Menantikan tempat penitipan anak?"

    show anon f_surprised
    show jenny f_angry
    jenny "Persetan tidak!"

    show jenny f_upset
    jenny "Aku benci memikirkan untuk meninggalkan mereka bersama orang asing."

    anon f_worried "Tidak akan asing lagi, {b}[jen_name]{/b}..."

    anon f_normal "{b}[deb_name]{/b} dan {b}Diane{/b} mengenal wanita yang mengelola tempat itu."

    anon "Kudengar dia sangat baik!"

    jenny "Aku tidak peduli apakah dia Mary Poppins, aku tidak suka meninggalkan anakku bersamanya!"

    anon "Heh, aku tidak pernah menganggapmu tipe ibu beruang..."

    show jenny f_happy_down
    jenny "Ya, baiklah... benar."

    anon f_laugh "Haha!"

    show anon f_normal
    return

label jenny_pregnancy_baby_leave:
    show anon f_normal
    anon "Aku akan meninggalkanmu."

    show jenny f_happy_down
    jenny "Ucapkan selamat tinggal pada {b}Ayah{/b}..."

    jenny "Sampai jumpa, {b}Ayah{/b}!"

    anon f_laugh "Hehe, sampai jumpa!"

    hide anon with dissolve
    return

label jenny_pregnancy_debbie_driving_crazy:
    show anon f_worried
    anon "{b}[deb_name]{/b} membuat Anda gila?"

    show jenny f_eyeroll
    jenny "Ya Tuhan, ya!!"

    show jenny f_upset
    anon "Bagaimana bisa?"

    jenny "Dia selalu mengikutiku kemana-mana, mencoba membuatku makan..."

    jenny "Itu menjengkelkan!!"

    anon "Itu hanya naluri keibuannya yang muncul, {b}[jen_name]{/b}."

    anon "Dia ingin menjaga putri dan cucunya."

    show jenny f_eyeroll
    jenny "Ya, ya, aku tahu."

    show jenny f_upset
    jenny "Aku hanya berharap dia tutup mulut tentang semua hal menjadi seorang nenek..."

    jenny "... Aku bersumpah, dia lebih ceria darimu dalam hal ini."

    anon f_normal "Hehe, menurutku itu manis."

    show jenny f_eyeroll
    jenny "Ugh, terserah."

    show jenny f_upset
    return

label jenny_pregnancy_can_i_get_you_something_3:
    show anon f_worried
    anon "Bolehkah aku memberimu sesuatu?"

    show jenny f_upset
    jenny "Seperti apa?!"

    anon f_normal "Entahlah, pijat kaki atau apa?"

    show anon f_grin
    show jenny f_gross
    jenny "Eww, tidak!"

    jenny "Aku bahkan tidak ingin memperlihatkan kakiku padamu sekarang, itu sangat besar!"

    anon f_flirt "Sungguh, aku tidak keberatan, kita hanya bisa-"

    jenny "Tidak!"

    anon f_skeptical "Oke, jangan menggosok kaki."

    show anon f_worried
    show jenny f_upset
    pause
    anon "Sesuatu untuk dimakan mungkin?"

    show jenny f_normal a_magic_sit_stand_belly_touch with dissolve
    jenny "Oh, itu akan luar biasa!"

    jenny "Tapi aku mendambakan hal-hal yang sangat aneh..."

    anon "Apa maksudmu?"

    show jenny f_upset
    jenny "Anda hanya akan menertawakan saya."

    anon f_normal "Tidak, aku tidak akan melakukannya."

    jenny @ -m_talk "..."
    anon "Saya berjanji!"

    show jenny f_sad
    jenny "Baiklah."

    show jenny f_eyeroll
    jenny "{i}*Huh*{/i} Kapur."

    show jenny f_sad
    anon f_shock "Apa?!"

    show anon f_surprised_teeth
    show jenny f_normal
    jenny "Aku tidak bisa menjelaskannya... Aku hanya ingin menggigit sebongkah besar kapur..."

    show jenny f_gross
    pause
    jenny "Aneh bukan?"

    anon "..."
    jenny "Apakah mereka membuat kapur yang bisa dimakan?"

    anon f_laugh "Ha ha ha!"

    show jenny f_angry a_magic_sit_stand_crossed with dissolve
    pause
    anon f_worried "Maafkan aku, aku hanya belum siap untuk-"

    jenny "Kamu bilang kamu tidak akan tertawa!"

    anon "Aku tahu, aku benar-benar minta maaf!"

    anon f_normal "Tidak, {b}[jen_name]{/b}, menurutku mereka tidak bisa membuat kapur yang bisa dimakan..."

    show jenny f_sad
    jenny "Hmmph, seharusnya begitu!"

    anon f_worried "Kamu benar-benar ingin makan kapur?!"

    jenny "Ya."

    show jenny f_grin a_magic_sit_stand_belly_touch with dissolve
    jenny "... Dan marshmallow."

    anon f_laugh "Oke, marshmallow pasti bisa kita buat."

    anon "Aku akan mengambilkanmu beberapa!"

    show anon f_normal
    show jenny f_normal
    jenny "Dengan acar!"

    anon f_surprised @ -m_talk "..."
    jenny "Oh, dan mustar!"

    anon f_worried "Eh, oke."

    show jenny f_eyeroll
    jenny "Tapi bukan mustard biasa."

    show jenny f_grin a_magic_sit_stand_crossed with dissolve
    jenny "Saya ingin barang Dijon yang mahal itu!"

    anon "B-benar."

    anon "Saya akan segera menyelesaikannya."

    anon @ -m_talk "(Ya Tuhan, itu sangat menjijikkan!!!)"

    return





label jenny_pregnancy_about_debbie:
    show anon f_worried
    anon "Tentang {b}[deb_name]{/b}..."

    show jenny f_grin
    jenny "Aku tidak percaya dia hampir mempercayai cerita omong kosong itu..."

    anon "Saya tidak mengerti mengapa kita tidak bisa mengatakan yang sebenarnya padanya?"

    show jenny f_angry
    jenny "Kamu ingin memberitahu ibuku bahwa kamulah ayahnya?!"

    jenny "Dia benar-benar akan marah, tolol!"

    anon "Menurutku dia tidak akan-"

    show anon f_surprised
    jenny "Tidak mungkin, {b}[firstname]{/b}!"

    anon f_worried "{b}[jen_name]{/b}..."

    jenny "SAYA BILANG TIDAK!"

    anon f_tired "{i}*Huh*{/i}"

    show anon f_worried
    return

label jenny_pregnancy_can_i_get_you_something:
    show anon f_worried
    anon "Bolehkah aku memberimu sesuatu?"

    show jenny f_eyeroll
    jenny "Ya, mesin waktu."

    show jenny f_upset
    anon f_confused "Hah?"

    show anon f_worried
    show jenny f_angry
    jenny "Jadi aku bisa kembali ke masa lalu dan membuatmu mundur!"

    show jenny f_gross
    anon @ -m_talk "..."
    return

label jenny_pregnancy_are_you_still_mad:
    show anon f_worried
    anon "Apakah kamu masih marah?"

    show jenny f_angry a_magic_sit_stand_crossed with dissolve
    jenny "Tentu saja aku marah, bodoh!"

    show jenny f_upset
    jenny "Apakah Anda sadar betapa besarnya biaya yang harus saya keluarkan untuk hal ini?"

    anon f_confused "Hah?"

    show anon f_worried
    jenny "Siapa yang akan menonton acaraku jika aku menjadi gemuk?!"

    anon "Anda tidak akan menjadi gemuk, {b}[jen_name]{/b}..."

    anon "... Dan bahkan jika Anda melakukannya, beberapa orang menyukainya."

    show jenny f_eyeroll
    jenny "Ugh, beberapa orang aneh yang kamu maksud."

    show jenny f_upset
    anon "Semuanya akan baik-baik saja, Anda akan lihat."

    show jenny f_phone_upset a_magic_sit_stand_phone with dissolve
    jenny "Apa pun."

    return

label jenny_pregnancy_leave:
    show anon f_worried
    anon "Aku akan meninggalkanmu."

    show jenny f_eyeroll
    jenny "Akhirnya sialan!"

    show jenny f_phone_upset
    anon "Anda akan memberi tahu saya jika Anda butuh sesuatu?"

    show jenny f_upset
    jenny "Ya, ya, aku akan memberitahumu."

    jenny "Pergilah."

    show jenny f_phone_upset
    anon f_tired "{i}*Huh*{/i}"

    hide anon with dissolve
    return

label jenny_pregnancy_you_doing_ok_1:
    show anon f_worried
    anon "Kamu baik-baik saja?"

    show jenny f_phone_upset
    jenny "Saya baik-baik saja."

    pause
    anon "Anda yakin?"

    anon "K-kita bisa membicarakannya, jika kamu-"

    show anon f_surprised
    if randomizer() > 50:
        show jenny f_angry
        jenny "Ya Tuhan, diamlah!"

        jenny "Ibuku mungkin mendengarmu, tolol!"

        anon f_worried "Aku hanya mengatakan-"

        show jenny f_eyeroll
        jenny "Saya tahu apa yang Anda katakan, {b}[firstname]{/b}!"

        show jenny f_upset
        jenny "Serius, aku baik-baik saja!"

    else:
        show jenny f_upset
        jenny "Aku bilang aku baik-baik saja, {b}[firstname]{/b}!"

    jenny "Jatuhkan itu."

    show jenny f_phone_upset
    anon "O-oke."

    return

label jenny_pregnancy_you_doing_ok_2:
    show anon f_worried
    anon "Kamu baik-baik saja?"

    show jenny f_gross
    jenny "Tidak, aku tidak baik-baik saja!"

    jenny "Semua ini menyebalkan!"

    anon "Ada apa?!"

    show jenny f_eyeroll
    jenny "Hmm, baiklah, mari kita lihat..."

    show jenny f_gross
    jenny "... Sebagai permulaan, aku muntah-muntah setiap pagi."

    jenny "Lalu aku makan seperti sapi karena anak idiotmu bertekad membuatku gemuk."

    show jenny f_upset
    anon "{b}[jen_name]{/b}..."

    jenny "Saya merasa tidak nyaman, hampir sepanjang hari."

    show jenny f_angry
    jenny "Oh, dan sekarang saya bangun dan buang air kecil empat kali dalam semalam!"

    show jenny f_gross
    anon "Saya minta maaf?"

    show jenny f_angry
    jenny "Anda seharusnya menyesal!"

    jenny "Ini semua salahmu, brengsek!"

    show jenny f_gross
    return

label jenny_pregnancy_you_doing_ok_3:
    show anon f_worried
    anon "Kamu baik-baik saja?"

    show jenny f_gross
    jenny "Tidak, aku tidak baik-baik saja!"

    show jenny f_angry a_magic_sit_stand_belly_touch with dissolve
    jenny "Lihat saja apa yang kamu lakukan padaku, {b}[firstname]{/b}!"

    jenny "Aku seekor paus sialan!"

    anon "Anda bukan ikan paus, {b}[jen_name]{/b}..."

    show jenny f_sad
    jenny "Ya, benar!"

    anon f_normal "Tidak, kamu cantik..."

    jenny "Cantik?!"

    show anon f_worried
    show jenny f_angry
    jenny "Apa yang kamu, terbelakang?!"

    anon "Anda sedang mengandung anak kami... Menurut saya itu indah."

    show jenny f_eyeroll a_magic_sit_stand_crossed with dissolve
    jenny "Ya Tuhan, kamu yang terburuk!"

    show jenny f_sad
    pause
    jenny "Aku hanya ingin hal ini keluar dari diriku!"

    return

label jenny_button_pregnancy_stage_1:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
        show anon b_dinner_sitting_look_left f_normal zorder 1
    else:
        scene expression player.location.background_closeup
        show anon f_normal zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    anon "Hai."

    show anon f_worried
    jenny @ -m_talk "..."
    return

label jenny_button_pregnancy_stage_2:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
        show anon b_dinner_sitting_look_left f_normal zorder 1
    else:
        scene expression player.location.background_closeup
        show anon f_normal zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    with dissolve
    anon "Hai, {b}[jen_name]{/b}."

    show jenny f_eyeroll
    jenny "Ugh, kamu mau apa, {b}[firstname]{/b}?"

    show jenny f_gross a_magic_sit_stand_crossed with dissolve
    return

label jenny_button_pregnancy_stage_3:
    if player.location == L_home_diningroom:
        scene expression game.timer.image("dining_room{}")
        show expression "characters/jenny/layeredimage/jenny_breakfast_table.png" zorder 2
        show anon b_dinner_sitting_look_left f_worried zorder 1
    else:
        scene expression player.location.background_closeup
        show anon f_worried zorder 1
    show jenny f_phone_upset a_magic_sit_stand_phone b_magic_sit_stand_dressed zorder 1
    anon "Hai, {b}[jen_name]{/b}."

    show jenny f_surprised a_magic_sit_stand_crossed with dissolve
    jenny "Sial, kamu membuatku takut!"

    show jenny f_upset
    jenny "Aku pikir kamu adalah ibuku..."

    jenny "... Dia membuatku gila."

    show jenny f_gross
    return

label jenny_button_pregnancy_holding_baby:
    scene expression player.location.background_closeup
    $ player.last_baby_gender = M_jenny.pregnancy.baby_gender
    show jenny a_baby b_casual f_happy_down
    show anon f_normal with dissolve
    jenny "Kamu sangat cantik, bukan, anak kecil?!"

    jenny "Kamu pasti mendapatkan penampilanmu dari ibumu."

    jenny "Beruntung sekali karena ayahmu pada dasarnya adalah seorang troll jembatan."

    anon f_worried "Hei!"

    show jenny f_laugh
    jenny "Hahahaah!"

    show jenny f_happy_down
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
