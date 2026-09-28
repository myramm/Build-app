label ano24_init_liu_lounge:
    scene location_apt_hall2_204_closeup as stage
    show location_apt_hall2_204_closeup_door1 as door behind stage
    show location_apt_hall2_204_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon
    anon @ -m_talk "( This is {b}Liu{/b}'s address. )"
    show anon a_knock with dissolve
    "{i}*Knock* *Knock*{/i}"
    anon a_sides f_worried @ -m_talk "( I hope she was right about {b}Kim{/b} working late. )"
    pause
    liu "Who is it?"
    anon "It's {b}[firstname]{/b}."
    liu "Oh, good."
    show anon f_normal
    liu "One second."
    pause
    show location_apt_hall2_204_closeup_door2 as door with dissolve
    show liu behind doorframe with dissolve
    liu "Hey, {b}[firstname]{/b}."
    anon @ a_wave "Hello."
    pause
    anon f_worried "{b}Kim{/b} isn't here, is he?"
    liu "Nope."
    show anon f_normal
    liu "He usually doesn't get home for another hour or two."
    pause
    liu "Come on in."
    hide liu with dissolve
    anon "Alright, thanks."
    hide anon with dissolve

    scene expression background(400, 400, 2) as stage
    show liu
    with fade
    show anon f_normal_high with dissolve
    anon "Wow, this is nice."
    anon f_normal "I like all the decor."
    liu @ f_laugh "Heh, thanks."
    liu "It took a lot of convincing before {b}Kim{/b} would agree to let me decorate in here."
    anon "Oh, yeah?"
    liu @ f_eyeroll "He still won't let me touch anything in the bedroom..."
    pause
    liu "... And he has awful taste."
    anon @ f_snarky "Heh, I can imagine."
    pause
    anon "So, ehh... anywhere in particular we should start looking?"
    liu f_surprised "Oh, right."
    liu f_curious "Umm."
    liu f_worried "What are we searching for again?"
    anon f_worried "Anything that connects your husband to {b}Mayor Rump{/b} and his illegal activities with the Russians."
    liu f_curious @ -m_talk "Hmm."
    anon "You said he often brings business documents home?"
    liu f_worried "Yeah, but I have no idea where it all ends up."
    anon "So it could be anywhere?"
    liu f_normal "He probably has a million little hiding places that I don't know about."
    anon f_surprised "Yikes, okay..."
    anon f_normal "I guess we should start in here then."
    anon "Just look for anything suspicious, okay?"
    liu "Y-yeah, okay."
    hide anon with dissolve
    hide liu with dissolve
    return


label ano24_seek_bag:
    scene expression background(216, 384, 4.5) as stage
    show anon f_thinking_down a_satchel with dissolve
    anon @ -m_talk "..."
    show liu f_worried with dissolve
    liu "Anything?"
    anon f_confused "Ehh, why does your husband have a bag full of junk food?"
    liu f_confused @ -m_talk "Hmm?"
    anon "Yeah."
    anon f_worried a_satchel_can "There's a bunch of cheese spray cans in here..."
    show liu f_happy
    anon a_satchel f_thinking_down "... And peanut butter..."
    pause
    anon "... And individually packaged snack cakes."
    liu @ f_laugh "Oh, {b}Kim{/b} loves American junk food."
    liu "You can't get that stuff in Korea."
    liu f_worried "He's probably stocking up for our return trip."
    anon "I see."
    show anon f_unimpressed a_up with dissolve
    pause
    anon f_worried a_sides "Ehh, let's see what else we can find."
    jump ano24_seek_check


label ano24_seek_bag.repeat:
    scene expression background(216, 384, 4.5) as stage
    show anon f_unimpressed a_sides with dissolve
    anon @ -m_talk "( Ehh, let's see what else we can find. )"
    hide anon with dissolve
    return


