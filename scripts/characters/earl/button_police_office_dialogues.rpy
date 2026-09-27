label earl_police_office_dialogue_roxxy_ask_earl_release:
    show earl
    show old_roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Permisi, Pak?"

    show player 5
    earl "Hah?"

    earl "Apa yang kalian lakukan di sini?"

    show earl f_eat a_donut_eat with dissolve
    show player 10
    player_name "Kami hanya mencoba mendapatkan informasi tentang penangkapan yang kalian lakukan hari ini."

    show player 5
    show earl f_normal a_idle with dissolve
    earl "Hmm, kamu adalah putri {b}Crystal{/b}, bukan?"

    show old_roxxy 1jf
    roxxy "..."
    show player 10
    player_name "Ya, benar, Pak."

    player_name "Bisakah Anda memberi tahu kami apa yang terjadi?"

    show player 5
    earl "Saya khawatir saya tidak diperbolehkan membicarakan masalah ini dengan siapa pun selain keluarganya."

    earl "Jika Anda ingin ikut dengan saya, Nona. Saya akan memberi tahu Anda cara kerjanya."

    show player 10
    player_name "... Ya baiklah. aku akan menunggu saja-"

    show player 11
    show old_roxxy 2c at Position (xpos=500) with dissolve
    roxxy "Tidak!"

    show old_roxxy 2cf at Position (xpos=434)
    with dissolve
    roxxy "... Maksud saya."

    show old_roxxy 33f at Position (xpos=400) with dissolve
    roxxy "Saya ingin dia tetap di sini. Tidak apa-apa."

    show old_roxxy 32f
    show player 13
    earl @ -m_talk "..."
    earl "Anda yakin?"

    show old_roxxy 33f
    roxxy "Ya."

    show old_roxxy 32f
    earl "Sesuaikan dirimu."

    earl "Kami mendapat tip anonim pagi ini mengenai simpanan besar obat-obatan di kediaman Anda."

    earl "Jadi kami melaju untuk melihat-lihat."

    earl "Tahukah kamu bahwa ibumu menyimpan lebih dari satu pon sabu di bawah sofa?"

    show old_roxxy 1if
    show player 23
    player_name "Satu pon?!"

    show player 22
    show old_roxxy 27f at Position (xoffset=67)
    roxxy "..."
    earl "Saya khawatir demikian."

    earl "Itu tuduhan kejahatan narkoba."

    earl "Kami menahan ibumu untuk dimiliki dengan tujuan untuk dijual."

    show old_roxxy 33bf at Position (xoffset=34) with dissolve
    roxxy "..."
    show player 10
    player_name "Itu tidak bagus."

    show player 5
    show old_roxxy 1jf with dissolve
    earl "Tidak, nak. Tentu saja tidak."

    earl "... Sekarang, saya sudah mengenal {b}Crystal{/b} sejak lama."

    earl "Kami pergi ke sekolah bersama pada hari itu."

    earl "Dia selalu pandai membuat dirinya mendapat masalah..."

    earl "... Tapi setelah menanyainya pagi ini, saya dapat memberi tahu Anda tanpa ragu bahwa dia tidak tahu apa-apa tentang memasak sabu."

    earl "Sekarang, dia mengklaim dia membuat semuanya sendiri dan ingin memindahkannya..."

    earl "... Tapi aku berani bertaruh dia hanya menyimpannya untuk orang lain!"

    roxxy "..."
    earl "Sayangnya, kecuali saya mendapatkan bukti. Dia akan berakhir di penjara untuk waktu yang sangat lama."

    show old_roxxy 33bf at Position (xoffset=34) with dissolve
    roxxy "{i}*Mengendus*{/i}"

    show player 10
    player_name "Oke, bagaimana dengan rumah temanku?"

    show old_roxxy 1jf with dissolve
    show player 5
    earl "Oh, trailernya?"

    earl "... Nah, jika {b}Crystal{/b} dinyatakan bersalah, maka akan diambil alih oleh negara dan dijual."

    show player 25
    player_name "Astaga..."

    show player 12
    player_name "Adakah yang bisa kita lakukan untuk mencegahnya?"

    show player 5
    earl "Tidak, kecuali kamu bisa meyakinkan {b}Crystal{/b} untuk menyerahkan siapa pun yang dia lindungi..."

    roxxy "..."
    show player 11
    player_name "..."
    show player 5
    earl "Aku benar-benar minta maaf atas kejadian ini, Nona."

    roxxy "{i}*Mengendus*{/i}"

    earl "Anda semua dapat {b}turun ke sel dan mengunjunginya{/b} jika Anda mau."

    earl "Mereka seharusnya sudah selesai menanyainya sekarang."

    show player 14
    player_name "Baiklah, terima kasih atas informasinya, Petugas."

    show player 13
    hide earl with dissolve
    pause
    show player 5
    show old_roxxy 33bf
    roxxy "... {i}*Sniff*{/i} Semua ini untuk si idiot bawaan itu..."

    show old_roxxy 1j with dissolve
    show player 10
    player_name "Ayo, kita pergi dan bicara dengan ibumu."

    hide player
    hide old_roxxy
    with dissolve
    return

