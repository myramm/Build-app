label ano25_find_maria_lounge:
    scene location_apt_hall3_301_closeup as stage
    show location_apt_hall3_302_closeup_door1 as door behind stage
    show location_apt_hall3_301_closeup as doorframe:
        crop (768, 0, 256, 768)
        right
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    anon a_sides f_worried @ -m_talk "( Hmm, I hope she's not sleeping... )"

    pause
    show anon a_knock with dissolve
    "{i}*Ketuk* *Ketuk*{/i}"

    show anon a_sides with dissolve
    anon "{b}Maria{/b}?"

    anon "Are you in there?"

    maria "{i}*AHHCHOOO*{/i}" with hpunch
    maria "Eugh, hold ya damn horses, I'm comin'..."

    pause
    show location_apt_hall3_302_closeup_door2 as door with dissolve
    show maria b_casual_magic f_annoyed a_handkerchief behind doorframe with dissolve:
        xoffset 50
    maria "What do ya want?!"

    maria f_surprised "Oh."

    anon "Did I wake you?"

    maria f_normal "Yeah, but that's alright."

    maria "Are you here to check on me?"

    anon f_normal "Errm, yeah... totally."

    show maria a_handkerchief_blow with {'master': dissolve}
    anon "Bagaimana perasaanmu?"

    maria f_taste @ -m_talk "{i}*Hrrnnn*{/i}"

    show maria a_handkerchief f_tired with {'master': dissolve}
    maria "Ya."

    maria "I've felt betta."

    maria "Damn head cold knocked me right on my ass!"

    show anon f_confused

    if M_maria.pregnancy.stage:
        anon "It's not going to hurt the baby is it?"

        maria "Oh, tidak..."

        maria "The doc said there was nothin' to worry about."

        maria "Prescribed cold medicine, lots of fluids, and rest."

    else:
        anon "Did you go see a doctor?"

        maria "Yeah, he said there was nothin' to worry about."

        maria "Prescribed cold medicine, lots of fluids, and rest."


    anon f_worried "And here I am, interrupting your rest."

    maria f_normal "Not at all, it's good to see you!"

    maria "I'd give ya a kiss but... well, you know."

    anon @ f_shy a_behind_head "Y-yeah, no... that's okay."

    anon "Ada yang bisa kuberikan padamu?"

    anon "Soup or some orange juice maybe?"

    maria "Nah, {b}Tony{/b}'s on it."

    maria "Told me he'd pick up a little care package full of goodies for me on his way home."

    anon f_shy "Good... good."

    maria a_handkerchief_blow f_taste @ -m_talk "{i}*Hrrnnn*{/i}"

    pause
    maria f_disgusted a_handkerchief "Ya."

    show maria f_tired
    anon f_worried "Well, I should probably let you get back to sleep, huh?"

    anon "Umm, before I go... {b}Tony{/b} said he had some tools stashed away I could borrow?"

    maria "Oh?"

    maria "Did something break?"

    anon "Y-yeah... umm, my..."

    anon @ f_shy "Uhh... dog."

    maria f_confused "Your dog?"

    anon "-'s house!"

    anon f_shy "My dog's house."

    maria f_sad "Oh tidak..."

    anon "Broke, last night actually..."

    maria "Poor puppers."

    anon f_worried "Ya."

    maria "Well, you're welcome to take whatever you want, of course..."

    maria "... If you can find it."

    maria "I got no idea where {b}Tony{/b} keeps that stuff."

    anon f_normal "Luar biasa!"

    hide maria with dissolve
    maria "Come on in."

    show anon with dissolve:
        xoffset 100
    anon "Thank you so much."

    anon "I'll be in and out, I promise."

    maria "Mhmmm."

    hide anon with dissolve
    maria "Just holler if you need somethin'."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
