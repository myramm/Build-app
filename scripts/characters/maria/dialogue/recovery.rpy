label maria_button_recovery:
    show tony b_casual behind maria:
        crop (0, 0, 1024, 650)
        flip
        xoffset 200
        zoom .9
    show anon with dissolve
    show tony with dissolve:
        unflip
        xoffset -100
    tony "Hey, champ."

    tony "Anda datang untuk memeriksa kami lagi?"


    menu:
        "Ya.":
            pass

    anon "Ya, bagaimana kabar kalian?"

    maria f_sad "I'm ready to get out of this hospital bed, I'll tell ya that!"

    maria "My back is killin' me!"

    tony "I keep tellin' the fuckin' nurse to bring more pillows, but she says they ain't got any extras..."

    maria f_annoyed "{b}Tony{/b}!!"

    show tony f_sad with dissolve:
        flip
        xoffset 200
    maria "How many times do I have to tell ya to watch your fuckin' mouth, eh?"

    tony "Sorry, darlin'."

    if M_maria.pregnancy.baby_gender == "twins":
        maria "I swear to god, our children's first words are gonna be cocksucker..."

    else:
        maria "I swear to god, our child's first word is gonna be cocksucker..."

    tony f_normal @ f_laugh a_belly "Haha!"

    anon @ -m_talk "..."
    tony "Just roll over on your side and I'll rub your back for ya, yeah?"

    maria @ f_eyeroll "Ugh, pass."

    tony "Aww, c'mon now, darlin'..."

    maria "No, your backrubs are the fuckin' worst!"

    tony @ -m_talk "..."
    maria "It's like you got orangutan hands or somethin'..."

    anon "I could try if you want?"

    tony "Ini dia."

    tony @ a_point_back "Let the kid give ya a backrub, if I'm so bad at it..."

    maria "No, I don't need no backrub."

    maria "I need to get outta this fuckin' hospital!"

    maria "Go talk to the nurse again, will ya?"

    tony @ a_calm_down "Alright, I'm goin'..."

    show tony with dissolve:
        unflip
        xoffset -100
    tony @ f_smirk_wink "You better get out of here while you can, champ."

    tony "Things are about to get ugly."

    anon "Y-ya, oke."

    anon "See ya, {b}Tony{/b}."

    anon "Bye, {b}Maria{/b}."

    tony "Nanti, juara."

    maria f_normal_down @ f_normal "See you soon, {b}[firstname]{/b}."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
