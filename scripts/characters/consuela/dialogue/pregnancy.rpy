label consuela_button_pregnant:
    show anon with dissolve
    consuela "Halo, ayah."

    anon "Hai, {b}Consuela{/b}."


    menu consuela_button_pregnant.choice:
        "Bagaimana perasaanmu?":
            if M_consuela.pregnancy.stage < 2:
                jump consuela_button_pregnant.nausea
            if M_consuela.pregnancy.stage < 3:
                jump consuela_button_pregnant.kick
            jump consuela_button_pregnant.poop
        "{b}Martinez{/b}.":

            jump consuela_button_pregnant.camila
        "Aku serahkan padamu kalau begitu.":

            pass

    anon f_normal "Aku serahkan padamu kalau begitu."

    consuela "Ya."

    consuela "saya membersihkan."

    anon @ a_point "Yup, kamu bersih-bersih."

    hide anon with dissolve
    return


label consuela_button_pregnant.nausea:
    anon f_normal "Bagaimana perasaanmu?"

    consuela @ -m_talk "Hmm?"

    consuela "Oh, aku baik-baik saja."

    consuela "Just a little morning sickness, not too bad." (show_native="Solo un poco de náuseas matutinas, no tan mal.")
    anon "Baiklah."

    anon "Bisakah saya melakukan sesuatu untuk Anda?"

    consuela "Lakukan untukku?"

    consuela @ f_laugh "Tidak, ayah... Aku bersedia untukmu!"

    anon "Heh, aku tahu itu tapi kamu sedang hamil sekarang dan-"

    pause
    anon "Ehh, sudahlah."

    anon "Beri tahu saya jika Anda butuh sesuatu, oke?"

    consuela "Ya."

    consuela "Terima kasih, ayah."

    jump consuela_button_pregnant.choice


label consuela_button_pregnant.kick:
    anon "Bagaimana perasaanmu?"

    consuela @ -m_talk "Hmm?"

    consuela "Oh, aku baik-baik saja."

    consuela f_normal_down "Our little one is starting to kick." (show_native="Nuestro pequeño está empezando a patear.")
    anon @ f_laugh "Saya tidak yakin apa maksudnya."

    consuela "Eh, dia membuat tendangan."

    consuela f_normal "Di dalam."

    anon f_surprised "{i}Dia{/i}?"

    anon "Maksudmu, itu laki-laki?"

    consuela "Ya, nak."

    anon f_normal "Hehe, bagaimana kamu tahu itu?"

    consuela @ a_boobs "Because my right breast is bigger than my left." (show_native="Porque mi seno derecho es más grande que el izquierdo.")
    anon f_worried @ f_shock "!!!"
    anon "Hmm, oke."

    anon f_confused "Ada hubungannya dengan payudaramu?"

    consuela "Ya, payudara."

    show anon f_normal
    consuela "Yang satu sangat besar."

    consuela "Satu ya, um..."

    anon "Kecil?"

    consuela "Yes, small." (show_native="Si, pequeña.")
    anon "Benar."

    anon @ f_shy a_behind_head "Kurasa aku harus menuruti kata-katamu saja."

    jump consuela_button_pregnant.choice


label consuela_button_pregnant.poop:
    anon "Bagaimana perasaanmu?"

    consuela f_sad "Ugh, not so good..." (show_native="Ugh, no tan bien...")
    consuela "I'm so incredibly constipated!" (show_native="¡Estoy tan increíblemente estreñido!")
    anon f_worried "Saya tidak tahu apa yang Anda katakan tetapi kedengarannya tidak bagus..."

    consuela f_surprised "I haven't pooped in five days!" (show_native="¡No he defecado en cinco días!")
    anon "Mungkin sebaiknya kau berbaring..."

    consuela f_sad @ -m_talk "Eh?"

    anon "Anda harus berada di tempat tidur."

    consuela "Tidak ada tempat tidur."

    consuela "saya membersihkan."

    anon "{b}Consuela{/b}..."

    consuela "I'm going to scrub the floors." (show_native="Voy a fregar el piso.")
    consuela "Maybe that will jar something loose..." (show_native="Tal vez eso sacudirá algo suelto...")
    anon @ -m_talk "..."
    jump consuela_button_pregnant.choice


label consuela_button_pregnant.camila:
    anon f_worried "Apakah Anda sudah memberi tahu putri Anda tentang bayi itu?"

    consuela "{b}Camila{/b}?"

    consuela "What about her?" (show_native="¿Que hay de ella?")
    anon @ -m_talk "..."
    anon "Bayi itu."

    consuela @ f_surprised "Oh!"

    consuela @ f_laugh "Ya, {b}Camila{/b} bagus."

    consuela f_smirk "Kamu pergi berkencan sekarang?"

    anon "Tidak, bukan itu yang aku-"

    show anon f_unimpressed
    pause
    anon "Ehh, sudahlah."

    jump consuela_button_pregnant.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
