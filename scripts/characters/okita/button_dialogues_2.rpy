label button_okita_ingredients_mushroom:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "{b}Falicum mushrooms grow in the forest{/b} here in Summerville."
    show okita 3
    okita "They are easy to spot because of their phallic shape."
    show okita 1
    anon @ f_sad_down "... Gross."
    return

label button_okita_ingredients_toad:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "It's breeding season for the {b}Horny Toad{/b}. So look for a {b}pond or stream{/b}."
    okita "They should be easily identifiable by their lumpy purple backsides."
    show okita 1
    anon "Sounds like one ugly frog..."
    return

label button_okita_ingredients_flower:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "The {b}Psychotropic Euphorbia{/b} is a luminescent flower that grows only in dark places."
    okita "Your best bet would be a {b}cave{/b}."
    show okita 1
    anon @ f_thinking a_thinking "Hmm, a {b}cave{/b}..."
    return

label button_okita_ingredients_stock:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "We'll need something mild to act as a base for the serum. Vegetable stock would work best."
    okita "You should be able to pick some up at Consum-R."
    show okita 1
    anon "... At least one of the ingredients is simple."
    return

label button_okita_ingredients_tissue:
    scene location_school_science_closeup
    show anon f_worried
    show okita 2 at right
    okita "A hair or saliva sample would work best."
    show okita 1
    anon @ f_skeptical "Yeah, okay, but how am I supposed to get that?"
    show okita 9
    okita "... I'm sure you'll think of something."
    show okita 4
    anon @ f_sad_down -m_talk "..."
    return

label button_okita_got_all_ingredients:
    scene location_school_science_closeup
    show anon
    show okita 1 at right
    with dissolve
    anon "Alright ma'am, I think I've got everything."
    show okita 3
    okita "... You think?"
    show okita 1
    hide anon
    show player 533 at left
    with dissolve
    anon "Well, there is one little issue..."
    show okita 3
    show player 532
    okita "... Is that chicken stock?"
    show player 533
    show okita 1
    anon "Yeah. It's all Consum-R had..."
    anon "I thought, maybe chicken stock would still work?"
    show player 532
    show okita 2b
    okita "Hah, yeah. That should be fine..."
    hide player
    show anon f_worried
    with dissolve
    show okita 6
    anon @ -m_talk "..."
    show okita 7
    okita "Looks like everything else is in order."
    okita "Meet me in my office this evening, and we'll start mixing."
    show okita 6
    anon "Tonight?"
    show okita 3
    okita "Problem?"
    show okita 4
    anon "No! ... No. I'll see you then."
    return

label button_okita_extract_cum:
    scene location_school_science_closeup
    show anon f_worried
    show okita 4 at right
    anon "So, we have everything we need to make your serum?"
    show okita 5
    okita "... Uhh, yeah. Isn't that what I just told you?!"
    okita "{b}Meet me in my office this evening{/b}, and so we can work on it."
    show okita 4
    anon "... O-okay."
    return

label button_okita_dose_smith:
    scene location_school_science_closeup
    show anon
    show okita 5 at right
    with dissolve
    okita "You still haven't dosed {b}Mrs. Smith{/b}?!"
    show okita 4
    anon f_sad_down @ -m_talk "..."
    show okita 5
    okita "What are you waiting for?"
    show okita 4
    anon f_worried "This isn't exactly easy you know!"
    anon "Can't you give me some advice or something?!"
    show okita 3
    okita "Here's some advice: hurry up and do it already!"
    show okita 5
    okita "All you have to do is {b}slip it into her food or something{/b}."
    show okita 4
    anon @ f_skeptical "Alright, alright. I'll be back."
    return

