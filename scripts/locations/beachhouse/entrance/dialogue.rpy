label beachhouse_entrance_babies:
    scene expression player.location.background_blur
    show consuela a_baby f_normal_down
    show anon with dissolve
    if M_consuela.pregnancy.baby_gender == 'twins':
        anon "Hey, what are you three doing here?"

    else:
        anon "Hey, what are you two doing here?"

    consuela f_normal "I come."

    consuela "Bersih bagus."

    anon "You don't have to do that!"

    consuela "No, I do."

    anon f_worried "Really, you don't."

    if M_consuela.pregnancy.baby_gender == 'twins':
        consuela f_sad "Ehh, es okay I bring ¿los bebes?"

        anon "¿Los bebes?"

        consuela "Babies."

    else:
        consuela f_sad "Ehh, es okay I bring ¿el pequeño?"

        anon "¿El pequeño?"

        consuela "Baby."

    anon @ f_normal "Oh, of course it's okay."

    anon "But seriously you don't have to clean-"

    consuela f_normal @ f_laugh "Gracias, papi!"

    consuela "Saya membersihkan sekarang."

    anon "No, but-"

    hide consuela with dissolve
    pause
    anon f_sad_down a_behind_head @ -m_talk "( {i}*Sigh*{/i} It's impossible to get her to stop cleaning... )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
