label scene_roxxy_boobjob:
    $ M_roxxy.set('sex speed', 1 / 8.)

    scene location_trailer_bedroom_sex_titjob
    show roxxy_sex_boobjob_insert as anim
    with fade
    show roxxy_sex_boobjob_base as anim
    show roxxy sex_boobjob
    with {'master': dissolve}

    anon "Man, you've got great tits!"

    roxxy "Aku tahu."

    show roxxy f_spit
    with {'master': dissolve}
    roxxy @ -m_talk "{i}*Mleh*{/i}"

    anon "Wah!"

    show roxxy -f_spit
    with {'master': dissolve}
    anon "Kamu luar biasa!"

    show roxxy f_laugh
    with {'master': dissolve}
    roxxy @ -m_talk "hehe!"

    show roxxy -f_laugh
    with {'master': dissolve}
    roxxy "Just lie back and relax, boo."

    roxxy "I'll take care of you."

    anon "Ini luar biasa!"

    hide roxxy
    show roxxy_boobjob as anim
    with {'master': dissolve}
    anon "Oh!"

    pause
    anon "Rasanya luar biasa!"

    roxxy "Ya?"

    anon "Oh ya!"

    pause
    anon "Does it feel good for you?"

    roxxy "It feels good to know I'm making you feel good."

    anon "Oh, you are!"

    anon "You really, {i}really{/i} are!"

    pause
    roxxy "C'mon, {b}[firstname]{/b}... Talk to me!"

    anon "Alright, umm..."

    anon "... H-how's things going with the cheer squad lately?"

    roxxy "No, not that!"

    roxxy "Talk dirty to me!!"

    anon "Oh!!"

    anon "Right, sorry..."

    pause
    roxxy "Tell me all the naughty things you wanna do to me!"

    anon "{i}*Ahem*{/i} {b}Roxxy{/b}, I wanna... uhh..."

    anon "L-love you... so hard."

    roxxy "..."
    anon "And I wanna roll around, on your..."

    anon "... Butt."

    roxxy "That's really not-"

    anon "And massage your umm..."

    anon "... Knees."

    roxxy "Oh my god, please stop talking."

    anon "Bad?"

    roxxy "So bad!"

    anon "Maaf!"

    pause
    anon "It's just hard to concentrate while you've got those phenomenal ta-tas wrapped around my cock!"

    roxxy "Oooh, yeah... Say more stuff like that!"

    anon "Ta-tas?"

    roxxy "You like my ta-tas, don't you?!"

    anon "I {i}love{/i} your ta-tas {b}Roxxy{/b}!"

    roxxy "Do you wanna suck 'em?"

    anon "If you want me to."

    roxxy "NO, {b}[firstname]{/b}... Tell me you wanna suck on them!"

    anon "Ah, god.. I wanna suck on your tits, {b}Roxxy{/b}!!"

    roxxy "What else?!"

    anon "I wanna squeeze them!"

    roxxy "Ya?"

    anon "And pinch your nipples!"

    roxxy "Terus berlanjut!"

    anon "And..."

    anon "... AND..."


    call scene_roxxy_boobjob.loop

    roxxy "And what?!"

    anon "... AND I'M CUMMING!!"

    pause
    show roxxy_sex_boobjob_cum as anim
    show roxxy_sex_boobjob_cumshot as cum
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."

    hide cum
    show roxxy_sex_boobjob_base as anim
    show roxxy sex_boobjob o_cum
    with {'master': dissolve}
    roxxy "Heh, wow..."

    roxxy "... You drenched me!"

    show roxxy f_lick
    with {'master': dissolve}
    anon "Y-yeah, sorry... about that."

    show roxxy -f_lick
    with {'master': dissolve}
    roxxy @ -m_talk "Mmm. {i}*Smack*{/i}"

    anon "!!!"
    roxxy "That's alright, babe."

    roxxy "I liked it."

    anon "Ya?"

    roxxy "Oh ya!"

    pause
    roxxy "Hand me one of those dirty shirts would ya?"

    anon "Tentu saja."

    return


label scene_roxxy_boobjob.loop:
    call screen scene_roxxy_boobjob_controls

    if _return:
        return _return

    python hide:
        blocks = 4
        limit = 2

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_roxxy_boobjob.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_roxxy_boobjob.loop


