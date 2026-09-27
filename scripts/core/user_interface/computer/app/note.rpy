screen pc_app_note(app, title=None):
    style_prefix 'app_note'

    use pc_window(app, ' - '.join((title or __(app.title), __('Nopepad')))):
        vbox:

            hbox:
                null
                text _('File')
                text _('Edit')
                text _('View')
                add 'pc_note_bold' yanchor 8 ypos .5
                add 'pc_note_italic' yanchor 8 ypos .5
                add 'pc_note_underline' yanchor 8 ypos .5
                add 'pc_note_color' yanchor 8 ypos .5
                add 'pc_note_left' yanchor 8 ypos .5
                add 'pc_note_center' yanchor 8 ypos .5
                add 'pc_note_list' yanchor 8 ypos .5

            add Solid('aac', ysize=2)

            frame:
                has frame
                style_prefix 'app_note_doc'
                vbox:
                    transclude


init python hide:
    def error_tag(tag, argument, contents):
        yield (renpy.TEXT_TAG, 'rb')
        
        for tag in contents:
            yield tag
        
        yield (renpy.TEXT_TAG, '/rb')
        yield (renpy.TEXT_TAG, 'rt')
        for _ in xrange(0, int(argument or 2)):
            yield (renpy.TEXT_DISPLAYABLE, ImageReference('pc_note_mistake'))
        yield (renpy.TEXT_TAG, '/rt')


    config.custom_text_tags['e'] = error_tag


style app_note_doc_frame:
    background '#fff'
    padding (30, 20, 30, 60)

style app_note_doc_vbox:
    first_spacing 20
    spacing 10
    xfill True

style app_note_hbox:
    first_spacing 10
    spacing 20
    ysize 30

style app_note_frame:
    background '#aac'
    margin (50, 10, 50, 0)
    padding (2, 2, 2, 0)

style app_note_text:
    align (.5, .565)
    color '669'
    size 14

style app_note_vbox:
    xsize 600
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