label ano24_seek_case:
    scene expression background(624, 400, 2.5) as stage
    show anon b_dressed_pickup with dissolve
    anon "What about this briefcase?"
    show liu f_normal_down with dissolve
    liu "I don't know... he usually keeps that in his car."
    show liu f_normal
    show anon b_dressed a_briefcase_kim f_surprised_low
    with {'master': dissolve}
    anon "What the-"
    pause
    anon f_worried "It's full of little toys!"
    liu f_confused "Toys?"
    anon "Yeah, it's like transformer action figures..."
    show anon f_worried_low
    pause
    anon "... and some little toy cars..."
    pause
    anon "... And-"
    anon f_surprised_low "Oh my god!"
    liu f_surprised "What is it?!"
    anon f_surprised a_briefcase_kim_pony "He's got little pony dolls."
    liu f_happy @ f_laugh "Oh, yes."
    liu "He's a big collector."
    anon f_worried "... Seriously?"
    liu f_normal "{b}Kim{/b}'s been mailing them back to his estate in Korea for years."
    anon a_briefcase_kim f_worried_low "I-"
    pause
    anon f_worried "I have no words."
    pause
    show liu f_normal_down
    show anon b_dressed_pickup
    with {'master': dissolve}
    anon "Let's just move on."
    show liu f_normal
    show anon f_unimpressed b_dressed a_idle
    with {'master': dissolve}
    liu "Okay."
    jump ano24_seek_check


label ano24_seek_case.repeat:
    scene expression background(624, 400, 2.5) as stage
    show anon f_unimpressed a_sides with dissolve
    anon @ -m_talk "( Let's just move on. )"
    hide anon with dissolve
    return


label ano24_seek_folder:
    scene expression background(720, 376, 3.5) as stage
    show anon f_confused a_point with {'master': dissolve}
    anon "What about that manilla folder?"
    show anon f_normal a_idle with {'master': dissolve}
    liu "Oh, right!"
    liu "Yeah, he was looking over this in bed last night."
    show liu a_folder behind anon with dissolve
    liu "He was really secretive about it too."
    show liu a_folder_give with dissolve
    pause 0.5
    show liu a_idle
    show anon f_normal_low a_folder_kim_closed
    with dissolve
    anon "That sounds promising."
    show anon f_surprised_low a_folder_kim with dissolve
    pause
    anon "Or not."
    liu f_worried "What is it?"
    anon "Feet."
    liu f_confused "Feet?!"
    anon f_worried "Yeah, it's just a bunch of pictures of feet."
    liu f_ashamed_down a_behind "Oh."
    pause
    liu "Umm, he kinda has a thing... for women's feet."
    anon @ f_skeptical "What, like a foot fetish?"
    liu f_worried "Y-yeah."
    show anon f_worried_low
    pause
    anon "But there's men's feet in here too..."
    liu f_surprised "There is?!"
    anon f_worried "... Yeah."
    show liu b_dressed_folder_anon f_worried_down
    show anon b_empty f_worried_low
    with dissolve
    pause
    liu "Oh, my."
    show liu b_dressed_folder_anon_tilt f_surprised_down
    show anon f_surprised_down:
        rotate -22
        xoffset -120
        yoffset -348
    with {'master': dissolve}
    anon "This is weird."
    liu @ -m_talk "..."
    show liu b_dressed f_worried a_idle:
        xoffset -320
    hide anon
    show anon a_folder_kim_closed f_worried
    with dissolve
    anon "Let's just move on."
    show anon a_sides behind liu
    liu a_folder @ f_ashamed_down "Y-yeah, I think that would be best."
    show liu with dissolve:
        xoffset 500
        xzoom -1
    hide liu with dissolve
    jump ano24_seek_check


label ano24_seek_folder.repeat:
    scene expression background(872, 376, 3.5) as stage
    show anon f_unimpressed a_sides with dissolve
    anon "No, I'm putting my foot down... there's no reason to retread that ordeal."
    liu "What was that?"
    show anon a_behind_head f_surprised with {'master': fastdissolve}:
        xoffset -500
        xzoom -1
    anon "Oh, heh, nothing over here!"
    hide anon with dissolve
    return


