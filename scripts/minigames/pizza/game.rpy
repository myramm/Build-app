init python hide:
    '''
    Deliver pizzas by making an attempt as Anon passes by the front door
    of the house with the corresponding slice over it. Returns a list of
    pizzas where success=True, failure=False, inaction=None.
    '''

    from itertools import chain
    from math import cos, pi, sin
    from random import randint, random, shuffle


    class PizzaMinigame(renpy.python.NoRollback):
        __version__ = 0
        
        house = 550
        vehicle = 450
        
        def __init__(self, level, **kwargs):
            super(PizzaMinigame, self).__init__(**kwargs)
            
            self.sm = sm = SpriteManager(ignore_time=True,
                                         predict=self.predict,
                                         update=self.update)
            
            self.level = level
            self.intro = 6. / level
            self.outro = 9. / level
            
            self.scene = ((sm.create('pizza_scene_sky'), 25.),
                          (sm.create('pizza_scene_grass'), 1),
                          (sm.create('pizza_scene_trees'), 5.),
                          (sm.create('pizza_scene_road'), .75))
            
            buyers = xrange(1, 7)
            pizzas = xrange(1, 4)
            
            self.span, self.houses, self.target = self.generate(buyers, pizzas)
            
            self.schedule = Scheduler()
            
            self.eta = self.intro + self.outro
            self.status = dict.fromkeys(pizzas)
            
            self.anon = sm.create(Fixed('pizza_vehicle_{:02d}'.format(level),
                                        xsize=self.vehicle))
        
        def attempt(self, pizza):
            sprite = self.target.get(pizza, None)
            
            if sprite:
                window = self.house / 4
                anon = self.anon.x + self.vehicle / 2
                self.status[pizza] = \
                    sprite.x + window <= anon <= sprite.x + self.house - window
        
        def exit(self):
            return self.status.values()
        
        def generate(self, buyers, pizzas):
            buyers, pizzas = list(buyers), list(pizzas)
            pizzas += [None] * (len(buyers) - len(pizzas))
            verges = chain((0,), iter(lambda: randint(450, 800), 0))
            
            shuffle(buyers)
            shuffle(pizzas)
            
            houses = []
            offset = 0
            target = {}
            
            for buyer, pizza, verge in zip(buyers, pizzas, verges):
                offset += verge
                
                house = Fixed('pizza_house_{:02d}'.format(buyer),
                              fit_first='height',
                              xsize=self.house,
                              yanchor=1., ypos=578)
                
                if pizza:
                    house.add('pizza_slice_{:02d}'.format(pizza))
                
                sprite = self.sm.create(Fixed(house, fit_first='width'))
                
                if pizza:
                    target[pizza] = sprite
                
                houses.append((sprite, offset))
            
            offset += self.house
            
            return offset, houses, target
        
        def update(self, st):
            speed = self.level * 200
            px = st * -speed
            pw = self.sm.width
            
            if st == 0:
                self.eta += float(pw + self.span) / speed
                self.schedule(self.eta, Function(self.exit))
                renpy.restart_interaction()
            
            for sprite, factor in self.scene:
                sprite.x = px / factor % pw - pw
            
            for sprite, offset in self.houses:
                sprite.x = speed * self.intro + offset + pw + px
                if sprite.x < -self.house:
                    sprite.destroy()
            
            if random() > .98:
                self.anon.y = random() * 3
            
            if st < self.intro:
                z = st / self.intro
                self.anon.x = self.vehicle * (sin(z * pi / 2) - 1)
            
            if st > self.eta - self.outro:
                z = (st - self.eta) / self.outro + 1
                self.anon.x = -pw * (cos(z * pi / 2) - 1)
            
            return .01
        
        def predict(self):
            return [s.cache.child for s in chain((s[0] for s in self.scene),
                                                 (h[0] for h in self.houses),
                                                 (self.anon,))]


    store.PizzaMinigame = PizzaMinigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
