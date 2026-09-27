label yoy01_meet_dealership_garage:
    scene expression background(200, 472, 4) as stage
    show yoyo a_behind b_army f_smirk o_hat
    anon "I hope you have whip cream because I about to go to town on that pie!"

    show anon a_sides f_surprised:
        xoffset 65
    with {'master': dissolve}
    pause
    anon f_normal "That's a nice uniform."

    pause
    anon "Where's the table?"

    yoyo "You simre foor!!"

    show anon f_confused
    yoyo "You rearry think {b}Kim{/b} make aporogy pie for bad boy rike you?!"

    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "T-there's no pie?"

    yoyo "{b}Kim{/b} ray trap for you!"

    show anon a_sides f_sad_down
    with {'master': dissolve}
    anon "Ah, kawan."

    yoyo "Now you arr arone and at {b}Kim{/b} mercy..."

    show anon f_worried:
        xoffset -435
        xzoom -1
    with {'master': dissolve}
    anon "Ehh..."

    show anon f_confused:
        xoffset 65
        xzoom 1
    with {'master': dissolve}
    anon "... Oke?"

    pause
    anon "Sekarang apa?"

    show yoyo a_pocket
    with {'master': dissolve}
    yoyo "Now you answer for crimes against {b}Kim{/b} famiry!"

    show yoyo a_taser
    with {'master': dissolve}
    anon f_worried @ f_confused_low "Umm, what the heck is that?"

    yoyo f_normal "{b}Kim{/b} give you one chance!"

    yoyo "Terr me rocation of {b}Rump{/b}'s derivery to grorious nation of North Korea..."

    yoyo "... And {b}Kim{/b} ret you go with onry srap on wrist."

    anon f_confused "{b}Rump{/b}'s delivery?"

    yoyo f_annoyed "You find coordinates for drop in {b}Kim{/b} statue!"

    yoyo "Give them to {b}Kim{/b} now!"

    show anon a_rub f_normal
    with {'master': dissolve}
    anon @ f_normal_low "Or what, you're gonna shoot me with that toy?!"

    yoyo f_normal "{b}Kim{/b} count to three."

    show anon a_sides
    with {'master': dissolve}
    yoyo "One."

    anon "I'm not scared of you lady!"

    show anon a_pocket f_brag
    with {'master': dissolve}
    anon "You're just like your brother, all bark and no bite..."

    show yoyo a_taser_point
    with {'master': dissolve}
    yoyo "Dua."

    anon "... You want to book a cell next to his, I've got no problem-"

    show anon a_surprised f_hurt
    show yoyo a_taser_shoot
    show yoyo_overlay_o_taser_shoot1 as wires
    with {'master': dissolve}
    anon "{i}*Hurk*{/i}"

    show anon b_dressed_zap behind yoyo:
        xoffset -115
    show yoyo f_smirk
    show yoyo_overlay_o_taser_shoot2 as wires
    "{i}*Bzzzzzzzzzzzzzzzt*{/i}" with hpunch
    show anon b_dressed f_surprised_forward o_boner:
        xoffset 0
    show anon_overlay_o_soot as soot
    show anon_overlay_o_taser_barbs as barbs
    show yoyo a_taser_point
    show yoyo_overlay_o_taser as wires
    with {'master': dissolve}
    pause
    show anon b_dressed_falling:
        xoffset -275
    show anon_overlay_falling_o_soot as soot:
        xoffset -275
    show anon_overlay_falling_o_taser_barbs as barbs:
        xoffset -275
    with {'master': dissolve}
    anon "Urrghh."

    show yoyo f_smirk_low
    hide anon
    hide barbs
    hide soot
    with vpunch
    pause
    anon "W-wha-wha-what happened to three?"

    yoyo "Three."

    show anon b_dressed_zap:
        offset (-600, 130)
        rotate -80
    show yoyo a_taser_shoot
    show yoyo_overlay_o_taser_shoot2 as wires
    "{i}*Bzzzzzzzzzzzzzzzt*{/i}" with hpunch
    hide anon
    show yoyo a_taser_point
    show yoyo_overlay_o_taser as wires
    with {'master': dissolve}
    pause
    yoyo @ f_laugh_low "Rona rona rona rona!"


    scene location_dealership_garage_kidnap1
    with fade
    anon "Ugh..."

    pause
    anon "... M-my freaking balls..."

    yoyo "Diam!"

    anon "{i}* Merengek*{/i}"


    scene location_dealership_garage_kidnap2
    with dissolve
    yoyo "Grrraaahh!!"

    yoyo "You need to rose some weight, dumb guy."

    anon "... N-no..."

    yoyo "{i}*Grunts*{/i}"

    anon "... Leave me."

    pause

    call scene_yoyo_truck_cowgirl
    $ unlock_scene('yoyo', '01_unlocked', variant='first')

    scene location_dealership_alley
    with fade
    anon "Ugh, my head..."

    anon "... What in the heck happened?"

    pause
    anon "And what's that awful smell?!"


    scene location_dealership_alley_garbage
    with fade
    pause
    show anon a_up f_disgusted_left_low o_sewage of_banana:
        offset (-200, 140) xzoom -1
    show location_dealership_alley_garbage_overlay as dumpster
    with {'master': dissolve}
    pause
    anon "Umm?"

    show anon f_disgusted_low
    pause
    anon "Ahh, kawan..."

    anon f_disgusted_down "... She threw me in the garbage?"

    anon f_annoyed "That's too much..."

    show anon a_fists:
        yoffset 0
    with {'master': dissolve}
    anon "... This aggression will not stand!"

    pause
    show anon a_sides
    with {'master': dissolve}
    anon "I'm gonna give that crazy bitch a piece of my mind!"

    pause
    show anon f_annoyed_up
    pause
    show anon a_banana_grab -of_banana
    with {'master': dissolve}
    pause
    show anon a_banana f_worried_low
    with {'master': dissolve}
    anon "I mean, after a thorough shower..."

    show anon a_surprised f_worried_down
    with {'master': dissolve}
    anon "... Or two."

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
