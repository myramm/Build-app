label gra01_init_grace:
    anon f_shy "I was hoping you could give me another massage?"
    grace f_surprised "O-oh?"
    anon "You know, without {b}Odette{/b} this time."
    grace f_uneasy "J-just you and I?"
    anon "Yeah, if that's okay?"
    grace "Mmm, I dunno {b}[firstname]{/b}..."
    show anon f_worried
    pause
    anon "I just thought, you might wanna practice..."
    anon f_shy "... And it felt so good last time..."
    show grace a_cover f_uneasy_back
    with {'master': dissolve}
    grace "{i}*Gulp*{/i} Y-yeah, I know."
    show anon a_give_me f_brag
    with {'master': dissolve}
    anon "And with {b}Odette{/b} downstairs, it won't get sexual."
    show anon a_sides
    with {'master': dissolve}
    grace @ -m_talk "..."
    show grace a_idle f_embarrassed
    with {'master': dissolve}
    grace "Maybe just a little one wouldn't hurt..."
    grace f_uneasy "... For practice."
    anon f_shy "Yeah, just for practice."
    show anon:
        xoffset -500
        xzoom -1
    hide grace
    with {'master': dissolve}
    grace "Why don't you undress and lay down while I'll get the oil ready."
    anon f_normal "Okay!"
    pause
    show anon a_cheering f_grin
    with {'master': dissolve}
    anon "( Sweet! )"

    scene location_tattoo_apartment_oil
    show anon grace_massage_apt roll
    with fade
    pause
    show anon back
    with {'master': dissolve}
    pause
    show anon climb
    with {'master': dissolve}
    pause
    show anon rub pause
    with {'master': dissolve}
    anon "Oh, that's really warm!"
    grace "Heh, yeah..."
    show anon -pause
    with {'master': dissolve}
    grace "... I heated the oil this time."
    anon "Mmm, it smells great too."
    grace "I know, right?"
    grace "Lavender and almond is my absolute favorite!"
    show anon grind
    with {'master': dissolve}
    anon "Okay, phew..."
    anon "... That's really nice."
    grace "Just relax and let yourself go limp."
    anon "O-okay, I'll try."
    pause
    show anon firm
    with {'master': dissolve}
    pause
    show anon hard
    with {'master': dissolve}
    pause .75
    show anon pause
    with {'master': dissolve}
    grace @ -m_talk "!!!"
    grace "Umm, {b}[firstname]{/b}?"
    anon "Yeah?"
    show anon boing
    show grace massage_apt back worried
    with dissolve
    show grace surprised
    grace @ -m_talk "!!!" with hpunch
    show grace worried
    grace "That's the opposite of limp..."
    anon "Sorry."
    anon "I'm trying not to, but this is just-"
    pause
    hide grace
    show anon rub pause
    with {'master': dissolve}
    grace "Heh, it's alright..."
    pause
    grace "... Uhh, why don't we talk about something and get your mind off it?"
    anon "Like what?"
    show anon -pause
    with {'master': dissolve}
    grace "Well, like, how you and my sister doing?"
    anon "Oh, umm... we're great..."
    anon "... She's great!"
    pause
    anon "We have so much fun together..."
    anon "... I can't believe how lucky I am to be with her."
    grace "Heh, I'm pretty sure {b}Eve{/b}'s the lucky one."
    pause
    anon "I've been thinking about taking her to see a concert soon."
    grace "Oh?"
    grace "She'll love that!"
    show anon firm
    with {'master': dissolve}
    anon "Yeah, I think so too."
    pause
    grace "Who are you gonna see?"
    anon "Oh, I dunno."
    anon "Whoever she wants, I guess?"
    grace "Aww, you're such a good guy, {b}[firstname]{/b}!"
    show anon soft
    with {'master': dissolve}
    pause
    anon "Maybe you and {b}Odette{/b} could come too?"
    grace "Oh, uhh... yeah, maybe..."
    grace "... If our schedule opens up a little."
    anon "Work's still busy?"
    grace "Yeah, {i}really{/i} busy."
    pause
    grace "But busy is good!"
    grace "We're caught up on all our bills and I've actually got some money saved up for the first time in..."
    grace "... Well, since before I bought this place!"
    anon "That's great, {b}Grace{/b}!"
    grace "Heh, yeah."
    pause
    grace "It feels good to have some breathing room for once."
    anon "So, your business is finally flourishing, you have disposable income for the first time in your life..."
    anon "... And you're in a caring and committed relationship with your best friend."
    show anon pause
    with {'master': dissolve}
    grace "Y-yeah, I suppose."
    anon "Sounds like everything's going your way."
    pause
    anon "You should buy a lottery ticket or something while your luck is up."
    pause
    show anon sad
    with {'master': dissolve}
    grace "..."
    anon "Why'd you stop?"
    grace "I-"
    show anon peek confused
    with {'master': dissolve}
    anon "Is something wrong?"
    pause
    show anon side
    with {'master': dissolve}
    grace "N-no, it's nothing."
    anon "Are you sure?"
    show anon push
    with {'master': dissolve}
    pause
    show anon back rub normal pause
    with {'master': dissolve}
    pause
    anon "You can talk to me, you know?"
    grace "Well, I-"
    pause
    show anon -pause
    with {'master': dissolve}
    pause
    grace "It's just-"
    grace "{i}*Sigh*{/i} You're right, I should be happy."
    anon "But you're not?"
    grace "No."
    grace "Err, I mean, I don't know..."
    pause
    grace "... Look, don't get me wrong, {b}Odette{/b} and I-"
    pause
    grace "{i}*Sigh*{/i} She's my best friend in the whole world... and I love her, I do..."
    grace "... She's really trying hard lately and I'm thankful for that, but it's-"
    pause
    anon "It's what?"
    grace "{b}Odette{/b} isn't-"
    pause
    grace "{i}*Sigh*{/i} I guess, I'm worried she's going to grow bored of all this..."
    anon "Hmm?"
    grace "... With the job... and the tiny apartment..."
    grace "... And with me."
    anon "What?!"
    anon "Nuh uh..."
    anon "... She's crazy about you, {b}Grace{/b}!"
    grace "{i}*Snort*{/i} Yeah, she says that now..."
    grace "... But commitment has never been her strong suit."
    pause
    grace "And, it's not like we're lesbians, you know?!"
    grace "I don't think I can go the rest of my life without men..."
    grace "... And I know for damn sure she can't!"
    anon "I err-"
    pause
    anon "I mean, it's not like you guys can't find a guy... you know, when the urge to be with one comes."
    show anon pause
    with {'master': dissolve}
    grace "Ugh, that's exactly what {b}Odette{/b} is going to say..."
    grace "... But how is that going to work?!"
    grace "We just go out and pick up some random stranger at some sleezeball bar or something?"
    anon @ -m_talk "..."
    grace "I don't wanna do that!"
    show anon -pause
    with {'master': dissolve}
    pause
    grace "{b}Odette{/b} might be perfectly fine with fucking strangers but I'm just not wired that way!"
    grace "I'm sorry, but I just don't think I can do it!"
    pause
    grace "I need to feel a connection."
    grace "Otherwise, all it's going to do is give me a bunch of anxiety that I don't need."
    pause
    anon "You shouldn't feel sorry because of that..."
    anon "... You're a very intelligent and responsible person, {b}Grace{/b}."
    anon "You know who you are."
    anon "It's one of the things I like most about you."
    show anon pause
    with {'master': dissolve}
    pause
    anon "I mean, you're also driven... and caring..."
    anon "... And {i}insanely{/i} beautiful..."
    show anon sad
    with {'master': dissolve}
    pause
    anon "But a person like you... If you feel like you need a connection, then you do!"
    show anon wipe
    with {'master': dissolve}
    pause
    anon "{b}Grace{/b}?"
    grace "{i}*Sniff*{/i}"
    show anon peek worried
    with {'master': dissolve}
    anon "You okay?"
    show anon side
    with {'master': dissolve}
    grace "Y-yeah, I'm sorry."
    pause
    grace "It's just... really nice to talk to someone about this..."
    grace "... And I-"
    show anon wipe
    with {'master': dissolve}
    grace "{i}*Sniff*{/i}"
    pause
    grace "{b}Eve{/b}'s so lucky she found you."
    grace "{i}*Sniff*{/i}"
    pause
    show anon kiss surprised
    with {'master': fastdissolve}
    grace "!!!"
    pause
    show anon grip
    with {'master': dissolve}
    grace "Mmm."
    show anon flip
    with dissolve
    show anon snog
    with {'master': dissolve}
    pause
    show anon over
    show grace massage_apt over
    with {'master': dissolve}
    anon "Ahh, man..."
    anon "... I'm really sorry, I shouldn't have-"
    anon "We should stop."
    grace "N-no, please... Don't stop."
    anon "Really?"
    hide grace
    show anon snog
    with {'master': dissolve}
    pause
    grace "Mmm."
    pause
    show anon over
    show grace massage_apt over
    with {'master': dissolve}
    anon "H-hey, can I ask you something?"
    grace "Hmm?"
    anon "Did you... feel a connection with me?"
    pause
    anon "You know, when we-"
    anon "The other day, you and I..."
    anon "... With {b}Odette{/b}, we-"
    grace "Yes."
    anon "You did?!"
    grace "Mhmm."
    pause
    hide grace
    show anon snog
    with {'master': dissolve}
    pause

    call scene_grace_sex_apt
    $ unlock_scene('Grace', '02_unlocked')

    scene expression background(o=1) as stage
    with fade
    anon "H-hey, hold on!"
    show grace a_vulnerable b_naked f_sad_down:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    pause
    show grace:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    grace "We can't keep doing this, {b}[firstname]{/b}!"
    grace "This is so wrong, I-"
    show anon b_dressed_changing
    with {'master': dissolve}
    pause
    show anon a_sides b_dressed f_worried
    show grace a_facepalm f_weary
    with {'master': dissolve}
    grace "{i}*Sigh*{/i} We have to tell her... you know that, right?"
    show anon a_surprised f_surprised
    with {'master': dissolve}
    anon "What, like now?!"
    show anon a_sides
    show grace a_hip f_sad
    with {'master': dissolve}
    grace "N-no, not... fuck, I don't know!"
    show grace f_sad_down
    pause
    show anon f_worried
    grace f_uneasy "Look, you should go..."
    anon @ f_confused "Are you sure, because we can talk about this if-"
    show grace a_defensive f_sad
    with {'master': dissolve}
    grace "No, {b}[firstname]{/b}... I just-"
    show anon f_worried_down
    show grace a_vulnerable f_sad_down
    with {'master': dissolve}
    pause
    grace "I need time alone to process all this."
    pause
    anon f_worried "Y-yeah, alright."
    show anon:
        xoffset -500
        xzoom -1
    hide grace
    with {'master': dissolve}
    pause
    show anon a_facepalm f_disgusted_wince
    with {'master': dissolve}
    anon "( Crap... )"
    show anon a_sides f_sad:
        xoffset 0
        xzoom 1
    with {'master': dissolve}
    pause
    hide anon with dissolve

    scene expression background(l=L_tattooparlor_fire_escape, o=1) as stage
    with fade
    show anon f_sad with dissolve
    anon @ -m_talk "( Well, that didn't end the way I wanted it to... )"
    anon @ -m_talk "( ... I hope I didn't just make a big mistake. )"
    pause
    anon f_sad_down "{i}*Sigh*{/i}"
    anon @ -m_talk "( I guess, there's nothing for it now... )"
    anon @ -m_talk "( ... I'll just have to wait and see how things play out. )"
    pause
    anon f_sad @ -m_talk "( It's getting late, I should get home. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
