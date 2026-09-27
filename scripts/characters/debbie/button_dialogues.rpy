label debbie_dialogue_jenny_pool_talk:
    scene expression player.location.background_closeup with None
    show anon f_normal
    show debbie
    debbie "Jadi, apa yang dia katakan?"

    anon f_worried @ -m_talk "Hmm?"

    anon "Oh, aku belum bertanya padanya..."

    show anon f_normal
    debbie "Heh, tunggu apa lagi, konyol?"

    anon "Aku akan pergi sekarang."

    debbie "Terima kasih sayang."

    anon "Tidak masalah."

    hide debbie
    show anon f_thinking a_thinking
    with dissolve
    anon @ -m_talk "( Hmm, menurutku {b}[jen_name] sedang bersantai di tepi kolam renang{/b}... )"

    hide anon with dissolve
    return

label debbie_dialogue_mom_relaxing:
    scene expression player.location.background_closeup
    show debbie
    show anon with dissolve
    debbie "Hei sayang! Bukankah sebaiknya kamu pergi?"

    anon "Ya. Aku sedang dalam perjalanan."

    hide anon with dissolve
    return

label debbie_dialogue_mom_not_revealing_kitchen:
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show old_debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show old_debbie 48 at Position(xpos=660,ypos=768) with dissolve
    debbie "( !!! )"
    show old_debbie 48c
    debbie "Sayang, apa yang kamu lakukan di belakang sana?"

    show old_debbie 50j
    player_name "Mmm, tidak apa-apa..."

    show old_debbie 50k
    debbie "Sayang!"

    debbie "Bagaimana jika {b}[jen_name]{/b} masuk?"

    debbie "Dia akan punya seekor sapi!"

    show old_debbie 50j
    player_name "Heh, jangan khawatir, dia ada di kamarnya."

    player_name "... Dan selain itu..."

    player_name "... Ini hanya akan memakan waktu sebentar."

    show old_debbie 50k
    debbie "Kamu sungguh jahat b-"

    debbie "Ahhh!"

    debbie "... Baiklah! Cepatlah!"

    show old_debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show old_debbie 48c with dissolve
    debbie "Oke oke! Kita harus berhenti!"

    show old_debbie 50k
    debbie "Lagi dan aku harus mengganti celana dalamku!"

    show player 1 at left
    show old_debbie 52 at right
    with dissolve
    debbie "Apa lagi yang bisa saya bantu?"

    show old_debbie 1
    return

label debbie_dialogue_mom_fetch_lotion:
    show player 13 at left
    show old_debbie 2 at right
    with dissolve
    debbie "Apakah kamu {b}menemukan losionku di lemari kamarku{/b}?"

    show old_debbie 1
    show player 10
    player_name "Tidak, belum."

    show player 5
    show old_debbie 2
    debbie "Nah, tunggu apa lagi?"

    return

label debbie_dialogue_mom_car_condition:
    scene expression player.location.background_blur
    show debbie
    show anon f_worried with dissolve
    anon "Ya, aku melihat mesinnya..."

    debbie "Dan?"

    anon "Jelek banget, {b}[deb_name]{/b}..."

    anon "Tidak mungkin aku bisa memperbaikinya sendiri."

    debbie f_sad "Ya ampun..."

    anon "Ya, sebenarnya, menurut saya Anda mungkin harus mengganti semuanya."

    anon "Ini benar-benar rusak parah!"

    debbie @ f_surprised "T-tapi, aku tidak sanggup mengganti mesinnya!"

    anon "Aku tahu."

    pause
    debbie "Bagaimana dengan garansinya?!"

    anon "Garansi?"

    debbie "Ya, ayahmu membayar ekstra untuk garansi lima tahun ketika dia membelikan mobil untukku."

    anon @ f_normal "Itu bisa berhasil."

    anon "Belum lebih dari lima tahun, bukan?"

    debbie "Aku tidak tahu."

    show anon f_normal
    debbie "Apakah menurut Anda mereka akan menanggung biaya perbaikannya?"

    anon "Mungkin."

    debbie "Oh, ini buruk..."

    debbie "Apa yang akan kita lakukan tanpa mobil itu, {b}[firstname]{/b}?"

    anon "Jangan khawatir, {b}[deb_name]{/b}."

    anon @ f_laugh "Saya akan {b}menelepon dan berbicara dengan mereka{/b}."

    debbie f_normal "Anda akan melakukannya?"

    anon "Tentu saja."

    debbie "Oh sayang..."

    anon "Saya yakin mereka bisa membantu kami."

    debbie "Saya harap Anda benar."

    anon "Saya akan {b}kembali ke mobil dan menelepon mereka sekarang{/b}."

    anon "Seandainya mereka membutuhkan detail."

    hide anon with dissolve
    return

label debbie_dialogue_mom_revealing_kitchen_pre:
    scene expression player.location.background_blur
    show old_debbieobj 2 at Position(xpos=590,ypos=768)
    return

