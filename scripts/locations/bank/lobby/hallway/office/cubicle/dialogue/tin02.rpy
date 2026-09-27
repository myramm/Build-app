label tin02_talk_bank_cubicle:
    scene expression background(712, 400, 2.5) as stage
    show tina o_glasses:
        flip
        xoffset 790
    show anon with dissolve
    anon "Halo?"

    show tina with {'master': dissolve}:
        unflip
        xoffset 0
    tina @ -m_talk "Hmm?"

    tina @ f_laugh "Oh, hey babyface!"

    show tina b_dressed_hug_anon f_sexy o_empty
    show anon b_empty f_shy
    with dissolve
    tina "It's good to see you."

    anon "Y-ya, kamu juga."

    pause
    show anon b_dressed
    show tina b_dressed f_sad o_glasses
    with dissolve
    tina "Sorry again about the other night..."

    anon f_confused "The other night?"

    tina "Yeah, you know... When my daughter and her little friend caught us kissing in my doorway."

    anon f_normal "Oh benar."

    anon "It's no problem, really."

    tina f_sexy "I'll make sure that doesn't happen next time."

    anon "Lain kali?"

    tina "Well, yeah."

    tina f_suspicious "Isn't that why you're here?"

    anon f_shy "Ya, saya kira."

    tina f_sexy "Are you free tonight?"


    menu:
        "Yes":
            jump tin02_talk_bank_cubicle.schedule
        "No":

            pass

    anon f_worried "Tidak."

    tina f_sad "Oh."

    tina f_normal "Well, that's alright."

    show anon f_shy
    pause
    tina "Now that you know where I work, you can swing by next time you have a free evening."

    tina "We'll set something up then."

    anon "Ya baiklah."

    tina "Did you need anything else?"

    return


label tin02_talk_bank_cubicle.schedule:
    anon f_flirt "Ya."

    tina f_sexy "Luar biasa!"

    tina "Aku akan mengirim {b}Becca{/b} ke rumah temannya dan kita akan menghabiskan malam itu sendirian."

    anon "Saya suka suaranya."

    tina "Mmm, you'd better bring your A game this time!"

    anon f_shy "{i}*Gulp*{/i} Y-ya, oke."

    tina f_normal "Did you need anything else?"

    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
