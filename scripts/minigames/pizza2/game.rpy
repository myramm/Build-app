init python hide:
    '''
    Make the pizzas by clicking the topppings in the correct order
    within the time limit. One mistake and you're out!
    '''

    from itertools import chain
    from random import sample


    def intersperse(iterable, item):
        it = iter(iterable)
        yield next(it)
        for v in it:
            yield item
            yield v


    class Pizza2Minigame(renpy.python.NoRollback):
        __version__ = 0
        
        PASS = 0
        FAIL = 1
        TIME = 2
        
        options = ('basil', 'beef', 'broccoli', 'cheese', 'ham', 'mushroom',
                   'olive_black', 'olive_green', 'onion', 'pepper_green',
                   'pepper_red', 'pepperoni', 'pineapple', 'tomato')
        
        recipes = {'hawaiian': ('pineapple', 'ham'),
                   'margherita': ('basil',),
                   'meatlover': ('mushroom', 'pepperoni', 'beef'),
                   'pepperoni': ('pepperoni', 'olive_black'),
                   'special': ('olive_green', 'mushroom', 'onion',
                               'pepper_green', 'broccoli', 'pepperoni'),
                   'spicy': ('pepper_green', 'onion', 'pepper_red', 'beef'),
                   'veggie': ('mushroom', 'broccoli', 'olive_green',
                              'pepper_green', 'onion')}
        
        def __init__(self, order=None, quota=None, **kwargs):
            super(Pizza2Minigame, self).__init__(**kwargs)
            
            self.schedule = Scheduler()
            
            self.opts = sample(self.options, len(self.options))
            self.order = order or \
                sample(self.recipes, quota or len(self.recipes))
            self.plan = chain(
                (('intro', 4), ('enter', 2)),
                intersperse((('play', p) for p in self.order), ('swap', 2)),
                (('leave', 1), ('pass',)))
            
            self.code = self.PASS
            self.expect = 'tomato'
            self.output = ()
            self.pizza = None
            self.toppings = []
            
            self.next()
        
        def __reduce__(self):
            return (self.__class__, (self.order,))
        
        def add(self, topping):
            self.toppings.append(topping)
            
            if topping != self.expect:
                return self.next(('fail', self.FAIL))
            
            try:
                self.expect = next(self.recipe)
            except StopIteration:
                self.output = self.order[:len(self.output) + 1]
                self.next()
        
        def next(self, spec=None):
            self.schedule.clear()
            
            if not spec:
                spec = next(self.plan)
            
            self.phase = spec[0]
            
            if self.phase == 'play':
                action = Function(self.next, ('fail', self.TIME))
                
                self.pizza = spec[1]
                recipe = ('tomato', 'cheese') + self.recipes[self.pizza]
                
                self.recipe = iter(recipe)
                self.toppings = []
                self.ttl = len(recipe) * 1.5
                
                self.expect = next(self.recipe)
            
            elif self.phase == 'fail':
                self.code = spec[1]
                self.ttl = 0
            
            else:
                self.ttl = spec[1] if len(spec) > 1 else 0
                action = False
            
            if self.ttl:
                self.schedule(self.ttl, action or Function(self.next))


    store.Pizza2Minigame = Pizza2Minigame
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