label debbie_dialogue_mom_revealing_feel_ass_sex_pre:
    $ player.go_to(L_home_kitchen)
    scene expression player.location.background_closeup with None
    show old_debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show old_debbie 48 at Position(xpos=660,ypos=768) with dissolve
    debbie "( !!! )"
    show old_debbie 48c
    debbie "Sayang?"

    debbie "Apa yang kamu lakukan di belakang sana?"

    show old_debbie 50j
    player_name "Mmm, tidak apa-apa..."

    show old_debbie 50k
    debbie "ah..."

    debbie "Bagaimana jika {b}[jen_name]{/b} masuk?"

    debbie "Dia akan punya seekor sapi!"

    show old_debbie 50j
    player_name "Hehe, jangan khawatir. Dia ada di kamarnya."

    show old_debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    pause
    show old_debbie 50j with dissolve
    player_name "Apakah itu terasa enak?"

    show old_debbie 50k
    debbie "Tentu saja..."

    debbie "Mmm, kamu membuatku basah kuyup!"

    debbie "Ahhh!"

    show old_debbie 50j
    player_name "Bagaimana jika aku menurunkan celana dalam ini dan menidurimu di sini?"

    show old_debbie 50k
    debbie "Ya Tuhan..."

    debbie "Oke, lakukanlah! Bawa aku ke sini! Cepatlah, sayang!"

    show old_debbie 50j
    player_name "Mmm, lebih baik kamu pegang lemari itu erat-erat!"

    show old_debbie 50c with dissolve
    pause
    show old_debbie 50d with dissolve
    pause
    hide old_debbie
    show old_debbie 50e at right
    with dissolve
    pause
    show old_debbie 50g with dissolve
    debbie "Oh ya!"

    hide old_debbie
    show debbies 164 at right
    with dissolve
    debbie "Ahhh!"

    player_name "Wah, kamu menetes..."

    return

label debbie_dialogue_mom_revealing_feel_ass_sex_after:
    show expression AnimatedImage("debbies", [164,165,166,167,168], M_debbie) as debbies at right with dissolve
    debbie "Oh, persetan denganku!"

    return

label mom_kitchen_fuck_loop:
    show screen sex_anim_buttons 
    pause
    hide screen sex_anim_buttons 
    $ animcounter = 0
    while animcounter < 4:
        if anim_toggle:
            if not animated:
                show expression AnimatedImage("debbies", [164,165,166,167,168], M_debbie) as debbies
                $ animated = True
            pause 4
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
            pause 3
        else:

            $ pose_counter = 0
            $ pose_list = [164,165,166,167,168]
            $ poses_done = []
            while poses_done != pose_list:
                show expression "debbies {}".format(pose_list[pose_counter]) as debbies
                pause
                $ poses_done.append(pose_list[pose_counter])
                $ pose_counter += 1
            if animcounter in [1,3]:
                call expression game.dialog_select("debbie_kitchen_hscene_dialog")
        $ animcounter += 1
    call screen mom_kitchen_fuck_options

label debbie_kitchen_hscene_dialog:
    if animcounter == 1:
        if randomizer() <= 50:
            debbie "Oh!!!{p=1}{nw}"

        else:
            debbie "AHHH!!!{p=1}{nw}"


    elif animcounter == 3:
        if randomizer() <= 50:
            debbie "Apakah kamu sudah cum?{p=2}{nw}"

            player_name "Belum...{p=2}{nw}"

            debbie "Cepatlah sayang... Kurasa... aku tak sanggup... Masih banyak lagi!{p=3}{nw}"

    return

label mom_kitchen_fuck_cum:
    call expression game.dialog_select("mom_kitchen_fuck_cum_dialogue")
    $ renpy.end_replay()
    $ persistent.cookie_jar["Debbie"]["unlocked"] = True
    $ persistent.cookie_jar["Debbie"]["gallery"]["09_unlocked"] = True
    $ game.timer.tick()
    $ game.main()

label mom_kitchen_fuck_cum_dialogue:
    player_name "( !!! )"
    player_name "Oh, {b}[deb_name]{/b}!"

    player_name "aku-"

    debbie "Ssst!"

    show debbies 169 with flash
    player_name "UHH!!!"

    hide debbies
    show old_debbie 50h at right
    with dissolve
    pause
    debbie "Oh, saya suka saat Anda mengambil alih!"

    player_name "Apakah kamu cum?"

    debbie "Oh ya!"

    show old_debbie 50i at right
    show player 434 at left
    with dissolve
    debbie "Fiuh, kakiku masih gemetar..."

    debbie "... Wow, kamu sering datang!"

    pause
    show old_debbie 61 with dissolve
    show player 10
    player_name "Maaf."

    show player 13
    show old_debbie 62
    debbie "Tidak, aku menyukainya! Rasanya menyenangkan di dalam diriku."

    show old_debbie 61
    show player 14
    player_name "Heh, aku suka kalau kamu mengatakan hal seperti itu."

    show player 13
    show old_debbie 62
    debbie "Hehe, itu faktanya.."

    hide player
    hide old_debbie
    with dissolve
    return

label debbie_dialogue_mom_revealing_feel_ass_no_sex:
    scene expression player.location.background_closeup with None
    hide old_debbieobj
    show old_debbie 47 at Position(xpos=656,ypos=768)
    with dissolve
    pause
    show old_debbie 50k at Position(xpos=660,ypos=768) with dissolve
    debbie "Baiklah, halo juga untukmu, sayang..."

    show old_debbie 50j
    player_name "Hai, {b}[deb_name]{/b}..."

    show old_debbie 50k
    debbie "Berhati-hatilah."

    show old_debbie 49_50_50b at Position(xpos=660,ypos=768) with dissolve
    pause
    pause
    show old_debbie 50k with dissolve
    debbie "Oke oke! Kita harus berhenti!"

    debbie "Lagi dan aku harus mengganti celana dalamku!"

    show player 1 at left
    show old_debbie 52 at right
    with dissolve
    debbie "Apa lagi yang bisa saya bantu?"

    show old_debbie 1
    return