label ano24_seek_wallet:
    scene expression background(216, 384, 4.5) as stage
    show anon a_wallet f_worried_low with dissolve
    anon @ -m_talk "( Hmm, it looks like {b}Kim{/b} forgot his wallet today... )"
    anon @ -m_talk "( ... I hate it when that happens! )"
    anon f_surprised_low a_wallet_kim @ -m_talk "( Oh, there's fifty bucks inside. )"
    show anon f_worried
    liu "Did you find something?"
    anon "Oh, ehh..."
    show anon f_worried_low a_wallet_think with dissolve

    menu:
        "Take the money.":
            jump ano24_seek_wallet.steal
        "Give the money to {b}Liu{/b}":

            pass

    anon f_normal a_wallet "Yeah."
    pause
    show liu with {'master': dissolve}
    anon "It looks like your husband forgot his wallet this morning."
    anon a_wallet_kim_give "Here."
    anon "It's got fifty bucks inside."
    liu f_worried "Oh, uhh..."
    anon "Take it."
    liu "You really think I should?"
    anon "Why not?"
    pause
    anon @ f_flirt "Call it a douchebag tax."
    liu f_happy @ f_laugh "Heh, you're so funny!"
    show anon a_idle
    show liu a_wallet
    with dissolve
    anon "We should keep looking."
    liu "Yeah, okay."
    hide anon with dissolve
    return False


label ano24_seek_wallet.steal:
    anon f_shy a_wallet "Nah, just an empty wallet."
    anon "We should keep looking."
    liu "Y-yeah, okay."
    show anon f_shy_low
    pause
    show anon a_wallet_money with dissolve
    pause
    hide anon with dissolve
    return True


label ano24_seek_check:
    if not all(M_liu.get('ano24_' + k, 0) for k in ('bag', 'case', 'folder')):
        hide anon with dissolve
        return

    show anon a_sides f_worried with {'master': dissolve}:
        flip
        xoffset -500
    anon @ -m_talk "..."
    show anon with dissolve:
        unflip
        xoffset 0
    anon "Actually, I think that's it for this room."

    if 'liu' not in renpy.get_showing_tags():
        show liu with {'master': dissolve}

    liu "Yeah."
    anon "Where to next?"
    pause
    liu a_behind f_ashamed_down "Oh, umm..."
    liu "... I guess... we should move on to the bedroom next."
    anon f_worried @ f_confused "Is something the matter?"
    show liu f_nervous o_blush with {'master': dissolve}
    liu "N-no, it's just..."
    liu f_ashamed_down "... I'm a little embarrassed."
    anon f_confused @ -m_talk "Hmm?"
    liu "{b}Kim{/b}... he's very... umm..."
    anon "Obnoxious?"
    liu "... Well..."
    show anon f_thinking a_thinking with dissolve
    pause .5
    anon a_point f_snarky "Immoral?"
    anon "Maniacal?"
    liu "... Yes, but-"
    anon a_thinking f_confused "Cocksure?"
    anon f_laugh a_idle "Short?"
    show liu f_surprised o_empty
    show anon f_normal
    with dissolve
    pause
    liu f_laugh "Hehe!"
    anon "Out of shape?"
    liu "Yes, he is all of those things!"
    show liu f_happy
    pause
    liu f_worried "Just try and remember that I had nothing to do with what's behind this door, okay?"
    anon "Heh, I know that, {b}Liu{/b}."
    anon "There's no need to be concerned."
    pause
    anon f_worried "This entire experience has been a very unsettling glimpse into your husband's twisted mind..."
    pause
    show liu f_ashamed_down
    anon f_normal "... How much worse can it get?"
    liu "Yeeeeaah."
    pause
    show liu f_nervous o_blush with {'master': dissolve}
    liu "Just, umm..."
    liu "... Hold that thought."
    hide liu with {'master': dissolve}
    anon f_confused @ -m_talk "..."
    hide anon with dissolve
    return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
