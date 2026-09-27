init -10 python:
    def fsm_action_locklocation(target, machine, from_load=False):
        if not isinstance(target, Location):
            raise FSMActionError("target for action 'locklocation' has to be a Location instance")
        elif not from_load:
            target.lock()
        else:
            return

    def fsm_action_unlocklocation(target, machine, from_load=False):
        if not isinstance(target, Location):
            raise FSMActionError("target for action 'unlocklocation' has to be a Location instance")
        elif not from_load:
            target.unlock()
        else:
            return

    def fsm_action_set(target, machine, from_load=False):
        if from_load:
            return
        value = True
        if isinstance(target, (list, tuple)):
            if len(target) == 3:
                machine, target, value = target
            elif len(target) == 2:
                machine, target = target
            else:
                raise FSMActionError("length of target list for action 'set' is not 2 or 3 on machine M_{}".format(machine._name))
            if isinstance(machine, unicode) or isinstance(machine, str):
                machine = store.machines[machine]
        machine.set(target, value)

    def fsm_action_clear(target, machine, from_load=False):
        if from_load:
            return
        if isinstance(target, (list, tuple)):
            if len(target) != 2:
                raise FSMActionError("length of target list for action 'clear' is not 2 on machine M_{}".format(machine._name))
            machine, target = target
            if isinstance(machine, unicode) or isinstance(machine, str):
                machine = store.machines[machine]
        machine.set(target, False)

    def fsm_action_toggle(target, machine, from_load=False):
        if from_load:
            return
        if machine.is_set(target):
            machine.set(target,False)
        else:
            machine.set(target,True)

    def fsm_action_assign(target, machine, from_load=False):
        if from_load:
            return
        if len(target) > 2:
            machine, field, value = target
        else:
            field, value = target
        if isinstance(machine, unicode) or isinstance(machine, str):
            machine = store.machines[machine]
        try:
            machine.set(field, eval(value))
        except TypeError:
            machine.set(field, value)

    def fsm_action_inc(target, machine, from_load=False):
        if from_load:
            return
        machine.increment(target,1)

    def fsm_action_dec(target, machine, from_load=False):
        if from_load:
            return
        machine.increment(target,-1)

    def fsm_action_triggeronzero(target, machine, from_load=False):
        if from_load:
            return
        machine.triggerOnZero(target[0],target[1])

    def fsm_action_trigger(target, machine, from_load=False):
        if from_load:
            return
        Machine.trigger(target)

    def fsm_action_call(target, machine, from_load=False):
        renpy.call(target)

    def fsm_action_location(target, machine, from_load=False):
        if isinstance(target, dict):
            machine.place(**target)
        elif len(target) == 2:
            m = target[0]
            if isinstance(m, unicode) or isinstance(m, str):
                m = store.machines[m]
            d = target[1]
            d["machine"] = machine
            m.place(**d)
        elif len(target) == 1:
            machine.place(**target[0])

    def fsm_action_force(target, machine, from_load=False):
        if isinstance(target, dict):
            machine.force(**target)
        elif len(target) == 2:
            m = target[0]
            if isinstance(m, unicode) or isinstance(m, str):
                m = store.machines[m]
            d = target[1]
            d["machine"] = machine
            m.force(**d)
        elif len(target) == 1:
            machine.force(**target[0])
        elif len(target) == 4:
            machine.force(flag=target)

    def fsm_action_unforce(target, machine, from_load=False):
        if target is None:
            machine.unforce()
        else:
            if isinstance(target, unicode) or isinstance(target, str):
                target = store.machines[target]
            target.unforce(machine)

    def fsm_action_exec(target, machine, from_load=False):
        if callable(target):
            target()
        elif isinstance(target, list):
            if callable(target[0]):
                callable(*target[1])
            else:
                raise FSMActionError("{} is not a callable object to exec in {}".format(target, machine._name))
        elif isinstance(target, str) or isinstance(target, unicode):
            eval(target)
        else:
            raise FSMActionError("{} is not a callable object to exec in {}".format(target, machine._name))

    def fsm_action_condition(target, machine, from_load=False):
        if eval(target[0]):
            actions = target[1]
            process_action_list(machine, actions, from_load)
        elif len(target) > 2:
            actions = target[2]
            process_action_list(machine, actions, from_load)

    def fsm_action_action(target, machine, from_load=False):
        m = target[0]
        if isinstance(m, str) or isinstance(m, unicode):
            m = store.machines[m]
        act = target[1]
        tgt = target[2]
        process_action(m, act, tgt, from_load)

    def fsm_action_setdefaultloc(data, machine, from_load=False):
        if isinstance(data, tuple):
            machine, data = data
        if isinstance(machine, basestring):
            machine = store.machines[machine]
        machine.set_default_locations(data)

    def fsm_action_setoutfit(target, machine, from_load=False):
        if from_load:
            return
        machine.outfit.bind_outfit_to_location(*target)

    def fsm_action_setnaked(target, machine, from_load=False):
        if from_load:
            return
        machine.outfit.is_naked = target

    def fsm_action_setdefaultoutfit(data, machine, from_load=False):
        if from_load:
            return
        if isinstance(data, tuple):
            machine, data = data
        if isinstance(machine, basestring):
            machine = store.machines[machine]
        machine.outfit.set_default_outfit_schedule(data)

    def fsm_action_setinshower(target, machine, from_load=False):
        if from_load:
            return
        global game
        if isinstance(target, unicode) or isinstance(target, str):
            target = store.machines[target]
        game._in_shower = target

    def fsm_action_setpriority(target, machine, from_load=False):
        if isinstance(target, list):
            m = target[0]
            if isinstance(m, str) or isinstance(m, unicode):
                m = store.machines[m]
            m.set_priority(target[1])
        else:
            machine.set_priority(target)

    def fsm_action_setcanleave(target, machine, from_load=False):
        if isinstance(target, Location):
            Location.set_can_leave(target)
        elif isinstance(target, list) or isinstance(target, tuple):
            Location.set_can_leave(*target)

    def fsm_action_setcannotleave(target, machine, from_load=False):
        if isinstance(target, Location):
            Location.set_cannot_leave(target)
        elif isinstance(target, list) or isinstance(target, tuple):
            Location.set_cannot_leave(*target)

    def fsm_action_forcemail(target, machine, from_load=False):
        if from_load:
            return
        mailbox = game.mail.get(machine._name)
        if mailbox is not None:
            mailbox.set(target)

    def fsm_action_setcantalk(target, machine, from_load=False):
        if isinstance(target, dict):
            for mname, tgt in target.items():
                store.machines[mname].set_can_talk_flags(tgt)
        else:
            machine.set_can_talk_flags(target)

    def fsm_action_cleanlocation(target, machine, from_load=False):
        if isinstance(target, (str, unicode)):
            target = store.machines[target]
        elif target is None:
            target = machine
        
        target._force_locations[machine._name] = [[None, None, None, None]]*7
        target._location_condition[machine._name] = None
        target._force_loc[machine._name] = [False, False, False, False]

    def process_action(machine, act, target, from_load=False):
        """
            ['set','flag_1']  set's the value of flag_1 to True
            ['clear','flag_1'] set's the value of flag_1 to False
            ['toggle','flag_1'] toggle's the value of flag_1 between True and False
            ['assign',['v1',100]] sets the value of v1 to 100
            ['inc','v1'] increase the value of v1 by 1
            ['dec','v1'] decrease the value of v1 by 1
            ['triggeronzero':['v1',T_a_trigger]] sets v1 -= 1 and if
                            v1 <= 0 it will fire the Trigger T_a_trigger
            ['trigger',T_a_trigger], fire the Trigger T_a_trigger
            ['call','label'], make a RenPy call to label. Label
                            MUST return
            ['location', [machine, {"tod":tod, "place":place}]], set the forced location for the
                            machine to place (Moves the NPC). tod is 1-indexed (1=morning, 4=night)
            ['force', [machine, {"tod": list or int, "flag": 4-list or bool}]]
                            Says if the location is forced at tod or sets force flags according to
                            the 4-list provided
            ['unforce', None/machine] unforce the locations for machine or the machine specified
            ['exec', callable], calls the callable (function or method)
            ['exec', [callable, *args]], calls the callable and pass in the args specified
                            forced.
            ['condition', [condition_string, actions_list_true, actions_list_false, (optional) machine]],
                            executes the actions in actions_list_true
                            if condition_string evaluates to True, otherwise executes actions_list_false.
            ['action', [target_machine, action, target]] Executes the action on another machine.
            ['setdefaultloc', [[Location, Location, Location, Location]]] Sets the default locations
                            for the current machine.
            ['setoutfit', [location, outfit]] Sets the outfit for that location. Outfit may be either a string,
                            or a 1x4,2x4,7x4 array of strings (similar to the locations)
            ['setnaked', True/False] Sets the is_naked attribute of the current machine's outfit
                            manager to True/False
            ['setdefaultoutfit', [outfit, {'tod':tod, 'dow':dow}]] Sets the current machine's default outfit.
                            tod and dow can be omitted. outfit is a required argument, can be a string
                            or a 1x4,2x4,7x4 matrix. If tod and dow are omitted, outfit cannot be a
                            matrix, but only a string. You can work around that by passing the
                            {"tod":None, "dow":None} dict.
            ['setinshower', machine/None] Sets the in_shower variable to None, or a given machine.
            ['priority', [machine, flag]] Sets the priority of the machine, to show or hide it in
                            the tips of the cellphone.
            ['setcanleave', location] See 'setcannotleave'
            ['setcannotleave', location] Sets the can_leave flag to False of target location.
                            Hides the exit button in most locations.
            ['unlocklocation', location] Unlocks target location. Does nothing if executed from a loading state.
            ['forcemail', mail_item] Forces that mail item for the next day.
            ['setcantalk', dict_or_list] Sets the can_talk flag for the machine.
                                        If a dict is provided, the key is excpected to be a machine name,
                                        and the values are supposed to be 4-lists
        """
        fsm_actions = {"set": fsm_action_set,
                       "clear": fsm_action_clear,
                       "toggle": fsm_action_toggle,
                       "assign": fsm_action_assign,
                       "inc": fsm_action_inc,
                       "dec": fsm_action_dec,
                       "triggeronzero": fsm_action_triggeronzero,
                       "trigger": fsm_action_trigger,
                       "call": fsm_action_call,
                       "location": fsm_action_location,
                       "force": fsm_action_force,
                       "unforce": fsm_action_unforce,
                       "exec": fsm_action_exec,
                       "condition": fsm_action_condition,
                       "action": fsm_action_action,
                       "setdefaultloc": fsm_action_setdefaultloc,
                       "setoutfit": fsm_action_setoutfit,
                       "setnaked": fsm_action_setnaked,
                       "setdefaultoutfit": fsm_action_setdefaultoutfit,
                       "setinshower": fsm_action_setinshower,
                       "priority": fsm_action_setpriority,
                       "setcannotleave": fsm_action_setcannotleave,
                       "setcanleave": fsm_action_setcanleave,
                       "locklocation": fsm_action_locklocation,
                       "unlocklocation": fsm_action_unlocklocation,
                       "forcemail": fsm_action_forcemail,
                       "setcantalk": fsm_action_setcantalk,
                       "cleanlocation": fsm_action_cleanlocation,
        }
        fsm_actions.update(ModManager.get_all_mods_fsm_actions())
        
        if from_load:
            logger.info("(FROM LOAD) Action {} executed on {} with target {}".format(act, machine._name, repr(target)))
        else:
            logger.info("Action {} executed on {} with target {}".format(act, machine._name, repr(target)))
        act = act.lower()
        action = fsm_actions.get(act)
        if action is None:
            raise FSMActionError("{} unknown action: {} on {}".format(machine._name, act,target))
        else:
            try:
                action(target, machine, from_load)
            except Exception as e:
                logger.error(str(machine.dump()))
                logger.error('  '.join((str(act), str(target))))
                raise e


    def process_action_list(machine, action_list, from_load=False):
        for i in xrange(0,len(action_list)-1,2):
            act = action_list[i].lower()
            target = action_list[i+1]
            process_action(machine, act, target, from_load)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
