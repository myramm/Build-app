label ano24_find_liu_bedroom:
    scene expression background(240, 400, 3.5) as stage
    show liu f_ashamed_down with dissolve:
        xoffset -350
    pause
    show liu f_worried_down with dissolve:
        xoffset 400
        xzoom -1
    show anon f_normal_left behind liu with dissolve:
        xoffset -350
        xzoom -1
    pause
    anon a_surprised f_surprised_high "!!!" with hpunch
    anon "Wow."
    show liu f_worried with {'master': dissolve}:
        xoffset -100
        xzoom 1
    liu "Yeeeeaah."
    show anon a_sides with {'master': dissolve}
    anon "This is-"
    pause
    anon "Wow."
    liu f_ashamed_down "Yeeeeaah."
    show anon a_sides f_confused with {'master': dissolve}:
        xoffset 150
        xzoom 1
    anon "He built a statue of himself?"
    show liu f_worried o_blush with {'master': dissolve}
    liu "Ehh, more of a shrine, really..."
    anon f_worried @ f_surprised "That's even worse!"
    pause
    anon "What kind of sick person creates something like this?"
    liu "My husband."
    anon @ a_behind_head "Oh, right."
    anon "Sorry... I didn't mean-"
    liu f_nervous "N-no, you're right."
    pause
    liu "I tried to warn you."
    show anon f_surprised_high with dissolve:
        xoffset -350
        xzoom -1
    anon "Yeah, you did... it's just-"
    pause
    anon "Not in my wildest dreams could I have imagined..."
    show liu f_ashamed_down
    pause
    anon "... There's just no words."
    pause
    show anon f_worried a_frustrated with dissolve:
        xoffset 150
        xzoom 1
    anon "I mean, anyone who could design something like this... is clearly unwell in the head."
    show anon a_idle with dissolve
    liu "Yeeeeaah."
    liu f_annoyed "Believe me, I hate it!"
    liu "I've begged him a million times to let me change it but he's steadfast about keeping it."
    pause
    liu @ f_eyeroll "Calls it his, \"Fortress of Solitude.\""
    pause
    anon "How do you sleep in here?"
    liu f_worried @ -m_talk "Hmm?"
    show liu behind anon
    anon a_point_back "I mean, with this thing in the room... there's no way I could sleep."
    show liu f_ashamed_down
    show anon f_surprised_high a_idle:
        xoffset -350
        xzoom -1
    with dissolve
    pause
    anon "It's like, the eyes follow me wherever I go."
    liu "I try not to think about it."
    pause
    show anon f_worried with dissolve:
        xoffset 150
        xzoom 1
    anon "We should start looking for that evidence and get out of here."
    liu f_worried "Y-yeah, okay."
    anon f_grin @ f_snarky "Just promise me you're going to redecorate in here the second the cops take him away..."
    liu f_nervous @ f_laugh "Hehe, I promise!"
    anon f_normal "Phew, thank god for that."
    liu "In fact, {b}Frank{/b} found this amazing painting for me that will look great in-"
    liu f_surprised a_mouth_cover "!!!"
    show anon f_worried
    liu f_ashamed_down a_behind "I uhh... never mind."
    anon "No, it's okay."
    anon "{b}Dad{/b} bought you a painting?"
    liu f_nervous "Y-yeah."
    liu "It didn't mean anything though, {b}[firstname]{/b}..."
    liu "... Not like you're probably thinking."
    anon @ f_confused -m_talk "Hmm?"
    liu f_worried "He was just being kind, you know?"
    liu "Trying to keep my spirits up."
    pause
    liu "It was meant for my new place..."
    liu "... Once I was free of {b}Kim{/b}."
    anon f_sad_down "{b}Dad{/b} was always good at cheering people up."
    liu f_nervous "He was."
    pause
    anon f_worried "Can I see it?"
    liu f_worried @ f_surprised "What, the painting?"
    pause
    liu "Umm, sure."
    liu f_nervous "Y-yeah, of course!"
    liu "It's not here though."
    anon @ f_confused "Oh?"
    liu "I couldn't bring it home, you know... because of {b}Kim{/b}."
    anon f_shy "Right."
    anon f_normal "No, that makes sense."
    show liu f_normal o_empty a_idle with dissolve
    liu "But you can come by the bank and see it anytime you'd like!"
    anon "Okay, I will."
    liu "Cool."
    pause
    anon f_worried "Say, {b}Liu{/b}..."
    anon "... Could you tell me anything more about {b}Dad{/b}?"
    liu f_nervous @ -m_talk "Hmm?"
    anon "It's just-"
    anon "From the sounds of it, you were pretty close with him the last few months of his life..."
    anon "... And I've been trying to find out why this all happened... You know?"
    show liu f_ashamed_down
    pause
    anon "I thought, maybe you could fill in the gaps?"
    liu "Y-yeah, I can try."
    liu f_worried "What do you wanna know?"
    show anon behind liu

    menu ano24_find_liu_bedroom.choice:
        "How did he get mixed up in this mess?":
            jump ano24_find_liu_bedroom.mess
        "Why did he keep everything secret?":

            jump ano24_find_liu_bedroom.secret
        "Are you sure you weren't more than friends?":

            jump ano24_find_liu_bedroom.more
        "Do you know why they killed him?":

            jump ano24_find_liu_bedroom.motive
        "That's enough.":

            pass

    show anon f_worried_high with {'master': dissolve}:
        xoffset -350
        xzoom -1
    anon "We should probably get back to looking for that evidence before {b}Kim{/b} comes home."
    liu f_worried "Y-yeah, okay."
    pause
    show liu a_intimate with {'master': dissolve}:
        xoffset -165
    liu "{b}[firstname]{/b}?"
    show liu a_idle
    show anon f_worried:
        xoffset -15
        xzoom 1
    with dissolve
    anon "Yeah?"
    liu "I want you to know... if I could trade places with him... I-"
    anon "Don't say that."
    show liu f_ashamed_down
    anon "He wouldn't want that... and neither do I."
    show liu behind anon
    anon a_liu_shoulder "There's no sense in torturing yourself..."
    anon "... You didn't do anything wrong, okay?"
    liu @ -m_talk "..."
    anon "We're going to get the people who did this to {b}Dad{/b}, okay?"
    show liu f_worried
    anon f_shy "I promise."
    liu "{i}*Sniff*{/i} Y-yeah."
    anon f_normal "But first, we gotta deal with your asshole husband..."
    liu f_nervous "Heh, okay."
    anon a_sides "There has to be something in here that proves he's involved in all this..."
    hide anon with dissolve
    return


