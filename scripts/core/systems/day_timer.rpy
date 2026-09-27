init python:
    LUNARDAY = 0.03386319269

    class Date:
        weekdays = (
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            )
        timeofdays = (
            'morning',
            'afternoon',
            'evening',
            'night',
        )
        weekdays_short = (
            "mon",
            "tue",
            "wed",
            "thu",
            "fri",
            "sat",
            "sun",
        )
        def __init__(self, tod=None, dow=None):
            if isinstance(tod, int):
                self.tod = tod
            elif isinstance(tod, str) or isinstance(tod, unicode):
                self.tod = self.timeofdays.index(tod.lower())
            elif tod is None:
                self.tod = None
            else:
                self.tod = None
            
            if isinstance(dow, int):
                self.dow = dow
            elif isinstance(dow, str) or isinstance(dow, unicode):
                self.dow = self.weekdays.index(dow.lower())
            elif dow is None:
                self.dow = None
            else:
                self.dow = None
            if self.dow is not None:
                self.weekday = self.weekdays[self.dow]
                self.weekday_short = self.weekdays_short[self.dow]
            else:
                self.weekday = ""
                self.weekday_short = ""
            if self.tod is not None:
                self.timeofday = self.timeofdays[self.tod]
            else:
                self.timeofday = ""
        
        def format(self):
            return {"tod":self.timeofday.capitalize(),
                    "dow":self.weekday.capitalize(),
                    "dow_short":self.weekday_short.capitalize(),
                    }
        
        def __eq__(self, date):
            if date.tod is None and date.dow is None:
                return True
            elif date.tod is not None and date.dow is None:
                return self.tod == date.tod
            elif date.tod is None and date.dow is not None:
                return self.dow == date.dow
            else:
                return self.dow == date.dow and self.tod == date.tod
        
        def advance(self):
            tod = self.tod + 1
            if tod < 4:
                return Date(tod, self.dow)
            else:
                dow = self.dow + 1
                if dow < 7:
                    return Date(0, dow)
                else:
                    return Date(0, 0)

    class DayTimer:
        _tod = 0
        _dow = 0
        _game_day = 0
        weekdays = (
            'Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun',
            )
        weekdays_long = (
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday',
            )
        scheduled_tasks_on_sleep = []
        
        def __init__(self):
            self._seed = random.random()
        
        def __getstate__(self):
            return {'gameday': self._game_day,
                    'seed': self._seed,
                    'tod': self._tod}
        
        def __setstate__(self, state):
            self._game_day = state["gameday"]
            self._seed = state.get('seed', None) or random.random()
            self._tod = state["tod"]
            self._dow = self._game_day % 7
        
        def __eq__(self, date):
            if date.tod is None and date.dow is None:
                return True
            elif date.tod is not None and date.dow is None:
                return self._tod == date.tod
            elif date.tod is None and date.dow is not None:
                return self._dow == date.dow
            else:
                return self._dow == date.dow and self._tod == date.tod
        
        def is_morning(self):
            return self._tod == 0
        
        def is_afternoon(self):
            return self._tod == 1
        
        def is_evening(self):
            return self._tod == 2
        
        def is_night(self):
            return self._tod == 3
        
        def is_dark(self):
            return self._tod >= 2
        
        def is_day(self):
            return not self.is_dark()
        
        def is_tick(self, *ticks):
            return self._tod in ticks
        
        def is_dow(self, *dows):
            return self._dow in dows
        
        def is_date(self, **kwargs):
            '''
                Method is_date of DayTimer object

                :param kwarg 'tod': a time of day to compare to.(integer) Cast into an iterable internally
                :param kwarg 'dow': a day of week to compare to (integer)
                :param kwarg 'date': a specific date to compare to (Date object)

                :returns: boolean True/False if the current date matches the tod/dow/date specified
                :raises: SummertimeSagaException if no kwarg are provided
                :raises: ValueError if time of days or days of week can't be casted into integers.
            '''
            tod = kwargs.get("tod", None)
            dow = kwargs.get("dow", None)
            date = kwargs.get("date", None)
            current_date = Date(tod=self._tod, dow=self._dow)
            if not isinstance(tod, Iterable) and tod is not None:
                tod = [tod]
            if not isinstance(dow, Iterable) and dow is not None:
                dow = [dow]
            
            if tod is not None:
                tod = [int(t) for t in tod]
            
            if dow is not None:
                dow = [int(d) for d in dow]
            
            if date:
                return current_date == date
            elif tod is not None and dow is not None:
                return current_date in [Date(tod=t, dow=d) for t in tod for d in dow]
            elif tod is not None and dow is None:
                return self.is_tick(*tod)
            elif tod is None and dow is not None:
                return self.is_dow(*dow)
            else:
                raise SummertimeSagaException("Method 'is_date' of DayTimer object needs one of the following kwargs: ('tod', 'dow', 'date')")
        
        def _image(self, name, layer="master"):
            if self.is_dark():
                name = ".".join(name.rsplit("_day.", 1))
                name = "_".join(name.rsplit("_day_", 1))
                name = "{}".join(name.rsplit("_day{}", 1))
                if self.is_evening():
                    tmp = name.format("_evening")
                    if Game.can_show(tmp, layer):
                        return tmp, False
                tmp = name.format("_night")
                if Game.can_show(tmp, layer):
                    return tmp, False
                tmp = name.format("_day")
                if Game.can_show(tmp, layer):
                    return tmp, False
            else:
                if Game.can_show(name, layer):
                    return name, False
                tmp = name.format("_day")
                if Game.can_show(tmp, layer):
                    return tmp, False
            return name.format(""), True
        
        def image(self, name, addendum="", layer = "master"):
            splits = name.split(".")
            extension = ""
            if len(splits) >= 2:
                extension = "."+splits[-1]
            name = splits[0]
            formatting = "{}" in name and name.split("{}")[1]
            after_formatting = ""
            if formatting:
                after_formatting = name.split("{}")[1]
                name = name.split("{}")[0]
            name2 = name
            if not re.search('\{}', name):
                name = name + '{}'
                extension = extension or ".jpg"
            if Game.is_christmas():
                name2 = name.format("_christmas")
            elif Game.is_halloween():
                name2 = name.format("_halloween")
            else:
                name2 = name.format("")
            name2 = name2 + addendum + "{}" + after_formatting
            name = name.format(addendum) + "{}" + after_formatting
            if len(splits) >= 2:
                name2 += extension
                name += extension
            formatted, default = self._image(name2, layer)
            if default:
                formatted, other_default = self._image(name, layer)
                return formatted
            else:
                return formatted
        
        
        def is_weekend(self):
            return self.is_dow(5, 6)
        
        def is_weekday(self):
            return not self.is_weekend()
        
        def is_fullmoon(self):
            return 0.5 <= self.lunation < 0.5 + (3 * LUNARDAY)
        
        def days_since_lunar(self, target):
            return int((self.lunation - target) % 1 / LUNARDAY)
        
        def days_until_lunar(self, target):
            return int(math.ceil((target - self.lunation) % 1 / LUNARDAY))
        
        @property
        def lunation(self):
            if Game.is_halloween():
                return .5
            return (self._seed + self._game_day * LUNARDAY) % 1
        
        def dayOfWeek(self, delta=0, full=False):
            if full:
                return self.weekdays_long[(self._dow + delta) % 7]
            else:
                return self.weekdays[(self._dow + delta) % 7]
        
        def game_day(self):
            return self._game_day
        
        def tick(self, tod=None):
            if tod is None:
                tod = self._tod + 1
            
            if not 0 <= tod <= 3:
                return
            
            renpy.block_rollback()
            
            self._tod = tod
            
            game.telescope.randomize(self)
            Machine.trigger(T_all_tick)
            Machine.machine_trigger(T_all_tick)
        
        def sleep(self):
            renpy.block_rollback()
            self._tod = 0
            self._dow = (self._dow +1) % 7
            self._game_day += 1
            game.telescope.randomize(self)
            for i in xrange(len(self.scheduled_tasks_on_sleep)):
                scheduled_task, args, kwargs = self.scheduled_tasks_on_sleep.pop()
                scheduled_task(*args, **kwargs)
        
        def schedule_on_sleep(self, function, args=[], kwargs={}):
            self.scheduled_tasks_on_sleep.append((function, args, kwargs))
        
        def skip_forward(self, nb_days):
            global game
            for n in xrange(nb_days):
                game.sleep()
        
        def set_time(self, tod=None, dow=None):
            if tod is not None:
                self._tod = tod
            if dow is not None:
                self._dow = dow
        
        def __repr__(self):
            t = ['morning', 'afternoon', 'evening', 'night'][self._tod]
            return '{} {}, day {}'.format(
                self.dayOfWeek(full=True), t, self._game_day)
        
        @property
        def now(self):
            return self._game_day * 4 + self._tod
        
        def random(self, key, tick=False):
            seed = self._game_day
            if tick:
                seed *= 4
                seed += self._tod
            seed += self._seed
            seed -= sum(ord(c) for c in key)
            return random.Random(seed).random()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
