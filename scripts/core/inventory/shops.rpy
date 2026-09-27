init python:
    class PinkItem:
        def __init__(self, item, name = "", image = "", idle = "", hover = "", price = 0, category = "", purchased = False):
            self.name = name
            self.image = image
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased


    class PinkStore (object) :
        def __init__(self):
            self.items = []

    class ComicItem:
        def __init__(self, item, name = "", image = "", idle = "", hover = "", price = 0, category = "", purchased = False, availability=None, callback=None):
            self.name = name
            self.image = image
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased
            self.availability = availability 
            self.callback = callback


    class ComicStore (object) :
        def __init__(self):
            self.items = []

    class CupidItem:
        def __init__(self, item, name = "", category = "", callback=None):
            self.name = name
            self.image = ""
            self.idle = Item(item).image
            self.hover = HoverImage(Item(item).image)
            self.price = Item(item).cost
            self.category = category
            self.item = item
            self.purchased = False
            self.callback = callback


    class CupidStore (object) :
        def __init__(self):
            self.items = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
