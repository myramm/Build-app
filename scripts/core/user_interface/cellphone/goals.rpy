init python hide in phone:
    from store import phone as exports


    icons = {'angelica': 'cookie_jar_07',
             'anna': 'cookie_jar_19',
             'annie': 'cookie_jar_23',
             'anon': 'cookie_jar_35',
             'aqua': 'cookie_jar_12',
             'becca': 'cookie_jar_25',
             'bissette': 'cookie_jar_15',
             'cassie': 'cookie_jar_10',
             'consuela': 'cookie_jar_34',
             'crystal': 'cookie_jar_26',
             'debbie': 'cookie_jar_01',
             'dewitt': 'cookie_jar_16',
             'diane': 'cookie_jar_03',
             'erik': 'cookie_jar_31',
             'eve': 'cookie_jar_24',
             'grace': 'cookie_jar_32',
             'helen': 'cookie_jar_06',
             'ivy': 'cookie_jar_08',
             'iwanka': 'cookie_jar_39',
             'jane': 'cookie_jar_22',
             'jenny': 'cookie_jar_02',
             'josie': 'cookie_jar_37',
             'judith': 'cookie_jar_14',
             'june': 'cookie_jar_09',
             'katya': 'cookie_jar_45',
             'khadne': 'cookie_jar_46',
             'maria': 'cookie_jar_36',
             'melonia': 'cookie_jar_40',
             'mia': 'cookie_jar_05',
             'micoe': 'cookie_jar_27',
             'mrsj': 'cookie_jar_04',
             'nadya': 'cookie_jar_42',
             'odette': 'cookie_jar_33',
             'okita': 'cookie_jar_18',
             'priya': 'cookie_jar_29',
             'ross': 'cookie_jar_17',
             'roxxy': 'cookie_jar_20',
             'roz': 'cookie_jar_11',
             'svetlana': 'cookie_jar_47',
             'terry': 'cookie_jar_28',
             'tina': 'cookie_jar_38',
             'yoyo': 'cookie_jar_48'}


    def goals(machines):
        for n, m in sorted(machines.iteritems(), key=priority):
            if m.priority <= 0:
                continue
            
            s = m.get_state()
            
            if s is None:
                continue
            
            if s.is_end_state:
                continue
            
            hint = s.hint or _('No hints for this quest.')
            
            if s.delay > 0:
                hint = _('Maybe I should wait a few days...')
            
            yield icons.get(n.lower(), 'empty'), hint


    def priority(item):
        return (-item[1].priority, item[0])


    exports.goals = goals
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
