label lily_dialogue_pre:
    scene expression player.location.background_closeup with None
    show xtra 17 zorder 2
    show lily zorder 1
    show player 1 zorder 3 at left
    with dissolve
    lily "What's up?"
    return

label lily_dialogue_familiar:
    show player 4
    player_name "I feel like I've seen you somewhere."
    show lily f_laugh
    show player 1
    lily "Right. Well, you've probably seen me on the internet..."
    show lily f_normal
    lily "I do a lot of {b}video game streams{/b} and I post them on my {b}GooTube channel{/b}."
    show lily f_sexy
    lily "I usually go by the name of {b}VirginLily69{/b}."
    show player 17
    player_name "Oh, right! My friend {b}Erik{/b} loves your stuff!"
    show player 21
    player_name "He keeps talking about your videos and your {b}huge{/b}... Err... Fan base!"
    show lily f_laugh
    show player 1
    lily "Aww... You guys are so sweet."
    show lily f_normal
    lily "Is there anything else you want to talk about?"
    return

label lily_dialogue_suggestions:
    show player 2
    player_name "Do you have any suggestions? New products that you would recommend?"
    show player 1
    lily @ -m_talk "Hmmm..."
    show lily f_normal
    lily "Well, I really love cosplay!"
    show lily f_sexy
    lily "I like to wear {i}sexy outfits{/i}. Actually, we have a new line of costumes that just came in!"
    show player 21
    player_name "Oh, yeah? Sounds interesting..."
    show player 1
    lily "It's sometimes hard to fit my... Umm... Forms into them."
    lily "They make them so tight, you know?"
    lily @ f_laugh "But guys usually don't seem to mind!"
    show player 29
    player_name "Haha. I see."
    show player 2
    player_name "Thanks, I'll have a look."
    show lily f_normal
    return

label lily_dialogue_leave:
    show player 2
    player_name "Yeah, I think I have everything I need. Thanks!"
    show lily f_normal
    show player 1
    lily "Great! Thanks for shopping at {b}Cosmic Cumics{/b}..."
    show lily f_laugh
    show player 13
    lily "And tell your friends about us!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
