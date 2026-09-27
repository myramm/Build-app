label josie_button_pregnant:
    show anon with dissolve
    anon "Hai, {b}Josephine{/b}."


    if M_josie.pregnancy.stage <= 2:
        josephine @ -m_talk "Hmm?"

        josephine f_normal "Oh, hei!"

        josephine "Saya senang Anda ada di sini!"

        anon "Ya?"

        josephine "Anda ingin menonton beberapa video Gootube dengan saya?"

        show josephine f_normal_down
    else:
        josephine "Ya Tuhan, {b}[firstname]{/b}!"

        show anon f_worried
        josephine "Aku panik di sini!"

        anon "Ada apa?"

        josephine @ f_angry_closed "Kau memasukkan bayi raksasa ke dalam tubuhku, itu masalahnya!"


    menu josie_button_pregnant.choice:

        "Tenang..." if M_josie.pregnancy.stage > 2:
            jump josie_button_pregnant.calm

        "Apa yang kamu tonton?" if M_josie.pregnancy.stage <= 2:
            if M_josie.pregnancy.stage == 1:
                jump josie_button_pregnant.gootube
            else:
                jump josie_button_pregnant.feeding

        "Bayi itu" if M_josie.pregnancy.stage <= 2:
            jump josie_button_pregnant.baby
        "Ayahmu?":

            if M_josie.pregnancy.stage == 1:
                jump josie_button_pregnant.notice
            elif M_josie.pregnancy.stage == 2:
                jump josie_button_pregnant.clueless
            else:
                jump josie_button_pregnant.grandpa

        "Saya tidak bisa tinggal." if M_josie.pregnancy.stage <= 2:
            pass

        "Saya harus pergi." if M_josie.pregnancy.stage > 2:
            pass

    if M_josie.pregnancy.stage <= 2:
        anon f_normal @ f_worried "Saya tidak bisa tinggal."

        anon "Aku hanya ingin melihat kabarmu."

        josephine f_normal_down @ f_bored "Hanya saja, bosan..."

        josephine "... Seperti biasa."

        anon "Sampai jumpa lagi, oke?"

        josephine @ -m_talk "Mhmm."

    else:
        anon f_worried "Apakah kamu akan baik-baik saja?"

        josephine f_concerned "Ya, ya..."

        josephine "Tapi aku harap kamu bisa tetap di sini."

        anon "Aku tahu."

        josephine "Entah kenapa, berbicara denganmu membuatku merasa lebih baik."

        anon f_normal "Aku akan segera kembali, oke?"

        josephine "Baiklah."


    hide anon with dissolve
    return


label josie_button_pregnant.baby:
    anon f_worried "Apakah kamu benar-benar yakin ingin menjalani ini?"

    josephine f_concerned "Apa maksudmu?"

    anon "Maksudku, anak-anak adalah tanggung jawab besar dan itu bukan sesuatu yang bisa Anda abaikan begitu saja ketika Anda menginginkannya..."

    josephine f_bored "Hmm, ya."

    josephine "Saya tidak bodoh, {b}[firstname]{/b}."

    anon "Saya tahu itu, {b}Josephine{/b}... Saya hanya mengatakan itu-"

    josephine f_sexy "Bung, kamu perlu bersantai."

    josephine "Kita berbicara tentang seorang anak kecil dengan DNA saya... Ini akan menjadi bayi paling keren yang pernah ada!"

    anon @ -m_talk "..."
    anon "{i}*Huh*{/i} Ya, setidaknya kamu berpikir positif..."

    show josephine f_normal_down
    jump josie_button_pregnant.choice