label debbie_dialogue_mom_revealing_talk:
    scene expression player.location.background_closeup with None
    hide old_debbieobj
    show old_debbie 1 at right
    show player 2 at left
    with dissolve
    player_name "Hai {b}[deb_name]{/b}, ada waktu sebentar?"

    show old_debbie 2
    show player 1
    debbie "Butuh sesuatu, {b}[firstname]{/b}?"

    show old_debbie 1
    return

label debbie_dialogue_mom_revealing:
    show player 1 at left
    show old_debbie 2 at right
    with dissolve
    if randomizer() <= 10:
        debbie "Itu pria besarku..."

    elif randomizer() <= 20:
        debbie "Hai, sayang."

        debbie "Apa yang bisa saya lakukan untuk Anda?"

    elif randomizer() <= 30:
        debbie "Awww..."

        debbie "Tidak, halo, remas?"

    elif randomizer() <= 70:
        debbie "Mencari saya, saya harap."

    elif randomizer() <= 80:
        debbie "Butuh sesuatu, sayang?"

        debbie "Atau bisakah aku melakukan sesuatu untukmu?"

    elif L_home_shower.is_here(M_jenny):
        debbie "{b}[jen_name]{/b} sedang mandi."

        debbie "Jika Anda membutuhkan saya sebentar."

    else:
        debbie "Aku berharap bisa bertemu denganmu hari ini."

    show old_debbie 1
    show player 14
    if randomizer() <= 50:
        player_name "Halo, {b}[deb_name]{/b}."

    else:
        player_name "Kamu terlihat baik hari ini."

    show player 13
    return

label debbie_dialogue_mom_not_revealing:
    show player 1 at left
    show old_debbie 2 at right
    with dissolve
    debbie "Hai sayang!"

    debbie "Apakah semuanya baik-baik saja di sekolah?"

    show player 14 at left
    show old_debbie 1 at right
    player_name "Ya..."

    show player 13 at left
    show old_debbie 13 at right
    debbie "Saya harap Anda tidak ketinggalan terlalu jauh, bagaimana dengan semua yang telah terjadi?"

    show old_debbie 14 at right
    show player 14 at left
    player_name "Tidak, aku akan menyusul."

    show player 13 at left
    show old_debbie 13 at right
    debbie "Beri tahu saya jika ada yang bisa saya lakukan untuk membantu?"

    show player 21 at left
    show old_debbie 14 at right
    player_name "Oke, {b}[deb_name]{/b}..."

    player_name "Saya harus pergi."

    show player 13 at left
    show old_debbie 3 at right
    debbie "Jangan keluar terlalu larut!"

    show old_debbie 1
    return

label debbie_dialogue_ask_about_dad:
    show player 10 at left
    show old_debbie 1 at right
    player_name "{b}[deb_name]{/b}, tahukah kamu apa yang terjadi pada ayah?"

    show player 11
    show old_debbie 60 at Position (xoffset=-28) with dissolve
    debbie "Oh... Sayang, aku..."

    show old_debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Tolong, saya ingin tahu yang sebenarnya!"

    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "Maafkan aku, sayang. Saya tidak punya jawaban apa pun untuk Anda."

    debbie "Investigasi polisi belum menemukan apa pun..."

    show old_debbie 59 at Position (xoffset=-28)
    show player 10
    player_name "Apakah menurut Anda mereka akan menemukan sesuatu?"

    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "Saya harap begitu."

    show old_debbie 59 at Position (xoffset=-28)
    pause
    show old_debbie 60 at Position (xoffset=-28)
    debbie "Sayang..."

    debbie "Aku juga ingin mengakhiri semua ini..."

    debbie "... Tapi ayahmu tidak ingin kita terobsesi dengan hal ini."

    show old_debbie 63 at Position (xoffset=-28)
    debbie "Anda seorang pria muda dan Anda harus fokus menjalani hidup Anda."

    debbie "Lakukan itu untuk ayahmu."

    show player 10
    show old_debbie 59 at Position (xoffset=-28)
    player_name "Ya. saya akan mencoba."

    show player 14
    show old_debbie 61 at Position (xoffset=-28)
    player_name "Terima kasih, {b}[deb_name]{/b}."

    show player 1
    show old_debbie 2 with dissolve
    debbie "Ada lagi yang Anda butuhkan?"

    show old_debbie 1
    show player 1
    return

