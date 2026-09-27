label button_eve_sexy_time:
    scene expression player.location.background_blur with None
    show anon with dissolve
    anon "Hei kamu."

    eve "!!!"
    show eve b_undies f_happy
    with dissolve
    eve "Aku sudah menunggumu!"

    anon "Oh?"

    anon "Apa yang terjadi-"

    hide anon
    show eve b_undies_kiss
    with dissolve
    anon "!!!"
    pause
    show anon
    show eve b_undies f_happy
    with dissolve
    anon "Heh, kamu hanya ingin langsung membahasnya, ya?"

    eve f_sexy "Ya!"

    pause
    eve "Naiklah ke tempat tidur."

    anon @ a_behind_head "O-oke."

    scene expression player.location.background_closeup with None
    show anon b_onbed_sit f_flirt
    show eve f_sexy b_onbed_top_remove3 with dissolve
    with dissolve
    pause
    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve
    pause
    show anon b_onbed_sit_changing3 with fastdissolve
    pause
    hide anon
    show eve b_onbed_cuddle_naked_kiss o_dick
    with dissolve
    eve "MM."

    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    pause
    anon "Wow, kamu agresif sekali malam ini!"

    eve "Hehe, maaf."

    pause
    eve "Anda tahu, {b}[firstname]{/b}, saya sedang berpikir..."

    pause
    eve "... Kamu seperti, orang yang paling menakjubkan di dunia."

    anon "Aku tidak tahu tentang itu..."

    eve "Tidak, aku serius!"

    eve "Kamu pintar, lucu, baik hati, bijaksana..."

    pause
    eve "Dan sungguh, BENAR-BENAR, panas!"

    anon "Haha, kamu pikir aku seksi?"

    eve "Duh!"

    pause
    eve "A-dan aku ingin kamu menjadi yang pertama bagiku..."

    anon f_worried_low "Yang pertama?"

    pause
    anon "Pertamamu apa?"

    eve @ f_thinking_down "Cih."

    eve "Saya bertanya apakah Anda ingin berhubungan seks dengan saya, {b}[firstname]{/b}..."

    anon @ f_surprised "!!!" with hpunch
    anon "Benar-benar?!"

    eve f_thinking_down "Maksudku, kita tidak perlu... Aku hanya berpikir-"

    anon f_flirt_low "Tentu saja aku tahu!"

    eve f_happy "Ya?"

    anon "Tentu saja."

    eve "Hehe, bagus!"

    $ M_eve.set('sex speed', .4)
    show eve a_jerk o_empty with dissolve
    pause
    anon "Sekarang?"

    eve "Sekarang."

    anon "{i}*Gulp*{/i} Oke."

    jump eve_sex_back_first_intro

label button_eve_maybe_another_time:
    anon f_worried "Aku ingin sekali, tapi kelasku tertinggal jauh... Itu mungkin ide yang buruk."

    eve f_sad_down "Ya, saya mengerti."

    pause
    eve f_happy "Kami akan melakukannya lain kali."

    anon f_normal "Untuk ya."

    return

label button_eve_nevermind_roof:
    anon f_worried "Aku mungkin harus pulang."

    eve f_normal "Senang bertemu denganmu, {b}[firstname]{/b}."

    anon "Ya, kamu juga."

    eve "Nanti."

    anon @ a_wave "Sampai jumpa, {b}Malam{/b}."

    hide anon with dissolve
    return

label button_eve_ill_be_there:
    anon "Saya akan berada di sana."

    eve @ f_laugh "Ya, hehe!"

    eve f_sexy "Kita bisa masuk ke kamarku dan {i}waktu sendirian{/i}, jika kamu mengerti maksudku?"

    anon f_flirt "Waktunya sendiri, ya?"

    eve @ -m_talk "Mmhmm."

    anon "Saya suka suaranya."

    eve "Saya pikir Anda mungkin melakukannya."

    return

label button_eve_how_are_odette_and_grace:
    anon "Bagaimana {b}Odette{/b} dan {b}Grace{/b}?"

    eve "Oh, mereka baik-baik saja!"

    eve "{b}Grace{/b} memiliki lebih banyak waktu luang sejak {b}Odette{/b} mulai membantu, dan kami sebenarnya menghabiskan waktu bersama {b}di malam hari{/b}."

    anon @ f_laugh "Itu luar biasa!"

    eve "Ya, benar."

    eve @ f_eyeroll "Sekarang jika saya bisa membuat mereka berhenti berhubungan seks di seluruh rumah, segalanya akan menjadi sempurna."

    anon f_surprised "S-seks?"

    eve @ f_eyeroll "Ya, maksudku, di mana-mana... Dan mereka tidak punya rasa malu!"

    eve f_angry "Kemarin aku berjalan masuk saat adikku sedang menjilati benda kotor {b}Odette{/b} di dapur kami!"

    anon f_flirt "B-benarkah?"

    eve "Dia telanjang bulat di atas meja dan segalanya!"

    anon "{i}*Gulp*{/i} Kedengarannya... Umm... Menjengkelkan?"

    eve "Ini sangat menjengkelkan."

    eve "Saya biasa makan pop-tart saya di sana!"

    eve f_sad "{i}*Huh*{/i}"

    eve "Tidak lagi..."

    show anon f_flirt_grin
    pause .5
    show anon f_normal
    return

label button_eve_nah_i_like_to_watch_you:
    anon f_worried "Tidak, aku suka memperhatikanmu."

    eve f_surprised "Anda suka memperhatikan saya, ya?"

    anon f_normal "Itu menyenangkan."

    eve f_sexy "Anda tahu, di luar konteks, kedengarannya sangat kotor..."

    anon f_confused @ -m_talk "Hmm?"

    eve @ f_laugh "Hehe, sudahlah."

    eve "Ayo duduk."

    show anon f_normal
    eve "Aku akan menaikkan peringkat {b}Cindel{/b}ku."

    anon @ f_confused "Apa itu gadis bertangan empat?"

    eve "Bukan, dialah yang berteriak dan memiliki rambut seperti {b}Odette{/b}."

    anon "Oh benar."

    anon @ f_laugh "Dingin!"


    scene location_tattoo_bedroom_cutscene06
    show text _ ("It was fun watching {b}Eve{/b} beat up on someone else for a change...\nShe almost never lost a match.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Those online players didn't stand a chance against her!") as caption with dissolve
    pause

    scene expression player.location.background_blur
    show anon
    show eve b_undies f_happy
    with fade
    eve "Sedang apa aku sekarang?"

    anon "Lima puluh tiga kemenangan dan dua kekalahan..."

    eve f_surprised "Lima puluh tiga?!"

    eve f_normal "Ya Tuhan, jam berapa sekarang?"

    anon "Sekarang jam setengah sepuluh."

    eve f_happy @ f_eyeroll "Aduh, kawan... Aku benar-benar lupa waktu!"

    anon "Ya, aku mungkin harus mulai pulang."

    eve f_sad_down "Maaf kami tidak melakukan sesuatu yang nakal..."

    anon "Tidak apa-apa."

    anon "Saya senang melihat Anda memukuli orang secara online!"

    eve f_sad "Aku akan menebusnya lain kali, oke?"

    anon @ f_laugh "Tentu, tidak sabar!"

    eve f_happy @ f_laugh "hehe!"

    hide anon
    show eve b_undies_kiss1
    with dissolve
    pause
    show eve b_undies
    show anon
    with dissolve
    eve "Sampai jumpa besok?"

    anon "Tentu saja."

    eve "Selamat malam, {b}[firstname]{/b}."

    anon @ a_wave "Selamat malam, {b}Malam{/b}."

    hide anon with dissolve
    return

label button_eve_i_should_go:
    anon f_worried "Sial, aku baru ingat."

    eve @ -m_talk "Hmm?"

    anon "Aku seharusnya berada di suatu tempat."

    eve f_sad "Anda akan pergi?"

    anon "Ya maaf."

    anon "Pemeriksaan hujan saat sendirian?"

    eve f_sad_down "Y-ya, oke."

    anon "Terima kasih."

    hide anon
    show eve b_undies_kiss1
    with dissolve
    pause
    show eve b_undies
    show anon
    with dissolve
    anon "Ngomong-ngomong, kamu terlihat luar biasa!"

    eve f_happy @ f_laugh "Hehe, terima kasih!"

    anon @ a_wave "Aku akan menemuimu nanti, oke?"

    eve "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return

label button_eve_how_come_not_at_the_park:
    anon "Kenapa kamu tidak ada di taman?"

    eve f_sad_down @ f_eyeroll "{b}Grace{/b} tidak ingin aku berada di sana lagi setelah gelap."

    anon f_worried "Oh."

    anon "Masalah narkoba?"

    eve "Ya."

    pause
    eve f_normal @ a_point "Sisi baiknya, saya tidak perlu khawatir tentang {b}Tyrone{/b} dan teman-teman bajingannya yang mengganggu saya di sini."

    anon @ f_laugh "Hehe, itu benar."

    eve "Mungkin saya benar-benar bisa menyelesaikan beberapa gambar."

    return

label button_eve_business_doing_any_better:
    anon "Bisnis menjadi lebih baik?"

    eve f_happy "Ya, selebaran itu sukses besar!"

    eve "Kami memiliki lebih banyak pelanggan yang datang sejak Anda membagikannya."

    anon "Itu luar biasa!"

    return

label eve_dialogue_intro_roof:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon "{b}Malam{/b}?"

    eve @ f_laugh "Hai, {b}[firstname]{/b}!"

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    anon "Apa yang kamu lakukan di sini?"

    eve "Oh, hanya orang-orang yang menonton..."

    anon "Temukan sesuatu yang menarik?"

    eve f_normal @ f_eyeroll "Tidak, tidak juga."

    eve "Ugh, kota ini terkadang sangat membosankan..."

    return

label button_eve_art_project:
    anon "Jadi {b}Nona Ross{/b} senang dengan gambar yang kita buat bersama?"

    eve f_happy @ f_laugh "Yup, dia menyukainya!"

    eve "Memberiku pidato panjang tentang betapa bangganya dia telah membantuku menemukan kecantikan batinku..."

    anon @ f_confused "Itu umm... Hebat?"

    eve "Saya senang akhirnya selesai dan saya bisa menggambar sesuatu selain potret diri untuk sementara waktu!"

    eve @ f_eyeroll "Sumpah, wanita itu lebih gila dari kotoran tupai!"

    anon @ f_laugh "{i}*Mendengus*{/i} Haha!"

    return

label button_eve_hows_everyone_at_home:
    anon "Bagaimana kabar semua orang di rumah?"

    eve f_normal "Oh, tahukah Anda... Sama saja, sama lamanya."

    eve "{b}Grace{/b} bekerja terlalu keras dan khawatir dengan tagihan."

    eve "{b}Tuuku{/b} melakukan yang terbaik untuk memastikan semua kepala pot di Summerville mendapatkan perbaikannya."

    eve "Dan {b}Odette{/b} membeli seluruh seri {i}False Blood{/i}, dan menontonnya secara berlebihan di toko setiap hari."

    anon f_surprised "{i}Darah Palsu{/i}?"

    eve @ f_eyeroll "Ya, itu acara tentang vampir seksi."

    eve "BANYAK ketelanjangan jadi, tentu saja, dia menyukainya."

    anon f_flirt "Ya, itu masuk akal."

    show anon f_normal
    return

label button_eve_something_simple:
    anon @ f_confused "Sesuatu yang sederhana?"

    eve "Terakhir kali dia menyuruh kami melukis hanya dengan menggunakan kaki kami."

    anon f_surprised "Dengan serius?"

    eve @ f_eyeroll "Ya, katanya itu akan membuka cakra kita dan membawa keseimbangan pada jiwa kita atau semacam omong kosong..."

    eve "Saya pikir dia hanya memiliki fetish kaki."

    anon f_normal @ f_laugh "Haha!"

    return

label button_eve_you_look_nice_today:
    anon f_flirt "Kamu terlihat cantik hari ini!"

    eve @ f_eyeroll "Diam."

    anon f_normal "aku serius!"

    eve "Tapi aku memakai pakaian yang sama persis dengan yang selalu kupakai..."

    anon "Ya, dan kamu selalu terlihat cantik!"

    eve f_nervous_down "Ayo, hentikan..."

    anon "Itu kebenarannya!"

    return

label button_eve_nevermind_park:
    anon f_worried "Aku mungkin harus pulang."

    eve f_normal "Ya, saya sendiri akan segera melakukan hal yang sama."

    anon "Hati-hati di sini, oke?"

    eve "Aku akan menjadi."

    anon @ a_wave "Nanti."

    hide anon with dissolve
    return

label button_eve_should_find_a_new_spot:
    anon f_confused "Sudahkah Anda mempertimbangkan untuk mencari tempat baru untuk nongkrong?"

    eve f_angry "Kenapa aku yang harus pergi?"

    eve f_angry_right "Aku di sini dulu!"

    show anon f_worried
    chico "Sekarang dia semua marah..."

    chad "Haha!"

    tyrone "Mengapa kamu tidak membawa pantatmu ke sini dan berbagi doobie dengan kami?"

    eve "Persetan denganmu!"

    tyrone "Ya, saya yakin Anda akan menyukainya, ya?"

    tyrone "Kami bisa menjalankan kereta untukmu sepanjang malam."

    show anon f_shock
    eve @ f_disgusted_wince_down "Ya."

    eve "Kamu menjijikkan!"

    show eve f_angry
    anon @ -m_talk "..."
    show anon f_worried
    return

label button_eve_hallway_really:
    anon f_worried "Benar-benar?"

    eve "Ya, aku ingin tapi kakakku akan membunuhku jika dia tahu, jadi..."

    eve f_nervous "... Mungkin bukan ide yang bagus."

    anon f_normal @ a_behind_head "Hehe, ya... Mungkin tidak."

    return

label button_eve_nevermind_school:
    anon f_normal "Saya mungkin harus bersiap-siap untuk kelas."

    eve f_normal "Ya, aku juga."

    anon "Aku akan bicara denganmu nanti, oke?"

    eve "Ya, nanti."

    hide anon with dissolve
    return

label button_eve_how_are_things_at_the_shop:
    anon f_normal "Bagaimana keadaan di toko?"

    eve "Mm, semuanya baik-baik saja, menurutku..."

    pause
    eve f_nervous_down "Saya berharap {b}Grace{/b} tidak perlu bekerja terlalu keras tetapi tidak ada yang bisa dilakukan."

    show anon f_worried
    eve "Kami tidak mampu mempekerjakan siapa pun, dan dia menolak membiarkan saya membantu!"

    anon "Ya, itu menyebalkan."

    return

label button_eve_street_kombat_rematch:
    anon f_snarky "Saya masih menginginkan pertandingan ulang itu!"

    eve f_normal "Hei, aku siap menendang pantatmu kapan saja kamu mau..."

    anon "Nah, aku pasti akan menemuimu lain kali!"

    eve @ f_laugh "Hehe, tentu saja."

    return

label button_eve_you_still_drawing:
    anon f_normal "Kamu masih menggambar?"

    eve @ f_eyeroll "Ugh, aku lebih banyak fokus pada proyek bodoh ini untuk {b}Nona Ross{/b}..."

    anon "Oh ya?"

    eve "Aku sudah menyerahkan enam gambar berbeda, dan dia terus memaksaku mengulanginya!"

    anon f_surprised "Dengan serius?"

    eve "Ya, wanita itu gila!"

    pause
    anon f_normal "Apakah ada yang bisa saya lakukan untuk membantu?"

    eve "Nah, saya menghargai tawaran itu tetapi tidak ada yang bisa dilakukan."

    eve f_sad_down "Aku mungkin akan meninggalkan kelasnya..."

    anon f_shock "Apa?!"

    anon f_worried "Tapi menurutku kamu suka menggambar?"

    eve "Ya, tapi dia menghilangkan semua kesenangannya..."

    anon @ -m_talk "..."
    return

label button_eve_love_the_hair:
    anon f_normal "Sudahkah aku menyebutkan aku menyukai rambut barumu?"

    eve a_hair f_nervous_down "Hehe, ya... Ya, pernah."

    anon "Itu terlihat sangat bagus untukmu!"

    eve "Terima kasih, {b}[firstname]{/b}."

    eve f_normal a_idle @ f_happy_right "Senang rasanya mendengarnya!"

    return

label eve_dialogue_intro_bedroom:
    scene expression player.location.background_closeup with None
    show anon
    with dissolve
    anon "{b}Malam{/b}?"

    show eve b_undies f_happy
    with dissolve
    eve "{i}*Terkesiap*{/i} Anda di sini!"

    hide anon
    show eve b_undies_kiss
    with dissolve
    pause
    show eve b_undies
    show anon
    with dissolve
    anon "Hehe, aku di sini."

    anon "Anda sedang bermain game?"

    eve @ -m_talk "Hmm?"

    eve "Oh, saya baru saja melakukan beberapa pertandingan online {i}Street Kombat{/i}."

    anon "Bisakah saya menonton?"

    eve @ f_eyeroll "Umm, ya... kurasa."

    eve f_sexy "Bukankah Anda lebih suka melakukan hal lain?"

    return

label eve_dialogue_intro_classroom_e1e12:
    scene expression player.location.background_closeup with None
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk
    with dissolve
    anon "Pagi, {b}Malam{/b}."

    eve "Hai, {b}[firstname]{/b}."

    anon "Bekerja keras?"

    eve "Hehe, ya benar..."

    eve @ f_eyeroll "Kelas ini SANGAT membosankan!"

    return

label eve_dialogue_intro_classroom_e13e20:
    scene expression player.location.background_closeup with None
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk
    with dissolve
    anon "Pagi, {b}Malam{/b}."

    eve "Hai, {b}[firstname]{/b}!"

    anon "Siap untuk hari sekolah yang menyenangkan lainnya?"

    eve @ f_eyeroll "Heh, ya... \"Menyenangkan.\""

    eve "Aku harap kita bisa melewatkannya dan nongkrong di tempatku."

    anon "Ya, aku juga."

    return

label eve_dialogue_intro_classroom_e21:
    scene expression player.location.background_closeup with None
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk
    with dissolve
    anon "Pagi, {b}Malam{/b}."

    eve "Hai, {b}[firstname]{/b}!"

    hide anon
    show eve b_dressed_kiss:
        xoffset -300
    show expression "characters/eve/eve_overlay_o_chair.png" zorder 1:
        xpos 450
    show expression "characters/eve/eve_overlay_o_desk.png" zorder 2:
        xpos 500
    show expression "characters/eve/eve_overlay_o_chair.png" as anon_chair zorder 1:
        xpos -50
    show expression "characters/eve/eve_overlay_o_desk.png" as anon_desk zorder 3:
        xpos 0
    with dissolve
    pause
    eve "MM."

    hide eve
    hide anon_desk
    hide anon_chair
    hide expression "characters/eve/eve_overlay_o_desk.png"
    hide expression "characters/eve/eve_overlay_o_chair.png"
    show eve b_desk_look_left f_happy:
        xoffset 500
    show anon b_desk f_flirt
    with dissolve
    anon "Hmm, itu bagus."

    eve @ f_laugh "hehe!"

    eve @ f_eyeroll "Ugh, aku sedang tidak mood untuk mengikuti kelas hari ini."

    eve "Anda ingin melewatkan dengan saya?"

    anon f_worried "Entahlah, mungkin."

    eve "Aww, ayolah... Tolong?"

    eve "Membosankan sekali kalau kamu tidak ada!"

    return

label eve_dialogue_intro_hallway_e1e12:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon @ a_wave "Sore, {b}Malam{/b}."

    eve @ a_wave "Hai, {b}[firstname]{/b}."

    anon "Apa yang terjadi?"

    eve f_nervous_down "Eh, tidak banyak."

    eve "Hanya berpikir untuk melewatkan kelas {b}Nona Ross{/b}'..."

    return

label eve_dialogue_intro_hallway_e13e20:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon @ a_wave "Sore, {b}Malam{/b}."

    eve "Hai, {b}[firstname]{/b}!"

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    anon "Anda menuju ke kelas {b}Miss Ross{/b}'?"

    eve f_normal "Sayangnya ya."

    eve "Sobat, kuharap dia merencanakan sesuatu yang sederhana hari ini..."

    return

label eve_dialogue_intro_hallway_e21:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    anon @ a_wave "Sore, {b}Malam{/b}."

    eve "Hai, {b}[firstname]{/b}!"

    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    pause
    show eve b_dressed:
        xoffset 0
    show anon
    with dissolve
    anon "Hmm, itu bagus."

    eve @ f_laugh "hehe!"

    eve "Apakah kamu akan datang malam ini?"

    anon "Entahlah, mungkin."

    eve @ f_eyeroll "Aww, ayolah... Tolong?"

    eve "Membosankan sekali kalau kamu tidak ada!"

    return

label eve_dialogue_intro_park_e1e12:
    scene expression player.location.background_closeup with None
    show anon f_worried with dissolve
    anon "{b}Malam{/b}?"

    pause
    anon f_angry "Bisakah kamu mendengarku?!"

    eve "Hmm?"

    eve "Oh, hai {b}[firstname]{/b}!"

    show anon f_shock
    show eve b_dressed_headphones_up with dissolve
    show anon f_normal
    pause
    show eve b_dressed_hoodless a_hoodless_remove_headphones with dissolve
    eve "Maaf."

    show eve b_dressed_headphones_down a_idle with dissolve
    anon "Apa aku mengganggumu?"

    eve "Tidak, tidak sama sekali."

    eve @ f_eyeroll "Aku hanya mencoba meredam musik rap jelek ini!"

    tyrone "Psh, jangan main-main cewek... Kamu tahu kamu menyukainya!"

    eve f_angry_right "Brengsek sialan..."

    eve f_normal "Jadi, ada apa?"

    return

