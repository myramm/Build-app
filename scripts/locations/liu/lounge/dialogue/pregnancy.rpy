label liu_lounge_liu_pregnancy_first:
    scene location_apt_hall2_204_closeup as stage
    show location_apt_hall2_204_closeup_door1 as door behind stage
    show location_apt_hall2_204_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock f_worried with dissolve
    "{i}*Knock* *Knock*{/i}"
    show anon a_sides with dissolve
    anon @ -m_talk "( Hmm, I've got a bad feeling... )"
    show location_apt_hall2_204_closeup_door2 as door behind stage with dissolve
    show liu a_shy b_robe_hair f_frightened o_tears behind doorframe with dissolve:
        xoffset -70
    pause
    liu "H-hey, {b}[firstname]{/b}."
    anon f_confused "Hey."
    anon "What's going on?"
    liu f_worried_down "It's umm..."
    show liu a_cover f_crying with dissolve
    pause
    show anon a_empty b_empty f_surprised
    show liu b_robe_hug:
        xoffset 0
    with dissolve
    anon "!!!"
    liu "I'm such an idiot!"
    anon f_confused "Huh?"
    liu "Everything was so perfect and I screwed it up!"
    anon "I don't understand... What's happened, {b}Liu{/b}."
    show anon a_handshake b_dressed behind liu
    show liu a_wipe_tears b_robe_hair behind doorframe:
        xoffset -250
    with dissolve
    liu "{i}*Sniff*{/i} You'd better come inside."
    anon f_worried "Alright."
    hide anon
    hide liu
    with dissolve

    scene expression background(400, 400, 2) as stage with fade
    show anon a_sides f_worried:
        xoffset 125
    show liu a_shy b_robe_hair f_worried_down o_tears:
        xoffset -125
    with dissolve
    anon "Are you gonna tell me what's going on?"
    liu f_crying "I'm pregnant."
    anon a_surprised f_shock "!!!" with hpunch
    anon f_surprised "You're pregnant?!"
    show anon a_sides
    show liu b_robe_cry
    with {'master': dissolve}
    liu "I know!"
    liu "I should have been more careful with my contraceptives and I'm so stupid..."
    show liu a_cover b_robe_hair f_worried
    with {'master': dissolve}
    liu "... P-please, don't leave me!"
    anon f_shock "Leave you?!"
    show anon f_surprised
    liu "I'm gonna make an appointment tomorrow and get it taken care of, I promise!"
    show anon a_up f_worried with {'master': dissolve}
    anon "Well, wait a second..."

    menu:
        "I'm not going to leave you.":
            jump liu_lounge_liu_pregnancy_first.support
        "Why don't we keep it?":

            pass

    show anon a_sides f_normal with {'master': dissolve}
    anon "... Why don't we keep it?"
    liu a_mouth_cover f_surprised "!!!" with hpunch
    liu "You're serious?"
    anon "Absolutely!"
    anon f_worried "You don't want it?"
    show liu a_cover f_nervous with {'master': dissolve}
    liu "N-no, I do... more than anything!"
    anon f_happy "Then let's keep it."
    pause
    show liu a_shy f_confused with {'master': dissolve}
    liu "You're not mad?"
    anon f_confused "Why would I be mad?"
    liu f_frightened "Well, because {b}Kim{/b} said-"
    show anon a_up f_annoyed with {'master': dissolve}
    anon "Okay, stop right there."
    show liu f_confused_down
    anon "You should just forget everything {b}Kim{/b} ever told you..."
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "... He was a total scumbag."
    show liu f_worried
    anon f_normal "Babies are a good thing, {b}Liu{/b}..."
    anon "... And I think you're gonna make a great mom."
    liu f_happy "Y-you do?"
    anon "Definitely."
    pause
    show anon a_empty b_empty f_normal_closed
    show liu b_robe_hug behind anon:
        xoffset 125
    with dissolve
    anon "Heh!"
    liu "You are the most wonderful man in the entire world!"
    anon f_shy_low "Aww, c'mon..."
    liu "No, I'm serious!"
    show anon a_sides b_dressed f_normal
    show liu a_wipe_tears b_robe_hair f_happy:
        xoffset -125
    with dissolve
    liu "How did I get so lucky?"
    show liu a_shy o_empty
    with dissolve
    pause
    liu f_sexy "I love you, {b}[firstname]{/b}."

    menu liu_lounge_liu_pregnancy_first.merge:
        "I love you too.":
            call liu_lounge_liu_pregnancy_first.love
        "Thank you.":

            call liu_lounge_liu_pregnancy_first.thank

    anon f_happy "Hey, we should celebrate!"
    anon f_normal "Why don't we have a sit down and some of that delicious tea?"
    liu "Y-yeah, okay."
    show anon a_sides f_thinking
    hide liu
    with {'master': dissolve}
    anon "We have to start thinking of baby names..."
    hide anon with {'master': dissolve}
    anon "... Do you have any ideas?"

    scene expression background(l=L_apt_hall2, o=1) with longfade
    show anon f_thinking with dissolve
    anon @ -m_talk "( Well, it looks like I'm going to be a father soon. )"
    anon f_happy @ -m_talk "( How exciting is that?! )"
    pause
    anon f_thinking_down @ -m_talk "( I'll have to check in with {b}Liu{/b} more often and make sure she doesn't want for anything during the pregnancy. )"
    hide anon with dissolve
    return True


