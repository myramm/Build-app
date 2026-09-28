label police_lobby_pika_dialogue:
    scene location_police_lobby_pika
    anon "( Officer P. Kachu, huh? )"

    $ renpy.dynamic(rng=renpy.random.random())

    if rng < .15:
        anon "( Why does that name sound familiar? )"
        pause
        anon "( I bet he'd fit right into one of those Police Academy movies. )"

    elif rng < .30:
        anon "( Why does that name sound familiar? )"
        pause
        anon "( I'm starting to think over the top facial hair is a prerequisite of working here... )"

    elif rng < .45:
        anon "( Why does that name sound familiar? )"
        pause
        anon "( He looks like he's seen some crazy shit... )"

    elif rng < .60:
        pause
        anon "( Oh, it's got his personal motto written here... )"
        anon "( {i}\"Gotta catch 'em all!\"{/i} )"

    elif rng < .75:
        pause
        anon "( Just looks like a normal beat cop... )"
        anon "( ... But I guess if he's on this wall, he must be super effective! )"

    elif rng < .90:
        pause
        anon "( I think I saw him surfing down at the beach a while ago... )"
        anon "( It was only the once though. It must be super rare to catch him doing that. )"
    else:

        anon "( Woah look at that facial hair! )"
        pause
        anon "( What's that saying again? \"The bigger the beard the smaller the...\" )"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