label eve_button_eve_six6nine9_time:
    scene expression player.location.background_closeup with None
    show anon with dissolve
    anon "Hei kamu."

    eve "!!!"
    show eve b_undies f_happy
    with dissolve
    eve "Hai, {b}[firstname]{/b}!"

    anon "Anda sedang bermain game?"

    eve "Ya."

    pause
    eve f_sexy "Tapi sekarang kamu di sini..."

    hide anon
    show eve b_undies_kiss
    with dissolve
    anon "!!!"
    pause
    show anon
    show eve b_undies f_happy
    with dissolve
    eve "Apakah kamu ingat malam itu di tenda... Saat kamu, umm-"

    eve "... Membuatku cum?"

    anon f_flirt "Ya?"

    eve "Bisakah kita, mungkin... Lakukan itu lagi?"

    menu:
        "Tentu saja.":
            anon a_thinking f_thinking "Hmm, biarkan aku memikirkannya."

            eve f_nervous @ -m_talk "..."
            show anon f_flirt_grin a_idle with dissolve
            pause
            anon f_flirt @ a_point "Tentu saja kita bisa!"

            eve f_sexy @ f_laugh "hehe!"

            eve "Naiklah ke tempat tidur, {b}[firstname]{/b}."

        "NERAKA YA!":

            anon @ f_laugh "Oh, kami bisa melakukan apapun yang kamu mau {b}Eve{/b}!"

            eve "Hehe, baiklah."

            eve f_thinking_down "Hmm."

            pause
            eve f_sexy "Mengapa saya tidak mengambil sedikit minyak pijat saudara perempuan saya, dan kita lihat berapa banyak minyak yang bisa muat di pantat Anda?"

            anon f_shock "!!!"
            anon f_worried "I-itu bukan-"

            anon "aku tidak bermaksud-"

            eve @ f_laugh "Hahaha!!"

            eve "Aku hanya bercanda... Sobat, kamu seharusnya melihat wajahmu!"

            anon f_shy @ a_behind_head "Sangat lucu."

            eve "Naiklah ke tempat tidur, {b}[firstname]{/b}."


    anon "Baiklah."

    scene expression player.location.background_closeup with None
    show anon b_onbed_sit f_flirt
    show eve b_onbed_tanktop f_sexy
    with dissolve
    eve "Saya rasa saya tidak membutuhkan pakaian ini lagi, bukan?"

    anon "Tidak uh."

    eve @ f_laugh "hehe."

    show eve b_onbed_top_remove3 with dissolve
    pause
    show eve b_onbed_top_remove4 with dissolve
    pause
    show eve f_sexy b_onbed_nude with dissolve
    eve "Di sana."

    eve "Giliranmu."

    show anon b_onbed_sit_changing3 with fastdissolve
    pause
    hide anon
    show eve b_onbed_cuddle_naked_kiss o_dick
    with dissolve
    pause
    show eve b_onbed_cuddle_naked f_happy
    show anon b_empty_eve_onbed_cuddle f_flirt_low zorder 1
    with dissolve
    eve "Mmm, aku suka menciummu!"

    anon "Y-ya, juga."

    pause
    $ M_eve.set('sex speed', .4)
    show eve a_jerk o_empty with dissolve
    eve f_thinking_down "Aku bahkan tidak bisa menyentuh penismu dengan jariku!"

    anon "Sudah kubilang, itu hanya tangan kecilmu."

    eve f_happy "Hehehe, entahlah.."

    pause
    eve "Bisakah kita mencoba sesuatu?"

    anon "Um, entahlah..."

    anon "Menurutku itu tergantung pada apa itu?"

    show eve a_jerk1
    eve "Tenang saja, tidak ada yang aneh..."

    anon "B-benarkah?"

    eve "Pernahkah Anda mendengar tentang posisi enam puluh sembilan?"

    if M_eve.get("biggus_dickus"):
        eve "Aku akan menindihmu dan kita berdua akan menggunakan mulut kita."

        anon "Kamu ingin memasukkan penismu ke dalam mulutku?"

    else:
        eve "Aku akan menindihmu dan memasukkanmu ke dalam mulutku, sementara kamu menggunakan lidahmu padaku."

        anon "Anda ingin saya menjilat vagina Anda?"

    eve "Ya, hanya jika Anda mau?"

    anon @ -m_talk "..."
    eve "Jika itu membuatmu takut, aku bisa merendahkanmu seperti biasa?"

    return

label eve_button_party_start:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk
    with dissolve
    eve "Anda masih datang ke pesta {b}Sabtu malam ini{/b}, kan?"

    anon "Ya, aku akan berada di sana."

    eve "Ini akan menjadi sangat luar biasa!"

    eve "Adikku dan {b}Odette{/b} mengadakan pesta terbaik!"

    anon @ f_laugh "Hehe, tidak sabar!"

    return

label eve_button_talked_to_eve:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show eve a_beer_hold
    with dissolve
    eve "Aku penasaran kenapa {b}Odette{/b} lama sekali?"

    anon "Dia bilang dia akan menutup tokonya, kan?"

    show anon a_beer_drink f_smoke with dissolve
    eve "Ya, tapi {b}Grace{/b} hanya memiliki dua pelanggan hari ini..."

    show anon a_beer f_normal with dissolve
    eve "Seharusnya dia tidak membutuhkan waktu selama ini."

    hide anon with dissolve
    return

