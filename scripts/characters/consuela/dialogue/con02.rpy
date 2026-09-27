label con02_tell_consuela:
    show anon with dissolve:
        flip
    anon "Hai, {b}Consuela{/b}!"

    consuela @ -m_talk "Hmm?"

    anon "Saya punya kabar baik!"

    consuela "{i}*Sigh*{/i} What do you want now?" (show_native="{i}*Sigh*{/i} ¿Y ahora que quieres?")
    anon "Saya menemukan Anda bekerja."

    consuela @ -m_talk "..."
    anon "Aku memberimu pekerjaan membersihkan gereja."

    consuela @ -m_talk "..."
    consuela "saya membersihkan?"

    anon @ f_laugh "Hehe, ya!"

    show consuela f_surprised
    anon "Anda membersihkan."

    anon "Ayo!"

    hide anon with dissolve
    consuela f_annoyed "Are you serious?" (show_native="¿Habla en serio?")
    hide consuela with dissolve

    scene black with dissolve
    $ player.go_to(L_church_front)
    $ M_consuela.trigger(T_con02_tell)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
