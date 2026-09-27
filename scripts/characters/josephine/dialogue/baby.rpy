label josie_button_baby:
    show anon with dissolve
    anon "Hai, kalian berdua."

    josephine @ -m_talk "..."
    if M_josie.pregnancy.baby_gender == 'boy':
        anon "Bagaimana kabar si kecilku?"

    else:
        anon "Bagaimana kabar gadis kecilku?"

    pause
    anon f_worried "Halo?"

    josephine @ -m_talk "..."
    anon f_sad_down "Dengan serius?!"

    josephine f_normal @ -m_talk "Hmm?"

    josephine "Oh, hai {b}[firstname]{/b}!"

    josephine "Apa yang terjadi?"


    menu josie_button_baby.choice:
        "Bayinya benar-benar mirip denganmu, ya?":

            jump josie_button_baby.phone
        "Kalian butuh sesuatu?":

            jump josie_button_baby.need
        "Aku akan meninggalkanmu.":

            pass

    anon f_normal @ a_wave "Aku akan meninggalkanmu."

    show josephine f_normal_down
    if M_josie.pregnancy.baby_gender == 'boy':
        anon "Jangan biarkan dia menatap benda itu terlalu lama."

        anon "Itu akan merusak otaknya."

    else:
        anon "Jangan biarkan dia menatap benda itu terlalu lama."

        anon "Itu akan merusak otaknya."

    josephine @ -m_talk "Mhmm."

    hide anon with dissolve
    return


label josie_button_baby.need:
    anon f_normal "Kalian butuh sesuatu?"

    josephine f_normal "Kamu jago dalam Candy Smash?"

    anon f_worried @ f_confused "Aku bahkan tidak tahu apa itu..."

    josephine f_normal_down "Ya, saya pikir."

    pause
    josephine "Kami baik-baik saja, terima kasih."

    jump josie_button_baby.choice


label josie_button_baby.phone:
    anon f_normal "Bayinya benar-benar mirip denganmu, ya?"

    josephine f_normal_down @ f_eyeroll "Duh."

    pause
    josephine "Anda harus bersyukur."

    josephine "Saya tidak tahu apakah Anda mengetahui hal ini, tetapi saya adalah orang paling keren yang Anda kenal."

    anon @ f_laugh "Heh, ya... Oke."

    josephine @ f_laugh "hehe!"

    jump josie_button_baby.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
