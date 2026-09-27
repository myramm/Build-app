default location_seed = random.randint(0, sys.maxint)

init -4 python:

    class LocationSounds(object):
        def __init__(self, loc):
            self.loc = loc
            self.cache = {}
        
        def get(key):
            if key not in self.cache:
                default = location_sounds['default'][key]
                self.cache[key] = cfg.get(self.loc.ref, {}).get(key, default)
            return self.cache[key]
        
        @property
        def ambiance(self):
            if game.timer.is_day():
                return SoundManager.get_sound_path(self.get('ambience'))
            else:
                return SoundManager.get_sound_path(self.get('ambience_night'))
        
        def play_music(self):
            if self.ambiance:
                SoundManager.play_music(self.get('ambience'))


    class LocationSchedule(): 
        def __init__(self, schedule=None):
            
            if schedule is None or isinstance(schedule, Location):
                schedule = [[schedule]*4]*7
            
            
            for dow, vdow in enumerate(schedule):
                for tod, vtod in enumerate(vdow):
                    if vtod is None:
                        schedule[dow][tod] = L_NULL
            
            self.seed = 0
            self.set_schedule(schedule)
        
        def set_schedule(self, schedule):
            """
            @method set_schedule := None
            ----
            Sets the schedule attribute of this LocationSchedule, and format it into a 4x7 matrix of locations.
            ----
            Args :
                - schedule
                    A 4x1, 4x2 or 4x7 matrix of Location instances.
                    4x1 matrices will be replicated 7 times (one for each day of the week)
                    4x2 matrices will be replicated 5 and 2 times (weekdays and weekends)
                    4x7 matrices will not be replicated.
            """
            if len(schedule) == 1:
                self.schedule = [schedule[0]]*7
            elif len(schedule) == 2:
                self.schedule = [schedule[0]]*5
                self.schedule.extend([schedule[1]]*2)
            elif len(schedule) == 7:
                self.schedule = schedule
            else:
                raise SummertimeSagaInitException("location attribute must be a matrix of 1x4, 2x4 or 7x4")
        
        @property
        def get(self):
            """
                @property get := Location
                ----
                Gets the location for that schedule based on the time of day and the day of the week.
            """
            global game
            rv = self.schedule[game.timer._dow][game.timer._tod]
            if isinstance(rv, Iterable):
                
                random.seed(self.seed + location_seed + game.timer._game_day * 4 + game.timer._tod)
                rv = random.choice(rv)
                random.seed()
            return rv


    class LocationData(object):
        @classmethod
        def new_location_data(cls):
            ld = LocationData()
            ld.visited_locations = [store.locations.values()]
            return ld
        
        def __init__(self):
            self.locked_locations = []
            self.visited_locations = []
        
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
        
        
        def dump(self):
            rv = "LOCKED: {}\nVISITED: {}".format(", ".join(self.locked_locations), ", ".join(self.visited_locations))
            logger.info(rv)


    class Location(object):
        """
            Location : A Location object represents the locations in the game as a tree.

            You can access any parent or child of a given location.
        """
        roots = []
        future_location = None
        
        def __init__(self, name="", background="ground", parents=[], locked=False, label="", background_fn=None, is_door=False, ref=None):
            self.name = name
            self.ref = ref or self.formatted_name
            self._locked = locked
            if isinstance(parents, Location):
                self.parents = [parents]
            else:
                self.parents = parents
            self.children = [] 
            if not self.is_root:
                for parent in self.parents:
                    parent.children.append(self) 
            self._background = background
            self.temporary_locked = False
            self._label = label
            self.can_leave = True
            if self.is_root:
                Location.roots.append(self)
            self._display_name = None
            if background_fn is None:
                self.background_fn = default_bg_fn
            else:
                self.background_fn = background_fn
            self.is_door = is_door
            self.sounds = LocationSounds(self)
        
        def __repr__(self):
            return '<{}.{} \'{}\'>'.format(self.__class__.__module__,
                                           self.__class__.__name__,
                                           self.name)
        
        def __str__(self):
            return self.ref or self.name.replace(" ", "_").strip("'").lower()
        
        def __eq__(self, other):
            try:
                return self.ref == other.ref
            except AttributeError:
                return True
        
        def copy(self):
            l = Location(self.name)
            for key, value in self.__dict__.items():
                if key not in ("parents", "children"):
                    l.__dict__[key] = copy(value)
            return l
        
        @classmethod
        def set_future_location(cls, location=None):
            cls.future_location = location
        
        @classmethod
        def get_first_children(cls):
            children = []
            for root in cls.roots:
                children.extend(root.children)
            children.extend(cls.roots)
            return children
        
        @classmethod
        def set_cannot_leave(cls, *locations):
            for loc in locations:
                loc.can_leave = False
        
        @classmethod
        def set_can_leave(cls, *locations):
            for loc in locations:
                loc.can_leave = True
        
        @property
        def _bg(self):
            if callable(self._background):
                return self._background()
            return self._background
        
        @property
        def formatted_name(self):
            name = self.name
            name = name.lower()
            name = name.replace("'", "")
            name = name.replace(" ", "_")
            return name
        
        @property
        def label(self):
            if self._label:
                return self._label
            else:
                return self.ref + "_dialogue"
        
        def _set_display_name(self, name):
            self._display_name = name
        
        def _get_display_name(self):
            if self._display_name is None:
                return self.name
            else:
                return self._display_name
        display_name = property(_get_display_name, _set_display_name)
        
        def call(self):
            """
                Method to call the correct location label

                The label name is supposed to be all lowercase,
                no ' characters (Mia's replaced with mias),
                spaces replaced by _ and ending in _dialogue.
            """
            renpy.call(self.label)
            pass
        
        def call_screen(self, ui=True, clear=True, new_context=False):
            """
                Method to call the screen associated with the location.
                Usually called from the player's location attribute
                    $ game.main()

                Arguments :
                    ui : defaults to True, whether the ui should be shown on the screen
                    clear : defaults to True : hide all images before calling the new screen
                    new_context : defaults to False : calls the screen in a new context.
            """
            renpy.hide_screen("ui")
            if new_context:
                renpy.call("new_context_screen", interface = ui, images = clear)
            if clear:
                for visible_image in renpy.get_showing_tags():
                    renpy.hide(visible_image)
            name = self.ref
            if game.timer.is_night() and self.ref in ["lair"]:
                name = "town_map"
                ui = True
            if ui:
                renpy.show_screen(name)
                renpy.call_screen("ui")
            else:
                renpy.call_screen(name)
            pass
        
        def hide_screen(self):
            """
                Hides the screens associated with that location.
            """
            renpy.hide_screen("ui")
            try:
                renpy.hide_screen(self.ref)
            
            except Exception as e:
                pass
            pass
        
        @property
        def sisters(self):
            """
                Property method that returns all the siblings of this Location node.

                Returns : list of all siblings of this location (Location instances)
            """
            sister_nodes = []
            for parent in self.parents:
                sis = copy(parent.children)
                sis.remove(self)
                sister_nodes.extend(sis)
            return sister_nodes
        
        def get_background(self, attr=0):
            if self._bg == "ground":
                return "ground.png"
            formatter = "location_{}".format(self._bg) + "{}{}{}"
            period = ("", "_christmas", "_halloween")[Game.period_index()]
            time = ("_morning", "_afternoon", "_evening", "_night")[game.timer._tod]
            daynight = ("_day", "_night")[1 if game.timer.is_dark() else 0]
            attr = ("", "_blur", "_closeup")[attr]
            args = ((period, time, attr),
                    (period, daynight, attr),
                    (period, '_any', attr),
                    ("", time, attr),
                    ("", daynight, attr),
                    ("", '_any', attr))
            for arg in args:
                newbg = formatter.format(*arg)
                if Game.can_show(newbg):
                    return newbg
        
        @property
        def background_path(self):
            """
                Property method to return the background of
                the location depending on time of day.
            """
            if self.name != "Town Map":
                rv = self.background_fn(blur=False)
                if rv is None:
                    if self._bg == "ground":
                        return "ground.png"
                    return game.timer.image("backgrounds/location_"+self._bg+"{}.jpg")
                else:
                    return rv
            else:
                return game.timer.image("map/map_base{}.jpg")
        
        @property
        def background(self):
            if self.ref != "town_map":
                rv = self.background_fn(blur=False)
                if rv is None:
                    return background(b=False, l=self)
                else:
                    return rv
            else:
                return game.timer.image("map_base{}")
        
        @property
        def background_blur(self):
            if self.ref != "town_map":
                rv = self.background_fn(blur=True)
                if rv is None:
                    rv = self.get_background(attr=1)
                    if rv is None:
                        rv = background(l=self)
                return rv
            else:
                return game.timer.image("map_base{}_blur")
        
        @property
        def background_closeup(self):
            if self.ref != "town_map":
                rv = self.get_background(attr=2)
                if rv is None:
                    rv = self.background_blur
                return rv
            else:
                return game.timer.image("map_base{}_blur")
        
        def get_background_path(self, addendum=""):
            if self.name != "Town Map":
                return game.timer.image("backgrounds/location_"+self._bg+"{}.jpg", addendum)
            else:
                return game.timer.image("map/map_base{}.jpg", addendum)
        
        def is_child_of(self, location):
            return self in location.get_all_children()
        
        def walk(self):
            """
                Generator method to walk down all the edges of this node one hierarchy.

                Use the syntax :
                    for child in location.walk():
                        #Code
            """
            for child in self.children:
                yield child
        
        def path_to(self, destination, maxcount=-1):
            """
                COMPLETELY NOT WORKING

                Should return a list of all the locations to go through to get to destination from self.

                Untested, so not sure that it works...
            """
            path = []
            node = self
            counter = 0
            while node != destination and (counter < maxcount or maxcount < 0):
                for child in node.can_go_to(check_locked=False):
                    if destination in child.get_all_children():
                        path.append(child)
                        node = child
                    elif node == destination:
                        path.append(destination)
                        break
                counter += 1
            return set(path)
        
        def can_go_to(self, check_locked=True):
            """
                Returns a list of all the nodes accessible from this node.
                Indexes are -1 for the root, -2 for the parent, the rest is children of the node.
            """
            rv = []
            for child in self.children:
                if not child.locked or not check_locked:
                    rv.append(child)
            for parent in self.parents:
                if not parent.locked or not check_locked:
                    rv.append(parent)
            return rv
        
        def get_all_children(self):
            """
                Method to return all the children of this location, recursively.

                Returns a list of all the children of this location.
            """
            to_return = []
            for child in self.children:
                if child not in to_return:
                    to_return.append(child)
                    to_return.extend(child.get_all_children())
            return to_return
        
        def get_all_children_inclusive(self):
            """
                Method to return all the children of this location, recursively, including
                this location.

                Returns a list of all the children of this location and this location.
            """
            
            rv = self.get_all_children()
            rv.append(self)
            return rv
        
        @property
        def is_leaf(self):
            """Returns wether this Location has children or not."""
            return len(self.children) == 0 
        
        @property
        def is_root(self):
            """Returns wether this node is a root or not"""
            return len(self.parents) == 0
        
        def get_root(self):
            """
                Gets the root node of this tree.
            """
            try:
                p = self
                while not p.is_root:
                    p = p.parents[0]
            except TypeError:
                pass
            return p
        
        @property
        def is_first_child(self):
            return True in [p.is_root for p in self.parents]
        
        
        def lock_all_children_but(self, location):
            """
                Locks all the children of this location but the location provided.
            """
            for child in self.children:
                child.locked = True
            location.locked = False
            pass
        
        def unlock_all_children(self):
            """
                Unlocks all the children of the location.
            """
            for child in self.children:
                child.locked = False
            pass
        
        def lock(self, lock_children=False):
            """
                Locks this location and if lock_children is True,
                also locks all its children recursively.
            """
            self.locked = True
            if lock_children:
                for child in self.children:
                    if not self.is_leaf:
                        child.lock(lock_children=True)
            pass
        
        def is_here(self, *machines):
            """
                Method to return whether the provided machine is in this location.
            """
            return [m.where for m in machines] == [self]*len(machines)
        
        def is_in_children(self, *machines):
            rv = []
            for loc in self.get_all_children_inclusive():
                if loc.is_here(*machines):
                    rv.append(1)
                else:
                    rv.append(0)
            return 1 in rv
        
        def miniature(self, adjust_timer=True):
            """
                Method that returns the miniature version of a location for the town map and unlock
                popups.

                1 argument : adjust_timer - whether the result should be adjusted by the in-game
                timer or not. boolean True/False

                returns : string formatted with the formatted_name property of that location.
            """
            if self.is_first_child:
                if adjust_timer:
                    return game.timer.image("map/"+self.ref+"01{}.png")
                else:
                    return "map/"+self.ref+"01.png"
            else:
                return None
        
        @property
        def first_visit(self):
            global location_data
            return self.ref not in location_data.visited_locations
        
        @first_visit.setter
        def first_visit(self, value):
            global location_data
            if value:
                if self.ref in location_data.visited_locations:
                    location_data.visited_locations.remove(self.ref)
            else:
                if self.ref not in location_data.visited_locations:
                    location_data.visited_locations.append(self.ref)
        
        @property
        def locked(self):
            global location_data
            return self.ref in location_data.locked_locations
        
        @locked.setter
        def locked(self, value):
            global location_data
            if value:
                if self.ref not in location_data.locked_locations:
                    location_data.locked_locations.append(self.ref)
            else:
                if self.ref in location_data.locked_locations:
                    location_data.locked_locations.remove(self.ref)
        
        def visited(self):
            self.first_visit = False
        
        def unvisit(self):
            self.first_visit = True
        
        @property
        def is_visited(self):
            return not self.first_visit
        
        def unlock(self, unlock_children=False, show_unlock_popup=True):
            """
                Unlocks this location.
                Location.unlock([unlock_children=False, show_unlock_popup=True)
                --------------
                Args:
                unlock_children : Whether the children of this location should be also unlocked (recursively)
                show_unlock_popup : shows this location's unlock popup (boolean)
            """
            if unlock_children:
                for child in self.children:
                    if not self.is_leaf:
                        child.unlock(unlock_children=True)
            if self.locked:
                self.locked = False
                if show_unlock_popup and self.is_first_child:
                    renpy.call_in_new_context('popup', 'location', self)
        
        @property
        def background_phone(self):
            if self == L_home_bedroom:
                rv = background(560, 320, 2.5, l=self)
            elif self == L_beachhouse_bedroom:
                rv = background(560, 420, 2.5, l=self)
            elif self in (L_home_mombedroom, L_home_sisbedroom):
                rv = background(360, 384, 1.5, l=self)
            elif self == L_tattooparlor:
                rv = background(120, 496, 4.5, l=self)
            elif self == L_church_graveyard:
                rv = background(768, 456, 3, l=self)
            else:
                rv = background(l=self)
            
            return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
