image popup_map = HBox('ui_piece_map_locked',
                       Crop((0, 0, 20, 30), 'to', align=(.5, .5)),
                       'ui_piece_map',
                       spacing=30)


init python in popup:
    def area(loc):
        return ('popup_notice',
                _('You have unlocked a new {=location_keyword}AREA{/}!'),
                loc.name,
                'popup_area_{}'.format(loc.formatted_name))


    def location(loc):
        return ('popup_notice',
                _('You have unlocked a new {=location_keyword}LOCATION{/}!'),
                loc.name,
                loc.miniature(adjust_timer=False))


    def map():
        return ('popup_notice',
                _('You can now access the {=map_keyword}MAP{/}!'),
                _('Use it to visit {b}other locations{/b} in Summerville.'),
                'popup_map')


style location_keyword:
    color '5eafe8'

style map_keyword:
    color 'aad51c'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
