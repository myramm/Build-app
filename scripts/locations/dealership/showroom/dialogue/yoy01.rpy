label yoy01_meet_dealership_showroom:
    scene expression background() as stage
    show anon a_sides with dissolve
    pause
    show yoyo a_clasp f_shy_sad
    with {'master': dissolve}
    yoyo "Hei, um..."

    yoyo f_shy_sad_down "... So {b}Kim{/b} has been thinking, and..."

    show anon f_confused
    show yoyo a_clench
    with {'master': dissolve}
    yoyo "... Maybe you right."

    anon "Hmm?"

    show yoyo a_clasp f_shy_sad_down
    with {'master': dissolve}
    yoyo "Maybe {b}Kim{/b} famiry {i}is{/i} evir for wanting worrd domination."

    pause
    yoyo f_shy_sad "Maybe {b}Kim{/b} shourd aspire to smarrer and more easiry obtainabre things."

    show yoyo a_clench
    with {'master': dissolve}
    yoyo "Rike, row paying management position at rocal retair outret."

    show anon a_crossed f_skeptical
    with {'master': dissolve}
    anon "Ehh, are you messing with me right now?"

    show yoyo a_stop
    with {'master': dissolve}
    yoyo "No, {b}Kim{/b} thank you!"

    show anon a_surprised f_surprised_low
    show yoyo b_dressed_bow
    with {'master': dissolve}
    pause
    show anon a_sides f_surprised
    show yoyo a_clasp b_dressed
    with {'master': dissolve}
    yoyo "You herp {b}Kim{/b} see the right."

    yoyo f_shy_sad_down "{b}Kim{/b} is meant for average rife."

    show anon f_confused
    yoyo "Sour crushing nine to five and a spineress, unattractive husband waiting at home with ritter of ungratefur brats."

    show anon a_rub f_worried
    with {'master': dissolve}
    anon "Oh, c'mon... you can do a lot better than that!"

    yoyo "Tidak, tidak apa-apa."

    show anon a_give_me
    with {'master': dissolve}
    anon "Seriously, you're a young and intelligent woman..."

    yoyo f_shy_sad "Menurutmu begitu?"

    show anon a_sides f_normal
    with {'master': dissolve}
    anon f_normal "Benar sekali!"

    anon "You're driven and well spoken..."

    anon "... And you're not unattractive."

    yoyo f_shy_sad_down "You're just being nice."

    anon "No, I mean it!"

    show anon a_behind_head f_shy
    with {'master': dissolve}
    anon "When you're not spouting off nonsense about dominating mankind, you're actually kinda cute."

    yoyo f_shy_sad "Reary?!"

    show anon a_sides
    with {'master': dissolve}
    anon "Tentu."

    show yoyo a_clench f_shy
    with {'master': dissolve}
    yoyo "Aww, you nice boy... very, very nice boy."

    anon "Hehe, terima kasih."

    show yoyo a_gimme
    with {'master': dissolve}
    yoyo "Come... I make for you, aporogy pie..."

    anon f_confused @ -m_talk "Hmm?"

    show yoyo a_sides
    with {'master': dissolve}
    yoyo "... Korean tradition."

    yoyo f_happy "Very dericious!"

    anon f_shy "Ah, tidak... itu tidak perlu."

    yoyo "Anda yakin?"

    pause
    yoyo "Apakah krim pisang."


    menu yoy01_meet_dealership_showroom.choice:
        "Tidak, terima kasih.":
            jump yoy01_meet_dealership_showroom.nah
        "Did you say banana cream?":

            pass

    anon f_confused "Banana cream?"

    yoyo f_smirk "Made speciar for just you."

    show anon a_thinking f_thinking
    with {'master': dissolve}
    anon "I do love banana cream..."

    pause
    show anon a_frustrated f_shy
    show yoyo f_happy
    with {'master': dissolve}
    anon "... Aww, what the heck..."

    anon f_happy "... I'd love to taste your pie, {b}Kim{/b}!"

    show anon a_sides
    with {'master': dissolve}
    yoyo f_happy_surprised "Yes, yes!"

    yoyo "{b}Forrow me into garage{/b}, I set up table for you."

    hide yoyo
    show anon f_thinking
    with {'master': dissolve}
    anon @ -m_talk "( Garage, huh? )"

    anon @ -m_talk "( That's an odd place for pie but sure! )"

    show anon f_grin
    pause
    hide anon with dissolve
    return T_yoy01_hold


label yoy01_meet_dealership_showroom.nah:
    anon f_normal "Mungkin lain kali."

    show yoyo a_clasp f_shy_sad_down
    with {'master': dissolve}
    yoyo "Oh baiklah."

    yoyo "{b}Kim{/b} understand."

    anon "I'm happy to see you're turning over a new leaf though..."

    anon "... Really, that's awesome!"

    show yoyo a_clench f_shy
    with {'master': dissolve}
    yoyo "Arr thanks to you!"

    yoyo "You come back soon, we have aporogy pie, okay?!"

    show anon a_wave
    show yoyo a_clasp
    with {'master': dissolve}
    anon "Tentu saja."

    hide anon with dissolve
    return T_yoy01_meet
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