label debbie_dialogue_ask_about_money_problems:
    show old_debbie 13
    show player 11
    debbie "Sudah kubilang jangan khawatir tentang itu."

    debbie "Semuanya akan baik-baik saja!"

    show old_debbie 14
    show player 14
    player_name "Oke, tapi bagaimana jika saya ingin membantu Anda?"

    player_name "Bagaimana jika saya mendapat pekerjaan nyata?"

    show player 10
    player_name "Saya merasa agak bertanggung jawab atas semua stres ini..."

    show old_debbie 52 at Position (xoffset=1)
    show player 11
    debbie "Anda dapat membantu saya dengan tetap bersekolah!"

    debbie "Ayahmu akan terguling dalam kuburnya jika aku membiarkanmu mendapatkan pekerjaan penuh waktu..."

    debbie "Dia ingin kamu menyelesaikan pendidikanmu."

    show old_debbie 51 at Position (xoffset=1)
    show player 10
    player_name "Tapi saya bisa bekerja sepulang sekolah dan di akhir pekan..."

    show old_debbie 53 at Position (xoffset=-18) with dissolve
    show player 13
    debbie "{i}*Huh*{/i} Kamu keras kepala sekali, sama seperti ayahmu..."

    show old_debbie 59 at Position (xoffset=-28) with dissolve
    debbie "Hmm..."

    show old_debbie 61 at Position (xoffset=-28)
    debbie "Fokuslah untuk menaikkan nilaimu dulu, oke?"

    debbie "Maka mungkin Anda bisa mendapatkan pekerjaan."

    show old_debbie 61 at Position (xoffset=-28)
    show player 18
    player_name "Y-ya, oke."

    show old_debbie 62 at Position (xoffset=-28)
    show player 1
    debbie "Ada lagi yang ingin kamu bicarakan, sayang?"

    show old_debbie 1 with dissolve
    return

label debbie_dialogue_ask_about_men_in_suits:
    show player 10
    player_name "{b}[deb_name]{/b}, saya ingin berbicara tentang apa yang dikatakan pria berjas itu..."

    show old_debbie 59 at Position (xoffset=-28) with dissolve
    player_name "Apakah ayah terlibat dengan mereka?"

    show player 11
    show old_debbie 53 at Position (xoffset=-18) with dissolve
    debbie "{i}*Huh*{/i} Sejujurnya, aku tidak tahu, sayang.."

    debbie "Ayahmu adalah pria yang baik, {b}[firstname]{/b}."

    debbie "Sulit membayangkan dia terlibat dengan sekelompok preman seperti itu..."

    debbie "... Tapi sekarang dia sudah pergi dan sepertinya masih banyak yang tidak dia ceritakan padaku."

    show old_debbie 60 at Position (xoffset=-28) with dissolve
    debbie "Orang-orang itu mengira ayahmu berhutang uang pada mereka, dan sekarang dia sudah meninggal, mereka ingin kita membayar utangnya."

    show player 10
    show old_debbie 59 at Position (xoffset=-28)
    player_name "Mengapa polisi tidak melakukan apa pun untuk menghentikan mereka?!"

    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "Tidak sesederhana itu, sayang..."

    show player 10
    show old_debbie 59 at Position (xoffset=-28)
    player_name "Kenapa tidak?!"

    show player 11
    show old_debbie 60 at Position (xoffset=-28)
    debbie "{i}*Huh*{/i} Ternyata tidak."

    show old_debbie 59
    pause
    show old_debbie 53 at Position (xoffset=-18) with dissolve
    debbie "Kadang-kadang saya berpikir kita harus mengambil {b}[jen_name]{/b} dan menghilang untuk sementara..."

    show player 1
    show old_debbie 63 at Position (xoffset=-28) with dissolve
    debbie "Heh, itu akan menjadi sebuah petualangan, bukan?"

    show old_debbie 51 at Position (xoffset=1)
    show player 2
    player_name "Ya, saya kira."

    show old_debbie 2 with dissolve
    show player 1
    debbie "Apakah ada hal lain yang ingin Anda bicarakan?"

    show old_debbie 1
    return

label debbie_dialogue_paint:
    show player 10
    player_name "Bukankah ada cat di garasi?"

    show player 5
    show old_debbie 13
    debbie "Cat? Apa yang Anda inginkan dengan cat lama?"

    show old_debbie 1
    show player 10
    player_name "Tadinya aku akan mencoba dan membuat... Sesuatu."

    show player 5
    show old_debbie 2
    debbie "Oh, baiklah, {b}Diane{/b} bilang dia akan membuangnya untukku."

    show old_debbie 1
    show player 12
    player_name "Benar-benar?"

    player_name "Baiklah, sebaiknya aku lihat apakah aku bisa mengambilnya sebelum dia membuangnya!"

    player_name "Terima kasih, {b}[deb_name]{/b}! Sampai jumpa, {b}[deb_name]{/b}!"

    hide player with dissolve
    show old_debbie 2
    debbie "Selamat tinggal!"

    return

label debbie_dialogue_help_mow_lawn:
    show player 10
    player_name "Apakah Anda memerlukan bantuan dalam hal apa pun?"

    show player 5
    show old_debbie 2
    debbie "Apakah kamu sudah selesai memotong rumput di halaman?"

    show old_debbie 1
    show player 10
    player_name "Oh benar!"

    player_name "Saya akan membahasnya."

    show player 13
    show old_debbie 2
    debbie "Aku akan sangat menghargainya, sayang."

    show old_debbie 1
    show player 14
    player_name "Tidak masalah!"

    hide player
    hide old_debbie
    with dissolve
    return

label debbie_dialogue_help_fix_broken_pipe:
    show player 4
    player_name "(Saya harus memperbaiki {b}wastafel kamar mandi{/b} entah bagaimana... )"

    return

label debbie_dialogue_help_chores_pre:
    show player 14
    player_name "Ada lagi yang perlu bantuan Anda?"

    show player 13
    show old_debbie 2
    return