label eve_button_eve_talked_to_both_girls:
    odette "Baiklah, jalang..."

    scene expression player.location.background_blur
    show odette a_whiskey_yay f_laugh zorder 1:
        xoffset 100
    with fade
    odette "Siapa yang siap berpesta?!"

    show anon a_beer zorder 1:
        xoffset -150
    show eve f_happy a_beer_hold zorder 0:
        flip
        xoffset 100
    show grace a_beer f_normal_back zorder 0:
        xoffset -150
    with dissolve
    odette f_moo "WOOOOOO!!!"

    eve f_happy @ f_moo "WOOOOOO!!!"

    show odette f_smirk a_whiskey with dissolve
    grace "Tolong jangan terlalu gila..."

    odette "Uh oh, sepertinya seseorang butuh tembakan bola api!"

    grace f_sad @ f_surprised_back "Sama sekali tidak!"

    eve f_sad "Aduh, ayolah {b}Grace{/b}..."

    show grace f_sad_back
    odette "Ya, ayolah {b}Grace{/b}!"

    odette "Jangan menjadi pengacau pesta!"

    grace "{i}*Huh*{/i} Baiklah, berikan di sini..."

    show eve f_happy
    show odette a_whiskey_pour with dissolve
    odette "Itu gadisku!"

    show odette a_whiskey
    show grace a_shot_drink f_proud m_talk
    with dissolve
    odette "Minumlah obatmu."

    show grace a_shot f_disgusted_wince -m_talk with dissolve
    grace "Ya Tuhan..."

    grace "{i}*Batuk* *Batuk*{/i}"

    grace f_happy "Sudah lama sejak saya mengalami semua itu!"

    odette "Sialan, ya?"

    eve "Bolehkah saya mencobanya?!"

    grace f_normal "Tidak, menurutku sebaiknya kamu tetap minum bir-"

    odette "Tentu saja, Anda dapat memilikinya!"

    grace f_sad_back @ f_surprised_back "{b}Odette{/b}!"

    show odette a_whiskey_pour with dissolve
    odette "Apa?!"

    show eve a_shot
    show odette a_whiskey
    with dissolve
    odette "Kami lebih muda darinya ketika kami mulai meminum minuman ini..."

    odette "... Dan hanya kami yang ada di sini."

    show eve a_shot_drink f_drink with dissolve
    odette "Hal terburuk apa yang bisa terjadi?"

    show eve a_shot f_disgusted with dissolve
    show grace f_surprised
    eve "{i}*Batuk* *Batuk*{/i}"

    show grace f_sad
    show eve f_sexy
    eve "H-sialan..."

    eve "Benda itu benar-benar terbakar!"

    odette "Mmhmm, begitulah cara Anda mengetahui itu berhasil."

    odette "Kamu mau, kawan?"

    show anon f_worried
    eve f_happy_right "Oh, dia ingin beberapa!"

    anon "Ehh, t-tentu... kurasa."

    show odette a_whiskey_pour with dissolve
    show eve f_happy
    show grace f_sad_back
    odette "Segera hadir, baiklah Pak!"

    show grace f_sad
    show anon a_shot
    show odette a_whiskey
    with dissolve
    eve f_happy_right @ f_laugh "Haha!"

    show anon a_shot_drink f_smoke with dissolve
    pause
    anon a_shot f_disgusted_down @ f_cough "!!!"
    grace "Anda baik-baik saja, {b}[firstname]{/b}?"

    anon "Eugh, tuan yang baik!"

    anon "Apa itu?"

    show anon f_worried
    show eve f_happy
    odette "Wiski kayu manis."

    show eve f_happy_right
    anon "Ini mengerikan!"

    show eve f_happy
    odette @ f_laugh "Haha!"

    grace @ f_sad_back "Apakah kamu mengunci semuanya di bawah?"

    eve f_sad "Maukah kamu berhenti khawatir dan bersenang-senang?!"

    grace f_sad "Aku hanya ingin memastikan-"

    show grace f_sad_back
    odette "Ya, semuanya terkunci... Tenang."

    odette "Mengapa kita tidak bermain game atau apalah?"

    show eve f_happy
    grace f_sad @ f_surprised_back "Sebuah permainan?"

    show anon f_normal
    eve "Ya, ya, ya!"

    eve @ f_confused "Kebenaran atau Tantangan?"

    show grace f_sad_back
    odette @ f_eyeroll "Bukan, bukan Kebenaran atau Tantangan... Itu omong kosong!"

    show grace f_sad
    eve @ f_nervous_down "Uhh, aku tidak tahu banyak permainan minum..."

    grace f_normal "Saya Belum Pernah?"

    odette @ f_laugh a_whiskey_yay "Bingo!"

    anon @ f_confused "Hah?"

    grace f_happy "Hehe, ini permainan minum."

    eve "Bagaimana cara kerjanya?"

    show grace f_happy_back
    odette "Ini sangat mudah."

    odette "Yang harus Anda lakukan adalah mengakui sesuatu yang belum pernah Anda lakukan."

    odette "Misalnya:"

    odette "{i}*Ahem*{/i} Belum pernah..."

    odette @ f_laugh a_whiskey_yay "Melakukan masturbasi dengan sisir rambut!"

    show grace f_weary
    anon f_worried @ f_shock "!!!"
    eve @ f_laugh "APA?!"

    odette "Sekarang, siapa pun di sini yang TELAH melakukan masturbasi dengan sisir rambut, minumlah sedikit."

    grace f_tired_back "Kamu menyebalkan, kamu tahu itu?"

    odette @ f_laugh "Ha ha ha!"

    grace "Kamu suka mengungkit hal ini..."

    show grace a_shot_drink f_proud m_talk with dissolve
    eve @ f_surprised "Jadi tunggu sebentar, itu berarti-"

    show grace a_shot f_eyeroll -m_talk with dissolve
    grace "{i}*Sigh*{/i} Ya, saya melakukan masturbasi dengan sikat rambut beberapa kali, dulu ketika saya tinggal di rumah bersama {b}Ibu{/b} dan {b}Ayah{/b}."

    show grace f_normal
    anon f_surprised_teeth "!!!"
    eve @ f_laugh "Haha, kenapa?!"

    grace f_sad @ f_eyeroll "Uhh, karena aku terangsang dan tidak punya apa-apa lagi?"

    show anon f_flirt_grin
    show grace f_normal_back
    odette @ f_confused "Mengapa kamu tidak membelikan dirimu sendiri sebuah penis buatan?"

    show anon f_normal
    grace "Umm, kamu memang bertemu orang tua kami, kan?"

    odette "Ya."

    grace f_sad_down "{b}Ayah{/b} tidak mengizinkan kami bekerja, jadi saya tidak punya uang untuk membelinya..."

    grace "... Dan jika itu belum cukup, {b}Ibu{/b} selalu mengintip di kamar kami."

    show grace f_normal
    eve "Ya Tuhan, bisakah Anda bayangkan jika dia menemukan penis buatan di kamar Anda?"

    grace f_happy "Dia pasti akan sial!"

    eve @ f_laugh "Benar sekali!"

    pause
    show grace f_normal_back
    odette "Tapi tetap saja, sisir rambut?"

    grace @ f_eyeroll "Hanya pegangannya..."

    show anon f_laugh
    odette @ f_laugh "Pfft, hahaha!"

    show anon f_normal
    grace f_tired_back "Baiklah kalau begitu, jalang... Giliranku!"

    grace "Belum pernah saya melakukan permainan tiga arah di meja biliar di depan ruangan yang penuh dengan orang."

    show eve f_surprised
    show anon f_shock
    odette @ f_eyeroll "..."
    anon f_normal "Wah, itu spesifik sekali.."

    show odette f_yawn a_whiskey_drink with dissolve
    show anon f_surprised
    show grace f_happy
    eve f_disgusted @ f_surprised "K-kamu benar-benar melakukan itu?"

    show grace f_happy_back
    odette f_smirk a_whiskey "Itu sudah lama sekali."

    show anon f_grin
    eve "Aduh!"

    show anon f_normal
    odette "Kamu hanya hidup sekali, {b}Evie{/b}..."

    grace "Saat itulah orang-orang mulai menjulukimu jebakan jari Tiongkok, kamu tahu?"

    show anon f_confused
    show eve f_confused
    odette "Ugh, jangan bahas itu."

    grace f_happy @ f_laugh "Ha ha ha!"

    anon "Saya tidak mengerti..."

    eve "Saya juga tidak."

    grace a_fingers "Pikirkan tentang hal ini."

    anon f_thinking a_thinking "..."
    eve f_thinking_down "..."
    grace a_shot @ f_eyeroll "Ehh, sudahlah."

    show eve f_happy
    show grace f_normal_back
    odette "Baiklah, bolehkah kita mengajukan pertanyaan yang tidak secara spesifik menargetkan satu sama lain sekarang?"

    show anon f_normal a_shot with dissolve
    grace "Hei, kamu yang memulainya!"

    odette "Ya, ya..."

    pause
    odette "Mengapa kamu tidak pergi, {b}[firstname]{/b}?"

    show grace f_normal
    show eve f_happy_right
    anon f_worried "A-aku?"

    eve "Apakah Anda memahami aturannya?"

    anon "Saya kira demikian."

    anon f_thinking "Hmm, mari kita lihat..."

    anon "Belum pernah aku..."

    anon f_snarky "Dicuri."

    show eve f_happy
    grace @ f_uneasy "Anda belum pernah mencuri apa pun sepanjang hidup Anda?!"

    show eve f_happy_right
    anon "Tidak."

    show odette f_yawn a_whiskey_drink
    show grace a_shot_drink f_proud m_talk
    with dissolve
    show eve a_shot_drink f_drink with dissolve
    pause
    show eve a_shot f_disgusted_wince_down
    show odette f_smirk a_whiskey
    show grace a_shot f_happy -m_talk
    with dissolve
    eve "Eugh!"

    eve "Saya pikir Anda seharusnya mengajukan pertanyaan nakal, {b}[firstname]{/b}..."

    show anon f_depressed
    show eve f_happy
    show grace f_normal_back
    odette "Tidak, pertanyaan itu sempurna!"

    show grace f_normal
    show anon f_worried
    eve f_confused @ -m_talk "Hmm?"

    show grace f_normal_back
    odette "Itu membuat kita semua minum, bukan?"

    eve "Ya, ya?"

    odette "Itulah keseluruhan tujuan dari permainan ini, {b}Evie{/b}!"

    odette "Kerja bagus, {b}[firstname]{/b}."

    show eve f_happy_right
    show grace f_normal
    anon f_normal @ f_laugh "Terima kasih."

    grace "Giliranmu, {b}Kak{/b}."

    show eve f_happy
    eve "Oke."

    eve "Aku punya satu yang pasti akan membuat kalian bertiga!"

    odette "Baiklah, mari kita dengarkan."

    eve "Belum pernah aku..."

    eve "Mencium seorang gadis."

    odette "Uh, terlalu mudah!"

    show grace a_shot_drink f_proud m_talk
    show odette f_yawn a_whiskey_drink
    show anon a_shot_drink f_smoke
    with dissolve
    pause
    show anon f_disgusted_wince a_shot
    show grace a_shot f_normal -m_talk
    show odette f_smirk a_whiskey
    with dissolve
    anon "Gaah!"

    show anon f_worried
    eve "Berapa banyak gadis yang telah kamu cium, {b}Odette{/b}?"

    show grace f_normal_back
    odette "Saya tidak tahu, empat atau lima?"

    show grace f_normal
    show anon f_normal
    eve "{b}Rahmat{/b}?"

    grace "Dua."

    eve "Saya pikir pasti akan lebih, {b}Kak{/b}..."

    grace "Tidak, hanya {b}Odette{/b} dan seorang gadis acak di sebuah pesta di sekolah menengah."

    odette "Aku tidak percaya kamu tidak pernah mencium seorang gadis, {b}Evie{/b}."

    show eve f_nervous_down
    eve "Aku belum pernah mencium siapa pun sebelumnya {b}[firstname]{/b}..."

    grace "Aduh, aku tidak tahu itu..."

    grace @ f_laugh "Kalian berdua manis sekali!"

    odette "Manis?"

    show grace f_normal_back
    odette @ f_laugh "Sungguh tragis!"

    odette a_shrug "Di Sini."

    show grace f_surprised
    eve f_surprised "A-apa yang kamu-"

    show odette b_kiss_eve:
        xoffset -400
    hide eve
    with dissolve
    show anon f_surprised
    eve "!!!"
    grace f_angry "{b}Odette{/b}!"

    anon "!!!"
    show anon f_flirt_grin
    pause
    odette "Muuah!"

    hide odette
    show odette a_whiskey f_smirk zorder 1:
        xoffset 100
    show eve f_angry a_shot zorder 0:
        flip
        xoffset 100
    with dissolve
    eve "A-apa itu tadi?!"

    show grace f_tired_back
    odette "Sekarang Anda bisa mengatakan Anda telah mencium seorang gadis!"

    grace "Sudah kubilang jangan terlalu gila..."

    grace "Kami bahkan baru saja memulai dan-"

    odette "Maukah kamu bersantai?!"

    odette "Itu hanya ciuman..."

    grace @ -m_talk "Hmph."

    show eve f_normal
    odette "Giliran siapa?"

    show grace f_normal
    anon f_normal "Milikmu, menurutku."

    show grace f_normal_back
    odette "Baiklah."

    show odette f_thinking
    pause
    odette "Belum pernah aku..."

    odette f_smirk "Keluar dari rumah orang tuaku."

    show grace f_normal
    eve @ f_eyeroll "Saya merasa itu sulit dipercaya."

    show grace f_normal_back
    odette "Mengapa Anda mengatakan itu?"

    grace "Ayahnya membiarkan dia melakukan apa pun yang dia inginkan, ingat?"

    show grace f_normal
    eve f_happy "Oh benar..."

    show grace a_shot_drink f_proud m_talk
    show eve a_shot_drink f_drink
    show anon a_shot_drink f_smoke
    with dissolve
    pause
    show anon f_disgusted_wince a_shot
    show eve a_shot f_disgusted_wince_down
    show grace a_shot f_disgusted_wince -m_talk
    with dissolve
    eve "Fiuh!"

    show grace f_normal
    eve "Oke, hal ini benar-benar mengejutkanku..."

    anon f_worried "Ya, sepenuhnya."

    odette @ f_laugh "Haha!"

    grace "Mungkin kita harus memperlambat sedikit..."

    eve f_surprised "Tidak!"

    show grace f_normal_back
    odette "Kami tidak melambat."

    show eve f_happy
    odette "Sekarang giliranmu!"

    grace f_sad_back "{i}*Huh*{/i} Baik."

    grace f_thinking @ -m_talk "Hmm."

    pause
    show grace f_happy
    grace "Belum pernah aku..."

    grace "Selesai anal."

    show odette f_surprised
    show eve f_surprised
    show anon f_surprised_teeth
    show grace f_normal_back
    odette "Wah, benarkah?"

    show anon f_flirt_grin
    show eve f_nervous_right
    odette f_smirk "Bertahun-tahun dan Anda tidak pernah membiarkan siapa pun memarkirnya di garasi belakang Anda?"

    show eve f_nervous_down
    grace "Tidak."

    grace "Banyak yang telah mencoba tetapi saya tidak pernah membiarkannya."

    grace f_happy_back "Harus menyimpan sesuatu untuk pernikahan, kau tahu?"

    odette "Psh, ya benar..."

    show odette f_yawn a_whiskey_drink with dissolve
    show grace f_normal
    show eve a_shot_drink f_drink with dissolve
    pause
    show eve a_shot f_disgusted_wince_down
    show odette f_smirk a_whiskey
    with dissolve
    show grace f_surprised
    anon f_shock "!!!"
    grace "{b}Hawa{/b} apa-apaan ini?!"

    show eve f_nervous
    show anon f_surprised_teeth
    grace "Anda belum pernah berhubungan seks sebelumnya!"

    eve "Anda tidak mengatakan seks, Anda hanya mengatakan anal."

    eve f_nervous_down "Aku pernah menempelkan barang di sana sebelumnya..."

    show anon f_disgusted_wince
    show grace f_surprised_back
    show eve f_nervous_right
    odette "Oh sial, dia benar!"

    show eve f_nervous_down
    show anon f_flirt_grin
    odette "Anda tidak mengatakan seks."

    show grace f_sad_down
    grace "Y-ya, tapi..."

    odette "Siapa sangka, {b}Evie{/b} kecil telah melakukan sesuatu yang belum Anda lakukan!"

    odette "Haha!"

    grace f_sad "Mengapa kamu-"

    eve "Aku penasaran dan... Rasanya sungguh menyenangkan..."

    odette "Saya tidak pernah begitu bangga!"

    grace "Ugh, alasan utama aku pergi ke sana adalah agar kamu tidak perlu minum!"

    show grace f_tired_back
    odette "Saya bisa memberi Anda beberapa petunjuk nanti, jika Anda mau?"

    grace "Diam, {b}Odette{/b}!"

    odette @ f_laugh "Ha ha ha!"

    show grace f_sad
    eve f_sad_right "M-maaf, {b}[firstname]{/b}..."

    eve "Saya harap Anda tidak menganggap saya menjijikkan?"

    anon f_normal @ f_laugh "Tentu saja tidak."

    show eve f_nervous
    show grace f_sad_back
    odette "Oh, sialnya!"

    odette "Tidak ada yang perlu disesali tentang {b}Evie{/b}!"

    odette "Hanya karena adikmu pemalu-"

    show eve f_happy
    grace f_tired_back "Saya bukan orang yang pemalu!"

    odette @ f_laugh "Ha ha ha!"

    pause
    show grace f_sad_back
    odette "Tapi serius, bereksperimen dengan hal-hal semacam itu adalah hal yang wajar..."

    odette "... Dan sebagai catatan, dia benar... Rasanya sungguh menyenangkan!"

    grace f_normal @ f_eyeroll "Uh, selanjutnya!"

    show grace f_sad
    eve f_happy_right "Saya pikir sekarang giliran {b}[firstname]{/b}."

    anon "Apakah itu?"

    eve @ -m_talk "Mmhmm."

    anon "O-oke."

    anon f_thinking "Hmm."

    pause
    anon "Belum pernah aku..."

    anon f_snarky "Melakukan masturbasi di depan umum."

    show eve f_happy
    show grace f_surprised
    odette @ f_laugh "Hah, dia menangkapku..."

    show grace f_sad_back
    show odette f_yawn a_whiskey_drink with dissolve
    pause
    show odette f_smirk a_whiskey with dissolve
    grace f_sad_down "{i}*Huh*{/i}"

    show grace a_shot_drink f_proud m_talk with dissolve
    show anon f_flirt_grin
    pause
    show grace a_shot f_sad_back -m_talk with dissolve
    odette f_surprised "Beneran, kapan?!"

    grace f_sad_down "Bukan urusanmu..."

    odette "Hei, itu aturan mainnya!"

    odette "Anda harus menumpahkannya!"

    show odette f_smirk
    grace @ f_eyeroll "..."
    eve @ f_laugh "Ayo, Kak..."

    grace f_normal "Uh, baiklah."

    show anon f_normal
    grace f_normal_back "Anda ingat Tuan Frampton?"

    odette "Guru IPS kita di sekolah menengah?"

    grace "Ya."

    grace "Yah, aku selalu mengira dia seksi dan suatu hari di kelas... Aku agak..."

    odette "Kamu melakukan masturbasi di kelas?!"

    grace "Ya, sedikit... Di bawah mejaku."

    odette @ f_laugh "Ya Tuhan!"

    grace "Tidak ada yang tahu, saya sangat berhati-hati!"

    show anon f_laugh
    odette "Kamu gadis nakal..."

    show anon f_normal
    grace f_sad_down @ f_tired_back "Diam!"

    odette @ f_laugh "Ha ha ha!"

    show eve a_shot_drink f_drink with dissolve
    show grace f_surprised
    pause
    show eve a_shot f_disgusted_wince_down with dissolve
    anon f_surprised "!!!"
    grace "Serius, kamu juga?!"

    show anon f_normal
    show eve f_happy
    eve "Y-ya, suatu saat..."

    show grace f_sad
    eve "Di kamar mandi di sekolah."

    odette "Apa yang memicunya?"

    show eve f_nervous_right
    eve "Uhh... T-tidak ada."

    show eve f_nervous_down
    odette @ -m_talk "Hmm?"

    eve "Saya tidak ingat."

    odette "Psh, ayolah!"

    odette "Apakah itu melibatkan {b}[firstname]{/b} atau semacamnya?"

    show eve f_hood_remove
    grace f_tired_back "{b}Odette{/b}!"

    grace f_sad "Dia tidak perlu mengatakan jika dia tidak mau..."

    show eve f_nervous_down
    odette "{i}*Huh*{/i} Ya, oke."

    grace "Saya pikir sebaiknya kita hentikan permainan ini di sini, saya tidak ingin ada yang sakit..."

    show grace f_surprised
    show anon f_grumpy
    eve f_surprised "TIDAK!"

    show anon f_surprised
    pause
    eve f_nervous "Maksudku, satu lagi..."

    show grace f_sad
    show anon f_normal
    eve "Sekarang giliranku."

    grace f_thinking @ -m_talk "..."
    grace f_normal @ f_eyeroll "Baiklah, satu lagi."

    eve f_nervous_right "Saya belum pernah berhubungan seks."

    show anon f_surprised_teeth
    show grace f_eyeroll
    show eve f_nervous
    odette "Ya, itu hal yang mudah."

    show odette f_yawn a_whiskey_drink
    show grace a_shot_drink f_proud m_talk
    with dissolve
    pause
    show grace a_shot f_normal -m_talk
    show odette f_smirk a_whiskey
    with dissolve
    if not M_player.is_virgin:
        show anon a_shot_drink f_smoke with dissolve
        show eve f_sad_right
        pause
        show anon f_disgusted_wince a_shot with dissolve
        show eve f_sad_down
        show grace f_sad
        odette "Benar-benar?"

        show anon f_worried
        odette "Siapa gadis yang beruntung itu?"

        grace @ f_sad_back "{b}Odette{/b}..."

        anon "Ehh, aku lebih suka tidak bilang... Kalau tidak apa-apa?"

        eve "Ya, tidak apa-apa."

        odette "Ah, tapi aku ingin-"

    else:
        show anon f_grin
        show eve f_nervous_right
        pause
        show eve f_happy_right
        show grace f_happy
        odette f_tired "Benar-benar?"

        odette "Kamu masih perawan?"

        show anon f_surprised
        grace @ f_tired_back "{b}Odette{/b}..."

        anon f_worried "Y-ya."

        anon "Saya sedang menunggu untuk menemukan orang yang tepat."

        eve "Manis sekali, {b}[firstname]{/b}!"

        show anon f_normal
        grace @ f_laugh "Memang benar!"

        odette f_smirk @ f_eyeroll "Laaaaaa."

    show eve f_normal
    grace f_tired_back "{b}Odette{/b}!"

    odette f_tired "Apa?!"

    show grace f_surprised
    pause
    show grace f_surprised_back
    pause
    odette f_smirk @ f_surprised "Oh."

    show grace f_normal
    pause
    grace "Baiklah, menurutku cukup permainan untuk malam ini."

    odette "Baiklah, aku akan terus minum..."

    show odette f_yawn a_whiskey_drink
    anon @ f_surprised "!!!" with hpunch
    show odette f_smirk a_whiskey with dissolve
    show grace f_normal_back
    pause
    odette @ f_burp "{i}*Buuuurp*{/i}"

    odette "Jika tidak apa-apa bagi kalian bertiga?"

    show eve f_happy
    grace "Hancurkan dirimu sendiri."

    odette "Jadi..."

    show grace f_surprised_back
    odette f_shy "Apakah kalian berdua berkencan sekarang atau bagaimana?"

    show eve f_surprised_right
    show grace f_surprised
    anon f_worried "Uhh..."

    eve "Saya rasa kami belum siap untuk memberi labelnya."

    odette "Tapi kamu menyukainya, kan?"

    eve f_nervous_down @ -m_talk "Mmhmm."

    odette f_smirk "aku tahu dia menyukaimu..."

    show grace f_normal
    anon f_flirt "Ya."

    if M_eve.biggus_dickus:
        odette "... Dan Anda telah melihat gadis itu."

        show anon f_surprised
    else:
        odette "... Dan Anda telah melihat bekas lukanya."

    show grace f_tired
    show odette f_laugh
    eve f_surprised "!!!"
    show odette f_smirk
    grace f_angry_back "{b}Odette{/b}!"

    show anon f_worried
    odette "Apa?!"

    odette "Dia sudah melakukannya, bukan?"

    show eve f_nervous_right
    anon f_normal "Saya memiliki."

    odette "Bisakah kita menyelesaikan semua kerahasiaan ini?"

    show eve f_nervous
    grace f_sad @ -m_talk "..."
    odette "{b}Evie{/b} tidak perlu malu... Dia patut bangga!"

    eve f_sad_down "Entahlah tentang bangga..."

    if M_eve.biggus_dickus:
        odette "Kamu gadis seksi dengan penis... Luar biasa!"

        eve f_sad "Ehh-"

        odette "Sungguh!"

    else:
        odette "Bekas luka itu sangat seksi, Nak."

        eve f_sad "Ehh-"

        odette "aku serius!"

    odette "Bukankah itu seksi, {b}[firstname]{/b}?"

    anon f_grin @ f_normal "Saya bersedia."

    eve f_surprised_right "K-kamu yakin?"

    grace f_normal @ f_uneasy "Aduh."

    eve f_nervous_down "T-tapi bagaimana dengan diriku yang lain?"

    show anon f_normal
    odette f_shy "Apa yang kamu bicarakan?!"

    eve "K-kau tahu, payudara kecilku..."

    show anon f_worried
    eve "... Dan pantatku yang rata."

    odette f_normal @ f_eyeroll "Oh, astaga!"

    show grace f_normal_back
    odette "Itu yang membuatmu malu sepanjang waktu?!"

    eve @ -m_talk "..."
    odette "Kamu harus bangun, Nak!"

    odette "Katakan padanya {b}[firstname]{/b}..."

    show grace f_normal
    show eve f_nervous_right
    anon f_normal "Aku suka tubuhmu."

    show eve f_happy_right
    odette f_shy "MELIHAT!"

    show grace f_normal_back
    show eve f_happy
    odette f_smirk "Aku yakin kamu punya tunas-tunas kecil yang lezat di bawah sana dan para pria menyukainya... Percayalah!"

    show grace f_eyeroll
    eve "B-benarkah?"

    show grace f_normal_back
    odette @ f_laugh "Ya, ya!"

    odette @ f_eyeroll "Maksudku, lihat adikmu... Payudaranya bukanlah sesuatu yang perlu dituliskan di rumah."

    show anon f_worried
    grace f_sad_down @ f_eyeroll "Ya ampun, terima kasih..."

    odette f_surprised "Apa-"

    odette f_confused "Itu bukan-"

    pause
    odette f_sad "Kau tahu, menurutku milikmu cantik, tapi ternyata tidak..."

    odette f_tired "Sialan, kamu tahu maksudku!"

    grace f_happy @ f_laugh "Haha!"

    show anon f_normal
    eve "Maksudmu, dia tidak bertumpuk sepertimu..."

    show grace f_happy_back
    odette f_normal "Ya, tepatnya!"

    odette f_shy "Dia tidak bertumpuk seperti saya, dan dia masih mendapat banyak perhatian, bukan?"

    eve "Ya."

    odette f_smirk "Pria menyukai segala bentuk dan ukuran..."

    odette "... Dan kamu lucu sekali!"

    pause
    odette "Aku akan menidurimu dalam sekejap."

    show eve f_eyeroll
    show anon f_flirt
    grace f_surprised_back "{b}Odette{/b}!!!"

    show eve f_happy
    odette f_confused "Apa?!"

    odette "saya akan melakukannya."

    grace f_sad_back @ f_eyeroll "Yesus."

    odette "Mengapa kamu tidak melepas hoodie itu dan biarkan kami menemuimu?"

    show anon f_surprised
    show grace f_sad
    eve f_nervous "Benar-benar?"

    show anon f_flirt_grin
    odette "Ya!"

    grace "Anda tidak perlu melakukan itu {b}Malam{/b}..."

    odette f_normal "Diam, pemalu!"

    grace f_angry_back "Berhenti memanggilku seperti itu!"

    show odette f_laugh
    show eve f_nervous_right
    show grace f_sad
    eve @ -m_talk "..."
    show odette f_normal
    pause
    show eve f_nervous_down
    show grace f_sad_back
    odette @ f_eyeroll "Ya Tuhan dengan hal rasa malu ini..."

    show odette f_yawn a_whiskey_drink with dissolve
    show eve f_nervous
    pause
    show odette b_skirt f_tired_down a_remove1 with dissolve
    pause
    show odette b_skirtblank a_remove2 with dissolve
    pause
    show odette a_remove3 with dissolve
    show odette a_remove4 with dissolve
    pause
    show odette f_smirk b_skirt a_whiskey
    show grace f_surprised_back
    show eve f_surprised
    anon f_shock "!!!" with hpunch
    show anon f_flirt_grin
    show grace f_weary a_facepalm with dissolve
    odette "Di sana, lihat..."

    odette "Itu tidak terlalu menakutkan."

    show eve f_nervous_down a_hoodless_remove2 with dissolve
    show grace f_normal_back a_shot with dissolve
    pause
    show odette b_skirtblank a_idle with dissolve
    show eve f_nervous a_shot with dissolve
    odette f_tired_down "Hal-hal sialan ini sangat menyebalkan, lebih dari segalanya..."

    grace @ f_tired_back "Kamu penuh omong kosong."

    odette f_normal "aku serius!"

    show odette b_skirt a_whiskey with dissolve
    odette "Beratnya satu ton!"

    odette @ f_eyeroll "Punggungku selalu sakit!"

    odette "Mereka selalu menghalangi jalanku..."

    odette "... Dan pernahkah kamu melihatku mencoba lari?"

    grace @ f_weary "Ehh."

    odette "Ingat konser yang kita ikuti beberapa tahun lalu?"

    odette "Di mana kami harus berlari melewati keamanan?"

    grace "Oh ya!"

    odette "Dadaku melambung dan memaku tepat di wajahku!"

    grace f_happy_back @ f_laugh "Haha, omong kosong itu lucu!"

    odette f_shy "Tidak, bukan itu!"

    odette "Saya praktis membuat mata saya hitam!"

    show grace f_laugh
    show odette f_laugh
    show anon f_laugh
    eve f_laugh "Haha!"

    anon "Haha!"

    show grace f_happy_back
    show eve f_happy
    show anon f_flirt_grin
    odette f_smirk "Jadi, tahukah Anda, payudara besar bukanlah segalanya yang mereka inginkan..."

    eve "Y-ya, menurutku."

    odette "Lepaskan hoodienya, saya ingin melihat apa yang sedang Anda kerjakan!"

    show grace f_normal
    eve f_nervous_down "{i}*Huh*{/i} Baiklah."

    show eve b_topless a_remove with dissolve
    pause .25
    show eve b_pants a_dressup with dissolve
    pause
    show eve a_shot with dissolve
    odette f_smirk @ f_moo a_whiskey_yay "Wooooo!!!"

    eve f_nervous @ f_eyeroll "Diam..."

    odette "Lihat, aku benar!"

    odette "Itu menggemaskan!"

    show eve f_nervous_right
    eve @ -m_talk "..."
    show eve f_nervous
    show grace f_normal_back
    odette "Anda pria yang beruntung, {b}[firstname]{/b}!"

    odette @ f_laugh "Saya akan memakannya segera!"

    show grace f_normal
    show eve f_nervous_right
    show odette f_tired_down a_remove5 with dissolve
    pause
    show odette b_remove6 with dissolve
    pause
    show odette b_panties f_smirk a_whiskey with dissolve
    show anon f_surprised
    show eve f_surprised
    grace f_surprised_back "Maukah kamu berhenti?!"

    show anon f_grin
    show eve f_nervous
    grace "Anda sudah melangkah cukup jauh!"

    show anon f_flirt
    show grace f_tired_back
    odette f_tired "Ya Tuhan, apa urusanmu, {b}Grace{/b}?!"

    odette "Kapan kamu menjadi pemalu?"

    grace f_angry_back "Aku bukan orang yang pemalu!"

    odette @ f_eyeroll "Ya benar."

    odette "Kapan terakhir kali kamu bercinta?"

    grace f_sad_down "Itu bukan-"

    odette "Karena aku belum pernah melihatmu bersama siapa pun di... Entahlah... Bagaimana menurutmu, {b}Evie{/b}?"

    eve "Tidak sejak kecelakaan {b}Ibu{/b} dan {b}Ayah{/b}."

    grace f_sad "Itu tidak ada hubungannya dengan itu."

    odette @ -m_talk "Mmhmm."

    odette f_normal "Dulu kamu menyenangkan, tahu?"

    grace f_sad_back "Saya masih menyenangkan!"

    odette f_smirk @ f_laugh "Kalau begitu buktikan, yuk kita lihat skinnya!"

    show eve f_happy
    grace f_sad_down @ f_eyeroll "{i}*Huh*{/i}"

    pause
    grace f_normal_down "Bagus. Persetan!"

    show grace a_remove1 with dissolve
    pause
    show grace b_shorts a_remove2 with dissolve
    pause
    show grace f_normal a_hip with dissolve
    show anon f_flirt
    eve @ f_moo a_shot_yay "Wooooo!!!"

    odette @ f_laugh "Haha, itulah semangatnya!"

    show grace f_proud a_remove3 with dissolve
    pause
    show grace b_remove4 with dissolve
    pause
    show grace f_normal_back b_underwear a_shot with dissolve
    grace "Di sana."

    grace "Puas?"

    odette "Tidak, tapi ini sebuah permulaan."

    grace @ -m_talk "..."
    odette "Di sini, Anda memerlukan lebih banyak lagi!"

    show odette a_idle
    show grace a_whiskey
    with dissolve
    grace f_sad_down "{i}*Huh*{/i}"

    show grace a_whiskey_drink f_proud m_talk with dissolve
    pause
    show grace a_whiskey f_normal -m_talk with dissolve
    odette "Bagaimana menurut Anda, {b}[firstname]{/b}?"

    odette "Apakah ini wanita jalang seksi atau apa?!"

    show eve f_happy_right
    anon "Sangat seksi."

    pause
    show odette f_surprised
    pause
    show grace f_happy_back
    show eve f_happy
    odette f_smirk_back @ f_laugh "Oh sial, ini selaiku!"

    show grace b_lead f_happy zorder 2
    show odette b_empty zorder 3:
        xoffset -545
    with dissolve
    odette "Ayo berdansa denganku!"

    grace @ f_laugh "hehe!"

    hide grace
    hide odette
    with dissolve
    eve f_happy_right "Anda ingin menari?"

    anon f_worried "Ehh, mungkin sebentar lagi."

    anon f_flirt "Saya hanya akan menontonnya untuk saat ini."

    eve f_laugh "Hehe, oke!"

    hide eve with dissolve
    show anon f_flirt_grin
    pause
    eve "Tunggu aku!"


    scene location_tattoo_rooftop_cutscene01
    show text _ ("The moment had me completely frozen in place.\nMesmerized by beautiful bodies of the girls dancing before me in the firelight.") as caption
    with fade
    hide caption with dissolve
    show text _ ("It was hard to fathom how I had ended up in this situation...\nWas I just the luckiest guy on the planet or what?") as caption with dissolve
    pause

    scene expression background(800, 400, 2.4) as stage
    show anon f_flirt_grin at flip
    with fade
    anon @ -m_talk "..."
    show eve b_pants f_laugh a_hip at flip with {'master': dissolve}
    eve "hehe!"

    show eve b_empty:
        xoffset -530
        xzoom 1
    show anon b_pulling4 f_grin
    with {'master': dissolve}
    eve f_happy_right "Ayo, {b}[firstname]{/b}... Ayo berdansa denganku!"

    anon f_flirt "O-oke."

    show anon:
        xoffset -188
    show eve f_happy:
        xoffset -718
    with dissolve
    pause
    anon f_surprised "Wah..."

    eve f_happy_right @ -m_talk "Hmm?"


    scene expression background(512, 400, 2.4) as stage
    show odette b_kiss_grace:
        xoffset -400
    with fade
    pause
    show anon f_flirt:
        xzoom -1
        xoffset 100
    show eve f_happy b_pants a_hip:
        xoffset -100
    with dissolve
    anon "Sepertinya {b}Odette{/b} akhirnya sampai di suatu tempat bersama adikmu..."

    eve "Y-ya, mungkin."

    pause
    show eve a_belly_sick f_disgusted_wince_down:
        xoffset 450
        xzoom -1
    with {'master': dissolve}
    eve "Ya."

    anon f_worried "Kamu baik-baik saja?"

    eve "Ya, aku hanya-"

    pause
    eve "Merasa sedikit pusing... Tiba-tiba..."

    anon "Bolehkah aku mengambilkanmu beberapa-"

    eve f_surprised a_puke "Astaga!"

    hide eve
    show anon a_surprised f_surprised:
        xzoom 1
        xoffset 600
    with dissolve
    anon "{b}Malam{/b}?!"

    show anon a_surprised_up f_surprised_teeth
    with {'master': dissolve}
    eve "{i}*BLLEEAARRGHHH*{/i}"

    show anon a_sides f_worried
    show odette b_panties f_confused:
        xoffset 100
        xzoom -1
    show grace b_underwear f_sad:
        xoffset -100
        xzoom -1
    with dissolve
    grace "Apakah dia muntah?"

    show anon:
        xoffset 50
        xzoom -1
    with {'master': dissolve}
    anon "Y-ya, menurutku begitu..."

    grace "Sial!"

    grace f_angry "Sudah kubilang ini keterlaluan!"

    show odette f_sad
    hide grace
    show anon:
        xzoom 1
        xoffset 550
    with dissolve
    grace "Ayo {b}Kak{/b}. Ayo kuantar kau ke bawah dan minum air..."

    odette @ -m_talk "..."
    odette "Sial!"

    show anon f_worried:
        xoffset 0
        xzoom -1
    with dissolve
    odette "Bicara tentang waktu yang buruk!"

    anon "Apakah {b}Eve{/b} akan baik-baik saja?"

    odette f_tired "Oh, dia akan baik-baik saja..."

    show anon:
        xoffset 500
        xzoom 1
    with {'master': dissolve}
    odette "Terlalu banyak dan terlalu cepat."

    pause
    odette f_smirk "Cukup malam, ya?"

    anon "Ya, cukup gila."

    odette "Saya yakin itu semua cukup menarik bagi Anda?"

    show anon a_behind_head f_surprised:
        xoffset 0
        xzoom -1
    with dissolve
    pause
    anon f_worried "Ehh, y-ya..."

    odette @ f_laugh "Hehe, ada apa?"

    odette "Kamu tampak sedikit malu..."

    anon @ -m_talk "..."
    show odette b_pantiesblank with dissolve
    odette "Kamu menyukai payudaraku, {b}[firstname]{/b}?"

    show odette f_smirk_down
    anon f_surprised_teeth_down o_boner "!!!" with hpunch
    anon f_depressed "M-maaf, aku tidak bermaksud-"

    odette f_smirk @ f_laugh "Haha!"

    odette "Tidak apa-apa, {b}[firstname]{/b}... Anda bisa melihatnya."

    anon a_sides f_flirt @ -m_talk "..."
    odette "Anda ingin menyentuhnya?"

    anon f_worried "Oh, uhh..."

    anon "... Menurutku itu bukan ide yang bagus."

    show odette b_panties
    with {'master': dissolve}
    odette "Kenapa tidak?"

    odette "{b}Evie{/b} tidak akan keberatan jika kita bersenang-senang sedikit..."

    anon @ -m_talk "..."
    show anon f_surprised behind odette
    show odette a_grope:
        xoffset 250
    with {'master': dissolve}
    odette "... aku berjanji!"

    show anon f_surprised_down
    with {'master': dissolve}
    anon @ -m_talk "!!!"
    odette a_idle f_surprised_down "Wow, {b}Tuuku{/b} tidak bercanda!"

    show anon a_sides f_surprised
    with {'master': dissolve}
    odette f_smirk "Kamu besar!"

    anon f_worried "Menurutku kita tidak seharusnya-"

    odette "Aww, jangan malu kawan."

    show anon a_up f_surprised_low -o_boner
    show odette a_anon_pants1 f_smirk_lip_down:
        offset (237, 207)
    with {'master': dissolve}
    anon "A-wah, {b}Odette{/b}!!"

    pause
    odette f_smirk_up "Kamu pasti sangat terangsang setelah malam yang baru saja kamu alami..."

    odette "... Heh, aku tahu, tentu saja!"


    menu:
        "Saya tidak bisa melakukan ini!":
            show odette a_anon_pants2 f_confused
            show anon a_cover_boner o_boner f_worried_low
            with {'master': dissolve}
            anon "Hentikan itu, {b}Odette{/b}."

            odette f_thinking @ -m_talk "Hmm?"

            show odette a_sides
            with {'master': dissolve}
            anon "{b}Eve{/b} dan {b}Grace{/b} ada di bawah!"

            show anon a_sides
            show odette f_smirk_up
            with {'master': dissolve}
            odette "Oh, santai saja... mereka akan sibuk untuk sementara waktu."

            show anon -o_boner
            show odette a_anon_pants1 f_smirk_lip_down
            with {'master': dissolve}
            anon "Bukan itu intinya, aku-"

            show odette a_anon_pants2 f_sad
            show anon a_cover_boner o_boner f_surprised_low
            with {'master': dissolve}
            anon "{b}Odette{/b}, berhenti!"

            show odette a_sides f_annoyed_up
            with {'master': dissolve}
            odette "Tunggu, serius?"

            anon "Ya!"

            odette f_thinking "Umm, kamu paham aku menawarkan untuk menghisap penismu sekarang... kan?"

            anon f_worried_low "Ya, menurutku... hanya saja-"

            show anon a_sides -o_boner
            with {'master': dissolve}
            anon "{i}*Sigh*{/i} Bisakah Anda berdiri?"

            pause
            show odette b_remove6:
                offset (200, 50)
            with {'master': dissolve}
            anon "Lihat, kamu seperti, sangat seksi dan sebagainya..."

            show anon f_worried of_blush
            show odette b_panties f_confused:
                offset (200, 0)
            with {'master': dissolve}
            anon "... Dan sangat, SANGAT telanjang..."

            show odette f_laugh
            with {'master': dissolve}
            odette "hehe!"

            show odette f_smirk
            with {'master': dissolve}
            odette "Eh ya?"

            show anon f_shy_left
            with {'master': dissolve}
            anon "... Tapi {b}Eve{/b} dan aku... yah, aku masih yakin kita seperti apa."

            show anon f_shy
            show odette f_confused
            with {'master': dissolve}
            anon "T-tapi aku ingin sekali mengetahuinya!"

            odette "Oh oke?"

            anon f_worried "Dan aku benar-benar tidak ingin mengambil risiko mengacaukan segalanya... kau tahu?"

            anon "Jadi, sama seperti aku menikmati... uhh..."

            odette f_smirk "Seks oral?"

            anon "... Y-ya, itu!"

            odette f_laugh "{i}*Mendengus*{/i}"

            show anon a_cover_boner
            with {'master': dissolve}
            anon "Saya khawatir saya harus menolaknya dengan hormat."

            odette f_smirk "Wow, menurutku belum pernah ada orang yang menolakku sebelumnya..."

            show anon f_surprised_low
            show odette a_excited f_shy:
                xoffset 275
            with {'master': dissolve}
            odette "... itu membuatku semakin bersemangat."

            anon f_shy "{i}*Gulp*{/i} B-benarkah?"

            odette @ -m_talk "Mhmm."

            grace "{b}Odette{/b}!"

            show anon a_sides f_worried_left -of_blush
            show odette f_confused
            with {'master': dissolve}
            grace "Saya butuh bantuan Anda!"

            odette f_sad "Ck, sepertinya kesenangan kita dipersingkat..."

            show anon f_worried
            show odette a_sides:
                xoffset 200
            with {'master': dissolve}
            odette f_smirk "Kamu sebaiknya pulang... Kami akan menjaga {b}Evie{/b}."

        "Sekarang apa?":

            show odette a_sides f_smirk_lip_down
            show anon b_shirt od_dick2
            with dissolve
            show anon od_dick3
            with fastdissolve
            show odette a_excited f_smirk_down
            show anon od_dick4
            with fastdissolve
            odette "Halo!"

            show odette a_anon_pants2 f_smirk_lip_down
            with {'master': dissolve}
            anon "Uhh, apa sebenarnya yang kamu-"


            call scene_odette_blowjob
            $ unlock_scene('Odette', '04_unlocked', variant='roof')

            scene expression background(512, 400, 2.4) as stage
            show anon a_sides b_shirt od_dick4_wet f_surprised:
                xzoom -1
            show odette a_wipe b_panties:
                xoffset 200
                xzoom -1
            with fade
            pause
            show odette a_sides
            with {'master': dissolve}
            odette "Sial, sebaiknya aku pergi..."

            anon f_confused "Tunggu, kamu pergi?!"

            odette f_smirk "Panggilan tugas, aku takut..."

            odette "... Tapi jangan khawatir, kawan..."


    show anon f_surprised
    show odette a_kiss f_moo
    with dissolve
    pause
    odette a_idle f_smirk "Untuk dilanjutkan."

    anon @ -m_talk "{i}*Meneguk*{/i}"

    show anon f_shy:
        xoffset 500
        xzoom 1
    hide odette
    with {'master': dissolve}
    odette "hehe!"

    pause
    anon f_flirt_grin @ -m_talk "(Sial!)"

    anon @ -m_talk "(Gadis itu adalah masalah besar...)"

    pause
    anon @ f_laugh -m_talk "(... Malam yang luar biasa!)"

    anon @ -m_talk "(Saya pikir {b}Eve{/b} dan saya mungkin benar-benar membangun sesuatu yang sangat istimewa di sini! )"

    anon @ -m_talk "(Saya harus memastikannya dan {b}memeriksanya besok{/b}. )"

    hide anon with dissolve
    return

