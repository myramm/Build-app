

init python:
    class RapGlowButton(renpy.Displayable):
        def __init__(self, img_path, freq=2, amplitude=0.1, const=0.8, **kwargs):
            super(RapGlowButton, self).__init__(**kwargs)
            self.time = 0  
            self.frequency = freq  
            self.amplitude = amplitude  
            self.const = const 
            self._img = img_path
        
        def clamp(self, value, mini=0.0, maxi=1.0):
            return min(max(value, mini), maxi)
        
        @property
        def get_intensity(self):
            return self.amplitude * (math.sin(self.time * self.frequency) + 1) + self.const
        
        
        @property
        def img(self):
            mat = im.matrix.identity()
            mat *= im.matrix.opacity(self.get_intensity)
            
            return im.MatrixColor(self._img, mat)
        
        def render(self, width, height, st, at):
            render = renpy.render(self.img, width, height, st, at)
            self.time += 0.01
            return render

    class RapMCFadeIn(renpy.Displayable):
        def __init__(self, image, fadein_time=2.0):
            self.fadein_time = fadein_time 
            self.image = image
            self.time_elapsed = 0
        
        @property
        def img(self):
            opacity_matrix = im.matrix.opacity(max(self.time_elapsed / self.fadein_time, 1.0))
            return im.MatrixColor(self.image, opacity_matrix)
        
        def render(self, width, height, st, at):
            render = renpy.render(self.img, width, height, st, at)
            self.time_elapsed += 0.01
            return render

    class RapCountdown(renpy.Displayable):
        def __init__(self, start=10, rapbtns=[]):
            super(RapCountdown, self).__init__()
            self.start = start  
            self.start_clock = clock()
            self.width, self.height = None, None
            self.rapbtns = rapbtns
        
        @property
        def clock(self):
            scale = max(100 - 2 * int(self.elapsed_time / 5), 20)
            return Text(str(self.remaining_time), style='style_rap_countdown', size = scale)
        
        @property
        def elapsed_time(self):
            return clock() - self.start_clock
        
        @property
        def remaining_time(self):
            return int(self.start - self.elapsed_time)
        
        def render(self, width, height, st, at):
            render = renpy.render(self.clock, width, height, st, at)
            for btn in self.rapbtns:
                btn.hovered = False
            self.rapbtns[int(self.elapsed_time) % len(self.rapbtns)].hovered = True
            return render


    class RapButton(renpy.Displayable):
        def __init__(self, id_, position, small=False, active=True, **kwargs):
            super(RapButton, self).__init__(**kwargs)
            self.scale_factor = 0.75
            self.x, self.y = position
            self._h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._n_matrix = im.matrix.identity()
            self._i_matrix = im.matrix.saturation(0.95) * im.matrix.brightness(-0.5)
            self.hovered = False
            self.displayable = renpy.displayable("minigames/rap_battle/rap_button_{:02}.png".format(id_))
            self.inactive_displayable = renpy.displayable("minigames/rap_battle/rap_button_00_small.png")
            self.width, self.height = 120, 120
            self.active = active
            self.small = small
            self.id = id_
        
        def render(self, width, height, st, at):
            render = self.h_image if self.hovered else self.n_image
            render = renpy.render(render, width, height, st, at)
            return render
        
        
        @property
        def position(self):
            return (self.x, self.y)
        
        @property
        def f_image(self):
            if self.active:
                if self.small:
                    return im.MatrixColor(im.FactorScale(self.displayable, self.scale_factor),
                                          self._i_matrix)
                else:
                    return self.displayable
            else:
                if self.small:
                    return self.inactive_displayable
                else:
                    return im.MatrixColor(self.displayable, self._i_matrix)
        
        @property
        def h_image(self):
            if self.small and self.active:
                return im.FactorScale(self.displayable, self.scale_factor)
            else:
                return im.MatrixColor(self.f_image, self._h_matrix)
        
        @property
        def n_image(self):
            return im.MatrixColor(self.f_image, self._n_matrix)
        
        def hitbox(self, x, y):
            return (self.x <= x <= self.x+self.width) and (self.y <= y <= self.y+self.height)

    class RapMinigame(renpy.Displayable):
        def __init__(self, difficulty=2):
            super(RapMinigame, self).__init__()
            self.bg = renpy.displayable("minigames/rap_battle/background.jpg")
            self.difficulty = 4 + 2 * min(difficulty, 2)
            self.answers = [random.randint(1,5) for i in xrange(self.difficulty)]
            self.screen_index = 1
            
            self.small_rap_buttons = self.init_small_rap_buttons()
            self.big_rap_buttons = self.init_big_rap_buttons()
            
            self.player_input = []
            self.current_input = 0
            self.countdown = RapCountdown(start=30.0 * ((player.stats.int() / 4) + 1), rapbtns=self.small_rap_buttons)
            
            self.started = None
            self.ticked = None
            self.tick_duration = 1.0 / 60 
            self.time_limit = 20 + 2 * player.stats.int()
            self._TIMER_BAR_LENGTH = 513
            self.bar_length = self._TIMER_BAR_LENGTH
            self._bar_empty = renpy.displayable("buttons/bar_empty.png")
            self._bar_full = renpy.displayable("buttons/bar_full.png")
            self.mc_pose_rapping = RapMCFadeIn("minigames/rap_battle/location_park_minigame_mc_01.png")
            self.mc_pose_win = RapMCFadeIn("minigames/rap_battle/location_park_minigame_mc_02.png", 4.0)
            self.mc_pose_lose = RapMCFadeIn("minigames/rap_battle/location_park_minigame_mc_03.png", 4.0)
            self.rap_win_button = RapGlowButton("minigames/rap_battle/rap_won.png")
            self.rap_lose_button = RapGlowButton("minigames/rap_battle/rap_lost.png")
        
        def init_small_rap_buttons(self):
            rap_buttons = []
            self.small_rap_buttons_pos = []
            xi, yi = 425, 160
            w, h = 90, 90
            wpad, hpad = 5, 30
            num_per_line = len(self.answers) / 2
            for i, answer in enumerate(self.answers):
                pos = (xi + (w + wpad) * (i % num_per_line) , yi + (h + hpad) * (i / num_per_line))
                self.small_rap_buttons_pos.append(pos)
                rap_buttons.append(RapButton(answer, pos, small=True))
            return rap_buttons
        
        def init_big_rap_buttons(self):
            rap_buttons = []
            positions = [(539, 459),
                         (675, 459),
                         (471, 596),
                         (607, 596),
                         (743, 596)]
            for i, pos in enumerate(positions):
                rap_buttons.append(RapButton(i+1, pos, small=False, active=False))
            return rap_buttons
        
        def first_screen(self, render, *args):
            for rapbtn in self.small_rap_buttons:
                btn_r = rapbtn.render(*args)
                render.blit(btn_r, rapbtn.position)
            for rapbtn in self.big_rap_buttons:
                btn_r = rapbtn.render(*args)
                render.blit(btn_r, rapbtn.position)
            
            countdown_r = self.countdown.render(*args)
            if self.countdown.width is None or self.countdown.height is None:
                self.countdown.width, self.countdown.height = countdown_r.get_size()
            cw, ch = countdown_r.get_size()
            cwi, chi = self.countdown.width, self.countdown.height
            cx = (cwi - cw) / 2 + 125
            cy = (chi - ch) / 2 + 285
            
            render.blit(countdown_r, (cx, cy))
            text = "Memorize the\npattern order!\n(Click to skip)"
            countdown_instructions_r = renpy.render(FilteredText(text, style='style_rap_countdown'), *args)
            render.blit(countdown_instructions_r, (50, 175))
            return render
        
        def second_screen(self, render, *args):
            width, height, st, at = args
            for rapbtn in self.small_rap_buttons:
                btn_r = rapbtn.render(*args)
                render.blit(btn_r, rapbtn.position)
            for rapbtn in self.big_rap_buttons:
                btn_r = rapbtn.render(*args)
                render.blit(btn_r, rapbtn.position)
            for rapbtn in self.player_input:
                btn_r = rapbtn.render(*args)
                render.blit(btn_r, rapbtn.position)
            
            time_left = 1 - min(1, (st - self.started) / self.time_limit)
            if time_left == 0:
                self.switch_screen(lose=True)
            
            
            ticks_elapsed = (st - self.ticked) / self.tick_duration
            if ticks_elapsed >= 1:
                self.ticked = st
                
                self.bar_length = time_left * self._TIMER_BAR_LENGTH
            
            bar_full_r = renpy.render(self._bar_empty, width, height, st, at)
            render.blit(bar_full_r, (400, 410))
            filler_r = renpy.render(self._bar_full, width, height, st, at)
            filler_r_crop = filler_r.subsurface((0, 0, self.bar_length, 33))
            render.blit(filler_r_crop, (400, 410))
            
            mc_pose_r = self.mc_pose_rapping.render(*args)
            render.blit(mc_pose_r, (0, 76))
            return render
        
        def win_screen(self, render, *args):
            mc_pose_r = self.mc_pose_win.render(*args)
            render.blit(mc_pose_r, (0, 76))
            button_r = self.rap_win_button.render(*args)
            render.blit(button_r, (507, 480))
            return render
        
        def lose_screen(self, render, *args):
            mc_pose_r = self.mc_pose_lose.render(*args)
            render.blit(mc_pose_r, (0, 76))
            button_r = self.rap_lose_button.render(*args)
            render.blit(button_r, (507, 480))
            return render
        
        def render(self, width, height, st, at):
            if self.started is None and self.screen_index == 2:
                self.started = self.ticked = st
            render = renpy.render(self.bg, width, height, st, at)
            s = "Recreate the correct order of rap moves to win the battle!" if self.screen_index < 3 else "Click to continue!"
            text = FilteredText(s, style="style_instructions")
            text_r = renpy.render(text, width, height, st, at)
            tw, th = text_r.get_size()
            render.blit(text_r, ((1024-tw)/2, 22))
            if self.screen_index == 1:
                render = self.first_screen(render, width, height, st, at)
            elif self.screen_index == 2:
                render = self.second_screen(render, width, height, st, at)
            elif self.screen_index == 3:
                render = self.win_screen(render, width, height, st, at)
            elif self.screen_index == 4:
                render = self.lose_screen(render, width, height, st, at)
            self.switch_screen()
            renpy.redraw(self, 0)
            return render
        
        def won_game(self):
            for panswer, answer in zip(self.player_input, self.answers):
                if answer != panswer.id:
                    return False
            return True
        
        def switch_screen(self, lose=False, skip_prep=False):
            if lose:
                self.screen_index = 4
            if (self.countdown.remaining_time <= 0 or skip_prep) and self.screen_index == 1:
                self.screen_index = 2
                for btn in self.small_rap_buttons:
                    btn.active = False
                    btn.hovered = False
                for btn in self.big_rap_buttons:
                    btn.active = True
                self.small_rap_buttons[self.current_input].hovered = True
            if self.screen_index == 2 and len(self.player_input) == len(self.answers):
                if self.won_game():
                    self.screen_index = 3
                else:
                    self.screen_index = 4
        
        def event(self, ev, x, y, st):
            if self.screen_index == 1 and ev.type == pygame.MOUSEBUTTONUP:
                self.switch_screen(skip_prep=True)
            elif self.screen_index == 2:
                for btn in self.big_rap_buttons:
                    if btn.hitbox(x, y):
                        btn.hovered = True
                        if ev.type == pygame.MOUSEBUTTONUP:
                            player_btn = RapButton(btn.id,
                                                   self.small_rap_buttons_pos[self.current_input],
                                                   small=True)
                            player_btn.hovered = True
                            
                            self.player_input.append(player_btn)
                            self.small_rap_buttons[self.current_input].hovered = False
                            self.current_input = min(self.current_input + 1, len(self.answers) - 1)
                            self.small_rap_buttons[self.current_input].hovered = True
                    else:
                        btn.hovered = False
            elif self.screen_index in (3, 4) and ev.type == pygame.MOUSEBUTTONUP:
                return self.screen_index == 3

screen rap_battle(difficulty=2):
    add RapMinigame(difficulty)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