label ano24_find_liu_bedroom.mess:
    anon f_worried "How did he get mixed up in this mess?"
    liu f_worried "Well, from what {b}Frank{/b} told me, I just assumed money was always a little tight for you guys at home..."
    anon "Oh, umm... that could be actually... I don't really know."
    anon "They never discussed that stuff with {b}[jen_name]{/b} and I."
    liu "He wanted to give your friends a better life and help you pay for college."
    liu "So when {b}Rump{/b} showed up at the bank waving huge stacks of money around and offering work... he jumped at the opportunity."
    liu f_ashamed_down "I did too actually... but {b}Rump{/b} wasn't interested in hiring a woman."
    anon f_unimpressed "That's not surprising."
    anon "He was almost as big a douchebag as your husband."
    pause
    anon f_worried @ f_confused "Did my dad know {b}Rump{/b} was working with the mob?"
    liu f_confused "No, not at first."
    pause
    liu "And by the time he found out, it was too late."
    liu f_worried "They weren't just going to let him walk away."
    anon f_sad_down "{i}*Sigh*{/i}"
    jump ano24_find_liu_bedroom.choice


label ano24_find_liu_bedroom.more:
    anon f_confused "Are you sure you weren't more than friends?"
    show liu f_worried
    anon "The way you talk about him."
    liu f_ashamed_down "I'm sure."
    show anon f_worried
    pause
    liu "I can't tell you how many times I begged him to run away with me..."
    liu "... We could have packed our bags and disappeared some place {b}Kim{/b} and the mob would never find us."
    liu "Start a new life together somewhere far away."
    liu f_worried "But {b}Frank{/b} could never have done anything like that to you and your friends..."
    liu "... He loved you all so much."
    liu f_ashamed_down "It was wrong of me to even suggest it."
    jump ano24_find_liu_bedroom.choice