label eve_button_eve_talk_to_girls:
    scene expression player.location.background_closeup with None
    show anon a_beer
    show eve f_happy a_ipod
    with dissolve
    anon "Ini dia."

    show eve a_beer_ipod
    show anon b_dressed_pickup
    with dissolve
    eve "Terima kasih, {b}[firstname]{/b}!"

    show anon b_dressed f_worried a_beer with dissolve
    anon "Maaf, saya tidak bisa menemukan yang hangat dan sigung; sudah lewat tanggal kadaluarsanya..."

    show eve f_confused
    anon f_snarky "Tahukah Anda, karena biasanya Anda meminumnya seperti itu?"

    eve f_happy @ f_laugh "Oh, hah hah, lucu sekali."

    anon f_normal @ f_laugh "Ha ha ha!"

    eve f_normal_down "Anda punya preferensi musik?"

    anon "Tidak, semuanya baik-baik saja."

    eve "Saya pikir saya akan memulai kita dengan musik rock klasik."

    eve "Itu favorit {b}Grace{/b}."

    anon "Bekerja untuk saya!"

    pause
    eve f_sad a_beer_hold "{i}*Sigh*{/i} Saya sangat berharap {b}Grace{/b} menghentikannya malam ini."

    eve "Anda tidak akan percaya betapa menyenangkannya dia dulu!"

    anon f_worried "Menurutku dia cukup menyenangkan sekarang, {b}Eve{/b}."

    eve "Y-ya, tapi tidak seperti sebelum kecelakaan itu..."

    anon "Anda benar-benar berpikir kecelakaan itu penyebabnya?"

    eve "Saya harap begitu."

    eve f_sad_down "Kalau tidak, ini salahku."

    anon f_skeptical "Bagaimana itu bisa menjadi kesalahanmu?"

    eve "K-kamu tahu, karena dia terjebak menjagaku..."

    anon "Bukankah mungkin dia tumbuh begitu saja dari suasana pesta?"

    anon "Maksudku, orang-orang melakukan itu..."

    anon "Mereka bertambah tua dan prioritas mereka berubah."

    eve "Ya, menurutku."

    anon "Jangan terlalu khawatir tentang hal itu."

    anon f_worried "Mari kita fokus bersenang-senang malam ini, ya?"

    eve "Anda benar."

    show anon b_hug_eve f_shy_down
    hide eve
    with dissolve
    eve "Kamu selalu membuatku merasa lebih baik, {b}[firstname]{/b}."

    eve "Terima kasih!"

    return


label eve_button_bike_breakdown_started:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk
    with dissolve
    eve "Hai, {b}[firstname]{/b}!"

    if player.location != L_school_frenchclassroom:
        hide eve
        show anon b_hug_eve f_shy_down
        with dissolve
    anon "Halo."

    if player.location != L_school_frenchclassroom:
        show anon b_dressed f_normal
        show eve f_happy
        with dissolve
    eve "Apakah Anda masih {b}akan datang akhir pekan ini{/b}?"

    anon "Tentu saja."

    eve "Saya sangat berharap {b}Grace{/b} memperbaiki sepedanya dan mengizinkan kami mengajaknya berkeliling!"

    anon "Ya, itu akan luar biasa!"

    return

label eve_button_bike_breakdown_start:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk
    with dissolve
    eve "Hai, {b}[firstname]{/b}!"

    if player.location != L_school_frenchclassroom:
        hide eve
        show anon b_hug_eve f_shy_down
        with dissolve
    anon "Halo."

    if player.location != L_school_frenchclassroom:
        show anon b_dressed f_normal
        show eve f_happy
        with dissolve
    anon "Kamu ingin jalan-jalan sepulang sekolah?"

    eve f_sad "Ah, kuharap aku bisa..."

    eve "Aku mendapat detensi, ingat?"

    anon f_worried "Oh benar."

    eve "Maaf."

    anon "Tidak masalah."

    eve f_happy "Kamu harus {b}datang ke rumahku akhir pekan ini{/b}!"

    show anon f_normal
    eve "{b}Grace{/b} mendapatkan suku cadang pengganti untuk sepedanya, jadi dia akan mencoba memperbaikinya."

    anon "Oh ya?"

    eve "Siapa tahu, jika dia berhasil, dia mungkin akan membiarkan kita mencobanya."

    anon @ f_laugh "Itu akan sangat luar biasa!"

    eve "Jadi kamu akan berada di sana?"

    anon "Anda yakin saya akan melakukannya."

    eve @ f_laugh "Hehe, aku tidak sabar!"

    hide anon with dissolve
    return

label eve_button_detention:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    eve "{b}[firstname]{/b}!"

    hide eve
    show anon b_hug_eve f_laugh
    with dissolve
    anon "Heh, hei {b}Hawa{/b}."

    anon f_shy_down "Bagaimana kabarmu?"

    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    eve "Luar biasa, terima kasih!"

    anon "Apa maksudmu?"

    eve "Saya menyerahkan sketsa Anda kepada {b}Nona Ross{/b}, dan dia menyukainya!"

    anon "Benar-benar?"

    eve "Ya!"

    eve "Anda benar-benar menyelamatkan saya dari banyak masalah."

    anon "Ah, ayolah... Bukan apa-apa."

    hide anon
    show eve b_dressed_kiss:
        xoffset -400
    with dissolve
    anon "!!!"
    pause
    show eve b_dressed f_surprised a_cover_mouth:
        xoffset 0
    show anon f_flirt
    with dissolve
    eve "Ups!"

    show eve f_nervous a_rossed
    eve "M-maaf, aku lupa dimana kita berada..."

    anon "T-tidak, tidak apa-apa."

    anon "Aku suka menciummu."

    eve @ f_surprised "Anda melakukannya?"

    anon "Tentu saja."

    eve a_idle "Hehe, aku juga suka menciummu."

    show anon f_grin
    show eve f_nervous_down
    pause
    eve "Tapi aku melakukannya... Agak... Berjanji {b}Grace{/b} bahwa kita akan melakukannya perlahan..."

    anon f_worried "Oh?"

    eve "Y-ya."

    eve f_nervous "Dia memainkan peran sebagai kakak perempuan yang peduli lagi."

    anon f_grin @ f_unimpressed "Hehe, tidak apa-apa."

    eve "Ya?"

    anon f_normal "Kita bisa melakukannya pelan-pelan, tidak masalah."

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "Ya Tuhan, kamu yang terbaik, {b}[firstname]{/b}!"

    eve "Terima kasih!"

    anon "Terima kasih kembali."

    pause
    show anon b_dressed f_normal
    show eve f_happy
    with dissolve
    anon "Jadi, bagaimana hubungan adikmu dan {b}Odette{/b} malam itu?"

    eve @ -m_talk "Hmm?"

    anon f_flirt "Tahukah mereka?"

    eve "Oh, kamu bertanya apakah mereka sudah terhubung?"

    anon f_flirt_grin @ -m_talk "Mmhmm."

    eve "Tidak, mereka tidak melakukannya."

    eve @ f_eyeroll "Rupanya, adikku tertidur tak lama setelah mereka memutar filmnya."

    anon f_normal @ f_laugh "Dia tertidur?"

    eve "Ya."

    anon "Selama film horor?"

    eve @ f_laugh "Haha!"

    eve "Aku tahu, gila kan?!"

    eve "Itu karena dia sendiri yang bekerja terlalu keras."

    eve "Dia kelelahan, sepanjang waktu!"

    anon "Ya, saya bisa membayangkannya."

    eve f_sad_down "Saya berharap dia mengizinkan saya membantunya."

    pause
    anon "Mengapa {b}Odette{/b} tidak membantunya?"

    eve f_normal "Apa?"

    anon "Maksudku, dia ada di tempatmu sepanjang waktu..."

    anon "Jika dia menawarkan bantuan {b}Grace{/b} dengan pekerjaan di toko, mungkin {b}Grace{/b} akan lebih menerima ajakannya?"

    eve f_thinking_down @ -m_talk "Hmm."

    anon "Menurutmu tidak?"

    eve f_normal "Tidak, itu sebenarnya ide yang bagus."

    eve a_hip @ f_eyeroll "Bahkan mungkin berhasil... JIKA {b}Odette{/b} tidak terlalu malas!"

    anon @ f_laugh "Haha!"

    eve "Gadis itu belum pernah bekerja sehari pun sepanjang hidupnya."

    anon "Anda harus memberitahunya."

    eve "Yaaah, tidak."

    anon "Kenapa tidak?"

    eve "Karena, aku tidak akan membantu {b}Odette{/b} merayu adikku!"

    eve "Itu akan menjadi aneh."

    anon "Mengapa itu aneh?"

    anon "Anda ingin {b}Grace{/b} bahagia, bukan?"

    eve "Tentu saja aku tahu!"

    eve "Tapi, itu {b}Odette{/b}... Dan adikku..."

    anon "Jadi?"

    eve f_sad_down a_idle "{i}*Huh*{/i} Entahlah, mungkin kamu benar."

    pause
    eve f_normal "Saya rasa tidak ada salahnya untuk mencoba."

    anon @ f_laugh "Tepat."

    pause
    eve f_happy "Anda harus datang malam ini, dan kita akan membicarakannya dengan {b}Odette{/b}."

    anon @ f_flirt "Saya bisa melakukan itu."

    eve @ f_laugh "Luar biasa!"

    eve "Setelah itu, saya akan bersorak lagi di {i}Street Kombat{/i}!"

    anon @ f_snarky a_point "Oh, kamu sangat terpuruk kali ini!"

    eve @ f_laugh "Haha!"

    roxxy "Hey, freak!" with hpunch
    show eve f_surprised:
        flip
        xoffset 100
    show becca f_upset:
        xoffset 100
    show missy f_angry:
        xoffset -50
    show roxxy f_angry:
        xoffset -200
    show anon f_surprised:
        xoffset -175
    with dissolve
    anon "{b}Roxxy{/b}?"

    show roxxy m_talk
    if M_roxxy.finished_state(S_roxxy_picnic_done):
        roxxy "Minggir, {b}[firstname]{/b}!"

    else:
        roxxy "Minggir, pecundang!"

    show anon f_surprised_teeth
    show roxxy b_dressed_toes with dissolve
    roxxy "Menurutmu itu lucu, mengolok-olok orang?!"

    show roxxy b_dressed -m_talk with dissolve
    eve f_confused "Hah?"

    roxxy "Aku tahu kaulah yang mengacak-acak rambutku!"

    becca "Dan kulitku!"

    eve a_hip f_normal @ f_eyeroll "Aku tidak tahu apa yang kamu bicarakan..."

    roxxy "Jangan mencoba dan menyangkalnya!"

    missy "Kamu menggambar penis di dahiku!"

    eve f_happy @ f_laugh "Ha ha ha!"

    missy @ -m_talk "..."
    becca "Kami tahu itu kamu!"

    show anon f_surprised_left
    eve "Bisakah Anda membuktikannya?"

    show anon f_surprised
    roxxy "Saya tidak perlu membuktikannya!"

    if M_roxxy.finished_state(S_roxxy_picnic_done):
        show roxxy b_empty zorder 2:
            xoffset -125
            yoffset 6
        show anon f_surprised_teeth b_pulling1 zorder 1:
            xoffset -120
        show becca:
            xoffset 150
        show missy:
            xoffset 20
        with dissolve
        show eve f_surprised
        roxxy "Ayo, {b}[firstname]{/b}!"

        roxxy "Aku tidak ingin kamu bergaul dengan wanita jalang jelek ini lagi!"

        eve f_angry "H-hei!"

        show eve b_empty zorder 2:
            xoffset -118
        show anon b_pulling2 f_surprised_left
        with dissolve
        eve "Anda tidak bisa mengendalikannya!"

        show anon f_surprised b_pulling3 with dissolve
        roxxy "Lepaskan!"

        show anon b_pulling2 f_surprised_left with dissolve
        eve "TIDAK!"

        show anon b_pulling3 f_surprised with dissolve
        pause
        anon "Oke, kalian berdua harus tenang..."

        show missy f_normal
        show anon b_pulling2 with dissolve
        eve "Dia bisa bergaul dengan siapa pun yang dia mau!"

        show anon f_hurt
        missy "Ini agak panas."

        becca @ f_eyeroll "Diam, {b}Nona{/b}..."

        show anon b_pulling3 with dissolve
        roxxy "Sebaiknya kau mundur saja, jalang!"

        show anon b_pulling2 with dissolve
        eve "Atau apa?!"

        show anon b_pulling3 with dissolve
        roxxy "Grr!"

        show anon b_pulling2 with dissolve
        eve "Aku tidak takut padamu!"

        show anon b_dressed a_up f_angry:
            xoffset 100
        show eve b_dressed f_surprised
        show roxxy b_dressed
        with dissolve
        anon "Itu sudah cukup!"

        show anon a_surprised
        roxxy "Kamu sudah mati..."

    else:
        roxxy "Tahukah kamu berapa lama waktu yang aku perlukan untuk membersihkan kotoran itu?!"

        eve "Saya harap sudah lama sekali!"

        roxxy "Jadi kamu mengakuinya?!"

        show anon f_surprised_left
        eve "Tidak, aku tidak mengakui apa-apa..."

        eve @ f_laugh "... Tapi Anda pasti pantas mendapatkannya!"

        show anon f_worried
        anon "Oke, semua orang harus tenang..."

        roxxy "Diam, {b}[firstname]{/b}!"

        eve "Hei, jangan bicara seperti itu padanya!"

        roxxy "Atau apa?!"

        pause
        show anon f_surprised
        roxxy "Mungkin aku harus mengacak-acak rambutmu?"

        show anon f_surprised_left
        eve "Aku tidak takut padamu!"

        anon f_angry "Itu sudah cukup!"

        roxxy "Sebaiknya kau dengarkan temanmu, aneh!"

    eve f_angry "Persetan, trailer sampah Barbie!"

    roxxy f_glaring @ -m_talk "!!!"
    show roxxy b_jump with dissolve
    show missy f_surprised
    show becca f_surprised
    show anon f_shock
    show eve f_surprised a_arrest
    roxxy "Raaaah!"

    show anon f_surprised_left
    hide eve
    hide roxxy
    eve "!!!" with hpunch
    becca "Sialan!"

    anon "{b}Roxxy{/b} berhenti!"


    scene location_school_right_hall_cutscene_02
    with fade
    eve "Aaahh!!"

    roxxy "Inilah yang terjadi!"

    eve "Lepaskan aku!"

    roxxy "Saat kamu macam-macam denganku!"

    eve "Aaahh!!"


    scene location_school_right_hall_cutscene_03
    with fade
    eve "{i}*Chomp*{/i}" with hpunch
    roxxy "!!!"
    roxxy "OOOWWWW!!!"

    anon "{b}Malam{/b}!"

    roxxy "Dasar jalang!"

    roxxy "AAAHHHH!!!"


    scene expression player.location.background_closeup
    show anon f_surprised
    show eve b_dressed_disheveled f_angry:
        flip
        xoffset -100
    show roxxy a_ouch f_glaring
    with fade
    roxxy "Kamu menggigitku!"

    eve "Benar sekali!"

    smith "Apa yang terjadi di sini?!"

    show anon f_sad_down
    anon "Oh, sial..."

    show smith f_angry
    show roxxy:
        flip
        xoffset 250
    with dissolve
    show anon f_hurt
    smith "Apakah kalian sudah kehilangan akal sehat?"

    roxxy f_angry "Dia memulainya!"

    show anon f_tired
    eve "APA?!"

    eve "Kaulah yang memulainya!"

    smith "That's enough!" with hpunch
    smith "Saya tidak akan mentolerir perilaku seperti ini di sekolah saya!"

    smith "Penahanan untuk kalian semua!"

    show anon f_depressed
    roxxy f_glaring "Dengan serius?"

    eve "Aduh, ayolah!"

    missy "Itu tidak adil!"

    becca "Ya, kami bahkan tidak melakukan apa pun!"

    smith "Silence!" with hpunch
    smith "Aku tidak mau berdebat dengan sekelompok bocah ingusan!"

    smith "Itu tugas {b}Annie{/b}."

    pause
    smith "Sekarang, ayo pergi!"

    roxxy f_angry_right "Bagus sekali, jalang..."

    eve "{i}*Huh*{/i} Diam, {b}Roxxy{/b}."

    show roxxy f_surprised
    show anon f_surprised_teeth
    show eve f_surprised
    smith @ f_scream "I SAID MOVE IT!" with hpunch
    scene black with fade
    pause
    $ player.go_to(L_school_frenchclassroom)
    scene expression player.location.background_blur with None
    show anon f_worried
    show eve a_hip:
        flip
        xoffset -100
    show roxxy:
        flip
        xoffset 250
    show annie f_annoyed
    with dissolve
    annie "Baiklah pembuat masalah, Anda tahu caranya."

    annie "Tidak boleh bicara, tidak boleh ada ponsel, tidak boleh makan atau minum-"

    roxxy @ f_eyeroll a_cross "Oh bagus, kita bisa menghabiskan empat jam berikutnya dengan orang bodoh ini..."

    eve f_happy @ f_laugh "Heh, iya... Dia satu-satunya orang di sekolah ini yang lebih kubenci daripada kamu..."

    roxxy @ f_laugh "Ha ha ha!"

    annie @ f_angry "Hei, aku bilang jangan bicara!"

    roxxy @ f_pouting_hair "Psh."

    eve f_disgusted "Hidung coklat yang aneh."

    annie "Apa yang kamu katakan?"

    eve f_sexy "Bukankah sebaiknya kamu pergi berciuman {b}Ny. Kaki Smith{/b} atau apalah?"

    roxxy @ f_laugh "Ha ha ha!"

    annie f_angry a_note @ a_note_write "Kalian berdua baru saja membeli penahanan lagi!"

    eve @ f_eyeroll "Ugh, kita hancur..."

    annie @ a_note_write "Anda baru saja membeli satu lagi, di sana!"

    show anon f_depressed
    roxxy "Yah, aku juga bebas lusa."

    roxxy "Selain itu, saya harus memeriksa kalender saya!"

    eve @ f_laugh "Ha ha ha!"

    annie "Bagus, karena akan diisi dengan penahanan!"

    show eve f_angry
    roxxy f_pouting @ -m_talk "..."
    annie "Apakah kamu sudah selesai?"

    roxxy f_normal "Tidak."

    show eve f_sexy
    annie @ a_note_write "Itu satu lagi!"

    pause
    annie "Saya bisa melakukan ini sepanjang hari."

    show anon f_worried
    eve "Jadi?"

    annie @ a_note_write "Itu satu lagi!"

    eve @ -m_talk "..."
    annie f_annoyed "Kami akan terus berjalan..."

    annie "Katakan saja."

    roxxy "Pergi."

    eve @ f_laugh "Ha ha ha!"

    annie @ a_note_write "Anda baru saja membeli satu lagi!"

    annie "Kamu pikir aku punya sesuatu yang lebih baik untuk dilakukan?"

    eve "Kami tahu Anda tidak punya hal lain yang lebih baik untuk dilakukan..."

    roxxy @ f_laugh "Haha!"

    annie "Apa itu tadi?"

    eve @ -m_talk "..."
    anon "Teman-teman, hentikan!"

    annie "Saya akan menemui Anda berdua di sini setiap hari selama sisa hidup alami Anda jika Anda tidak berhati-hati!"

    roxxy f_pouting @ -m_talk "..."
    eve f_angry @ -m_talk "..."
    annie "Itulah yang saya pikirkan..."

    annie f_angry a_idle @ a_point1 "Sekarang, duduklah!"

    hide eve
    hide roxxy
    with dissolve
    anon f_tired "Astaga."

    scene black with fade
    pause
    scene expression player.location.background_blur
    show anon b_desk f_sad_down:
        xoffset 600
    show eve b_desk_look_left f_sad_down:
        xoffset 300
    show roxxy b_desk_bored f_pouting:
        xoffset -50
    with fade
    pause
    anon @ -m_talk "..."
    pause
    show eve f_nervous_right
    pause
    eve "Hai, {b}Roxxy{/b}."

    show anon f_worried_left
    eve "Ssst."

    roxxy f_worried "Apa?"

    eve f_happy_right "Akan sangat disayangkan jika orang iseng yang membuatmu mengejar {b}Annie{/b} selanjutnya, bukan begitu?"

    show roxxy b_desk_normal with dissolve
    roxxy f_normal "Hah?"

    pause
    roxxy @ f_surprised "Oh."

    roxxy f_sexy @ f_laugh "Haha, ya!"

    roxxy "Wanita jalang itu benar-benar siap melakukannya!"

    eve @ f_laugh "Haha!"

    show anon f_normal_left
    roxxy "Pastikan saja itu sesuatu yang benar-benar memalukan..."

    eve "Benar sekali."

    pause
    anon f_thinking @ -m_talk "(Hah.)"

    anon @ -m_talk "(Tiba-tiba mereka bertingkah sangat ramah...)"

    anon f_normal_left @ -m_talk "(Apakah mereka benar-benar terikat karena kebencian yang sama terhadap {b}Annie{/b}? )"

    pause

    scene location_school_french_cutscene16
    show text _ ("I wasn't sure what {b}Eve{/b} was plotting but it was nice to see her and {b}Roxxy{/b} getting along for once.\nEven if it did spell trouble for {b}Annie{/b}...") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I just hope it doesn't land {b}Eve{/b} more detention!\nI can't imagine doing this every night for a week straight!") as caption with dissolve
    pause

    $ game.timer.tick(3)
    $ player.go_to(L_school_front)
    scene expression player.location.background_blur
    show eve f_eyeroll
    show anon f_depressed
    with fade
    eve "Ugh, empat jam terlama, PERNAH!"

    show eve f_normal
    anon f_tired "Ya, ceritakan padaku tentang hal itu..."

    pause
    eve @ f_sad_down "Maaf aku membuatmu ditahan."

    anon f_worried "Tidak apa-apa."

    show eve f_nervous
    pause
    anon "Maaf {b}Roxxy{/b} mencoba memenggal kepalamu."

    eve "Ya."

    pause
    anon f_normal @ f_laugh "Aku tidak percaya kamu menggigit payudaranya!"

    eve f_laugh "Yah, aku harus melakukan sesuatu..."

    eve "Dia mencoba membekapku dengan benda raksasa itu!"

    anon @ f_laugh "Ha ha ha!"

    eve @ f_laugh "Ha ha ha!"

    show eve f_normal
    pause
    eve f_sad_down "Sobat, {b}Grace{/b} akan marah ketika dia mendengar aku ditahan selama seminggu berturut-turut!"

    anon "Setidaknya kamu dan {b}Roxxy{/b} meninggalkan hubungan yang baik..."

    eve "Ya, menurutku."

    pause
    eve f_sad "{i}*Sigh*{/i} Aku mungkin harus pulang."

    anon "Ya, aku juga."

    eve "Sayang sekali rencana kita hancur..."

    anon "Hehe, jangan khawatir."

    anon f_snarky "Saya hanya perlu menendang pantat Anda di {i}Street Kombat{/i} di lain hari."

    eve f_happy @ f_laugh "Hehe, ya benar!"

    eve "Dalam mimpimu."

    anon f_normal @ f_laugh "hehe!"

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    pause
    eve "Sampai jumpa besok?"

    anon "Tentu saja."

    pause
    show eve f_happy
    show anon b_dressed f_normal
    with dissolve
    eve "Oke."

    pause
    eve @ a_wave "Sampai jumpa."

    anon @ a_wave "Nanti, {b}Malam{/b}."

    hide anon with dissolve
    return

