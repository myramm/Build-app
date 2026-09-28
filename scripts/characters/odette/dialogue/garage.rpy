label odette_repeat_sex_couch:
    anon "On the couch. Naked."
    odette f_pouting "Hmm, that's kind of boring, isn't it?"
    show anon f_worried

    if M_odette.once('couch_sex') and not M_odette.once('couch_anal'):
        jump odette_repeat_sex_couch.second

    jump odette_repeat_sex_couch.repeat


label odette_repeat_sex_couch.repeat:
    pause
    odette f_normal "Oh, alright."
    show anon f_normal
    odette f_smirk "I suppose I can't blame you for wanting to see the twins bounce around."
    anon f_confused "The twins?"
    show odette b_skirt f_happy_down a_remove1
    with dissolve
    pause
    show anon f_flirt_low
    show odette b_skirtblank a_remove2
    with dissolve
    pause
    show odette a_remove3
    with dissolve
    show odette a_remove4
    with dissolve
    show odette f_smirk b_skirt a_reveal
    with {'master': dissolve}
    odette "Ta-da!!"
    anon f_flirt "Oh, right."
    show anon f_flirt_low
    show odette f_happy_down a_remove5
    with dissolve
    pause
    show odette b_remove6
    with dissolve
    pause
    show odette a_hips b_panties f_smirk
    with {'master': dissolve}
    anon f_happy "Geez, your body is ridiculous!"
    odette f_shy "Heh, thanks."
    show anon f_shy_low
    show odette b_remove7 f_happy_down
    with dissolve
    pause
    show anon f_shy
    show odette b_naked f_smirk
    with {'master': dissolve}
    odette "Now, c'mon big fella..."
    hide odette
    with {'master': dissolve}
    odette "... My pussy is yearning for a churning!"
    anon f_confused "Yearning for what now?!"
    odette "Get over here and fuck me!"
    hide anon
    with {'master': dissolve}
    anon "Yes, ma'am."

    call scene_odette_couch_back.repeat (M_odette.get('couch_anal', False))
    $ unlock_scene('Odette', '06_unlocked', variant='back')

    if 'anal' in _return:
        jump odette_repeat_sex_couch.recovery

    scene expression background(l=L_tattooparlor_garage) as stage
    show odette a_grab_top b_wakeup f_tired_down:
        xoffset 100
        xzoom -1
    show anon b_dressed_changing at flip
    with fade
    pause
    show odette a_pull_top
    show anon a_sides b_dressed
    with {'master': dissolve}
    pause
    show odette a_sides b_dressed f_surprised
    with {'master': dissolve}
    odette @ -m_talk "!!!"
    show anon f_surprised
    odette "Holy shit, is it that late already?!"
    odette f_sad "I gotta get to the shop or {b}Grace{/b} is gonna kill me!"
    show anon f_worried
    anon "Yeah, alright."
    anon "See you later?"
    show anon f_normal
    odette f_smirk "Later, big fella."
    show odette a_kiss f_kiss
    with {'master': dissolve}
    odette @ -m_talk "Muah!"
    hide odette
    show anon a_wave f_flirt_grin
    with {'master': dissolve}
    odette "Tell {b}Evie{/b} I said hello!!"
    anon f_happy "Will do!"
    hide anon with dissolve
    return 'afterglow'


label odette_repeat_sex_couch.second:
    pause
    show odette f_thinking
    pause
    show anon f_confused
    odette f_smirk "Or maybe not!"
    show anon f_surprised
    odette "You wanna stick that big thing in my ass?"
    show anon f_brag
    anon "I mean, if you think you can handle it?"
    odette f_smirk_lip_down @ -m_talk "Hmm."
    pause
    odette f_smirk "Well, there's only one way to find out!"
    show odette b_skirt f_happy_down a_remove1
    with dissolve
    pause
    show anon f_flirt_low
    show odette b_skirtblank a_remove2
    with dissolve
    pause
    show odette a_remove3
    with dissolve
    show odette a_remove4
    with dissolve
    show anon f_flirt
    show odette f_normal b_skirt a_hips
    with {'master': dissolve}
    anon "Is that a yes?"
    odette f_smirk "It's a tentative yes..."
    odette "... Just, go slow at first, yeah?"
    odette "It's been a while."
    show anon f_flirt_low
    show odette f_happy_down a_remove5
    with dissolve
    pause
    show odette b_remove6
    with dissolve
    pause
    show odette a_hips b_panties f_smirk
    with {'master': dissolve}
    anon f_shy "Slow, right."
    anon f_brag "Yeah, I can do that."
    show anon f_shy_low
    show odette b_remove7 f_happy_down
    with dissolve
    pause
    show anon f_brag
    show odette b_naked f_smirk
    with {'master': dissolve}
    odette "C'mon then!"
    hide odette
    with {'master': dissolve}
    anon f_happy "Awesome."

    call scene_odette_couch_anal
    $ unlock_scene('Odette', '06_unlocked', variant='anal')

    label odette_repeat_sex_couch.recovery:
    scene expression background(l=L_tattooparlor_garage) as stage
    show odette a_grab_top b_wakeup f_tired_down:
        xoffset 100
        xzoom -1
    show anon b_dressed_changing at flip
    with fade
    pause
    show odette a_pull_top
    show anon a_sides b_dressed
    with {'master': dissolve}
    pause
    show odette a_butthurt b_dressed f_pouting_right
    with {'master': dissolve}
    odette "Geez, I'm gonna be walking funny for the rest of the day..."
    anon f_confused "Yeah?"
    show odette a_hips f_pouting
    with {'master': dissolve}
    odette "... You really did a number on me."
    anon f_worried "You think {b}Grace{/b} will notice?"
    odette f_smirk "Oh, don't worry."
    odette "I'll just tell her I went too hard with one of my toys."
    anon f_brag "Do that often, do you?"
    odette @ f_wink "Occasionally."
    pause
    odette "Hehe, later, big fella."
    show odette a_kiss f_kiss
    with {'master': dissolve}
    odette @ -m_talk "Muah!"
    hide odette
    show anon a_wave f_happy
    with {'master': dissolve}
    anon "Later, {b}Odette{/b}."
    return 'afterglow'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
