label consuela_button_mall:
    show anon f_worried with dissolve:
        flip
    anon @ -m_talk "..."
    anon "B-permisi, {b}Consuela{/b}?"

    consuela @ -m_talk "Hmm?"

    consuela f_annoyed "Oh, it's you..." (show_native="Oh, eres tú...")
    consuela "Have you found me a job?" (show_native="¿Me has encontrado un trabajo?")
    anon @ f_sad_down a_behind_head "Ehh."


    menu consuela_button_mall.choice:
        "Bisakah kamu memahamiku?":
            jump consuela_button_mall.comprende
        "Tanda Anda salah eja.":

            jump consuela_button_mall.sign
        "Sudahlah.":

            pass

    anon @ a_wave "Aku akan mencarikanmu pekerjaan, oke?"

    anon "Saya berjanji."

    consuela "Y-ya."

    consuela "Cari pekerjaan."

    consuela "saya membersihkan."

    show anon f_unimpressed
    anon @ -m_talk "..."
    consuela @ -m_talk "..."
    anon "Benar."

    anon @ a_wave "Saya akan kembali."

    hide anon with dissolve

    scene expression player.location.background_blur with fade
    show anon with dissolve
    anon a_thinking f_thinking @ -m_talk "( Hmm, saya perlu mencari {b}Consuela{/b} pekerjaan. )"

    anon @ -m_talk "( Saya harus {b}mulai dari gereja{/b}, saya yakin orang-orang di sana akan bersedia membantu {b}Consuela{/b} pada saat dia membutuhkan. )"

    hide anon with dissolve
    return


label consuela_button_mall.comprende:
    anon @ a_point_self "Bisakah kamu memahamiku?"

    consuela f_sad @ -m_talk "..."
    consuela "What?" (show_native="¿Qué?")
    show anon f_hurt a_facepalm with dissolve
    pause
    anon a_idle f_worried @ f_angry "BISA. ANDA. MEMAHAMI. AKU?"

    consuela f_annoyed "I. DON'T. SPEAK. ENGLISH." (show_native="NO. HABLO. INGLES.")
    consuela "Idiot." (show_native="Idiota.")
    anon @ a_thinking f_thinking "Hmm, kurasa tidak."

    jump consuela_button_mall.choice


label consuela_button_mall.sign:
    anon @ a_point "Tanda Anda salah eja."

    consuela f_sad @ -m_talk "..."
    anon "Itu seharusnya C-L-E-A-N."

    anon "Bukan C-L-E-E-N."

    show consuela f_sad_down
    pause
    consuela f_sad "What?" (show_native="¿Qué?")
    anon @ -m_talk "..."
    consuela "I do not understand you..." (show_native="No te entiendo...")
    anon @ f_sad_down "Sudahlah."

    jump consuela_button_mall.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
