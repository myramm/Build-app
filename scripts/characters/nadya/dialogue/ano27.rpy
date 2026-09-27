label ano27_plan_nadya:
    scene expression game.timer.image('location_warehouse_pipe{}') as stage
    show keeves b_suit:
        xoffset 50
        xzoom -1
    show nadya b_traditional f_disgusted:
        xoffset -100
        xzoom -1
    nadya "Ugh, bau ini tak tertahankan."

    keeves "Kami berdiri di samping saluran pembuangan limbah, apa yang Anda harapkan?"

    nadya f_angry "Saya berharap untuk tidak terlibat dalam bagian ini..."

    keeves "Yah, tidak ada yang menodongkan pistol ke kepalamu, tuan putri."

    keeves "Mengapa kamu tidak kembali ke dalam dan biarkan aku yang menangani ini?"

    show nadya with dissolve:
        xoffset -250
        xzoom 1
    nadya "Apa, kamu ingin menyingkirkanku?!"

    keeves "Tidak, aku hanya bilang, jika kepekaan halusmu tidak bisa menangani sedikit pun-"

    nadya "Jangan bicara padaku seolah aku anak kecil!"

    nadya "Aku sudah muak dengan pembicaraan ini dari papa!"

    keeves @ -m_talk "..."
    show nadya a_crossed f_pouting with {'master': dissolve}:
        xoffset 300
        xzoom -1
    nadya @ -m_talk "Hmph."

    pause
    keeves f_happy "Ngomong-ngomong, gaunmu terlihat bagus."

    keeves "Anak itu akan menyukainya."

    show nadya f_angry with {'master': dissolve}:
        xoffset -250
        xzoom 1
    nadya f_angry "Diam!"

    nadya "Kamu tahu ayah membuatku berpakaian konservatif!"

    keeves f_normal @ -m_talk "Mhmm."

    nadya @ f_eyeroll "I'm so sick of stupid men!" (show_native="YA tak ustal ot glupykh muzhchin!")
    nadya "Aku mengirim kalian semua pergi setelah papa pergi."

    nadya "Bratva hanya mengambil wanita setelah aku memimpin!"

    keeves "Diam, mereka datang."

    show nadya f_worried with {'master': dissolve}:
        xoffset -100
        xzoom -1
    nadya @ -m_talk "Hmm?"

    tony "Sepertinya aku melihat mereka di sana!"

    harold "Ssst!!"

    tony "Apa?!"

    harold "Bisakah kamu menurunkannya sedikit?!"

    harold "Kau akan membuat semuanya menjadi tanggung jawab kami!"

    tony "Bagus."

    tony "Lalu kita bisa mengalahkan mereka semua dengan cepat dan pulang tepat waktu untuk mengikuti beberapa inning terakhir permainan."

    harold "Kamu tidak mungkin sebodoh itu..."

    tony "Hei, siapa yang kamu sebut bodoh?!"

    show nadya f_eyeroll
    harold "Anda sadar ada puluhan preman bersenjata di sana, kan?!"

    show nadya f_worried
    anon "Bisakah kalian berdua berhenti berdebat?"

    tony "Katakan itu pada cupcake sialan di sana..."

    tony "... Dialah yang membuat celana dalamnya berantakan!"

    show keeves f_happy
    harold "Grr, kamu akan membuat kami semua terbunuh!"

    keeves @ f_laugh "Heh, kedengarannya seperti kumpulan warna-warni."

    anon "Cukup, kalian berdua!!"

    show keeves f_normal
    pause
    anon "Yesus!"

    show anon f_worried behind nadya with dissolve:
        xoffset 150
        xzoom -1
    anon "{i}*Huh*{/i} Kita sudah sampai."

    nadya "Ya, kami mendengarmu dari jauh!"

    show anon f_tired
    show tony a_pipe_hold_shoulder b_casual f_glaring behind anon:
        xoffset 40
    show harold a_gun_side b_tanktop f_angry behind tony:
        xoffset 340
        xzoom -1
    with {'master': dissolve}
    harold "Lihat, sudah kubilang!"

    show anon f_eyeroll
    tony f_angry "Ah, sial."

    show anon f_worried
    show harold f_angry_right_up:
        xoffset -160
        xzoom 1
    with {'master': dissolve}
    pause
    show anon f_hurt
    show harold f_worried_down
    show tony a_pipe_point_forward f_suspicious
    with {'master': dissolve}
    tony "Kenapa gadis itu memakai karung kentang?"

    show anon a_facepalm
    show harold f_worried
    show nadya a_showoff f_surprised_down
    show tony a_pipe_hold_shoulder
    with {'master': dissolve}
    nadya "Apa-"

    show anon a_sides f_annoyed
    show nadya a_crossed f_angry
    with {'master': dissolve}
    nadya "Apakah pakaian tradisional ada di negara saya!!"

    tony "Mereka memaksamu memakai karung kentang sebagai tradisi?"

    show anon f_worried
    show keeves f_surprised
    tony "Pantas saja kalian para gadis Ruskie begitu pendendam..."

    keeves f_happy @ f_laugh "Pfft, haha!"

    nadya "Go to hell, old man!" (show_native="Poshyel k chyertu, starik!")
    nadya "Bukankah karung kentang!"

    show harold f_worried_right_up
    show tony f_eyeroll
    anon "Menurutku itu terlihat bagus."

    show harold f_worried
    show tony f_question
    keeves "Lihat, aku benar."

    keeves "Anak itu menyukainya."

    anon f_surprised "Tunggu sebentar, {b}Pastor Keeves{/b}?!"

    show harold f_surprised
    show tony f_surprised
    anon "Apa yang kamu lakukan di sini?"

    show harold f_suspicious
    show tony f_suspicious
    anon f_confused "Dan ada apa dengan penampilan salesman keliling?"

    nadya f_normal @ f_sexy "Anda meminta bantuan saya, ya?"

    show anon f_worried
    show harold f_worried
    tony f_sad "Ehh, jangan tersinggung Ayah... tapi aku berharap tidak ada seorang pun yang membutuhkan pendeta malam ini."

    nadya @ f_laugh "Hah, mereka pikir kamu pendeta sungguhan!"

    anon f_confused @ -m_talk "Hmm?"

    show harold f_suspicious
    keeves @ f_laugh "Tenang kawan."

    show tony f_question
    keeves "Pekerjaanku dengan gereja hanyalah kedok."

    harold "Penutup untuk apa?"

    show anon f_surprised
    nadya "Dia disewa senjata."

    nadya "{b}Johnny Silverdick{/b}."

    show anon f_confused
    show harold f_concerned
    tony f_surprised "{b}Silverdick{/b}?!"

    tony f_suspicious "Seperti dalam THE {b}Johnny Silverdick{/b}?"

    tony "... Siapa yang menjatuhkan Geng Gogolak di Chicago?"

    keeves "Itu sudah lama sekali."

    tony f_surprised "Sialan!"

    tony f_normal_right "Orang ini sungguh legenda!"

    tony f_normal "Saya tidak percaya Anda ada di sini secara langsung!"

    show tony a_pipe_handshake
    show keeves a_empty
    with {'master': dissolve}
    tony "Suatu kehormatan bisa bertemu denganmu."

    show nadya f_eyeroll
    keeves f_laugh "Tolong, kamu membuatku tersipu."

    show nadya f_worried
    show tony a_pipe_hold_shoulder
    show keeves a_idle f_happy
    with {'master': dissolve}
    tony "Hei, benarkah kamu membunuh Jimmy Tudeski dan Frankie Figs dengan pena tinta?"

    keeves @ f_laugh "Hehe, tidak..."

    show anon f_worried_surprised
    keeves "... Itu sebenarnya adalah pensil timah nomor 2."

    tony @ f_laugh "Hah, pria sialan ini!"

    anon f_worried "Ehh, {b}Tony{/b}?"

    tony f_normal_right @ -m_talk "Hmm?"

    anon "Kita benar-benar harus mempercepat ini..."

    tony "Oh, sial... kamu benar."

    tony "Saya buruk."

    show tony f_normal
    pause
    show keeves f_normal
    anon "Pernahkah kamu melihat gadis-gadis di sana?"

    anon "Apakah mereka baik-baik saja?"

    show tony f_sad
    nadya f_worried "{b}Dimitri{/b} telah mengikat mereka dan akan segera membawa mereka ke ruang interogasi."

    show anon f_surprised_teeth
    show harold f_worried
    show keeves f_sad
    nadya "Mereka masih utuh untuk saat ini tetapi dia akan segera mulai mengeluarkan bagian-bagiannya."

    anon f_worried "Kalau begitu kita harus bergegas!"

    show keeves f_normal
    anon "Apakah ini jalan masuk kita?"

    show nadya behind harold
    show keeves behind nadya
    nadya a_hips_point f_normal "Ya, di sini."


    scene expression background(500, 384, 1.5, b=0, l='warehouse_pipe') as stage with fade
    anon "Ini sangat kecil..."

    anon "... Dan bau."

    tony "Ya, tidak mungkin aku cocok di sana."

    pause

    scene location_warehouse_pipe_night as stage
    show keeves b_suit:
        xoffset 50
        xzoom -1
    show harold a_gun_side b_tanktop f_worried:
        xoffset -160
        xzoom 1
    show tony a_pipe_hold_shoulder b_casual f_sad:
        xoffset 40
    show anon a_sides f_worried:
        xoffset 150
        xzoom -1
    show nadya a_crossed b_traditional f_normal:
        xoffset -100
        xzoom -1
    with fade
    nadya "{b}[firstname]{/b} harus pergi sendiri, menurutku."

    anon "Ah, kawan."

    harold "Sekarang tunggu sebentar, kita tidak bisa mengirim anak itu sendirian..."

    show harold f_angry_right_up
    tony f_question "Kau akan memeras pantatmu yang sedang makan donat di sana, cupcake?"

    show harold f_angry with dissolve:
        xoffset 340
        xzoom -1
    pause
    harold "Jelas tidak... tapi-"

    tony "Percayalah, anak itu bisa menangani dirinya sendiri dengan baik."

    tony f_normal_right "Tidak bisakah kamu, juara?"

    show harold f_worried
    pause
    show anon f_worried_surprised
    nadya "Tidak perlu khawatir."

    show anon f_worried
    show tony f_question
    show harold:
        xoffset -160
        xzoom 1
    with {'master': dissolve}
    nadya "Aku meninggalkan minionku {b}Jab{/b} di sisi lain untuk menemuinya dengan tas perbekalan."

    harold @ f_suspicious "antekmu?"

    show tony f_sad
    nadya "Dia adalah pengawal."

    nadya "Bersama-sama mereka akan membuka jalan dan memberi sinyal bagi Anda untuk bergabung dengan mereka."

    nadya "Lalu kalian semua membersihkan gudang bersama-sama."

    anon "Ehh, ya.. oke.."

    pause
    anon "... B-bagaimana tepatnya aku melakukan itu?"

    nadya @ f_eyeroll "Ck, bagaimana aku bisa tahu?!"

    nadya f_angry "Berimprovisasi!"

    show tony f_normal
    anon "Berimprovisasi?"

    nadya "Rencanaku untuk membuat separuh pria bergairah pada papa dalam beberapa hari, ingat?!"

    nadya @ a_hips_point "Apakah ANDA yang membuat kami pergi malam ini!"

    nadya "Sekarang ini adalah masalah dan ANDA harus menemukan solusinya!"

    show harold f_worried_right_up
    tony f_normal_right "Buka saja pintu atau jendela dan kami akan menemukannya, jagoan."

    anon f_confused "Bagaimana dengan penjaga di luar?"

    show harold f_worried
    show tony f_normal
    keeves "Saya akan menanganinya."

    keeves "Anda hanya fokus mencari jalan masuk bagi orang lain."

    show harold f_worried_right_up
    show tony f_normal_right
    anon f_worried "Y-ya, oke."


    if M_tony.watches:
        show anon behind tony
        show tony a_mc_hip_single f_normal:
            xoffset 182
            xzoom -1
        show tony_arms_dressed_a_mc_shoulder_single as arm:
            xoffset 182
            xzoom -1
        with dissolve
        tony "Semuanya akan baik-baik saja, ya?"

        tony "Para Ruskie kotor itu tidak tahu apa yang akan menimpa mereka!"

        anon "Tapi bagaimana jika-"

        tony "Anda bisa melakukan ini, jagoan!"

        pause
        anon "Terima kasih, {b}Tony{/b}."

        hide arm
        show tony a_pipe_hold_shoulder f_normal_right behind anon:
            xoffset 40
            xzoom 1
        with dissolve
        pause

    elif M_mia.finished_state(S_mia_route_split):
        show anon behind harold
        show tony behind anon
        show harold a_gun_side_shoulder f_worried:
            xoffset 282
            xzoom -1
        with dissolve
        harold "Kamu akan melewati ini, Nak."

        harold "Tetaplah berada dalam bayangan dan tetaplah rendah, ya?"

        pause
        harold "Kami akan berada di sana untuk mendukung Anda begitu Anda memberi sinyal kepada kami."

        anon "Terima kasih, {b}Harold{/b}."

        show harold a_gun_side f_worried_right_up behind tony with dissolve:
            xoffset -160
            xzoom 1
        pause

    anon "Saat itu juga."

    pause
    anon "Saya kira sudah waktunya."

    show harold f_concerned
    show keeves a_go
    show tony f_smirk
    show nadya behind keeves
    with {'master': dissolve}
    keeves "Kalian berdua ikuti aku."

    show keeves a_sides with {'master': dissolve}
    keeves "Saya akan menempatkan Anda pada posisi untuk melakukan pelanggaran jika terjadi kesalahan."

    tony "Kedengarannya bagus."

    harold "Tepat di belakangmu."

    hide keeves
    hide tony
    hide harold
    show nadya:
        xoffset -650
        xzoom 1
    with dissolve
    tony "{b}Johnny{/b} sialan {b}Silverdick{/b}..."

    tony "... Bisakah kamu mempercayainya?!"

    harold "Saya belum pernah mendengar tentang dia."

    tony "... Ini luar biasa!"

    show anon f_worried with {'master': dissolve}:
        xoffset -150
    anon "Di mana kamu akan berada selama semua ini?"

    show nadya a_idle f_bored with {'master': dissolve}:
        xoffset -50
        xzoom -1
    nadya "Dengan papa di kantor lantai atas..."

    pause
    show anon a_surprised f_surprised_down behind nadya
    show nadya a_hips_point f_sexy
    with {'master': dissolve}
    nadya "... Menunggumu."

    show anon a_sides f_shy
    show nadya a_idle
    with {'master': dissolve}

    menu:
        "Jangan khawatir, saya akan berada di sana.":
            anon f_normal "Jangan khawatir, saya akan berada di sana."

            nadya "Keyakinan itu bagus."

            nadya "Anda akan membutuhkannya."

            pause
            show nadya b_traditional_kiss_cheek behind anon:
                xoffset -150
            show anon b_empty f_surprised
            with {'master': dissolve}
            anon @ -m_talk "!!!"
            show anon b_dressed
            show nadya b_traditional f_normal:
                xoffset 100
            with {'master': dissolve}
            anon f_shy "Untuk apa itu?"

            nadya "Untuk keberuntungan."

            nadya "Anda juga akan membutuhkannya."

            pause
            nadya "Dan untuk mengatakan kamu suka pakaian."

            anon "Oh, aku menyukainya."

            anon "Kamu terlihat sangat cantik."

            pause
            nadya "Lalu mungkin aku akan memakainya untukmu lain kali?"

            anon "{i}*Gulp*{/i} Saya ingin itu..."

        "Ciuman untuk keberuntungan?":

            anon f_normal "Ciuman untuk keberuntungan?"

            nadya f_angry @ -m_talk "Hmph."

            nadya "Misi pertama."

            nadya "Ciuman nanti."

            anon f_worried "Ya baiklah."

            pause
            anon "Ngomong-ngomong, aku bersungguh-sungguh dengan apa yang kukatakan..."

            nadya f_worried @ -m_talk "Hmm?"

            anon f_normal "Kamu terlihat sangat cantik dengan gaun itu."

            nadya f_normal @ -m_talk "..."
            nadya @ f_eyeroll "Oke, Anda meyakinkan saya!"

            show nadya b_traditional_kiss_cheek behind anon:
                xoffset -150
            show anon b_empty f_surprised
            with {'master': dissolve}
            anon @ -m_talk "!!!"
            show anon b_dressed f_shy
            show nadya b_traditional f_sexy:
                xoffset 100
            with {'master': dissolve}
            nadya "Untuk keberuntungan."

            anon f_normal "Oh, itu pasti berhasil..."

            anon "... Aku bisa merasakannya."

            nadya @ f_laugh "hehe!"


    pause
    nadya f_angry "Pergilah sekarang."

    anon "Y-ya, oke."

    hide nadya with dissolve
    show anon f_disgusted with dissolve
    pause
    anon @ -m_talk "(Euh, ini akan menyebalkan...)"

    show anon b_climb_pipe with dissolve:
        xoffset 0
        xzoom 1
    pause

    scene location_warehouse_sewers_cutscene_01
    show text _ ("The interior of the tunnel was dark, slippery, and cramped.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("I thought to use my phone as a flashlight at first but immediately regretted it.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The muck I was crawling through was better left unseen... And the smell was indescribable!") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("My every instinct was screaming to turn back, but that wasn't an option.") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("The girls were somewhere on the other side of this abomination and they needed me!") as caption with dissolve
    pause

    show screen minigame_sewer() with fade
    call screen empty()

    scene location_warehouse_sewers_cutscene_02
    show text _ ("It had been pure hell in that sewage drain.") as caption
    with fade
    pause
    hide caption with dissolve
    show text _ ("The horrors I beheld within will haunt me until the end of my days...") as caption with dissolve
    pause
    hide caption with dissolve
    show text _ ("... I will never feel clean again.") as caption with dissolve
    pause

    scene expression background(312, 360, 2.5, l=L_warehouse_sewer) with fade
    show anon f_disgusted_low o_sewage with dissolve:
        xoffset -250
        xzoom -1
    anon @ -m_talk "(Sial, namamu saluran pembuangan limbah.)"

    anon @ -m_talk "(Tidak mungkin aku akan kembali ke sana!)"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