label ano24_find_liu_bedroom.motive:
    anon f_worried "Do you know why they killed him?"
    liu f_ashamed_down "No, not really."
    pause
    liu f_worried "I know that he was desperate and trying to come up with a way out..."
    liu "... I can't imagine why he'd try and steal money from them, though."
    liu "It doesn't make sense!"
    anon "Yeah, that's the part I don't understand either."
    pause
    anon "Do you think they're making it up?"
    liu "Maybe."
    show liu f_ashamed_down
    pause
    liu "Then he disappeared and I didn't know..."
    liu "... I was going to call the police but then the painting showed up, And I half-thought..."
    liu f_worried "... Maybe he'd figured it out, you know?"
    pause
    liu b_dressed_cry "Then I heard about the body, and... I-"
    anon f_sad_down @ -m_talk "..."
    liu "I didn't know what to do."
    anon "You don't have to say anymore... I know the rest."
    liu a_wipe_tears b_dressed f_crying @ -m_talk "{i}*Sniff*{/i}"
    liu a_idle f_worried "I'm so sorry, {b}[firstname]{/b}."
    anon "Yeah, me too."
    jump ano24_find_liu_bedroom.choice


label ano24_find_liu_bedroom.secret:
    anon f_worried "Why did he keep everything secret?"
    liu f_worried "He couldn't risk putting you and your friends in danger."
    show anon f_sad_down
    pause
    liu f_worried_down "It's probably the only reason he and I got so close."
    anon f_confused "What do you mean?"
    liu f_worried "He had nowhere else to turn, you know?"
    show anon f_sad_down
    pause
    liu "He was stuck."
    pause
    show anon f_sad_down
    liu "Cut off from his friends and surrounded by wolves..."
    liu f_ashamed_down "... I was the only person he could confide in."
    liu "And I was so caught up in my own selfish shit, I didn't-"
    pause
    show liu b_dressed_cry with dissolve
    liu "{i}*Sniff*{/i} I should have done more to try and help him!"
    anon a_handshake f_worried "Aww, c'mon {b}Liu{/b}... you can't blame yourself."
    liu "Instead, I tried to tear him away from you guys."
    anon "It's not your fault."
    liu "{i}*Sobs*{/i}"
    anon "What else could you have done?"
    show anon a_sides
    show liu a_wipe_tears b_dressed f_crying
    with {'master': dissolve}
    liu "{i}*Sniff*{/i} I don't know."
    show liu a_sides f_worried
    with {'master': dissolve}
    liu "Something!"
    anon a_idle "You're being silly."
    jump ano24_find_liu_bedroom.choice


label ano24_find_bomb:
    scene expression background(776, 360, 2.5) as stage
    show anon f_worried a_point_back with dissolve:
        xoffset -150
        xzoom -1
    anon "Why is there a nuclear warhead above the bed?"
    show liu:
        xzoom -1
    show anon a_idle
    with dissolve
    liu "Don't worry, it's not real."
    liu "Just some model he bought online."
    liu "{b}Kim{/b} was obsessed with building it..."
    liu "... It took him years to put it together."
    anon "That long, really?"
    liu "I'm still not sure he got it right."
    pause
    anon "Well, at least we don't have to worry about any explosions..."
    hide anon with dissolve
    return


label ano24_find_bomb.repeat:
    scene expression background(776, 360, 2.5) as stage
    show anon f_worried_high with dissolve:
        xoffset 200
    anon @ -m_talk "( I really hope it {i}is{/i} \"just some model!\" )"
    hide anon with dissolve
    return


label ano24_find_picture:
    scene expression background(520, 392, 4.75) as stage
    show anon f_disgusted with dissolve:
        xoffset 250
    anon "Ugh, this is so creepy..."
    pause
    anon "I don't suppose there's a hidden safe behind this portrait?"
    show liu with dissolve:
        xzoom -1
    liu "Uhh, no?"
    pause
    liu "Is that a thing?"
    show anon f_normal with {'master': dissolve}:
        xoffset -250
        xzoom -1
    anon "Yeah, {b}Mayor Rump{/b} had one in his office."
    pause
    liu "Surely they wouldn't use the same gag twice?"
    liu "That's just lazy writing."
    anon f_bored "I wouldn't put it past them..."
    show anon a_handshake f_worried_low:
        crop (0, 0, 554, 768)
        xoffset 250
        xzoom 1
    with dissolve
    pause
    show anon a_sides f_confused with {'master': dissolve}:
        reset
        xoffset -250
        xzoom -1
    anon "Nope, nothing there."
    liu "I told you."
    anon "Guess we'll have to keep looking."
    hide anon with dissolve
    return


label ano24_find_picture.repeat:
    scene expression background(520, 392, 4.75) as stage
    show anon with dissolve
    anon "Nope, nothing there."
    hide anon with dissolve
    return


