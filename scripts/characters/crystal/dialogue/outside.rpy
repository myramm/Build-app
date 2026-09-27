label crystal_button_outside:
    scene location_trailer_closeup01_new_evening
    show location_trailer_closeup01_chair as chair
    show crystal b_dressed_sitting

    if M_crystal.mood == 'bitter':
        jump crystal_button_outside.bitter

    if M_crystal.mood == 'bliss':
        jump crystal_button_outside.bliss

    show anon with {'master': dissolve}:
        xoffset 100
        xzoom -1
    crystal f_smirk "Mmm, sekarang ada pria yang baik dan cakap!"

    show anon a_wave
    with {'master': dissolve}
    anon "Heh, hai {b}Kristal{/b}..."

    show anon a_sides
    with {'master': dissolve}
    crystal f_normal "Mengapa kamu tidak minum bir dan duduk bersamaku, Romeo?"

    crystal f_smirk "Anda bisa memamerkan lidah perak itu lagi..."

    show anon a_shy_neck f_shy_left
    with {'master': dissolve}
    anon "Oh, entahlah... {b}Roxxy{/b} tidak akan-"

    crystal f_normal "Kamu di sini untuk menelepon {b}Roxxy{/b}?"

    show anon a_sides f_normal
    with {'master': dissolve}

    menu crystal_button_outside.choice:
        "Kilat?" if M_roxxy.get('roxxy crystal sex'):
            jump crystal_button_outside.quickie
        "Ya, apakah dia ada di sini?":

            jump crystal_button_outside.roxxy
        "Saya harus pergi.":

            pass

    show anon a_point_back
    with {'master': dissolve}
    anon "Aku mungkin harus masuk ke sana..."

    show anon a_sides
    with {'master': dissolve}
    crystal "Ya, menurutku kamu benar tentang itu."

    crystal "Jaga baik-baik gadisku sekarang, dengar?"

    show anon a_salute f_happy_closed
    with {'master': dissolve}
    anon "Ya, Bu."

    hide anon
    show crystal f_laugh
    with {'master': dissolve}
    crystal @ -m_talk "Ha ha ha!"

    crystal f_normal "\"Nyonya\"..."

    crystal "... Itu membunuhku setiap saat!"

    return


label crystal_button_outside.bitter:
    show crystal f_annoyed
    show anon a_sides with {'master': dissolve}:
        xoffset 100
        xzoom -1
    crystal "Baiklah, lanjutkan!"

    show anon f_confused
    crystal "Masuk ke sana dan persetan dengan putriku!"

    show anon f_worried
    crystal "Ya, tinggalkan aku di sini untuk mendayung kano merah muda sendirian..."

    crystal "... Setidaknya yang bisa kamu lakukan adalah memberiku sesuatu yang perlu kamu dengarkan!"

    anon "Maaf, {b}Kristal{/b}..."

    hide anon
    show crystal f_eyeroll
    with {'master': dissolve}
    crystal "Ya, terserah."

    crystal f_annoyed "Buncha tidak berterima kasih-"

    return


label crystal_button_outside.bliss:
    show crystal b_pantless_sitting f_smirk
    show anon a_sides with {'master': dissolve}:
        xoffset 100
        xzoom -1
    crystal "Ayo sekarang..."

    show anon f_grin
    crystal "... Aku butuh waktu untuk memulihkan diri setelah kejadian seperti itu!"

    anon f_normal "Hehe, oke."

    show anon a_wave
    with {'master': dissolve}
    anon "Sampai jumpa, {b}Kristal{/b}."

    hide anon
    with {'master': dissolve}
    crystal @ -m_talk "Mhmm."

    pause
    crystal "Wah..."

    crystal "... sial!"

    return