label debbie_dialogue_help_chores_later:
    debbie "Tidak. Tidak sekarang, sayang."

    debbie "Mungkin nanti, jika Anda masih tersedia."

    return

label debbie_dialogue_help_chores_tomorrow:
    debbie "Tidak. Tidak hari ini, sayang."

    debbie "Mungkin besok, jika Anda masih tersedia."

    return

label debbie_dialogue_help_chores_after:
    show old_debbie 3
    debbie "Terima kasih sudah bertanya!"

    show old_debbie 1
    show player 14
    player_name "Sama-sama, {b}[deb_name]{/b}."

    return

label debbie_dialogue_help_check_car:
    show player 4
    player_name "(Saya harus {b}pergi memeriksa mobil{/b} seperti {b}[deb_name]{/b} meminta saya melakukannya. )"

    return

label debbie_dialogue_help_fix_car:
    scene expression player.location.background_closeup
    show debbie
    show anon with dissolve
    debbie "Adakah keberuntungan dengan dealernya, sayang?"

    anon @ -m_talk "Hmm?"

    anon @ f_brag_closed "Oh benar!"

    debbie "Apakah kamu lupa?"

    anon "Tidak, aku akan mengurusnya sekarang."

    anon "Saya akan {b}menelepon dari dekat mobil{/b} jika mereka memerlukan detailnya."

    debbie "Terima kasih sayang."

    hide anon with dissolve
    return

label debbie_dialogue_mech_en_route:
    scene expression player.location.background_closeup
    show debbie
    show anon with dissolve
    debbie "Adakah keberuntungan dengan dealernya, sayang?"

    anon "Mereka mengirim seseorang ke sana secepat mungkin."

    debbie "Oh luar biasa! Terima kasih sayang."

    hide anon with dissolve
    return

label debbie_dialogue_help_nothing:
    show player 2
    player_name "Hai, {b}[deb_name]{/b}, ada yang bisa saya lakukan untuk membantu pekerjaan rumah?"

    show player 1
    debbie "Hmm..."

    show old_debbie 2
    debbie "Tidak ada yang bisa kupikirkan saat ini, tidak."

    show old_debbie 1
    show player 2
    player_name "Dingin. Beri tahu saya jika terjadi sesuatu."

    return

label debbie_dialogue_lotion_fun_had_sex:
    show player 14
    player_name "Perlu aku mengoleskan lotion lagi pada... Kakimu?"

    show player 13
    show old_debbie 2
    debbie "Kedengarannya luar biasa, sayang."

    debbie "Aku benar-benar membutuhkan sentuhan lembutmu saat ini."

    return

label debbie_dialogue_lotion_fun:
    show player 10
    player_name "Perlu aku mengoleskan lotion lagi pada... Kakimu?"

    show player 5
    show old_debbie 13
    debbie "Oh... Lagi? Yah, aku..."

    show old_debbie 14
    show player 10
    player_name "Apakah saya melakukan pekerjaan yang buruk?"

    show player 5
    show old_debbie 13
    debbie "Oh, tidak, sayang. Itu... Sangat bagus."

    show old_debbie 14
    pause
    show old_debbie 13
    debbie "Tentu, saya kira saya perlu istirahat."

    show old_debbie 1
    show player 14
    player_name "Besar!"

    show player 13
    show old_debbie 2
    return

label debbie_dialogue_lotion_fun_after:
    debbie "Pergi dan ambil {b}lotion dari lemari kamar tidurku{/b}."

    show old_debbie 1
    show player 14
    player_name "Baiklah!"

    return

label debbie_dialogue_shopping:
    scene location_home_kitchen_day_blur
    show player 2 at left
    show old_debbie 1 at right
    player_name "Ingatkah saat kamu mengajakku pergi berbelanja bersamamu?"

    show player 1
    show old_debbie 2
    debbie "Ya."

    show player 2
    show old_debbie 1
    player_name "Yah, aku bebas sekarang. Apakah kamu masih ingin pergi?"

    show player 1
    show old_debbie 3
    debbie "Benar-benar?! Besar!"

    show old_debbie 2
    debbie "Biarkan aku bersiap-siap dan aku akan menemuimu di mobil, oke?"

    show old_debbie 1
    show player 2
    player_name "Baiklah."

    return

label debbie_dialogue_shower_basement:
    show player 2
    show old_debbie 1
    player_name "Jadi uhh..."

    player_name "Kupikir kita mungkin bisa... Mandi bersama?"

    show player 13
    show old_debbie 2
    debbie "Sekarang?"

    show old_debbie 1
    debbie "Hmm..."

    show old_debbie 3
    debbie "Kurasa aku bisa mandi."

    show old_debbie 2
    debbie "Biarkan aku menyelesaikan cucian ini dan aku akan menemuimu di lantai atas."

    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    debbie "Semoga Anda belum hampir selesai..."

    debbie "Aku berharap kita bisa menghabiskan waktu di sini."

    return

label debbie_dialogue_shower_kitchen:
    show player 2
    show old_debbie 1
    player_name "Hai, {b}[deb_name]{/b}!"

    player_name "Saya bertanya-tanya..."

    show player 21
    player_name "Maukah kamu mandi bersamaku?"

    show player 14
    show old_debbie 2
    debbie "Cuaca di rumah mulai panas..."

    show old_debbie 3
    debbie "Tentu! Mandi terdengar menyenangkan saat ini."

    show old_debbie 2
    debbie "Beri aku waktu sebentar. Saya akan bergabung dengan Anda setelah saya selesai di sini."

    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    debbie "Maaf membuatmu menunggu, sayang..."

    return

