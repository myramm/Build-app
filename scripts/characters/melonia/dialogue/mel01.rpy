label mel01_init_melonia:
    show melonia f_disgusted_down:
        flip
        xoffset 350
    show anon f_worried with dissolve:
        xoffset -100
    melonia "Eugh, bak mandi air panas ini menjijikkan!"

    melonia "Apa yang sedang dilakukan anak biliar baru itu?!"

    show melonia f_annoyed with dissolve:
        unflip
        xoffset -250
    pause
    melonia "Itu dia!"

    anon "Ehh."

    melonia @ a_point_back "Mau menjelaskan mengapa bak mandi air panas saya belum dibersihkan?!"

    anon a_behind_head "aku um-"

    melonia f_confused "Dan di mana seragammu?!"

    anon "Ehh."

    anon "Apakah seragam itu memang diperlukan, Bu?"

    melonia f_annoyed "Tentu saja itu perlu!"

    anon a_sides "Aku agak tidak nyaman-"

    melonia "Jangan tanya aku, {b}Hector{/b}!"

    melonia "Anda akan pergi dan berbicara dengan {b}Ricky{/b} tentang hal itu begitu Anda selesai membersihkan!"

    anon "Bagaimana jika, sebaliknya-"

    melonia a_crossed @ f_yell "Tidak satu kata lagi, {b}Hector{/b}!"

    anon f_sad_down @ -m_talk "..."
    melonia a_point_back "Saya ingin bak mandi air panas ini digosok dan disaring sekarang juga!"

    melonia a_point_down "Dan besok pagi, Anda AKAN tiba di sini tepat waktu dan mengenakan seragam yang pantas..."

    melonia a_idle "... Apakah ada pemahaman di antara kita?!"

    anon "{i}*Huh*{/i} Y-iya, Bu."

    show melonia a_crossed with dissolve
    pause
    melonia "Aku sadar ini hari pertamamu, namun aku mengharapkan yang lebih baik darimu, {b}Hector{/b}."

    anon @ -m_talk "..."
    show anon f_surprised
    melonia "Sekarang selesaikan!"

    hide melonia
    show anon:
        flip
        xoffset -600
    with dissolve
    pause
    anon f_worried @ -m_talk "(Yah, itu bukanlah awal yang baik.)"

    pause
    show anon f_worried_low with dissolve:
        unflip
        xoffset 200
    anon @ -m_talk "(Saya tidak tahu cara membersihkan bak mandi air panas...)"

    anon @ -m_talk "( ... Saya harus {b}berbicara dengan Ricky{/b} dan melihat apakah dia dapat membantu saya. )"

    hide anon with dissolve
    return


label mel01_more_melonia:
    scene expression background(768, 368, 4.) as stage
    show location_rump_backyard_jacuzzi_overlay as hottubback:
        yoffset 140
    show melonia b_jacuzzi:
        yoffset 155
    show location_rump_backyard_jacuzzi_overlay as hottub:
        yoffset 155
    show anon f_worried_low with dissolve
    melonia "{b}Hektor{/b}?"

    melonia f_annoyed "Apa yang masih kamu lakukan di sini?"

    anon "Hanya memeriksa untuk melihat apakah Anda memerlukan sesuatu."

    melonia "Saya baik-baik saja."

    melonia f_normal "{b}Ricky{/b} memenuhi kebutuhan saya."

    anon "B-benar, oke."

    melonia f_annoyed "Pulanglah hari ini, aku sudah selesai denganmu."

    anon f_sad_down a_sides "Tentu saja, Bu."

    melonia "Dan pastikan bak mandi air panas ini tetap bersih!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