label crystal_button_outside.quickie:
    crystal f_smirk "Hei, bagaimana kalau sebentar sebelum kamu masuk ke dalam?"

    anon f_confused @ -m_talk "Hmm?"

    crystal "Sepertinya aku... jika aku harus mendengarkan kalian semua berkeliaran di sana sepanjang malam..."

    crystal f_normal "... Wajar kalau biskuit mentega mah dulu sekarang!"

    anon f_surprised "Wha-" with hpunch
    anon "Kita tidak bisa melakukan itu!"

    crystal f_annoyed "Nah, kenapa tidak?!"

    anon f_worried_surprised "{b}Roxxy{/b} ada di dalam..."

    anon f_worried "... Dia pasti akan mendengarkan kita!"

    crystal f_smirk "Pfft, dia tidak akan memedulikan kita..."

    show anon f_worried_left
    crystal "... Tidak saat dia di dalam sana sambil mengoceh dengan telepon bodoh miliknya itu!"

    anon f_worried "Oh, entahlah..."

    crystal f_annoyed "Cih, ayo sekarang..."

    crystal "... Kamu tidak akan meninggalkanku begitu saja di sini sendirian dan terluka untuk muncrat kan?!"

    show anon f_confused
    crystal "Dan di sini saya pikir Anda adalah seorang pria sejati..."

    anon @ f_skeptical "Umm, apa kamu baru saja bilang, \"Sakit mau muncrat?!\""

    crystal f_smirk "Anda sebaiknya mempercayainya!"

    show anon f_worried:
        xoffset 600
        xzoom 1
    with {'master': dissolve}
    anon "A-bagaimana dengan tetangganya?!"

    crystal f_annoyed "Oh, persetan dengan tetangga!"

    show anon f_worried:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    crystal "Aku tidak peduli dengan apa yang mereka pikirkan..."

    show crystal b_dressed_sitting_beer
    with {'master': dissolve}
    pause
    show crystal b_dressed_sitting f_smirk
    with {'master': dissolve}
    crystal "... Selain itu, meskipun gelap di sini... mereka tidak akan melihat apa pun."

    show anon a_rub
    with {'master': dissolve}
    anon @ -m_talk "{i}*Meneguk*{/i}"


    menu:
        "Maaf, tapi tidak.":
            pass
        "Baiklah, tapi ayo cepat!":

            jump crystal_button_outside.sex

    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Maaf, tidak."

    crystal f_annoyed @ f_eyeroll "Uh, baiklah."

    crystal "Lanjutkan dan singkirkan mah putri kalau begitu..."

    crystal "... Kurasa aku harus menjaga diriku sendiri... seperti biasa!"

    show crystal b_dressed_sitting_beer
    with {'master': dissolve}
    anon f_shy "Mungkin lain kali?"

    show crystal b_dressed_sitting
    with {'master': dissolve}
    crystal @ -m_talk "Mhmm."

    hide anon
    show crystal a_beer_throw f_annoyed
    with {'master': dissolve}
    pause
    show crystal a_resting
    with {'master': dissolve}
    crystal @ f_burp -m_talk "{i}*Buuuurp*{/i}"

    crystal "Anak nakal yang tidak tahu berterima kasih!"

    crystal "Ya tahu, aku juga punya kebutuhan... tapi apakah mereka peduli?!"

    crystal f_eyeroll "Psh, tentu saja tidak!"

    return 'bitter'


label crystal_button_outside.roxxy:
    anon f_confused "Ya, apakah dia ada di sini?"

    crystal "Oh ya, dia ada di dalam..."

    show anon f_normal
    crystal @ f_eyeroll "Mungkin menyalak di ponselnya, seperti biasa."

    crystal "Jika aku tidak mengetahuinya, aku berani bersumpah benda itu menempel di sisi kepala gadis itu!"

    anon "Hehe, ya."

    jump crystal_button_outside.choice


