label crystal_button_outside:
    scene location_trailer_closeup01_new_evening
    show location_trailer_closeup01_chair as chair
    show crystal b_dressed_sitting

    if M_crystal.mood == 'bitter':
        jump crystal_button_outside.bitter

    if M_crystal.mood == 'bliss':
        jump crystal_button_outside.bliss

    show anon with {'master': dissolve}:
        xoffset 100
        xzoom -1
    crystal f_smirk "Mmm, now there's a nice capable man!"
    show anon a_wave
    with {'master': dissolve}
    anon "Heh, hi {b}Crystal{/b}..."
    show anon a_sides
    with {'master': dissolve}
    crystal f_normal "Why don't you grab a beer and come sit with me, Romeo?"
    crystal f_smirk "You can show off that silver tongue some more..."
    show anon a_shy_neck f_shy_left
    with {'master': dissolve}
    anon "Oh, I dunno... {b}Roxxy{/b} wouldn't-"
    crystal f_normal "Yer here to call on {b}Roxxy{/b} then?"
    show anon a_sides f_normal
    with {'master': dissolve}

    menu crystal_button_outside.choice:
        "Quickie?" if M_roxxy.get('roxxy crystal sex'):
            jump crystal_button_outside.quickie
        "Yeah, is she here?":

            jump crystal_button_outside.roxxy
        "I should go.":

            pass

    show anon a_point_back
    with {'master': dissolve}
    anon "I should probably get in there..."
    show anon a_sides
    with {'master': dissolve}
    crystal "Yeah, I reckon yer right about that."
    crystal "Take good care of my girl now, ya hear?"
    show anon a_salute f_happy_closed
    with {'master': dissolve}
    anon "Yes, ma'am."
    hide anon
    show crystal f_laugh
    with {'master': dissolve}
    crystal @ -m_talk "Hahaha!"
    crystal f_normal "\"Ma'am\"..."
    crystal "... That kills me every time!"
    return


label crystal_button_outside.bitter:
    show crystal f_annoyed
    show anon a_sides with {'master': dissolve}:
        xoffset 100
        xzoom -1
    crystal "Well, go on!"
    show anon f_confused
    crystal "Get in there and fuck mah daughter!"
    show anon f_worried
    crystal "Ya gon' leave me out here ta paddle the pink canoe by myself..."
    crystal "... Least ya can do is give me somethin' perty ta listen to!"
    anon "Sorry, {b}Crystal{/b}..."
    hide anon
    show crystal f_eyeroll
    with {'master': dissolve}
    crystal "Yeah, whatever."
    crystal f_annoyed "Buncha ungrateful-"
    return


label crystal_button_outside.bliss:
    show crystal b_pantless_sitting f_smirk
    show anon a_sides with {'master': dissolve}:
        xoffset 100
        xzoom -1
    crystal "Get on now..."
    show anon f_grin
    crystal "... I need me some time to recuperate after a fuckin' like that!"
    anon f_normal "Heh, okay."
    show anon a_wave
    with {'master': dissolve}
    anon "See ya, {b}Crystal{/b}."
    hide anon
    with {'master': dissolve}
    crystal @ -m_talk "Mhmm."
    pause
    crystal "Whew..."
    crystal "... God damn!"
    return


