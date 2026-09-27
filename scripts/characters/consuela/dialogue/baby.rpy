label consuela_button_baby:
    show consuela a_baby f_normal_down
    show anon with dissolve
    consuela "Halo, ayah."

    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Hei, kalian bertiga."

    else:
        anon "Hei, kalian berdua."

    anon "Apakah kamu membantu ibu bersih-bersih?"

    consuela f_normal @ f_laugh "Hehe, saudara."

    consuela "Bantuan yang bagus."


    menu consuela_button_baby.choice:
        "Bisakah saya meyakinkan Anda untuk berhenti membersihkan?":
            jump consuela_button_baby.stop
        "Kalian butuh sesuatu?":

            jump consuela_button_baby.need
        "Aku serahkan padamu kalau begitu.":

            pass

    anon "Aku akan meninggalkanmu."

    consuela "Ya, ayah."

    consuela "Saya membersihkan sekarang."

    hide anon with dissolve
    return


label consuela_button_baby.stop:
    anon "Bisakah saya meyakinkan Anda untuk berhenti membersihkan?"

    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Setidaknya saat bayinya ada di sini?"

    else:
        anon "Setidaknya selama bayinya ada di sini?"

    consuela f_sad "Apa?"

    consuela "Tidak bersih?"

    anon "Ya, tidak bersih."

    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Bermain dengan bayi."

    else:
        anon "Bermain dengan bayi."

    consuela "No, my children must learn that work comes first." (show_native="No, mis hijos deben aprender que el trabajo es lo primero.")
    consuela f_normal_down "I want them to be responsible people." (show_native="Quiero que sean personas responsables.")
    anon f_worried @ -m_talk "..."
    consuela f_normal "Tidak apa-apa."

    consuela @ f_laugh "saya membersihkan."

    anon "{i}*Huh*{/i} Baiklah, jika Anda bersikeras."

    jump consuela_button_baby.choice


label consuela_button_baby.need:
    anon f_normal "Kalian butuh sesuatu?"

    consuela "Tidak, itu bagus."

    consuela f_normal_down "saya mengajar."

    consuela "Bekerja keras."

    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Anda mengajari bayi kami untuk bekerja keras?"

        consuela "You will be great workers someday, right?" (show_native="Serán grandes trabajadores algún día, ¿verdad?")
    else:
        anon "Anda mengajari bayi kami untuk bekerja keras?"

        consuela "You will be a great worker someday, right?" (show_native="Serás un gran trabajador algún día, ¿no?")
    anon @ -m_talk "..."
    anon "Baiklah, jangan memaksakan diri terlalu keras..."

    consuela f_normal "Oke, ayah."

    jump consuela_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
