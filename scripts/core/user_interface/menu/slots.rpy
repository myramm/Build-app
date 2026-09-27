screen load():
    modal True tag menu

    use slots(_('Load'), _('Select a slot from above to {b}load{/b} a previous game.'))



screen save():
    modal True tag menu

    use slots(_('Save in'), _('Select a slot from above to {b}save{/b} the current game.'))



screen slots(title, tip):
    use common_menu():
        style_prefix 'slots'

        vbox:

            textbutton _('Back') action Return()

            hbox:
                style_prefix 'pages'
                textbutton _('Previous{#page}') action FilePagePrevious()
                if config.has_autosave or config.has_quicksave:
                    hbox:
                        style_prefix 'pages_group'
                        if config.has_autosave:
                            textbutton _('A{#auto_page}') action FilePage('auto')
                        if config.has_quicksave:
                            textbutton _('Q{#quick_page}') action FilePage('quick')
                hbox:
                    style_prefix 'pages_group'
                    $ lower = max(1, int(FilePageName(0, 0)) - 2)
                    for page in xrange(lower, lower + 5):
                        textbutton str(page).zfill(2) action FilePage(page)
                textbutton _('Next{#page}') action FilePageNext()

            grid 3 2:
                style_prefix 'slot'

                for slot in xrange(1, 7):
                    python:
                        ref = '{}-{}'.format(FileCurrentPage(), slot)
                        date = FileTime(slot, format=__('{#date_fmt}%B %d, %H:%M'),
                                          empty=__('{i}empty slot{/i}'))
                        action = FileAction(slot)

                        if FileLoadable(slot):
                            icon = False
                            note = FileSaveName(slot)
                            origin = FileJson(slot, '_version') or '???'
                            shot = FileScreenshot(slot, empty=empty)
                            ver = util.version(origin)
                            
                            if ver < (0, 19, 0) or ver > app.version:
                                if isinstance(action, FileLoad):
                                    action = ShowPopup('incompatible',
                                                   background='#0009')
                                icon = 'slot_broken'
                                note = '{{color=#cb3d3b}}{}{{/color}}'.format(note)
                                shot = im.Grayscale(shot)
                            elif ver < app.version:
                                icon = 'slot_compat'
                                note = '{{color=#fbb259}}{}{{/color}}'.format(note)
                                shot = im.Sepia(shot)
                            
                            shot_over = im.MatrixColor(shot, over)


                    vbox:
                        label '[ref]. [date]'
                        null height 5

                        frame:
                            has button
                            action If(isinstance(action, FileSave),
                                  If(FileCurrentPage() == 'auto',
                                     None, Show('slots_note', None, slot)),
                                  action)
                            alt '{} {}. {}'.format(title, ref, date)

                            if FileLoadable(slot):
                                background shot
                                hover_background shot_over
                                tooltip note

                                if icon:
                                    add icon:
                                        align 1., 1.
                                    text origin

                                imagebutton:
                                    action FileDelete(slot)
                                    alt _('Delete {}. {}').format(ref, date)
                                    hover 'delete_btn_over'
                                    idle 'delete_btn_idle'
                                    tooltip FileSaveName(slot)

                                key 'save_delete' action FileDelete(slot)

            fixed:
                text tip
                label GetTooltip() or ''


screen slots_note(slot):
    modal True

    default note = '{} - Day {}'.format(firstname, game.timer.game_day())

    frame:
        style_prefix 'slot_prompt'

        has vbox

        label _('Enter a note to help recognise this save:')

        frame:
            style_prefix 'text_input'
            input:
                allow ('abcdefghijklmnopqrstuvwxyz'
                       'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                       '0123456789 -_!()@:;?<>,.#/')
                length 32
                value ScreenVariableInputValue('note')

        hbox:
            button:
                action (SetField(store, 'save_name', note.strip()),
                        FileSave(slot, confirm=False),
                        SetField(store, 'save_name', ''),
                        Hide('slots_note'))
                keysym 'input_enter'
                selected False
                sensitive note.strip()

                if FileLoadable(slot):
                    style_suffix 'warn_button'
                    text _('Overwrite') style_suffix 'warn_button_text'
                else:
                    text _('OK') style_suffix 'button_text'

            textbutton _('Cancel'):
                action Hide('slots_note')
                keysym 'game_menu'


style pages_button is menu_button:

    xsize 150

style pages_button_text is menu_button_text


style pages_group_button is menu_button:

    xsize 60

style pages_group_button_text is menu_button_text


style pages_group_hbox is menu_hbox:

    align (.5, .5)
    spacing 10

style pages_hbox is menu_hbox:

    spacing 30
    xalign .5

style slot_button:
    xysize (config.thumbnail_width, config.thumbnail_height)

style slot_frame:
    background 'menu_frame'
    padding (4, 4, 4, 4)

style slot_grid:
    align (.5, .5)
    spacing 30

style slot_image_button:
    align (1., 0.)
    offset (-2, 2)

style slot_prompt_button is menu_button:

    xysize (150, 50)

style slot_prompt_button_text is menu_button_text:

    size 14

style slot_prompt_frame is menu_frame:

    align (.5, .5)
    background 'menu_frame_opaque'
    fit_first True
    padding (25, 35, 25, 25)
    xmaximum 650

style slot_prompt_hbox:
    spacing 50
    xalign .5

style slot_prompt_label:
    xalign .5

style slot_prompt_text_input_input:
    size 18

style slot_prompt_vbox:
    spacing 20

style slot_prompt_warn_button take slot_prompt_button


style slot_prompt_warn_button_text take slot_prompt_button_text


style slot_text:
    align (.5, .95)
    bold True
    outlines ((2, '000', 0, 0),)

style slots_button is menu_button


style slots_button_text is menu_button_text


style slots_fixed:
    fit_first True
    xalign .5

style slots_label:
    xalign .5
    yoffset 25

style slots_label_text:
    bold True
    text_align .5

style slots_text:
    color '8b94aa'

style slots_vbox:
    align (.5, .5)
    spacing 30
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
