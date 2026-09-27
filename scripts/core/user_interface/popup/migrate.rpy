screen popup_migrate():
    modal True tag popup

    zorder 100

    use popup_warning():
        text _("This save has been migrated!")
        text _("An attempt has been made to make this older save compatible with the current version of the game. Any routes affected by new content MIGHT be reset (completely, or just a bit) and the items associated with them added or removed from your inventory (along with a refund for the more expensive items) to allow you to continue.")
        text _("{b}This is not a bug!{/b}")
        text _("Just an unfortunate side effect of our Patreon funded business model, coupled with Summertime Saga's sandbox-like gameplay.")
        text _("Please understand that at this point in development we cannot guarantee save compatiblity.")
        text _("Best of luck and happy fappy!")

    key 'dismiss' action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