label eve_button_voyeurism_follow_roof:
    scene expression player.location.background_closeup with None
    show anon
    show eve
    with dissolve
    anon "Wah, ini luar biasa!"

    eve f_happy "Hehe, menurutmu begitu?"

    anon "Tentu saja!"

    pause
    anon "Ini semua milik {b}Tuuku{/b}?"

    eve "Sebagian besar, ya."

    eve "Dia kadang-kadang membutuhkan tempat untuk tidur atau bersembunyi dan {b}Grace{/b} tidak mengizinkannya masuk ke apartemen."

    eve "Jadi dia membangun semua ini."

    anon "Apakah speaker itu berfungsi?"

    eve "Jika kita mencolokkannya, tentu saja."

    eve "{b}Tuuku{/b} terkadang suka memutar musik untuk tanamannya."

    anon f_worried "Dia memainkan musik untuk tanaman ganjanya?"

    eve @ f_laugh "Hehe, ya."

    eve "Dia mengatakan itu membantu mereka tumbuh."

    anon f_normal @ f_confused "Apakah itu benar-benar berhasil?"

    eve @ f_eyeroll "Tidak tahu."

    pause
    anon @ f_laugh "Ini sangat keren!"

    eve "Mengapa kamu tidak duduk di sana dan aku akan mengambilkan kita bir."

    anon f_worried "Y-maksudmu di pinggir atap?"

    eve "Ya."

    pause
    eve "Anda tidak takut ketinggian, bukan?"

    anon "T-tidak, aku tidak takut ketinggian..."

    hide eve with dissolve
    eve "hehe!"

    anon f_sad_down "Aku takut terjatuh."

    hide anon with dissolve
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg" with None
    show eve b_sidebed f_disgusted a_beer_hold
    show anon b_sit:
        yoffset 20
    with dissolve
    eve "Aduh, mereka seksi."

    pause
    eve f_happy "Anda menginginkannya?"

    anon f_unimpressed "Anda bertanya apakah saya ingin bir panas?"

    eve @ f_laugh "Hehe, ya."

    pause
    anon "Sudah berapa lama di sini lagi?"

    eve "Tidak tahu."

    pause
    anon "Saya pikir saya akan lulus."

    show anon f_normal
    eve "Mungkin langkah yang cerdas..."

    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "UEGH!!"

    eve f_disgusted "Oke, jelas merupakan langkah yang cerdas."

    eve "Itu mengerikan!"

    anon @ f_laugh "Haha!"

    pause
    eve f_happy "Pemandangannya bagus sekali, bukan?"

    anon "Ya, Anda dapat melihat hampir seluruh kota dari sini..."

    eve "Ya, cukup banyak."

    pause
    anon "Jadi ceritakan lebih banyak tentang {b}Odette{/b} dan {b}Grace{/b}."

    eve @ f_confused -m_talk "Hmm?"

    eve f_nervous "Oh benar."

    eve "Sebenarnya tidak banyak yang perlu dibicarakan."

    eve @ f_eyeroll "{b}Odette{/b} naksir {b}Grace{/b} selamanya."

    anon @ f_confused "Saya pikir mereka hanya berteman?"

    eve "Ya, itulah yang saya katakan."

    eve "Mereka hanya berteman dan sudah berteman sejak mereka masih kecil tapi..."

    eve "... {b}Odette{/b} ingin menjadi lebih."

    anon "Dan adikmu tidak?"

    eve @ f_eyeroll "Adikku tidak tahu {b}Odette{/b} menyukainya..."

    anon @ f_surprised "Benar-benar?"

    eve "Ya."

    eve "Itu hal yang paling aneh."

    eve "{b}Odette{/b} selalu mampu merayu pria mana pun yang diinginkannya dengan mudah..."

    anon "Eh ya."

    eve "Ini seperti, mudah sekali baginya."

    eve "... Tapi jika menyangkut adikku, dia berubah menjadi orang yang sama sekali berbeda."

    eve "Dia menjadi sangat canggung dan kikuk, selalu mengatakan hal yang salah..."

    eve "Agak lucu, kalau boleh jujur."

    anon "Sepertinya dia sedang jatuh cinta."

    eve f_laugh "Haha, ya benar!"

    eve "{b}Odette{/b} sedang jatuh cinta."

    eve f_happy "Bagus."

    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "Ya."

    anon @ f_confused "Kenapa kamu masih meminum minuman itu?"

    eve @ f_burp "{i}*Bersendawa*{/i}"

    eve f_nervous_down "Saya punya perasaan sebelum malam berakhir, saya akan membutuhkannya..."

    anon f_worried "Maksudnya itu apa?"

    eve f_nervous @ f_laugh "Hehe, sudahlah."

    show anon f_thinking
    pause
    anon f_normal @ f_confused "Jadi, {b}Odette{/b} itu bi?"

    eve "Sepertinya begitu."

    anon "Dan adikmu tidak?"

    eve "Sejauh yang saya tahu, dia tidak."

    anon @ -m_talk "Mmhmm."

    pause
    anon f_skeptical "Bagaimana denganmu?"

    eve f_nervous_down "A-aku?"

    anon f_flirt "Ya kamu."

    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "Ya."

    eve f_nervous_down "Entahlah..."

    anon f_normal "Anda tidak tahu?"

    eve "Aku tidak pernah benar-benar memikirkannya."

    pause
    anon @ f_laugh "Hehe, baiklah, pikirkanlah!"

    pause
    eve "Saya kira saya bisa saja menjadi seperti itu."

    anon @ f_surprised "Benar-benar?"

    eve f_nervous "Maksudku, ya, dengan gadis yang tepat..."

    eve "Gender tidak sepenting kepribadian... Setidaknya, itulah yang saya pikirkan."

    anon f_flirt "Menarik."

    show eve f_nervous_down
    pause
    eve f_nervous "Bagaimana denganmu?"

    anon f_surprised @ -m_talk "Hmm?"

    eve "Bisakah Anda membayangkan diri Anda bersama pria lain?"

    show anon f_thinking
    menu:
        "Mustahil.":
            anon f_unimpressed "Cowok itu menjijikkan!"

            eve f_happy @ f_disgusted "Jadi, maksudmu... Kamu menjijikkan?"

            anon f_normal @ f_laugh "Oh, tentu saja!"

            anon "Aku tidak tahu bagaimana kamu bisa bertahan denganku..."

            anon "... aku menjijikkan!"

            eve @ f_laugh "Ha ha ha!"

            eve "Kamu selalu tahu cara membuatku tertawa!"

            anon "Itu hal yang bagus, ya?"

            eve "Ya, sangat bagus."

            $ M_eve.set("biggus_dickus", "")
        "Mungkin.":

            anon f_shy "Aku tidak tahu."

            anon "Saya tidak pernah memikirkannya."

            pause
            eve f_happy @ f_laugh "Ha ha ha!"

            anon f_normal "Apa?"

            eve "Nah, pikirkanlah!"

            anon "Hehe, baiklah."

            show anon f_thinking
            show eve f_drink a_beer_drink with dissolve
            pause
            show eve f_disgusted a_beer_hold with dissolve
            anon @ -m_talk "Hmm."

            pause
            eve f_happy "Dengan baik?!"

            anon "saya sedang berpikir!"

            eve @ f_laugh "Ha ha ha!"

            pause
            anon f_shy "Saya kira saya setuju dengan Anda..."

            anon f_normal @ f_brag_closed "Kepribadian lebih penting daripada gender."

            eve f_surprised "Benar-benar?"

            anon "Ya."

            eve f_nervous_down "Saya tidak mengharapkan itu."


    show eve f_drink a_beer_drink with dissolve
    pause
    eve a_beer_hold f_disgusted_wince_down "Eugh, aku tidak akan pernah terbiasa dengan hal ini."

    anon "Berhenti meminumnya!"

    eve f_disgusted "Tidak, tidak, tidak... Percayalah, aku membutuhkannya."

    anon f_confused "Untuk apa?"

    eve "Hanya-"

    pause
    eve f_nervous "Diam saja!"

    anon f_normal "Oke..."

    eve f_nervous_down a_idle "Di Sini."

    show eve f_nervous a_paper
    show expression "characters/eve/eve_arms_sidebed_a_paper.png"
    with dissolve
    anon "Apa ini?"

    eve "Ini untukmu."

    eve f_nervous_down "Aku uhh... Agak... Dibuat untukmu."

    hide expression "characters/eve/eve_arms_sidebed_a_paper.png"
    show eve a_idle
    show anon f_surprised a_paper
    with dissolve
    anon "Benar-benar?"

    scene expression player.location.background_blur
    show expression "objects/closeup_drawing_02.png" as drawing with fade
    anon "Wah!"

    pause
    anon "Anda menggambar ini?"

    eve "Y-ya."

    pause
    eve "Anda menyukainya?"

    anon "Saya menyukainya!"

    pause
    hide drawing
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed f_happy
    show anon b_sit a_paper zorder 1:
        yoffset 20
    with fade
    anon "Aku tidak percaya kamu membuatkan ini untukku!"

    eve "Y-yah, kemarin kamu bilang kamu menyukai semua hal tentang Bonnie dan Clyde..."

    anon "Ya, saya ingat!"

    eve f_nervous_down "... Dan aku memikirkanmu dan mencoret-coret, dan... Itu hanya... Agaknya, terjadi."

    anon "Keren banget, {b}Eve{/b}!"

    anon "Terima kasih!"

    eve f_happy @ f_laugh "Hehe, sama-sama."

    pause
    anon @ f_laugh "Wow, lihat dirimu mengenakan gaun itu!"

    eve f_nervous_down "K-kamu suka itu?"

    anon "Tentu saja!"

    anon f_flirt "Kamu terlihat seksi!"

    eve f_happy @ f_laugh "Diam!"

    anon "Apa?!"

    anon f_normal "Anda melakukannya!"

    pause
    show anon a_idle with dissolve
    pause
    show eve f_nervous_down
    pause
    eve "Terima kasih, ngomong-ngomong..."

    anon @ -m_talk "Hmm?"

    eve f_nervous "Untuk menyemangatiku beberapa hari yang lalu!"

    anon "Tentu saja."

    pause
    show eve f_nervous_down
    pause
    anon f_flirt "Jadi, kamu memikirkanku, ya?"

    eve f_surprised @ -m_talk "!!!"
    eve "Hehe, uhh..."

    eve f_nervous @ f_laugh "Subjek baru!"

    anon f_normal "Ah, ayolah!"

    eve "Oh, aku punya ide!"

    hide eve with dissolve
    anon @ f_worried "Kemana kamu pergi?"

    eve "Tunggu sebentar."

    pause
    eve "Aku tahu mereka ada di sini, di suatu tempat..."

    pause
    anon "Apakah Anda memerlukan bantuan?"

    eve "Tidak, aku mengerti."

    pause
    eve "Ah hah!"

    pause
    show eve b_sidebed f_happy a_binocular zorder 0 with dissolve
    eve "Menemukannya."

    anon @ f_confused "Teropong?"

    eve "Ya."

    eve "Seperti yang Anda katakan, kita bisa melihat seluruh kota dari sini."

    eve @ f_laugh "Jadi, mari kita ajak beberapa orang menonton!"

    anon "Anda ingin memata-matai orang?"

    eve f_confused "Anda belum pernah melakukan itu sebelumnya?"

    anon f_worried_low "T-tidak..."

    eve f_happy @ f_eyeroll "Ya benar."

    anon "Oke, mungkin sedikit..."

    eve "Pembohong!"

    show eve f_normal_out a_binocular_look with dissolve
    show anon f_normal
    pause
    eve @ -m_talk "Hmm."

    anon "Anda melihat sesuatu?"

    eve "Belum."

    pause
    eve "Sepertinya {b}Tyrone{/b} dan anak buahnya tidak ada di taman malam ini."

    anon @ f_laugh "Heh, ya... Mereka mungkin di rumah masih mencoba membersihkan bom bau itu!"

    show eve a_binocular with dissolve
    eve @ f_laugh "Ha ha ha!"

    pause
    show eve f_normal_out a_binocular_look with dissolve
    pause
    eve "Ya Tuhan..."

    anon @ -m_talk "Hmm?"

    eve "Ada dua wanita bertelanjang dada sedang jogging di taman!"

    show anon f_shock:
        flip
        xoffset -350
    with fastdissolve
    anon "T-topless?"

    anon f_normal_out "Anda berbohong."

    show eve a_binocular_give
    show expression "characters/eve/eve_arms_sidebed_a_binocular_give.png" zorder 2
    with dissolve
    eve "Tidak serius!"

    show anon a_binocular
    show eve f_normal_out a_point
    hide expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    show expression "characters/eve/eve_arms_sidebed_a_point.png" zorder 2
    with dissolve
    eve "Coba lihat!"

    show eve a_idle
    hide expression "characters/eve/eve_arms_sidebed_a_point.png"
    show anon a_binocular_look
    with dissolve
    pause
    anon "!!!"
    scene expression "backgrounds/location_tattoo_rooftop_spy01.jpg" with fade
    pause
    anon "{b}M-Nyonya. Johnson{/b}?"

    eve "Apakah Anda kenal mereka?"

    anon "Eh, ya..."

    anon "Si rambut merah adalah induk semang temanku."

    eve "Wah, benarkah?"

    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed
    show anon b_sit a_binocular_give:
        flip
        xoffset -350
        yoffset 20
    with fade
    anon "Anda tahu {b}Erik{/b}?"

    show anon a_idle
    show eve a_binocular f_confused
    with dissolve
    eve "Anak gendut dengan semua bintik-bintiknya?"

    anon "Y-ya."

    show eve f_normal_out a_binocular_look with dissolve
    eve "Itu induk semangnya?!"

    anon "Ya."

    eve "Wow, dia sangat seksi..."

    anon f_flirt "... Ya."

    pause
    eve "Aku ingin tahu siapa gadis lainnya?"

    anon f_normal @ f_skeptical "Salah satu temannya dari kelas yoga, menurutku..."

    pause
    eve "Mengapa mereka bertelanjang dada?"

    anon "Tidak tahu."

    pause
    eve "Hmm, keriting."

    pause
    eve "!!!"
    pause
    eve "Hehe lagi?"

    show eve f_sexy a_binocular_give
    show expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    with dissolve
    eve "Anda akan menyukai yang ini..."

    anon f_normal_left @ -m_talk "Hmm?"

    show anon a_binocular
    show eve f_normal_out a_point
    hide expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    show expression "characters/eve/eve_arms_sidebed_a_point.png"
    with dissolve
    eve "Gedung apartemen di sana, lantai dua, jendela paling kiri."

    hide expression "characters/eve/eve_arms_sidebed_a_point.png"
    show eve a_idle f_sexy
    show anon f_normal_out a_binocular_look
    with dissolve
    anon "O-oke."

    pause
    anon "!!!"
    scene expression "backgrounds/location_tattoo_rooftop_spy02.jpg" with fade
    anon "Apakah itu-"

    eve "Itu {b}Ny. Kim{/b}."

    eve "Dia bekerja di konter di bank..."

    anon "Y-ya, aku pernah melihatnya di sana sebelumnya."

    pause
    anon "Dia sedang melakukan masturbasi..."

    pause
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed f_sexy
    show anon b_sit f_normal_out a_binocular_look:
        flip
        xoffset -350
        yoffset 20
    with fade
    anon "Apakah itu suaminya yang berbaring di sebelahnya?"

    eve "Ya, yang gemuk dan jelek."

    pause
    show anon f_normal_left a_binocular with dissolve
    eve "Dia sering melakukan ini."

    show eve a_binocular
    show anon a_idle
    with dissolve
    anon "Maksudmu, kamu pernah memata-matainya sebelumnya?"

    eve "Ya, {b}Tuuku{/b} menemukannya suatu hari ketika kami semua ada di sini."

    show eve f_normal_out a_binocular_look with dissolve
    eve "Dia mengawasinya sepanjang waktu."

    anon "Agak menyeramkan, bukan?"

    eve "Yah, dialah yang melakukan masturbasi di depan jendela..."

    eve "Jika dia tidak ingin orang lain melihatnya, dia harus membeli tirai!"

    pause
    anon "Ya, saya kira itu benar."

    eve "Aku hanya merasa kasihan padanya."

    eve "Anda tahu suaminya mungkin tidak dapat memenuhi kebutuhannya..."

    anon f_surprised_left @ -m_talk "..."
    pause
    eve "Hmm, tidak ada yang terjadi di perpustakaan malam ini."

    show anon f_normal_out
    eve "Itu tidak biasa."

    anon "Apakah itu?"

    show eve f_happy a_binocular with dissolve
    eve "Benar sekali."

    eve "Sejak mereka mulai mengadakan pertemuan pecandu seks di sana, banyak orang yang bercinta di mana-mana."

    show eve f_normal_out a_binocular_look with dissolve
    anon f_normal @ f_normal_left "Benar-benar?"

    eve "Hehe, ya."

    pause
    eve "!!!"
    pause
    eve "Aduh."

    anon f_normal_left "Apakah Anda menemukan sesuatu?"

    eve "Ya."

    show eve a_binocular_give f_happy
    show expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    with dissolve
    eve "Anda ingin melihat di sepanjang garis pantai untuk mencari dermaga."

    show anon f_normal_out a_binocular
    show eve a_point f_normal_out
    hide expression "characters/eve/eve_arms_sidebed_a_binocular_give.png"
    show expression "characters/eve/eve_arms_sidebed_a_point.png"
    with dissolve
    eve "Di sebelah sana."

    show anon a_binocular_look
    hide expression "characters/eve/eve_arms_sidebed_a_point.png"
    show eve a_idle
    with dissolve
    anon "Oke."

    pause
    anon "!!!"
    scene expression "backgrounds/location_tattoo_rooftop_spy03.jpg" with fade
    anon "Saya melihat mereka."

    eve "Mereka menyaksikan matahari terbenam bersama."

    eve "Bukankah itu romantis?"

    anon "Y-ya, menurutku."

    pause
    anon "Menurutku dia telanjang."

    pause
    scene expression "backgrounds/location_tattoo_rooftop_ledge.jpg"
    show eve b_sidebed f_eyeroll
    show anon b_sit f_normal_out a_binocular_look:
        flip
        xoffset -350
        yoffset 20
    with fade
    eve "Tipikal pria..."

    eve f_happy "Dua orang berbagi momen indah bersama dan yang Anda pedulikan hanyalah dia telanjang."

    show anon f_normal_left a_binocular with dissolve
    pause
    show anon a_idle
    show eve a_binocular
    with dissolve
    anon "Hehe, maaf."

    show eve f_normal_out a_binocular_look with dissolve
    eve "Tidak, tidak apa-apa... Aku mengerti."

    pause
    eve "Dia sangat cantik."

    pause
    eve @ -m_talk "Hmm."

    pause
    eve "Saya rasa itu saja."

    show eve a_idle f_happy
    hide anon
    show anon b_sit:
        yoffset 20
    with dissolve
    pause
    anon "Jadi..."

    pause
    anon "Sekarang apa?"

    eve f_nervous_down a_cover "Di sini agak dingin, bukan?"

    anon "Sedikit."

    eve "Mengapa kita tidak memeriksa tendanya?"

    eve "Mungkin di sana lebih hangat."

    anon "Apakah kamu yakin {b}Tuuku{/b} tidak keberatan?"

    eve f_happy @ f_laugh "Ya, selama kita tidak merusak barangnya."

    eve "Ayo, aku akan balapan denganmu!"

    hide eve with dissolve
    anon f_unimpressed @ f_worried "Hei, tidak adil!"

    eve "Ha ha ha!"

    anon "Penipu."

    return

