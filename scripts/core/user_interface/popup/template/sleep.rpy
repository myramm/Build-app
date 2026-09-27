init python in popup:
    def groggy():
        return ('popup_notice',
                _('After a few hours, you feel {=sleep_keyword}GROGGY{/}.'),
                _('{#groggynote}'),
                'popup_sleep')


    def sleep():
        return ('popup_notice',
                _('After a full night of sleep, you feel {=sleep_keyword}RESTED{/}!'),
                _('{#sleepnote}'),
                'popup_sleep')


style sleep_keyword:
    color '99f4ff'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
