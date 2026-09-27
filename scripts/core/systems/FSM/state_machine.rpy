init -9 python:
    class Trigger(object):
        """A Trigger is just a place holder used for the FSM

        Triggers are global in nature and when applied to any state machine
        it triggers to all statemachines.
        """
        def __init__(self, *args, **kwargs):
            self._name = "default"
        
        def copy(self):
            t = Trigger(self._name)
            for k, v in self.__dict__.items():
                t.__dict__[k] = v
            return t
        
        def __repr__(self):
            return self._name
        
        def __eq__(self, other):
            if isinstance(other, Trigger):
                return self._name == other._name
            else:
                return False
        
        def __ne__(self, other):
            return not self.__eq__(other)
        
        def fire(self, blank=False):
            for m in store.machines:
                m = store.machines[m]
                if blank:
                    m.trigger(self, blank)
                m.trigger(self)

    class State(object):
        """A State object holds a list of all the states that are
        Reachable from this state.  The next state is determined by
        the trigger supplied.

        In addition to keeping track of the state transitions, there
        is also the ability to accomplish tasks.  Tasks consist of
        setting, clearing, assigning, or generating one or more new
        Triggers.
        """
        def __init__(self, hint=None, help=None, delay=0):
            self._name = name
            self.hint = hint
            self.help = help
            self._delay = self.init_delay = delay
            self._table = {}
            self._actions = {}
        
        def __repr__(self):
            return '<{}.{} \'{}\'>'.format(self.__class__.__module__,
                                           self.__class__.__name__,
                                           self._name)
        
        def __str__(self):
            return self._name.replace(" ", "_").strip("'").lower()
        
        def __eq__(self, other):
            if isinstance(other, (unicode, str)):
                return self._name == other
            elif isinstance(other, State):
                return self._name == other._name
            else:
                raise TypeError
        
        def __ne__(self, other):
            return not (self == other)
        
        def copy(self):
            s = State(self._name)
            for k, v in self.__dict__.items():
                s.__dict__[k] = v
            return s
        
        def dump(self, log=True):
            result = ""
            for t in self._table:
                result += str(t)+"\n"
            if log:
                logger.info(result)
            return result
        
        def change_description(self, new_description):
            if isinstance(new_description, (str, unicode)):
                self.description = new_description
        
        
        
        
        
        def add(self, trigger, state, actions = None):
            if trigger._name in self._table.keys():
                raise DuplicateTriggerAddedException(message="Duplicate Trigger added : trigger name : "+trigger._name)
            self._table[trigger._name] = state
            if actions:
                self._actions[trigger._name] = actions
            else:
                self._actions[trigger._name] = []
        
        def clear(self, cleardelay=False):
            self._actions = {}
            if cleardelay:
                self.delay = 0
            self._table = {}
        
        def add_delay(self, amount=1):
            self.delay += amount
            return self.delay
        
        
        
        
        def trigger(self, trigger, machine, noactions, skip_delay=False, from_load=False):
            if isinstance(trigger, Trigger):
                tname = trigger._name
            else:
                tname = trigger
            
            if (self.delay != 0 and tname == "T_all_sleep" and not from_load):
                self.delay -= 1
                return None
            elif tname in self._table.keys() and (self.delay == 0 or skip_delay):
                
                
                if not noactions:
                    actions = self._actions[tname]
                    process_action_list(machine, actions, from_load)
                return self._table[tname]
            elif tname is None:
                return self._table.keys()[0], self._table[self._table.keys()[0]]
            else:
                return None
        
        def get_actions(self,trigger):
            return self._actions[trigger._name]
        
        @property
        def is_end_state(self):
            return not self._table
        
        @property
        def delay(self):
            return self._delay
        
        @delay.setter
        def delay(self, value):
            global fsm_data
            self._delay = value
            fsm_data.update_state_delay(self)


    def lookup_machine(name):
        return machines[name]


    class Machine(object):
        _trigger_queue = []
        _running = False
        
        def __init__(self, name, default_loc=[[None, None, None, None]],
                     vars=None, from_load=False,
                     default_outfit='dressed', outfits={},
                     default_pregnancy_schedule={}, can_birth_twins=True,
                     home_birth=False,
                     priority=0, can_talk=[True, True, True, True],
                     pregnancy_chance=0.4):
            if not from_load:
                self.init_args = {"name":name,
                                  "default_loc": default_loc,
                                  "vars": vars,
                                  "default_outfit": default_outfit,
                                  "outfits": outfits,
                                  "default_pregnancy_schedule": default_pregnancy_schedule,
                                  "can_birth_twins": can_birth_twins,
                                  "home_birth": home_birth,
                                  "priority": priority,
                                  "can_talk": can_talk,
                                  "pregnancy_chance": pregnancy_chance}
                self._states = {}
                self._actions = {}
                self.initial_state = None
            
            self.priority = priority
            
            self.set_can_talk_flags(can_talk)
            
            self._state = self.initial_state
            self._cleared_states = {}
            self._trigger_index = 0
            
            self._name = name.lower()
            
            if vars:
                self._vars = copy(vars)
            else:
                self._vars = {}
            
            
            
            self.outfit = OutfitManager(
                self, default_outfit, outfits=deepcopy(outfits))
            
            
            self.pregnancy = PregnancyManager(
                self._name, default_schedule=default_pregnancy_schedule,
                chance=pregnancy_chance, can_birth_twins=can_birth_twins,
                home_birth=home_birth)
            
            
            self.dating = DatingSystem(self._name)
            
            
            self._force_loc = LastUpdatedOrderedDict()
            self._force_loc[self._name] = [False, False, False, False]
            self.set_default_locations(default_loc)
            
            self._force_locations = LastUpdatedOrderedDict()
            self._force_locations[self._name] = [[None, None, None, None]]*7
            self._location_condition = LastUpdatedOrderedDict()
            self._location_condition[self._name] = None
            
            self.triggers = [var for name, var in globals().items() if name.startswith("T_"+self._name.lower())]
            
            self.talking = False
        
        def __reduce__(self):
            return (lookup_machine, (self._name,))
        
        def __repr__(self):
            if self._state is None:
                state = "NOT INIT."
            else:
                state = self._state._name
            
            if self.forced:
                return "{}@{} forced at {}. ({}%)".format(self._name, state, self.where, self.progress)
            else:
                return "{}@{} at {}. ({}%)".format(self._name, state, self.where, self.progress)
        
        def __str__(self):
            return self._name.replace(" ", "_").strip("'").lower()
        
        def __getattr__(self, name):
            vars = {k.replace(" ", "_").lower().replace("'", ""):v for k, v in self.__dict__.get('_vars', {}).items()}
            if name in vars.keys() and name not in self.__dict__.keys():
                return vars[name]
            elif name in self.__dict__.keys():
                return self.__dict__[name]
            else:
                raise AttributeError('{}.{} is not defined.'.format(self.__class__.__name__, name))
        
        def get_button_path(self, button_index=1, use_day_timer=False, use_old_path=False, use=(), name=None, **kwargs):
            if use_old_path:
                formatter = "objects/character_{0}_{1:02}"
            else:
                if isinstance(button_index, int):
                    formatter = "characters/{0}/buttons/character_{0}_{1:02}"
                else:
                    formatter = "characters/{0}/buttons/character_{0}_{1}"
            
            machine = kwargs.get('machine', self)
            stages = (None, None, 'bump', 'belly', 'belly', 'baby', 'baby')
            
            name = name or self._name
            stage = stages[machine.pregnancy.stage]
            use = set(use)
            
            use_baby = kwargs.get('use_baby', False)
            if use_baby:
                use.add('baby')
            if kwargs.get('use_pregnancy', use_baby):
                use |= {'bump', 'belly'}
            
            if stage in use:
                formatter += "{2}"
                suffix = machine.pregnancy.to_full_string
                formatted = formatter.format(name, button_index, suffix)
            else:
                formatted = formatter.format(name, button_index)
            
            if use_day_timer:
                return game.timer.image(formatted + "{}.png")
            else:
                return formatted + ".png"
        
        def copy(self):
            m = store.machines[self._name]
            for key, value in self.__dict__.items():
                if key == "_state" and value is not None:
                    m.__dict__[key] = self.__dict__[key].copy()
                elif key == "_states":
                    m.add(*[store.states[v._name].copy() for v in value if v is not None])
                elif key == "_cleared_states":
                    m._cleared_states = {v.copy():v.copy() for v in value if v is not None}
                elif isinstance(value, LastUpdatedOrderedDict):
                    newdict = LastUpdatedOrderedDict()
                    if key in ("_force_loc", "_location_condition"):
                        for k, v in reversed(value.items()):
                            newdict[k] = copy(v)
                    else:
                        for k, v in reversed(value.items()):
                            tmp = []
                            for l_dow in v:
                                tmp_tod = []
                                for l_tod in l_dow:
                                    if l_tod is not None:
                                        tmp_tod.append(l_tod.copy())
                                    else:
                                        tmp_tod.append(None)
                                tmp.append(tmp_tod)
                            newdict[k] = copy(tmp)
                    m.__dict__[key] = copy(newdict)
                elif key == "pregnancy":
                    m.__dict__[key] = self.pregnancy.copy()
                elif key == "triggers":
                    m.__dict__[key] = [store.triggers[v._name].copy() for v in value if v is not None]
                elif key == "_vars":
                    m._vars = {k:v for k, v in value.items()}
                else:
                    m.__dict__[key] = copy(value)
            return m
        
        def set_priority(self, priority):
            if renpy.game.context().init_phase:
                self.init_args['priority'] = priority
            self.priority = priority
        
        def get_default_locations(self):
            return deepcopy(self._default_locations)
        
        def set_default_locations(self, locations):
            if len(locations) == 1:
                self._default_locations = [locations[0]]*7
            elif len(locations) == 2:
                self._default_locations = [locations[0]]*5
                self._default_locations.extend([locations[1]]*2)
            elif len(locations) == 7:
                self._default_locations = deepcopy(locations)
            else:
                raise SummertimeSagaInitException("location attribute must be a matrix of 1x4, 2x4 or 7x4")
        
        @property
        def button_dialogue(self):
            return self._name+"_button_dialogue"
        
        @property
        def progress(self):
            if self._state is None or self._state.is_end_state:
                return 100
            elif len(self._states) != 0:
                return int(round(float(len(self._cleared_states))/float(len(self._states))*100, 0))
            else:
                return 0
        
        @property
        def can_talk(self):
            if self.forced:
                return True
            tow = 1 if game.timer.is_weekend() else 0
            return self._can_talk[tow][game.timer._tod]
        
        def dump(self, log=True):
            vlist = ""
            for k, v in self._vars.iteritems():
                vlist += "\n{}:{}".format(k, v)
            loc = "Location: {} Forced: {}\n".format(self.where, self._force_loc)
            rv = self._state.dump(False) + loc + vlist
            if log:
                logger.info(rv)
            return rv
        
        def add_action(self, *args):
            args = list(args)
            actions = args.pop() 
            for trigger in args: 
                try:
                    act = self._actions[trigger]
                except KeyError:
                    act = []
                act.extend(actions)
                self._actions[trigger] = act
            pass
        
        @classmethod
        def machine_trigger(self, trigger):
            for m_name, m in store.machines.items():
                try:
                    actions = m._actions[trigger]
                except KeyError:
                    
                    actions = []
                for i in xrange(0, len(actions) - 1, 2):
                    act = actions[i].lower()
                    target = actions[i + 1]
                    process_action(m, act, target)
        
        def advance(self, table_index=0):
            
            self.trigger(triggers[self._state._table.keys()[table_index]],
                         skip_delay=True, from_load=self, force_save=True)
            renpy.notify(self._state._name)
        
        @classmethod
        def trigger(cls, trigger,
                    noactions=False, skip_delay=False,
                    from_load=False, force_save=False):
            
            
            
            
            
            
            
            
            
            
            if trigger in cls._trigger_queue:
                return False
            cls._trigger_queue.append(trigger)
            
            
            if cls._running:
                return False
            cls._running = True
            machines_changed = []
            
            while len(cls._trigger_queue) > 0:
                trigger = cls._trigger_queue.pop()
                if from_load:
                    machines = {None: from_load}
                else:
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    machines = store.machines
                for m in machines.values():
                    s = m.get_state()
                    result = None
                    if s is not None:
                        result = s.trigger(trigger, m, noactions,
                                           skip_delay, bool(from_load))
                    if result is not None:
                        if result is not s:
                            m._cleared_states[m._state] = m._state
                        m._state = result
                        machines_changed.append(m)
                        if not from_load or force_save:
                            fsm_data.update_triggers(m, trigger)
            cls._running = False
            return len(machines_changed) > 0
        
        def add(self,*args):
            if len(args) != 0:
                for s in args:
                    if self._state is None:
                        self.initial_state = s
                        self._state = s
                    self._states[s] = s
            else:
                for s in [state for key, state in globals().items() if key.startswith("S_"+self._name)]:
                    if self._state is None:
                        self._state = s
                    self._states[s] = s
        
        def get(self, var, default=util.notset):
            if default is util.notset:
                return self._vars[var]
            return self._vars.get(var, default)
        
        def set(self, var, value):
            self._vars[var] = value
            fsm_data.update_vars(self, varname=var)
        
        def once(self, var):
            rv = self._vars.get(var, False)
            if not rv:
                self.set(var, True)
            return rv
        
        def max(self, *vars):
            vars = [self.get(v) for v in vars]
            return max(*vars)
        
        def min(self, *vars):
            vars = [self.get(v) for v in vars]
            return min(*vars)
        
        def toggle(self, flag):
            self._vars[flag] = not self._vars[flag]
            fsm_data.update_vars(self, varname=flag)
        
        def increment(self, var, amount=1):
            rv = self.get(var, 0) + amount
            self.set(var, rv)
            return rv
        
        def decrement(self, var, amount=1):
            rv = self.get(var, 0) - amount
            self.set(var, rv)
            return rv
        
        def get_state(self):
            return self._state
        
        def is_set(self,flag):
            fsm_data.update_vars(self, varname=flag)
            return self._vars[flag]
        
        def triggerOnZero(self, target, trigger):
            if target in self._vars:
                r = self._vars[target]-1
                if r < 0:
                    r = 0
            else:
                r = 0
            self._vars[target] = r
            fsm_data.update_vars(self, varname=target)
            if r <= 0:
                self.trigger(trigger)
        
        def set_can_talk_flags(self, can_talk):
            if len(can_talk) == 4:
                self._can_talk = [can_talk] * 2
            elif len(can_talk) == 2:
                self._can_talk = can_talk
            elif len(can_talk) == 1:
                self._can_talk = can_talk * 2
        
        def place(self, tod=None, dow=None, place=None, condition=None, machine=None, stack=False): 
            m = machine or self
            if stack:
                new_force_locations = self._force_locations[m._name]
            else:
                new_force_locations = [[None, None, None, None]]*7
            if tod is None and dow is None:
                if isinstance(place, list):
                    if len(place) == 1:
                        new_force_locations = [place[0]]*7
                    elif len(place) == 2:
                        new_force_locations = [place[0]]*5
                        new_force_locations.extend([place[1]]*2)
                    elif len(place) == 7:
                        new_force_locations = place
                    else:
                        raise SummertimeSagaInitException("location attribute must be a matrix of 1x4, 2x4 or 7x4")
                else:
                    new_force_locations = [[place]*4]*7
            elif tod is None and dow is not None:
                if isinstance(dow, list):
                    for d in dow:
                        new_force_locations[d] = [place]*4
                else:
                    new_force_locations[dow] = [place]*4
            elif tod is not None and dow is None:
                if isinstance(tod, list):
                    for i, current_dow in enumerate(self._force_locations[self._name]):
                        tmp = []
                        for j, current_tod in enumerate(current_dow):
                            if j not in tod:
                                tmp.append(current_tod)
                            else:
                                tmp.append(place)
                        new_force_locations[i] = copy(tmp)
                else:
                    for i, current_dow in enumerate(self._force_locations[self._name]):
                        tmp = []
                        for j, current_tod in enumerate(current_dow):
                            if j != tod:
                                tmp.append(current_tod)
                            else:
                                tmp.append(place)
                        new_force_locations[i] = copy(tmp)
            else:
                dow = list(dow)
                tod = list(tod)
                for d in dow:
                    for t in tod:
                        new_force_locations[d][t] = place
            self._location_condition[m._name] = condition
            self._force_locations[m._name] = copy(new_force_locations)
        
        def force(self, tod=None, flag=True, machine=None):
            m = machine or self
            new_force = [False, False, False, False]
            if isinstance(flag, list) and len(flag) == 4:
                new_force = flag
                self._force_loc[m._name] = copy(new_force)
                return
            if tod is None:
                new_force = [flag]*4
                self._force_loc[m._name] = copy(new_force)
                return
            if not isinstance(tod, list):
                tod = [tod]
            for current_tod in tod:
                new_force[current_tod] = flag
            self._force_loc[m._name] = copy(new_force)
            return
        
        def unforce(self, machine = None):
            m = machine or self
            if m is self:
                self._force_loc[self._name] = [False, False, False, False]
                self._force_locations[self._name] = [[None, None, None, None]]*7
                self._location_condition[self._name] = None
            
            else:
                try:
                    del self._force_loc[m._name]
                except KeyError:
                    pass
                try:
                    del self._force_locations[m._name]
                except KeyError:
                    pass
                try:
                    del self._location_condition[m._name]
                except KeyError:
                    pass
            
            if self._force_loc.isempty:
                self._force_loc[self._name] = [False, False, False, False]
            if self._force_locations.isempty:
                self._force_locations[self._name] = [[None, None, None, None]]*7
            if self._location_condition.isempty:
                self._location_condition[self._name] = None
        
        def move(self, location, ticks=1):
            if isinstance(location, Location):
                location = location.var_name
            self.set('_move', (location, game.timer.now + ticks))
        
        @property
        def where(self):
            global game
            _loc = None
            _loc_self = None
            
            move, expire = self.get('_move', (None, -1))
            if move and move in locations:
                if expire <= game.timer.now:
                    self.set('_move', (None, -1))
                else:
                    return locations[move]
            
            shadow = self.get('_shadow', None)
            if shadow and shadow in machines:
                return machines[shadow].where
            
            if self.pregnancy:
                if self.pregnancy.where is not None:
                    return self.pregnancy.where
            try:
                for key in reversed(self._force_loc):
                    if not self._force_loc[key][game.timer._tod]:
                        _loc = self._default_locations[game.timer._dow][game.timer._tod]
                    else:
                        if self._force_locations[key][game.timer._dow][game.timer._tod] is not None:
                            if self._location_condition[key] is None or eval(self._location_condition[key]):
                                if self._name == key:
                                    if not self._state or self._state.delay == 0:
                                        _loc_self = self._force_locations[key][game.timer._dow][game.timer._tod]
                                else:
                                    _loc = self._force_locations[key][game.timer._dow][game.timer._tod]
                                    break
                            else:
                                _loc = self._default_locations[game.timer._dow][game.timer._tod]
                        else:
                            _loc = self._default_locations[game.timer._dow][game.timer._tod]
            except IndexError:
                _loc = self._default_locations[game.timer._dow][game.timer._tod - 1]
            if game.in_shower is not None:
                if game.in_shower._name == self._name and (_loc in L_home.get_all_children() and (_loc_self is None)):
                    _loc = L_home_shower
            if (_loc_self or _loc) is None:
                rv = self._default_locations[game.timer._dow][game.timer._tod]
            else:
                rv = _loc_self or _loc
            if isinstance(rv, list):
                ls = LocationSchedule([[rv] * 4])
                ls.seed = hash(self._name + ':MACHINE')
                return ls.get
            return rv
        
        def where_is(self, *locations):
            for loc in locations:
                if loc.is_here(self):
                    return True
            return False
        
        @property
        def forced(self):
            return self.pregnancy.character_bedridden or \
                   self._force_loc[self._name][game.timer._tod]
        
        def between_states(self, beginning_state, *end_states):
            if len(end_states) == 1:
                end_states = end_states[0]
                try:
                    s = iter(end_states) 
                except TypeError:
                    if isinstance(end_states, State):
                        return (((beginning_state == self._state and beginning_state.delay == 0) or beginning_state in self._cleared_states) and end_states not in self._cleared_states)
                    return False
                else:
                    if (beginning_state == self._state and beginning_state.delay == 0) or beginning_state in self._cleared_states:
                        for s in end_states:
                            if s in self._cleared_states:
                                return False
                        return True
                    return False
            else:
                if (beginning_state == self._state and beginning_state.delay == 0) or beginning_state in self._cleared_states:
                    for s in end_states:
                        if s in self._cleared_states:
                            return False
                    return True
                return False
        
        def finished_state(self, *states):
            if len(states) == 1:
                states = states[0]
                try:
                    s = iter(states) 
                except TypeError:
                    if isinstance(states, State):
                        return (states in self._cleared_states)
                    else:
                        return
                else:
                    for s in states:
                        if s not in self._cleared_states:
                            return False
                    return True
            else:
                for s in states:
                    if s not in self._cleared_states:
                        return False
                return True
        
        def is_state(self, *states):
            if len(states) == 1 and isinstance(states[0], (list, tuple, set)):
                states = states[0]
            if self._state in states:
                return self._state.delay == 0
        
        def finished_inclusive(self, *states):
            return (self.is_state(*states) or self.finished_state(*states))
        
        def reset(self):
            self.__init__(from_load=True, **self.init_args)
            for s in self._states:
                s.delay = s.init_delay
            fsm_data.update_vars(self)
            fsm_data.machine_triggers = [r for r in fsm_data.machine_triggers if r[0] != self._name]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