label ano24_find_statue:
    scene location_liu_bedroom_statue
    anon "( \"All hail our glorious leader.\" )"
    anon "( Man, this guy is really sick in the head! )"
    pause
    anon "( You know, I can't put my finger on it, but... )"
    anon "( ... Something seems off about this statue. )"
    return


label ano24_find_statue.repeat:
    scene location_liu_bedroom_statue
    anon "( Something seems off about this statue. )"
    return


label ano24_find_wardrobe:
    scene expression background(472, 396, 6) as stage
    show anon f_worried_low with dissolve:
        xoffset 50
        xzoom -1
    anon @ -m_talk "Hmm."
    show liu behind anon with dissolve:
        xzoom -1
    anon "Not much for variety, is he?"
    liu f_normal_down "No."
    pause
    liu f_normal "In fact, he only owns two outfits."
    anon f_worried "I can see that."
    liu "He'd probably just wear the one if the dealership didn't have a dress code."
    pause
    show anon a_point_back with {'master': dissolve}:
        xoffset -250
    anon "Well, there doesn't appear to be anything out of the ordinary in the closet."
    hide anon with dissolve
    return


label ano24_find_wardrobe.repeat:
    scene expression background(432, 396, 6) as stage
    show anon with dissolve
    anon "There doesn't appear to be anything out of the ordinary in the closet."
    hide anon with dissolve
    return


