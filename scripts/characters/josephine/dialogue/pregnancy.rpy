label josie_pregnancy_notify:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset -400
    show josephine a_phone_talk f_concerned:
        xoffset -500
    show xtra3 as counter at right:
        xoffset -400

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_thinking_down "Itu {b}Josephine{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    josephine f_bored "Hei, ada apa, potongan mangkuk?"

    anon f_unimpressed "{i}*Huh*{/i} Berapa kali aku harus memintamu berhenti memanggilku seperti itu?"

    josephine f_sexy @ f_laugh "Hehe, setidaknya satu lagi."

    anon "Berhenti memanggilku potongan mangkuk!!"

    josephine @ f_eyeroll "Benar."

    pause
    josephine "Jadi coba tebak!"

    anon "Apa?"

    josephine "Saya pikir saya hamil."

    anon f_shock "!!!" with hpunch
    anon "K-kamu hamil?!"

    show anon f_surprised_teeth
    josephine f_normal_down @ -m_talk "Mhmm."

    anon f_worried "Seperti... Dengan bayi?"

    josephine f_angry "Jenis hamil apa lagi yang ada?"

    anon f_skeptical "Apakah ini lelucon?"

    pause
    anon f_normal @ f_laugh "Atau hal troll yang kamu suka lakukan?"

    josephine "Tidak."

    josephine f_bored "Saya serius, {b}[firstname]{/b}."

    show anon f_worried
    josephine "Aku punya bayi yang tumbuh di dalam diriku dan itu milikmu..."

    pause
    anon "Dan kamu seratus persen yakin itu milikku?"

    josephine f_angry "Hei, apa maksudnya itu?!"

    anon "T-tidak ada, aku hanya-"

    josephine "Menurutmu apa yang baru saja aku tiduri dengan setiap pria yang masuk ke dealer?!"

    anon "Tentu saja tidak, aku hanya-"

    pause
    anon "Sudahlah."

    anon "Apakah Anda berencana untuk menyimpannya?"

    josephine f_sexy @ f_laugh "Ya, aku akan menyimpannya!"

    josephine "Apakah kamu bercanda?"

    josephine "Saya akan mendapat cuti hamil tiga bulan!"

    anon f_hurt @ -m_talk "..."
    josephine "Ditambah lagi, itu benar-benar akan membuat ayahku kesal."

    anon f_worried "{b}Josephine{/b}, keduanya sepertinya merupakan alasan yang sangat buruk untuk memiliki bayi..."

    josephine "Menurutmu begitu?"

    anon "Ya."

    josephine f_pouting @ -m_talk "Hmm."

    pause
    josephine f_sexy "Tidak, saya tidak setuju."

    anon "Mungkin kita harus-"

    josephine "aku sedang mengalaminya."

    anon @ -m_talk "..."
    anon "Oh oke."

    josephine f_bored "Saya pikir Anda harus datang hari ini..."

    anon "Entahlah, aku punya beberapa hal-"

    josephine "... Kita bisa mendiskusikan nama dan hal lainnya."

    anon @ -m_talk "..."
    josephine "Saat ini, saya condong ke arah Gaylord jika dia laki-laki..."

    anon f_surprised "!!!"
    josephine "... Mungkin Phelony jika dia perempuan."

    anon f_angry "Anda tidak menamai anak kami Gaylord atau Phelony!"

    josephine f_sexy @ f_laugh "Haha, kenapa tidak?!"

    anon f_worried "Aku akan segera ke sana!"

    josephine "Panggilan bagus."

    josephine "Sampai jumpa lagi, potongan mangkuk!"

    show josephine a_phone with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    anon "Berhenti memanggilku potongan mangkuk!!!"

    pause
    anon "{b}Yosephine{/b}?!"

    pause
    anon f_worried "Halo?"

    anon f_thinking_down a_phone @ -m_talk "(Sial...)"

    anon f_surprised_teeth_low @ -m_talk "(Apa yang telah kulakukan?!)"

    hide anon with dissolve
    return True


label josie_pregnancy_notify.repeat:
    scene expression player.location.background
    "{i}*Brrrzzzt* *Brrrzzzt*{/i}"


    scene expression background(608, 512, 3.8, l=L_dealership_showroom) as underlay:
        xoffset -400
    show josephine a_phone_talk f_bored:
        xoffset -500
    show xtra3 as counter at right:
        xoffset -400

    $ renpy.dynamic(stage=player.location.background_phone)
    show expression stage as stage
    show anon f_confused with dissolve:
        flip
    anon @ -m_talk "Hmm?"

    anon a_phone f_worried_low "Itu {b}Josephine{/b}."

    show anon a_phone_talk f_normal with dissolve:
        unflip
        xoffset 500
    show expression stage as stage at phoneleft with phoneleft.show
    anon "Halo?"

    josephine "Hai, {b}[firstname]{/b}."

    anon "Apa yang terjadi?"

    josephine "Ya, aku hamil lagi..."

    anon f_worried @ f_surprised "!!!"
    anon "Lagi?!"

    josephine "Ya."

    josephine "Permainan tarikmu itu lemah, kawan..."

    anon "Saya berasumsi Anda akan menyimpannya?"

    josephine "Duh."

    josephine f_sexy "Cuti hamil tiga bulan."

    anon f_sad_down "{i}*Huh*{/i} Benar."

    josephine "Ayo jalan-jalan bersamaku di dealer."

    anon "Ya baiklah."

    anon "Sampai jumpa lagi."

    show josephine a_phone
    show anon f_worried_low a_phone
    with dissolve
    show expression stage as stage with {'master': phoneleft.hide}
    "{i}*Bip*{/i}"

    pause
    anon "Aduh, terjadi lagi."

    hide anon with dissolve
    return True


label josie_pregnant_labor_1:
    scene expression player.location.background_blur
    show anon f_normal with dissolve
    anon "Sepertinya aku mendapat pesan teks."

    hide anon with dissolve
    return


label josie_pregnant_labor_2:
    scene expression player.location.background_blur
    if player.location != L_map:
        show anon f_surprised a_phone with dissolve
    anon "{b}Josephine{/b} punya bayinya?!"

    anon "Sialan!"

    pause
    anon "Sebaiknya saya pergi ke {b}klinik{/b} untuk memeriksanya."

    if player.location != L_map:
        hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
