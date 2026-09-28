label ronda_dialogue_intro:
    scene gym
    show ronda b_jersey
    show anon a_wave
    with dissolve
    anon "Hey, {b}Ronda{/b}. How are you?"
    show anon a_idle with dissolve
    ronda "I'm doing fine. The question is, have you been training?"
    anon f_worried_low @ -m_talk "..."
    anon "No-"
    show anon f_worried
    ronda f_upset @ f_upset_angry "Then stop moving those lips and start moving those... Legs!"
    anon f_skeptical @ -m_talk "???"
    ronda f_normal "Never mind. It's just something my dad always says..."
    show anon f_worried
    ronda "Anyway, you better hurry up 'cause the trials are coming up fast!"
    return

label ronda_dialogue_talent_show_help:
    anon f_worried "I don't suppose you'd be interested in volunteering for {b}Miss Dewitt{/b}'s musical talent show?"
    show ronda b_jersey f_normal
    ronda "Musical talent? No, I would not be interested."
    anon "Are you sure? You don't play any instruments or sing at all?"
    ronda "Umm, can't you see I have more important things to focus on. Like track and swimming..."
    ronda "Stuff you should be focusing on as well!"
    ronda "You're never gonna make the team if you keep ignoring your training!"
    anon @ f_skeptical "You know, there's more to life than sports, {b}Ronda{/b}..."
    ronda "Pfft, yeah right."
    return

label ronda_dialogue_model_help:
    show ronda b_jersey f_normal
    anon f_normal "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    anon @ a_point "Would you be interested?"
    ronda "Busy."
    anon f_worried "Busy?"
    anon "Doing what?"
    show ronda
    ronda f_upset_angry "For real, {b}[firstname]{/b}?!"
    ronda "I've gotta run 6 miles and hit an ice bath before soccer practice."
    show ronda f_upset
    anon f_surprised @ f_worried_low "Uhh..."
    ronda @ f_upset_angry "Afterwards, I've only got 40 minutes to get some laps in before the pool closes."
    anon "That's cra-"
    show anon f_surprised_teeth
    ronda @ f_upset_angry "Then it's back home to a heating pad and crunches."
    anon f_worried "OKAY! Okay! I got it..."
    hide ronda with dissolve
    anon f_surprised "That girl is insane!"
    return

label ronda_dialogue_leave:
    show anon
    anon "Alright."
    anon @ a_wave "See you later."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
