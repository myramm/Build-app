label consuela_button_recovery:
    show anon with dissolve
    consuela "Halo, ayah."

    consuela "Kamu datang menemui sayang?"


    menu consuela_button_recovery.choice:
        "Ya.":
            pass

    anon "Ya, bagaimana kabar kalian?"

    consuela "Itu bagus."

    consuela f_normal_down "Tidur banyak."

    anon "Ya, aku yakin kamu kelelahan."

    consuela "Ya, kelelahan."

    consuela f_normal "And hungry!" (show_native="¡Y hambriento!")
    anon @ -m_talk "Hmm?"

    consuela "Eh, makanan?"

    anon @ f_surprised "Oh, kamu lapar?"

    consuela "Ya, lapar."

    anon @ f_laugh "Aku akan memberi tahu perawatnya, oke?"

    consuela "Terima kasih, ayah."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
