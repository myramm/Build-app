init python in popup:
    def bugs(win):
        if win:
            return ('popup_notice',
                    _('You have killed the {=bugs_keyword}BUGS{/}!'),
                    _('The garden is no longer {b}infested{/b}.'),
                    'popup_bugs_pass')
        else:
            return ('popup_notice',
                    _('You were not able to kill the {=bugs_keyword}BUGS{/}!'),
                    _('The garden is still {b}infested{/b}.'),
                    'popup_bugs_fail')


    def cat():
        return ('popup_notice',
                _('The kitten now lives in your room!'),
                '[cat_name]',
                'character_cat_01')


    def computer(fixed):
        if fixed:
            return ('popup_notice',
                    _('Your computer is {=repair_keyword}REPAIRED{/}!'),
                    _('You can now play games and do your homework!'),
                    'popup_computer_repair')
        else:
            return ('popup_notice',
                    _('Your computer is {=broken_keyword}BROKEN{/}!'),
                    _('You\'ll need to buy new parts before you can repair it.'),
                    'popup_computer_broken')


    def larry():
        return ('popup_notice',
                _('Larry is now in jail at the {=location_keyword}POLICE STATION{/}!'),
                _('You can visit him in the {b}cells{/b}.'),
                'popup_larry')


    def valve():
        return ('popup_notice',
                _('You have shut off the {=object_keyword}WATER VALVE{/}!'),
                _('The flooding should subside now.'),
                'popup_valve')


style bugs_keyword:
    color 'bf7f58'

style broken_keyword:
    color 'ff3000'

style repair_keyword:
    color '21ff3b'

style object_keyword:
    color 'abc6f2'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
