label ano09_brat_dealership:
    $ renpy.dynamic(unknown=Character('???', kind=character.nadya))

    scene expression background(728, 480, 1.75) as stage
    show anon with dissolve
    anon @ -m_talk "( I wonder how {b}Josephine{/b}'s getting along? )"
    anon @ -m_talk "( Surely, she's warmed up to the dealership by now. )"
    pause
    anon @ -m_talk "( Hopefully, I don't have to jump through a bunch of hoops this- )"
    unknown "I SAID I DON'T WANT IT!!!{w=.25}{nw}" with hpunch
    show anon f_surprised with {'master': fastdissolve}:
        flip
        xoffset -500
    unknown "I SAID I DON'T WANT IT!!!{fast}"
    anon "What the-"

    scene expression background(88, 536, 6.) as stage
    show goon f_concerned:
        xoffset -100
    show thug f_concerned:
        xoffset 100
    show nadya f_angry:
        xoffset -300
    with fade
    unknown @ f_pouting "Grrr!!!"
    thug "{b}Miss Chernyshevsky{/b}, please!"
    thug "We fix."
    unknown @ f_eyeroll "How will you fix, idiot?!"
    show nadya with dissolve:
        flip
        xoffset 200
    unknown "Are you wizard?"
    unknown "Can you wave hands and make car gunmetal instead of slate gray?!"
    thug "N-no..."
    unknown "I did not think so."
    goon "What if we make pig man order new car?"
    unknown "NO!"
    unknown "{b}Papa{/b} say, you buy me new car today!"
    unknown "Gunmetal Baudi B5!"
    unknown a_crossed @ a_point "{i}Gunmetal{/i}."
    unknown "Not fucking slate gray!"
    thug "Maybe we find better car?"
    unknown "NO!"
    unknown "Nothing is better than Baudi B5!"
    unknown "I must have!"
    goon "What you want us to do?"
    show nadya with dissolve:
        unflip
        xoffset -400
    unknown "We go elsewhere."
    goon "Elsewhere?!"
    thug "We can't do this..."
    goon "Nearest dealership, twenty miles away!"
    show nadya with dissolve:
        flip
        xoffset 200
    unknown @ a_point "I want Baudi B5 and I want it TODAY!"
    thug "But Miss..."
    unknown "You do what I say or {b}Papa{/b} will have your heads!"
    show nadya with dissolve:
        unflip
        xoffset -400
    thug "No, no, I didn't mean-"
    hide nadya with dissolve
    goon @ a_point "There's no need to involve {b}Raz{/b}..."
    goon "We take you to find car."
    thug "Please, slow down..."
    hide goon
    hide thug
    with dissolve
    pause

    scene expression background(872, 480, 3.5) as stage
    show anon a_up f_surprised_teeth:
        flip
        offset (50, 295)
    anon @ -m_talk "( Phew, that was close... )" with fade
    anon f_surprised_down @ -m_talk "( Good thing this text box was here. )"
    anon f_surprised_forward @ -m_talk "( Good thing this text box was here. ){fast}"
    show anon a_sides f_surprised with {'master': dissolve}:
        offset (0, 0)
    anon @ -m_talk "( I almost walked right into them! )"
    pause
    anon @ a_thinking f_thinking -m_talk "( It sounded like the Russians were looking to buy a car here. )"
    anon @ -m_talk "( And did that girl say that {b}Raz{/b} was her father? )"
    pause
    anon f_worried @ -m_talk "( I should {b}speak with Josephine{/b} and find out what she knows about this... )"
    hide anon with dissolve
    return


label ano09_sale_dealership:
    scene expression background(512, 480, 1.75) as stage
    show tony_overlay_o_racer as coupe
    with fade
    show anon f_laugh behind coupe at flip with dissolve
    anon "( Holy crap, this car is a beast! )"
    anon f_grin @ -m_talk "( {b}I can't wait to show Tony{/b}. )"
    hide anon
    hide coupe
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