label eve_button_voyeurism_meetup:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    anon "Hai."

    eve "Hai, {b}[firstname]{/b}."

    eve "Anda masih {b}datang malam ini{/b}?"

    anon @ f_laugh "Ya, aku akan ke sana."

    eve "Saya akan mencarikan kita sesuatu yang SANGAT menakutkan untuk ditonton!"

    anon "Hehe, tidak sabar."

    eve "Ya, aku juga tidak!"

    hide anon with dissolve
    return

label eve_button_voyeurism_start:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_happy
    with dissolve
    anon @ a_wave "H-hei."

    eve "{b}[firstname]{/b}!"

    hide eve
    show anon b_hug_eve f_shy_down
    with dissolve
    eve "Senang bertemu denganmu!"

    anon "Heh, suasana hatimu sedang bagus hari ini..."

    eve "Terima kasih!"

    show anon b_dressed f_normal a_behind_head
    show eve f_happy
    with dissolve
    anon "Aku senang kamu merasa lebih baik."

    eve @ f_laugh "Ya, jauh lebih baik."

    pause
    eve "Katakan, apakah kamu sibuk malam ini?"

    anon a_idle @ -m_talk "Hmm?"

    anon "Saya masih belum yakin, kenapa?"

    eve "Anda ingin datang dan jalan-jalan?"

    anon "Ya baiklah."

    eve "{b}Grace{/b} dan {b}Odette{/b} sedang menuju ke kota untuk mengambil senjata tato bekas yang {b}Grace{/b} temukan secara online."

    eve "Jadi, kita harus memiliki rumah untuk diri kita sendiri untuk sementara waktu."

    anon "Oh?"

    eve "Ya, kupikir kita bisa mengeluarkan beberapa bir {b}Odette{/b} dari lemari es dan menonton film seram atau semacamnya?"

    anon @ f_laugh "Aku kecewa karena itu!"

    eve @ f_laugh "Luar biasa!"

    eve "Saya sangat bersemangat!"

    anon @ a_wave "{b}Sampai jumpa malam ini{/b}."

    eve @ a_wave "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return

label eve_button_police_trouble:
    scene expression player.location.background_closeup
    show grace f_angry a_hips_mad
    show eve f_sad_down:
        flip
    with fade
    grace "Ya, bagus sekali... Bolehkah aku menggunakan permintaan maafmu untuk membayar denda ini?!"

    eve @ -m_talk "..."
    grace "Tiga ribu dolar, {b}Malam{/b}!"

    grace "Anda tahu, kita hampir tidak bisa bertahan seperti sekarang!"

    eve f_sad_down @ a_wipe_tears "{i}*Mengendus*{/i} Saya tahu..."

    grace f_weary a_facepalm "Aku tidak percaya kamu melakukan ini..."

    pause
    eve f_sad "Ini tidak adil, semua orang melakukannya!"

    grace f_angry a_hips_mad "Tidak, mereka tidak melakukannya."

    eve f_sad_down "{i}*Sniff*{/i} Kamu dan {b}Odette{/b} melakukan..."

    grace @ a_idea "{b}Malam{/b}, ada perbedaan besar antara sesekali merokok di rumah dan berjalan-jalan di depan umum dengan setengah pon ganja di saku Anda!"

    eve @ -m_talk "..."
    grace "Menurutmu apa yang akan terjadi?!"

    eve "{i}*Mengendus*{/i} Maaf..."

    grace @ f_angry_yelling_closed a_upset "Aku akan membunuh {b}Tuuku{/b} saat kita sampai di rumah!"

    eve f_surprised "Dia tidak terlibat dalam hal ini!"

    grace "Pfft, ya benar... Aku tidak percaya itu sedetik pun."

    eve "Dia tidak!"

    show grace f_eyeroll
    pause
    show eve f_cry_down a_wipe_tears with dissolve
    grace f_weary a_facepalm "Naik saja sepedanya dan ayo keluar dari sini..."

    hide eve with dissolve
    grace f_angry_yelling_closed a_upset "Grr, aku tidak tahu apa yang akan kita lakukan!"

    hide grace with dissolve
    scene expression player.location.background_blur
    show anon f_worried
    with fade
    anon @ -m_talk "(Kedengarannya buruk.)"

    anon @ -m_talk "( Kasihan {b}Malam{/b}... )"

    hide anon with dissolve
    return

label eve_button_prank_douches_park:
    scene expression player.location.background_closeup with None
    show eve f_happy_right:
        flip
        xoffset 250
    show anon f_worried:
        xoffset -100
    show tuuku:
        xoffset 50
    with dissolve
    anon "{b}Malam{/b}?"

    show anon f_normal
    eve f_happy a_hip "Lihat, sudah kubilang dia akan datang."

    eve f_happy_right "Hai, {b}[firstname]{/b}!"

    anon "Apa yang terjadi?"

    eve "Tidak banyak."

    show eve f_happy
    tuuku "Ahh, aku ingat orang ini..."

    tuuku "Anda berada di toko tato beberapa hari yang lalu!"

    anon "Ya, itu aku."

    tuuku f_happy "Kalian berdua bercinta?"

    anon f_surprised "!!!"
    eve f_surprised a_rossed "APA?!"

    anon f_worried a_behind_head "Uhh..."

    eve f_angry "Jangan jawab itu {b}[firstname]{/b}!"

    eve "Dia hanya menjadi bajingan..."

    tuuku "Bajingan?!"

    tuuku f_laugh @ f_confused "Untuk menanyakan sedikit pertanyaan?"

    eve "Itu bukanlah pertanyaan kecil!"

    show tuuku f_happy
    eve @ f_eyeroll "... Dan selain itu, aku sudah bilang padamu, {b}[firstname]{/b} tidak tertarik padaku!"

    menu:
        "Ya, benar!":
            anon a_rub f_shy_left "Um, sebenarnya..."

            show tuuku f_laugh
            eve f_surprised "!!!"
            eve f_nervous_down "Itu tidak lucu, {b}[firstname]{/b}!"

            anon a_idle f_worried "Saya tidak bercanda."

            tuuku f_happy @ a_thumb "Aku mengetahuinya!"

            tuuku "Kamu sangat bodoh dalam hal ini..."

            eve "I-itu bukan-"

            eve a_idle "Maksudku, dia tidak-"

            pause
            tuuku @ f_eyeroll a_point "Tsk, maukah kamu bersantai... Bagus sekali, {b}Evie{/b}!"

            eve f_angry @ -m_talk "..."
            tuuku @ f_laugh "Bukankah dia menggemaskan saat dia malu?"

            show eve a_flip with dissolve
            pause
            tuuku @ f_laugh "Ha ha ha!"

            show eve a_idle with dissolve
        "...":

            anon a_rub f_worried_left "..."
            tuuku f_confused "Ya, tapi {b}Odette{/b} berkata-"

            eve f_angry "Aku tidak ingin mendengarnya!"

            eve "Itu bukan urusannya..."

            tuuku f_annoyed @ a_point "Kamu tidak perlu bersikap defensif, aku hanya-"

            eve "... Dan kamu juga harus ikut campur!"

            show anon f_worried a_idle with dissolve

    tuuku a_arrest "Baiklah, baiklah... Astaga!"

    tuuku f_happy "Aku hanya bilang kalian berdua serasi..."

    show tuuku a_idle with dissolve
    eve "YA TUHAN, JATUHKAN!!!"

    tuuku @ f_laugh "Ha ha ha!"

    pause
    tuuku @ a_thumb "Ngomong-ngomong, aku {b}Tuuku{/b}."

    anon f_confused "kamu apa?"

    tuuku f_normal @ a_thumb "{b}Tuuku{/b}."

    anon @ -m_talk "..."
    anon "Maksudnya itu apa?"

    eve f_normal_right "Itu namanya..."

    anon f_worried @ f_surprised a_behind_head "Oh."

    show eve f_normal
    tuuku f_happy "Nama panggilan sebenarnya..."

    tuuku "Agak aneh, saya tahu, tapi para wanita menyukainya!"

    eve @ f_eyeroll a_facepalm "{i}*Mendengus*{/i} Anda ingin."

    anon "Apakah ada cerita di baliknya?"

    tuuku @ f_wink "Ya, tapi aku tidak bisa memberitahumu."

    anon "Kenapa?"

    tuuku f_angry @ a_point "... Karena kalau begitu aku harus membunuhmu."

    show anon f_surprised_teeth
    eve f_normal_right @ f_laugh "Pfft, ya benar!"

    eve "Jangan dengarkan dia, {b}[firstname]{/b}... Dia hanya berusaha bersikap keren."

    show anon f_worried
    show eve f_normal
    tuuku f_happy @ a_thumb "Hei, aku keren!"

    eve @ f_eyeroll "Heh, dengan rambut itu?"

    eve "Sepertinya seseorang menyerah di tengah jalan saat memotongnya!"

    show anon f_normal
    tuuku "Aduh, tidak keren {b}Evie{/b}."

    tuuku a_rub "Jangan pernah mengolok-olok doo!"

    eve @ f_laugh "Hahahaah!"

    tuuku @ f_laugh "hehe!"

    show tuuku a_idle
    pause
    tuuku "Jadi, apakah Anda sudah memberi tahu dia tentang rencananya?"

    show eve f_normal_right
    anon "Yang aku tahu hanyalah kami sedang mengerjai {b}Tyrone{/b} dan teman-temannya..."

    show eve f_normal
    tuuku f_normal @ a_point "Itu benar, kita akan memberi pelajaran pada bajingan itu malam ini!"

    tuuku "Tidak ada yang main-main dengan {b}Evie{/b} dan lolos begitu saja!"

    anon @ f_laugh "Heh, baiklah... Jadi bagaimana caranya?"

    eve f_normal_right "Kita akan menyabotase barang-barang mereka!"

    anon f_worried @ f_confused "Apa maksudmu?"

    eve f_normal "Apakah kamu membawa barangnya?"

    tuuku f_happy "Tentu saja."

    show tuuku a_vials with dissolve
    show eve f_nervous_down
    anon f_worried_low "Apa sajakah itu?"

    eve f_happy_right "Bom bau."

    anon @ f_surprised "Bom bau?!"

    eve @ f_laugh "Hehe, ya!"

    eve "Pada dasarnya, {b}Tuuku{/b} akan mengalihkan perhatian mereka saat Anda dan saya menyelundupkan ini ke dalam tas mereka."

    anon f_confused "Bagaimana cara kerjanya?"

    show eve f_normal
    tuuku "Oh, sederhana sekali... Yang harus Anda lakukan hanyalah memasukkannya ke dalam sana, menutupnya, dan memukulnya."

    show tuuku a_hips
    show anon a_vials f_worried_low
    with dissolve
    tuuku "Botol-botol ini sangat mudah pecah dan baunya meresap ke dalam semuanya!"

    eve f_normal_right "Berhati-hatilah, {b}[firstname]{/b}... Hal-hal ini SANGAT ampuh."

    anon f_worried "Y-ya, oke."

    show eve f_happy
    tuuku "Jika kita beruntung, mereka bahkan tidak akan menyadari apa yang terjadi sampai mereka tiba di rumah."

    eve "Oh, itu akan luar biasa!"

    tuuku "Hehe, begitu mereka membuka ransel itu, baunya akan keluar!"

    eve @ f_laugh "Haha!"

    anon "T-tapi bagaimana kamu akan mengalihkan perhatian mereka?"

    tuuku "Oh, itu bagian yang mudah."

    tuuku @ f_laugh a_thumb "Saya dealer mereka."

    anon f_confused "Hah?"

    eve @ f_laugh "Dia menjual obat-obatan kepada mereka sepanjang waktu."

    anon f_surprised "Anda melakukannya?"

    tuuku @ a_shrug "Hei, seorang pria harus mencari nafkah, kan?"

    eve f_confused "Saya masih tidak mengerti mengapa tidak apa-apa menjual kepada mereka dan bukan kepada saya?!"

    eve "Kami seumuran!"

    tuuku f_normal "Umm, karena mereka tidak punya {b}kakak perempuan{/b} yang mengancam akan menghancurkan bolaku jika mereka ketahuan membawa barang-barangku!"

    show eve f_normal
    anon f_worried @ f_skeptical "eh..."

    tuuku "Benar?!"

    tuuku f_happy @ a_point "Lihat, {b}[firstname]{/b} mengerti!"

    eve @ f_eyeroll "Ugh, terserah... Ayo kita lanjutkan saja!"

    show anon f_normal
    tuuku "Hehe, dengan senang hati."

    tuuku "Saya akan memberi sinyal kepada Anda ketika saya sudah mendapatkan perhatian mereka."

    tuuku @ a_thumb "Beri aku waktu beberapa menit untuk melakukan keajaibanku!"

    hide tuuku with dissolve
    pause
    tuuku "Heeey, apa kabar teman-temanku?!"

    pause
    anon "Dia tampak baik."

    anon f_worried "K-kamu tahu, untuk pengedar narkoba."

    eve @ f_laugh "Itu hanya pot, {b}[firstname]{/b}..."

    eve f_happy_right "Dia sebenarnya bukan pengedar narkoba."

    anon f_shy @ a_behind_head "Hehe, aku tahu."

    pause
    anon f_normal a_idle "Bagaimana kalian berdua saling kenal?"

    eve @ -m_talk "Hmm?"

    eve "Oh, adikku berkencan dengannya sebentar saat SMP."

    eve "Dia telah bergaul dengannya dan {b}Odette{/b} sejak saat itu."

    anon f_surprised "Dia berkencan dengan {b}Grace{/b}?"

    eve @ f_eyeroll "Ya, selama sebulan..."

    anon "Jadi apakah mereka seperti, berteman dengan keuntungan atau semacamnya?"

    eve f_surprised "Apa?!"

    eve f_happy_right @ f_laugh "Haha, tentu saja tidak!"

    eve "{b}Tuuku{/b} menjadi lebih seperti saudara bagi kami..."

    show eve f_happy
    show anon f_brag_closed a_facepalm with dissolve
    pause
    show anon f_normal a_idle
    show eve f_sad_thinking
    with dissolve
    pause
    eve f_happy "... Atau mungkin seperti sepupu norak, heh."

    eve f_happy_right "Bagaimanapun, aku cukup yakin mereka bahkan tidak pernah berciuman."

    anon "Oh."

    pause
    eve @ f_eyeroll "Menurutku {b}Odette{/b} menidurinya beberapa kali, tapi dia sering tidur dengan semua orang, jadi..."

    anon f_surprised "!!!"
    anon f_flirt "B-dia melakukannya?"

    eve f_happy "Benar sekali."

    anon f_surprised_down a_cover_boner "{i}*Meneguk*{/i}"

    pause
    eve "Itu sinyalnya."

    show anon f_surprised
    eve "Anda siap?"

    anon f_worried "Siap semampu saya..."

    eve "Hehe, ayolah!"

    hide eve with dissolve
    anon f_worried_low a_vials "{i}*Huh*{/i} Tidak ada apa-apa..."

    hide anon with dissolve
    return

label eve_button_prank_douches_school:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_happy
        show anon
    else:
        show eve b_desk_look_left f_happy:
            xoffset 500
        show anon b_desk zorder 3
    with dissolve
    eve "Jangan lupa, {b}kita akan bertemu di taman malam ini{/b} untuk membalas para bajingan yang menyemprotku!"

    anon f_worried "Maukah kamu memberitahuku apa yang kamu rencanakan?"

    eve "Mustahil!"

    eve "Aku tidak ingin merusak kejutannya!"

    anon f_tired "Uh, baiklah."

    anon "Saya akan berada di sana."

    eve "Itu akan menyenangkan, aku janji."

    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" zorder 1:
            xpos 450
        show expression "characters/eve/eve_overlay_o_desk.png" zorder 2:
            xpos 500
    hide eve
    with dissolve
    pause
    anon f_surprised_teeth "( Sobat, aku benar-benar tidak ingin memulai perang iseng dengan {b}Tyrone{/b} dan teman-temannya... )"

    anon @ -m_talk "( ... Tapi aku tidak bisa membiarkan {b}Eve{/b} melakukan ini sendirian. )"

    if player.location != L_school_frenchclassroom:
        show anon f_tired a_facepalm with dissolve
    anon "(Saya harap dia tidak merencanakan sesuatu yang terlalu gila.)"

    hide anon
    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" as anon_chair zorder 1:
            xpos -50
        show expression "characters/eve/eve_overlay_o_desk.png" as anon_desk zorder 3:
            xpos 0
    with dissolve
    return

