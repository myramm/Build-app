label ano27_tony_pizzeria_interior:
    scene expression game.timer.image('location_warehouse_office_couch{}') as underlay:
        xoffset -671
    show nadya b_dressed_couch a_phone_talk f_angry:
        xoffset -500

    $ renpy.dynamic(stage=background(400, 368, 2.5, t=2))
    show expression stage as stage
    show tony a_pipe_touch b_casual f_angry:
        xoffset -250
    show maria b_casual_magic f_sad:
        xoffset -200
        xzoom -1
    tony "Buncha cowards, goin' after defenseless women!"
    tony "They're gonna get what's comin' to 'em and more!"
    show maria f_surprised
    show anon b_dressed_catch_breath behind tony:
        xoffset 100
        xzoom -1
    with {'master': dissolve}
    anon "Haah... Haah... I'm here!"
    show tony a_pipe_hold_shoulder f_suspicious with dissolve:
        xoffset 0
        xzoom -1
    maria "Thank goodness you're alright!"
    maria f_sad "Can your contact inside help?"
    show anon a_sides b_dressed f_worried with {'master': dissolve}:
        xoffset 50
    anon @ -m_talk "Hmm?"
    maria "The bosses' daughter or whatever... did you try callin' her?"
    anon "No."
    pause
    anon @ f_confused "... Should I?"
    maria "Well, yeah... maybe she can tell you what's going on?"
    anon "{b}Tony{/b}?"
    tony f_sad "Ehh..."
    tony "... Seems like a big risk to me."
    maria "What do you mean?"
    tony "Far as we know, she's the one who sent 'em to his house!"
    anon "N-no, I don't think so..."
    anon "... The cop stationed at our house said the Russians were looking for the briefcase."
    anon "That means {b}Raz{/b} sent them."
    tony f_thinking @ -m_talk "Hmm."
    pause
    tony f_suspicious @ a_pipe_point "I dunno, it's your call, champ."
    maria f_annoyed "He should call her!"
    show tony with {'master': dissolve}:
        xoffset -410
        xzoom 1
    tony "I don't trust the bitch."
    maria "The two of you can't do it alone!"
    show tony a_pipe_touch f_smirk with {'master': dissolve}:
        xoffset 0
        xzoom -1
    tony "Vera and I seen worse odds!"
    maria f_glaring @ f_angry "{b}Tony{/b}!"
    show tony a_pipe_hold_shoulder with dissolve
    anon "I'll call her."
    show maria f_shy
    tony f_sad @ -m_talk "Hmm?"
    anon "She's right, {b}Tony{/b}."
    anon "We could use the help."
    show anon f_sad_down a_phone with dissolve
    tony f_suspicious "Suit ya self."
    show anon f_worried a_phone_talk with dissolve:
        xoffset 550
        xzoom 1
    "{i}*Ring* *Ring*{/i}"
    anon @ -m_talk "( I hope she answers... )"
    "{i}*Ring* *Ring*{/i}"
    show tony m_talk with dissolve:
        xoffset -410
        xzoom 1
    hide tony
    hide maria
    show expression stage as stage at phoneleft
    with phoneleft.show
    nadya "Da?"
    anon "Yeah, it's me."
    anon "Your father's goons took my friends!"
    nadya "Yes, I know."
    anon f_worried "Have you seen them?!"
    anon "Are they okay?!"
    nadya "I do not know."
    show anon f_worried_surprised
    anon f_skeptical "What do you mean, you don't know?!"
    nadya "They are here, in warehouse..."
    nadya "... {b}Dimitri{/b} prepares them for questioning."
    anon f_angry "That's not happening!"
    anon "We're going in tonight!"
    nadya f_worried "No, is too soon..."
    anon f_annoyed "I'm not going to let them hurt my friends, {b}Nadya{/b}!"
    nadya "... I have not turned men against father ye-"
    anon f_angry "{b}Nadya{/b}, we're going tonight!"
    show nadya f_angry
    anon "End of story."
    pause
    anon f_annoyed "If there's anything you can do to help us, I need you to do it now!"
    nadya "What you want me do, pull miracle out of ass?!"
    nadya "No one talks to me this way, I am-"
    anon "You're wasting time!"
    pause
    nadya "Grr, fine!!"
    nadya "I will make calls and try to help... but I make no promises!"
    nadya "{b}Meet me at sewage drain entrance in twenty minutes{/b}."
    anon "Yes, okay!"
    anon "We'll be there."
    nadya "You fuck this up and I haunt you in afterlife!"
    nadya "Stubborn American fool!" (show_native="Upryamyy Amerikanskiy durak!")
    show nadya a_phone with {'master': dissolve}
    anon f_skeptical "Huh?"
    show tony a_pipe_hold_shoulder b_casual f_suspicious:
        xoffset -410
    show maria b_casual_magic f_sad:
        xoffset -200
        xzoom -1
    show expression stage as stage
    with {'master': phoneleft.hide}
    "{i}*Beep*{/i}"
    anon "{b}Nadya{/b}?"
    pause
    show anon f_sad_down a_phone with {'master': dissolve}:
        xoffset 50
        xzoom -1
    anon "She hung up."
    show tony f_sad:
        xoffset 0
        xzoom -1
    with {'master': dissolve}
    tony "Told ya it was a bad idea."
    show anon f_worried a_sides with {'master': dissolve}
    maria "She's not gonna help?"
    anon "N-no, she said she'd make some calls and meet us in front of the building in twenty minutes."
    anon "C'mon, {b}Tony{/b}... we need to hurry."
    tony f_smirk @ a_pipe_touch "You got it, champ!"
    maria "This is all happening too fast..."
    show maria with {'master': dissolve}:
        xoffset -150
        xzoom 1
    maria "... I don't like it, {b}Tony{/b}."
    tony f_smirk "'Ey, c'mon darlin'... have a little faith in us, eh?"
    show tony b_casual_hug1 f_surprised
    hide maria
    with {'master': dissolve}
    pause
    tony f_smirk "Everything will be fine, I promise."

    if M_tony.watches:
        show tony b_casual_hug2 with dissolve
        tony "C'mere, ya knucklehead."
        show tony b_casual_hug3
        hide anon
        with dissolve
        pause
        tony "Cook us up somethin' nice, will ya?"
        tony "We're gonna be good and hungry when we get back, right, champ?"
        anon "Y-yeah."
        maria "You betta take care of him, {b}Tony{/b}."
        tony "Heh, I will darlin'."
        tony "I will."
    else:
        show tony b_casual a_pipe_hold_shoulder
        show anon f_worried_low
        show maria b_casual_magic f_sad:
            xoffset 200
            xzoom -1
        with dissolve
        maria "C'mere, handsome."
        show maria b_casual_hug_mc behind anon:
            xoffset 50
        show anon b_empty
        with dissolve
        pause
        tony "Cook us up somethin' nice, will ya?"
        show anon f_worried
        tony "We're gonna be good and hungry when we get back, right, champ?"
        anon "Y-yeah."
        maria "You betta take care of him, {b}[firstname]{/b}."
        anon "I will."
        show tony behind maria
        show anon b_dressed behind tony
        show maria b_casual_magic f_sad:
            xoffset 200
            xzoom -1
        with {'master': dissolve}
        maria "You'd betta!"
        show anon f_surprised_left
        show maria f_surprised

    show tony f_surprised
    harold "So these are the friends you keep bringing up?"
    show maria f_sad b_casual_magic:
        xoffset -200
        xzoom -1
    show tony f_angry b_casual behind maria:
        xoffset 0
    show anon f_annoyed b_dressed behind tony:
        xoffset 200
        xzoom 1
    with {'master': dissolve}
    tony "What the fuck are you doin' here?!"
    show harold behind tony with {'master': dissolve}:
        xoffset 100
    harold "I'm trying to protect the kid."
    tony @ f_eyeroll "Oh, well you've done a great job of that so far!"
    tony f_angry "You know the Russians took his friends on your watch?!"
    harold f_angry_down "Yes, I know."
    tony "Why don't ya just go back to your nice little police station and have some donuts..."
    show harold f_angry
    tony "... We'll handle things from here."
    harold "Can't do that."
    pause
    show tony a_pipe_point with dissolve
    tony "Am I gonna have to put ya down?!"
    tony "'Cause I got no problem-"
    harold "I'm coming with you."
    show tony f_surprised
    show maria f_surprised
    anon f_surprised "Huh?!" with hpunch
    tony a_pipe_hold_shoulder "The hell you say?!"
    harold "I know you're going to that warehouse..."
    show maria f_sad
    harold "... And you're gonna need my help."
    show anon f_annoyed
    tony f_smirk "{i}*Snort*{/i} Yeah, right."
    harold f_angry "I'm done doing things by the book!"
    harold "Those assholes crossed a line tonight, taking your friends!"
    show harold f_worried
    pause
    harold "And they almost killed {b}Yumi{/b}..."
    show anon f_worried
    show tony f_suspicious
    pause
    harold "... I can't let it lie."
    pause
    tony "Well, we ain't exactly goin' there to arrest 'em, Officer Do-good!"
    tony "You and your morals are just gonna get in the way of what needs doin'!"
    harold "That's not gonna be a problem."
    tony @ f_question "Eh?"
    show anon f_worried_low
    show harold a_remove_badge f_angry_badge
    with dissolve
    pause
    show harold a_remove_badge_look f_angry_down with dissolve
    harold "I'm not a cop tonight."
    show anon f_surprised_down
    show maria f_sad_down
    show harold a_remove_badge_throw
    with {'master': dissolve}
    tony "This fuckin' guy..."
    show anon f_surprised
    show maria f_sad
    show harold a_remove_shirt1
    with dissolve
    pause
    show harold b_tanktop a_remove_shirt2 with dissolve
    tony f_smirk "... He thinks he's in an action movie or something."
    show harold b_tanktop a_remove_shirt3 with dissolve
    anon f_sad_down @ -m_talk "..."
    show tony f_sad
    show harold b_tanktop f_angry a_idle with dissolve
    tony "Don't tell me you're considerin' this..."
    show anon f_worried with {'master': dissolve}:
        xoffset -250
        xzoom -1
    anon "He's right, {b}Tony{/b}... we need all the help we can get."
    tony "Ugh, lord help me."
    show tony f_angry
    pause
    tony "Just stay out of my fuckin' way, you hear me?!"
    show anon with dissolve:
        xoffset 200
        xzoom 1
    pause
    harold "Yeah, I got it."
    tony f_smirk "Good."
    tony "Let's get this fuckin' show on the road then."
    hide tony
    show harold:
        xoffset 600
        xzoom -1
    with {'master': dissolve}
    tony "Vera's itchin' to crack some Ruskie skulls!"
    hide harold with dissolve
    pause
    show anon with {'master': dissolve}:
        xoffset -300
        xzoom -1
    maria "Just, please come back safe, okay?"
    anon a_liu_shoulder "We will."
    hide anon with dissolve

    scene expression background(760, 512, 3, l=L_pizzeria_exterior) as stage
    show tony b_casual f_suspicious a_pipe_hold_shoulder:
        xoffset 100
    show harold b_tanktop:
        xoffset -200
    with fade
    show anon f_worried a_sides with dissolve:
        xoffset -100
    harold "How are you planning to get past the guards?"
    anon "I have a contact on the inside."
    anon "She's gonna help us."
    harold f_surprised "Someone on the inside?!"
    harold f_suspicious "How in the hell did you manage that?"
    tony f_smirk "It's called doin' actual investigation work..."
    tony "... I guess they didn't teach you anything about that in the police academy, eh?"
    show harold f_angry with dissolve:
        xoffset 300
        xzoom -1
    harold "You're a real asshole, you know that?!"
    tony @ f_laugh "Hah!"
    tony "Better an asshole than a worthless fuckin' cop."
    pause
    anon f_angry a_frustrated "Enough!"
    show tony f_sad
    show harold b_tanktop f_worried:
        xoffset -200
        xzoom 1
    with {'master': dissolve}
    anon a_idle f_annoyed "Save it for the Russians, both of you!"
    anon "{b}Nadya is gonna be waiting for us in front of the warehouse{/b}..."
    hide anon
    show harold:
        xoffset 300
        xzoom -1
    show tony:
        xoffset 500
        xzoom -1
    with {'master': dissolve}
    anon "... We need to hurry."
    pause
    show tony a_pipe_point_back f_smirk with {'master': dissolve}:
        xoffset 100
        xzoom 1
    tony "After you, cupcake."
    show harold f_eyeroll
    pause
    hide harold
    show tony f_laugh a_pipe_hold_shoulder:
        xoffset 500
        xzoom -1
    with dissolve
    pause
    hide tony with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