label scene_roxxy_boobjob.dialogue(opt, rng=-1):

    if opt == 1:
        anon "I wanna suck them..."

        anon "... And squeeze them..."

        anon "... And nibble at your perky little nipples."

        roxxy "Ah, fuck ya!"

        roxxy "Terus berlanjut!"


    elif opt == 2:
        anon "I wanna throw you down on this bed and ravage your tight little pussy."

        roxxy "Hmm, Tuhan."


    elif opt == 3:
        anon "I wanna fuck you so hard and deep that you'll be begging me to stop and keep going at the same time."

        roxxy "Sial!"


    return


label scene_roxxy_boobjob.repeat:
    $ M_roxxy.set('sex speed', 1 / 8.)

    scene location_trailer_bedroom_sex_titjob
    show roxxy_sex_boobjob_insert as anim
    with fade
    show roxxy_sex_boobjob_base as anim
    show roxxy sex_boobjob
    with {'master': dissolve}

    anon "Man, I love your tits!"

    roxxy "Aku tahu."

    show roxxy f_spit
    with {'master': dissolve}
    roxxy @ -m_talk "{i}*Mleh*{/i}"

    pause
    show roxxy -f_spit
    with {'master': dissolve}
    anon "I will never get tired of watching you do that."

    show roxxy f_laugh
    with {'master': dissolve}
    roxxy @ -m_talk "hehe!"

    show roxxy -f_laugh
    with {'master': dissolve}
    roxxy "And I'll never get tired of pleasing my man..."

    roxxy "... Now lie back and relax, boo."

    anon "You are so freaking sexy, {b}Roxxy{/b}!"

    hide roxxy
    show roxxy_boobjob as anim
    with {'master': dissolve}
    anon "Oh, baby... just like that."

    roxxy "Ya?"

    anon "Ya!"

    pause
    anon "Work those big titties for me, {b}Roxxy{/b}."

    roxxy "Mmm, yeah."

    pause
    roxxy "You like my big titties, don't you?!"

    anon "I {i}love{/i} your titties {b}Roxxy{/b}!"

    roxxy "Do you wanna suck 'em?"

    anon "Saya bersedia."

    pause
    call scene_roxxy_boobjob.dialogue (1)
    pause
    call scene_roxxy_boobjob.dialogue (2)
    pause
    call scene_roxxy_boobjob.dialogue (3)
    pause
    anon "I wanna..."

    anon "... I WANNA...."


    call scene_roxxy_boobjob.loop

    roxxy "You wanna what?!"

    anon "... I WANNA CUM!!"

    pause
    show roxxy_sex_boobjob_cum as anim
    show roxxy_sex_boobjob_cumshot as cum
    anon "HNNGGG!!!" with flash
    pause
    anon "Haah... Haah..."

    hide cum
    show roxxy_sex_boobjob_base as anim
    show roxxy sex_boobjob o_cum
    with {'master': dissolve}
    roxxy "Heh, geez..."

    roxxy "... Always so much!"

    show roxxy f_lick
    with {'master': dissolve}
    anon "Y-yeah, sorry... about that."

    show roxxy -f_lick
    with {'master': dissolve}
    roxxy @ -m_talk "Mmm. {i}*Smack*{/i}"

    anon "!!!"
    roxxy "That's alright, babe."

    roxxy "That was hot as fuck!"

    anon "Ya?"

    roxxy "Oh ya!"

    pause
    roxxy "Hand me one of those dirty shirts would ya?"

    anon "Tentu saja."

    return


label scene_roxxy_boobjob.first:
    jump scene_roxxy_boobjob


label scene_roxxy_boobjob.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['Roxxy']['variants']['09_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_trailer_bedroom) with fade
        menu:
            "Pertama" if 'first' in variants:
                jump scene_roxxy_boobjob.first

            "Ulangi" if 'repeat' in variants:
                jump scene_roxxy_boobjob.repeat

    jump expression 'scene_roxxy_boobjob.{}'.format(next(iter(variants)))

    return



screen scene_roxxy_boobjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return()

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_roxxy.set, 'sex speed',
                                 1 / (1 / M_roxxy.get('sex speed') - 2)),
                        Return(False))
                sensitive M_roxxy.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_roxxy.set, 'sex speed',
                                 1 / (1 / M_roxxy.get('sex speed') + 2)),
                        Return(False))
                sensitive M_roxxy.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