label crystal_button_outside.sex:
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "Kita harus cepat!"

    crystal "Sekarang kita memasak dengan bensin!"

    show crystal b_dressed_sitting_beer
    with {'master': dissolve}
    crystal "Hmm!"

    show crystal a_beer_throw b_dressed_sitting
    with {'master': dissolve}
    pause
    show anon f_surprised
    show crystal a_resting
    with {'master': dissolve}
    crystal @ f_burp -m_talk "{i}*Buuuurp*{/i}"

    show crystal a_sides b_dressed:
        xoffset 310
        xzoom -1
    with {'master': dissolve}
    crystal "Sekarang..."

    show anon a_empty f_shock behind crystal
    show crystal a_grab_anon
    with {'master': dissolve}
    crystal "... Kenapa kamu tidak..."

    show anon a_empty f_surprised:
        xoffset 300
        xzoom 1
    show crystal:
        xoffset 90
        xzoom 1
    with {'master': dissolve}
    crystal "... Silakan duduk di sebelah sini?"

    show anon a_surprised_up f_confused_back_low
    show crystal a_hip
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"

    show anon b_dressed_falling:
        xoffset -30
    show crystal a_push
    with fastdissolve
    pause
    show anon a_down b_dressed_sitting_chair f_shy_cringe:
        xoffset 0
    anon @ -m_talk "!!!" with vpunch
    show anon a_rest f_worried_surprised
    show crystal a_remove01
    with {'master': dissolve}
    crystal "Kamu akan belajar sesuatu malam ini, romeo..."

    show anon f_surprised
    show crystal a_remove02 b_topless_boobless
    with dissolve
    show crystal a_remove03
    with dissolve
    show crystal a_remove04 b_topless
    with {'master': dissolve}
    crystal "... Aku beritahu kamu apa!"

    show crystal b_dressed_back_shake01:
        xoffset 300
        xzoom -1
    with {'master': dissolve}
    crystal "Perbaikan ibu akan menunjukkan padamu apa yang bisa dilakukan wanita sejati!"

    show anon f_flirt_low
    show crystal b_dressed_back_shake
    with {'master': dissolve}
    pause
    show crystal b_dressed_back_remove_pants01
    with {'master': dissolve}
    crystal "Ya, kamu suka itu, kan?!"

    show anon f_shy_low
    show crystal b_dressed_back_remove_pants02
    with {'master': dissolve}
    pause
    show anon f_flirt
    show crystal a_hold_pants b_pantless:
        xoffset 50
        xzoom 1
    with {'master': dissolve}
    crystal "Anda pikir Anda bisa menangani ini?"

    anon f_shy "Y-ya, Bu."

    crystal @ f_laugh -m_talk "Hehehe..."

    crystal "... Ya sebaiknya lanjutkan dan keluarkan penis besar itu!"

    anon f_shy_down "Oh, uhh... benar."


    call scene_crystal_sex_trailer.repeat
    $ unlock_scene('Crystal', '02_unlocked')

    scene location_trailer_closeup01_new_evening
    show crystal b_pantless_disheveled f_tired_low:
        xoffset -150

    if _return == 'outside':
        show crystal a_wipe01 o_cum_drip01

    show location_trailer_closeup01_chair as chair
    show anon a_down b_dressed_sitting_chair f_flirt od_firm
    with fade
    crystal "Haaah... Haaah..."


    if _return == 'outside':
        show crystal a_wipe02 o_cum_drip02
        with {'master': dissolve}

    crystal "... Maksudku, sial!"

    show anon a_remove_shorts b_dressed f_shy_down:
        xoffset 600
    show crystal f_tired_low_back

    if _return == 'outside':
        show crystal a_idle o_empty

    with {'master': dissolve}
    crystal "Itu adalah penis rak paling atas..."

    show anon a_cover_boner
    show location_trailer_closeup01_chair as chair behind crystal
    show crystal f_smirk:
        xoffset 300
        xzoom -1
    with {'master': dissolve}
    crystal "... Aku tidak tahu di mana putriku menemukanmu, tapi aku senang dia menemukannya!"

    show anon a_sides b_dressed f_shy:
        xoffset 100
        xzoom -1
    show crystal f_smirk
    with {'master': dissolve}
    anon "Hehe, ya..."

    anon "... Saya juga."

    show anon a_surprised_up_both f_surprised
    show crystal b_pantless_falling:
        xoffset -50
        xzoom 1
    with {'master': dissolve}
    crystal "Fiuh!"

    show crystal b_pantless_sitting f_tired:
        xoffset 0
    anon f_worried "You okay?" with vpunch
    crystal @ -m_talk "Mhmm."

    show anon a_sides
    with {'master': dissolve}
    pause
    crystal "Sebaiknya Anda masuk ke dalam dan menemui {b}Roxanne{/b} sekarang..."

    crystal f_smirk "... Iffin' kamu bisa menidurinya setengah sebaik kamu baru saja meniduriku..."

    crystal "... Kita mungkin benar-benar bisa mendapatkan tidur yang nyenyak sekali!"

    anon f_shy "Hehe, aku akan mencobanya."

    crystal f_tired "Bocah Atta."

    hide anon
    with {'master': dissolve}
    pause
    crystal "Wah..."

    crystal "... Gadis itu sebaiknya bersiap untuk menikah dengan yang ini, kuberitahu ya!"

    return 'bliss'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
