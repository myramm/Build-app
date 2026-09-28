label button_eve_talent_show_help:
    anon f_worried "Do you play any instruments?"
    eve "No, I don't play any instruments. I've always wanted to learn but I just haven't had the time, you know?"
    anon "Okay, well, how about singing?"
    eve f_nervous_down "Oh, umm..."
    eve @ f_nervous "Yeah, I like to sing I guess... I dunno if I'm any good though."
    anon f_normal "I bet you are! You should sign up for the talent show with me!"
    anon "We're really hurting for more volunteers."
    eve f_nervous "... Yeah, I dunno."
    eve @ f_confused "You want me to sing in front of the entire school? That sounds pretty embarrassing..."
    eve "... And I haven't sung in a while. Not since my karaoke machine broke."
    eve "I'm quite out of practice."
    anon @ f_thinking a_thinking "Hmm..."
    anon "You know, I think my friend {b}Erik{/b} has a {b}karaoke machine{/b} in his basement."
    eve "Oh, yeah?"
    anon @ f_laugh "Totally!"
    anon "You should come over sometime and practice!"
    eve f_happy @ f_laugh "Heh, you want me to sing for you and your friend?"
    anon "Nah, we can all sing together! C'mon, we'll do it tonight, it'll be fun!"
    eve f_nervous_down @ -m_talk "..."
    eve f_happy @ f_eyeroll a_wtf "Alright, I guess I can stop by for a little while."
    anon "Awesome! {b}I'll meet you at Erik's house tonight{/b}."
    return

label button_eve_ross_find_art_pad:
    anon "I need to ask you for a favor."
    eve f_confused "Oh?"
    anon "You see, I'm kinda helping {b}Miss Ross{/b} with something, and we need your art pad."
    eve f_normal "Well, that's no problem."
    eve "You just have to {b}help me find my backpack{/b} first."
    anon f_worried "You lost your backpack?"
    eve f_nervous_down "Yeah..."
    eve f_normal "My art pad should be inside it."
    anon "Where was the last place you remember having it?"
    eve @ f_sad_thinking "Hmm..."
    eve "Well, I think {b}I had it when I went to hang out with the guys in the park last night{/b}."
    anon f_normal "Alright, I'm on it!"
    return

label button_eve_ross_find_eve_backpack_have_backpack:
    hide anon
    show player 610 at left
    with dissolve
    anon "Look what I found!"
    show player 609
    eve f_happy @ f_laugh "Niiiice!"
    hide player
    show anon
    with dissolve
    eve "Thanks, {b}[firstname]{/b}!"
    anon "No worries. I couldn't find your art pad though."
    eve f_confused "It wasn't in my bag?"
    anon "Nope."
    eve f_normal "Weird."
    eve @ f_confused "I wonder if {b}Chad{/b} snatched it again?"
    anon f_worried "{b}Chad{/b}?"
    eve "Yeah, he digs my art."
    anon "Interesting..."
    anon f_normal "I'll go ask him."
    eve "Cool. See ya, {b}[firstname]{/b}."
    anon "See ya, {b}Eve{/b}."
    return

label button_eve_ross_find_eve_backpack_no_backpack:
    anon f_normal "Where did you leave your backpack, again?"
    eve @ f_confused "I'm not entirely sure. I remember having it with me {b}at the park{/b} last night."
    anon "Okay, I'll check there!"
    return

label button_eve_ross_get_eve_drawing:
    anon f_worried "Where did you say that art pad was again?"
    eve @ f_eyeroll "Oh, {b}Chad probably has it{/b}."
    eve "He digs my art."
    anon f_normal "Gotcha, thanks!"
    return

label button_eve_ask_model:
    anon f_normal "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    anon "Would you be interested?"
    eve "Modeling? That could be fun."
    anon "Really?! Awesome! I was hoping you would say that!"
    eve "Yeah, I don't mind."
    eve @ f_laugh "It's a good thing I wore this cute outfit today."
    anon f_worried "... Oh, umm. It would be nude modeling."
    eve f_surprised a_rossed "Nude?!"
    eve "Oh, hell no!"
    show eve f_nervous_down
    anon "So you won't do it? I thought you were into artsy stuff?"
    eve f_surprised "Yeah, but that doesn't mean I'm into public nudity!"
    show eve f_nervous
    anon "Good point. Sorry."
    eve "It's alright. Just not interested."
    anon f_normal @ a_wave "Well, thanks anyways..."
    return

label button_eve_ross_get_paint:
    anon f_normal "I'm looking for some paint. Any idea where I could find some?"
    show eve f_confused a_idle
    eve "I dunno, maybe try a store?"
    show eve f_normal
    anon "Well, yeah, I know... Duh, right?"
    anon "But this paint is for {b}Miss Ross{/b}, and she can't afford to buy it."
    eve @ f_laugh "Oh, hehe."
    eve "Hmm, free paint. That's a toughie..."
    anon "Tell me about it..."
    eve @ a_point "We could try asking my sister."
    if M_eve.finished_state(S_eve_visit_bedroom):
        anon "You think {b}Grace{/b} would give me some?"
        eve f_happy "Well, she probably won't just give it to you..."
        eve "... But I'm sure you two can work something out."
        anon "That would be a big help!"
        eve "We can ask her after school if you want?"
        anon @ f_confused "I'll just meet you at {b}Sugar Tats{/b} then?"
        eve "Sure, that works."
    else:
        anon "She's a tattoo artist, right?"
        eve f_happy "She's the best tattoo artist!"
        eve "You should check out her work, it's amazing!"
        anon "You think she would let me have some paint?"
        eve "We can go ask her."
        anon @ f_skeptical "Isn't her parlor called {b}Sugar Tats{/b}?"
        eve "Yuuuup. It's {b}on the north side of town{/b}."
    anon "Alright, I'll meet you there!"
    return

label button_eve_ross_get_paint_grace:
    anon @ f_worried "Where's your sister's parlor again?"
    eve f_happy "{b}Sugar Tats{/b}? It's on the {b}North{/b} side of town."
    anon "Okay, {b}I'll meet you there{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
