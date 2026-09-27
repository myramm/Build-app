label tattoo_parlor_fireescape_eve_visit_roof:
    scene expression player.location.background_blur with None
    show tuuku a_sides with None:
        xoffset 100
    show anon
    show eve:
        flip
        xoffset 300
    with dissolve
    pause
    tuuku "Hey there, {b}Evie{/b}."

    eve f_disgusted "{b}Tuuku{/b}?"

    eve "Apa yang kamu lakukan di sini?"

    show tuuku a_thumb f_happy with dissolve
    tuuku "I was watering my babies before work."

    show tuuku a_sides with dissolve
    eve f_nervous "Oh."

    pause
    eve f_wink "You think you could hook us up with some?"

    show eve f_nervous
    show anon f_thinking
    tuuku f_nervous "Ehh, I don't think {b}Grace{/b} would like that..."

    eve f_happy "Hey, what she doesn't know, won't hurt her!"

    show anon f_worried
    tuuku f_laugh "Hah, yeah right!"

    tuuku f_happy "More like, what she doesn't know will get my ass kicked!"

    eve f_nervous "C'mon, pleeeeease?"

    show tuuku f_annoyed a_hips with dissolve
    tuuku "Mustahil."

    eve f_pouting "Lame!"

    tuuku "You'll just have to make due with your own stash."

    eve f_disgusted "Eugh, all I have left is dirtbud, man."

    eve "That shit's not even worth smoking..."

    tuuku "Can't help ya, kiddo."

    tuuku "Maaf."

    hide tuuku with dissolve
    show eve a_rossed f_nervous_down with dissolve
    eve "Tsk, damn it..."

    pause
    anon "What was that about?"

    hide eve
    show eve a_sides f_nervous with dissolve
    eve @ -m_talk "Hmm?"

    eve "Oh, don't worry about it."

    show eve f_happy a_hip with dissolve
    show anon f_normal
    pause
    eve "C'mon, I'll show you the rest of the house."

    hide eve
    hide anon
    with dissolve
    return


label tattoo_parlor_fire_escape_party_up_to_roof:
    scene expression player.location.background_blur with None
    show anon f_surprised with dissolve
    anon @ -m_talk "( Sheesh, there are people everywhere! )"

    anon f_normal @ -m_talk "( {b}Odette must be up near Tuuku's tent{/b}. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
