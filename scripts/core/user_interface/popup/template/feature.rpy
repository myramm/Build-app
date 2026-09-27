init python in popup:
    def feature(ref):
        return ('popup_notice',
                _('You have unlocked a new {=feature_keyword}FEATURE{/}!')) \
             + feature.data[ref]


    feature.data = {
        'easel': (_('You can now use the easel.'), 'item_easel1'),
        'tv': (_('You can now watch TV.'), 'popup_feature_tv')}


style feature_keyword:
    color 'fff6c6'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
