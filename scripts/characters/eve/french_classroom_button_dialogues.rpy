label eve_classroom_dialogue_eve_intro:
    scene expression player.location.background_blur with None
    show eve b_desk_look_left f_normal:
        xoffset 500
    show anon b_desk
    with {'master': dissolve}
    eve "Hey, welcome back!"
    anon "Hi, {b}Eve{/b}."
    anon "Wow, I really like the new hair color!"
    show eve a_hair f_laugh with dissolve
    eve "Yeah?"
    show eve f_normal a_idle with dissolve
    eve "I was a little worried I couldn't pull it off..."
    anon @ f_laugh "Oh, you definitely pull it off!"
    eve @ f_laugh "Hehe, thanks, {b}[firstname]{/b}..."
    show eve f_nervous
    pause
    eve f_sad "... Sorry to hear about your dad."
    show anon f_worried
    eve "I know it's rough."
    anon "Yeah."
    eve "If you ever need to talk or something..."
    anon "Nah, it's really nice of you to offer but I'm okay."
    anon "I'm just trying not to think about it."
    anon "Focus on getting back into the swing of things, you know?"
    eve "Yeah, believe me, {b}[firstname]{/b}... I get it."
    show eve f_sad_down
    pause
    eve f_nervous_down "You know, sometimes when I'm feeling down or whatever..."
    eve f_nervous "... I take my drawing pad and sit by this big fountain, over at the park."
    anon f_shy "Oh, yeah?"
    eve "It's so peaceful there, especially in the evenings..."
    anon "Sounds nice."
    eve "It is."
    eve "You should {b}come check it out{/b}, sometime."
    anon f_normal "Alright, maybe I will."
    eve f_laugh "Cool."
    show eve f_nervous_down
    pause
    anon f_worried "So, are you going to take {b}Miss Bissette{/b} up on her private lessons?"
    eve f_confused "Private lessons?"
    anon "Yeah, the ones she was talking about at the start of class..."
    anon "Weren't you paying attention?"
    eve f_laugh "I might have dozed off a bit, haha."
    show eve f_normal
    anon "Really?!"
    eve "Yeah, most of these classes put me to sleep..."
    anon f_shock "But don't you have one of the highest GPAs in school?"
    eve f_nervous "Y-yeah, sorta..."
    anon f_worried "How do you manage that?"
    eve @ f_eyeroll "Oh, I dunno... Just lucky, I guess..."
    anon f_shy "What, that's crazy..."
    eve @ f_laugh "No, I'm serious!"
    eve "I've just always been good at school."
    eve "It's like a gift or something, I can't really explain it."
    anon "Well, it's quite a gift."
    eve f_eyeroll "Yeah, I guess..."
    show eve f_nervous_down
    pause
    show anon f_normal
    pause
    anon "I can curl my tongue."
    eve f_confused "Hmm?"
    show eve f_nervous
    show anon f_unimpressed_tongue
    pause
    anon @ -m_talk "Thee?"
    eve @ f_laugh "Hehe!"
    show eve f_happy
    show anon f_grin
    pause
    anon f_normal "That's really my only gift."
    anon "I'll trade you?"
    eve @ f_laugh "Heh, mmm... Tempting but no."
    anon "Dang."
    show eve f_nervous_down
    show anon f_shy_down
    pause
    show eve f_nervous
    pause
    eve "Seriously {b}[firstname]{/b}, if you ever need a pick me up... {b}Come see me at the park{/b}."
    show anon f_normal zorder 3
    eve @ f_wink "Bring that sense of humor with you."
    anon "Yeah, okay."
    anon "{b}The park in the evening{/b}, huh?"
    eve f_laugh "Yup!"
    show expression "characters/eve/eve_overlay_o_chair.png" zorder 0:
        xpos 450
    show eve f_happy b_dressed zorder 1:
        xoffset -100
    show expression "characters/eve/eve_overlay_o_desk.png" zorder 2:
        xpos 500
    with {'master': dissolve}
    eve "I should get going."
    eve "{b}Miss Ross{/b} had some art project she wanted to talk to me about..."
    anon "Alright."
    show eve a_wave with {'master': dissolve}
    eve "Later, {b}[firstname]{/b}!"
    anon @ f_laugh "See ya!"
    hide eve
    with {'master': dissolve}
    return

