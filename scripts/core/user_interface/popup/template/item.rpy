init python in popup:
    def give(item):
        Item = renpy.store.Item 
        item = item if isinstance(item, Item) else Item(item)
        return ('popup_notice',
                _('You have a new item in your {=item_keyword}BACKPACK{/}!'),
                item.name, item.image)


    def shop(item, buy_action=None, own_action=None):
        Item = renpy.store.Item 
        item = item if isinstance(item, Item) else Item(item)
        return ('popup_shop', item, buy_action, own_action)


    def take(item):
        Item = renpy.store.Item 
        item = item if isinstance(item, Item) else Item(item)
        return ('popup_notice',
                _('An item was {=item_keyword}STOLEN{/}!'),
                item.name, item.image)


    def dupe(item):
        Item = renpy.store.Item 
        item = item if isinstance(item, Item) else Item(item)
        return ('popup_notice',
                _('You already have this {=item_keyword}ITEM{/}!'),
                item.name, item.image)


style item_keyword:
    color 'e00'
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