label debbie_dialogue_sex_in_debbies_room_basement:
    show player 14
    player_name "Maukah kamu bergabung denganku di kamarmu?"

    show player 13
    show old_debbie 3
    debbie "Sekarang?"

    show old_debbie 1
    show player 10
    player_name "Sangat!"

    show player 5
    show old_debbie 2
    debbie "Hehe, baiklah..."

    show player 13
    debbie "... Pastikan saja, {b}[jen_name]{/b} tidak melihat kita."

    show old_debbie 1
    show player 14
    player_name "Saya akan."

    show player 13
    show old_debbie 2
    debbie "Hehehe..."

    debbie "Kamu akan membuatku lelah!"

    show old_debbie 1
    show player 14
    player_name "Saya hanya memastikan Anda banyak berolahraga!"

    show player 13
    show old_debbie 3
    debbie "Ha ha ha."

    show old_debbie 2
    debbie "Angkat pantatmu ke atas dan buka baju itu!"

    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_1:
        show old_debbie 86 at left
        show player 434f at right
        with dissolve
        debbie "Spreinya sangat bagus dan lembut... Mengapa kamu tidak ikut berbaring denganku..."

        show old_debbie 84
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show old_debbie 85
        show player 263 with dissolve
        debbie "Anak nakal."

        show old_debbie 84
        show player 262
        player_name "Apa?"

        show player 263
        show old_debbie 85
        debbie "Anda benar-benar tidak pernah puas."

        show old_debbie 84
        show player 262
        player_name "Anda bisa berbaring telentang dan saya bisa melakukan sisanya."

        show player 263
        show old_debbie 86
        debbie "Nah, di mana serunya itu?"

        show old_debbie 84
        show player 262
        player_name "Hehe, jangan khawatir. Aku akan membuatnya menyenangkan!"

        show player 263
        show old_debbie 84
        debbie "Mmm, saya tidak ragu tentang itu!"

        show old_debbie 89 with dissolve
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_kitchen:
    show player 14
    player_name "Maukah kamu bergabung denganku di kamarmu?"

    show player 13
    show old_debbie 2
    debbie "Sekarang?"

    debbie "Sangat!"

    debbie "Mari kita pastikan, {b}[jen_name]{/b} tidak melihat kita."

    show old_debbie 1
    show player 14
    player_name "Ya."

    show player 13
    scene debbie_bedroom_closeup2

    label sex_mom_bed_intro_2:
        show player 434f at right
        show old_debbie 86 at left
        with dissolve
        debbie "Saya berharap Anda akan membawa saya ke sini hari ini!"

        show old_debbie 84
        show player 435f
        player_name "Anda benar-benar memikirkannya?"

        show player 434f
        show old_debbie 86
        debbie "Apakah itu mengejutkan Anda?"

        debbie "Aku selalu memikirkan ayam besarmu itu..."

        show old_debbie 84
        show player 435f
        player_name "Heh, aku juga sering memikirkannya... Apalagi saat kamu mengenakan jubahmu itu."

        show player 434f
        show old_debbie 89 with dissolve
        debbie "Maksudmu benda lama ini?"

        show old_debbie 90
        show player 435f
        player_name "... Oh ya."

        show player 434f
        show old_debbie 89
        debbie "Hehe, kenapa kamu tidak melepas baju itu dan ikut bermain denganku?"

        show old_debbie 90
        show player 8f with dissolve
        pause
        show player 261 with dissolve
        pause
        show player 263
        show old_debbie 102
        with dissolve
        debbie "Mmmm..."

        show old_debbie 103
        if not store._in_replay == None:
            call expression game.dialog_select("debbie_dialogue_sex_in_debbies_room_after")
            jump expression game.dialog_select("mom_sex")
    return

label debbie_dialogue_sex_in_debbies_room_after:
    debbie "Datang dan tangkap aku, Nak!"

    hide player
    show old_debbie 104 at left
    with dissolve
    pause
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_sex_in_my_room:
    show player 2
    player_name "Kamu ingin tidur di kamarku malam ini?"

    show player 1
    show old_debbie 2
    debbie "Mmm, aku akan menyukainya, sayang."

    show player 2
    show old_debbie 1
    player_name "Besar! Aku akan menunggumu kalau begitu."

    show player 1
    show old_debbie 2
    debbie "Tak sabar menunggu!"

    return

