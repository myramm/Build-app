label erikshouse_erik_intro_known:
    scene erikhouse
    show anon with dissolve
    show erik f_worried with dissolve
    anon @ a_wave "Hey, {b}Erik{/b}!"
    erik "Hey, {b}[firstname]{/b}..."
    anon f_worried "You look really tired... You alright?"
    erik "Well, I was on the computer all night playing this new game that came out..."
    show erik b_dressed_depressed with dissolve
    erik "... And I just hate going to school."
    show erik b_dressed
    erik "I wish I could just stay at home all the time."
    anon "Yeah, I hear ya..."
    erik "Sorry to hear about your dad, by the way. How are you holding up?"
    anon f_sad_down "I'll be alright, man. Thanks for asking!"
    anon "We should really get going before we're late for class."
    hide anon
    hide erik
    with dissolve
    return

label erikshouse_erik_intro_started:
    scene erikhouse
    show player 11 at left
    show old_erik 5 at right
    erik "Shouldn't we be going to {b}school{/b}?"
    show old_erik 1 at right
    show player 14 at left
    player_name "Oh, yeah. You're right..."
    hide player 14 at left
    hide old_erik 1 at right
    hide erikhouse
    return

label eriks_mailbox_magazine:
    show expression "objects/object_mailbox_item01_closeup.png" with {'master': dissolve}
    player_name "( Huh. A magazine. I wonder who it could be for... )"
    player_name "( Milfness? Well, I know it's for {b}Mrs. Johnson{/b}. I didn't know she subscribed to these, though... )"
    player_name "( I'd better put this back. )"
    hide expression "objects/object_mailbox_item01_closeup.png" with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
