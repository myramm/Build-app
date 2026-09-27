image popup_poor = Fixed(Transform('popup_money', align=(.5, .5)),
                         Transform('popup_denied', align=(.5, .5)),
                         maximum=(300, 125))


init python in popup:
    def earn(value):
        return ('popup_money',
                value,
                _('Money can be {b}banked{/b} or {b}spent{/b} around Summerville.'))


    def poor():
        return ('popup_notice',
                _('You do not have enough {=money_keyword}MONEY{/}!'),
                _('Earn money by doing {b}jobs{/b} around Summerville.'),
                'popup_poor')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
