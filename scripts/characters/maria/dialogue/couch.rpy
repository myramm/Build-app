label maria_button_couch:
    show maria a_wine
    show anon with dissolve:
        flip
        xoffset 100
    anon "Hey, {b}Maria{/b}."
    anon "Enjoying your evening?"
    maria "You betcha."
    maria a_wine_give "You wanna join me for a glass?"
    pause
    maria a_wine f_confused "You're old enough to drink, aren't you?"
    anon f_shy a_behind_head "Ehh, technically..."
    anon "... No."
    show anon a_idle with dissolve
    maria f_normal "Hehe, I'd better hold onto this."

    menu maria_button_couch.choice:
        "What are you watching?":

            jump maria_button_couch.soccer

        "Sex." if M_anon.finished_state(S_ano11_bone):
            jump maria_button_couch.sex
        "Good night.":

            pass

    anon f_normal "Good night."
    if M_anon.finished_state(S_ano11_bone):
        maria f_normal "Oh, okay."
        maria "Be careful out there."
    else:
        maria f_normal "Good night, kid."
    maria "Be careful goin' home, yeah?"
    anon @ a_wave "I will be."
    hide anon with dissolve
    return


label maria_button_couch.soccer:
    anon f_normal "What are you watching?"
    maria f_normal "I'm watching the game."
    anon "Baseball?"
    maria @ f_disgusted "Eww, no way!"
    maria "I'm a soccer girl."
    anon "You like soccer?"
    maria f_annoyed "I'm Italian, aren't I?"
    anon "Yeah, but since {b}Tony{/b}'s so into baseball I just assumed-"
    maria @ f_eyeroll "{b}Tony{/b} doesn't know what he's talking about."
    maria "If it doesn't have grown men hitting each other or smashing things with wooden sticks, he's not interested."
    pause
    maria "He has no appreciation for the technique and finesse the game requires at high level play..."
    maria "... Says it's just a sport for crybabies and women."
    anon @ f_skeptical "Really?"
    maria f_sad "{i}*Sigh*{/i} I gave up on trying to get him interested years ago."
    maria f_normal "But it doesn't stop me from enjoying it."
    jump maria_button_couch.choice


label maria_button_couch.sex:
    anon f_flirt "Want to have sex?"
    maria f_surprised "What, now?"
    anon "Yeah, why not?"
    maria f_sexy @ f_sexy_lipbite -m_talk "Mmm."
    maria "I suppose we should do it as often as possible..."
    pause
    maria f_shy "... You know, since we're trying to concieve."
    anon "Definitely."
    maria f_sexy "What do you say, we move this to the bedroom then?"
    anon "I'm right behind you."
    hide anon
    hide maria
    with dissolve
    return 'sex'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
