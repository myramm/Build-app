label yoyo_event_intro:
    show anon a_behind_head f_worried with dissolve
    anon "Umm, h-hai."

    yoyo "Pahlawan."

    show anon a_sides
    show yoyo a_sides
    with {'master': dissolve}
    yoyo "Bisakah saya membantu Anda?"

    anon "aku rasa kita belum pernah bertemu..."

    anon "... aku-"

    show anon a_surprised f_surprised_teeth
    yoyo f_angry "Sirence!!" with hpunch
    anon "!!!"
    yoyo "Kamu mengajakku jalan-jalan?!"

    show anon a_up f_surprised with {'master': dissolve}
    anon "Apa-"

    show yoyo f_normal
    with {'master': dissolve}
    anon "T-tidak, aku tidak-"

    yoyo "{b}Kim{/b} mengenalmu!"

    anon "Eh?"

    yoyo "Pria bodoh yang mencuri istri pelacur {b}Kim{/b} dan mengirimnya penjara."

    show anon a_sides f_unimpressed with {'master': dissolve}
    anon "Oh."

    anon f_skeptical "Umm, bisakah kamu tidak membicarakan {b}Liu{/b} seperti itu?"

    anon "Dia gadis yang baik, dan dia cukup menderita."

    show anon a_surprised_up f_surprised_teeth
    yoyo f_angry "Sirence!!" with hpunch
    yoyo "Anda mengasuransikan {b}Kim{/b} kehormatan keluarga!"

    show anon a_up f_worried with {'master': dissolve}
    anon "Ayolah, nona... aku tidak mau-"

    yoyo "{b}Kim{/b} sampai jumpa lagi atas kejahatanmu!"

    show anon a_sides f_confused with {'master': dissolve}
    anon "Hah?!"

    yoyo "Aku berkata, {b}Kim{/b} wirr-"

    anon f_skeptical "Ya, aku mendengarmu..."

    anon "... Tapi bagaimana dia akan melakukan itu dari sel penjara?"

    show yoyo a_stop with {'master': dissolve}
    yoyo f_normal "Bukan itu {b}Kim{/b}..."

    show yoyo a_crossed
    with {'master': dissolve}
    yoyo "... Ini {b}Kim{/b}."

    anon f_surprised @ -m_talk "!!!"
    yoyo "Aku."

    anon f_skeptical "Jadi tunggu dulu, kalian berdua bernama {b}Kim{/b}?"

    yoyo "Ya."

    pause
    anon f_laugh @ f_happy "Bukankah itu membingungkan?"

    show yoyo a_sides with {'master': dissolve}
    yoyo @ -m_talk "..."
    show anon f_normal
    yoyo "Ha ha."

    yoyo "Raugh semampumu, pria bodoh..."

    yoyo "... Pembalasan datang untukmu dengan sayap cepat."

    show anon f_worried
    pause
    anon f_confused "Bisakah kita tidak melakukan ini?"

    yoyo f_quizzical @ -m_talk "...?"
    anon f_worried "Kau tahu, seluruh musuh bebuyutan ini... penjahat jahat yang ingin membalas dendam atas keluarga mereka yang juga jahat..."

    show yoyo f_normal
    anon "... Karena aku harus memberitahumu, aku sangat lelah setelah berurusan dengan kakakmu..."

    pause
    anon f_confused "... Tidak?"

    pause
    anon f_tired "{i}*Huh*{/i} Baik."

    pause
    anon a_wave f_unimpressed "Kurasa aku akan segera menemuimu?"

    yoyo @ -m_talk "..."
    hide anon with dissolve

    scene expression background(l=L_dealership_showroom) as stage with fade
    show anon f_unimpressed with dissolve:
        xoffset -350
        xzoom -1
    anon "Luar biasa."

    pause
    anon "Ya, ada sesuatu yang tidak ingin aku tangani..."

    anon f_thinking_down "Saya ingin tahu apa yang {b}Josephine{/b} katakan tentang ini?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
