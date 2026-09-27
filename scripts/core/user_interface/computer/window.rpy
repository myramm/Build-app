screen pc_window(app, title=None, base='#fffc'):
    drag as self:
        style_prefix 'pc_window'
        drag_name app.ref
        droppable False
        dragged computer.apps.move
        clicked If(not app.focused, Return(app.show))
        pos app.pos


        $ self.z = app.z

        if self.z <= 0:
            null
        else:
            side 't tl tr l r bl b br c':

                side 't c b':
                    add 'pc_window_frame_h'

                    frame:
                        has hbox
                        text title or app.title
                        hbox:
                            style_suffix 'ctrl_hbox'
                            add 'pc_window_min'
                            add 'pc_window_max'
                            imagebutton:
                                idle 'pc_window_close_idle'
                                hover 'pc_window_close_over'
                                action Return(app.hide)

                    add 'pc_window_frame_h'

                add 'pc_window_frame_v'
                add 'pc_window_frame_v'
                add 'pc_window_frame_v'
                add 'pc_window_frame_v'
                add 'pc_window_frame_c'
                add 'pc_window_frame_h'
                add 'pc_window_frame_c'

                button:
                    action NullAction()
                    key_events True
                    background base

                    has fixed

                    transclude

                    if not app.focused:
                        imagebutton:
                            idle 'clear'
                            action Return(app.show)


init python hide:
    color = '40556a'
    size = 1

    renpy.image('pc_window_frame_h', Solid(color, ysize=size))
    renpy.image('pc_window_frame_v', Solid(color, xsize=size))
    renpy.image('pc_window_frame_c', Solid(color, xysize=(size, size)))


style pc_window_ctrl_hbox:
    spacing 3
    xalign 1.

style pc_window_fixed:
    fit_first True

style pc_window_frame:
    background '#669c'
    padding (6, 3, 3, 3)

style pc_window_hbox:
    xfill True

style pc_window_image_button:
    xalign 1.

style pc_window_text:
    outlines ((1, '5559', 1, 1),)
    size 15
    yalign 1.
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
