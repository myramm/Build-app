init -10 python:
    def orphaned_states():
        s_notin_m = []
        for st in store.states:
            s_notin_m.append(store.states[st])
        for m in store.machines:
            for s in store.machines[m]._states:
                if s in s_notin_m:
                    s_notin_m.remove(s)
        if s_notin_m:
            raise OrphanedStateException("Orphaned States: {}".format(s_notin_m))

    def instantiate_machines():
        store.machines = {}
        store.triggers = {}
        store.states = {}
        for varname, var in globals().items():
            if varname.startswith("M_"):
                store.machines[var._name] = var
            if varname.startswith("T_"):
                store.triggers[var._name] = var
            if varname.startswith("S_"):
                store.states[var._name] = var
        return

    def pregnant_machines():
        return [machine for mname, machine in store.machines.items() if machine.pregnancy]

    def check_misnamed_triggers():
        rv = []
        for tname, t in [(k, v) for k, v in globals().items() if k.startswith("T_")]:
            if "default" == tname:
                rv.append(t)
        if rv:
            tnames = []
            for k, v in globals().items():
                if v in rv:
                    tnames.append(k)
            raise MisnamedTriggerException("Misnamed trigger found. Triggers: {}.Do any of them are instantiated later than init -3?".format(tnames))

    def machines_label_check(prt=False):
        wrong_labels = []
        dont_care = ('anon', 'frank', 'player')
        for mname, m in store.machines.items():
            if not renpy.has_label(m.button_dialogue) and mname not in dont_care:
                wrong_labels.append(m.button_dialogue)
        padded = sorted(wrong_labels)
        padded.extend([""] * (len(wrong_labels) % 4))
        if wrong_labels:
            if prt:
                print("DEBUG : MACHINE LABELS NAMES CHECK :")
            else:
                logger.debug("MACHINE LABELS NAMES CHECK :")
        for i in xrange(0, len(padded), 4):
            if prt:
                print("DEBUG : " + ", ".join(padded[i:i+4]))
            else:
                logger.debug(", ".join(padded[i:i+4]))
        return wrong_labels
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
