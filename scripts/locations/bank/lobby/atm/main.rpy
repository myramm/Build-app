transform atm_caret:
    alpha 1.
    1.
    alpha 0.
    1.
    repeat


init python:
    class ATMCursor(renpy.Displayable):
        def __init__(self, position, **kwargs):
            super(ATMCursor, self).__init__(**kwargs)
            self.x, self.y = position
            self.xinit = self.x
            self.cursor = atm_caret("atm/atm_underscore.png")
            self.character_width = 20
        
        @property
        def position(self):
            return (self.x, self.y)
        
        def added_number(self):
            self.x += self.character_width
        
        def removed_number(self):
            self.x -= self.character_width
        
        def reset_position(self):
            self.x = self.xinit
        
        def render(self, width, height, st, at):
            return renpy.render(self.cursor, width, height, st, at)

    class ATMButton(renpy.Displayable):
        def __init__(self, displayable, position, string, offset=(0,0), style="style_atm_keypad", **kwargs):
            super(ATMButton, self).__init__(**kwargs)
            self.string = string
            self.x, self.y = position
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self.should_blit = False
            self.displayable = displayable
            self.inactive_displayable = im.MatrixColor(displayable, dead)
            self.width, self.height = 120, 56
            self.offset = Vector2(*offset)
            self._style = style
            self.active = True
        
        def render(self, width, height, st, at):
            if self.active:
                render = self.h_image if self.should_blit else self.n_image
            else:
                render = self.inactive_displayable
            render = renpy.render(render, width, height, st, at)
            style = self._style if self.active else "style_atm_button_locked"
            text_r = renpy.render(FilteredText(str(self.string), style=self._style), width, height, st, at)
            t_w, t_h = text_r.get_size()
            w, h = render.get_size()
            x = (w - t_w) / 2
            y = (h - t_h) / 2
            pos = Vector2(x, y)
            pos += self.offset
            render.blit(text_r, pos.tuple)
            self.width, self.height = w, h
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

    class BankATM(renpy.Displayable):
        def __init__(self, **properties):
            super(BankATM, self).__init__(**properties)
            self._bg = renpy.displayable("atm/location_bank_atm_01.jpg")
            offset = (-35, 0)
            self._chg_acct_btn = ATMButton("atm/atm_button_05.png", (40, 580), "[player.inventory.money]", offset, "style_atm_button")
            self._exit_btn = ATMButton("atm/atm_button_02.png", (40, 670), "Exit", offset, "style_atm_button")
            self._deposit_btn = ATMButton("atm/atm_button_03.png", (750, 580), "Deposit", offset, "style_atm_button")
            self._withdraw_btn = ATMButton("atm/atm_button_04.png", (750, 670), "Withdraw", offset, "style_atm_button")
            xpad = 5 
            ypad = 5 
            keyw, keyh = 120, 56
            xstart, ystart = 327, 507
            self.keypad = []
            for i in xrange(10):
                name = "_keypad_" + str(i)
                if i == 0:
                    value = ATMButton("atm/atm_keypad_01.png", (452, 687), str(i), (0,0), "style_atm_keypad")
                else:
                    j = i - 1
                    x = xstart + (keyw + xpad) * (j % 3)
                    y = ystart + (keyh + ypad) * (j / 3)
                    value = ATMButton("atm/atm_keypad_01.png", (x, y), str(i), (0,0), "style_atm_keypad")
                self.__dict__[name] = value
                self.keypad.append(name)
            
            self._keypad_dot = ATMButton("atm/atm_keypad_01.png", (329, 687), "")
            self._keypad_arrow = ATMButton("atm/atm_keypad_03.png", (576, 687), "")
            self._cursor = ATMCursor((370, 444))
            self.money_input = ""
            self.update_btns()
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            chg_acct_r = self._chg_acct_btn.render(width, height, st, at)
            exit_r = self._exit_btn.render(width, height, st, at)
            deposit_r = self._deposit_btn.render(width, height, st, at)
            withdraw_r = self._withdraw_btn.render(width, height, st, at)
            render.blit(chg_acct_r, self._chg_acct_btn.position)
            render.blit(exit_r, self._exit_btn.position)
            render.blit(deposit_r, self._deposit_btn.position)
            render.blit(withdraw_r, self._withdraw_btn.position)
            money_txt_r = renpy.render(Text(self.money_input, style="style_atm_money_input"), width, height, st, at)
            acct_txt_r = renpy.render(Text('[player.name!c]', style="style_atm_account"), width, height, st, at)
            balance_lbl_r = renpy.render(FilteredText(self.get_balance_txt, style="style_atm_labels"), width, height, st, at)
            interests_lbl_r = renpy.render(FilteredText(self.get_interests_txt, style="style_atm_labels"), width, height, st, at)
            savings_r = renpy.render(Text(self.get_account_money, style=self.get_money_style), width, height, st, at)
            interests_r = renpy.render(Text(self.get_account_interests, style=self.get_money_style), width, height, st, at)
            
            render.blit(money_txt_r, (375, 418))
            w, h = render.get_size()
            acct_w, acct_h = acct_txt_r.get_size()
            acct_x = (w - acct_w) / 2
            render.blit(acct_txt_r, (acct_x, 170))
            
            right_edge = 820
            sav_w, _ = savings_r.get_size()
            int_w, _ = interests_r.get_size()
            sav_x = right_edge - sav_w - 5
            int_x = right_edge - int_w - 5
            
            render.blit(balance_lbl_r, (206, 243))
            render.blit(interests_lbl_r, (206, 332))
            render.blit(savings_r, (sav_x, 243))
            render.blit(interests_r, (int_x, 332))
            
            cursor_r = self._cursor.render(width, height, st, at)
            render.blit(cursor_r, self._cursor.position)
            
            for name in self.keypad:
                key = self.__dict__[name]
                key_r = key.render(width, height, st, at)
                render.blit(key_r, key.position)
            
            keypad_dot_r = self._keypad_dot.render(width, height, st, at)
            keypad_arrow_r = self._keypad_arrow.render(width, height, st, at)
            
            render.blit(keypad_arrow_r, self._keypad_arrow.position)
            render.blit(keypad_dot_r, self._keypad_dot.position)
            
            return render
        
        @property
        def get_account_money(self):
            return '{:,}'.format(player.inventory.savings)
        
        @property
        def get_account_interests(self):
            return '{:,}'.format(int(round(player.inventory.savings * 0.03, 0)))
        
        @property
        def get_interests_txt(self):
            return "INTEREST"
        
        @property
        def get_money_style(self):
            return "style_atm_money"
        
        @property
        def get_balance_txt(self):
            return "BALANCE"
        
        def exit(self):
            renpy.jump("bank_dialogue")
        
        def deposit(self):
            try:
                money = int(self.money_input)
            except ValueError:
                money = 0
            
            if player.inventory.money >= money:
                player.inventory.savings += money
                player.inventory.money -= money
                self.money_input = ""
                self._cursor.reset_position()
            
            renpy.restart_interaction()
        
        def withdraw(self):
            try:
                money = int(self.money_input)
            except ValueError:
                money = 0
            
            if player.inventory.savings >= money:
                player.inventory.savings -= money
                player.inventory.money += money
                self.money_input = ""
                self._cursor.reset_position()
            
            renpy.restart_interaction()
        
        def add_number(self, number):
            n = str(number)
            if len(self.money_input) >= 8:
                return
            self.money_input += n
            self._cursor.added_number()
            self.update_btns()
        
        def remove_number(self):
            if self.money_input:
                self.money_input = self.money_input[:-1]
                self._cursor.removed_number()
            self.update_btns()
        
        def update_btns(self):
            value = int(self.money_input or 0)
            self._deposit_btn.active = value and value <= player.inventory.money and not player.inventory.savings + value > 999999999
            self._withdraw_btn.active = value and value <= player.inventory.savings
        
        def event(self, ev, x, y, st):
            class nonlocal:
                redraw = False
            
            def is_clicked(btn):
                hover = btn.hitbox(x, y) and btn.active
                rv = hover and ev.type == pygame.MOUSEBUTTONUP
                nonlocal.redraw |= rv or btn.should_blit != hover
                btn.should_blit = hover
                return rv
            
            if is_clicked(self._exit_btn):
                self.exit()
            
            if is_clicked(self._deposit_btn):
                self.deposit()
            
            if is_clicked(self._withdraw_btn):
                self.withdraw()
            
            if is_clicked(self._keypad_arrow):
                self.remove_number()
            
            for i, name in enumerate(self.keypad):
                key = self.__dict__[name]
                if is_clicked(key):
                    self.add_number(int(key.string))
            
            keys = list(xrange(48, 58))
            keys.extend([pygame.K_KP0, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4,
                         pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9])
            keys.extend([pygame.K_DELETE, pygame.K_BACKSPACE])
            
            if ev.type == pygame.KEYDOWN and ev.key in keys:
                nonlocal.redraw = True
                if ev.key in (pygame.K_0, pygame.K_KP0):
                    self.add_number(0)
                elif ev.key in (pygame.K_1, pygame.K_KP1):
                    self.add_number(1)
                elif ev.key in (pygame.K_2, pygame.K_KP2):
                    self.add_number(2)
                elif ev.key in (pygame.K_3, pygame.K_KP3):
                    self.add_number(3)
                elif ev.key in (pygame.K_4, pygame.K_KP4):
                    self.add_number(4)
                elif ev.key in (pygame.K_5, pygame.K_KP5):
                    self.add_number(5)
                elif ev.key in (pygame.K_6, pygame.K_KP6):
                    self.add_number(6)
                elif ev.key in (pygame.K_7, pygame.K_KP7):
                    self.add_number(7)
                elif ev.key in (pygame.K_8, pygame.K_KP8):
                    self.add_number(8)
                elif ev.key in (pygame.K_9, pygame.K_KP9):
                    self.add_number(9)
                elif ev.key in (pygame.K_DELETE, pygame.K_BACKSPACE):
                    self.remove_number()
            
            if nonlocal.redraw:
                renpy.redraw(self, 0)

screen atm():
    add BankATM()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
