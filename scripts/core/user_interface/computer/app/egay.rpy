screen pc_app_egay(app):
    style_prefix 'app_egay'

    $ app.tmp.init(host='https://www.egay.cum', last='', path='/', query='')

    use pc_app_web(app):
        vbox:

            fixed:
                style_prefix 'app_egay_search'

                add 'pc_egay_search'
                text _('Search for items')

                if app.focused:
                    input:
                        style_prefix 'app_egay_text'
                        pixel_width 215
                        value DictInputValue(pc.tmp.apps[app.ref], 'query')
                    key 'input_enter' action computer.apps.egay.search(app)
                else:
                    label app.tmp.query:
                        style 'app_egay_text_input'

            frame:
                style_prefix 'app_egay_header'

                has hbox

                if app.tmp.path in ('/', '/search'):
                    fixed:
                        style_prefix 'app_egay_spotlight'
                        add 'pc_egay_spotlight'
                        text _('75% OFF'):
                            at Transform(rotate=-12.5, rotate_pad=False)

                    text _('On all\nsummer items!'):
                        style_suffix 'promo_text'

                if app.tmp.path == '/orcette':
                    fixed:
                        style_prefix 'app_egay_spotlight'
                        add 'pc_egay_spotlight' xzoom .75
                        add 'pc_egay_orcette' align .5, .5
                        text '$300':
                            style_suffix 'price_text'

                    vbox:
                        add 'pc_egay_brand' xalign .5
                        text _('Free shipping!'):
                            style_suffix 'brand_text'

                if app.tmp.path == '/purchase':
                    add 'pc_egay_success' align .5, .5
                    text _('Congratulations!')
                    add 'pc_egay_cart' align .5, .5

            frame:
                style_prefix 'app_egay_body'

                if app.tmp.path == '/':
                    hbox:
                        style_prefix 'app_egay_home'
                        fixed:
                            add 'pc_egay_stick'
                            text _('Selfie Stick')
                        fixed:
                            add 'pc_egay_spinner'
                            text _('Meat Spinner')
                        fixed:
                            add 'pc_egay_board'
                            text _('Hoverboard')

                if app.tmp.path == '/search':
                    text _('- No items found -')

                if app.tmp.path == '/orcette':
                    vbox:
                        style_prefix 'app_egay_product'

                        text _('{b}{size=+2}Zug Zug!{/size}{/b}')
                        text _('Go where no manhood has gone before past the alluring pussy of the Orcette. This mesmerizing pearlescent green begs to eat you up for a close encounter of the preferred kind. The Orcette Fleshlight comes with the pearlescent green Orc sleeve and a deep green outer case that combine to take your orcette fantasy to the outer limits of your imagination.')

                        textbutton _('Purchase now!'):
                            action Return(If(player.has_money(300),
                                         (app.tmp.set('path', '/purchase'),
                                          Call('pc_hook_egay_buy_success')),
                                         Call('pc_hook_egay_buy_failure')))

                if app.tmp.path == '/purchase':
                    text _('Your payment went through!\nYour package should arrive\non {color=00f}{u}TUESDAY{/u}!{/color}')


init python in computer.apps.egay:
    from renpy import store
    from renpy.store import NullAction, Return

    from store.computer.apps import Update


    def orcette_quest_active():
        return store.M_erik.is_state(store.S_erik_orc_order)


    def search(app):
        rv = []
        
        if app.tmp.query != app.tmp.last:
            rv.append(app.tmp.set('last', app.tmp.query))
            rv.append(app.tmp.set('query', app.tmp.query))
        
        if app.tmp.query.lower() == 'orcette' and orcette_quest_active():
            if app.tmp.path != '/orcette':
                rv.append(Update(app.ref, 'path', '/orcette'))
        else:
            if app.tmp.path != '/search':
                rv.append(Update(app.ref, 'path', '/search'))
        
        return Return(rv) if rv else NullAction()


    text_color = '12213f'
    text_outline = ((1, '0004', 0, 1),)


style app_egay_body_frame:
    background 'pc_egay_body'
    padding (14, 10, 14, 0)
    xysize (550, 150)

style app_egay_body_text:
    align (.5, .45)
    color computer.apps.egay.text_color
    outlines computer.apps.egay.text_outline
    size 18
    text_align .5

style app_egay_frame:
    margin (10, 10, 10, 0)

style app_egay_header_brand_text:
    color computer.apps.egay.text_color
    outlines computer.apps.egay.text_outline
    size 20
    xalign .5

style app_egay_header_frame:
    background 'pc_egay_head'
    padding (14, 2, 14, 2)
    xsize 550

style app_egay_header_hbox:
    spacing 10
    xfill True
    ysize 108

style app_egay_header_promo_text:
    align (.5, .5)
    color '536d9f'
    outlines computer.apps.egay.text_outline
    size 30
    text_align .5

style app_egay_header_text:
    align (.5, .5)
    bold True
    outlines ((1, '0003', -1, -1),)
    size 26

style app_egay_header_vbox:
    align (.5, .6)
    spacing 6
    xfill True

style app_egay_home_fixed:
    fit_first True

style app_egay_home_hbox:
    align (.5, 1.)
    spacing 25

style app_egay_home_text:
    align (.5, .075)
    color computer.apps.egay.text_color
    outlines computer.apps.egay.text_outline
    size 18

style app_egay_product_button:
    idle_background 'pc_egay_buy_idle'
    hover_background 'pc_egay_buy_over'
    padding (30, 9)
    xalign .5

style app_egay_product_button_text:
    bold True

style app_egay_product_text:
    color computer.apps.egay.text_color
    size 13
    xalign .5

style app_egay_product_vbox:
    spacing 6

style app_egay_search_fixed:
    fit_first True

style app_egay_search_text:
    align (.775, .25)
    color computer.apps.egay.text_color
    outlines computer.apps.egay.text_outline

style app_egay_spotlight_fixed:
    fit_first True

style app_egay_spotlight_price_text:
    align (.5, 1.)
    outlines ((2, '000', 0, 0),)
    size 18
    bold True

style app_egay_spotlight_text:
    align (.5, .5)
    bold True
    outlines ((1, '0009', -1, 1),)
    size 45

style app_egay_text_input:
    background '#0000'
    caret Solid('333', xsize=1)
    color '333'
    anchor (0., .7)
    pos (.525, .715)

style app_egay_text_input_text:
    color '333'

style app_egay_vbox:
    first_spacing 10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
