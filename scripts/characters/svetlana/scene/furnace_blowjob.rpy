label scene_svetlana_furnace_blowjob:
    $ M_svetlana.set('sex speed', 1 / 8.)

    call scene_svetlana_furnace_blowjob.stage
    with fade
    svetlana "Lovely." (show_native="Prekrasnyy.")
    pause
    show svetlana f_normal_back
    with {'master': dissolve}
    svetlana "This is a beautiful penis."
    anon "T-thanks."
    show anon f_surprised
    show svetlana a_rub f_normal
    with {'master': dissolve}
    anon "Haaah!"
    pause
    svetlana "It is rare to find one so tall but also so fat..."
    show anon f_confused
    with {'master': dissolve}
    anon "F-fat?"
    show svetlana f_sexy_back
    with {'master': dissolve}
    svetlana "Da, fat."
    show anon f_surprised
    show svetlana f_sexy
    with {'master': dissolve}
    pause
    svetlana "I bet it tastes of cheeseburgers and cola drinks."
    show anon f_nervous
    with {'master': dissolve}
    anon "Ehh, I dunno about tha-"
    call scene_svetlana_furnace_blowjob.insert
    with {'master': dissolve}
    anon "Ohhh, god!"
    call scene_svetlana_furnace_blowjob.animate
    with {'master': dissolve}
    call scene_svetlana_furnace_blowjob.dialogue (1)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (2)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (3)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (4)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (5)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (6)
    pause
    call scene_svetlana_furnace_blowjob.stage
    with {'master': dissolve}
    svetlana f_sexy @ -m_talk "Mmm."
    show svetlana f_sexy_back
    with {'master': dissolve}
    svetlana "I was wrong, you taste of coconut."
    show anon f_confused
    with {'master': dissolve}
    anon "Oh?"
    pause
    show anon f_thinking_up
    show svetlana f_normal
    with {'master': dissolve}
    anon "That's probably the soap I shower with..."
    anon "... My landlady buys it."
    show anon f_surprised
    show svetlana a_rub
    with {'master': dissolve}
    anon @ -m_talk "!!!"
    show anon f_nervous
    with {'master': dissolve}
    anon "... I'm not sure why I just told you that."
    svetlana "Heh, it's okay... you don't have to be embarrassed."
    show anon f_surprised
    with {'master': dissolve}
    pause
    show svetlana a_hold f_sexy_back
    with {'master': dissolve}
    svetlana "Alright, I believe you are ready."
    show anon f_confused
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    anon "Ready for what?"
    svetlana "Shut up and lie back."
    anon "Wha-"
    show anon f_thinking_up
    with {'master': dissolve}
    anon "On the conveyor belt?"
    show anon f_nervous
    with {'master': dissolve}
    svetlana "Da."
    return


label scene_svetlana_furnace_blowjob.stage:
    scene location_warehouse_furnace_convey_front_any
    show svetlana furnace_blowjob
    show anon svet_furnace_blowjob
    return


label scene_svetlana_furnace_blowjob.insert:
    hide anon
    show svetlana furnace_blowjob b_anim01
    return


label scene_svetlana_furnace_blowjob.animate:
    hide svetlana
    show svetlana_furnace_blowjob_body_b_anim as anim
    return


label scene_svetlana_furnace_blowjob.loop:
    call screen scene_svetlana_furnace_blowjob_controls

    if _return:
        return _return

    python hide:
        blocks = 6
        limit = 3

        renpy.dynamic(pool=random.sample(range(2 - limit, blocks + 1), limit))

    pause

    while pool:
        call scene_svetlana_furnace_blowjob.dialogue (pool.pop(), rng=random.random())
        pause

    jump scene_svetlana_furnace_blowjob.loop


label scene_svetlana_furnace_blowjob.dialogue(opt, rng=-1):

    if opt == 1:
        anon "Okay..."
        svetlana "{i}*Sluuuurp*{/i}"
        anon "... Oh KAY!"

    elif opt == 2:
        anon "Wow!"
        svetlana "Mmm."
        anon "Okay, you're really good at that!"

    elif opt == 3:
        svetlana "{i}*Glllck* *Glllck* *Glllck*{/i}"
        anon "Holy shit!"

    elif opt == 4:
        svetlana "{i}*Humming sounds*{/i}"
        anon "Ohh, what's that?!"
        anon "Are you humming?"
        svetlana "Mhmm."

    elif opt == 5:
        anon "Ahh!!"
        anon "Oh my god!"

    elif opt == 6:
        svetlana "{i}*Humming intensifies{/i}"
        anon "Fucking wow!"
        anon "That feels incredible!"

    return


