init python:
    class PregnancyMinigame(renpy.Displayable):
        def __init__(self, chance, **properties):
            super(PregnancyMinigame, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/pregnancy_minigame_01.jpg")
            self.spin_button = renpy.displayable("buttons/pregnancy_button.png")
            self._wheel_base = renpy.displayable("buttons/pregnancy_wheel.png")
            self.is_spinning = False
            self.delay = 0
            self.angle = 0
            self.speed = 0
            self.center = (512, 384)
            self.pregnancy_chance = chance
            self.result = None
        
        def spin(self):
            self.is_spinning = True
            self.speed = random.randint(30, 71)
            rotation = self.speed * (self.speed + 1) / 2
            if random.randint(1, 100) <= self.pregnancy_chance:
                self.angle = -15 + random.randint(1, 30) - rotation
            else:
                self.angle = +15 + random.randint(1, 330) - rotation
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            self.angle = (self.angle+self.speed) % 360
            if self.speed > 0:
                self.speed -= 1
            if self.delay > 0:
                self.result = self.angle >= 345 or self.angle <= 15
                renpy.timeout(0)
            if self.speed == 0 and self.is_spinning:
                self.delay = 1
            
            instructions_r = renpy.render(Text("Spin the wheel of conception!", style = "style_instructions"), width, height, st, at)
            text_width, text_height = instructions_r.get_size()
            render.blit(instructions_r, ((512 - (text_width / 2)), 24))
            percentage_r = renpy.render(Text("{}%".format(self.pregnancy_chance)), width, height, st, at)
            text_width, text_height = percentage_r.get_size()
            render.blit(percentage_r, ((512 - (text_width / 2)),(384-(text_height/2))))
            self.wheel = Fixed(Transform(self._wheel_base,
                anchor=(.5, .501), pos=(.5, .5), rotate=self.angle,
                rotate_pad=False, subpixel=True, transform_anchor=True))
            if not self.is_spinning:
                spin_button_r = renpy.render(self.spin_button, width, height, st, at)
                render.blit(spin_button_r, (422, 666))
            wheel_r = renpy.render(self.wheel, width, height, st, at)
            render.blit(wheel_r, (0, 0))
            renpy.redraw(self, self.delay)
            return render
        
        def event(self, ev, x, y, st):
            if not self.is_spinning:
                if 422<=x<=585 and 666<=y<=733:
                    self.spin_button = im.MatrixColor(renpy.displayable("buttons/pregnancy_button.png"), im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07))
                    if ev.type == pygame.MOUSEBUTTONDOWN and not self.is_spinning:
                        self.spin()
                else:
                    self.spin_button = renpy.displayable("buttons/pregnancy_button.png")
            
            if self.result is not None:
                return self.result


screen pregnancy_minigame(chance):
    add PregnancyMinigame(chance)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
