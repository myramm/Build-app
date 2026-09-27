label melonia_button_common(venue, level):
    call expression 'melonia_button_{}.intro{}'.format(venue, level)

    label melonia_button_common.choice:
    if level == 0:
        menu:
            "Tolong, berhenti memanggilku Hector...":
                jump melonia_button_common.hector
            "Bagaimana rasanya menjadi istri walikota?":

                jump melonia_button_common.wife

            "Konsuela." if venue == 'bedroom' and M_consuela.is_state(S_con01_init):
                jump con01_init_melonia

            "Pengganti Consuela." if M_consuela.between_states(S_con01_plan, S_con01_give) and not M_consuela.finished_state(S_con01_skip):
                jump con01_plan_melonia
            "Sudahlah.":

                pass

    elif level == 1:
        menu:
            "Apa pun yang saya inginkan?":
                jump melonia_button_common.names

            "Baiklah, aku akan menari." if venue == 'hottub':
                jump melonia_button_hottub.dance
            "Bagaimana rasanya menjadi istri walikota?":

                jump melonia_button_common.wife

            "Konsuela." if venue == 'bedroom' and M_consuela.is_state(S_con01_init):
                jump con01_init_melonia

            "Pengganti Consuela." if M_consuela.between_states(S_con01_plan, S_con01_give) and not M_consuela.finished_state(S_con01_skip):
                jump con01_plan_melonia

            "Bantuan dengan para penjaga." if game.timer.is_evening() and M_anon.is_state(S_ano19_code):
                jump melonia_button_bedroom.guards

            "Bantuan dengan para penjaga." if game.timer.is_evening() and M_anon.is_state(S_ano20_init):
                jump ano20_init_melonia_guards
            "Seks.":

                jump expression 'melonia_button_{}.suggest'.format(venue)
            "Mungkin nanti.":

                pass
    else:

        menu:
            "Kamu telanjang!":
                jump melonia_button_common.naked
            "Tentang suamimu...":

                jump melonia_button_common.husband

            "Haruskah aku menari untukmu?" if venue == 'hottub':
                jump melonia_button_hottub.dance
            "Seks.":

                jump expression 'melonia_button_{}.suggest'.format(venue)
            "Saya harus pergi.":

                pass

    call expression 'melonia_button_{}.outro{}'.format(venue, level)
    return _return


label melonia_button_common.hector:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Nama saya {b}[firstname]{/b}."


    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Oh, berhenti main-main, {b}Hector{/b}."

    melonia "Aku sedang tidak mood untuk bermain game."

    anon "aku serius!"


    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    melonia "Aku juga."

    pause
    anon @ f_sad_down "{i}*Huh*{/i}"

    jump melonia_button_common.choice


label melonia_button_common.husband:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Tentang suamimu..."


    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal b_naked a_idle with dissolve

    anon "Saya kira Anda cukup bahagia sekarang karena suami Anda telah tiada, ya?"

    melonia "Oh, bebannya seperti terangkat, {b}[firstname]{/b}!"

    melonia f_disgusted "Bobotnya besar, gemuk, keriput, berwarna oranye..."


    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Sebenarnya, aku sedang berpikir untuk berlibur atau apalah!"


    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon "Oh?"

    melonia "Pernahkah Anda ke Bahama, {b}[firstname]{/b}?"

    anon "Tidak bisa bilang aku punya, tidak."

    melonia "Saya melakukan satu panggilan telepon dan kami bisa berada di pantai, menyeruput Mai Tais dalam beberapa jam."

    melonia "Apa yang kamu katakan?"


    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Ehh, entahlah..."

    anon "... Ini bukan waktu yang tepat untukku."


    if venue == 'hottub':
        show melonia f_confused_up
    else:
        show melonia f_confused

    melonia @ -m_talk "Hmm?"

    anon "Mungkin lain kali?"


    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    melonia "Dengan serius?"

    anon "Maaf."

    melonia "Baiklah baiklah."

    pause

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Kurasa, kita hanya perlu menghibur diri kita sendiri di sini, hmm?"


    if venue != 'hottub':
        show melonia b_naked_sexy with dissolve
    jump melonia_button_common.choice


