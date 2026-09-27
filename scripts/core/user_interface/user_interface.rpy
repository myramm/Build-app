init python:
    class UIMessage(renpy.Displayable):
        def __init__(self, message="",redraw=True):
            super(UIMessage, self).__init__()
            if renpy.loadable(message):
                self._displayable = renpy.displayable(message)
                self.is_text = False
            else:
                self.message = message
                self.is_text = True
            if message.startswith('+') and self.is_text:
                self.stylename = 'style_ui_message_add_money'
            elif message.startswith('-') and self.is_text:
                self.stylename = 'style_ui_message_rem_money'
            else:
                self.stylename = None
            
            self.fadeout_time = 3.0 
            self.start_time = clock()
            self.x, self.y = 0, 30
            self.redraw = redraw
        
        @property
        def position(self):
            time_elapsed = float(clock() - self.start_time())
            x = 0
            y = int(self.y * (1 - (time_elapsed / self.fadeout_time)))
            y = max(0, y)
            return x, y
        
        @property
        def get_text_d(self):
            text_d = FilteredText(self.message, style=self.stylename)
            time_elapsed = clock() - self.start_time
            opacity_percent = float(time_elapsed) / self.fadeout_time
            matrix = im.matrix.opacity(opacity_percent)
            return im.MatrixColor(text_d, matrix)
        
        @property
        def get_image_d(self):
            time_elapsed = clock() - self.start_time
            opacity_percent = float(time_elapsed) / self.fadeout_time
            matrix = im.matrix.opacity(opacity_percent)
            return im.MatrixColor(self.displayable, matrix)
        
        def render(self, width, height, st, at):
            render = renpy.render(renpy.displayable("ground.png"), width, height, st, at)
            if self.stylename is None:
                return render
            w, h = 0, 0
            to_r = None
            if self.is_text:
                to_r = renpy.render(self.get_text_d, width, height, st, at)
            else:
                to_r = renpy.render(self.get_image_d, width, height, st, at)
            w, h = to_r.get_size()
            
            render = render.subsurface((0, 0, w, 30))
            render.blit(to_r, self.position)
            if self.redraw:
                renpy.redraw(self, 0)
            return render

    class UIButton(renpy.Displayable):
        def __init__(self, displayable, position, action=None, **kwargs):
            super(UIButton, self).__init__(**kwargs)
            self.x, self.y = position
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self.should_blit = False
            self.displayable = renpy.displayable(displayable.format(""))
            self.inactive_displayable = renpy.displayable(displayable.format("_locked"))
            self.width, self.height = 0, 0
            self.active = True
            self.action = action if action is not None else NullAction()
        
        def render(self, width, height, st, at):
            if self.active:
                render = self.h_image if self.should_blit else self.n_image
            else:
                render = self.inactive_displayable
            render = renpy.render(render, width, height, st, at)
            self.width, self.height = render.get_size()
            return render
        
        @property
        def position(self):
            return (self.x, self.y)
        
        @property
        def h_image(self):
            return im.MatrixColor(self.displayable, self._h_matrix)
        
        @property
        def n_image(self):
            return im.MatrixColor(self.displayable, self._n_matrix)
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class UICDD(renpy.Displayable):
        def __init__(self, **kwargs):
            super(UICDD, self).__init__(**kwargs)
            self.show_clock = kwargs.get("show_clock", True)
            self.show_map = kwargs.get("show_map", True)
            self.show_day_info = kwargs.get("show_day_info", True)
            self.show_money_info = kwargs.get("show_money_info", True)
            self.show_cellphone = kwargs.get("show_cellphone", True)
            self.show_backpack = kwargs.get("show_backpack", True)
            self.show_settings = kwargs.get("show_settings", True)
            self.redraw = kwargs.get("redraw", True)
            self.inactive = kwargs.get("inactive", False)
            
            self._bg = renpy.displayable("ground.png")
            if self.show_day_info:
                self.day_info = renpy.displayable("ui/ui_piece_space.png")
                day_string = game.timer.dayOfWeek(full=True)
                self.day_text = Text("{b}[day_string]{/b}")
                self.loc_text = Text("{b}[player.location.display_name]{/b}")
                self.day_info_pos = (97, 11)
                self.day_text_pos = (105, 45)
                self.loc_text_pos = (105, 15)
            if self.show_clock:
                self.clock = renpy.displayable("ui/ui_piece_time.png")
                self.time_piece = renpy.displayable("ui/ui_piece_time.png")
                self.skip = UIButton("ui/ui_piece_skip{}.png", (441, 2), TickTimer())
                self.cycle_bar = renpy.displayable("ui/ui_day_cycle_bar.png")
                num_cycles = 3 - game.timer._tod
                self.cycle_bar_pos = [(554, 29), (499, 29), (444, 29)][num_cycles:]
                self.time_piece_pos = (441, 2)
            if self.show_map:
                self.map_icon = UIButton("ui/ui_piece_map{}.png", (13, 5), MapAction())
                self.map_icon.active = game.ui_locked
            if self.show_backpack:
                self.backpack = UIButton("ui/ui_piece_backpack{}.png", (867, 5), OpenBackpack())
            if self.show_cellphone:
                self.cellphone = UIButton("ui/ui_piece_phone{}.png", (802, 5), Show('phone'))
                self.app_alert = None
                if game.new_achievements:
                    self.app_alert = renpy.displayable("cellphone/phone_alert.png")
                elif game.new_message:
                    self.app_alert = renpy.displayable("cellphone/phone_alert_feats.png")
                self.app_alert_pos = (835, 5)
            if self.show_settings:
                self.settings = UIButton("ui.ui_piece_settings{}.png", (946, 5), ShowMenu("game_menu"))
            if self.show_money_info:
                self.money = renpy.displayable("ui/ui_piece_money.png")
                self.money_pos = (646, 11)
                self.money_txt = Text("{b}[player.inventory.money]{/b}")
                self.money_txt_pos = (765, 16)
        
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            args = [width, height, st, at]
            if self.show_clock:
                clock_r = renpy.render(self.clock, *args)
                render.blit(clock_r, self.time_piece_pos)
                cycle_bar_r = renpy.render(self.cycle_bar, *args)
                for x in self.cycle_bar_pos:
                    render.blit(cycle_bar_r, x)
                skip_r = self.skip.render(*args)
                if player.location not in Location.get_first_children() and M_player.get_state() != S_player_start or game.timer.game_day() == 0:
                    render.blit(skip_r, self.skip.position)
            if self.show_day_info:
                space_r = renpy.render(self.day_info, *args)
                render.blit(space_r, self.day_info_pos)
                text_r = renpy.render(self.day_text, *args)
                render.blit(text_r, self.day_text_pos)
                text_r = renpy.render(self.loc_text, *args)
                render.blit(text_r, self.loc_text_info)
            if self.show_map:
                map_r = self.map_icon.render(*args)
                render.blit(map_r, self.map.position)
            if self.show_backpack:
                backpack_r = self.backpack.render(*args)
                render.blit(backpack_r, self.backpack.position)
            if self.show_settings:
                settings_r = self.settings.render(*args)
                render.blit(settings_r, self.settings.position)
            if self.show_cellphone:
                cell_r = self.cellphone.render(*args)
                render.blit(cell_r, self.cellphone.position)
                if self.app_alert is not None:
                    app_alert_r = renpy.render(self.app_alert, *args)
                    render.blit(app_alert_r, self.app_alert_pos)
            if self.show_money:
                money_r = renpy.render(self.money, *args)
                render.blit(money_r, self.money_pos)
                money_txt_r = renpy.render(self.money_txt, *args)
                render.blit(money_txt_r, self.money_txt_pos)
            
            if self.redraw:
                renpy.redraw(self, 0.05)
            return render
        
        def event(self, ev, x, y, st):
            if self.show_clock  and (self.show_clock != "inactive" or self.inactive):
                if self.skip.hitbox(x, y):
                    self.skip.should_blit = True
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self.skip.action()
                else:
                    self.skip.should_blit = False
            if self.show_map and (self.show_map != "inactive" or self.inactive):
                if self.map_icon.hitbox(x, y):
                    self.map_icon.should_blit = True
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self.map_icon.action()
                else:
                    self.map_icon.should_blit = False
            if self.show_backpack and (self.show_backpack != "inactive" or self.inactive):
                if self.backpack.hitbox(x, y):
                    self.backpack.should_blit = True
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self.backpack.action()
                else:
                    self.backpack.should_blit = False
            if self.show_cellphone and (self.show_cellphone != "inactive" or self.inactive):
                if self.cellphone.hitbox(x, y):
                    self.cellphone.should_blit = True
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self.cellphone.action()
                else:
                    self.cellphone.should_blit = False
            if self.show_settings and (self.show_settings != "inactive" or self.inactive):
                if self.settings.hitbox(x, y):
                    self.settings.should_blit = True
                    if ev.type == pygame.MOUSEBUTTONUP:
                        self.settings.action()
                else:
                    self.settings.should_blit = False

