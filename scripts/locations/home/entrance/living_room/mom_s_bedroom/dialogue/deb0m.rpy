label deb0m_init:
    scene expression background(236, 432, 4.5, l=L_home_livingroom) as stage
    show anon with {'master': dissolve}:
        xzoom -1
    debbie "Hehehe!"

    anon f_confused @ -m_talk "(Hmm?)"

    pause
    debbie "Stop it, that tickles!!"

    anon f_surprised @ -m_talk "( That's coming from {b}[deb_name]{/b}'s room! )"

    debbie "Hehehe!"

    anon f_confused @ -m_talk "( Is someone in there with her? )"

    show anon:
        xoffset -350
    with {'master': dissolve}
    diane "What if I do this?"

    debbie "Ya ampun..."

    diane "Mmm, that brings back some memories, doesn't it?"

    debbie "Ngh, yes..."

    anon @ -m_talk "( That's {b}Diane{/b}! )"

    diane "hehe!"

    show anon b_dressed_bending1
    with {'master': dissolve}
    anon @ -m_talk "( What are they doing in there? )"

    anon a_surprised b_dressed f_surprised_forward of_blush @ -m_talk "!!!" with hpunch
    show anon a_sides
    with {'master': dissolve}
    debbie "Ya Tuhan... di sana!"

    show anon b_dressed_bending1 -of_blush
    with dissolve
    jump deb0m_view


label deb0m_init.repeat:
    scene expression background(236, 432, 4.5, l=L_home_livingroom) as stage
    show anon with {'master': dissolve}:
        xzoom -1
    debbie "Mmm, don't tease me!"

    anon f_confused @ -m_talk "(Hmm?)"

    pause
    debbie "{b}Diane{/b}, I'm serious!"

    anon f_surprised @ -m_talk "( That's coming from {b}[deb_name]{/b}'s room! )"

    diane "Hehehe!"

    anon f_flirt_grin @ -m_talk "( Are they going at it again? )"

    show anon:
        xoffset -350
    with {'master': dissolve}
    diane "Is this better?"

    debbie "Ngh, yes..."

    show anon b_dressed_bending1
    with {'master': dissolve}
    diane "How about this?"

    debbie "Ya Tuhan... di sana!"

    jump deb0m_view.repeat


label deb0m_view:
    call scene_debbie_diane_bedroom.repeat
    $ unlock_scene('Debbie', '13_unlocked')

    scene location_home_debbiesidebed_lesb_after
    show debbie deb0m_post
    show diane deb0m_post
    with fade
    diane "Fiuh."

    debbie "Worn out?"

    diane @ -m_talk "Mhmm."

    pause
    diane "Bukan?"

    debbie @ f_laugh "Ya."

    pause
    debbie "You know, I remember we used to do this three or four times a night..."

    diane @ f_laugh "Heh, yeah... when we were teenagers!"

    show debbie f_lipbite
    pause
    debbie f_calm "Remember summer camp?"

    diane "Tentu saja."

    debbie "With that stupid counselor, what was her name?"

    debbie "Meg?"

    diane "Yeah, Meg."

    diane "I hated that bitch."

    debbie "You broke into her cabin after everyone fell asleep and threw all her clothes into the lake."

    diane "Hehe, ya."

    debbie "And she forced us to sleep in that secluded cabin at the edge of camp by ourselves for the last two weeks."

    show debbie f_lipbite
    diane "Silly bitch thought she was punishing us."

    show diane f_laugh m_talk
    debbie f_laugh m_talk "Hehehe!"

    diane "Hehehe!"

    show debbie f_lipbite -m_talk
    show diane f_calm_close -m_talk
    pause
    diane "Remember the night we broke the bed?"

    debbie f_calm "Heh, yeah!"

    debbie "We had to tie a bunch of our socks around the frame to keep it together."

    diane "It held though, didn't it?"

    show diane f_laugh m_talk
    debbie f_laugh m_talk "Hehehe!"

    diane "Hehehe!"

    show debbie f_calm_close -m_talk
    show diane f_calm_close -m_talk
    pause
    debbie "I miss those days."

    diane "Saya juga."


    scene expression background(236, 432, 4.5, l=L_home_livingroom) as stage
    show anon b_dressed_bending1:
        xoffset -350
        xzoom -1
    with fade
    show anon a_sides b_dressed f_flirt_grin o_boner
    with {'master': dissolve}
    anon @ -m_talk "( Looks like they're done for now. )"

    show anon:
        xoffset 150
        xzoom 1
    with {'master': dissolve}
    anon @ -m_talk "( Man, that was hot! )"

    anon @ -m_talk "( I'm so glad {b}Diane{/b} is staying with us! )"

    show anon f_surprised_down
    pause
    anon @ -m_talk "( I should probably go take care of this. )"

    hide anon with dissolve
    return


label deb0m_view.repeat:
    call scene_debbie_diane_bedroom.repeat
    $ unlock_scene('Debbie', '13_unlocked')

    scene location_home_debbiesidebed_lesb_after
    show debbie deb0m_post
    show diane deb0m_post
    with fade
    diane "Fiuh."

    debbie "Anda merasa lebih baik sekarang?"

    diane @ -m_talk "Mhmm."

    debbie "Bagus."

    pause
    debbie f_calm_close "I always sleep better when you're here."

    pause
    debbie "Good night, {b}Diane{/b}."

    diane @ -m_talk "Zzz..."

    pause

    scene expression background(236, 432, 4.5, l=L_home_livingroom) as stage
    show anon b_dressed_bending1:
        xoffset -350
        xzoom -1
    with fade
    show anon a_sides b_dressed f_flirt_grin o_boner
    with {'master': dissolve}
    anon @ -m_talk "( Looks like they're done for now. )"

    show anon:
        xoffset 150
        xzoom 1
    with {'master': dissolve}
    anon @ -m_talk "( Man, that was hot! )"

    anon @ -m_talk "( I'm so glad {b}Diane{/b} is staying with us! )"

    show anon f_surprised_down
    pause
    anon @ -m_talk "( I should probably go take care of this. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
