init -6 python:
    class OutfitManager(object):
        def __init__(self, owner, default_outfit="dressed", is_naked=False, outfits={}):
            self.owner = owner
            self.default_outfit = self.format_outfit_schedule(default_outfit)
            self.outfits = outfits
            self._is_naked = is_naked
            self.name = owner._name
        
        @property
        def is_naked(self):
            return self.get == 'naked'
        
        @is_naked.setter
        def is_naked(self, value):
            self._is_naked = bool(value)
            if not renpy.is_init_phase():
                self.serialize()
        
        def deserialize(self, obj):
            for k, v in obj.items():
                self.__dict__[k] = v
            pass
        
        def set_default_outfit_schedule(self, outfit, tod=None, dow=None):
            if outfit is None:
                raise SummertimeSagaException("No outfit provided")
            if tod is None and dow is None:
                rs = False
                if not is_string(outfit) and not isinstance(outfit, list):
                    rs = True
                if (isinstance(outfit, list) and len(outfit) not in (1,2,7)):
                    rs = True
                if rs:
                    raise SummertimeSagaException("Outfit provided is not a list or string, or that list is not of length 1,2 or 7")
                self.default_outfit = self.format_outfit_schedule(outfit)
            elif tod is None and dow is not None:
                self.default_outfit.pop(dow)
                self.default_outfit.insert(dow, outfit)
            elif tod is not None and dow is None:
                rv = []
                for v in self.default_outfit:
                    v[tod] = outfit
                    rv.append(v)
                self.default_outfit = rv
            elif tod is not None and dow is not None:
                self.default_outfit[dow][tod] = outfit
            
            if renpy.is_init_phase():
                self.owner.init_args['default_outfit'] = copy(self.default_outfit)
            else:
                self.serialize()
        
        
        def bind_outfit_to_location(self, location, outfit):
            if isinstance(location, Location):
                self.outfits[location.formatted_name] = self.format_outfit_schedule(outfit)
            else:
                raise SummertimeSagaInitException("Error in bind_outfit_to_location, location attribute is not of type 'Location'")
            
            if renpy.is_init_phase():
                self.owner.init_args['outfits'] = copy(self.outfits)
            else:
                self.serialize()
        
        def format_outfit_schedule(self, outfit_schedule):
            if isinstance(outfit_schedule, str) or isinstance(outfit_schedule, unicode):
                return [[outfit_schedule]*4]*7
            else:
                if len(outfit_schedule) == 1:
                    return [outfit_schedule[0]]*7
                elif len(outfit_schedule) == 2:
                    rv = [outfit_schedule[0]]*5
                    rv.extend([outfit_schedule[1]]*2)
                    return rv
                elif len(outfit_schedule) == 7:
                    return deepcopy(outfit_schedule)
                else:
                    raise SummertimeSagaInitException("Outfit Schedule attribute must be a matrix of 1x4, 2x4 or 7x4")
        
        def serialize(self):
            global fsm_data
            name = self.name.lower()
            data = {"_is_naked":self._is_naked,
                    "outfits": self.outfits,
                    "default_outfit": self.default_outfit,
            }
            fsm_data.machine_data[name]["outfit"] = copy(data)
        
        def deserialize(self, obj):
            for k, v in obj.items():
                self.__dict__[k] = v
        
        def copy(self):
            o = OutfitManager(self.owner, self.default_outfit, self.is_naked)
            for key, value in self.__dict__.items():
                o.__dict__[key] = copy(value)
            return o
        
        @property
        def get(self):
            if self._is_naked:
                return 'naked'
            try:
                outfit = self.outfits[player.location.formatted_name]
                return outfit[game.timer._dow][game.timer._tod]
            except KeyError:
                return self.default_outfit[game.timer._dow][game.timer._tod]
        
        def __str__(self):
            return self.get
        
        def is_wearing(self, outfit):
            return (outfit.lower() == self.get.lower())
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