label button_okita_wait_for_smith_serum:
    scene location_school_science_closeup
    show anon
    show okita 6 at right
    anon "Alright, {b}Miss Okita{/b}. It's done."
    show okita 7
    okita "Wonderful!"
    okita "Now we just wait to see the effects..."
    show okita 6
    anon "How long should it take?"
    show okita 7
    okita "It'll work fast. Why don't you stick around, and we'll check on her after class?"
    show okita 6
    anon "Sure."
    pause 1
    scene black with dissolve
    scene location_school_lounge_day_blur
    show okita 5f zorder 1 at Position(xpos=0.3, ypos=1.0)
    show anon f_worried zorder 0:
        xoffset -100
    show principal 33 at right
    with dissolve
    okita "{i}*Ahem*{/i}"
    show okita 4f
    show principal 32 with dissolve
    smith "Hmm? Oh, hello there {b}Tori{/b}..."
    smith "How's little Miss Know-it-all today?"
    show principal 31
    okita "... Hmmph."
    show okita 3f
    okita "I was just checking on the status of my office?"
    show okita 4f
    show principal 32
    smith "Your office?"
    show okita 5f
    show principal 31
    okita "Well, the other day you seemed pretty adamant about changing the locks."
    show okita 4f
    show principal 32
    smith "Was I?"
    smith "That's funny... I don't recall."
    show okita 3f
    show principal 31
    okita "Oh, really?"
    smith "..."
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smith "Bawk bawk."
    show principal 31 at right with dissolve
    show okita 8f
    okita "..."
    show okita 3f
    okita "... Are you alright?"
    show okita 4f
    show principal 32
    smith "... Huh?"
    smith "I'm fine, why?"
    show okita 5f
    show principal 31
    okita "You were saying something, regarding the lock on my office?"
    show okita 4f
    show principal 32
    smith "Was I?"
    smith "That's funny... I don't-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smith "BAWK!!! Bawk bawk bawk..."
    show principal 31 at right with dissolve
    show okita 6f
    anon "Uhh..."
    show okita 9f
    okita "Shh!"
    show principal 33 with dissolve
    okita "Don't interrupt us {b}[firstname]{/b}."
    show okita 4f
    show principal 32 with dissolve
    smith "... This coffee tastes funny."
    show principal 31
    anon @ -m_talk "..."
    show okita 7f
    okita "Did I tell you about the new invention I was working on?"
    show okita 6f
    show principal 32
    smith "Invention?"
    smith "No, I don't think yo-"
    show principal 30b at Position(xpos=0.95, ypos=1.0) with dissolve
    smith "Bawk bawk..."
    smith "Bawk bawk BAWK!!"
    show principal 31 at right with dissolve
    show okita 7f
    okita "I'll have to bring it by your office sometime. It's really fascinating!"
    show principal 32
    show okita 6f
    smith "Sure, okay!"
    show okita 7f
    show principal 31
    okita "Oh my, look at the time."
    okita "We should really be going."
    show okita 7 at Position(xpos=0.05, ypos=1.0) with dissolve
    okita "Come along, {b}[firstname]{/b}."
    hide okita with dissolve
    anon @ -m_talk "..."
    show principal 32
    hide anon with dissolve
    smith "... This coffee tastes funny."
    scene black with dissolve
    scene location_school_science_closeup
    show anon f_worried
    show okita 7 at right
    okita "So, I guess that {b}chicken stock{/b} created a bit of a side effect after all..."
    show okita 2b
    okita "Pffft, hahaha!!"
    show okita 6
    anon @ f_skeptical "How is this funny?!"
    anon "We screwed with her head, and she's in there clucking like a chicken!"
    show okita 2b
    okita "Yeah she is! Hahaha!"
    show okita 7
    okita "Oh, would you relax?"
    okita "It's only temporary."
    show okita 9
    okita "... I think."
    show okita 6
    anon f_surprised "You think?!"
    show okita 9
    okita "I mean, I'm pretty sure."
    show okita 7
    okita "Look the important thing here is that the serum worked!"
    okita "She's completely impartial to my experiments now!"
    okita "... And she didn't even remember wanting to lock me out of my office!"
    show okita 6
    anon f_worried "Yeah, but she's clucking like a chicken!"
    show okita 2b
    okita "Pffftt, hahahaaaah!"
    anon @ f_skeptical "Well, I'm glad you think it's so funny..."
    show okita 6
    anon "So, what now?"
    show okita 7
    okita "Now, I need some time to study the effects of the other serum."
    show okita 6
    anon "Oh, I completely forgot about the other serum!"
    anon "Are you feeling any different?"
    show okita 7
    okita "Mmm, maybe..."
    show okita 2b
    okita "Hehehe!"
    anon "You do seem kinda, different."
    show okita 7
    okita "How so?"
    show okita 6
    anon f_skeptical "You're like... Giddy."
    show okita 2b
    okita "Hehehe! I'm just happy."
    anon f_worried "It's kinda freaking me out to be honest."
    show okita 7
    okita "... And hot."
    show okita 3
    okita "Are you hot? It's hot in here!"
    show okita 6
    anon "No, I'm fine."
    show okita 7
    okita "Alright, well, I'm gonna head up to my office and get some work done."
    okita "Come see me in a few days."
    show okita 6
    anon "Umm, okay."
    show okita 2b
    okita "Byeee, {b}[firstname]{/b}!"
    okita "Hehehehe..."
    hide okita with dissolve
    anon "I hope she's gonna be okay..."
    return

