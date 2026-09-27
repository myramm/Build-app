default ward = {'L_hospital_recovery1': None,
                'L_hospital_recovery2': None,
                'L_hospital_recovery3': None,
                'L_hospital_recovery4': None}

init -5 python hide:















    consts = _dict()


    class PregnancyManager(object):
        def __init__(self, name, default_schedule={}, chance=0.4,
                     home_birth=False, can_birth_twins=True, copy=False):
            self.name = name
            self.debug_baby_gender = None
            self.init(copy, first_init=True)
            self.number_of_babies = 0
            self.location_schedule = {
                                    "":None,
                                    "_pregnant_bump":None,
                                    "_pregnant_belly":None,
                                    "_labor":None,
                                    "_baby_twins":None,
                                    "_baby_girl":None,
                                    "_baby_boy":None,
            }
            
            
            for v in default_schedule.values():
                if isinstance(v, LocationSchedule):
                    v.seed = hash(self.name)
            
            self.location_schedule.update(default_schedule)
            
            consts.setdefault(name, {
                'chance': chance,
                'twins': can_birth_twins,
                'birth': 'home' if home_birth else 'ward',
                'actions': {"first": [None] * 8, "repeat": [None] * 8}})
        
        @property
        def chance(self):
            return consts[self.name]['chance']
        
        @property
        def can_birth_twins(self):
            return consts[self.name]['twins']
        
        @property
        def home_birth(self):
            return consts[self.name]['birth'] == 'home'
        
        def init(self, copy=False, first_init=False):
            self.stage = 0
            self.days_elapsed = 0
            self.is_pregnant = False
            self.announced_pregnancy = False
            self.baby_gender = "boy"
            
            self.seen_in_labor = False
            self.seen_lady = False
            self.character_bedridden = False
            self.gave_birth = False
            
            self.text_announcement_seen = False
            self.text_labor_seen = False
            self.gave_birth_dialogue_seen = False
            
            if not copy and not first_init:
                prefix = '{}_pregnancy'.format(self.name)
                player.messages = [m for m in player.messages
                                     if not m.startswith(prefix)]
        
        def set(self, k, v=True):
            self.__dict__[k] = v
            self.serialize()
        
        def copy(self):
            p = PregnancyManager(self.name, default_schedule=self.location_schedule, copy=True)
            for key, value in self.__dict__.items():
                p.__dict__[key] = copy(value)
            return p
        
        def abort_baby(self):
            if self.is_pregnant:
                self.act(7)
            self.init()
        
        def serialize(self):
            global fsm_data
            name = self.name
            data = {"stage": self.stage,
                    "days_elapsed": self.days_elapsed,
                    "is_pregnant": self.is_pregnant,
                    "announced_pregnancy": self.announced_pregnancy,
                    "baby_gender": self.baby_gender,
                    "seen_in_labor": self.seen_in_labor,
                    "character_bedridden": self.character_bedridden,
                    "gave_birth": self.gave_birth,
                    "text_announcement_seen": self.text_announcement_seen,
                    "text_labor_seen": self.text_labor_seen,
                    "gave_birth_dialogue_seen": self.gave_birth_dialogue_seen,
                    "number_of_babies": self.number_of_babies}
            fsm_data.machine_data.setdefault(name, {})["pregnancy"] = copy(data)
        
        def deserialize(self, obj):
            for k, v in obj.items():
                if isinstance(v, Iterable):
                    self.__dict__[k] = copy(v)
                else:
                    self.__dict__[k] = v
        
        def add_action(self, key, index, actionslist):
            """
                Adds a stage action to that pregnancy manager.
                Args:

                key : either "first" or "repeat"
                index : the stage index for that action, in range 0..6 (inclusive)
                actionslist : a list of actions (same as FSM actions)
            """
            if not renpy.is_init_phase():
                return 
            if not 0 <= index <= 7:
                logger.warning("index not in range 0..6")
                return
            if key not in ("first", "repeat"):
                logger.warning("key must be either 'first' or 'repeat'")
                return
            if len(actionslist) % 2 != 0:
                logger.warning("actionslist is not of even length")
                return
            now = consts[self.name]['actions'][key]
            if now[index] is None:
                now[index] = actionslist
            else:
                now[index].extend(actionslist)
        
        @classmethod
        def increment_pregnancy(cls):
            for mname, m in store.machines.items():
                pm = m.pregnancy
                pm._increment_pregnancy()
        
        def _increment_pregnancy(self):
            global player
            if self.is_pregnant:
                self.days_elapsed += 1
                if self.character_bedridden and self.days_elapsed == 38:
                    ward[self.character_bedridden] = None
                    self.character_bedridden = False
                
                if self.days_elapsed % 7 == 0:
                    self.stage += 1
                    self.act(self.stage)
                    if self.stage > 6:
                        self._increment_babies()
                        self.init()
                if self.days_elapsed == 7:
                    if self.first_baby and "{}_pregnancy_first".format(self.name) in phone.data:
                        player.receive_message("{}_pregnancy_first".format(self.name))
                    elif "{}_pregnancy".format(self.name) in phone.data:
                        player.receive_message("{}_pregnancy".format(self.name))
                if self.days_elapsed == 35:
                    if not self.home_birth:
                        room = next(k for k, v in sorted(
                            ward.items(),
                            key=lambda x: x[1] and ~machines[x[1]].pregnancy.days_elapsed))
                        occupant = ward[room]
                        if occupant is not None:
                            machines[occupant].pregnancy.set('character_bedridden', False)
                        
                        ward[room] = self.name
                        self.character_bedridden = room
                    
                    self.gave_birth = True
                    
                    player.receive_message("{}_pregnancy_labor".format(self.name))
            self.serialize()
        
        def _increment_stage(self):
            for i in xrange(7):
                self._increment_pregnancy()
        
        def _increment_babies(self):
            self.number_of_babies += 1
            if self.baby_gender == "twins":
                self.number_of_babies += 1
        
        @classmethod
        def total_babies(cls):
            return sum([m.pregnancy.number_of_babies for m in store.machines.values()])
        
        def set_debug_baby_gender(self, gender):
            self.debug_baby_gender = gender if gender in ("boy", "girl", "twins", None) else None
        
        def randomize_gender(self):
            if self.debug_baby_gender is not None:
                self.baby_gender = self.debug_baby_gender
                return
            pool = ('boy', 'girl') * 10
            if self.can_birth_twins:
                pool += ('twins',)
            self.baby_gender = random.choice(pool)
        
        def get_pregnant(self):
            self.init()
            self.randomize_gender()
            self.is_pregnant = True
        
        def __str__(self):
            stage = self.stage
            if stage > 4:
                stage = 0
            return ["", "", "_pregnant_bump", "_pregnant_belly", "_pregnant_belly"][stage]
        
        def __bool__(self):
            return self.is_pregnant and self.stage > 0
        
        def __nonzero__(self):
            return self.__bool__()
        
        @property
        def to_string(self):
            return self.__str__()
        
        @property
        def to_belly_string(self):
            if 3 <= self.stage <= 4:
                return '_pregnant_belly'
            return ''
        
        @property
        def to_full_string(self):
            if self.stage <= 4:
                return self.__str__()
            else:
                return "_baby_" + self.baby_gender
        
        @property
        def apparent_stage(self):
            if self.stage in (3,4):
                return 3
            else:
                return self.stage
        
        @property
        def first_baby(self):
            return self.number_of_babies == 0 and self.is_pregnant
        
        @property
        def had_baby(self):
            return self.number_of_babies > 0
        
        @property
        def show_baby_intro(self):
            return (self.first_baby and
                    self.gave_birth and
                    not self.character_bedridden and
                    not self.gave_birth_dialogue_seen)
        
        @property
        def where(self):
            if self.character_bedridden:
                return locations[self.character_bedridden]
            if '_announce' in self.location_schedule and not self.announced_pregnancy:
                loc_schedule = self.location_schedule['_announce']
            else:
                loc_schedule = self.location_schedule.get(self.to_full_string, None)
            if isinstance(loc_schedule, LocationSchedule):
                return loc_schedule.get
            return None
        
        def act(self, stage):
            key = 'first' if self.first_baby else 'repeat'
            actions = consts[self.name]['actions'][key][stage]
            machine = store.machines.get(self.name, None)
            if actions and machine:
                for fn, args in zip(*(iter(actions),) * 2):
                    process_action(machine, fn, args)


    store.PregnancyManager = PregnancyManager
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
