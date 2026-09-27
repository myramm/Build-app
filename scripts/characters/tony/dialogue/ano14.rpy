label ano14_tony_tony_lockbox:
    anon f_unimpressed "Jadi saya pergi ke bank dan melihat kotak kunci itu..."

    tony f_normal "Oh ya?"

    tony @ f_smirk_wink "Apakah itu banyak uang?"

    anon "Tidak."

    anon "Benda bodoh itu kosong!"

    tony f_question "Kosong?"

    tony "Mengapa ayahmu menyembunyikan kunci kotak kunci yang kosong?"

    anon f_worried @ f_sad_down "{i}*Huh*{/i} Entahlah..."

    tony f_suspicious "Katakan padaku sesuatu, ayahmu... Apakah kepalanya lembut atau apa?"

    anon @ f_skeptical -m_talk "Hmm?"

    tony "Tahukah Anda, sedikit topping untuk pizza?"

    anon @ -m_talk "..."
    tony "Lampu ovennya menyala tapi tidak ada apa-apa di sana?"

    anon @ f_skeptical "Apa yang kamu bicarakan?"

    tony @ f_eyeroll "Hehe, sudahlah."

    pause
    tony f_normal "Jadi apa yang akan kamu lakukan sekarang?"

    anon "Saya berharap Anda punya ide?"

    tony "Nah, satu-satunya petunjuk lain yang kita miliki adalah {b}Walikota Rump{/b}."

    tony "Kami tahu dia terlibat tetapi tidak tahu bagaimana atau mengapa."

    tony "Aku akan mulai mencari tahu tentang dia."

    anon "Apa maksudmu?"

    tony "Anda tinggal di dekat rumahnya, bukan?"

    anon "Ya, tapi penuh dengan penjaga keamanan."

    anon "Aku tidak akan pernah masuk ke dalam."

    tony "Heh, jangan pernah bilang tidak pernah, jagoan..."

    tony "Jika dia adalah pendukung politik dan finansial mereka, maka ini adalah tempat yang tepat untuk menyerang mereka."

    anon "Ya baiklah."

    tony "{b}Aku akan mulai mengintip di sekitar rumahnya{/b} jika aku jadi kamu."

    tony "Pasti ada {b}seseorang di dalam{/b} yang bisa kita paksa untuk membantu kita?"

    tony "Kamu pikir kamu bisa mengatasinya?"

    anon "saya akan mencoba."


    if L_pizzeria_interior.is_here(M_tony):
        show tony a_mc_hip_single f_laugh:
            xoffset 32
        show tony_arms_dressed_a_mc_shoulder_single:
            flip
            xoffset 32
    else:
        show tony a_mc_hip_single f_laugh:
            xoffset -32
        show tony_arms_dressed_a_mc_shoulder_single:
            xoffset -32

    with dissolve
    tony "Attaboy!"

    show tony a_idle f_normal:
        xoffset 0
    hide tony_arms_dressed_a_mc_shoulder_single
    with dissolve

    $ M_anon.trigger(T_ano14_tony)
    jump tony_button_pizzeria.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