label scene_svetlana_furnace_blowjob.first:
    jump scene_svetlana_furnace_blowjob


label scene_svetlana_furnace_blowjob.repeat:
    $ M_svetlana.set('sex speed', 1 / 8.)

    call scene_svetlana_furnace_blowjob.stage
    with fade
    svetlana "It's even larger than I remember." (show_native="Ty dazhe bol'she, chem ya pomnyu.")
    anon @ -m_talk "Hmm?"
    show svetlana f_normal_back
    with {'master': dissolve}
    svetlana "Nothing."
    show anon f_surprised
    show svetlana a_rub f_normal
    with {'master': dissolve}
    anon "Haaah!"
    pause
    show svetlana f_normal_back
    with {'master': dissolve}
    svetlana "You like to see your big, fat American cock rubbing against my nipples?"
    show anon f_nervous
    with {'master': dissolve}
    anon @ -m_talk "Mhmm."
    show svetlana f_sexy_back
    with {'master': dissolve}
    svetlana "Should I put in my mouth now?"
    anon "Oh, yes... please."
    svetlana "Heh, you ask so politely..."
    show svetlana f_sexy
    with {'master': dissolve}
    svetlana "... I like this."
    call scene_svetlana_furnace_blowjob.insert
    with {'master': dissolve}
    anon "Ohhh, god!"
    call scene_svetlana_furnace_blowjob.animate
    with {'master': dissolve}
    call scene_svetlana_furnace_blowjob.dialogue (1)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (2)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (3)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (4)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (5)
    pause
    call scene_svetlana_furnace_blowjob.dialogue (6)
    pause
    svetlana "{i}*Glllck* *Glllck* *Glllck*{/i}"
    anon "Jesus!"
    anon "I'm getting close!"
    svetlana "{i}*Sluuuurp*{/i}"
    pause

    call scene_svetlana_furnace_blowjob.loop

    anon "Here it..."
    anon "... Comes!!"
    pause
    hide anim
    show svetlana furnace_blowjob b_cum
    anon "HNNGGG!!!" with flash
    pause
    svetlana "{i}*Gulp* *Gulp*{/i}"
    anon "Ahhh!!!"
    pause
    show anon svet_furnace_blowjob f_surprised
    show svetlana b_base f_cum o_cum
    with {'master': dissolve}
    anon "Haah... Haah..."
    show svetlana f_sexy
    with {'master': dissolve}
    svetlana @ -m_talk "{i}*Gulp*{/i}"
    show anon f_nervous
    show svetlana f_sexy_back
    with {'master': dissolve}
    anon "Phew, I'm seeing stars here."
    svetlana "Heh."
    return


label scene_svetlana_furnace_blowjob.replay:
    $ renpy.dynamic(variants=persistent.cookie_jar['svetlana']['variants']['01_unlocked'])

    if len(variants) > 1:
        scene expression background(l=L_warehouse_furnace) with fade
        menu:
            "First" if 'first' in variants:
                jump scene_svetlana_furnace_blowjob.first

            "Repeat" if 'repeat' in variants:
                jump scene_svetlana_furnace_blowjob.repeat

    jump expression 'scene_svetlana_furnace_blowjob.{}'.format(next(iter(variants)))



screen scene_svetlana_furnace_blowjob_controls():
    style_prefix 'sex'

    vbox:

        frame:
            has hbox
            textbutton _('Keep Going') action Return(False)
            textbutton _('Cum') action Return('inside')

        frame:
            has hbox
            textbutton _('« Slower'):
                action (Function(M_svetlana.set, 'sex speed',
                                 1 / (1 / M_svetlana.get('sex speed') - 2)),
                        Return(False))
                sensitive M_svetlana.get('sex speed') < 1 / 8.
            textbutton _('Faster »'):
                action (Function(M_svetlana.set, 'sex speed',
                                 1 / (1 / M_svetlana.get('sex speed') + 2)),
                        Return(False))
                sensitive M_svetlana.get('sex speed') > 1 / 16.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