screen ui():
    default time_pieces_positions = [554, 499, 444]
    default day_string = game.timer.dayOfWeek(full=True)
    default locations_time_skippable = Location.get_first_children()

    default on_rails = game.rails()

    $ locations_time_skippable.append(L_map)

    if renpy.get_screen("town_map"):
        imagebutton:
            focus_mask True
            pos 17, 5
            idle "ui/ui_piece_bed.png"
            hover HoverImage("ui/ui_piece_bed.png")
            action MapAction()
    else:
        imagebutton:
            focus_mask True
            pos 13, 5
            if on_rails or game.ui_locked or (player.location not in Location.get_first_children()) and not game.force_unlock_map:
                idle "ui/ui_piece_map_locked.png"
                action NullAction()
            else:
                idle "ui/ui_piece_map.png"
                hover HoverImage("ui/ui_piece_map.png")
                action MapAction()


    add "ui/ui_piece_time.png" xpos 441 ypos 2
    for i in xrange(3 - game.timer._tod):
        add "ui/ui_day_cycle_bar.png" pos time_pieces_positions[i], 29
    if not on_rails and player.location in locations_time_skippable and not M_player.is_state(S_player_start) and not M_anon.is_state(S_ano27_home):
        imagebutton:
            focus_mask None
            pos 507, 46
            idle "ui/ui_piece_skip.png"
            hover HoverImage("ui/ui_piece_skip.png")
            action TickTimer()


    add "ui/ui_piece_space.png" xpos 97 ypos 11
    if Location.future_location is None:
        text "{b}[player.location.display_name]{/b}" xpos 105 ypos 15 xalign 0.0
    else:
        text "{b}[Location.future_location.display_name]{/b}" xpos 105 ypos 15 xalign 0.0
    text "{b}[day_string]{/b}" xpos 105 ypos 45 xalign 0.0


    add "ui/ui_piece_money.png" pos 646, 11
    text "{b}[player.inventory.money_str]{/b}" xpos 765 ypos 16 xalign 1.0


    imagebutton:
        focus_mask True
        pos 802, 5
        idle "ui/ui_piece_phone.png"
        hover HoverImage("ui/ui_piece_phone.png")
        action [Show('phone'), Play("audio", "audio/sfx_phone_notification.ogg")]
    if game.new_message:
        add "cellphone/phone_alert.png" pos 835,5
    elif game.new_achievements:
        add "cellphone/phone_alert_feats.png" pos 835,5


    imagebutton:
        focus_mask True
        pos 867, 5
        idle "ui/ui_piece_backpack.png"
        hover HoverImage("ui/ui_piece_backpack.png")
        action OpenBackpack()


    imagebutton:
        focus_mask True
        pos 946, 5
        idle "ui/ui_piece_settings.png"
        hover HoverImage("ui/ui_piece_settings.png")
        action ShowMenu("game_menu")


    key "shift_K_w" action If(persistent.skip_debug_menu_popup, Show("debug_menu", None, "general"), Show("debug_menu_popup"))
    key "shift_K_x" action Show('phone', None, 'goals')


