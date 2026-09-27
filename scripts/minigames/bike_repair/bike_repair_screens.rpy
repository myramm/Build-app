init python:
    class BikeRepairMinigame(renpy.Displayable):
        def __init__(self, **properties):
            super(BikeRepairMinigame, self).__init__(**properties)
            self.bg = renpy.displayable('minigames/bike_repair/location_tattoo_garage_minigame.jpg')
            self._wrench_base = renpy.displayable('minigames/bike_repair/repair_wrench.png')
            self.repair_counter = renpy.displayable('minigames/bike_repair/repair_counter.png')
            self._repair_arrow = "minigames/bike_repair/repair_arrow.png"
            
            self.wrench_angle = 0
            self.fadeout_tick = 0.0
            self.FADEOUT_TIMEOUT = 200
            self.started = False
            self.mouse_positions = []
            self.mouse_pressed = False
            self.gesture_resolution = 10 
            self.turns_to_win = 20
            
            self.base_wrench_pos = Vector2(453, 303)
            self.arrow_pos = Vector2(314, 153)
            self.wrench_pivot = Vector2(505, 378)
            self.counter_pos = Vector2(17, 600)
        
        def check_point_in_ring(self, x, y):
            base_radius = (self.wrench_pivot - self.mouse_positions[0]).magnitude
            upper_radius = base_radius + self.gesture_resolution
            lower_radius = base_radius - self.gesture_resolution
            return True 
        
        def get_angle(self):
            if len(self.mouse_positions) >= 2:
                v1 = Vector2(self.mouse_positions[0])
                v2 = Vector2(self.mouse_positions[-1])
                return v1.angle_to(v2) * 180.0 / math.pi
            else:
                return 0.0
        
        @property
        def turn_count(self):
            return int(self.wrench_angle) / 360
        
        @property
        def wrench(self):
            anchor = self.wrench_pivot - self.base_wrench_pos
            return Fixed(Transform(self._wrench_base, rotate=self.wrench_angle, anchor=(53, 73),
                             transform_anchor=True, pos=(0.5, 0.5)))
        
        @property
        def repair_arrow(self):
            opacity = 1.0 - (self.fadeout_tick / self.FADEOUT_TIMEOUT)
            return im.MatrixColor(self._repair_arrow, im.matrix.opacity(opacity))
        
        def check_win(self):
            return self.turn_count >= self.turns_to_win
        
        def render(self, width, height, st, at):
            args = (width, height, st, at)
            if self.started and self.fadeout_tick <= self.FADEOUT_TIMEOUT:
                self.fadeout_tick += 1.0
            if self.mouse_pressed:
                self.wrench_angle += self.get_angle()
            if self.check_win():
                renpy.jump("bike_repair_success")
            render = renpy.render(self.bg, *args)
            
            instructions_r = renpy.render(Text("Crank the WRENCH {} times to fix the bike!".format(self.turns_to_win), style = "style_instructions"), *args)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)), 24))
            
            arrow_r = renpy.render(self.repair_arrow, *args)
            render.blit(arrow_r, self.arrow_pos.tuple)
            
            wrench_r = renpy.render(self.wrench, *args)
            render.blit(wrench_r, (0,0))
            
            counter_r = renpy.render(self.repair_counter, *args)
            render.blit(counter_r, self.counter_pos.tuple)
            
            turn_count_r = renpy.render(Text(str(int(self.turn_count)), style="style_bike_repair_count"), *args)
            render.blit(turn_count_r, (70 - 4 * (self.turn_count / 10), 650))
            
            renpy.redraw(self, 0)
            return render
        
        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN or self.mouse_pressed:
                self.mouse_positions.append((x, y))
                self.mouse_pressed = True
            if ev.type == pygame.MOUSEBUTTONUP:
                self.started = True
                self.mouse_positions = []
                self.mouse_pressed = False
            pass


screen bike_repair_minigame():
    add BikeRepairMinigame()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
