label melonia_button_baby(low=False):
    if low:
        show anon f_worried_low with dissolve
    else:
        show anon f_worried with dissolve
    anon "{b}Melonia{/b}?"

    melonia "Hai, {b}[firstname]{/b}."

    anon "Mengapa robot itu menggendong anak kita?"

    melonia "Maksudmu pembantunya?"

    anon "Ya, pelayan {i}robot{/i}."

    melonia "Tidak apa-apa, {b}[firstname]{/b}."


    menu melonia_button_baby.choice:
        "Ini tidak baik!":

            jump melonia_button_baby.thotbot
        "Lakukan pemanasan terhadap anak kita?":

            jump melonia_button_baby.effort
        "Nikmati waktu {i}saya{/i} Anda, saya rasa.":

            pass

    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "Nikmati waktu {i}saya{/i} Anda, saya rasa."

    if low:
        show melonia f_smirk_up
    else:
        show melonia f_smirk
    melonia "Oh, jangan terlalu murung."

    melonia "Saya akan kembali ke seratus persen sebelum Anda menyadarinya."

    anon "Maksudnya itu apa?"

    melonia "Artinya, sebaiknya Anda mengosongkan jadwal Anda."

    if low:
        show melonia f_relax
    else:
        show melonia f_smirk
    melonia "Karena kau berutang padaku orgasme yang luar biasa setelah semua barang bayi ini dan aku yakin akan menagihnya!"

    anon f_sad_down "{i}*Huh*{/i} Ya, oke."

    hide anon with dissolve
    return


label melonia_button_baby.effort:
    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "Anda setidaknya harus berusaha menjalin ikatan dengan anak kita."

    if low:
        show melonia f_relax
    else:
        show melonia f_normal
    anon "Oke, tapi kapan?"

    melonia "Ketika sudah tua..."

    melonia "... Dan tidak mudah mengotori dirinya sendiri."

    anon "{b}Melonia{/b}..."

    melonia "Mungkin kita akan beruntung dan yang ini akan meninggalkan sarangnya pada usia normal alih-alih mencemoohku seumur hidupnya..."

    melonia "...Seperti anak lain yang namanya tidak akan saya sebutkan."

    jump melonia_button_baby.choice


label melonia_button_baby.thotbot:
    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "Ini tidak baik!"

    anon "Aku tidak suka kamu meninggalkan bayi kita dengan benda itu."

    if low:
        show melonia f_relax
    else:
        show melonia f_normal
    melonia "Kenapa tidak?"

    melonia "Saya memasukkannya ke mode penitipan anak."

    anon "Karena itu-"

    if low:
        show anon f_surprised_low
    else:
        show anon f_surprised
    pause
    anon @ a_point_back "Tunggu, ada mode penitipan anak?"

    melonia "Tentu saja."

    show anon f_thinking
    pause
    if low:
        show anon f_worried_low
    else:
        show anon f_worried
    anon "Tidak, tidak... Aku masih tidak menyukainya."

    if low:
        show melonia f_annoyed_up
    else:
        show melonia f_annoyed
    melonia "Kalau begitu, tonton sendiri!"

    melonia "Saya menghabiskan sembilan bulan membawa benda itu dan sekarang saya ingin waktu {i}saya{/i}!"

    jump melonia_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
