label kha01_init_nadya:
    show anon a_wave behind nadya with dissolve:
        xoffset -100
    show nadya a_sides
    with {'master': dissolve}
    nadya "Oh bagus, kamu di sini!"

    show svetlana a_sides:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    nadya "Aku punya pekerjaan untukmu."

    show anon a_sides
    with {'master': dissolve}
    anon f_worried "Uhh, aku masih perlu waktu lagi untuk memikirkan tawaranmu jika kamu-"

    show svetlana f_curious_back
    nadya "Tidak, tidak, tidak... Bukan pekerjaan itu!"

    show anon f_confused
    nadya "Sesuatu yang lain."

    nadya "Sesuatu yang kecil."

    anon "Oh?"

    show svetlana a_hips f_concerned:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "That was not a small mess that I had to clean up." (show_native="Eto byl ne malen'kiy besporyadok, kotoryy mne prishlos' ubrat'.")
    show nadya a_dismiss
    with {'master': dissolve}
    nadya @ f_eyeroll "Oh, berhentilah melebih-lebihkan!"

    nadya "Itu hanyalah ledakan kecil dan sangat kecil."

    show anon f_surprised
    show nadya a_sides
    show svetlana a_crossed f_bored:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    svetlana @ f_eyeroll -m_talk "Pfft!"

    anon f_worried_surprised "Ledakan?"

    anon f_worried "Y-maksudmu tempo hari... Saat {b}Katya{/b} dan aku-"

    nadya f_bored "Ya."

    nadya "Salah satu potongan gambar kami di laboratorium."

    nadya "Tampaknya penyuling utama kita tertidur dan gagal dalam tugasnya."

    show anon f_confused

    if M_khadne.get('chat', False):
        anon "Maksudmu {b}Khadne{/b}?"

        nadya f_normal "Ya."

    else:

        anon "Penyuling ahli?"

        nadya f_normal "Ya."

        nadya "Namanya {b}Khadne{/b}."


    show nadya a_hips
    with {'master': dissolve}
    nadya "Pernah menjadi budak rendahan Papa, aku menyadari bahwa bakatnya ada di tempat lain."

    nadya f_happy "Vodkanya tidak hanya enak, tetapi juga sangat menguntungkan."

    svetlana @ f_eyeroll "Dia membuat lebih banyak masalah daripada vodka."

    nadya f_frowning "Have you tried her recipe?" (show_native="Vy poprobovali yeye retsept?")
    show svetlana a_sides f_bored:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "{i}*Sigh*{/i} Yes, it is quite good." (show_native="Da, eto ochen' khorosho.")
    nadya f_happy "It's exquisite!" (show_native="Eto izyskanno!")
    svetlana f_concerned @ f_annoyed "Tapi tidak ada gunanya mati di neraka gudang."

    nadya f_normal "Setuju."

    show nadya a_point
    with {'master': dissolve}
    nadya "Itu sebabnya saya meminta bantuannya."

    show anon a_point_self f_surprised
    show svetlana:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    anon "A-aku?"

    show nadya a_sides
    with {'master': dissolve}
    anon "Apa yang bisa saya lakukan?"

    show anon a_sides f_confused
    with {'master': dissolve}
    nadya "Masalah {b}Khadne{/b} bukanlah masalah kelalaian."

    svetlana f_concerned_back "Stupidity more like..." (show_native="Glupost' bol'she pokhozha...")
    nadya f_frowning "Nyet." (show_native="No.")
    nadya "Dia hanya mengalami depresi."

    show svetlana a_confused f_curious:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "Apa yang membuatnya depresi?!"

    nadya f_normal "Dia sendirian, di negara asing... melakukan pekerjaan yang menurut dia tidak cocok dilakukannya sejak dia masih kecil."

    show svetlana a_hips
    with {'master': dissolve}
    svetlana "Kita semua sendirian di tempat ini."

    svetlana "You should not baby her." (show_native="Vy ne dolzhny yeye detka.")
    nadya "Not everyone is as strong as you, {b}Svetlana{/b}." (show_native="Ne vse takiye sil'nyye, kak ty, {b}Svetlana{/b}.")
    show svetlana a_crossed f_bored
    with {'master': dissolve}
    svetlana @ -m_talk "Hmph."

    show anon a_wave f_shy
    with {'master': dissolve}
    anon "Permisi, nona-nona?"

    show svetlana:
        xoffset -100 xzoom 1
    with {'master': dissolve}
    nadya @ -m_talk "Hmm?"

    show anon a_sides
    with {'master': dissolve}
    anon "Aku masih tidak yakin bagaimana aku bisa menyesuaikan diri dengan semua ini."

    nadya f_happy "Saya pernah mendengar, bahwa seorang pemimpin yang baik harus menggunakan segala alat yang dimilikinya untuk memecahkan masalah yang sulit..."

    show anon f_confused
    show nadya f_sexy_low
    with {'master': dissolve}
    pause
    show nadya a_point
    with {'master': dissolve}
    nadya "Dan di dalam kamu, Aku mempunyai alat yang sangat besar."

    show anon a_crossed f_unimpressed
    show nadya f_laugh
    with {'master': dissolve}
    svetlana f_happy_back @ f_laugh "Hah!"

    svetlana "That's an understatement." (show_native="Eto preumen'sheniye.")
    show nadya a_hips f_happy
    with {'master': dissolve}
    nadya "Hehe, right?" (show_native="Hehe, verno?")
    show svetlana f_happy
    anon f_skeptical "Jadi apa, kamu ingin aku tidur dengannya juga?"

    nadya f_sexy "Jika perlu."

    show nadya a_finger f_normal
    with {'master': dissolve}
    nadya "Yang terpenting, saya ingin Anda menghiburnya."

    show anon a_sides f_disgusted
    show nadya f_sexy
    with {'master': dissolve}

    if M_khadne.get('chat', False):
        nadya "Dari apa yang kudengar, kamu sudah mempunyai hubungan baik dengannya."

        show nadya a_hips
        with {'master': dissolve}
        anon f_confused "Saya bersedia?"

        nadya f_normal "Ya."

        nadya "{b}Katya{/b} memberitahuku bahwa gadis itu cukup menyukaimu."

        anon f_worried "Hmm, bukan itu kesan yang saya dapatkan."

        show nadya a_hips_shrug f_pouting
        with {'master': dissolve}
        nadya "Ya, baiklah... {b}Khadne{/b} bukanlah orang yang paling mudah dibaca."

        show nadya a_hips f_normal
        with {'master': dissolve}
    else:

        nadya "Dan berdasarkan pengaruh yang kamu berikan pada gadis-gadisku yang lain..."

        show nadya a_hips
        with {'master': dissolve}
        nadya f_sexy "... Menurutku kamu adalah orang yang tepat untuk tugas itu."


    anon f_unimpressed "Kau tahu, aku mulai merasa seperti pelacur di sini."

    nadya f_confused "Dan ini hal yang buruk?"

    nadya "Saya berasumsi manusia menikmati pekerjaan ini."

    nadya "Apakah kamu tidak menganggap gadis-gadisku cantik?"


    menu:
        "Bagaimana dengan kamu dan aku?":
            anon f_shy "Aku hanya berpikir, mungkin kita..."

            show anon a_shy_neck f_shy_down
            with {'master': dissolve}
            anon "... Punya sesuatu yang istimewa, kamu tahu?"

            show anon a_sides f_surprised
            show nadya a_sides f_sexy:
                xoffset -398
            show svetlana a_sides f_surprised
            with {'master': dissolve}
            pause
            show anon a_surprised_up f_empty
            show nadya a_pinch_face f_pouting
            with {'master': dissolve}
            nadya "Aduh, apakah ini yang membuatmu kesal?"

            show svetlana f_smirk
            nadya "Kamu {i}{/i} spesial bagiku, {b}[firstname]{/b}..."

            show anon a_surprised f_surprised
            show nadya a_finger f_frowning
            with {'master': dissolve}
            nadya "... Tapi bisnis adalah yang utama, mengerti?"

            show anon a_sides f_frown_down
            with {'master': dissolve}
            anon "Saya rasa begitu."

            show nadya a_hips
            with {'master': dissolve}
        "Tentu saja saya tahu.":

            show anon a_surprised_up f_worried
            with {'master': dissolve}
            anon "T-tidak, bukan itu!"

            anon "Menurutku mereka semua cantik."

            show anon a_sides f_flirt
            with {'master': dissolve}
            anon "Seperti, gila super duper panas."

            show anon f_flirt_grin
            show nadya f_surprised
            show svetlana a_surprised f_surprised
            with {'master': dissolve}
            pause
            show svetlana a_sides f_happy_down o_blush
            with {'master': dissolve}
            pause
            show anon a_surprised_up_both f_surprised_teeth
            show nadya a_crossed f_angry:
                xoffset -398
            with {'master': dissolve}
            anon @ -m_talk "!!!"
            anon f_worried @ f_shy "{i}*Ahem*{/i} T-tidak secantik kamu, tentu saja."

            show anon a_sides
            show svetlana f_surprised -o_blush
            with {'master': dissolve}
            nadya f_bored @ -m_talk "Mhmm."

            show svetlana f_concerned
            nadya f_confused "Jadi apa masalahnya?!"

            anon f_sad_down "{i}*Huh*{/i} Tidak ada, kurasa..."


    nadya f_normal "Then it's settled!" (show_native="Togda eto resheno!")
    nadya "Sekarang tolong..."

    show nadya a_point_angry behind anon:
        xoffset 150 xzoom -1
    show svetlana f_happy
    with {'master': dissolve}
    nadya "... Kerjakan sihirmu."

    svetlana @ f_laugh "Hehe..."

    show nadya a_sides
    with {'master': dissolve}
    svetlana "... dick magic." (show_native="... dik magiya.")
    show anon f_unimpressed
    show svetlana f_laugh
    nadya f_laugh "hehe!"

    anon "Ya baiklah."

    hide anon
    show svetlana a_sides f_smirk:
        xoffset 450 xzoom -1
    with {'master': dissolve}
    svetlana "Tangkap dia, harimau."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
