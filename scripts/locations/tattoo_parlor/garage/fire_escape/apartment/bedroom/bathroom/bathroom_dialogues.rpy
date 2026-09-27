label tattoo_parlor_bathroom_eve_bathroom_break:
    scene expression "backgrounds/location_tattoo_bathroom_cutscene01.jpg" with fade
    anon "!!!" with hpunch
    eve "{b}[firstname]{/b}?!"

    $ player.go_to(L_tattooparlor_bathroom)
    scene expression player.location.background_blur
    show anon f_surprised o_boner a_surprised_up_both
    show eve b_undies_surprised
    with fade
    eve "Whoa, don't look!!"

    show eve f_nervous_down b_undies a_towel with dissolve
    anon a_cover_boner3 f_worried "Oh, sial... maafkan aku!"

    anon "I was just... I..."

    pause
    eve "Apa yang kamu lakukan di sini?!"

    eve "You didn't see anything, did you?!"

    anon f_worried "A-apa?!"

    anon "N-no, I didn't see-"

    eve "K-kamu yakin?"

    anon "Err, well... I mean, I saw a little bit but..."

    anon "Nothing bad... Err, I mean... Y-you look really good... I-"

    show eve f_surprised
    anon "I'm so sorry!!"

    eve "A-are you..."

    pause
    eve "Is that your dick?!"

    anon @ f_surprised_teeth "!!!"
    show anon a_cover_boner2
    show expression "characters/anon/anon_arms_dressed_a_cover_boner2.png"
    with dissolve
    anon f_shock "N-no, it's not-"

    eve "A-are you hard?"

    anon f_surprised_teeth @ f_worried "Uhh, I..."

    eve "Because of me?!"

    anon f_surprised_teeth @ f_surprised "I'm just gonna head home, okay?"

    eve "Head home?"

    eve "Apakah kamu baik-baik saja?"

    anon f_surprised "Y-yeah, everything is fine!"

    anon f_surprised_teeth @ f_surprised "I just... I'm embarrassed, I didn't mean to walk in on you."

    eve f_nervous_down "I-it's alright, {b}[firstname]{/b}-"

    anon f_surprised_teeth @ f_surprised "I'll see you tomorrow at school, yeah?"

    eve @ f_nervous "O-oke..."

    anon f_surprised_teeth @ f_surprised "Sampai jumpa."

    $ player.go_to(L_tattooparlor_bedroom)
    scene expression player.location.background_blur
    show anon f_sad_down o_boner with dissolve
    anon "( Holy crap, could this get any more embarrassing?! )"

    anon "( I've just gotta get out of here... )"

    hide anon with dissolve
    return

label tattoo_parlor_bathroom_pantie_collection:
    scene expression player.location.background_blur with None
    if player.location.is_here(M_eve) or (player.location.is_here(M_grace) and not M_eve.pregnancy.character_bedridden) or player.location.is_here(M_odette):
        show anon f_surprised with dissolve
        anon @ -m_talk "( Don't want to get caught, they can stay there for now. )"

    else:
        show anon f_shy_down a_panties_grace1 with dissolve
        anon @ -m_talk "( These are {b}Grace{/b}'s panties. )"

        anon @ -m_talk "( They're a lot simpler than I'd imagined... )"

        pause
        if M_somrak.finished_state(S_somrak_start):
            anon f_grin "( I bet {b}Master Somrak{/b} would like these. )"

            $ player.get_item("grace_panties")
        else:
            anon f_shy_down @ -m_talk "( I'll put them back like I was never here. )"

        hide anon with dissolve
    $ game.main()
    return

label tattoo_parlor_bathroom_eve_shower:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show eve b_naked_pregnant_belly f_happy a_towel_back
    show anon f_flirt with dissolve
    anon "Whatcha doing?"

    eve "Heh, showering..."

    eve "Apa yang sedang kamu lakukan?"

    anon "Oh, just trying to sneak a peek of that sexy bod you got."

    eve @ f_eyeroll "Oh, please... I'm a big fat cow."

    anon "No you're not!"

    anon "I think you look beautiful."

    eve "Anda melakukannya?"

    anon "Tentu saja."

    anon "You always look beautiful."

    pause
    anon "C'mon, just give me a little peek?"

    eve "Hehe, you really wanna see?"

    anon "I really wanna see."

    eve "{i}*Sigh*{/i} Alright, but only because I love you."

    show eve a_remove1 with dissolve
    pause
    show eve a_remove2 with dissolve
    pause
    anon "Wow, that's sexy!"

    show eve a_remove1 with dissolve
    eve @ f_laugh "Hehehe!"

    show eve a_towel_back with dissolve
    pause
    hide anon with dissolve
    return

label tattoo_parlor_bathroom_grace_shower:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show grace b_naked_pregnant_belly a_cover f_sad
    show anon f_flirt with dissolve
    grace "{b}[firstname]{/b}?!"

    anon "Oh sial."

    anon "Sorry, I didn't know you were in here..."

    anon "I just thought someone forgot to shut the light off."

    grace "No, it's alright... You just scared me, is all."

    pause
    anon "Wow, you look amazing!"

    grace f_sad_down a_shy "Saya bersedia?"

    anon "Yeah, that baby bump is so sexy!"

    grace f_sexy "Oh, kamu menyukainya, ya?"

    anon "I like it a lot!"

    grace a_idle "You better get a good look then, 'cause I won't have it very long."

    anon "Mmm, I could stare at this all day."

    grace @ f_laugh "Hehehe!"

    pause
    hide anon with dissolve
    return

label tattoo_parlor_bathroom_odette_shower:
    scene expression background(544, 288, 2.) as stage at flip
    show layer master at flip
    show odette f_smirk b_naked_pregnant_belly a_towel
    show anon f_flirt with dissolve
    odette "You lost, big fella?"

    anon "T-tidak."

    anon "Sorry, I didn't know you were in here..."

    anon "I just thought someone forgot to shut the light off."

    odette "Mmhmm, likely excuse."

    odette "You sure you're not spying on me?"

    anon "aku tidak-"

    odette "Because you're more than welcome to watch, if you want?"

    anon @ -m_talk "Hmm?"

    show odette a_remove1 with dissolve
    pause
    show odette a_remove2
    anon f_shock "!!!" with hpunch
    odette a_squeeze "kamu suka?"

    pause
    anon f_flirt "Y-ya."

    show odette a_touch with dissolve
    odette @ f_laugh "Hehehe!"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