label liu_lounge_liu_pregnancy_first.love:
    anon f_normal "I love you too, {b}Liu{/b}."
    hide anon
    show liu b_robe_kiss:
        xoffset 0
    with dissolve
    pause
    liu "Mmm."
    pause
    show anon a_handshake b_dressed f_normal behind liu:
        xoffset -50
    show liu a_shy b_robe_hair f_happy:
        xoffset -300
    with dissolve
    return


label liu_lounge_liu_pregnancy_first.support:
    show anon a_sides f_normal with {'master': dissolve}
    anon "... I'm not going to leave you."
    liu f_surprised "Y-you're not?"
    anon f_annoyed "No!"
    anon f_confused "Why would I leave, {b}Liu{/b}?"
    show liu a_shy f_frightened with {'master': dissolve}
    liu "Well, because {b}Kim{/b} said-"
    show anon a_up f_annoyed with {'master': dissolve}
    anon "Okay, stop right there."
    anon "You should just forget everything {b}Kim{/b} ever told you..."
    show anon a_sides f_worried
    with {'master': dissolve}
    anon "... He was a total scumbag."
    pause
    liu f_nervous "{i}*Sniff*{/i} S-so you're not mad?"
    anon f_normal "Of course not."
    show anon a_empty b_empty f_surprised
    show liu b_robe_hug behind anon:
        xoffset 125
    with dissolve
    pause
    anon f_normal_low "Aww, c'mon..."
    anon "... Everything's going to be fine."
    anon "We'll just have to be more careful in the future, yeah?"
    show anon a_sides b_dressed f_normal
    show liu a_shy b_robe_hair f_nervous:
        xoffset -125
    with dissolve
    liu "Y-yeah, no... absolutely!"
    liu "I'll be much more careful in the future, I promise!"
    show anon a_empty b_empty f_shy_low
    show liu b_robe_hug:
        xoffset 125
    with dissolve
    liu "{i}*Sniff*{/i} Thank you for being so understanding..."
    pause
    liu "... And for not leaving me."
    anon f_normal_closed "I could never just leave you, {b}Liu{/b}."
    pause
    show anon a_sides b_dressed f_normal
    show liu a_shy b_robe_hair f_nervous:
        xoffset -125
    with dissolve
    anon "Do you want me to go with you to the clinic tomorrow?"
    liu f_nervous_back "O-oh, no... don't be silly."
    show liu f_nervous
    anon "I really don't mind."
    liu "No, no... it was my screw up..."
    liu "... I'll take care of it."
    anon "C'mere."
    show anon a_empty b_empty f_normal_closed
    show liu b_robe_hug:
        xoffset 125
    with dissolve
    pause
    anon f_shy_low "You're very important to me, you know?"
    liu "I love you, {b}[firstname]{/b}."

    menu:
        "I love you too.":
            call liu_lounge_liu_pregnancy_first.love
        "Thank you.":

            call liu_lounge_liu_pregnancy_first.thank

    anon f_normal "Why don't we have a sit down and a nice cup of tea, huh?"
    anon "Calm your nerves a little bit?"
    liu "Y-yeah, okay."
    anon "I'm always gonna be here for you, alright?"
    hide anon
    hide liu
    with dissolve
    anon "No matter what."

    scene expression background(l=L_apt_hall2, o=1) with longfade
    show anon f_worried with dissolve
    anon @ -m_talk "( Phew, that poor girl... )"
    anon @ -m_talk "( ... all those years living with {b}Kim{/b} really did a number on her. )"
    anon @ -m_talk "( I hate seeing her upset like that. )"
    pause
    anon f_normal @ -m_talk "( Well, at least she's feeling better now. )"
    anon @ -m_talk "( I should get back to it. )"
    hide anon with dissolve
    return


