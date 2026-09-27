screen popup_recovery():
    modal True tag popup

    zorder 100

    use popup_warning():
        text _("This save could not be loaded normally!")
        text _("An attempt has been made to recover it so that play may continue, however you may experience unexpected behavior.")
        text _("Regrettably, If problems persist you may need to try different save (don't forget to check autosaves) or begin a new game.")

    key 'dismiss' action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
