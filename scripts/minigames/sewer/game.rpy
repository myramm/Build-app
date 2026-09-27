init python hide:
    '''
    Infiltrate the warehouse via the poop chute by clearing piles of
    poop and heaving as appropriate. Talk about going in the out door!
    '''

    from math import ceil, floor
    from random import randint, random

    from store import ImageReference as Ref


    ANIMATION = .5
    ANON = config.screen_width / 2 - 512
    LOOP = 1366
    POOP = config.screen_width / 2 + 80
    SPEED = 135.
    STRIDE = 120.
    SWAP = {'left': 'right', 'right': 'left'}


    class SewerMinigame(renpy.python.NoRollback):
        __version__ = 0
        
        def __init__(self, **kwargs):
            super(SewerMinigame, self).__init__(**kwargs)
            
            self.sm = sm = SpriteManager(ignore_time=True,
                                         predict=self.predict,
                                         update=self.update)
            
            self.sewer = sm.create('sewer_pipe')
            self.poop = sm.create('sewer_poop')
            self.anon = sm.create('empty')
            self.water = sm.create('sewer_water')
            
            paces = int(floor(600 / STRIDE))
            
            self.anon.x = ANON - floor(paces * STRIDE - ANIMATION * SPEED)
            self.anon.y = 58
            
            self.poop.x = POOP
            self.poop.y = 138
            
            self.water.y = 263
            
            self.clock = 0
            self.crawl = 0
            self.delay = False
            self.frame = ['left', 'right'][paces % 2]
            self.phase = 'intro'
            self.score = 0
        
        def update(self, st):
            delta = st - self.clock
            self.clock = st
            
            travel = 0
            
            if self.delay > 0:
                self.delay -= delta
            
            elif self.delay is not False:
                self.phase = 'stop'
                self.delay = False
                renpy.restart_interaction()
            
            elif self.phase == 'intro':
                travel = delta * SPEED
                self.anon.x = min(self.anon.x + travel, ANON)
                if self.anon.x == ANON:
                    self.phase = 'poop'
                    renpy.restart_interaction()
            
            elif self.phase == 'outro':
                travel = delta * SPEED
                self.anon.x = self.anon.x + travel
            
            elif self.phase == 'stop' and self.poop.x <= POOP:
                push = ceil((self.sm.width - self.poop.x) / STRIDE) + randint(0, 6)
                push += 1 - (push % 2)
                self.poop.set_child(Ref('sewer_poop'))
                self.poop.x += push * STRIDE + ANIMATION * SPEED
            
            elif self.phase in ('poop', 'sick', 'stop'):
                pass
            
            elif self.phase == 'move':
                travel = delta * SPEED
                
                self.poop.x = self.poop.x - travel
                self.sewer.x = (self.sewer.x - travel) % LOOP - LOOP
                
                if self.poop.x <= POOP:
                    self.phase = 'poop'
                    renpy.restart_interaction()
            
            if travel:
                b = self.crawl / STRIDE
                self.crawl += travel
                a = self.crawl / STRIDE
                
                if b == 0 or b < floor(a):
                    sick = self.phase == 'move' and self.frame == 'right' and \
                           self.crawl / self.sm.width / 2 > random()
                    
                    if sick:
                        self.phase = 'sick'
                        self.anon.set_child(Ref('sewer_anon_sick'))
                        self.poop.x = self.poop.x + travel
                        self.sewer.x = self.sewer.x + travel
                        renpy.restart_interaction()
                    
                    else:
                        self.frame = SWAP[self.frame]
                        self.anon.set_child(Ref('sewer_anon_' + self.frame))
            
            self.water.x = (self.sewer.x + st * -30) % LOOP - LOOP
            
            return .01
        
        def move(self):
            self.crawl = 0
            self.score += 1
            if self.score > 7 and self.poop.x > self.sm.width:
                self.phase = 'outro'
            else:
                self.phase = 'move'
        
        def puke(self):
            self.phase = 'wait'
            self.anon.set_child(Ref('sewer_anon_puke'))
            self.delay = 1.3
        
        def push(self):
            self.phase = 'wait'
            self.anon.set_child(Ref('sewer_anon_push'))
            self.poop.set_child(Ref('sewer_poop_push'))
            self.delay = 1.1
        
        def predict(self):
            return ('sewer_anon_left',
                    'sewer_anon_puke',
                    'sewer_anon_push',
                    'sewer_anon_right',
                    'sewer_anon_sick',
                    'sewer_pipe',
                    'sewer_poop',
                    'sewer_poop_push',
                    'sewer_water')


    store.SewerMinigame = SewerMinigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
