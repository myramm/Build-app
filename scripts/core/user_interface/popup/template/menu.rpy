image popup_compat = Fixed(Transform('item_usb1', align=(.5, .5), zoom=.65),
                           Transform('popup_denied', align=(.5, .5)),
                           maximum=(300, 125))


init python in popup:
    def compat():
        return ('popup_notice',
                _('Your save file is {=menu_keyword}INCOMPATIBLE{/}!'),
                _('Save compatibility is not supported yet, sorry!'),
                'popup_compat')


    def locked(ref):
        return ('popup_notice',
                locked.data[ref],
                _('Unlock scenes for characters by advancing their story.'),
                'popup_padlock')


    locked.data = {
        'character': _('This character is still {=menu_keyword}LOCKED{/}!'),
        'scene': _('This scene is still {=menu_keyword}LOCKED{/}!')}


style menu_keyword:
    color '818d98'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