label crystal_button_outside.quickie:
    crystal f_smirk "Hey, how 'bouts a quickie 'fore ya head inside?"
    anon f_confused @ -m_talk "Hmm?"
    crystal "Seems ta me... iffin' I gots to listen to y'all ruttin' around in there all evenin'..."
    crystal f_normal "... It's only fair that ya butter mah biscuit first now!"
    anon f_surprised "Wha-" with hpunch
    anon "We can't do that!"
    crystal f_annoyed "Well, why the heck not?!"
    anon f_worried_surprised "{b}Roxxy{/b}'s right inside..."
    anon f_worried "... She'll hear us for sure!"
    crystal f_smirk "Pfft, she ain't gon' pay no mind to us..."
    show anon f_worried_left
    crystal "... Not while she's in there yappin' away on that dumb phone a hers!"
    anon f_worried "Oh, I dunno..."
    crystal f_annoyed "Tch, c'mon now..."
    crystal "... Yer not just gonna leave me out here all by mah lonesome and hurtin' fer a squirtin' is ya?!"
    show anon f_confused
    crystal "And here I thought you was a gentleman..."
    anon @ f_skeptical "Umm, did you just say, \"Hurtin' for a squirtin'?!\""
    crystal f_smirk "You better believe it!"
    show anon f_worried:
        xoffset 600
        xzoom 1
    with {'master': dissolve}
    anon "W-what about the neighbors?!"
    crystal f_annoyed "Oh, fuck the neighbors!"
    show anon f_worried:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    crystal "I don't give a shit what they think..."
    show crystal b_dressed_sitting_beer
    with {'master': dissolve}
    pause
    show crystal b_dressed_sitting f_smirk
    with {'master': dissolve}
    crystal "... Besides, dark as it is out here... they ain't gon' see nothin'."
    show anon a_rub
    with {'master': dissolve}
    anon @ -m_talk "{i}*Gulp*{/i}"

    menu:
        "Sorry, but no.":
            pass
        "Alright, but let's be quick!":

            jump crystal_button_outside.sex

    show anon a_sides f_worried
    with {'master': dissolve}
    anon "Sorry, no."
    crystal f_annoyed @ f_eyeroll "Ugh, fine."
    crystal "Go on and get ta poundin' away on mah daughter then..."
    crystal "... I reckon I'll hafta take care of mah own damn self... as usual!"
    show crystal b_dressed_sitting_beer
    with {'master': dissolve}
    anon f_shy "Maybe next time?"
    show crystal b_dressed_sitting
    with {'master': dissolve}
    crystal @ -m_talk "Mhmm."
    hide anon
    show crystal a_beer_throw f_annoyed
    with {'master': dissolve}
    pause
    show crystal a_resting
    with {'master': dissolve}
    crystal @ f_burp -m_talk "{i}*Buuuurp*{/i}"
    crystal "Damned ungrateful brats!"
    crystal "Ya know, I got needs too... but do they care?!"
    crystal f_eyeroll "Psh, course not!"
    return 'bitter'


label crystal_button_outside.roxxy:
    anon f_confused "Yeah, is she here?"
    crystal "Oh, yeah she's in there..."
    show anon f_normal
    crystal @ f_eyeroll "Probably yappin' on her phone, as usual."
    crystal "If I didn't know better, I'd swear that thing was glued to the side of that girl's head!"
    anon "Heh, yeah."
    jump crystal_button_outside.choice


