label mailbox_orcette:
    player_name "( Sweet! It looks like I'm the first one to get the mail! )"

    menu:
        player_name "The package is addressed to me. This must be {b}Erik{/b}'s toy."

        "Leave it alone.":
            pass
        "Open it.":
            show mailbox_item04_c at truecenter with dissolve
            pause
            player_name "( So this is what he's been waiting for... )"

            player_name "( The {b}Orcette{/b}. )"

            player_name "( I'd better put this back in the box. )"

            hide mailbox_item04_c with dissolve
    player_name "( Time to get this to {b}Erik{/b} before someone catches me carrying this thing around. )"

    call popup ('give', 'orcette')
    return

label mailbox_pizza_pamphlet:
    show expression "objects/object_mailbox_item02_closeup.png" with {'master': dissolve}
    player_name "( This is probably junk mail. )"

    player_name "( Tony's Pizza? I haven't been to that place in a while. )"

    player_name "( I'd better put this back. )"

    hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
    return

label mailbox_newspaper:
    show expression "objects/object_newspaper.png" with {'master': dissolve}
    player_name "( Local news. This should be interesting... )"

    player_name "( The thief is still on the loose? You'd think they would've caught him by now... )"

    player_name "( I'd better put this back. )"

    hide expression "objects/object_newspaper.png" with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
