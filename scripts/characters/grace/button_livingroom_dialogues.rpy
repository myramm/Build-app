label button_grace_livingroom_no_thanks:
    anon "That's probably not a good idea."
    grace f_normal @ f_surprised "I agree!"
    odette f_tired "Tch, you two are no fun..."
    pause
    anon f_normal "Is {b}Eve{/b} here?"
    grace "Yeah, she's in her room, {b}[firstname]{/b}."
    anon @ f_laugh "Thanks!"
    odette f_smirk "You know, she's probably really busy in there..."
    odette "I don't think she'd mind if you stayed and watched us for a bit."
    grace f_angry_back "{b}Odette{/b}!"
    odette "What?!"
    odette "It wouldn't hurt to watch!"
    grace "Leave my sister's boyfriend alone!"
    odette @ f_eyeroll "Ugh, fine."
    return

label button_grace_livingroom_odette_no:
    anon f_worried "I was just curious how things are going with you and {b}Grace{/b}?"
    odette f_angry @ -m_talk "..."
    odette "You're serious?"
    anon @ a_behind_head "Yeah?"
    pause
    odette @ f_eyeroll "Well, they were going a lot better before you interrupted us!"
    odette "I was rounding second and now I'll have to warm her up again!"
    anon f_sad_down "I'm sorry, I-"
    odette "Tch, I thought you were gonna give me some of that sweet, sweet, dick I've been craving!"
    anon @ -m_talk "..."
    odette @ f_eyeroll "Ugh, just forget it."
    hide odette with dissolve
    pause
    anon f_tired "Oops."
    hide anon with dissolve
    return

label button_grace_livinroom_odette_yeah:
    anon f_flirt "Y-yeah."
    odette "Oh, I'm always down for a romp with you, big fella!"
    odette @ f_laugh "Get that dick out and let's do this!"
    return

label button_grace_livingroom_speak_with_odette:
    anon f_worried "Actually, can I borrow {b}Odette{/b}?"
    show odette f_smirk
    grace f_suspicious "Borrow her?"
    anon "Yeah, I just need to ask her something."
    anon "It'll only take a minute."
    odette "Well, hopefully longer than a minute, big fella..."
    anon f_surprised @ -m_talk "!!!"
    grace f_tired_back "What does that mean?"
    odette f_normal @ f_surprised -m_talk "Hmm?"
    odette "Oh, nothing at all."
    odette f_smirk "Let me put my clothes on and I'll meet you downstairs, okay?"
    anon f_flirt "Thanks."
    pause
    grace f_tired_back "Is something going on between you two, {b}Odette{/b}?"
    odette f_normal @ f_laugh "Oh, don't be silly!"
    odette "He probably just needs some advice or something."
    grace "What kind of advice could he possibly need from you?!"
    odette "Hmm, I dunno..."
    odette f_smirk "Maybe he wants to know how to make your sister writhe in the same ecstasy I give you..."
    grace f_surprised "Writhe?!"
    grace f_surprised_back "T-that's not- "
    odette @ f_laugh "Hahaha!"
    odette "Just relax, I'll be back before you know it."
    hide grace
    show odette b_massage_kiss
    with dissolve
    pause
    show grace b_massage_laying behind grace_sex_mc_foreground
    hide odette
    with dissolve
    grace f_normal_down "O-okay."
    $ player.go_to(L_tattooparlor_garage)
    scene expression player.location.background_blur
    show anon f_worried
    show odette f_smirk
    with fade
    pause
    odette @ a_point "Wanna fuck?"
    return

label button_grace_livinroom_yes_please:
    anon @ f_laugh a_point "Yes, please!"
    grace f_sad "Uhh, I'm not so sure that's a good idea..."
    odette f_smirk "Oh, don't be silly!"
    odette "It's just a little harmless fun."
    grace f_sad_down "Y-yeah, but-"
    odette "Why don't you take those clothes off big fella and lay down right here."
    odette "I'm sure {b}Grace{/b} is eager to start."
    grace @ -m_talk "{i}*Gulp*{/i}"
    odette @ f_laugh "Hehe!"
    return

label button_grace_livingroom_intro:
    scene location_tattoo_apartment_oil
    show odette b_massage_leaning
    show grace b_massage_laying
    show odette_arms_massage_leaning_a_rub1_2
    show grace_sex_mc_foreground
    with dissolve
    anon "Hello, ladies."
    show odette f_smirk
    grace f_surprised "!!!"
    odette "Look {b}Grace{/b}, {b}[firstname]{/b} is here!"
    show odette b_massage
    hide odette_arms_massage_leaning_a_rub1_2
    show grace b_massage f_sad a_cover
    with dissolve
    grace "H-hi {b}[firstname]{/b}..."
    odette @ f_laugh "Isn't she adorable when she's being shy?"
    grace f_angry_back "I'm not-"
    odette "You don't have to cover up, silly... he's seen everything already."
    grace f_sad @ -m_talk "..."
    odette "I swear, you're more repressed than your little sister!"
    odette @ f_laugh "Hahaha!"
    pause
    odette "You wanna join us?"
    return

label button_grace_livingroom_intro_no_threesome:
    scene location_tattoo_apartment_oil
    show grace b_massage_odette
    show grace_sex_mc_foreground
    with dissolve
    anon "Oh, crap!"
    show grace b_massage f_surprised a_surprised
    show odette b_massage_laying_back behind grace_sex_mc_foreground
    with dissolve
    grace "!!!"
    show grace a_cover with dissolve
    anon f_worried "I'm sorry, I didn't mean to-"
    odette "Hey, why'd you stop?!"
    show odette b_situp f_smirk
    with dissolve
    odette "Mmm, hello {b}[firstname]{/b}."
    grace f_angry_back "{b}Odette{/b}, cover up!"
    odette "Oh, don't be silly... he's a grown man."
    if randomizer() > 50:
        show odette a_pussy
    else:
        show odette a_squeeze
    with dissolve
    odette "Besides, I've got nothing to be ashamed of... do I big fella?"
    show grace f_tired
    anon @ -m_talk a_behind_head "{i}*Gulp*{/i}"
    anon "I was just-"
    anon "Umm."
    grace "{b}Eve{/b}'s in her bedroom."
    anon f_surprised "Y-yeah, that!"
    anon f_normal "Thanks!"
    odette a_idle "Care to join us, {b}[firstname]{/b}?"
    grace f_surprised_back "{b}Odette{/b}, that's my sister's boyfriend!"
    odette "So?"
    odette "Maybe your sister would like to join us too, you ever think of that?"
    grace f_tired @ f_disgusted "Don't be gross."
    odette @ f_eyeroll "You two are so repressed."
    show odette b_massage_laying_back f_normal with dissolve
    odette "You'd better leave, {b}[firstname]{/b} before the prude gets too uncomfortable..."
    grace "I'm not a prude!"
    grace "I just don't want you corrupting my sister!"
    odette "Yeah, right."
    anon f_flirt_grin @ -m_talk "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