label liu_lounge_liu_pregnancy_first.thank:
    anon f_shy "O-oh, that's umm..."
    show anon a_sides b_dressed
    show liu a_sides b_robe_hair f_worried:
        xoffset -125
    with dissolve
    pause
    anon f_shy_left "... Thank you."
    show liu f_worried_down
    pause
    show liu f_worried
    return


label liu_lounge_liu_pregnancy:
    scene location_apt_hall2_204_closeup as stage
    show location_apt_hall2_204_closeup_door1 as door behind stage
    show location_apt_hall2_204_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock f_worried with dissolve
    "{i}*Knock* *Knock*{/i}"
    show anon a_sides with dissolve
    pause
    show location_apt_hall2_204_closeup_door2 as door behind stage with dissolve
    show liu a_shy b_robe_hair f_nervous behind doorframe with dissolve:
        xoffset -70
    pause
    liu "H-hey, {b}[firstname]{/b}."
    anon "Hey."
    liu "Come on in."
    hide liu with dissolve
    hide anon with dissolve

    scene expression background(400, 400, 2) as stage with fade
    show anon a_sides f_worried:
        xoffset 125
    show liu a_shy b_robe_hair f_worried:
        xoffset -125
    with dissolve
    anon "What's going on?"
    liu f_worried_down "Well, umm..."
    liu "... I think, I might be... pregnant... again."
    show liu f_ashamed_down
    anon f_surprised "!!!"
    anon "Again?!"
    liu f_frightened "I know we agreed to be more careful... and I really have been, I swear!"
    liu "This shouldn't have happened!"
    anon f_normal "Heh, it's fine {b}Liu{/b}..."
    show liu f_nervous
    anon "... Remember what I told you last time?"
    anon f_happy "Babies are good thing."
    anon "You don't have to be stressed out about telling me."
    pause
    show liu b_robe_hug behind anon:
        xoffset 125
    show anon a_empty b_empty f_surprised
    with dissolve
    pause
    anon f_normal_closed "Heh!"
    liu "You are the most wonderful man in the entire world!"
    anon f_shy_low "Aww, c'mon..."
    liu "No, I'm serious!"
    show anon a_sides b_dressed f_normal
    show liu a_shy b_robe_hair f_nervous:
        xoffset -125
    with dissolve
    liu "How did I get so lucky?"
    show liu f_happy
    pause
    liu f_sexy "I love you, {b}[firstname]{/b}."
    jump liu_lounge_liu_pregnancy_first.merge
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