label earl_police_office_dialogue_first_visit:
    show earl
    show player 11 at left
    with dissolve
    earl "Apa yang kamu lakukan di sini?!"

    earl @ f_eat a_donut_eat "Apakah ini salah satu hari \"membawa anak Anda ke tempat kerja\"?"

    show player 14
    player_name "Oh tidak, saya hanya lewat saja, Pak."

    player_name "Saya ingin berbicara dengan {b}Harold{/b}."

    show player 1
    earl "Tunggu sebentar... Apakah kamu tidak pergi ke sekolah dengan putriku?"

    show earl f_eat a_donut_eat with dissolve
    show player 14
    player_name "Oh benar! Anda adalah ayah {b}Ronda{/b}!"

    show earl a_idle f_normal
    show player 1
    earl "Siiiiiiiiiiiiiiiiiiiiii!"

    show player 11
    earl "Sebaiknya kau jaga dirimu di sekitar bayi perempuanku, atau aku harus mengawasi {b}kamu{/b}."

    show earl f_annoyed
    earl "Mengerti?!"

    show player 29
    player_name "Uhh... Tentu saja, Pak!"

    player_name "aku tidak akan pernah-"

    show player 13 at left
    earl f_normal @ f_laugh "Tenang, aku hanya main-main denganmu! Bergeraklah sekarang."

    return

label earl_police_office_dialogue_pre:
    show earl
    show player 1 at left
    with dissolve
    earl "Hei, ada apa?"

    return

label earl_police_office_dialogue_donuts:
    show earl
    show player 14
    player_name "Ini mungkin tampak seperti pertanyaan konyol, tapi donat seperti apa yang disukai {b}Harold{/b}?"

    show player 1
    earl @ f_laugh "Hah!"

    earl "{b}Harold{/b} hanya memakannya jika {b}[harold_glaze]{/b}..."

    earl @ f_eat a_donut_eat "... Tapi aku tidak yakin apa lagi yang dia kenakan pada mereka."

    show player 14
    player_name "Jadi begitu."

    show player 11
    earl "Mengapa kamu bertanya?"

    show player 17
    player_name "Oh, tidak ada alasan."

    show player 11
    earl f_annoyed "Tunggu, bukankah kamu seharusnya berada di sekolah? Apa yang kamu lakukan di sini-"

    show player 14
    player_name "Err..."

    show player 17
    player_name "Terima kasih sampai jumpa!"

    return

label earl_police_office_dialogue_harold:
    show player 10
    player_name "Tahukah Anda di mana {b}Harold{/b} berada?"

    player_name "Aku perlu berbuat salah... Kembalikan sesuatu padanya!"

    show player 11
    show earl f_normal
    earl "Saya tidak yakin kemana dia pergi, tapi saya melihatnya kemarin di kantor..."

    earl "Dia terlihat dalam kondisi yang buruk, itu sudah pasti!"

    earl "Untuk sesaat saya pikir dia akan berhenti..."

    earl "... Jadi aku menyuruhnya untuk mengambil cuti."

    show player 12
    player_name "Apakah dia menyebutkan di mana dia akan berada saat tidak bertugas?"

    show player 5
    earl "Saya tidak ingin bertanya terlalu banyak, Anda tahu?"

    earl "Terkadang pria hanya butuh waktu sendiri..."

    show player 14
    player_name "Baiklah terima kasih."

    return

label earl_police_office_dialogue_roxxys_mom:
    show earl
    show player 12
    player_name "Dimana kita bisa ngobrol dengan {b}ibu temanku{/b} lagi?"

    show player 5
    earl "Dia {b}di lantai bawah dalam sel{/b}."

    earl "Petugas {b}Yumi{/b} ada di bawah sana, tapi dia akan memberi kalian privasi untuk berbicara."

    show player 14
    player_name "Baiklah terima kasih."

    return

label earl_police_office_dialogue_leave:
    show player 14
    player_name "Hanya lewat saja, Pak."

    show player 1
    earl "Baiklah kalau begitu."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
