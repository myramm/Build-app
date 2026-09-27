screen popup_shop(item, buy_action, own_action):
    imagebutton:
        action Hide('popup')
        idle 'clear'

    use popup_generic():
        style_prefix 'shop_popup'

        vbox:

            label _('{=item_keyword}ITEM{/}: [item.name]')

            frame:
                minimum (300, 125)
                has transform
                maxsize (300, 125)
                frame:
                    minimum (300, 125)
                    add item.image align .5, .5

            button:
                action BuyItem(item, buy_action, own_action)
                has hbox
                frame:
                    style_prefix 'shop_popup_cost'
                    text '[item.cost]'
                frame:
                    style_prefix 'shop_popup_buy'
                    text _('BUY')


style shop_popup_button is default:

    xalign .5

style shop_popup_frame is default:

    align (.5, .5)

style shop_popup_label:
    xalign .5

style shop_popup_buy_frame:
    hover_background 'shop_text_over'
    idle_background 'shop_text_idle'
    padding (20, 8)
    ysize 53

style shop_popup_buy_text:
    anchor (.5, .5)
    outlines ((2, '0006', 1, 2), (0, 'fff', 0, 0))
    pos (.5, .6)
    size 20

style shop_popup_cost_frame:
    hover_background 'shop_cost_over'
    idle_background 'shop_cost_idle'
    padding (20, 8, 55, 8)
    ysize 53

style shop_popup_cost_text:
    anchor (.5, .5)
    bold True
    outlines ((2, '0006', 1, 2),)
    pos (.5, .6)
    size 25
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