label debbie_dialogue_sex_in_car:
    show player 14
    player_name "{b}[deb_name]{/b}, maukah kamu ikut denganku sebentar?"

    show player 13
    show old_debbie 2
    debbie "Hmm?"

    show old_debbie 1
    show player 14
    player_name "Ikuti saja aku."

    show player 13
    show old_debbie 2
    debbie "Hehe, apa yang sedang kamu lakukan?"

    show old_debbie 2
    debbie "..."
    show old_debbie 3
    debbie "Anda sedang merencanakan sesuatu!"

    show old_debbie 2
    debbie "hehe!"

    debbie "Apakah ini kejutan?"

    debbie "... Saya suka kejutan!"

    show old_debbie 1
    show player 14
    player_name "Hehe, aku tahu kamu tahu."

    player_name "Tapi aku tidak akan menyebutnya sebagai kejutan..."

    show player 13
    show old_debbie 3
    debbie "hehe!"

    show old_debbie 2
    debbie "Kalau begitu, kamu akan menyebutnya apa?"

    show old_debbie 1
    debbie "..."
    show old_debbie 2
    debbie "Apakah ini sesuatu yang nakal?"

    debbie "..."
    show old_debbie 1
    show player 14
    player_name "Mungkin."

    show old_debbie 2
    debbie "Hehe, baiklah. Ayo cepat selagi {b}[jen_name]{/b} ada di atas."

    hide player
    hide old_debbie
    scene black
    with fade
    return

label debbie_dialogue_watch_movie:
    show player 2
    player_name "Saya berpikir, mungkin kita harus menonton film lain malam ini. Tertarik?"

    show player 1
    show old_debbie 2
    debbie "Mmm, nonton film malam, ya?"

    debbie "Kedengarannya itu ide yang bagus, sayang!"

    show player 2
    show old_debbie 1
    player_name "Luar biasa!"

    player_name "Sampai jumpa {b}malam ini{/b} di {b}ruang tamu{/b} kalau begitu?"

    show player 1
    show old_debbie 2
    debbie "Saya tidak sabar..."

    return

label debbie_dialogue_laundry_sex_basement:
    scene home_basement
    show old_debbie 122 at right
    show player 14 at left
    player_name "Apakah Anda hampir selesai mencuci?"

    show player 13
    show old_debbie 123
    debbie "Hampir. Saya hanya perlu memindahkan beban ini ke pengering."

    debbie "Kenapa, ada apa sayang?"

    show player 14
    show old_debbie 122
    player_name "Saya hanya berpikir Anda mungkin ingin pergi jalan-jalan?"

    show player 13
    show old_debbie 123
    debbie "Oh, merasa agak nakal, ya?"

    show player 8 with dissolve
    pause
    show player 261f with dissolve
    pause
    show old_debbie 123
    debbie "Hehe, saya anggap itu sebagai ya!"

    show player 263f with dissolve
    debbie "..."
    show old_debbie 121
    show player 432
    player_name "Sangat!"

    show player 431
    pause
    show old_debbie 123
    debbie "Lepaskan pakaian itu dan masuk ke mesin cuci!"

    scene home_basement_sex_01
    show player 271 at Position(xpos=655,ypos=768)
    show old_debbie 107 zorder 0 at Position(xpos=200)
    with dissolve
    pause
    show old_debbie 108
    debbie "Giliranku..."

    debbie "Mmm, aku sudah menunggu sepanjang pagi untuk ini!"

    show old_debbie 109
    pause
    show old_debbie 110
    pause
    show old_debbie 111
    pause
    show old_debbie 112
    pause
    show old_debbie 113
    pause
    show old_debbie 114
    pause
    player_name "Kamu terlihat cantik, {b}[deb_name]{/b}."

    show old_debbie 115
    debbie "Duduk saja dan rileks, sayang."

    debbie "aku akan mengurus semuanya..."

    debbie "... Pastikan saja kamu tetap bersamaku."

    hide player
    hide old_debbie
    show debbies 124 at Position(xpos=650)
    with dissolve
    pause
    show debbies 125 at Position(xpos=655)
    pause
    show debbies 126f with dissolve
    debbie "Oh!"

    show debbies 126e
    pause
    show debbies 126d
    pause
    show debbies 126c
    pause
    show debbies 126b
    pause
    show debbies 126
    return

label debbie_dialogue_laundry_sex_basement_random_true:
    debbie "Mmmm..."

    debbie "Aku hampir tidak bisa menampung kalian semua."

    return

label debbie_dialogue_laundry_sex_basement_random_false:
    debbie "ah..."

    player_name "( !!! )"
    player_name "Kamu sangat hangat..."

    return

label debbie_dialogue_laundry_sex_kitchen:
    show player 14
    player_name "Hai, {b}[deb_name]{/b}... Apakah kamu ingin nongkrong di ruang bawah tanah untuk bersenang-senang sebentar?"

    show player 13
    show old_debbie 2
    debbie "Oh?"

    show old_debbie 1
    show player 14
    player_name "Saya pikir kita bisa menyalakan pengering dan Anda bisa bersuara sekeras yang Anda inginkan..."

    show player 13
    show old_debbie 3
    debbie "Haha."

    show old_debbie 2
    debbie "Itu cukup nakal, sayang."

    show old_debbie 1
    pause
    show old_debbie 2
    debbie "Hmm... Baiklah!"

    debbie "Saya punya waktu luang dan saya bisa menggunakan... Perhatian."

    show old_debbie 1
    show player 14
    player_name "Benar-benar?"

    show player 13
    show old_debbie 2
    debbie "Tentu!"

    debbie "Temui aku di sana sebentar lagi..."

    hide old_debbie
    hide player
    with dissolve
    return