label button_okita_wait_for_okita_serum:
    scene location_school_science_closeup
    show anon f_worried
    show okita 6 at right
    with dissolve
    anon "You doing okay, ma'am?"
    anon "Notice any side effects with your serum yet?"
    show okita 7
    okita "I'm still testing."
    okita "... I appreciate you checking in with me though."
    show okita 6
    anon "... You do?"
    show okita 7
    okita "Of course!"
    show okita 2b
    okita "It makes me feel all warm and fuzzy!"
    show okita 6
    anon @ -m_talk "..."
    anon f_skeptical "Okay, seriously! You are acting really weird!"
    show okita 7
    okita "Am I?"
    show okita 2b
    okita "I don't know what to tell you. I feel great!"
    show okita 6
    anon f_worried "Okay, well, just be careful, I guess."
    show okita 7
    okita "Will do, handsome!"
    show anon f_surprised
    show okita 2b
    okita "Hehehe!"
    anon f_worried @ f_sad_down a_behind_head "..."
    return

label button_okita_serum_effects:
    scene location_school_science_closeup
    show anon f_worried
    show okita 6 at right
    with dissolve
    anon "Any results from the serum yet?"
    show okita 7
    okita "Actually, {b}[firstname]{/b}, I was hoping you could help me test my newest invention?"
    show okita 6
    anon "Oh man, you want me to build something else?"
    show okita 3
    okita "Hmm? No, no!"
    show okita 7
    okita "I built this one myself. It's revolutionary!"
    show okita 6
    anon "You built it?"
    anon "But building is monkey work. I thought you didn't do monkey work?"
    show okita 7
    okita "I made an exception this time because..."
    okita "Well, I made this invention for you, as a surprise."
    show okita 6
    anon "For me?"
    show okita 7
    okita "Yeah, come to my office this evening after school and I'll show you."
    show okita 7
    anon "This is starting to worry me..."
    anon "What are you up to?"
    show okita 2b
    okita "Don't be a baby! You have to come and see!"
    show okita 6
    anon "Fine."
    show okita 7
    okita "You promise?"
    show okita 6
    anon f_skeptical "Uhh, yeah."
    anon "... I promise."
    show okita 2b
    okita "Yay!"
    show okita 7
    okita "See you soon, {b}[firstname]{/b}!"
    hide okita with dissolve
    anon f_worried @ f_sad_down "..."
    return

label button_okita_generic_after_q3:
    call expression game.dialog_select("button_okita_generic_after_q3_intro")
    menu:
        "New invention." if M_okita.is_state(S_okita_is_hypersexual):
            call expression game.dialog_select("button_okita_generic_after_q3_new_invention")
        "Nothing.":

            call expression game.dialog_select("button_okita_generic_after_q3_leave")
    return

label button_okita_generic_before_q3:
    scene location_school_science_closeup
    show anon
    show okita 4 at right
    with dissolve
    anon "Hey, {b}Miss Okita{/b}."
    show okita 5
    okita "What is it, {b}[firstname]{/b}?"
    okita "I'm very busy..."
    show okita 4
    return

label button_okita_generic_after_q3_intro:
    scene location_school_science_closeup
    show anon
    show okita 6 at right
    with dissolve
    anon "Hey, {b}Miss Okita{/b}."
    show okita 2b
    okita "{b}[firstname]{/b}!"
    show okita 7
    okita "How nice of you to visit!"
    okita "What can I help you with?"
    show okita 6
    return

label button_okita_generic_after_q3_new_invention:
    show anon f_normal
    anon "So, you've been working on a new invention, huh?"
    show okita 7
    okita "Oh, yes!"
    okita "It's revolutionary! You absolutely have to come and see it!"
    show okita 6
    anon "Heh, okay! I'll {b}meet you in your office this evening{/b}."
    show okita 2b
    okita "You have to promise you'll come and see!"
    show okita 6
    anon f_skeptical @ -m_talk "..."
    anon "... Yeah. I promise."
    show okita 2b
    show anon f_worried
    okita "I can't wait!"
    return

label button_okita_generic_after_q3_leave:
    show anon f_normal
    anon "Nothing, I just wanted to say hi!"
    show okita 5
    okita "That's nice of you."
    okita "Although, I'm busy working on some new designs at the moment."
    show okita 7
    okita "Come see me in my {b}classroom{/b} if you want to help me."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