label josie_button_pregnant.calm:
    anon f_worried "Semuanya akan baik-baik saja, aku janji."

    josephine f_bored "Ya, sangat mudah bagimu untuk mengatakannya!"

    josephine "Bukan Anda yang harus mengeluarkan benda sialan itu dari vagina Anda!"

    anon "Wanita melahirkan setiap hari, tubuh Anda tahu persis apa yang harus dilakukan..."

    josephine f_angry "Tidak, persetan!"

    josephine "Saya tidak mau!"

    anon "Ehh."

    josephine "Itu hanya harus tetap di sana."

    anon "{b}Yosephine{/b}..."

    josephine "Kenapa aku membiarkanmu membujukku melakukan hal ini?"

    anon f_surprised "AKU?!"

    anon "akulah yang-"

    anon f_shock "Itu-"

    anon f_hurt a_sides @ -m_talk "{i}*Huh*{/i}"

    anon a_idle f_worried "Lihat aku."

    josephine f_concerned @ -m_talk "Hmm?"

    pause
    anon "Bernapaslah saja, oke?"

    josephine @ -m_talk "Mhmm."

    anon "Anda telah menonton ratusan video tentang persalinan beberapa minggu terakhir ini..."

    josephine @ -m_talk "..."
    anon "... Aku tahu itu karena kamu memaksaku menonton sebagian besarnya bersamamu, ingat?"

    josephine f_sexy @ f_laugh "Hehe, ya."

    show anon f_normal
    josephine "Lucu sekali ketika satu video itu membuatmu muntah!"

    anon "Wanita itu menyebarkan diare ke mana-mana!"

    josephine @ f_laugh "Hahahaah!"

    anon "Itu terjadi pada bayinya!"

    josephine "{i}*Mendengus*{/i}"

    pause
    anon "Serius, {b}Josephine{/b}... Anda tahu segalanya tentang hal ini."

    anon "Anda punya ini."

    pause
    josephine "Terima kasih, {b}[firstname]{/b}."

    jump josie_button_pregnant.choice


label josie_button_pregnant.clueless:
    anon f_worried "Dia masih belum tahu?"

    josephine f_normal_down "Tidak."

    josephine "Dia benar-benar tidak mengerti, seperti dugaanku..."

    anon f_confused "Bagaimana mungkin dia tidak tahu?"

    anon f_normal @ f_laugh "Anda jelas-jelas menunjukkannya."

    josephine f_bored "Pfft, hanya di perutku sedikit..."

    josephine f_angry_down "Payudaraku belum tumbuh sama sekali."

    show anon f_worried
    josephine "Itu omong kosong!"

    josephine f_angry "Itu seharusnya menjadi salah satu bagian terbaik dari kehamilan!"

    anon "Payudaramu baik-baik saja..."

    josephine f_normal_down @ f_eyeroll "Ya benar."

    jump josie_button_pregnant.choice


label josie_button_pregnant.feeding:
    anon f_normal "Apa yang kamu tonton?"

    josephine f_normal_down "Video tentang menyusui."

    josephine "Mau bergabung dengan saya?"

    anon f_worried "Ehh..."

    josephine "Banyak dari video ini menyarankan untuk sering menggosok puting Anda dengan sikat atau loofah selama kehamilan untuk menguatkannya."

    anon "Benar-benar?"

    josephine @ -m_talk "Mhmm."

    pause
    anon @ f_disgusted "Kedengarannya sangat tidak menyenangkan."

    josephine f_sexy "Ya, aku tidak melakukan itu."

    josephine "Mereka juga mengatakan bahwa saya harus meminta pasangan saya mengoleskan minyak lanolin ke payudara saya setelah setiap sesi menyusui."

    anon f_normal "Oh?"

    josephine f_normal_down "Ya, aku pikir kamu akan menyukainya..."

    anon @ f_laugh "hehe."

    jump josie_button_pregnant.choice


