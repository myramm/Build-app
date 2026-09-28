label con02_job1_church:
    scene expression player.location.background_blur with None
    show anon:
        xoffset 100
    show consuela b_casual f_sad:
        flip
        xoffset -100
    show keeves f_happy
    with dissolve
    anon "Hello, {b}Father Keeves{/b}."
    keeves "Heeey, how's it going, little dude?"
    anon "This is {b}Consuela{/b}, the woman I told you about."
    keeves "Ahh, excellent!"
    keeves "Hello, {b}Consuela{/b}." (show_native="Hola, {b}Consuela{/b}.")
    keeves @ a_point "You are stunningly beautiful." (show_native="Eres asombrosamente hermosa.")
    consuela a_cover f_smirk "Oh, you're too kind, Father..." (show_native="Ay, es usted muy amable Padre...")
    anon @ f_surprised "Whoa."
    show consuela f_normal a_hips with dissolve
    anon "You speak Spanish, {b}Father Keeves{/b}?"
    keeves f_confused "I do?"
    anon f_unimpressed "You just did..."
    keeves f_happy @ f_normal "Oh."
    keeves "Then yeah, I guess I do."
    keeves @ a_rock f_laugh "Most excellent!"
    consuela "Are you really going to hire me?" (show_native="¿De verdad me va a dar trabajo?")
    keeves "Of course, pretty lady!" (show_native="Por supuesto, bella dama!")
    keeves "Anything for you!" (show_native="¡Cualquier cosa por ti!")
    show anon b_empty f_surprised_down zorder 1:
        flip
        xoffset -450
    show consuela b_dressed_hug zorder 0:
        xoffset -450
    with dissolve
    anon "!!!"
    consuela "Oh, thank you, {b}Mister [firstname]{/b}!" (show_native="Oh, gracias, {b}Mister [firstname]{/b}!")
    consuela "Thank you!" (show_native="Gracias!")
    anon f_shy_down @ f_brag_closed "Y-you're welcome."
    pause
    keeves @ a_point "That's it, little dude..."
    keeves "Soak that in."
    keeves "Enjoy the moment."
    show anon f_shy b_dressed:
        unflip
        xoffset 100
    show consuela b_casual:
        xoffset -100
    with dissolve
    pause
    show keeves with dissolve:
        flip
        xoffset 500
    keeves "Hey, {b}Sister Angelica{/b}!"
    keeves "Can you come here for a second?"
    angelica "Ugh, just a second..."
    pause
    show keeves:
        xoffset 400
    show angelica:
        xoffset 100
    with dissolve
    angelica "What?"
    consuela a_cover f_surprised "{i}*Gasp*{/i}"
    consuela "A demon..." (show_native="Un demonio...")
    show keeves with dissolve:
        unflip
        xoffset -100
    keeves "This here is {b}Consuela{/b}."
    keeves "She's going to be cleaning up the chapel from now on."
    angelica f_smirk "Oh, really?"
    angelica "Nice to meet you, {b}Consuela{/b}."
    consuela f_sad a_cross "Oh, no..." (show_native="Ay, no...")
    consuela "Don't touch me, demon!" (show_native="¡No me toques, demonio!")
    anon f_worried_left @ -m_talk "Hmm?"
    anon "What's the matter?"
    consuela "This woman is evil!" (show_native="¡Esta mujer es malvada!")
    consuela "We have to go!" (show_native="¡Tenemos que irnos!")
    anon f_worried "What is she saying, {b}Father Keeves{/b}?"
    keeves "No idea, little dude..."
    keeves "I can't speak Spanish."
    anon @ f_unimpressed "But you were just-"
    show consuela b_casual_fear:
        xoffset -191
    show anon b_empty f_worried_left
    with dissolve
    consuela "Come!"
    consuela "We go now!"
    anon "!!!"
    hide consuela
    hide anon
    with dissolve

    $ player.go_to(L_church_front)
    scene expression player.location.background_blur with fade
    show anon f_worried
    show consuela b_casual f_sad a_cross
    with dissolve
    anon "What the heck was that?"
    consuela a_crossed "Bad lady!"
    consuela "I no clean!"
    anon @ f_skeptical "You don't like the nun?"
    consuela f_annoyed "Bad lady!"
    anon @ -m_talk "..."
    anon "So, what now?"
    show consuela a_idle with dissolve:
        flip
        xoffset 600
    pause 1
    anon f_surprised "Hey, hold on a second!"
    hide consuela
    show consuela b_casual f_annoyed a_crossed
    anon f_worried @ a_point "Where are you going?"
    consuela @ -m_talk "..."
    consuela "Mall."
    consuela "I go."
    anon "What?"
    anon "No, don't go back to the mall..."
    anon "{i}*Sigh*{/i} Just give me a second to think, okay?"
    consuela @ -m_talk "..."
    show anon f_thinking a_thinking with dissolve
    pause
    show consuela a_hips with dissolve
    pause
    anon "Maybe you could work {b}at my school{/b}?"
    consuela "School?"
    anon f_normal "Yeah, like a janitor or something?"
    consuela @ -m_talk "..."
    consuela "Okay."
    anon f_surprised "Yeah?"
    consuela "I clean school."
    anon f_normal a_idle "Let's hope so."
    anon "C'mon, {b}we can head there now{/b}."
    hide anon with dissolve
    hide consuela with dissolve

    scene black with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
