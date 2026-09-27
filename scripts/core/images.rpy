init -5 python:
    class AnimatedImage(renpy.Displayable):
        def __init__(self, name, images, machine, scale=1., **kwargs):
            super(AnimatedImage, self).__init__(**kwargs)
            self._name = name
            self._images = images
            self._image_count = 0
            self._image_length = len(images)
            self._machine = machine
            self._scale = scale
        
        def render(self, width, height, st, at):
            if self._image_count >= self._image_length:
                self._image_count = 0
            
            r = renpy.render(renpy.displayable(self._name + " " + str(self._images[self._image_count])), width, height, st, at)
            renpy.redraw(self, self._machine.get("sex speed") * self._scale)
            self._image_count += 1
            return r

    class PulseImage(renpy.Displayable):
        def __init__(self, img1, img2, delay1 = 0.1, delay2 = 0.1, **kwargs):
            super(PulseImage, self).__init__(**kwargs)
            self._image1 = renpy.displayable(img1)
            self._image2 = renpy.displayable(img2)
            self._toggle = True
            self._delay1 = delay1
            self._delay2 = delay2
        
        def render(self, width, height, st, at):
            if self._toggle:
                self._toggle = False
                r = renpy.render(self._image1, width, height, st, at)
                delay = self._delay1
            else:
                self._toggle = True
                r = renpy.render(self._image2, width, height, st, at)
                delay = self._delay2
            renpy.redraw(self, delay)
            return r

    class PulseHoverImage(renpy.Displayable):
        def __init__(self, img1, delay1 = 0.1, delay2 = 0.1, **kwargs):
            super(PulseHoverImage, self).__init__(**kwargs)
            self._image1 = renpy.displayable(img1)
            self._image2 = HoverImage(img1)
            self._toggle = True
            self._delay1 = delay1
            self._delay2 = delay2
        
        def render(self, width, height, st, at):
            if self._toggle:
                self._toggle = False
                r = renpy.render(self._image1, width, height, st, at)
                delay = self._delay1
            else:
                self._toggle = True
                r = self._image2.render(width, height, st, at)
                delay = self._delay2
            renpy.redraw(self, delay)
            return r

    class HoverImage(renpy.Displayable):
        h_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
        n_matrix = im.matrix.identity()
        def __init__(self, img, **kwargs):
            super(HoverImage, self).__init__(**kwargs)
            if isinstance(img, basestring) and img.startswith("transform"):
                self._image = img
            else:
                self._image = renpy.displayable(img)
            
            self._matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
        
        def render(self, width, height, st, at):
            if str(self._image).startswith("transform"):
                r = renpy.render(renpy.displayable(ImageReference(str(self._image).split("-")[1] + "b")), width, height, st, at)
            else:
                r = renpy.render(im.MatrixColor(self._image, self._matrix), width, height, st, at)
            return r

    class Timer(renpy.Displayable):
        def __init__(self, bg, screen, label, timer, timer_decrement = 0.1, **kwargs):
            super(Timer, self).__init__(**kwargs)
            self._bg = renpy.displayable(bg)
            self._screen = screen
            self._label = label
            
            self._TIMER = timer
            self._timer = self._TIMER
            self._TIMER_DECREMENT = timer_decrement
            self._start_timer = clock()
        
        def render(self, width, height, st, at):
            if int((self._TIMER - self._timer) / self._TIMER_DECREMENT) <= int((clock() - self._start_timer) / self._TIMER_DECREMENT):
                self._timer -= self._TIMER_DECREMENT
            
            if self._timer <= 0:
                renpy.hide_screen(self._screen)
                renpy.jump(self._label)
            
            render = renpy.render(self._bg, width, height, st, at)
            renpy.redraw(self, 0)
            return render

    class Cutscene(renpy.Displayable):
        def __init__(self, image, text, **properties):
            super(Cutscene, self).__init__(**properties)
            self.image = renpy.displayable(image)
            self.text = Text(text, style = "style_cutscene")
        
        def render(self, width, height, st, at):
            render = renpy.render(self.image, width, height, st, at)
            text_r = renpy.render(self.text, width, height, st, at)
            text_w, text_h = text_r.get_size()
            render.blit(text_r, ((1024-text_w)/2,650))
            return render
        
        def event(self, ev, x, y, st):
            pass

    def FilteredText(txt, style="style_cutscene", **kwargs):
        return Text(_(config.say_menu_text_filter(txt)), style=style, **kwargs)

    class BoxButton(renpy.Displayable):
        def __init__(self, text, text_style="style_box_default", image=None, **properties):
            super(BoxButton, self).__init__(**properties)
            self.text = text
            self._style = text_style
            self._image = image
            self.start = renpy.displayable("buttons/custom_box_end.png")
            self.end = renpy.displayable(im.Flip("buttons/custom_box_end.png", horizontal=True))
            self.middle = renpy.displayable("buttons/custom_box_middle.png")
            self.bg = renpy.displayable("buttons/custom_box_ground.png")
            self.text_d = Text(self.text, style=self._style)
            self.width = 20
            self.height = 39
            self.char_width = 10
            self.min_width = 280
            self.image_margin = 10
        
        def get_renders(self, width, height, st, at):
            start_r = renpy.render(self.start, width, height, st, at)
            middle_r = renpy.render(self.middle, width, height, st, at)
            end_r = renpy.render(self.end, width, height, st, at)
            text_r = renpy.render(self.text_d, width, height, st, at)
            if self._image is not None:
                image_r = renpy.render(renpy.displayable(self._image), width, height, st, at)
            else:
                image_r = None
            return start_r, middle_r, end_r, text_r, image_r
        
        def render(self, width, height, st, at):
            render = renpy.render(self.bg, width, height, st, at)
            start_r, middle_r, end_r, text_r, image_r = self.get_renders(width, height, st, at)
            render.blit(start_r, (0, 0))
            num_middle = len(self.text) * float(self.char_width) / self.width
            num_middle = int(num_middle)
            min_middle = int(float(self.min_width)/self.width - 2)
            if num_middle < min_middle:
                num_middle = min_middle
            for i in range(num_middle):
                render.blit(middle_r, ((i+1)*self.width, 0))
            render.blit(end_r, ((num_middle+1)*self.width, 0))
            text_width, text_height = text_r.get_size()
            text_x = (self.width * (num_middle + 2) / 2) - (text_width / 2)
            text_y = max(0, self.height / 2 - (text_height / 2))
            render.blit(text_r, (text_x, text_y))
            self.total_width, self.total_height = self.width * (num_middle + 2), 39
            if image_r is not None:
                w, h = image_r.get_size()
                y = (self.height - h) / 2
                render.blit(image_r, (self.image_margin, y))
            return render
        
        def event(self, ev, x, y, st):
            pass

    class HoverBoxButton(BoxButton):
        def get_renders(self, width, height, st, at):
            start_r = renpy.render(im.MatrixColor(self.start, HoverImage.h_matrix), width, height, st, at)
            middle_r = renpy.render(im.MatrixColor(self.middle, HoverImage.h_matrix), width, height, st, at)
            end_r = renpy.render(im.MatrixColor(self.end, HoverImage.h_matrix), width, height, st, at)
            text_r = renpy.render(self.text_d, width, height, st, at)
            if self._image is not None:
                image_r = renpy.render(im.MatrixColor(renpy.displayable(self._image), HoverImage.h_matrix), width, height, st, at)
            else:
                image_r = None
            return start_r, middle_r, end_r, text_r, image_r

    class SexButton(renpy.Displayable):
        def __init__(self, text, **properties):
            super(SexButton, self).__init__(**properties)
            self._bg = renpy.displayable("buttons/button_sex_options.png")
            self._text = text
        
        def get_renders(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            text_r = renpy.render(Text(self._text), width, height, st, at)
            return render, text_r
        
        def render(self, width, height, st, at):
            render, text_r = self.get_renders(width, height, st, at)
            mw, mh = render.get_size()
            w, h = text_r.get_size()
            x = (mw - w) / 2
            y = (mh - h) / 2
            render.blit(text_r, (x, y))
            return render

    class HoverSexButton(SexButton):
        def get_renders(self, width, height, st, at):
            render = renpy.render(im.MatrixColor(self._bg, HoverImage.h_matrix), width, height, st, at)
            text_r = renpy.render(Text(self._text), width, height, st, at)
            return render, text_r
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