label eve_button_prank_roxxy:
    scene expression player.location.background_closeup with None
    show anon f_worried
    show eve f_happy
    with dissolve
    anon "{b}Malam{/b}?"

    eve "Oh, hai {b}[firstname]{/b}!"

    anon f_confused "Mengapa Anda nongkrong di dekat ruang ganti?"

    eve "aku menunggu..."

    anon "Menunggu?"

    anon "Menunggu apa?"

    show anon f_worried
    eve "Tetaplah di sini dan Anda akan mengetahuinya..."

    anon @ -m_talk "..."
    anon "Um, oke..."

    pause
    anon @ f_sad_down "Aku merasa aku harus meminta maaf kepadamu lagi atas apa yang terjadi di rumahmu..."

    eve @ f_laugh "Heh, maksudmu saat kamu menyerbuku dan berganti pakaian dengan ular piton yang mengamuk di celanamu?"

    anon f_tired a_behind_head "Uhh, y-ya."

    eve "Tenang, {b}[firstname]{/b}... Ini bukan masalah besar."

    anon f_worried a_idle "Kamu tidak marah?"

    eve f_happy a_hip_angry @ f_laugh "Apakah saya terlihat gila?"

    anon "Tidak."

    pause
    anon f_skeptical "Kamu terlihat sangat bahagia."

    eve "Sangat senang!"

    anon f_worried "Kenapa kamu-"

    roxxy "AHHHH!!" with hpunch
    eve @ f_laugh "Hehehe!"

    anon "Apa yang-"

    hide anon with dissolve
    eve "Ini akan bagus!"

    scene black with fade
    pause
    $ player.go_to(L_school_boysroom)
    scene expression player.location.background_blur
    show roxxy b_undies a_hair f_surprised:
        flip
        xoffset 400
    with None
    show anon f_worried:
        xoffset -200
    with dissolve
    pause
    roxxy f_angry "YA TUHAN!!"

    anon f_shock "!!!"
    show anon f_surprised_teeth
    roxxy "ITU CAT SEMPROT!"

    roxxy f_worried "TIDAK TIDAK NONONO!!"

    show missy o_doodles f_yawn a_yawn zorder 1:
        xoffset 50
    with dissolve
    missy "{i}*Menguap*{/i}"

    show missy f_tired a_idle
    missy "Apa yang kamu teriakkan?!"

    roxxy f_angry "LIHAT RAMBUT SAYA, KAU IDIOT!!!"

    missy f_normal "Wah, bagaimana itu bisa terjadi?!"

    roxxy "Seseorang mengganti hairsprayku dengan cat!"

    show roxxy f_pouting_hair with None
    show becca b_towel:
        flip
        xoffset 200
    with dissolve
    becca "Siapa yang berteriak?!"

    missy a_point f_surprised "Sialan!"

    missy f_laugh "Ha ha ha ha!"

    show missy a_idle
    becca "Apa?!"

    missy f_normal @ f_laugh "Kamu berwarna oranye!"

    becca f_confused "Oranye?"

    show becca a_look f_shocked_down
    becca "!!!" with hpunch
    becca f_upset "OH, APA-APAAN?!"

    hide becca with dissolve
    missy f_laugh "Hahahaah!"

    missy "Kenapa kamu berwarna oranye?"

    becca "AKU TIDAK TAHU!!"

    missy f_normal @ f_laugh "Hahahaah!"

    pause
    becca "Oh sial!"

    pause
    show becca b_towel a_bottle f_upset zorder 1:
        flip
        xoffset 200
    becca "Seseorang memasukkan sunless tanner ke dalam sabun mandiku!"

    missy "Dengan serius?!"

    show becca a_hip
    hide roxxy
    show roxxy b_undies a_hair f_angry zorder 0:
        xoffset -200
    with dissolve
    roxxy "Maukah kalian diam?!"

    roxxy "Apa yang akan saya lakukan dengan rambut saya?"

    becca "Siapa yang peduli dengan rambut bodohmu?!"

    becca "Saya ORANGE!"

    missy @ f_laugh "PFFFT, HAHAHAHA!!!"

    show roxxy b_undies a_hair f_glaring:
        flip
        xoffset 400
    with dissolve
    show becca f_glaring
    missy "Kalian terlihat sangat konyol!"

    roxxy @ -m_talk "..."
    becca @ -m_talk "..."
    missy "A-apa?"

    show becca f_upset a_mirror with dissolve
    pause
    missy f_surprised "!!!"
    show becca a_hip
    show missy a_mirror f_confused
    with dissolve
    show roxxy f_angry
    missy "Oh, wah..."

    pause
    missy "Ada penis di wajahku!"

    becca "Tidak apa-apa?"

    pause
    missy f_surprised "Oh, kawan... Ini sangat berurat..."

    becca "Bagaimana itu bisa terjadi?"

    missy f_normal a_idle @ a_yawn f_yawn "Aku tidak tahu... Aku sedang tidur."

    becca "Kamu sedang tidur... Di ruang ganti?"

    missy "Ya?"

    becca @ -m_talk "..."
    missy "Saya bosan!"

    missy "Kalian berdua butuh waktu lama untuk bersiap..."

    becca "Menurut Anda siapa yang melakukan ini?"

    show missy a_think f_thinking with dissolve
    roxxy "Aku tidak tahu tapi siapa pun orangnya, mereka sudah mati!"

    show anon f_surprised_teeth:
        xoffset -250
    with dissolve
    hide anon with dissolve
    roxxy "aku serius!"

    show roxxy f_pouting_hair
    missy a_idle f_normal @ a_point "Aku yakin itu adalah para pemandu sorak nakal dari regu B..."

    becca "Pelacur tingkat dua itu?"

    missy "Ya, kamu tahu mereka sangat iri pada kita, kan?"

    becca @ f_eyeroll "Mereka tidak punya nyali untuk melakukan hal seperti ini!"

    roxxy @ -m_talk "..."
    show missy a_yawn f_yawn with dissolve
    scene black with fade
    pause

    $ player.go_to(L_school_lefthallway)
    scene expression player.location.background_blur with None
    show anon f_surprised
    show eve f_happy
    eve "Hmm, sepertinya {b}Roxxy{/b} dan si kembar bodoh sedang mengalami hari yang berat..."

    anon "Anda melakukan itu?"

    eve @ f_laugh "Ha ha ha ha!"

    if M_roxxy.finished_inclusive(S_roxxy_end):
        anon f_worried a_rub "Tidakkah menurut Anda itu sedikit ekstrem?"

        eve @ a_wtf "Psh, santai {b}[firstname]{/b}..."

        eve "Semuanya akan hilang."

        anon "Y-ya, tapi-"

        eve f_eyeroll @ a_up "Sejujurnya, aku tidak tahu apa yang kamu lihat pada perempuan jalang itu..."

        anon a_idle "Ayolah, dia tidak seburuk itu."

        eve f_angry @ a_wtf "Dia selalu menindasku!"

        anon "Ya, saya tahu..."

        anon "Dia hanya marah karena kehidupan rumah tangganya buruk."

        eve "Ya baiklah, bagaimanapun juga... Dia sudah menduga hal ini akan terjadi."

    else:
        anon f_normal "Bagaimana kamu bisa melakukan semua itu?!"

        eve @ a_wtf "Oh, aku punya caraku..."

        eve "Cukup bagus, ya?"

        anon "Hehe, ya..."

        eve @ f_laugh "Ha ha ha ha!"

        anon "Saya pikir Anda mungkin bereaksi sedikit berlebihan..."

        eve f_eyeroll "Bisa aja."

        eve "Itulah yang mereka dapatkan karena menindas saya!"

    eve f_happy @ f_laugh a_point "Dan mereka bukanlah satu-satunya targetku!"

    anon f_worried @ -m_talk "Hmm?"

    eve "Aku membalas {b}Tyrone{/b} dan teman-teman bajingannya juga!"

    anon a_behind_head "Oh, kawan... Apakah kamu serius?"

    eve "Anda ingin membantu?"

    anon a_idle "Ehh, entahlah... Apa sebenarnya yang kamu rencanakan?"

    eve @ f_laugh "Hehe, kamu akan lihat."

    eve "{b}temui aku di taman malam ini{/b}, oke?"

    anon "Y-ya, oke."

    eve "Jangan lupa!"

    hide eve with dissolve
    anon "saya tidak akan..."

    pause
    anon f_surprised_teeth "( Sobat, aku benar-benar tidak ingin memulai perang iseng dengan {b}Tyrone{/b} dan teman-temannya... )"

    anon @ -m_talk "( ... Tapi aku tidak bisa membiarkan {b}Eve{/b} melakukan ini sendirian. )"

    show anon f_tired a_facepalm with dissolve
    anon "(Saya harap dia tidak merencanakan sesuatu yang terlalu gila.)"

    hide anon with dissolve
    return

label eve_button_bridgets_help:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_sad_down
        show anon
    else:
        show eve b_desk_look_left f_sad_down:
            xoffset 500
        show anon b_desk
    with dissolve
    anon "{b}Malam{/b}!"

    eve f_sad "Hai, {b}[firstname]{/b}."

    anon "Anda tidak akan percaya apa yang terjadi!"

    eve @ -m_talk "Hmm?"

    anon "Saya meminta {b}Pelatih Bridget{/b} untuk berbicara dengan {b}Ny. Smith{/b} tentang aturan berpakaian, dan dia membuang semuanya!"

    eve f_surprised "!!!"
    eve f_nervous "Benar-benar?!"

    anon "Ya, bukankah itu bagus?"

    anon "Anda dapat menjaga rambut biru Anda sesuai keinginan Anda!"

    eve @ f_laugh "Luar biasa sekali, {b}[firstname]{/b}!"

    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" zorder 2:
            xpos 450
        show expression "characters/eve/eve_overlay_o_chair.png" as anon_chair zorder 1:
            xpos -50
        show expression "characters/eve/eve_overlay_o_desk.png" zorder 3:
            xpos 500
        show expression "characters/eve/eve_overlay_o_desk.png" as anon_desk zorder 4:
            xpos 0
    hide eve
    show anon b_hug_eve f_surprised_low zorder 2
    with dissolve
    anon "!!!"
    eve "Kamu yang terbaik!"

    anon f_shy_low "Hehe, terima kasih!"

    show eve b_dressed f_nervous_down
    show anon f_shy b_dressed
    with dissolve
    eve "Oh, ehh... Maaf."

    eve f_nervous "Aku tidak bermaksud-"

    anon "Tidak apa-apa."

    anon "Itu bagus."

    eve "Y-ya, itu-"

    tyrone "Ada apa, jalang?!"

    if player.location == L_school_frenchclassroom:
        show expression "characters/eve/eve_overlay_o_chair.png" zorder 0
        show anon f_worried zorder 1:
            xoffset -100
    else:
        show anon f_worried zorder 1:
            xoffset -100
    show chad
    show chico a_gun_up:
        xoffset 100
    show tyrone f_smirk:
        xoffset -125
    show eve f_surprised zorder 1:
        flip
        xoffset 200
    with dissolve
    eve "!!!"
    chad "Apa yang kalian berdua bicarakan?"

    anon "Tidak ada, kami hanya ngobrol."

    eve f_angry "Apa yang kamu inginkan?"

    tyrone "Sekali lagi dengan semua sikap itu..."

    tyrone "Anda tahu Anda menangkap lebih banyak lalat dengan madu, bukan?"

    eve @ f_eyeroll "Psh, seolah-olah..."

    eve "Meskipun pantas jika dalam metaforamu ini, kalian adalah serangga yang menghisap serangga!"

    chad @ f_angry "Meta-ya?"

    tyrone "Ck, gadis sialan... Kenapa kamu harus seperti itu?!"

    anon "Bisakah kami membantu kalian dengan sesuatu?"

    tyrone "Heh, iya sebenarnya, menurutku kamu bisa!"

    tyrone "Soalnya, anakku {b}Chico{/b} di sini ingin melakukan latihan target..."

    show eve f_confused
    anon f_confused "Latihan sasaran?"

    show chico f_cocky a_gun_down zorder 2 with dissolve
    chico "Sampaikan salamku pada teman kecilku!"

    show chico a_gun_shoot
    show eve f_surprised a_wtf
    show anon b_dressed_blocking
    anon "!!!" with hpunch
    show anon b_dressed f_surprised
    show chico a_gun_down
    show eve f_sad_down b_dressed_wet
    with dissolve
    eve "Ahh!!!"

    show eve f_angry
    anon f_angry "Bung, apa-apaan ini?!"

    tyrone f_laugh "Ha ha ha!"

    chad @ f_laugh "Ha ha ha!"

    eve "Dasar brengsek!!!"

    tyrone f_smirk "Sial, kamu membuatnya baik, yo!"

    eve "Euh, apakah ini bir?!"

    eve "Kamu menyemprotku dengan bir?!"

    tyrone "Daww, jangan marah sayang..."

    tyrone "Kenapa kamu tidak minta pacarmu mengambilkan handuk sementara kami membantumu melepaskan pakaian basah itu, ya?"

    show eve a_sides:
        xoffset 0
    show anon a_point zorder 3:
        xoffset 150
    with dissolve
    anon "Kalian harus pergi."

    show anon a_sides with dissolve
    chad "Psh, lihat dia, bertingkah keras sekarang."

    chico @ f_laugh "Haha!"

    tyrone "Sungguh, santai saja, Opie..."

    tyrone "Kami hanya mempermainkanmu."

    anon "Yah, itu tidak lucu!"

    eve f_sad_down "Adikku akan membunuhku!"

    tyrone "Saudari?"

    show eve f_angry
    tyrone "Mm, aku yakin dia baik-baik saja, sama sepertimu."

    eve "Persetan!"

    anon "Serius teman-teman, berangkat!"

    tyrone "Ya, ya... Kami berangkat."

    tyrone f_laugh "Beritahu adikmu kami menyapa!"

    show eve zorder 3
    eve @ a_flip -m_talk "..."
    hide chico
    hide chad
    hide tyrone
    with dissolve
    pause
    hide eve
    show eve b_dressed_wet a_wtf f_sad
    show anon f_worried
    eve "{i}*Huh*{/i} Apa yang harus aku lakukan?"

    eve "Kalau aku pulang dengan bau bir, adikku akan panik."

    show eve a_idle
    anon "Tidak bisakah kamu menyelinap masuk?"

    eve "Hmm, mungkin tidak..."

    eve "Dia biasanya mengatur waktu istirahatnya sehingga dia bisa bertanya padaku tentang hariku."

    anon "Hmm, kamu bisa datang ke tempatku dan mandi jika kamu mau."

    anon "Teman sekamarku bisa meminjamkanmu satu set pakaian bersih..."

    eve f_sad_down "T-tidak, menurutku itu bukan ide yang bagus."

    pause
    eve f_sad "Mungkin kamu bisa ikut denganku dan mengalihkan perhatian {b}Grace{/b} selagi aku berganti pakaian?"

    anon f_confused @ a_thinking "Mengalihkan perhatiannya?"

    eve "Ya, tanyakan saja padanya beberapa pertanyaan atau sesuatu..."

    anon "Ehh, maksudku... aku bisa mencobanya."

    eve "Silakan?!"

    anon f_worried "Y-ya, oke."

    eve "Terima kasih, {b}[firstname]{/b}!"

    anon "Ini, aku akan mengambil tasmu."

    eve f_sad_down a_wtf "Eh, ini menjijikkan!"

    hide anon
    hide eve
    with dissolve
    return

label eve_button_dress_code_ask_teachers:
    scene expression player.location.background_closeup with None
    show anon
    show eve f_sad_down
    with dissolve
    anon @ a_wave "Hai, {b}Hawa{/b}."

    eve f_sad "Hai, {b}[firstname]{/b}."

    anon "Kamu ingin jalan-jalan nanti?"

    eve "Nah, mungkin lain kali..."

    eve "Aku hanya ingin sendiri hari ini."

    anon f_worried "Oh, oke... Tentu."

    eve "Sampai jumpa."

    anon "Sampai jumpa."

    hide eve with dissolve
    pause
    anon @ -m_talk "(Kasihan {b}Eve{/b}, dia tidak bisa istirahat. )"

    anon f_angry @ -m_talk "( {b}Saya harus berbicara dengan guru{/b} di sekitar sekolah tentang perubahan aturan berpakaian baru ini. )"

    hide anon with dissolve
    return

label eve_button_school_dress_code:
    scene expression player.location.background_closeup with None
    if player.location != L_school_frenchclassroom:
        show eve f_sad_down
        show anon f_worried
    else:
        show eve b_desk_look_left f_sad_down:
            xoffset 500
        show anon b_desk f_worried
    with dissolve
    anon "Hai, {b}Hawa{/b}."

    eve "Hai, {b}[firstname]{/b}."

    anon "Kamu ingin jalan-jalan nanti?"

    eve f_sad "Nah, mungkin lain kali..."

    if player.location != L_school_frenchclassroom:
        show eve a_rossed with dissolve
    eve f_sad_down "Aku hanya ingin sendiri hari ini."

    anon f_tired "Oh, oke... Tentu."

    eve "Sampai jumpa."

    anon "Sampai jumpa."

    hide eve with dissolve
    pause
    anon @ -m_talk "(Kasihan {b}Eve{/b}, dia tidak bisa istirahat. )"

    anon f_angry @ -m_talk "( {b}Saya harus berbicara dengan Ny. Smith{/b} tentang perubahan aturan berpakaian baru ini. )"

    hide anon with dissolve
    return

label eve_button_roxxy_bullying_upset:
    scene school_assembly_hall_closeup_floor
    show eve b_sidebed f_sad_down
    show anon b_sit f_worried with dissolve
    anon "H-hei."

    eve "Hai."

    pause
    anon "Apa yang telah terjadi?"

    eve "Tidak ada yang luar biasa."

    eve "Hanya {b}Roxxy dan teman-teman idiotnya{/b} menjadi pelacur..."

    anon "Oh."

    pause
    anon "Apakah kamu baik-baik saja?"

    eve "Ya, aku akan baik-baik saja."

    eve "{i}*Huh*{/i} S.S.D.D."

    anon f_confused "SDD?"

    eve f_nervous "Anda belum pernah mendengarnya?"

    anon f_worried "Tidak?"

    eve @ f_laugh "Hehe, artinya, \"Sama saja, di hari yang berbeda\"."

    anon f_laugh "Oh, saya mengerti!"

    anon "Hehe."

    show anon f_normal
    show eve f_sad_down
    pause
    anon f_worried "Apakah mereka sangat mengganggumu?"

    eve "Nah, biasanya aku hanya menjauhi mereka, dan mereka mengabaikanku."

    pause
    eve f_nervous a_hair "{b}[firstname]{/b}, bolehkah saya menanyakan sesuatu?"

    anon f_normal "Tentu!"

    eve "Haruskah aku mengganti rambutku?"

    anon f_worried "Apa?!"

    eve "Itu adalah ide {b}Grace{/b} untuk mewarnainya menjadi biru."

    eve "Saya tidak begitu yakin tetapi sekarang setelah selesai, saya sangat menyukainya."

    pause
    anon "Itukah yang {b}Roxxy{/b} menggodamu?"

    eve a_down f_sad_down "Y-ya, mereka menyebutku menjijikkan..."

    anon f_skeptical "Itu konyol!"

    eve @ -m_talk "..."
    anon "Anda seperti, kebalikan dari menjijikkan!"

    eve f_confused "Sebaliknya?"

    show anon f_normal
    eve f_nervous "Heh, aku tidak yakin apa itu-"

    anon "Kamu cantik!"

    eve f_surprised "!!!"
    show eve f_nervous_down
    anon "... Dan rambutnya sangat cocok untukmu!"

    eve @ f_eyeroll "Cih, kamu hanya bersikap baik..."

    anon "Tidak, aku serius!"

    anon "Kamu cantik, {b}Hawa{/b}."

    eve f_happy "Heh, kamu terdengar seperti adikku dan {b}Odette{/b}."

    show eve f_sad_down
    pause
    eve "Jika Anda benar-benar mengenal saya, Anda tidak akan berpikir bahwa..."

    anon f_worried "Apa maksudmu?"

    eve @ -m_talk "..."
    eve "Sudahlah."

    pause
    eve f_nervous "Kita mungkin harus ke kelas, ya?"

    anon f_shy "Ya, mungkin..."

    eve "Terima kasih telah membuatku merasa lebih baik, {b}[firstname]{/b}."

    anon "Tidak masalah-"

    annie "Ah hah!"

    show anon f_surprised_left
    eve f_surprised @ -m_talk "!!!"
    annie "Aku tahu aku akan menemukan kalian berdua melakukan hal yang tidak baik!"

    show eve b_dressed f_sad a_idle
    show anon b_dressed f_surprised behind eve:
        flip
        xoffset -150
    with dissolve
    show annie at flip with dissolve
    annie "Melewatkan kelas, kan?!"

    anon f_worried "T-tidak, kami baru saja menuju ke sana sekarang..."

    annie "Ya benar."

    annie a_note "Aku menulis surat kepada kalian berdua untuk ini."

    eve "Apakah kamu bercanda?!"

    annie "Tidak, saya tidak."

    pause
    annie a_note_write @ f_smirk a_note "Hmm, sepertinya satu teguran lagi untukmu pembuat onar dan kamu mendapat detensi!"

    eve f_angry @ a_wtf "Demi Tuhan..."

    eve "Apa kau tidak punya hal lain yang lebih baik untuk dilakukan selain merepotkanku sepanjang hari?!"

    annie f_angry a_note "Hei, jaga mulutmu!"

    pause
    annie "Saya hanya melakukan pekerjaan saya dan menegakkan kebijakan sekolah."

    annie f_smirk "Ah, itu mengingatkanku..."

    annie "{b}Ny. Smith{/b} menerapkan beberapa aturan berpakaian baru di sekolah ini."

    annie "Pewarna rambut sekarang dilarang, jadi nikmatilah warna biru itu selagi masih ada..."

    eve f_surprised @ -m_talk "!!!"
    annie "Setelah hilang, itu hilang untuk selamanya."

    annie "Kalau tidak, itu pengusiran!"

    anon "Dia tidak bisa melakukan itu, ini sekolah umum..."

    anon "Sekolah umum tidak memiliki aturan berpakaian!"

    annie "Ini sudah selesai."

    show eve f_sad_down a_rossed with dissolve
    annie "Jangan ragu untuk membawanya jika Anda memiliki masalah."

    eve @ -m_talk "..."
    annie f_angry a_point1 "Sekarang bersiaplah ke kelas!!"

    hide annie with dissolve
    eve "Hari ini tidak bisa lebih buruk lagi..."

    hide anon
    show anon f_worried
    with dissolve
    anon "Serius, dia tidak bisa melakukan itu."

    anon "Ayo pergi dan bicara dengan {b}Nyonya. Smith{/b}."

    eve "{i}*Huh*{/i} Apa gunanya?"

    eve "Dia hanya akan mengatakan tidak dan jika beruntung, aku hanya akan memperburuk keadaan..."

    hide eve with dissolve
    anon @ -m_talk "(Kasihan {b}Eve{/b}, dia tidak bisa istirahat. )"

    anon f_angry @ -m_talk "( {b}Saya harus berbicara dengan Ny. Smith{/b} tentang perubahan aturan berpakaian baru ini. )"

    hide anon with dissolve
    return

