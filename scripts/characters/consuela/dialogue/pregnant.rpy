label consuela_button_event_pregnancy:
    $ M_consuela.pregnancy.set('announced_pregnancy')
    if not M_consuela.pregnancy.number_of_babies:
        jump consuela_button_event_pregnancy.initial
    jump consuela_button_event_pregnancy.repeat


label consuela_button_event_pregnancy.initial:
    show consuela b_magic a_hips
    show anon f_worried with dissolve
    consuela "Ayah!"

    anon "Itu dia."

    anon "Apa yang terjadi?"

    consuela @ a_idle "We're going to have a baby!" (show_native="¡Vamos a tener un bebé!")
    anon f_confused @ -m_talk "Hmm?"

    consuela f_sad "Eh."

    consuela "saya"

    consuela "hamil."

    anon "Hamil?"

    consuela f_normal @ f_laugh "Ya, hamil!"

    anon "Itu bukan sebuah kata."

    consuela "Hamil, hamil."

    anon f_surprised "Tunggu sebentar..."

    anon @ f_surprised_teeth -m_talk "!!!" with hpunch
    anon "Apakah Anda mencoba mengatakan bahwa Anda sedang hamil?"

    consuela "Ya."

    consuela "Anda."

    consuela "Taruh sayang."

    consuela f_normal_down @ a_idle "Di dalam."

    anon f_sad_down a_behind_head "Sialan..."

    show consuela f_sad
    pause
    consuela "Kamu tidak suka, papi?"

    anon f_worried "Tidak, aku suka."

    anon "aku, um-"

    consuela f_angry "Sayang itu berkah!"

    anon "Y-ya, aku tahu."

    anon f_normal a_idle "Itu hanya sedikit tidak terduga, itu saja."

    show consuela f_normal
    pause
    anon "Wow, aku akan menjadi seorang ayah?"

    consuela "Ya, ayah."

    consuela "I'm so excited to have your baby!" (show_native="¡Estoy tan emocionada de tener a tu bebé!")
    consuela "I will pray for a boy this time." (show_native="Rezaré por un chico esta vez.")
    anon "Ada yang bisa kuberikan padamu?"

    consuela @ -m_talk "..."
    anon "Tahukah Anda, seperti minuman hangat atau pijat kaki atau semacamnya?"

    consuela @ f_sad "Kaki?"

    anon "Ya."

    consuela "Tidak, oke."

    consuela "saya membersihkan."

    anon f_worried @ f_unimpressed "{b}Consuela{/b}..."

    anon "Anda sebenarnya tidak boleh melakukan pekerjaan kasar saat Anda hamil."

    consuela "Baik, ayah."

    consuela "saya membersihkan."

    consuela "Lebih banyak uang untuk bayi."

    anon "Anda yakin?"

    consuela "Ya."

    consuela "Don't worry, hard work will strengthen the baby." (show_native="No se preocupe, el trabajo duro fortalecerá al bebé.")
    anon @ -m_talk "Hmm?"

    show consuela b_kiss
    hide anon
    with dissolve
    pause
    consuela "Muah!"

    show consuela b_magic
    show anon
    with dissolve
    consuela "Our baby will be beautiful, daddy." (show_native="¡Nuestro bebé será hermoso, papi.")
    consuela "You'll see." (show_native="Verás.")
    anon @ -m_talk "..."
    consuela "Saya membersihkan sekarang."

    anon "O-oke."

    hide consuela with dissolve
    anon @ -m_talk "(Saya yakin dia tahu apa yang dia lakukan...)"

    anon @ -m_talk "(Lagi pula, dia telah melakukan ini sebelumnya.)"

    pause
    anon f_worried @ -m_talk "( Sobat, bagaimana reaksi {b}Martinez{/b} dan {b}Lopez{/b} terhadap hal ini? )"

    anon f_surprised_teeth @ -m_talk "(Aku bahkan takut untuk memikirkannya.)"

    hide anon with dissolve
    return


label consuela_button_event_pregnancy.repeat:
    show consuela b_magic a_hips
    show anon f_worried with dissolve
    consuela "Ayah!"

    anon "Itu dia."

    anon "Apa yang terjadi?"

    consuela @ a_idle "I'm with child again." (show_native="Estoy con un niño otra vez.")
    anon f_normal @ f_surprised "Anda hamil lagi?"

    consuela "Ya, hamil."

    anon "Itu luar biasa!"

    consuela "Ya, luar biasa."

    show consuela b_kiss
    hide anon
    with dissolve
    pause
    show consuela b_magic
    show anon
    with dissolve
    consuela "It's greedy for me to have more of your children..." (show_native="Es codicioso para mí tener más de tus hijos...")
    consuela "{b}Camila{/b} and you should be giving me grandbabies!" (show_native="¡{b}Camila{/b} y tú deberías darme nietos!")
    anon "Ya, saya tidak mengerti apa yang Anda katakan."

    consuela "Tidak apa-apa."

    consuela "Saya melakukannya untuk Anda, {b}[firstname]{/b}."

    anon "Terima kasih, {b}Consuela{/b}."

    anon "Aku melakukannya untukmu juga."

    consuela @ f_laugh "hehe!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
