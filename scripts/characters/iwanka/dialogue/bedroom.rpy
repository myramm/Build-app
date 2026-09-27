label iwanka_button_bedroom:
    show iwanka f_excited
    show anon with dissolve
    iwanka "Ya ampun!!"

    hide anon
    show iwanka b_dressed_kiss:
        xoffset -200
    with dissolve
    anon "!!!"
    show anon
    show iwanka b_dressed:
        xoffset 0
    with dissolve
    anon "Wah, oke."

    iwanka "Saya sangat senang Anda ada di sini!"

    iwanka "Terjebak di rumah ini adalah hal terburuk!"

    anon @ -m_talk "..."
    iwanka "Jadi apa yang terjadi?"


    menu iwanka_button_bedroom.choice:
        "{b}Consuela{/b}." if M_consuela.between_states(S_con01_init, S_con01_give) and not M_consuela.finished_state(S_con01_skip):
            jump con01_init_iwanka
        "Bekerja untuk ayahmu?":

            jump iwanka_button_bedroom.work
        "kapal pesiar":

            jump iwanka_button_bedroom.yacht
        "Seks oral.":

            jump iwanka_button_bedroom.blowjob

        "Seks." if M_iwanka.finished_state(S_iwa01_pier):
            jump iwanka_button_bedroom.sex
        "Saya harus pergi.":

            pass

    anon f_normal @ a_wave "Saya harus pergi."

    iwanka f_normal "Ya baiklah."

    iwanka f_smirk "Temui aku di kapal pesiar nanti dan kita akan berpesta, oke?"

    anon "Ya mungkin."

    iwanka @ f_laugh "Sampai jumpa, {b}[firstname]{/b}."

    hide anon with dissolve
    return


label iwanka_button_bedroom.blowjob:
    anon f_normal "Bolehkah memberiku pekerjaan pukulan?"

    iwanka f_smirk "Hehe, benarkah?"

    anon "Ya kenapa tidak?"

    iwanka "Umm, kamu sadar ayahku akan mengirimmu ke negara dunia ketiga jika dia menangkap kita, kan?"

    anon f_worried "Tunggu, apa?"

    iwanka "Ya."

    pause
    anon "Kamu serius?"

    iwanka "Sangat serius."

    iwanka "Dan itu setelah dia mengebirimu."

    anon f_surprised "!!!"
    iwanka @ -m_talk "Mhmm."

    show anon f_surprised_down
    pause
    iwanka "Anda masih menginginkan pekerjaan pukulan itu?"

    anon f_worried "saya-"

    anon f_shy a_behind_head "Umm, kamu tahu... Setelah dipikir-pikir lagi..."

    iwanka @ f_laugh "Haha!"

    iwanka "Menurutku tidak."

    show anon a_idle with dissolve
    jump iwanka_button_bedroom.choice


label iwanka_button_bedroom.sex:
    anon f_flirt "Ingin melakukannya?"

    iwanka f_smirk "Hehe, benarkah?"

    anon "Ya kenapa tidak?"

    iwanka f_excited "Umm, kamu sadar ayahku akan mengirimmu ke negara dunia ketiga jika dia menangkap kita, kan?"

    anon f_worried a_behind_head "Tunggu, apa?"

    iwanka f_smirk "Ya."

    show anon f_surprised_teeth
    pause
    anon f_worried "Kamu serius?"

    iwanka "Sangat serius."

    iwanka "Dan itu setelah dia mengebirimu."

    anon "!!!"
    iwanka @ -m_talk "Mhmm."

    pause
    iwanka "Anda masih menginginkan seks?"

    anon "saya-"

    anon "Umm, kamu tahu... Setelah dipikir-pikir lagi..."

    iwanka "Haha!"

    iwanka "Menurutku tidak."

    show anon a_idle with dissolve
    jump iwanka_button_bedroom.choice


label iwanka_button_bedroom.work:
    anon f_worried "Bukankah kamu seharusnya membantu ayahmu mengerjakan pekerjaannya?"

    iwanka f_normal "Tidak, aku sedang mogok kerja."

    anon "Memukul?"

    iwanka f_annoyed "Itu benar."

    iwanka "Saya menuntut jam kerja yang lebih pendek dan istirahat yang lebih lama!"

    iwanka @ a_finger "Saya ingin kantor saya sendiri dengan TV plasma dan salah satu kursi pijat!"

    anon @ -m_talk "..."
    iwanka "Tunjangan tambahan lima ribu dolar seminggu!"

    iwanka "Irisan lemon segar untuk air kemasan saya!"

    pause
    iwanka "Dan yang tak kalah pentingnya, saya ingin omong kosong tahanan rumah ini berakhir!"

    iwanka f_smirk "Kemudian, dan hanya setelah itu saya akan kembali bekerja."

    anon "Wow."

    anon @ a_behind_head "Hmm, oke."

    iwanka f_annoyed "Saya tidak akan diperlakukan seperti tahanan di rumah saya sendiri."

    iwanka @ a_finger "Ini adalah Amerika, bukan Tiongkok komunis!"

    jump iwanka_button_bedroom.choice


label iwanka_button_bedroom.yacht:
    anon f_normal "Setidaknya kamu masih bisa menyelinap ke kapal pesiar, bukan?"

    iwanka f_smirk "Ya, dan terima kasih Tuhan untuk itu!"

    iwanka "Saya akan memanjat tembok jika Anda tidak menunjukkan kepada saya cara melakukan itu."

    anon "Bukan apa-apa, aku hanya senang bisa membantu."

    iwanka "Tidak, aku berhutang banyak padamu."

    show iwanka a_touch_sexy:
        xoffset -200
    show anon f_shy behind iwanka
    with dissolve
    iwanka "Dan aku tak sabar untuk membalas budimu... Berkali-kali."

    anon "{i}*Gulp*{/i} Y-ya, aku juga menantikannya."

    show iwanka a_idle behind anon with dissolve:
        xoffset 0
    iwanka "Tapi tidak di sini."

    iwanka "Ayahku akan membunuhmu jika dia menangkap kami."

    jump iwanka_button_bedroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
