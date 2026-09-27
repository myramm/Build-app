init python in popup:
    def scene(ref):
        return ('popup_notice',
                _('You have unlocked a new {=scene_keyword}SCENE{/}!')) \
             + scene.data[ref]


    scene.data = {
        'deb_sex': (_('Sex with [deb_name]'), 'character_debbie_03'),
        'deb_shower': (_('Shower with [deb_name]'), 'popup_scene_deb_shower'),
        'deb_sleep': (_('Sleep in [deb_name]\'s bed'), 'popup_scene_deb_sleep'),
        'milker': (_('The Milker'), 'popup_scene_milker'),
        'seasucc': (_('The SeaSucc'), 'object_seathrone_01')}


style scene_keyword:
    color 'ae8bff'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
