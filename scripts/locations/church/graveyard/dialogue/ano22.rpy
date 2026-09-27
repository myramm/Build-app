label ano22_sign_headstone:
    scene
    show screen church_graveyard_grave()
    anon "( Hmm, these flowers were put here only recently... )"

    anon "( ... I wonder who brought them? )"

    anon "..."
    anon "( I didn't think to bring him anything. )"

    pause 1.5

    if not renpy.mobile:
        call screen empty()

    scene location_church_graveyard_visit with fade
    anon "H-hey, {b}Dad{/b}."

    pause
    anon "I'm sorry I didn't come and see you sooner."

    anon "aku hanya-"

    pause
    anon "I guess... I was afraid..."

    anon "... Of how this would make me feel."

    pause
    anon "So much has happened since..."

    anon "... Since you..."

    pause
    anon "{i}*Sigh*{/i} I still can't believe you're gone."

    anon "I keep hoping that tomorrow I'll wake up to find that this has all been a bad dream..."

    anon "... And you'll be sitting at the breakfast table with your paper and coffee."

    anon "Annoying {b}[jen_name]{/b} with your silly dad jokes and trying to trick {b}[deb_name]{/b} into giving you answers for the crossword puzzle."

    pause
    anon "Heh, things are so much different without you."

    pause
    anon "I'm trying my best to keep things afloat, but honestly, I'm a poor substitute."

    anon "{b}[jen_name]{/b} has been even bitchier than ever."

    pause
    anon "She'd never admit it but I think your passing hurt her a lot."

    pause
    anon "I've been trying to bond with her like you and {b}[deb_name]{/b} always wanted but she's not making things easy."

    pause

    if M_jenny.finished_state(S_jenny_cheerleader_sex):
        anon "Heh, she's got this silly plan to make a bunch of money on the internet and you know how she is..."

        anon "... Once she's made up her mind, there's no talking her out of it."

        pause
        anon "But the crazy thing, is that it's actually working!"

        anon "She made a ton of money during our last show and she was actually smiling at the end!"

        anon "I'm talking big, happy, almost giddy smiling... like she used to do when we were kids."

        anon "You should have seen her!"

        anon "( !!! )"
        anon "Err... well, maybe it's a good thing you couldn't..."

        anon "... Or at least I hope you couldn't."

        pause
        anon "I uhh... Heh."

        anon "Sudahlah."

        pause
        anon "The important thing is that she's getting along okay..."

        anon "... And who knows?!"

        anon "She might even start helping {b}[deb_name]{/b} out with the bills."

        anon "So, that's great... Right?"


    anon "Oh, and speaking of {b}[deb_name]{/b}..."

    anon "... She's been a rock through this whole thing."

    anon "You'd really be proud of her, {b}Dad{/b}."


    if M_debbie.finished_state(S_debbie_night_visit_three):
        anon "She always makes sure to put on a brave face for {b}[jen_name]{/b} and my sake..."

        anon "... Even though deep down, I can tell she's a wreck over losing you."

        pause
        anon "I've been making an effort and help her around the house more often and assure her that everything is gonna be okay..."

        anon "... And it seems like it's working."

        anon "She's slowly but surely starting to mend and show flashes of her old self."

        pause
        anon "But things have also gotten a little... umm..."

        anon "... Rumit."

        pause
        anon "A-and it's not something I'm going to apologize for!"

        anon "Because it just sort of happened on its own..."

        pause
        anon "... And {b}[deb_name]{/b} deserves to be happy and so do I... even if it's just in the here and now."

        anon "Benar?"

        pause

    anon "{i}*Sigh*{/i} I really don't think I could have made it through this without her..."

    anon "... She's amazing!"

    pause
    pause
    anon "I should probably tell you about my new friends, {b}Tony{/b} and {b}Maria{/b}."

    anon "They've been helping me try and get to the bottom of this whole mess you left us."

    pause
    anon "You would have liked {b}Tony{/b}, I think."

    anon "He shares your sense of humor."

    pause
    anon "And his wife {b}Maria{/b} is one of the strongest and most beautiful women I've ever met."

    anon "A couple of these big goons came by their store a while back and she chased them away all on her own... at gunpoint no less!"

    anon "You should have seen the size of this shotgun she brought out... it was bigger than she was!"

    anon "Heh, they practically pooped themselves!"

    pause
    pause
    anon "Anyways, they're the ones who worked out exactly who you got mixed up with..."

    anon "... This {b}Raz Chernyshevsky{/b} and his Russian minions."

    anon "Oh, and {b}Mayor Rump{/b}, of course."

    anon "Who, I'm sure you'll be happy to learn, is now behind bars."

    pause
    anon "Hopefully, you can rest a little easier knowing that."

    pause
    anon "I wanted to get {b}Raz{/b} too... but..."

    anon "... Things are getting really dangerous now and he's pulled his entire organization back into their warehouse."

    pause
    anon "{b}Tony{/b} wants to keep going but {b}Maria{/b} is starting to get really worried."

    anon "And I can't blame her to be honest."

    pause
    anon "We've got no way inside and no idea how many goons will be waiting for us."

    anon "And they've only just had a baby... so, I really don't feel good about putting {b}Tony{/b} in danger."

    pause
    anon "By the way, you're technically the grandfather..."

    anon "... So, umm... congratulations... I think?"

    anon "Heh, I just wish you were here to see it."

    pause
    anon "{i}*Sigh*{/i} {b}Maria{/b} says we've accomplished enough."

    anon "That you wouldn't want me to risk my life for revenge."

    anon "And deep down, I know she's right."

    anon "You wouldn't want that for me."

    pause
    anon "But I just-"

    pause
    anon "It makes me feel sick, you know?"

    anon "Our family won't ever be the same because of this guy..."

    anon "... I'm never going to see you again."

    pause
    anon "There has to be something we can do..."

    anon "... Something I'm overlooking."

    pause
    anon "{i}*Sniff*{/i} I just miss you so much {b}Dad{/b}."

    pause
    anon "I hope wherever you are... you know that I love you..."

    anon "... And I don't want you to worry about the girls and me."

    anon "{i}*Sniff*{/i} I'm going to take care of everything, I promise."

    pause
    pause
    anon "Heh, see... this is why it took me so long to come out here!"

    anon "I knew the dam was gonna break once I started speaking with you..."

    pause
    anon "... It's too bad you can't send me a sign or something from the beyond, you know?"

    anon "Set me on the right course to ending this whole mess."

    pause
    anon "I guess that would be cheating though, huh?"

    keeves "♪ ... said anybody caught trespassin' would be shot on sight. ♪"


    scene expression background(312, 440, 4) as stage
    show anon f_surprised_left:
        xzoom -1
    anon @ -m_talk "( !!! )" with hpunch
    show anon f_surprised with {'master': dissolve}:
        xoffset 500
        xzoom 1
    keeves "♪ So I jumped on the fence and-a yelled at the house! ♪"

    anon @ -m_talk "( Somebody's coming! )"


    scene expression background(824, 440, 4) as stage
    show keeves a_burrito_sing f_sing:
        xoffset 500
        xzoom -1
    with {'master': MultipleTransition([
        False, pushleft, background(568, 440, 4), pushleft, True])}
    keeves "♪ Hey, what gives you the right?! ♪"

    keeves a_burrito_eat f_eat "Om, nom, nom..."

    keeves a_burrito f_laugh "... Mmm, that's a good burrito, man..."

    keeves a_burrito_sing f_sing "♪ To put up a fence to keep me out or to keep mother nature in. ♪"

    keeves "♪ If God was here he'd tell you to your face, man, you're some kinda sinner! ♪"

    show anon f_worried with {'master': dissolve}:
        xoffset -100
    anon "Umm, excuse me?"

    keeves f_surprised a_burrito_drop "Oh lord, help me Jesus!!"

    show keeves f_ninja a_ninja with fastdissolve:
        xoffset 0
        xzoom 1
    keeves "Waaaah!!"

    show anon b_dressed_blocking with {'master': dissolve}
    anon "!!!"
    keeves f_confused "Who goes there?!"

    show anon a_surprised_up_both b_dressed f_worried with dissolve
    anon "It's just me."

    keeves "Oh."

    show keeves a_idle f_normal with dissolve
    keeves "Hey there, little dude."

    keeves "You know, you really shouldn't sneak up on people like that..."

    show anon a_sides with {'master': dissolve}
    keeves "... I almost delivered a spin-kick right to your melon!"

    anon a_idle @ f_confused "M-my what?"

    keeves f_sad_down "Aduh, bung..."

    show keeves b_dressed_bend_down
    show anon f_worried_low
    with dissolve

    if M_keeves.finished_state(S_kee_intro_meet):
        anon "Why are you out here, {b}Father{/b}?"

        show keeves b_dressed a_burrito_sad f_sad_down
        show anon f_worried
        with dissolve
        pause
        keeves "Well, I was enjoying a delicious burrito from the Circle K down the street..."

        keeves "... Which is no longer most triumphant."

        show keeves f_sad
        anon "In the middle of a graveyard?"

    else:
        anon "Do you work here or something?"

        show keeves b_dressed a_burrito_sad f_sad_down
        show anon f_worried
        with dissolve
        pause
        keeves "This is not most triumphant..."

        show keeves a_burrito_point
        show anon o_crumbs
        with dissolve
        keeves "... Do you believe in the five-second rule?"

        show keeves f_sad a_burrito with dissolve
        anon "Not in a graveyard, I don't."


    keeves f_confused "Graveyard?"

    pause
    keeves f_woa "Whoa."

    keeves f_confused "How did I get here?"

    anon "Uhh??"

    keeves f_surprised "Wait a second, am I dead again?!"

    anon "T-tidak?"

    keeves "Because if I'm dead you have to tell me!"

    anon f_skeptical @ -m_talk "..."
    keeves "Is the Grim Reaper here?"

    show keeves with dissolve:
        xoffset 500
        xzoom -1
    anon "Grim Reaper?!"

    show keeves a_burrito_point f_confused:
        xoffset 0
        xzoom 1
    show anon f_surprised_down o_crumbs
    with {'master': dissolve}
    keeves "If we're playing board games again, we're not going best of seven..."

    show keeves a_burrito
    show anon f_unimpressed a_brush_cumbs o_empty
    with {'master': dissolve}
    keeves "... That was totally bogus last time!"

    anon f_worried a_idle "Okay, you have completely lost me."

    keeves "You tell him I'll do one game of battleship and that is it!"

    anon "Battleship?!"

    keeves f_normal "No Candyland!"

    keeves "No Clue!"

    anon "{b}Father{/b}, I-"

    keeves "And definitely no Twister!"

    keeves "Because that dude has a serious foot fungus problem!"

    anon f_angry "OH MY GOD SHUT UP!"

    keeves f_surprised @ -m_talk "..."
    anon f_worried "saya-"

    anon f_sad_down "Sorry, that was an overraction."

    keeves f_normal "Jeez, little dude... you need to like, take a chill pill."

    anon f_worried "I'm trying to tell you that you're not dead."

    keeves f_confused "bukan aku?"

    anon "Tidak."

    pause
    keeves a_burrito_eat f_eat @ f_laugh a_burrito_rock "Bagus sekali!"

    keeves "Om, nom, nom."

    show keeves f_normal_food a_burrito with dissolve
    pause
    keeves "... Mmm, that's a good burrito, man..."

    keeves "So what brings you out here, little dude?"

    anon f_unimpressed "That was my question."

    keeves f_normal "I know but I'm still waiting on you to answer it..."

    anon f_worried "But that's not-"

    keeves "... So what brings you out here, little dude?"

    anon f_tired @ -m_talk "..."
    anon f_skeptical "Are you high or something?"

    keeves @ f_laugh "Pfft, whaaaaat?!"

    keeves "Tidak."

    pause
    show keeves a_burrito_point f_confused
    show anon o_crumbs
    with {'master': dissolve}
    keeves "Mengapa?"

    show keeves a_burrito with dissolve
    anon "I dunno, you just seem..."

    anon f_worried "... Well, high."

    keeves "You're not a cop, are you?"

    show keeves a_burrito_point
    show anon f_disgusted_down m_talk
    with {'master': dissolve}
    keeves "Because if you're a cop, you have to tell me!"

    show keeves a_burrito
    show anon a_brush_cumbs f_unimpressed o_empty -m_talk
    with {'master': dissolve}
    anon "No, I'm not a cop."

    show anon a_idle with {'master': dissolve}
    keeves "Bagus sekali!"

    pause
    show keeves f_eat a_burrito_eat with dissolve
    pause
    keeves a_burrito f_normal_food "So what brings you out here, little dude?"

    anon f_sad_down "{i}*Huh*{/i}"

    anon "I was here talking with my {b}Dad{/b}, if you must know."

    keeves f_normal @ f_laugh "That's cool, little dude."

    keeves "I usually meet my father at like, a restaurant or something..."

    anon "Well, my father's dead."

    keeves "Oh, begitu."

    pause
    keeves f_surprised "Tunggu sebentar."

    keeves "Are you saying your father's a ghost?!"

    show anon f_skeptical
    keeves "Because if so, we gotta call those guys, man..."

    anon "Eh?"

    keeves f_annoyed "... You know the ones from the song?"

    keeves "Ghost-something..."

    anon "Busters?"

    keeves f_laugh "Yeah, man... That's them!"

    show keeves a_burrito_eat f_eat with dissolve
    pause
    keeves a_burrito f_normal_food "Do you know their number?"

    keeves "Because they ain't afraid of no ghost."

    anon "My dad isn't a ghost, {b}Father{/b}."

    keeves f_confused "He isn't?"

    anon "Tidak."

    pause
    anon f_worried "I was just... Well, speaking to his spirit, I guess... in the beyond or whatever."

    keeves "Oh, like heaven?"

    anon a_behind_head "Y-ya, menurutku."

    keeves f_laugh "Right on, little dude."

    show keeves f_eat a_burrito_eat
    show anon a_idle
    with dissolve
    pause
    keeves a_burrito f_normal_food "How did he die?"

    anon "He was murdered."

    keeves f_surprised "Mustahil!"

    keeves f_confused "Do you know who did it?"

    anon "Y-yeah, I do but..."

    anon "... I really don't think I should be talking about this with you."

    keeves "Kenapa tidak?"

    anon "Because it's dangerous, and kinda complicated."

    keeves "How's it dangerous?"

    anon "{i}*Sigh*{/i} Let's just say that the guy who killed him is still out there..."

    pause
    anon "... And he's causing everyone who gets close to me a lot of problems, okay?"

    keeves f_sad "Oh, that does not sound most triumphant, little dude."

    keeves "Sama sekali tidak."

    anon f_sad_down "Yeah, it's not."

    pause
    anon "I've been trying to do something about it, but..."

    anon "... It's out of my hands now."

    keeves "Why's that?"

    anon f_worried "Apa?"

    keeves "How come it's out of your hands?"

    show keeves f_eat a_burrito_eat with dissolve
    anon "Well, that's the part where it gets complicated..."

    keeves a_burrito f_normal_food "It doesn't seem complicated to me, man."

    keeves "If somebody killed my father, I'd wanna go and kill them right back."

    show keeves f_normal
    anon "Yeah, well that's-"

    pause
    anon f_skeptical "That's a very odd thing for a priest to say."

    keeves "Oh, you think so?"

    show keeves f_eat a_burrito_eat with dissolve
    pause
    keeves a_burrito f_normal_food "Well, what did your old man say about it?"

    anon f_sad "Heh, he uhh... Wasn't very talkative, I'm afraid."

    keeves f_normal "Hmm, that's a bummer."

    pause
    keeves "Sounds like you're stuck with me then."

    show anon f_worried
    pause
    keeves "Lay it on me, little dude."

    anon "Benar-benar?"

    keeves "Yeah, c'mon... I'm a priest, remember?"

    keeves "Listening to other people's problems is like ninety percent of what I do."

    anon "Okay, but did you miss the part where this guy causes everyone I get close with problems?"

    keeves "Tidak."

    pause
    keeves "Did you miss the part where I almost spin-kicked you in the melon?"

    anon "Heh, what?"

    keeves "I'm not worried about it, little dude."

    keeves "{b}Father Keeves{/b} is righteous and God protects his flock."

    anon f_skeptical @ -m_talk "..."
    anon "You're a weird guy, you know that?"

    keeves @ f_laugh "Cool, man."

    anon @ -m_talk "..."
    anon f_worried @ a_frustrated "I suppose it wouldn't hurt to tell you."

    keeves @ f_laugh a_burrito_rock "Bagus sekali!"

    anon "{i}*sigh*{/i} The man who killed my father... he's..."

    anon "... Well, let's just say that he's the head of a big criminal organization here in Summerville."

    keeves @ f_woa "Whoa."

    keeves "Summerville has criminal organizations?"

    anon "Benar?!"

    anon "I was surprised by that too."

    anon "And... well, long story, short, he's got an army of goons protecting him."

    anon "So I can't just waltz in there and get him."

    keeves "Have you spoken with the police about this?"

    anon "Of course, but they won't do anything."

    show keeves f_eat a_burrito_eat with dissolve
    anon "They just fed me some lame excuse about not having the manpower to take on an organization this large."

    keeves a_burrito f_normal_food "Aww, that sounds bogus, little dude!"

    anon "Aku tahu."

    anon @ f_eyeroll "{i}*Sigh*{/i} And after I brought them {b}Rump{/b} on a silver platter too."

    keeves f_normal @ f_woa "Whoa."

    keeves "You're responsible for {b}Mayor Rump{/b} getting thrown in the slammer?"

    anon "Yeah, he was involved in my father's murder as well."

    keeves "Tidak bercanda?"

    pause
    keeves "You're a busy little dude, huh?"

    anon "Kukira."

    pause
    keeves "You want some advice, little dude?"

    anon "Umm, sure."

    keeves "People don't often get what they want in life, you know?"

    keeves "You have to like, learn to appreciate what you have and stuff."

    anon @ f_worried_surprised -m_talk "..."
    keeves "For instance..."

    keeves "... Did I want a microwaved burrito from the Circle K?"

    anon f_worried @ -m_talk "..."
    keeves "Tidak, tidak juga."

    keeves "Would I rather have a bodacious double cheeseburger with carmelized onions and fresh tomato?"

    anon @ -m_talk "..."
    keeves "You betcha!"

    keeves "But alas, little dude..."

    keeves "... The Circle K doth not provide such culinary delights."

    pause
    show keeves a_burrito_eat f_eat with dissolve
    pause
    keeves a_burrito f_normal_food "And so, I must learn to be content with this..."

    keeves "... Most triumphant burrito instead."

    pause
    keeves f_normal "You get what I'm saying?"

    anon "Y-ya, menurutku begitu."

    anon "You're saying I should be content with what I've accomplished already?"

    keeves "Nah, little dude."

    keeves "I'm saying, I could really go for a burger right now."

    anon f_unimpressed @ -m_talk "..."
    show keeves a_burrito_point
    show anon o_crumbs
    with dissolve
    keeves f_confused "You wouldn't happen to have one, would you?"

    show anon f_disgusted_down m_talk
    pause .25
    show anon a_facepalm f_hurt -m_talk with {'master': dissolve}
    keeves a_burrito "Because if you have one, you have to tell me!"

    show anon a_brush_cumbs o_empty f_unimpressed with dissolve
    anon "{i}*Sigh*{/i} No, why would I have a burger on me here?"

    show anon a_idle with dissolve
    keeves "Aduh, bung..."

    pause
    show keeves a_burrito_eat f_eat with dissolve
    pause
    keeves a_burrito f_normal_food "You wanna head to the Circle K with me and get another burrito?"

    anon f_worried @ f_tired a_point_back "You know what, I think I'm just gonna go."

    keeves "Oh?"

    keeves "Alright, little dude..."

    show keeves a_burrito_eat f_eat with dissolve
    pause
    keeves a_burrito f_normal_food "Well, if you ever need to talk or something..."

    keeves "... You know where to find me."

    show keeves f_normal
    anon a_up "No, honestly... that's okay."

    anon a_behind_head "I'll just... umm..."

    anon @ f_skeptical "I'll see you later... maybe..."

    keeves @ a_burrito_rock f_laugh "Rock on, little dude!"

    anon "B-benar."

    show anon a_sides f_worried_surprised with {'master': dissolve}:
        xoffset -600
        xzoom -1
    anon @ -m_talk "( What in the heck is wrong with that guy? )"

    hide anon with dissolve
    pause
    show keeves f_sad
    pause
    show keeves a_sides with dissolve:
        xoffset 500
        xzoom -1
    pause
    show keeves a_phone with dissolve
    pause
    keeves "Halo?"

    pause
    keeves "Ya, ini aku."

    pause
    keeves "You know that problem you wanted my help with?"

    show keeves with dissolve:
        xoffset 0
        xzoom 1
    pause
    keeves "Well, I think I can help you out after all..."

    keeves "... Assuming you can still afford me?"

    pause
    keeves f_laugh "Bagus sekali."

    return


label ano22_sign_headstone.wait:
    scene expression background(360, 448, 4.) as stage
    show anon a_sides f_worried_low at flip with dissolve
    anon @ -m_talk "( I'm ready, but it's too dark to see anything right now. )"

    anon @ -m_talk "( I should come back tomorrow when the sun is shining. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
