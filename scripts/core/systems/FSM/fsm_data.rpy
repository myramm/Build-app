init -10 python:
    class FSMData(object):
        def __init__(self, *args, **kwargs):
            self.machine_data = {}
            self.machine_triggers = []
            self.preload()
        
        def __getattr__(self, attr):
            """
                This getattr overloading ensures that something will always return
                when trying to access one of this class' attribute.

                If the attribute already has a value, then return that (classic behavior),
                otherwise, reinstantiate the class locally, and return the attribute
                as defined in the __init__ method.

                If there is still no attribute, will return None. This behavior can be changed
                by editing the line
                    return self.__class__().__dict__[attr]
                into
                    return self.__class__().__dict__[attr]
                which will throw a KeyError exception if the attribute doesn't exist.
            """
            val = self.__dict__.get(attr)
            if val is not None:
                return val
            else:
                try:
                    return self.__class__().__dict__[attr]
                except KeyError:
                    return object.__getattr__(attr)
        
        
        def preload(self):
            if 'states_delays' not in self.__dict__.keys():
                self.states_delays = {}
            for mname, m in store.machines.items():
                if m._name.lower() not in self.machine_data.keys():
                    self.machine_data[m._name.lower()] = {}
                update_dict = {
                                "triggers": [],
                                "vars": {},
                                "pregnancy": {},
                                "outfit": {},
                                "dating": {},
                }
                
                for key in update_dict.keys():
                    if key not in self.machine_data[m._name.lower()].keys():
                        self.machine_data[m._name.lower()][key] = copy(update_dict[key])
        
        
        
        
        
        
        
        
        
        def dump(self):
            for key, items in self.machine_data.items():
                logger.info("name : " + key)
                for key, value in items.items():
                    logger.info(key + " : " + repr(value))
        
        def update_vars(self, machine, varname="all"):
            if isinstance(machine, str) or isinstance(machine, unicode):
                machine = store.machines[machine]
            if varname.lower() == "all":
                self.machine_data[machine._name.lower()]["vars"].update(machine._vars)
            else:
                varvalue = copy(machine._vars[varname])
                self.machine_data[machine._name.lower()]["vars"][varname] = varvalue
            renpy.retain_after_load()
        
        def update_triggers(self, machine, *triggers):
            for trigger in triggers:
                self.machine_triggers.append((machine._name, trigger))
            renpy.retain_after_load()
        
        def update_state_delay(self, state):
            self.states_delays[state._name] = state.delay
            renpy.retain_after_load()
        
        
        def saved_triggers(self, machine):
            if isinstance(machine, str) or isinstance(machine, unicode):
                machine = store.machines[machine]
            return [data[1] for data in self.machine_triggers if data[0] == machine._name]
        
        def saved_vars(self, machine):
            return self.machine_data[machine._name.lower()]["vars"]


    def load_fsm_data():
        logger.info("Loading stored machine state...")
        time_start = clock()
        global fsm_data
        fsm_data.preload()
        
        for machine in store.machines.values():
            machine.__init__(from_load=True, **machine.init_args)
        for sname, s in store.states.items():
            s._delay = s.init_delay
        
        
        for state, delay in fsm_data.states_delays.items():
            s = store.states.get(state)
            if s is not None:
                s._delay = delay
        
        
        for (machine, trigger) in fsm_data.machine_triggers:
            try:
                m = store.machines[machine]
                m.trigger(trigger, skip_delay=True, from_load=m)
            except NameError:
                continue
        
        
        for name, machine in store.machines.items():
            try:
                items = fsm_data.machine_data[name]
            except KeyError:
                continue
            machine._vars.update(copy(items["vars"]))
            machine.pregnancy.deserialize(items["pregnancy"])
            machine.outfit.deserialize(items["outfit"])
            machine.dating.deserialize(items["dating"])
        
        logger.info("Finished loading stored machine state. Loading took {} ms".format((clock()-time_start)*1000))

    def reset_machines_to_init_state():
        for mname, m in store.machines.items():
            m.__init__(from_load=True, **m.init_args)
        for sname, s in store.states.items():
            s.delay = s.init_delay
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
