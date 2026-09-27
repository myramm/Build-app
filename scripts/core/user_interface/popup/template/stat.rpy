init python in popup:
    def chr(inc):
        if inc:
            return ('popup_notice',
                    _('You have won a {=chr_keyword}RAP BATTLE{/}!'),
                    _('You seem to be more {b}charismatic{/b}.'),
                    'popup_chr_pass')
        else:
            return ('popup_notice',
                    _('You have lost a {=chr_keyword}RAP BATTLE{/}!'),
                    _('You do not seem any more {b}charismatic{/b}.'),
                    'popup_chr_fail')


    def dex(inc):
        if inc:
            return ('popup_notice',
                    _('You have trained in {=dex_keyword}MUAY THAI{/}!'),
                    _('You seem to be more {b}agile{/b}.'),
                    'popup_dex_pass')
        else:
            return ('popup_notice',
                    _('You were not able to train {=dex_keyword}MUAY THAI{/}!'),
                    _('You do not seem any more {b}agile{/b}.'),
                    'popup_dex_fail')


    def int(inc):
        if inc:
            return ('popup_notice',
                    _('You have beaten {=int_keyword}THE MAZE{/}!'),
                    _('You seem to be {b}smarter{/b}.'),
                    'popup_int_pass')
        else:
            return ('popup_notice',
                    _('You were not able to beat {=int_keyword}THE MAZE{/}!'),
                    _('You do not seem any {b}smarter{/b}.'),
                    'popup_int_fail')


    def str(inc):
        if inc:
            return ('popup_notice',
                    _('You successfully {=str_keyword}LIFTED{/}, bro!'),
                    _('You seem to be {b}stronger{/b}.'),
                    'popup_str_pass')
        else:
            return ('popup_notice',
                    _('Do you even {=str_keyword}LIFT{/}, bro?'),
                    _('You do not seem any {b}stronger{/b}.'),
                    'popup_str_fail')


style chr_keyword:
    color 'ff6b23'

style dex_keyword:
    color '4effbe'

style int_keyword:
    color 'a7d5ff'

style str_keyword:
    color 'fd0000'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