screen ui_message(screen_name, position, displayable, fadeout_tick=0.0, anim_tick_rate=0.1, timeout=3.0):
    default offset = 1

    $ next_fadeout_tick = fadeout_tick + anim_tick_rate
    $ next_position = (position[0], position[1] - offset)

    add Transform(displayable, alpha=1.0 - (fadeout_tick / timeout)) pos position

    timer anim_tick_rate action [Hide(screen_name),
                                 If(fadeout_tick <= timeout,
                                    Show(screen_name, None, next_position, displayable,
                                         next_fadeout_tick, anim_tick_rate, timeout),
                                    MarkLayerAvailable(screen_name))]


screen ui_message0(*args):
    tag ui_message0
    use ui_message("ui_message0", *args)


screen ui_message1(*args):
    tag ui_message1
    use ui_message("ui_message1", *args)


screen ui_message2(*args):
    tag ui_message2
    use ui_message("ui_message2", *args)


screen ui_message3(*args):
    tag ui_message3
    use ui_message("ui_message3", *args)


screen ui_message4(*args):
    tag ui_message4
    use ui_message("ui_message4", *args)


screen ui_message5(*args):
    tag ui_message5
    use ui_message("ui_message5", *args)


screen ui_message6(*args):
    tag ui_message6
    use ui_message("ui_message6", *args)