label ano24_find_stash:
    scene expression background(240, 400, 3.5) as stage
    show anon f_surprised_high with dissolve:
        xoffset -350
        xzoom -1
    anon "Wait a second, this is definitely something..."
    liu "Umm, what are you doing?!"
    anon "I have a hunch."

    scene location_liu_bedroom_statue_open with fade
    pause
    anon "Ah hah!"
    liu "!!!"

    show screen ano24_find_stash() with fade
    anon "I knew something was off about this statue!"
    liu "I had no idea it did that!"
    anon "Wow, there's a bunch of stuff in here!"
    call screen empty()

    scene location_liu_bedroom_statue_coseup with {'master': dissolve}
    liu "Like what?"
    anon "Here, help me down."
    liu "Okay."

    scene expression background(320, 400, 3.5) as stage
    show liu f_worried
    show anon a_paper_multiple f_worried_low
    with fade
    pause
    liu "So?"
    pause
    liu "{b}[firstname]{/b}, what is it?!"
    anon "I'm not sure."
    pause
    anon "This one is just a bunch of random numbers..."
    show liu f_worried_down with dissolve:
        xoffset -200
    pause
    liu "Those look like coordinates."
    anon "Coordinates?"
    anon f_worried "Coordinates to what?"
    liu f_worried "Umm..."
    liu f_worried_down "... What's on the other ones?"
    show anon f_worried_low
    pause
    anon "This one looks like a shipping list."
    pause
    anon "\"15x 10lb Caspian Sea Caviar\""
    anon "\"750x 59.3oz Pizza Rolls - Pepperoni\""
    anon "\"250x 5lb Coffee Beans - Dark Brazilian Santos\""
    anon "5000x Bite Sized Peanut Butter Cups - Individually Packaged\""
    anon "\"25x 18lb Emmentaler Cheese Wheel\""
    anon "\"750x 58.74oz Classic Corn Dogs - 22 Count\""
    anon f_confused "Is any of this making any sense to you?"
    liu @ f_worried "He must have ordered all this knowing we'd be going back to Korea."
    show anon f_worried_low
    anon "\"1200x 12oz Dijon Mustard - Easy Squeeze\""
    anon "\"100x 750ml Snake Wine\""
    anon "\"5x 750ml Hennessy\""
    anon "\"100x 25kg Compressed Hydrogen\""
    pause
    show anon f_surprised_low
    pause
    anon "Holy crap!"
    show liu f_surprised
    anon f_surprised "\"750lb Yellowcake Uranium\""
    anon "Where in the heck did {b}Kim{/b} get yellowcake uranium?!"
    liu f_worried "I have no idea."
    anon "Well, that's definitely not good!"
    liu "Those coordinates are probably a spot in Korea where everything is being dropped."
    anon f_worried "Yeah, I bet you're right."
    liu f_worried_down "What's that last thing?"
    anon f_worried_low "Oh, umm..."
    anon "\"Dearest Kim,\""
    anon "\"I wanted to thank you once again on behalf of my Russian associates.\""
    anon "\"They were more than happy to provide the uranium you requested but I'm afraid the plutonium is another matter.\""
    anon "\"I'm sure the eggheads back in your home country will sort it out for you eventually.\""
    anon "\"I wasn't able to secure that propulsion mechanism that you wanted either but I had them fax over a copy of the blueprints.\""
    anon "\"They assured me that it was the best solution to your problem, given your limited resources.\""
    anon "\"Best of luck in Korea, {b}Kim{/b}.\""
    anon "\"Give that beautiful wife of yours a kiss from me.\""
    liu @ f_gross "Eugh."
    anon "\"Sincerely, {b}Mayor Ronald Rump{/b}\""
    anon "\"P.S. - Try not to blow yourself up.\""
    anon f_worried "Holy crap."
    show liu f_worried
    anon "Do you realize what this means?"
    liu "That I'm married to a genocidal maniac?"
    anon f_shy "Err."
    anon "Well, yeah... that."
    anon f_normal "But also, we've found what we're looking for!"
    liu f_surprised "You think that's enough?!"
    anon "{b}Liu{/b}, he's buying yellowcake uranium and having it shipped to Korea!"
    show liu f_nervous
    anon "That is so unbelievably illegal!"
    anon "They lock people up and throw away the key for doing stuff like this."
    liu "So we did it?"
    anon f_laugh "We did it."
    liu f_laugh "Eeeeeeee!!!"
    show anon b_empty
    show liu b_dressed_hug:
        xoffset 0
    with dissolve
    liu "You are, the greatest man, I have EVER met!"
    anon f_shy_low "Oh, ehh... I dunno about that..."
    liu "No, seriously."
    liu "I've been dreaming about this, every day, since {b}Kim{/b} took me away from my village eighteen years ago!"
    liu "There's no way I could ever properly repay you for this."
    anon "Aww, c'mon... you don't have to repay me..."
    anon "... Besides, you're helping me with my Russian problem, remember?"
    show anon a_sides b_dressed f_shy
    show liu b_dressed f_happy:
        xoffset -200
    with {'master': dissolve}
    liu "Y-yeah, of course."
    liu "I'll do anything."
    pause
    liu "This is just so exciting... I can't-"
    pause
    hide anon
    show liu b_dressed_kiss1:
        xoffset 0
    anon "!!!" with hpunch
    pause
    show liu b_dressed f_nervous o_blush a_mouth_cover:
        xoffset -200
    show anon f_shy a_sides
    with dissolve
    liu "I am so sorry!"
    liu f_ashamed_down "That was-"
    liu a_cover "I should never-"
    hide anon
    show liu b_dressed_kiss_2 -o_blush:
        xoffset 150
    with fastdissolve
    liu "!!!"
    pause
    show liu with dissolve:
        xoffset 250
    pause
    hide liu with dissolve
    anon "Whoa!"
    liu "Hehe!"

    scene location_liu_bedroom_bed_day
    show liu b_bed_dressed_kiss
    with fade
    pause
    liu "Mmm."
    show anon b_liu_dressed f_shy_high behind liu
    show liu b_bed_dressed_sit
    with dissolve
    liu "I want you."
    show liu b_bed_dressed_kiss
    hide anon
    with dissolve
    pause
    show anon b_liu_dressed f_shy_high behind liu
    show liu b_bed_dressed_sit
    with dissolve
    liu "Ngh, I want you so bad!"
    liu "Please!"
    anon "Y-yeah, okay."
    show anon b_liu_remove_shirt
    show liu b_bed_skirt_remove_top
    with dissolve
    pause
    show anon b_liu_shorts_throw_shirt
    show liu b_bed_skirt_sit_throw_top
    with dissolve
    pause
    show anon b_liu_shorts
    show liu b_bed_skirt_sit
    with dissolve
    pause
    show liu b_bed_skirt_kiss
    hide anon
    with dissolve
    liu "Mmm."
    pause
    show anon b_liu_shorts f_shy_high behind liu
    show liu b_bed_skirt_remove_bottom
    with dissolve
    pause
    show liu b_bed_naked_sit_throw_skirt with dissolve
    pause
    show liu b_bed_shorts_kiss
    hide anon
    with dissolve
    liu "Mmm."
    show anon b_liu_shorts f_shy_high behind liu
    show liu b_bed_naked_sit_red
    with dissolve
    liu "Ngh, why are you still wearing pants?!"
    show anon b_liu_shorts_remove_shorts f_worried_low
    show liu b_bed_naked_raised
    with {'master': dissolve}
    anon "R-right, sorry."
    show anon b_liu_naked f_shy_high
    show liu b_bed_naked_sit
    with dissolve
    pause
    show liu b_bed_naked_kiss
    hide anon
    with dissolve
    pause

    call scene_liu_sex_bedroom

    scene location_liu_bedroom_caught
    show anon b_liu_naked f_surprised_teeth_left
    show liu b_naked_caught1 f_worried_down m_talk
    liu "!!!" with hpunch
    show liu b_naked_caught2 with dissolve:
        .5
        'liu b_naked_caught3 f_ashamed_down m_talk' with fastdissolve
        .2
        'liu b_naked_caught4 f_ashamed_down m_talk' with fastdissolve
    anon f_surprised "Oh, shit!!"
    show anon f_surprised_teeth_left
    show liu b_naked_caught4 f_worried_down
    kim "YOU DARE FUCK {b}KIM{/b} WIFE?!!!"

    scene expression background(352, 400, 3.85) as stage
    show kim f_angry a_point:
        xoffset -64
        xzoom -1
    with fade
    kim "{b}KIM{/b} GONNA KIRR YOU!!!"
    show kim a_fists
    show liu b_naked_hair f_frightened a_timid:
        xoffset 100
    with dissolve
    liu "{b}Kim{/b}, please... It's not his faul-"
    kim "YOU SHUT UP, WHORE!"
    show anon_overlay_dick_od_naked_dick1 as dick behind liu:
        xoffset 0
        xzoom -1
    show anon b_naked_changing3 behind dick:
        xoffset 0
        xzoom -1
    with dissolve
    kim "YOU BAD WIFE!"
    show anon b_shirt f_worried a_surprised od_dick1:
        xoffset -64
    hide dick
    with dissolve
    kim "{b}KIM{/b} TIE YOU TO CART IN CENTER OF KOREA!"
    show anon f_surprised
    kim "EVERY MAN PAY ME TO TAKE TURN WITH DIRTY WHORE!"
    show anon f_angry a_empty
    show liu a_behind_anon behind anon:
        xoffset 50
    with {'master': dissolve}
    anon "H-hey, don't you talk to her like that!"
    kim "SHE MY WIFE!"
    kim "AND SHE BAD WIFE!"
    kim "SHE WIRR DO WHAT {b}KIM{/b} SAY!"
    show anon a_sides
    show liu a_timid
    with dissolve
    anon "Not anymore."
    kim @ f_surprised "Oh?"
    kim "And you gonna stop {b}Kim{/b}, poor boy?!"
    anon "That's right."
    kim @ a_point "{b}KIM{/b} FUCK YOU UP!"
    liu "{b}Kim{/b}, please... Don't hurt him!"
    kim f_angry_yell m_talk "SIRENCE!!!" with hpunch
    kim @ a_point "POOR BOY BRING THIS ON HIMSERF!!!"
    kim "AAIIIYAAAAHHH!!!"
    show liu f_wincing behind kim
    show kim b_dressed_reach1 -m_talk:
        crop (370, 0, 654, 768)
    show kim_body_b_dressed_reach1 behind kim:
        crop (0, 0, 370, 510)
        xalign 1.
        xoffset -64
        xzoom -1
    show anon b_empty f_surprised_low
    show anon_body_b_shirt as no_pants:
        crop (0, 510, 1024, 258)
        offset (-64, 510)
        xzoom -1
    show anon_overlay_dick_shirt_od_dick1 as shirt_dick:
        xoffset -64
        xzoom -1
    show anon_arms_dressed_a_surprised_up:
        crop (0, 510, 200, 258)
        align (1., 1.)
        xoffset -64
        xzoom -1
    with {'master': dissolve}
    kim f_angry "NGH!"
    kim "GRR!!"
    anon f_unimpressed "Seriously, man?"
    show liu f_wincing_peeking
    show kim b_dressed_reach with dissolve
    kim "RAAARGH!!"
    pause
    show liu b_naked_hair f_worried a_sides
    show kim b_dressed:
        xzoom -1
    show anon b_shirt
    hide no_pants
    hide shirt_dick
    hide kim_body_b_dressed_reach1
    hide anon_arms_dressed_a_surprised_up
    with dissolve
    kim "STOP THAT!"
    kim "FIGHT {b}KIM{/b} RIKE MAN, COWARD!"
    show kim b_dressed_reach1 -m_talk:
        crop (370, 0, 654, 768)
    show kim_body_b_dressed_reach1 behind kim:
        crop (0, 0, 370, 510)
        xalign 1.
        xoffset -64
        xzoom -1
    show anon b_empty f_disgusted_low
    show anon_body_b_shirt as no_pants:
        crop (0, 510, 1024, 258)
        offset (-64, 510)
        xzoom -1
    show anon_overlay_dick_shirt_od_dick1 as shirt_dick:
        xoffset -64
        xzoom -1
    show anon_arms_dressed_a_surprised_up:
        crop (0, 510, 200, 258)
        align (1., 1.)
        xoffset -64
        xzoom -1
    with {'master': dissolve}
    kim "YAAAHH!"
    kim "ACK!!"
    show liu f_confused
    show kim b_dressed_reach with dissolve
    kim "SUBMIT!"
    pause
    kim "SUBMIT TO YOUR GRORIOUS READER!!!"
    anon f_worried_low "Alright, pipsqueak... you need to calm down before you hurt yourself."
    show kim b_dressed behind anon:
        xoffset 0
        xzoom -1
    show anon b_shirt f_confused
    hide no_pants
    hide shirt_dick
    hide kim_body_b_dressed_reach1
    hide anon_arms_dressed_a_surprised_up
    with dissolve
    kim "YOU WIRR TIRE EVENTUARRY!"
    kim "THAT WHEN {b}KIM{/b} STRIKE!!!"
    anon "Uh huh."
    show anon a_flick1 with dissolve:
        xoffset -175
    show anon a_flick2
    show kim f_wincing
    with vpunch
    pause
    show liu f_surprised a_laugh
    show anon a_crossed:
        xoffset -64
    show kim a_rubbing f_angry_yell
    with {'master': dissolve}
    kim "AII!!!"
    show liu a_sides
    kim "WHAT THE-"
    kim a_fists f_angry_yell "YOU DARE STRIKE {b}KIM{/b}?!"
    show kim f_angry
    anon "I asked you to calm down..."
    kim a_counter_raised f_angry_yell "{b}KIM{/b} NO TAKE ORDER FROM RIKE OF YOU!!"
    kim m_talk "STUPID POOR BOY AND BAD WIFE!"
    show anon f_skeptical
    show liu f_annoyed
    show kim a_fists with dissolve
    kim -m_talk "DIRTY WHORE!"
    show kim f_angry
    show anon a_flick1 with dissolve:
        xoffset -175
    show anon a_flick2
    show kim f_wincing
    with vpunch
    pause
    show kim a_rubbing f_angry_yell behind liu:
        xoffset -40
    show anon a_crossed:
        xoffset -64
    with {'master': dissolve}
    kim "OUCH!!!"
    kim "STOP DOING THAT!!"
    show kim f_angry
    anon "I told you not to speak to her like that."
    kim a_fists "GRR!"
    kim f_angry_yell "{b}RIU{/b} COME TO ME, NOW!!"
    kim "WE GO BACK TO KOREA, THIS INSTANT!"
    show kim f_angry
    liu f_gross "No."
    kim f_surprised "What you say?!"
    kim f_angry_yell "YOU NEVER SAY NO TO {b}KIM{/b}!"
    kim "I BUY YOU!"
    kim "YOU MINE!!"
    show kim f_angry
    liu "Not anymore."
    kim @ f_angry_yell "GET OVER HERE NOW!"
    show anon a_surprised f_surprised
    show liu:
        xoffset -300
    with dissolve
    pause .5
    show liu a_flick1 with dissolve
    show liu a_flick2
    show kim f_wincing
    with vpunch
    pause
    show liu a_sides
    show kim a_rubbing f_angry_yell:
        xoffset -64
    with {'master': dissolve}
    kim "AII!!!"
    kim "GOD DAMNIT!"
    show kim f_angry
    show anon a_sides f_laugh
    with {'master': dissolve}
    liu f_laugh "Pfft, hahahahaah!!"
    kim a_fists f_angry_yell "STOP RAUGHING!"
    kim "THIS NOT FUNNY!!"
    show kim f_angry
    show anon f_normal
    liu f_normal a_hips "I'm not scared of you anymore, you bastard!"
    pause
    show anon a_empty f_flirt_left
    show liu a_cowering2 f_sexy:
        xoffset 36
    show liu_arms_naked_a_cowering2:
        xoffset 36
    with dissolve
    liu "I have a real man now."
    liu "And he made me feel things in bed you've never even dreamed of!"
    kim f_surprised @ -m_talk "..."
    anon f_snarky "Listen {b}Kim{/b}... because this is what's going to happen next..."
    anon "You're gonna turn around and walk directly out of this apartment."
    anon "Where you go from there, is entirely up to you... but I'd suggest boarding a plane back to Korea as quickly as possible."
    anon "{b}Liu{/b} will not be joining you."
    kim f_angry "Oh, you think so, poor boy?!"
    anon "I know so."
    show anon a_crossed
    show liu a_idle
    hide liu_arms_naked_a_cowering2
    with dissolve
    anon "Because {b}Liu{/b} will be coming with me, down to the police station..."
    show anon b_dressed_pickup with dissolve:
        yoffset 100
    pause
    show anon a_empty b_shirt:
        yoffset 0
    show anon_arms_dressed_a_paper_multiple as left_arm:
        crop (300, 0, 724, 768)
        xoffset -64
        xzoom -1
    show anon_arms_dressed_a_sides as right_arm:
        crop (0, 0, 300, 768)
        xalign 1.
        xoffset -64
        xzoom -1
    with dissolve
    anon "... With these."
    show kim f_baby_cry a_scare with dissolve
    pause
    kim "I uhh..."
    kim "... those don't berong to {b}Kim{/b}!"
    kim a_idle "They prove nothing!"
    anon "Mmm, pretty sure the cops are gonna disagree with you on that."
    pause
    anon "You should probably start running now."
    kim f_angry "Grr, you think you win?!"
    kim "You no win!"
    kim "{b}Kim{/b} reave this time..."
    kim a_counter_raised "... But it not over, poor boy!!"
    hide kim with dissolve
    pause
    hide left_arm
    hide right_arm
    show anon a_wave:
        xoffset -300
    with dissolve
    anon "Bye, {b}Kim{/b}."
    anon "Pleasant journey."
    liu a_laugh @ f_laugh "Hehe!"
    show anon a_sides f_brag behind liu:
        xoffset 200
        xzoom 1
    show liu a_sides
    with {'master': dissolve}
    liu "That was amazing!!"
    liu f_surprised "I can't believe I struck him..."
    liu f_sexy @ f_laugh a_laugh "Did you see?!"
    anon @ f_laugh "Heh, yeah... you did great!"
    show liu b_naked_anon_arms f_happy_closed:
        xoffset 200
    show anon a_empty f_surprised_low behind liu
    with {'master': dissolve}
    liu "This is the greatest day of my life!!"
    show anon f_shy_low
    liu f_happy "I can't believe he's finally gone..."
    liu "... I'm free."
    anon "Well, you can believe it."
    anon "He's never gonna bother you again, I promise."
    anon "But we should probably hurry these documents down to the police station so the cops have a better chance of catching him."
    liu f_confused "Aww, I suppose you're right."
    show anon b_shirt f_normal a_sides
    show liu b_naked_hair f_sexy:
        xoffset 0
    with {'master': dissolve}
    liu "But I want a rain check on the sex, okay?"
    hide liu
    show anon a_behind_head
    with {'master': dissolve}
    anon f_flirt @ f_laugh "Heh, a sex rain check?"
    pause
    liu "Where the heck did my panties go?"
    anon f_confused a_thinking "Uhh..."
    show anon f_surprised_high
    pause
    anon a_sides f_flirt "... Is that them, hanging off the model airplane?"
    liu "!!!"
    liu "How did they get up there?!"
    anon f_laugh "Hahahaah!"

    scene expression background(l=L_police_front, t=3) with longfade
    show anon f_tired with dissolve
    anon @ -m_talk "( Finally, I thought I'd never get out of there... )"
    anon @ -m_talk "( ... I had no idea filing a police report involved so much paperwork! )"
    pause
    anon @ -m_talk "( I hope they catch him quickly. )"
    anon @ -m_talk "( The police said they'd station an officer outside {b}Liu{/b}'s building for the next few nights... but I'll feel much better once {b}Kim{/b} is behind bars. )"
    anon f_laugh -m_talk "( And {b}Liu{/b} promised to {b}meet me at Tony's tomorrow{/b} and help us figure out how to get that briefcase. )"
    show anon f_yawn a_yawn with dissolve
    pause
    anon f_tired a_idle @ -m_talk "( Man, I'm beat. )"
    anon @ -m_talk "( I should get home and get some rest. )"
    anon f_laugh @ -m_talk "( It's been a good day. )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
