init python:
    class JennyCamera(renpy.Displayable):
        def __init__(self, background_nb, exit_label, **properties):
            super(JennyCamera, self).__init__(**properties)
            self._bg = "backgrounds/location_home_jennybedroom_photo{}.jpg".format(background_nb)
            self.pos = Vector2.center(1600,900)
            self.exit_lbl = exit_label
            self.mouse_down = False
            self.old_x, self.old_y = 0,0
            self.overlay = renpy.displayable("characters/jenny/layeredimage/jenny_camera_view.png")
            self.time = 0
            self.snap = renpy.displayable("buttons/jenny_camera.png")
            self.blur_level = random.randint(-30, 30) / 10.0 if not renpy.variant("mobile") else 0
        
        def render(self, width, height, st, at):
            render = renpy.render(renpy.displayable("ground.png"), width, height, st, at)
            if self.blur_level:
                _bg = im.Blur(self._bg, abs(self.blur_level))
            else:
                _bg = renpy.displayable(self._bg)
            
            pic_r = renpy.render(_bg, width, height, st, at)
            render.blit(pic_r, self.pos.tuple)
            overlay_r = renpy.render(self.overlay, width, height, st, at)
            render.blit(overlay_r, (0,0))
            snap_r = renpy.render(self.snap, width, height, st, at)
            render.blit(snap_r, (850,650))
            renpy.redraw(self, 0)
            return render
        
        def take_pic(self):
            renpy.jump(self.exit_lbl)
        
        def blur_increment(self, amount):
            minmax = 5.0
            self.blur_level = min(minmax, max(self.blur_level + amount, -minmax))
            self.blur_level = float(self.blur_level)
        
        def move(self, x, y):
            move_dst = Vector2(x, y)-Vector2(self.old_x, self.old_y)
            self.pos = self.pos - move_dst
            self.pos.clamp(Vector2(1024-1600,768-900), Vector2(0,0))
        
        def event(self, ev, x, y, st):
            if self.mouse_down:
                self.move(x, y)
                self.old_x, self.old_y = x, y
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if ev.button == 1:
                    if not self.mouse_down:
                        self.mouse_down = True
                        self.old_x, self.old_y = x, y
            
            elif ev.type == pygame.MOUSEBUTTONUP:
                if ev.button == 1:
                    self.mouse_down = False
                    if 850<=x<=850+125 and 650<=y<=650+106:
                        self.take_pic()
                elif ev.button == 4:
                    
                    self.blur_increment(-0.1)
                elif ev.button == 5:
                    
                    self.blur_increment(0.1)

screen jenny_photo1():
    add JennyCamera("01", "kitchen_jenny_sluttygram_pics_post_photo1")

screen jenny_photo2():
    add JennyCamera("03", "kitchen_jenny_sluttygram_pics_post_photo2")

screen jenny_photo3():
    add JennyCamera("02", "kitchen_jenny_sluttygram_pics_post_photo3")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