screen ui_message7(*args):
    tag ui_message7
    use ui_message("ui_message7", *args)


screen ui_message8(*args):
    tag ui_message8
    use ui_message("ui_message8", *args)


screen ui_message9(*args):
    tag ui_message9
    use ui_message("ui_message9", *args)


screen backpack():
    button:
        action (Hide('backpack'),
                Play('audio', 'audio/sfx_backpack_close.ogg'))
        has fixed
        add 'ui/backpack.png' align .5, 1.

    button:
        action NullAction()
        anchor 0., 1.
        pos 187, 610
        fixed:
            xysize 658, 480

    default active = None
    default backback_page = 1
    default items_per_page = 15
    default current_item = 0
    default start_item = 0
    default total_items = len(player.inventory.items)
    default Inv = player.inventory.items

    for current_item in xrange(start_item, (backback_page * items_per_page)):
        if current_item < total_items:
            $ start_xpos = 191
            $ start_ypos = 134
            $ row_ypos = math.trunc(current_item / 5)
            $ row_xpos = current_item - (row_ypos * 5)
            $ row_ypos -= math.trunc(start_item / 5)
            $ start_xpos += 130 * row_xpos
            $ start_ypos += 130 * row_ypos

            vbox:
                area (start_xpos,start_ypos,130,130)
                imagebutton:
                    idle Item(Inv[current_item]).image
                    if Item(Inv[current_item]).transform == None:
                        hover HoverImage(Item(Inv[current_item]).image)
                    else:
                        hover HoverImage(Item(Inv[current_item]).transform)
                    xalign 0.5
                    yalign 0.5
                    action (If(Item(Inv[current_item]).dialogue,
                               (Function(renpy.call_in_new_context,
                                         Item(Inv[current_item]).dialogue,
                                         item=Item(Inv[current_item])),
                                Play("audio", "audio/sfx_backpack_select2.ogg")),
                               NullAction()))
                    hovered SetScreenVariable('active', Item(Inv[current_item]))
                    unhovered SetScreenVariable('active', None)

    if active:
        vbox:
            pos 202, 537
            spacing 10
            xsize 628
            text active.name bold True
            text active.description

    if backback_page > 1:
        imagebutton:
            focus_mask True
            pos 43, 261
            idle "ui/backpack_left.png"
            action (SetScreenVariable('backback_page', backback_page - 1),
                    SetScreenVariable('start_item', start_item - 15))

    if current_item + 1 < total_items:
        imagebutton:
            focus_mask True
            pos 874, 264
            idle "ui/backpack_right.png"
            action (SetScreenVariable('backback_page', backback_page + 1),
                    SetScreenVariable('start_item', start_item + 15))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