label crystal_button_outside.sex:
    show anon a_sides f_shy
    with {'master': dissolve}
    anon "We'll need to be quick!"
    crystal "Now we're cookin' with gasoline!"
    show crystal b_dressed_sitting_beer
    with {'master': dissolve}
    crystal "Mmm!"
    show crystal a_beer_throw b_dressed_sitting
    with {'master': dissolve}
    pause
    show anon f_surprised
    show crystal a_resting
    with {'master': dissolve}
    crystal @ f_burp -m_talk "{i}*Buuuurp*{/i}"
    show crystal a_sides b_dressed:
        xoffset 310
        xzoom -1
    with {'master': dissolve}
    crystal "Now then..."
    show anon a_empty f_shock behind crystal
    show crystal a_grab_anon
    with {'master': dissolve}
    crystal "... Why don't you..."
    show anon a_empty f_surprised:
        xoffset 300
        xzoom 1
    show crystal:
        xoffset 90
        xzoom 1
    with {'master': dissolve}
    crystal "... Have a seat right over here?"
    show anon a_surprised_up f_confused_back_low
    show crystal a_hip
    with {'master': dissolve}
    anon @ -m_talk "Hmm?"
    show anon b_dressed_falling:
        xoffset -30
    show crystal a_push
    with fastdissolve
    pause
    show anon a_down b_dressed_sitting_chair f_shy_cringe:
        xoffset 0
    anon @ -m_talk "!!!" with vpunch
    show anon a_rest f_worried_surprised
    show crystal a_remove01
    with {'master': dissolve}
    crystal "Yer gon' learn somethin' tonight, romeo..."
    show anon f_surprised
    show crystal a_remove02 b_topless_boobless
    with dissolve
    show crystal a_remove03
    with dissolve
    show crystal a_remove04 b_topless
    with {'master': dissolve}
    crystal "... I tell ya what!"
    show crystal b_dressed_back_shake01:
        xoffset 300
        xzoom -1
    with {'master': dissolve}
    crystal "Momma's fixin' ta show you what a real woman can do!"
    show anon f_flirt_low
    show crystal b_dressed_back_shake
    with {'master': dissolve}
    pause
    show crystal b_dressed_back_remove_pants01
    with {'master': dissolve}
    crystal "Yeah, you like that, don'tcha?!"
    show anon f_shy_low
    show crystal b_dressed_back_remove_pants02
    with {'master': dissolve}
    pause
    show anon f_flirt
    show crystal a_hold_pants b_pantless:
        xoffset 50
        xzoom 1
    with {'master': dissolve}
    crystal "You think you can handle this?"
    anon f_shy "Y-yes, ma'am."
    crystal @ f_laugh -m_talk "Heh heh..."
    crystal "... Ya best go on and get that big dick out then!"
    anon f_shy_down "Oh, uhh... right."

    call scene_crystal_sex_trailer.repeat
    $ unlock_scene('Crystal', '02_unlocked')

    scene location_trailer_closeup01_new_evening
    show crystal b_pantless_disheveled f_tired_low:
        xoffset -150

    if _return == 'outside':
        show crystal a_wipe01 o_cum_drip01

    show location_trailer_closeup01_chair as chair
    show anon a_down b_dressed_sitting_chair f_flirt od_firm
    with fade
    crystal "Haaah... Haaah..."

    if _return == 'outside':
        show crystal a_wipe02 o_cum_drip02
        with {'master': dissolve}

    crystal "... I mean, god damn!"
    show anon a_remove_shorts b_dressed f_shy_down:
        xoffset 600
    show crystal f_tired_low_back

    if _return == 'outside':
        show crystal a_idle o_empty

    with {'master': dissolve}
    crystal "That is some fuckin' top shelf dick..."
    show anon a_cover_boner
    show location_trailer_closeup01_chair as chair behind crystal
    show crystal f_smirk:
        xoffset 300
        xzoom -1
    with {'master': dissolve}
    crystal "... I dunno where mah daughter found ya but I sure am glad she did!"
    show anon a_sides b_dressed f_shy:
        xoffset 100
        xzoom -1
    show crystal f_smirk
    with {'master': dissolve}
    anon "Heh, yeah..."
    anon "... Me too."
    show anon a_surprised_up_both f_surprised
    show crystal b_pantless_falling:
        xoffset -50
        xzoom 1
    with {'master': dissolve}
    crystal "Phew!"
    show crystal b_pantless_sitting f_tired:
        xoffset 0
    anon f_worried "You okay?" with vpunch
    crystal @ -m_talk "Mhmm."
    show anon a_sides
    with {'master': dissolve}
    pause
    crystal "Best you get on inside and see to {b}Roxanne{/b} now..."
    crystal f_smirk "... Iffin' ya can fuck her half as good as ya just fucked me..."
    crystal "... We might actually get some decent sleep fer once!"
    anon f_shy "Heh, I'll try."
    crystal f_tired "Atta' boy."
    hide anon
    with {'master': dissolve}
    pause
    crystal "Whew..."
    crystal "... That girl best be fixin' to marry this one, I tell ya what!"
    return 'bliss'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