label eve_button_auditorium_bummed:
    scene school_assembly_hall_closeup_floor
    show eve b_sidebed f_sad_down
    pause
    show anon f_worried with dissolve
    anon "{b}Malam{/b}?"

    show eve a_startled f_surprised with hpunch
    eve "!!!"
    eve "Apa yang-"

    eve "{b}[firstname]{/b}?!"

    show eve a_down with dissolve
    eve "Sheesh, kamu membuatku takut!"

    anon "Maaf."

    eve f_nervous "Fiuh, jantungku berdebar kencang!"

    pause
    eve "Lagi pula, apa yang kamu lakukan di sini?!"

    anon "Baiklah, saya melihat Anda berdebat dengan {b}Nona Ross{/b} dan kemudian Anda menyelinap ke sini..."

    eve f_confused "Mengawasiku, ya?"

    anon "T-tidak, tidak seperti itu."

    anon "Hanya memastikan kamu baik-baik saja, itu saja..."

    eve f_nervous "Anda khawatir tentang saya?"

    anon f_normal "Yah, kita berteman, kan?"

    eve "Ya, menurutku begitu."

    anon "Teman saling menjaga satu sama lain."

    eve f_laugh "Heh, itu menyedihkan sekali..."

    anon f_worried "..."
    eve f_wink "... Tapi aku agak menyukainya."

    show anon f_normal
    eve f_happy "Terima kasih, {b}[firstname]{/b}."

    anon "Terima kasih kembali."

    pause
    show eve f_nervous_down
    pause
    anon f_worried "Jadi..."

    anon "Anda ingin membicarakannya?"

    eve "Tidak, itu bodoh."

    anon "Oke, cukup adil."

    anon "Kami hanya akan membicarakan hal lain."

    show eve f_nervous
    anon f_normal "Misalnya, mengapa Anda nongkrong di auditorium yang gelap sendirian?"

    eve f_laugh "Heh, aku hanya ingin mengeluarkan tenaga."

    show eve f_nervous_down
    anon "Oh?"

    show eve a_idle with dissolve
    pause
    show eve f_nervous a_joint_show with dissolve
    anon f_shock "!!!"
    anon "Darimana kamu mendapatkan itu?!"

    show anon f_worried
    show eve f_nervous_down a_joint with dissolve
    eve "Saudariku."

    anon f_skeptical "Kakakmu memberimu satu porsi?"

    eve f_laugh "Ya Tuhan, tidak!"

    eve f_happy "Aku mengambilnya dari simpanannya pagi ini."

    anon "Benar-benar?"

    anon f_worried "Bukankah dia akan marah?"

    eve @ f_eyeroll "Psh, dia mungkin tidak akan menyadarinya..."

    show eve f_nervous_down a_idle with dissolve
    pause
    show eve a_down with dissolve
    eve @ f_nervous "... Dan bahkan jika dia melakukannya, dia akan menganggap salah satu temannya merokok."

    anon f_normal "Oh, begitu."

    pause
    anon "Kalian berdua rukun?"

    eve f_confused @ -m_talk "Hmm?"

    anon "Kamu dan adikmu."

    eve f_nervous "Oh."

    pause
    eve "Ya, sebagian besar."

    eve @ f_laugh "Heh, saat dia tidak melakukan {i}kesan sebagai ibu{/i}."

    anon f_confused "{i}Kesan ibu{/i}?"

    eve "Ya, dia seperti, mencoba memberikan contoh yang baik untukku atau semacamnya..."

    pause
    anon f_worried "... Dan itu hal yang buruk?"

    eve @ f_eyeroll "Itu menjengkelkan!"

    eve f_happy "Maksudku, dia dulu sangat menyenangkan!"

    eve "Saya berbicara tentang pesta, setiap malam!"

    eve "Seperti, benar-benar menjalani kehidupan liar..."

    eve f_disgusted "... Dan sekarang, dia berpura-pura tidak ingin berurusan dengan hal itu."

    eve "Meski begitu, semua orang tahu, dia sangat merindukannya!"

    eve f_sad "Itu hanya membuatku merasa seperti aku menghalanginya dan-"

    eve f_laugh "Hehe."

    show eve f_nervous
    eve "Maaf, aku bodoh."

    anon "Tidak, kamu tidak."

    anon "Saya mengerti."

    eve "Adikku sebenarnya sangat hebat!"

    eve "Saya beruntung memilikinya."

    show eve f_normal_up
    pause
    eve f_happy "Kamu tahu apa?!"

    anon f_normal @ -m_talk "Hmm?"

    eve "Anda harus datang dan menemuinya kapan-kapan!"

    anon f_worried "T-ke rumahmu?"

    eve "Ya!"

    eve f_nervous "Maksudku, jika kamu mau..."

    anon f_confused "Ehh."

    eve "Saya bisa memperkenalkan kalian berdua."

    anon "B-tentu saja, menurutku."

    show anon f_surprised_forward
    show eve f_normal_up
    "{i}*Bel berbunyi*{/i}"

    show anon f_unimpressed a_behind_head with dissolve
    anon "Oh sial."

    anon "Apakah itu belnya?"

    show anon a_idle with dissolve
    eve f_nervous_down "Heh, kurasa kesenangannya sudah berakhir..."

    eve f_nervous "Kamu bisa {b}mampir ke tempatku malam ini{/b}, jika kamu mau..."

    show anon f_normal
    eve "... Atau {b}malam lainnya{/b}, dalam hal ini."

    anon "Oke."

    anon "Saya akan segera datang."

    eve f_laugh "Luar biasa!"

    show eve a_wave with dissolve
    eve f_happy "Nanti, {b}[firstname]{/b}!"

    anon "Sampai jumpa, {b}Malam{/b}."

    hide eve
    hide anon
    with dissolve
    return

label eve_button_ross_argument:
    scene expression player.location.background_blur with None
    show eve f_nervous_down:
        xoffset -50
    show ross f_sad:
        flip
        xoffset 220
    with dissolve
    ross "Kamu harus mencobanya, sayang..."

    eve @ f_eyeroll "..."
    show eve f_sad
    ross "Seorang seniman hebat harus bisa melihat keindahan dalam segala hal, terutama dirinya sendiri."

    eve "{i}*Huh*{/i} Saya mencoba, hanya saja..."

    eve f_sad_down "... Rumit."

    ross "Saya hanya tidak mengerti mengapa proyek ini memberi Anda begitu banyak masalah..."

    show ross a_touch_comfort with dissolve
    ross "Mungkin sebaiknya kamu datang ke ruang seni sepulang sekolah, dan kita akan mengerjakannya bersama?"

    show ross a_sides
    show eve f_sad a_up
    with dissolve
    pause
    eve "T-tidak, tidak apa-apa."

    show eve a_cover f_sad_down with dissolve
    eve "Saya lebih suka melakukan ini sendirian."

    ross "Baiklah."

    pause
    eve f_nervous "Aku harus benar-benar masuk kelas, {b}Nona Bissette{/b} akan marah kalau aku terlambat lagi..."

    show ross a_hip with dissolve
    ross f_normal "Oh, mewah sekali!"

    show eve f_sad_down
    ross "Saya belum pernah melihat {b}Vivienne{/b} marah pada siapa pun."

    ross "Apalagi salah satu murid terbaiknya!"

    eve @ -m_talk "..."
    show ross f_confused a_hip_angry with dissolve
    ross "Cih, baiklah."

    ross "Kamu boleh pergi, segera setelah kamu berjanji padaku, kamu akan terus mengerjakannya."

    eve "Y-ya, aku akan melakukannya."

    ross f_normal "Anak yang baik."

    ross "Kita akan menaklukkan hal ini pada akhir semester, oke sayang?"

    eve f_eyeroll "Eh ya."

    hide eve with dissolve
    pause
    show ross a_yell with dissolve:
        xoffset 600
    ross "Datang dan temui aku sepulang sekolah jika kamu butuh bantuan!"

    show ross f_sad a_hip with dissolve
    pause
    ross "Kasihan..."

    hide ross
    show anon
    show ross f_sad
    with dissolve
    ross "Oh!"

    if not M_ross.is_state(S_ross_end):
        ross f_normal "Halo, {b}[firstname]{/b}."

        anon f_normal "Halo, {b}Nona Ross{/b}."

        ross "Bukankah kamu seharusnya berada di kelas?"

        anon "Y-ya, Bu."

        anon "Aku sedang dalam perjalanan ke sana sekarang."

        ross "Bagus, bagus."

        ross "Ingatlah untuk segera datang dan {b}berbicara dengan saya{/b} di {b}ruang seni{/b}, oke?"

        ross "Jika kami ingin menaikkan nilaimu, kami perlu-"

    else:
        ross f_sexy "Hai, tampan!"

        anon f_flirt "Heh, hai {b}Nona Ross{/b}."

        show ross a_touch_sexy:
            xoffset -200
        with dissolve
        ross "Apa yang kamu lakukan di sini, berkeliaran di aula?"

        anon "Heh, aku hanya... Uhh..."

        ross "Kamu tidak berencana membolos kelas {b}Nona Bissette{/b} kan, bocah nakal?"

        ross "Karena aku baru saja hendak berangkat ke kantorku dan aku tidak keberatan sedikit pun."


    scene location_school_right_hall_cutscene_01
    with fade
    anon "(Hmm?)"

    anon "( Kemana {b}Eve{/b} pergi?! )"

    anon "( Itu bukan {b}ruang kelas Bissette{/b}. )"

    pause

    scene expression player.location.background_blur
    show anon f_worried
    show ross f_confused:
        xoffset -200
    with fade
    ross "{b}[firstname]{/b}?"

    ross "Apakah Anda mendengar apa yang saya katakan?"

    anon "Oh, aku umm... M-maaf, apa tadi tadi?"

    ross "Kamu merasa baik-baik saja?"

    anon "Y-ya, benar-benar... Aku uhh... Maksudku, tidak... Aku-"

    anon "Sebenarnya aku merasa kurang enak badan hari ini..."

    ross "Oh?"

    anon "Ya, aku hanya perlu duduk, menurutku..."

    ross f_sad "Baiklah, baiklah, merasa lebih baik."

    anon f_normal "Ya, cukup!"

    anon "Terima kasih, {b}Nona Ross{/b}."

    hide ross with dissolve
    anon f_worried @ -m_talk "(Hmm, itu agak canggung...)"

    anon @ -m_talk "( Oh baiklah, setidaknya aku bebas {b}memeriksa Eve{/b} sekarang. )"

    anon @ -m_talk "( Apa yang dia lakukan {b}di Auditorium{/b}? )"

    hide anon with dissolve
    return

label eve_button_park_hangout:
    show expression player.location.background_closeup with None
    show eve a_artpad f_happy
    show anon
    with dissolve
    eve "Hei, kamu muncul!"

    anon f_snarky "Aku bilang aku akan melakukannya, bukan?"

    anon f_normal "Apakah ini tempat yang kamu bicarakan?"

    eve @ f_laugh "Ya!"

    show anon f_normal_left
    pause
    anon f_normal "Hmm, ini bagus..."

    eve "Hehe, kan?!"

    eve "Saya suka di sini!"

    eve "Entah kenapa, tapi air mancur itu benar-benar membuatku rileks."

    anon "Ya, itu masuk akal."

    anon @ f_brag_closed "Suara gemericik air, menenangkan."

    eve @ f_laugh "Tepat!"

    anon "Anda tahu, jika Anda menyukai air, kami memiliki beberapa pantai indah di sekitar sini."

    anon "Anda bisa menjejakkan kaki di pasir dan mendengarkan deburan ombak di bibir pantai."

    eve "Y-ya?"

    anon "Beberapa matahari terbenam yang sangat indah juga."

    eve f_nervous "Kedengarannya bagus tapi bukankah ada banyak orang di sana?"

    anon "Ya, mungkin ada... Terutama pada saat ini."

    eve @ f_laugh "Heh, terima kasih, tapi aku akan tetap menggunakan air mancurku yang bagus, tenang, dan terpencil..."

    anon @ f_laugh "Hehe, cukup adil."

    pause
    show eve f_nervous_down
    pause
    anon f_shy "J-jadi, kamu sudah tahu kotanya?"

    eve f_nervous "Ya, menurutku begitu."

    eve "Maksudku, tidak banyak, sungguh..."

    anon "Hehe, benar."

    anon "Apakah Anda rindu kota besar?"

    eve f_nervous_down "Mm, sebenarnya bukan kotanya..."

    pause
    eve f_nervous "Aku rindu makanannya."

    anon f_confused "Makanannya?"

    eve "Ya, ada begitu banyak restoran, dan mereka tetap buka seperti, dua puluh empat tujuh."

    eve "Ada tempat Cina yang bagus di dekat rumah kami."

    eve "Aku bersumpah, aku akan membunuh demi perintah lo-mein mereka!"

    anon f_normal "Hah, aku bahkan tidak tahu apa itu..."

    eve f_surprised "Dengan serius?"

    eve f_sad "Sungguh tragis, {b}[firstname]{/b}..."

    anon f_snarky "Tragis, ya?"

    show anon f_grin
    eve f_laugh "Haha, sepenuhnya."

    show eve f_happy
    pause
    show anon f_normal
    show eve f_nervous_down
    pause
    show anon a_point with dissolve
    anon "Jadi, apa yang kamu gambar?"

    show anon a_idle with dissolve
    eve f_confused "Hmm?"

    eve f_normal "Oh, bukan apa-apa... Hanya coretan-coretan."

    anon "Dapatkah saya melihat?"

    eve f_nervous_down "Ehh, ya... kurasa."

    show eve a_artpad_show
    pause
    show eve a_crossed f_nervous
    show anon a_artpad_catch
    with dissolve
    pause

    scene location_park_cutscene_02
    show text _ ("I was really surprised when {b}Eve{/b} agreed to let me see her art pad.\nShe was always so protective and secretive with it at school.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("It felt good to know that she trusted me enough to share.\nShe was one of the few people who actually treated me with kindness after all and I was eager to return the favor.") as caption with dissolve
    pause

    scene location_park_cutscene_01
    show text _ ("She was an amazing artist!") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("Her style and use of vibrant colors made the character on the page look almost real.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("Like she could spring to life at any moment and fly away into the night.") as caption with dissolve
    pause
    scene expression player.location.background_closeup
    show eve f_nervous:
        xoffset -250
    show anon a_artpad_catch
    with fade
    anon "Wah, ini bukan coretan..."

    anon "Ini luar biasa!"

    eve "K-menurutmu?"

    anon "Tentu saja!"

    anon "Siapa itu?"

    eve "Itu umm... Adikku..."

    anon f_shock "Benar-benar?"

    eve f_nervous_down "Y-ya."

    anon f_normal "Ini sangat bagus!"

    anon "Ini seperti, barang-barang yang dibayar mahal oleh orang-orang, tahu?!"

    eve f_eyeroll "Psh, ya benar..."

    show eve f_nervous
    anon "aku serius!"

    anon "Anda harus melakukan ini untuk mencari nafkah."

    show anon f_surprised_forward
    show expression "characters/anon/anon_overlay_o_can_hit.png":
        flip
        xoffset -500
    with dissolve
    "Tink!"

    show anon a_artpad_rub
    hide expression "characters/anon/anon_overlay_o_can_hit.png"
    with dissolve
    anon f_skeptical "Aduh!"

    show eve f_surprised
    anon "Apa yang-"

    chico "Pfft, hahahaha!!"

    show anon f_surprised_teeth a_artpad_catch:
        xoffset -100
    show eve f_disgusted:
        flip
        xoffset 150
    show chad
    show chico:
        xoffset 100
    show tyrone f_smirk:
        xoffset -125
    with dissolve
    tyrone @ f_laugh "Yo, apakah kamu melihat benda itu memantul dari kepalanya?!"

    show anon f_depressed
    chad "Ha ha ha!"

    chico "Ya, itu menamparnya tepat pada potongan rambut bodohnya..."

    tyrone @ f_laugh "Hahahah!!"

    show anon a_artpad_catch with dissolve
    anon f_worried "Kenapa kalian melemparkan barang ke arahku?!"

    eve "Uh, jangan ini lagi..."

    eve "Berapa kali aku harus memberitahumu ASSHOLES untuk meninggalkanku sendirian?!"

    chico "Cih, sial... Dia bersemangat malam ini!"

    tyrone "Apa yang kalian berdua lihat di sini?"

    eve "Bukan urusanmu!"

    show anon f_surprised a_surprised_up_both
    show tyrone a_artpad_steal
    with dissolve
    pause
    show anon f_angry a_sides
    show eve a_hip_angry f_angry
    with dissolve
    eve "Hai!!"

    show tyrone a_artpad f_surprised_down with dissolve
    pause
    show tyrone f_uneasy_down
    pause
    show tyrone a_artpad with dissolve
    tyrone f_smirk "Ohoho, DAYUM!!"

    tyrone "Siapa wanita jalang ini? Dia baik-baik saja!"

    anon "Kembalikan itu!"

    tyrone "Yo, santai saja Opie..."

    tyrone "Bukannya aku akan mencurinya..."

    show tyrone a_artpad_throw with dissolve
    tyrone "Di Sini."

    show anon a_artpad_catch
    show tyrone a_sides
    pause
    show anon a_artpad_sides
    eve "Persetan denganmu, {b}Tyrone{/b}!"

    tyrone "Ayolah, jangan sampai tubuhmu bengkok..."

    show tyrone a_hands_rub with dissolve
    tyrone "Kamu tahu, kamu adalah wanita jalang utamaku!"

    chad "Haha!"

    eve f_eyeroll "Eugh, dalam mimpi sialanmu..."

    tyrone "Mengapa kamu tidak ikut sajak bersama kami malam ini?"

    show eve f_angry
    tyrone "Aku akan menghubungkanmu dengan lebih banyak kine bud itu, kamu suka."

    eve "Tidak mungkin!"

    show tyrone a_sides with dissolve
    tyrone "Cih, baiklah... Jadilah seperti itu."

    pause
    show tyrone a_point with dissolve
    tyrone "Bagaimana denganmu?"

    show tyrone a_sides with dissolve
    anon f_worried @ -m_talk "Hmm?"

    tyrone "Kau ingin bersenang-senang atau kau hanya akan duduk di sini bersama nona kecil sepanjang malam?"

    show eve f_surprised
    pause
    show eve a_cover f_sad_down with dissolve
    eve @ -m_talk "..."
    anon f_angry "Tidak, aku baik-baik saja di sini."

    tyrone "Cih, terserah dirimu sendiri."

    tyrone "{b}Kami akan segera ke sana jika Anda sadar{/b}..."

    show tyrone f_kiss_drink
    pause
    tyrone f_smirk "Sampai jumpa, Boo..."

    show eve f_angry a_flip with dissolve
    tyrone f_laugh "Hahahaah!"

    hide tyrone
    hide chico
    hide chad
    with dissolve
    pause
    hide eve
    hide anon
    show anon a_artpad_catch f_worried
    show eve f_sad_down
    with dissolve
    pause
    show anon a_artpad_give with dissolve
    anon "Kamu baik-baik saja?"

    show anon a_idle
    show eve a_artpad
    with dissolve
    eve f_sad_down "Y-ya."

    anon "Anda yakin?"

    show eve a_crossed with dissolve
    eve f_sad "Ya, aku baik-baik saja..."

    pause
    eve "Aku mungkin harus pulang, sebelum adikku khawatir."

    anon "Ya baiklah..."

    eve "Maaf tentang mereka."

    anon "Itu bukan salahmu."

    show eve:
        flip
        xoffset 650
    with dissolve
    pause
    anon "Hai, {b}Malam{/b}..."

    hide eve
    show eve f_sad with dissolve
    eve @ -m_talk "Hmm?"

    anon "Serius, jangan dengarkan orang-orang itu... Mereka idiot."

    eve f_nervous "Hehe, aku tahu..."

    show eve f_nervous_down
    pause
    eve f_nervous "Terima kasih, {b}[firstname]{/b}."

    show anon f_grin
    pause
    anon f_shy "Kapan saja."

    hide eve
    hide anon
    with dissolve
    return

label eve_button_heisenberg:
    scene expression player.location.background_blur
    show player 90
    show player_outfit bb 638e
    with dissolve
    anon "(Sebaiknya aku tidak melakukannya. Tidak ingin membuka penyamaranku!)"

    hide player
    hide player_outfit
    with dissolve
    return

label eve_button_crypt:
    anon f_worried "Aku sedang berpikir untuk {b}mengunjungi Odette di ruang bawah tanah pada bulan purnama berikutnya{/b}..."

    show eve f_sad
    anon "... Maukah kamu... Mau... Ikut denganku?"

    eve "Apakah kamu serius?"

    anon "Ya, menurutku itu akan sangat membantuku memahami semua ini."

    eve "Aku tidak... Menurutku itu ide yang bagus."

    anon @ -m_talk "Hmm?"

    eve "Jika aku beruntung, beberapa hantu akan mengikutiku pulang."

    eve "Atau setan akan merasukiku atau semacamnya."

    anon f_shy "Itu tidak akan terjadi."

    anon @ f_laugh "aku akan melindungimu!"

    eve f_normal "Anda akan melakukannya?"

    anon "Tentu saja."

    anon "Kamu gadisku, ingat?"

    show eve f_happy
    pause
    eve "Aku sangat senang ketika kamu mengatakan hal seperti itu..."

    anon f_normal "Jadi kamu akan pergi?"

    eve f_nervous "Hmm..."

    pause
    eve f_sad "... Tidak."

    eve "Saya tidak bisa melakukannya."

    anon f_worried "Tidak?"

    eve "Maaf, {b}[firstname]{/b}..."

    eve "Mungkin lain kali."

    anon f_normal "Tidak apa-apa, {b}Hawa{/b}."

    anon "Jika Anda belum siap, maka Anda belum siap."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
