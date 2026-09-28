label con02_tell_consuela:
    show anon with dissolve:
        flip
    anon "Hey, {b}Consuela{/b}!"
    consuela @ -m_talk "Hmm?"
    anon "I've got great news!"
    consuela "{i}*Sigh*{/i} What do you want now?" (show_native="{i}*Sigh*{/i} ¿Y ahora que quieres?")
    anon "I found you work."
    consuela @ -m_talk "..."
    anon "I got you a job cleaning the church."
    consuela @ -m_talk "..."
    consuela "I clean?"
    anon @ f_laugh "Heh, yes!"
    show consuela f_surprised
    anon "You clean."
    anon "Come on!"
    hide anon with dissolve
    consuela f_annoyed "Are you serious?" (show_native="¿Habla en serio?")
    hide consuela with dissolve

    scene black with dissolve
    $ player.go_to(L_church_front)
    $ M_consuela.trigger(T_con02_tell)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
