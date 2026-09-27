label town_map_mugging:
    scene location_mugging_closeup
    show thug:
        flip
        xoffset 300
    show goon:
        xoffset 100
    show anon f_surprised_teeth a_sides with dissolve
    anon "!!!" with hpunch
    anon @ -m_talk "( Oh, shit! )"

    anon @ -m_talk "( I gotta get out of here quick before they notice me! )"

    show anon with dissolve:
        xoffset -50
    goon f_curious "Hey, isn't that guy whose father stole from {b}Raz{/b}?"

    show thug with dissolve:
        unflip
        xoffset -200
    thug "You mean the one {b}Dimitri{/b} calls little bunny?"

    goon f_normal "Hah, it is him!"

    anon f_worried "Look fellas, I don't want any trouble."

    thug "What are you doing here, little bunny?"

    goon "Should we take him to hideout?"

    goon "{b}Raz{/b} is sure to give us big money."

    show thug with dissolve:
        flip
        xoffset 300
    thug "Mustahil."

    thug "{b}Dimitri{/b} say he bring this one in personally."

    goon "Ugh, why do he always have all the fun?"

    thug "Because he is {b}Raz{/b} right-hand man."

    thug "You know this."

    goon "Can we at least take his money?"

    thug "Oh, that's good thinking."

    show thug with dissolve:
        unflip
        xoffset -200
    thug "Hey you, give us money!"

    anon "Aww, man... Seriously?"

    goon a_gun "Unless you prefer I shoot you in face?"

    anon "!!!" with hpunch
    anon "N-no, no... I would NOT in fact prefer that!"

    show anon a_backpack with dissolve
    pause
    if player.has_money(1):
        show anon a_money with dissolve
        pause
        show thug a_money_count
        show anon a_sides
        with dissolve
    else:
        show anon a_ticket with dissolve
    if player.has_money(5000):
        thug "This just walking around tax. We leave some.{w=2}{nw}"

        thug f_laugh "This just walking around tax. We leave some.{fast} Not monsters."

        anon "Th-thanks..?"

        show thug f_normal
    else:
        thug "Is this all you have?"

        anon "That's all I have on me, I swear!"

        if player.has_money(1):
            thug "It will do."

        else:
            thug "Get job!"

    goon a_idle @ a_point "Run along home now, little bunny."

    thug "Remind nice lady that {b}Dimitri{/b} collect soon."

    show thug f_laugh
    goon f_laugh "Ha ha ha!"

    hide thug
    hide goon
    with dissolve
    pause
    anon f_sad_down a_behind_head @ -m_talk "( Well, that was terrifying... )"

    if player.has_money(5000):
        anon "( {i}*Sigh*{/i} And an awful lot of money. )"

        anon "( Wonderful. )"

    elif player.has_money(1):
        anon "( {i}*Sigh*{/i} And now I'm broke. )"

        anon "( Wonderful. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
