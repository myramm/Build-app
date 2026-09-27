label lucy_creche_board_dialogue:
    $ renpy.dynamic(kids=PregnancyManager.total_babies())

    scene
    show screen lucy_creche_board(kids + 7)
    anon "( Hmm, this must be the number of kids currently enrolled in {b}Lucy{/b}'s daycare... )"


    if kids <= 3:
        anon "( So few? )"

        anon "( No wonder she's struggling. )"


    elif kids < 10:
        anon "( That seems like a nice manageable number for her small business. )"

        anon "( I'm happy to see she's doing so well. )"


    elif kids < 20:
        anon "( Whoa, she must have a lot of patience to look after so many kids at once. )"

        anon "( And she's still so upbeat and full of energy... )"


    elif kids < 35:
        anon "( Holy crap, how in the world is she taking care of so many kids by herself?! )"

        anon "( She should look into hiring some help or something... )"


    elif kids < 50:
        anon "( There can't really be this many kids here, right? )"

        anon "( I mean, c'mon people, they're called condoms... Try them sometime. )"


    elif kids < 100:
        scene expression background(312, 400, 4.5) as stage
        show anon f_grumpy:
            flip
        with fade
        anon @ -m_talk "( What are you trying to prove, man?! )"

        anon @ -m_talk "( You think this is a game?! )"

        pause
        anon @ -m_talk "( How the hell am I supposed to support all these kids?! )"

        hide anon with dissolve

    elif kids < 150:
        scene expression background(312, 400, 4.5) as stage
        show anon b_dressed_bow:
            flip
        with fade
        anon @ -m_talk "( Please... No more! )"

        anon @ -m_talk "( I'm begging you, man... Find another outlet to vent your sexual frustrations! )"

        pause
        anon a_cover_boner b_dressed f_shy_cringe @ -m_talk "( My dick is going to fall off if this keeps up! )"

        hide anon with dissolve

    elif kids < 200:
        scene expression background(312, 400, 4.5) as stage
        show anon a_sides f_worried:
            flip
        with fade
        anon @ -m_talk "( This isn't a baby making simulator, you know? )"

        anon @ -m_talk "( There's tons of other stuff we could be doing besides marathon breeding sessions... )"

        pause
        anon f_normal @ -m_talk "( Why don't we go solve my father's murder or take a girl to the big dance, huh? )"

        anon f_laugh @ -m_talk "( That sounds like fun! )"

        pause
        show anon f_worried with {'master': dissolve}
        pause
        anon f_squint @ -m_talk "( You're not going to stop, are you? )"

        pause
        anon f_sad "{i}*Huh*{/i}"

        anon f_sad_down @ -m_talk "( Damnit. )"

        hide anon with dissolve
    else:

        scene expression background(312, 400, 4.5) as stage
        show anon a_sides f_surprised_forward:
            flip
        with fade
        anon @ -m_talk "( Over two hundred... )"

        pause
        anon f_worried "Do you have any idea the kind of stress that comes from fathering two hundred children?"

        anon a_frustrated f_angry "No, of course you don't!"

        anon a_surprised "You just sit there on your little computer or whatever, forcing the goofy, lovable, little protagonist to shove his mutant hog into everything you can find!"

        anon a_frustrated "Over and over and OVER!!"

        anon "With no regard of the consequences!"

        pause
        show anon a_surprised f_worried with {'master': dissolve}
        pause
        anon a_sides f_sad "I gotta live with this stuff man, I can't-"

        anon a_cover_boner3 f_shy_cringe @ -m_talk "Ergh!"

        show anon a_sides f_sad with {'master': dissolve}
        pause
        anon f_normal_out "Well guess what, pal?!"

        anon "I'm done!"

        anon "Yeeeeeah, that's right!"

        anon a_point_back "I don't have to take this crap, I'm outta here!"

        anon a_surprised "Let's see how far you make it in Summerville without me, huh!?"

        show anon a_sides m_talk with {'master': dissolve}:
            unflip
            xoffset 550
        anon "Hahahaah!"

        hide anon with {'master': dissolve}
        anon "Hahahahahahaaaaaah!!!"


        $ A_game_over.unlock()
        show screen confirm(
            _('GAME OVER...'),
            _layer='master',
            background='menu_condom',
            no_action=MainMenu(),
            no_text=_('Quit'),
            yes_action=Return(),
            yes_text=_('Restore')) with gameover
        call screen empty()

    return


screen lucy_creche_board(kids):
    layer 'master'
    sensitive False

    add 'backgrounds/location_annie_daycare_board_closeup.jpg'

    text _('LIL\' ONES'):
        align .5, .5
        ypos 105
        color '000a'
        font 'fonts/caveat.ttf'
        size 50

    text str(kids):
        align .5, .55
        color 'e75d48cc'
        at Transform(rotate=3, transform_anchor=True, xzoom=1.5)
        font 'fonts/alphabetizedcassettetapes-classic.ttf'
        size 250
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