label josie_button_pregnant.gootube:
    anon f_normal "Apa yang kamu tonton?"

    josephine f_normal "Gootube."

    anon f_confused @ -m_talk "..."
    josephine f_bored "Serius, apakah kamu tinggal di bawah batu atau semacamnya?"

    anon f_worried @ f_sad_down "Entahlah..."

    anon "Apa itu Gootube?"

    josephine f_normal "Ini adalah platform berbagi video di internet."

    josephine "Orang-orang pada dasarnya mengunggah apa pun yang mereka inginkan dan menontonnya gratis."

    anon @ f_confused "Suka porno?"

    josephine @ f_eyeroll "Bukan, bukan porno..."

    pause
    josephine f_surprised "Err, baiklah... Maksudku, mereka {i}DO{/i} punya film porno."

    josephine f_sexy "Sebenarnya cukup banyak."

    anon f_normal "Saya mengetahuinya."

    josephine f_surprised "Tapi aku tidak menontonnya!"

    josephine f_normal a_phone_show_left "Inilah yang diharapkan saat Anda mengharapkan video."

    anon f_surprised "Perlengkapan bayi?"

    josephine f_sexy "Ya, sejauh ini sangat menarik."

    anon f_worried "Baiklah, saya senang melihat Anda akhirnya menganggap ini setidaknya sedikit serius..."

    josephine f_normal_down a_phone "Eh ya."

    pause
    josephine f_sexy "Tahukah Anda bahwa sembilan puluh persen wanita buang air besar saat melahirkan?"

    show anon f_disgusted
    pause
    anon "Yah, itu tidak berlangsung lama."

    josephine f_normal_down @ f_laugh "Hahahaah!"

    show anon f_worried
    jump josie_button_pregnant.choice


label josie_button_pregnant.grandpa:
    anon f_worried "Mari kita pikirkan hal lain, oke?"

    josephine f_concerned "Ya baiklah."

    anon "Pasti ayahmu sudah mengetahui kamu hamil sekarang, kan?"

    josephine "Dia punya..."

    pause
    josephine f_bored "... Dan jangan panggil aku {b}Shirley{/b}."

    anon f_normal @ f_laugh "Hehe, lucu sekali."

    josephine f_sexy @ f_laugh "hehe!"

    anon f_worried "Apa yang dia katakan?"

    josephine "Dia kesal karena aku tidak memberitahunya dan dia mencoba membentakku..."

    pause
    josephine @ f_eyeroll "... Tapi itu tidak terlalu meyakinkan."

    josephine "Dia sangat bersemangat menjadi seorang kakek."

    anon f_normal "Ya, itu kabar baik!"

    josephine "Ya, menurutku."

    jump josie_button_pregnant.choice


label josie_button_pregnant.notice:
    anon f_worried "Tidakkah menurutmu kita harus memberi tahu ayahmu bahwa kamu hamil?"

    josephine f_angry "Tidak, kami belum memberitahunya!"

    josephine f_sexy "Aku ingin dia menyadarinya sendiri."

    anon f_confused "Itu-"

    pause
    anon "Mengapa?"

    josephine "Karena akan lebih lucu seperti itu!"

    anon f_worried @ -m_talk "..."
    anon "Bukankah dia akan marah?"

    anon "Aku tidak ingin dia membenciku atau semacamnya..."

    josephine @ f_eyeroll "Ayahku tidak akan membencimu."

    josephine "Dia tidak memilikinya di dalam dirinya."

    anon "Mungkin saja, saat dia tahu aku menghamilimu."

    josephine "Kawan, kau meniduri putrinya di meja kantornya..."

    anon f_surprised "!!!"
    anon f_worried @ f_surprised_left "Ssst, jangan terlalu keras!"

    josephine f_concerned "... Dia benar-benar berjalan mendekatimu jauh di dalam diriku."

    pause
    josephine f_sexy "Jika dia mampu membenci seseorang, kamu akan menjadi nomor satu dalam daftarnya."

    anon f_surprised_teeth @ -m_talk "..."
    josephine "Percayalah, kamu baik-baik saja."

    show anon f_worried
    show josephine f_normal_down
    jump josie_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
