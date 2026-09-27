screen popup_finale():
    modal True tag popup

    zorder 100

    side 'c t':
        style_prefix 'branch_popup'

        use popup_warning():
            text _('You are about to set off a chain of events that will prevent you from exploring the map until after the conclusion of the main story.')
            if player.stats._dex < 10 or player.stats._str < 10:
                text _('Make sure to {b}check your stats{/b} before proceeding!')
            null height 5
            hbox:
                textbutton _('Go Back') action Return(False)
                textbutton _('Continue') action Return(True)

        frame:
            style_prefix 'branch_popup_hint'
            text _('Remember to save!')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