label melonia_button_common.names:
    anon f_skeptical "Apa pun yang saya inginkan?"


    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia @ -m_talk "Mhmm."


    melonia "Apa pun!"

    anon f_thinking @ -m_talk "Hmm."

    anon f_skeptical "Pak?"


    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    pause
    melonia @ f_eyeroll "Saya mengharapkan sesuatu yang sedikit lebih imajinatif."


    if venue == 'hottub':
        show anon f_shy_low
    else:
        show anon f_shy

    anon "Guru?"


    if venue == 'hottub':
        show melonia f_confused_up
    else:
        show melonia f_confused

    melonia "Benar-benar?"


    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Tidak?"


    anon f_thinking a_thinking "Oke..."

    pause

    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon a_idle "Bagaimana dengan, \"{b}Raja [firstname]{/b}?\""


    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Oh, sekarang kamu menghidupkan mesinku!"

    melonia "Bolehkah aku mengurus tongkat kerajaanmu, {b}Raja [firstname]{/b}?"

    pause
    anon f_grin @ f_surprised "Tunggu, aku mengerti!"

    pause
    anon f_brag_closed a_point_self "Panggil aku..."

    anon "\"Tuan Presiden!\""

    show anon f_grin a_idle with dissolve

    if venue == 'hottub':
        show melonia f_surprised_up
    else:
        show melonia f_surprised

    pause
    melonia f_disgusted_down "eh!"


    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Tidak?"

    melonia "My lady wood baru saja berubah dari tengah malam menjadi pukul enam."

    anon "Hah?!"

    melonia "Itu salah!"

    anon f_sad_down "Ah, kawan."

    jump melonia_button_common.choice


label melonia_button_common.naked:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Kenapa kamu telanjang?"


    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia b_naked a_idle f_smirk with dissolve

    melonia "Kenapa tidak?"

    show anon f_flirt_low
    melonia "Ini rumahku sekarang dan aku akan melakukan apa yang aku suka."

    pause
    melonia "Saya pikir pertanyaan yang lebih baik adalah..."

    melonia "... Kenapa kamu masih memakai pakaian?"

    jump melonia_button_common.choice


label melonia_button_common.wife:
    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon @ f_skeptical "Bagaimana rasanya menjadi istri walikota?"


    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal

    melonia "Ugh, ini serangan kebosanan yang menghancurkan jiwa tanpa henti."

    anon "B-benarkah?"

    melonia "Sebagian besar waktuku dihabiskan untuk memainkan peran sebagai orang yang menarik perhatian dan membiarkan orang-orang geriatri melirikku dengan imbalan dana kampanye..."

    anon "Jadi, itu menyebalkan?"

    melonia @ f_eyeroll "Yah, tidak semuanya..."

    melonia "Aku punya pelayan yang menungguku dua puluh empat jam sehari dan terus-menerus mencium pantatku."

    anon @ -m_talk "..."

    if venue == 'hottub':
        show melonia f_smirk_up
    else:
        show melonia f_smirk

    melonia "Cukup menyenangkan memesannya."

    pause
    melonia "Apa yang kamu katakan, {b}Hector{/b}?"

    melonia "Apakah kamu ingin aku... Memerintahkanmu berkeliling?"


    if venue == 'hottub':
        show anon f_surprised_low
    else:
        show anon f_surprised

    anon "{i}*Gulp*{/i} Y-ya, mungkin..."

    melonia @ f_laugh "Ha ha ha!"

    jump melonia_button_common.choice


label melonia_button_common.outro0:
    if venue == 'hottub':
        show anon f_normal_low
    else:
        show anon f_normal

    anon "Saya mungkin harus mulai bekerja."


    if venue == 'hottub':
        show melonia f_normal_up
    else:
        show melonia f_normal

    melonia "Jangan lupa kenakan seragammu."

    anon "Ya, Bu."

    hide anon with dissolve
    return


label melonia_button_common.outro1:
    if venue == 'hottub':
        show anon f_worried_low
    else:
        show anon f_worried

    anon "Mungkin nanti."


    if venue == 'hottub':
        melonia f_pouting_up "Hanya tarian cepat..?"

    else:
        melonia f_pouting "Tapi aku menginginkannya sekarang..."


    anon a_behind_head "Maaf."


    if venue == 'hottub':
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed

    melonia "Anda tidak serius mengatakan tidak, bukan?"

    anon "Aku ada urusan yang harus diselesaikan."

    pause

    if venue == 'hottub':
        show melonia f_yell
    else:
        show melonia f_yell a_fists with dissolve

    melonia "Uh, baiklah!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