label debbie_dialogue_kiss:
    show player 10 at left
    show old_debbie 1 at right
    player_name "Hei... Umm, {b}[deb_name]{/b}?"

    show player 5
    show old_debbie 2
    debbie "Ya, sayang?"

    show player 10
    show old_debbie 1
    player_name "Bolehkah aku menanyakan sesuatu padamu?"

    show player 5
    show old_debbie 3
    debbie "Tentu saja! Anda bisa bertanya apa saja kepada saya."

    show player 10
    show old_debbie 1
    player_name "Yah, itu agak... Memalukan."

    show player 5
    show old_debbie 13
    debbie "Oh? Baiklah, {b}[firstname]{/b}."

    debbie "Tidak perlu merasa malu."

    debbie "Tidak denganku..."

    show old_debbie 14
    show player 10
    player_name "Oke."

    return

label debbie_dialogue_kiss_teach:
    show player 10 at left
    show old_debbie 14 at right
    player_name "Saya ingin tahu apakah Anda bisa..."

    player_name "Ya..."

    show player 5
    show old_debbie 13
    debbie "Jika aku bisa apa, sayang?"

    show player 10
    show old_debbie 14
    player_name "Err... Ingat tempo hari di mall?"

    show player 5
    show old_debbie 14b
    player_name "..."
    show old_debbie 13
    debbie "... Ya?"

    show player 10
    show old_debbie 14b
    player_name "Baiklah... Aku berharap kamu bisa mengajariku lebih banyak, kamu tahu, tentang berciuman?"

    show player 5
    show old_debbie 13
    debbie "Apa?!"

    show old_debbie 14b
    player_name "..."
    show old_debbie 13
    debbie "Itu sebuah kesalahan, sayang. Aku seharusnya tidak pernah..."

    debbie "Apa yang kamu harap aku akan ajarkan padamu?"

    show player 10
    show old_debbie 14b
    player_name "Anda tahu, seperti, bagaimana melakukannya."

    player_name "Saya pikir, mungkin Anda bisa menunjukkan kepada saya apa yang disukai wanita?"

    show player 5
    show old_debbie 13
    debbie "Hmm, baiklah, aku pasti bisa memberitahumu apa yang disukai wanita."

    debbie "... Tapi menurutku menunjukkan padamu bukanlah ide yang bagus. Itu akan menjadi hal yang tidak pantas..."

    show old_debbie 14b
    return

label debbie_dialogue_kiss_teach_stat_fail:
    show player 10 at left
    show old_debbie 14b at right
    player_name "Apa kamu yakin?"

    player_name "Saya sangat ingin berlatih bersama Anda."

    show player 5
    debbie "..."
    show old_debbie 13
    debbie "Itu bukan ide bagus, sayang."

    show player 10
    show old_debbie 14b
    player_name "Oh... B-baiklah."

    show player 5
    show old_debbie 13
    debbie "Maaf, sayang."

    show player 10
    show old_debbie 14b
    player_name "Tidak apa-apa, {b}[deb_name]{/b}."

    return

label debbie_dialogue_kiss_leave:
    show player 10 at left
    show old_debbie 14 at right
    player_name "... Sebenarnya."

    player_name "Sudahlah."

    show old_debbie 13
    show player 5
    debbie "Apa kamu yakin?"

    debbie "Anda selalu dapat berbicara dengan saya, {b}[firstname]{/b}."

    show player 10
    show old_debbie 14
    player_name "Ya, tidak apa-apa."

    player_name "Maaf mengganggumu."

    show player 5
    show old_debbie 13
    debbie "Kamu tidak pernah menggangguku, sayang."

    return

label debbie_dialogue_kiss_practice:
    show player 2 at left
    show old_debbie 1 at right
    player_name "Apa menurutmu kita bisa berlatih lagi?"

    player_name "Kamu tahu... Berciuman?"

    show player 1
    show old_debbie 13
    debbie "Lagi?"

    show player 2
    show old_debbie 14b
    player_name "Y-ya. Saya pikir saya menjadi lebih baik!"

    show player 1
    show old_debbie 13
    debbie "... Baiklah."

    debbie "Tapi hanya sedikit!"

    show player 2
    show old_debbie 14
    player_name "Oke, tentu saja."

    hide player
    show old_debbie 79 at Position(xpos=0.70, ypos=1.0) with dissolve
    pause
    show old_debbie 80
    debbie "Hmm..."

    show old_debbie 79
    pause
    show old_debbie 78 at Position(xpos=0.80, ypos=1.0) with dissolve
    show player 233 at Position(xpos=0.30, ypos=1.0) with dissolve
    pause
    show old_debbie 77
    debbie "Wow... Menurutku kamu pasti menjadi lebih baik."

    debbie "... Dan kamu sudah sangat baik sejak awal!"

    show player 232
    show old_debbie 76
    player_name "Terima kasih, {b}[deb_name]{/b}!"

    show player 231
    show old_debbie 74
    pause
    show player 230
    pause
    show player 232
    show old_debbie 76
    player_name "Maaf tentang... Anda tahu."

    show player 231
    show old_debbie 75
    debbie "Hehe, tidak apa-apa, sayang."

    debbie "Sangat alami."

    debbie "Gadis-gadis di kota ini sedang dalam masalah."

    show player 232
    show old_debbie 72
    player_name "Hah, tentu saja!"

    show player 231
    show old_debbie 73
    debbie "Tangkap mereka, sayang!"

    show player 232
    show old_debbie 72
    player_name "Ya, Bu!"

    return

label debbie_dialogue_leave:
    show player 2
    player_name "Sebenarnya sudahlah, sampai jumpa lagi, {b}[deb_name]{/b}."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