label eve_classroom_dialogue_talent_show_help:
    show eve b_desk_look_left:
        xoffset 500
    show anon b_desk f_normal
    anon "Do you play any instruments?"
    eve "No, I don't play any instruments. I've always wanted to learn but I just haven't had the time, you know?"
    anon f_worried "Okay, well, how about singing?"
    eve f_nervous_down "Oh, umm..."
    eve "Yeah, I like to sing I guess... I dunno if I'm any good though."
    if M_eve.finished_state(S_eve_visit_bedroom):
        anon f_normal "Oh, c'mon! I've heard you singing at the park before, you're great!"
        anon "We're really hurting for more volunteers."
        eve "Y-you really think I'm a good singer?"
        pause
        eve f_nervous "I don't know if I can sing in front of the entire school? That sounds pretty embarrassing..."
        eve f_nervous_down @ a_hair "I've never sung for a crowd before."
    else:
        anon f_normal "I bet you are! You should sign up for the talent show with me!"
        anon "We're really hurting for more volunteers."
        eve "Yeah, I dunno."
        eve f_nervous "You want me to sing in front of the entire school? That sounds pretty embarrassing..."
        eve f_nervous_down @ a_hair "... And I haven't sung in a while. Not since my karaoke machine broke."
    eve "I'm quite out of practice."
    anon @ f_thinking -m_talk "Hmm..."
    anon "You know, I think my friend {b}Erik{/b} has a {b}karaoke machine{/b} in his basement."
    eve f_nervous "Oh, yeah?"
    anon "Totally!"
    if M_eve.finished_state(S_eve_visit_bedroom):
        anon "You could practice there and build your confidence up!"
    else:
        anon "You should come over sometime and practice!"
    eve @ f_laugh "Heh, you want me to sing for you and your friend?"
    anon "Nah, we can all sing together! C'mon, we'll do it tonight, it'll be fun!"
    eve f_nervous_down @ -m_talk "..."
    eve f_nervous "Alright, I guess I can stop by for a little while."
    anon @ f_laugh "Awesome!"
    anon "{b}I'll meet you at Erik's house tonight{/b}."
    return

label eve_classroom_dialogue_adehsive:
    show eve b_desk_look_left f_normal:
        xoffset 500
    show anon b_desk f_normal
    anon "What was the plan again?"
    eve "You're supposed to {b}meet Kevin in the science lab after class{/b}."
    eve "Remember?"
    anon "Oh, that's right. Thanks, {b}Eve{/b}!"
    return

label eve_classroom_dialogue_bissettes_reward:
    show eve b_desk_look_left f_normal:
        xoffset 500
    show anon b_desk f_normal
    anon "Are you going to sign up to be tutored by {b}Miss Bissette{/b}?"
    eve "I'm already doing pretty well, so it's not even worth trying."
    anon "Why not?"
    eve f_confused "Well, you can't really improve an A+."
    eve f_nervous "It's more likely she'd pick someone like you..."
    anon "Me?"
    eve "Well, yeah... You're failing right now, aren't you?"
    eve "You've got lots of room for improvement."
    eve "Plus, {b}Miss Bissette{/b} favors boys."
    eve "You should seriously consider it."
    return

label eve_classroom_dialogue_hang_out:
    show eve b_desk_look_left f_nervous:
        xoffset 500
    show anon b_desk f_normal
    if M_eve.finished_state(S_eve_pot_cheerup):
        anon "Do you still hang out at the park?"
        eve "No, {b}I mostly hang around at home in the evenings now{/b}."
    else:
        anon "Where did you say you hung out at?"
        eve "{b}I usually hang out at the park in the evenings{/b}."
    eve "You should swing by sometime."
    anon "Alright, I'll do that."
    eve f_nervous_down "Heh, cool!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
