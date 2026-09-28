label yoyo_button_showroom:
    show anon a_point f_annoyed with {'master': dissolve}
    anon "Alright, crazy lady, I've got a serious bone to pick with you!"
    yoyo f_eyeroll "Ugh, go away dumb guy..."
    show anon a_sides
    with {'master': dissolve}
    yoyo f_normal "... {b}Kim{/b} done with you."
    anon f_skeptical "Huh?!"
    anon "I-"
    pause
    anon f_annoyed "Well, I'm not done!"
    show anon a_frustrated
    with {'master': dissolve}
    anon "I woke up in a garbage bin!"
    yoyo f_normal "Yeah, {b}Kim{/b} put you there."
    show anon a_sides
    with {'master': dissolve}
    anon @ -m_talk "..."
    show yoyo a_point_under
    with {'master': dissolve}
    yoyo "You berong in trash, you worthress."
    anon "Hey, screw you lady!"
    show yoyo a_gimme
    with {'master': dissolve}
    yoyo "Rook, it obvious you don't know coordinates..."
    yoyo "... You break rike rittre girr during interrogation."
    show anon a_crossed f_unimpressed
    show yoyo a_sides
    with {'master': dissolve}
    anon "I did not."
    yoyo "Did so."
    anon "No, I didn't."
    show yoyo a_tantrum f_annoyed
    with {'master': dissolve}
    yoyo "Yes, you did!"
    anon "No, I didn't!"
    show yoyo a_frustrated f_angry
    with {'master': dissolve}
    yoyo "YES, YOU DID!!"
    show anon a_tantrum f_annoyed
    with {'master': dissolve}
    anon "Didn't!"
    yoyo "DID!!"
    show anon a_angry f_angry
    with {'master': dissolve}
    anon "DIDN'T!!"
    yoyo f_scary @ f_angry_teeth "DID!!!"
    pause
    show anon a_sides f_tired
    with {'master': dissolve}
    pause
    anon "Lady, you couldn't break wind in a bean factory."
    show yoyo f_annoyed
    with {'master': dissolve}
    yoyo f_cynical "Can too."
    anon "Sex is not an effective interrogation tool."
    show yoyo a_crossed
    with {'master': dissolve}
    yoyo "Is too."
    yoyo "Back in Korea, {b}Kim{/b} brother break countress women with threat of sex arone."
    show anon a_facepalm f_disgusted
    with {'master': dissolve}
    anon "Eugh, no... I did not need that mental image!"
    show anon f_disgusted_wince
    pause
    show anon a_sides f_tired
    with {'master': dissolve}
    anon "{i}*Sigh*{/i}"
    anon f_worried "Look, maybe your brother can... he's basically a goblin but you..."
    show yoyo f_confused
    anon "... Well, you're-"
    show anon f_disgusted
    pause
    anon f_worried "Nah, I can't bring myself to say it."
    show yoyo a_point_under f_smirk
    with {'master': dissolve}
    yoyo "Just admit you break!"
    show anon a_crossed f_unimpressed
    with {'master': dissolve}
    anon "Umm, no... because I didn't."
    show yoyo a_sides f_angry
    with {'master': dissolve}
    yoyo "Grr, okay, dumb guy..."
    yoyo "... We go again and this time {b}Kim{/b} break you twice as hard!"
    show anon f_surprised

    menu yoyo_button_showroom.choice:
        "Screw that!":

            jump yoyo_button_showroom.nah
        "Bring it on!":

            pass

    anon f_annoyed "You know what, fine!"
    show anon a_sides f_grumpy
    with {'master': dissolve}
    anon "Other than the taser, I found your interrogation techniques to be strangely enjoyable..."
    anon "... After getting past the initial revulsion of having you touch me, of course."
    yoyo f_annoyed "Pervert."

    if 'counter' not in renpy.get_showing_tags():
        show anon a_point_back
        with {'master': dissolve}

    anon f_annoyed "Shut up and get in the garage!"
    hide yoyo
    with {'master': dissolve}
    yoyo "Hmph!"

    if 'counter' not in renpy.get_showing_tags():
        show anon a_sides:
            xoffset -500
            xzoom -1
        with {'master': dissolve}

    pause
    show anon a_frustrated f_eyeroll
    with {'master': dissolve}
    anon "Freaking {b}Kim{/b}s and their crazy shit."
    hide anon with dissolve

    call scene_yoyo_truck_cowgirl.repeat
    $ unlock_scene('yoyo', '01_unlocked', variant='repeat')

    scene location_dealership_alley
    with fade
    anon "Ugh, no..."
    anon "... Not again."

    scene location_dealership_alley_garbage
    with fade
    pause
    show anon a_up f_disgusted_low o_sewage of_banana:
        offset (-200, 140) xzoom -1
    show location_dealership_alley_garbage_overlay as dumpster
    with {'master': dissolve}
    pause
    anon f_tired "Ahh, man..."
    anon "... I have only myself to blame for this one."
    show anon a_sides:
        yoffset 0
    with {'master': dissolve}
    pause
    show anon f_tired_up
    pause
    show anon a_banana_grab -of_banana
    with {'master': dissolve}
    pause
    show anon a_banana f_tired_low
    with {'master': dissolve}
    anon "{i}*Sigh*{/i} Freaking {b}Kim{/b}s."
    show anon a_sides f_disgusted_low
    with {'master': dissolve}
    pause
    hide anon with dissolve
    return 'dumpster'


label yoyo_button_showroom.nah:
    anon f_annoyed "Yeah, in your dreams I'm doing that again."
    hide anon
    with {'master': dissolve}
    yoyo "Hey, where you going?!"
    anon "As far away from you as possible, crazy lady!"
    show yoyo a_hips:
        xoffset -250
    with {'master': dissolve}
    yoyo "You come here right now and have sex with {b}Kim{/b}!"
    anon "Nope."
    yoyo "I mean it!!"
    anon "Can't hear you!"
    hide yoyo
    with {'master': dissolve}
    yoyo "Get back here, you bad boy!!"
    return L_dealership


label yoyo_button_showroom.repeat:
    show anon a_sides with {'master': dissolve}
    yoyo f_laugh_low "Hue hue hue."
    show anon f_unimpressed
    show yoyo a_point_under f_smirk
    with {'master': dissolve}
    yoyo "{b}Kim{/b} break you so hard rast time..."
    anon "Umm, no you didn't."
    show yoyo a_sides
    with {'master': dissolve}
    yoyo "Did so."
    anon "No, you didn't."
    show yoyo a_tantrum f_annoyed
    with {'master': dissolve}
    yoyo "Did so!"
    show anon a_tantrum f_annoyed
    with {'master': dissolve}
    anon "No, you didn't!"
    show yoyo a_frustrated f_angry
    with {'master': dissolve}
    yoyo "DID!!"
    show anon a_angry f_angry
    with {'master': dissolve}
    anon "DIDN'T!!"
    yoyo f_scary @ f_angry_teeth "DID!!!"
    pause
    show anon a_sides f_tired
    with {'master': dissolve}
    anon "{i}*Sigh*{/i}"
    anon f_grumpy "Arguing with you pointless..."
    show yoyo a_crossed f_annoyed
    with {'master': dissolve}
    yoyo "Just admit you break!"
    show anon a_pocket f_unimpressed
    with {'master': dissolve}
    anon "Umm, no... because I didn't."
    show yoyo a_sides f_angry
    with {'master': dissolve}
    yoyo "Grr, okay, dumb guy..."
    yoyo "... We go again and this time {b}Kim{/b} break you twice as hard!"
    jump yoyo_button_showroom.choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
